"""Smoke test for the remote Ollama server exposed through Cloudflare."""

from __future__ import annotations

import json
from pathlib import Path
import urllib.error
import urllib.request


PROJECT_ROOT = Path(__file__).resolve().parent
ANALOGY_PROMPT_PATH = PROJECT_ROOT / "prompts" / "analogy_generator.txt"

OLLAMA_BASE_URL = "https://das-guests-police-supply.trycloudflare.com"
OLLAMA_MODEL = "llama3.2:3b"


def ollama_generate(prompt: str) -> str:
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.35,
        },
    }
    request = urllib.request.Request(
        f"{OLLAMA_BASE_URL}/api/generate",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            data = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Ollama HTTP {exc.code}: {body}") from exc

    return data.get("response", "").strip()


def build_analogy_prompt(concept: str, interest: str, level: str = "Class 11") -> str:
    system_prompt = ANALOGY_PROMPT_PATH.read_text(encoding="utf-8")
    user_message = "\n".join(
        [
            f"Concept: {concept}",
            f"Student interest: {interest}",
            f"Level: {level}",
            "",
            "Generate the final student-facing explanation now.",
            "The first line of your response must be exactly: 1. SCENARIO",
            (
                "Do not include planning notes, checklists, drafts, "
                "self-corrections, word-count checks, or prompt summaries."
            ),
        ]
    )
    return f"{system_prompt}\n\n---\n\n{user_message}"


if __name__ == "__main__":
    prompt = build_analogy_prompt(
        concept="relative velocity",
        interest="football",
        level="Class 11",
    )
    print(ollama_generate(prompt))
