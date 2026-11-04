"""A minimal OpenAI-compatible chat client with a model fallback chain.

Configuration (environment variables, or the project's .env):

    LLM_BASE_URL          default http://localhost:20128/v1 (OmniRoute)
    LLM_API_KEY           optional; sent as a Bearer token when set
    LLM_MODEL             the model to use; the layer is OFF until this is set
    LLM_FALLBACK_MODELS   optional, comma-separated, tried in order on failure
    LLM_CRITIC_MODEL      optional; a different model for checking work
    LLM_TIMEOUT_SECONDS   default 60

"Off" is a normal state: every feature built on this layer has a non-AI
fallback, so an unset LLM_MODEL means those features quietly use it.

Written on httpx (already installed with google-genai) rather than the openai
package, so the project gains no new dependency.

USAGE LOG (2026-10-03): every model call, answered or failed, is reported to a
sink (set_usage_sink) with its model, tokens, latency and tags. The tags come
from `usage_context(feature=..., student_id=...)`, a context variable, so
callers label their calls without any signature changing. The boundary
connects the sink to the database; this module stays free of storage code,
and a failing sink never breaks a call.
"""

from __future__ import annotations

import contextvars
import json
import os
import time
from contextlib import contextmanager
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Iterator

import httpx

_PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_BASE_URL = "http://localhost:20128/v1"


class LLMError(RuntimeError):
    """The model couldn't be reached or gave no usable answer."""


@dataclass
class ChatResult:
    text: str
    tool_calls: list[dict[str, Any]] = field(default_factory=list)  # [{id, name, args}]
    message: dict[str, Any] = field(default_factory=dict)  # the assistant message, for replay
    model: str = ""


def _env(name: str, default: str | None = None) -> str | None:
    """The environment first, then the project's .env.

    A variable that is SET in the environment wins even when it is empty:
    `LLM_MODEL=` means "off", which is how tests and the load test switch the
    AI off without editing .env (the load test found an empty value falling
    through to .env and calling a real provider). The .env file is parsed once
    per version (src/file_cache.py), so a key added while the server runs is
    still picked up without a restart.
    """
    if name in os.environ:
        return os.environ[name] or default
    path = _PROJECT_ROOT / ".env"
    try:
        from dotenv import dotenv_values

        from src.file_cache import cached_parse
        value = cached_parse(path, lambda p: dict(dotenv_values(p)), "dotenv").get(name)
    except Exception:  # noqa: BLE001 — no .env, or unreadable: use the default
        value = None
    return value or default


def configured_models(role: str = "main") -> list[str]:
    """The model chain for a role ("main" or "critic"); [] when the layer is off."""
    main = _env("LLM_MODEL")
    if not main:
        return []
    fallbacks = [m.strip() for m in (_env("LLM_FALLBACK_MODELS") or "").split(",") if m.strip()]
    chain = [main] + fallbacks
    if role == "critic" and _env("LLM_CRITIC_MODEL"):
        chain = [_env("LLM_CRITIC_MODEL")] + chain
    seen: list[str] = []
    return [m for m in chain if not (m in seen or seen.append(m))]


def is_configured() -> bool:
    return bool(configured_models())


# ---------------------------------------------------------------------------
# Usage log
# ---------------------------------------------------------------------------
_usage_tags: contextvars.ContextVar[dict[str, Any]] = contextvars.ContextVar(
    "llm_usage_tags", default={})
_usage_sink: Callable[[dict[str, Any]], None] | None = None


def set_usage_sink(sink: Callable[[dict[str, Any]], None] | None) -> None:
    """Where call records go (the boundary passes store.record_llm_call)."""
    global _usage_sink
    _usage_sink = sink


@contextmanager
def usage_context(**tags: Any) -> Iterator[None]:
    """Label the model calls made inside: feature=..., student_id=..., class_id=..."""
    token = _usage_tags.set({**_usage_tags.get(), **tags})
    try:
        yield
    finally:
        _usage_tags.reset(token)


def _report(model: str, ok: bool, started: float, usage: dict[str, Any] | None,
            error: str | None = None) -> None:
    if _usage_sink is None:
        return
    usage = usage if isinstance(usage, dict) else {}

    def tokens(key: str) -> int | None:
        value = usage.get(key)
        return int(value) if isinstance(value, (int, float)) else None

    tags = _usage_tags.get()
    try:
        _usage_sink({
            "feature": tags.get("feature", "other"),
            "student_id": tags.get("student_id"), "class_id": tags.get("class_id"),
            "model": model, "ok": ok,
            "prompt_tokens": tokens("prompt_tokens"),
            "completion_tokens": tokens("completion_tokens"),
            "latency_ms": int((time.monotonic() - started) * 1000),
            "error": error,
        })
    except Exception:  # noqa: BLE001 — logging must never break a model call
        pass


# Tests swap this for an httpx.MockTransport; None means real network.
_transport: httpx.BaseTransport | None = None


def _post(model: str, payload: dict[str, Any], timeout: float | None = None) -> dict[str, Any]:
    base = (_env("LLM_BASE_URL", DEFAULT_BASE_URL) or DEFAULT_BASE_URL).rstrip("/")
    headers = {"Content-Type": "application/json"}
    key = _env("LLM_API_KEY")
    if key:
        headers["Authorization"] = f"Bearer {key}"
    timeout = timeout or float(_env("LLM_TIMEOUT_SECONDS", "60") or 60)
    try:
        with httpx.Client(timeout=timeout, transport=_transport) as client:
            response = client.post(f"{base}/chat/completions", headers=headers,
                                   json={**payload, "model": model})
    except httpx.HTTPError as exc:
        raise LLMError(f"{model}: {type(exc).__name__}") from exc
    if response.status_code >= 400:
        raise LLMError(f"{model}: HTTP {response.status_code}")
    try:
        return response.json()
    except ValueError as exc:
        raise LLMError(f"{model}: not JSON") from exc


