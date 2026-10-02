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
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

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
    """os.environ first, then the project's .env (read each time: cheap, and a
    key added while the server runs is picked up without a restart)."""
    value = os.getenv(name)
    if value:
        return value
    try:
        from dotenv import dotenv_values
        value = dotenv_values(_PROJECT_ROOT / ".env").get(name)
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


# Tests swap this for an httpx.MockTransport; None means real network.
_transport: httpx.BaseTransport | None = None


def _post(model: str, payload: dict[str, Any]) -> dict[str, Any]:
    base = (_env("LLM_BASE_URL", DEFAULT_BASE_URL) or DEFAULT_BASE_URL).rstrip("/")
    headers = {"Content-Type": "application/json"}
    key = _env("LLM_API_KEY")
    if key:
        headers["Authorization"] = f"Bearer {key}"
    timeout = float(_env("LLM_TIMEOUT_SECONDS", "60") or 60)
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
            return ChatResult(text=text, tool_calls=calls, message=message,
                              model=data.get("model") or model)
        except LLMError as exc:
            failures.append(str(exc))
    raise LLMError("All models failed: " + "; ".join(failures))


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