def chat(
    messages: list[dict[str, Any]],
    *,
    role: str = "main",
    models: list[str] | None = None,
    tools: list[dict[str, Any]] | None = None,
    temperature: float = 0.4,
    max_tokens: int = 1200,
) -> ChatResult:
    """Send a chat; try each model in the chain until one answers.

    `tools` uses the OpenAI format ({"type": "function", "function": {...}}).
    Tool calls come back parsed: [{"id", "name", "args": dict}].

    Raises:
        LLMError: the layer is off, or every model failed.
    """
    chain = models if models is not None else configured_models(role)
    if not chain:
        raise LLMError("No model configured (set LLM_MODEL).")
    payload: dict[str, Any] = {"messages": messages, "temperature": temperature,
                               "max_tokens": max_tokens}
    if tools:
        payload["tools"] = tools
    failures = []
    for model in chain:
        started = time.monotonic()
        try:
            data = _post(model, payload)
            choice = (data.get("choices") or [{}])[0]
            message = choice.get("message") or {}
            calls = []
            for call in message.get("tool_calls") or []:
                fn = call.get("function") or {}
                try:
                    args = json.loads(fn.get("arguments") or "{}")
                except ValueError:
                    args = {}
                calls.append({"id": call.get("id") or fn.get("name", ""), "name": fn.get("name", ""),
                              "args": args if isinstance(args, dict) else {}})
            text = message.get("content") or ""
            if not text and not calls:
                raise LLMError(f"{model}: empty answer")
            _report(data.get("model") or model, True, started, data.get("usage"))
            return ChatResult(text=text, tool_calls=calls, message=message,
                              model=data.get("model") or model)
        except LLMError as exc:
            _report(model, False, started, None, str(exc))
            failures.append(str(exc))
    raise LLMError("All models failed: " + "; ".join(failures))


# ---------------------------------------------------------------------------
# Is the AI up?
# ---------------------------------------------------------------------------
_HEALTH_TTL_SECONDS = 60
_health_cache: dict[str, Any] = {"at": 0.0, "value": None}
# The probe must look like a real call, or it reports the wrong thing (2026-10-27): with 8 tokens
# and a 30 s timeout it said "down" while real calls answered, because "thinking" models spend
# their first tokens reasoning (an 8-20 token budget came back empty) and free models often take
# 20-60 s. So: the real calls' timeout, room to think, and an empty reply counts as a failure,
# exactly as in chat().
_HEALTH_MAX_TOKENS = 512
SLOW_MS = 15_000  # answering, but slower than a student should wait for


def health(force: bool = False) -> dict[str, Any]:
    """Is a model answering right now, the way real calls would? The answer is kept for a minute.

    Tries the main chain in order and stops at the first model that answers, so a
    healthy primary costs one small call. Same timeout as real calls (LLM_TIMEOUT_SECONDS),
    and an empty reply is a failure, as in chat(). Used by the teacher's status badge
    and scripts/ai_check.py; never on a student's path.

    Returns {"configured": bool, "up": bool, "model": answering model | None,
             "primary": the first model of the chain | None,
             "on_fallback": bool, "latency_ms": int | None, "slow": bool,
             "tried": [{"model", "ok", "error", "latency_ms"}], "checked_at": epoch seconds}.
    """
    now = time.time()
    cached = _health_cache["value"]
    if not force and cached is not None and now - _health_cache["at"] < _HEALTH_TTL_SECONDS:
        return cached
    chain = configured_models("main")
    tried: list[dict[str, Any]] = []
    answering, latency = None, None
    for model in chain:
        started = time.monotonic()
        try:
            data = _post(model, {"messages": [{"role": "user", "content": "Reply with the word OK."}],
                                 "temperature": 0, "max_tokens": _HEALTH_MAX_TOKENS})
            message = ((data.get("choices") or [{}])[0].get("message") or {})
            if not (message.get("content") or "").strip():
                raise LLMError(f"{model}: empty answer")
            answering, latency = model, int((time.monotonic() - started) * 1000)
            tried.append({"model": model, "ok": True, "error": None, "latency_ms": latency})
            break
        except LLMError as exc:
            tried.append({"model": model, "ok": False, "error": str(exc)[:200],
                          "latency_ms": int((time.monotonic() - started) * 1000)})
    value = {"configured": bool(chain), "up": answering is not None, "model": answering,
             "primary": chain[0] if chain else None,
             "on_fallback": answering is not None and answering != chain[0],
             "latency_ms": latency, "slow": latency is not None and latency > SLOW_MS,
             "tried": tried, "checked_at": now}
    _health_cache["at"], _health_cache["value"] = now, value
    return value


def parse_json_object(text: str) -> dict[str, Any] | None:
    """The first JSON object in a model's reply (free models often wrap it in
    prose or ``` fences), or None."""
    if not text:
        return None
    start = text.find("{")
    while start != -1:
        depth = 0
        for i in range(start, len(text)):
            if text[i] == "{":
                depth += 1
            elif text[i] == "}":
                depth -= 1
                if depth == 0:
                    try:
                        value = json.loads(text[start:i + 1])
                        return value if isinstance(value, dict) else None
                    except ValueError:
                        break
        start = text.find("{", start + 1)
    return None
