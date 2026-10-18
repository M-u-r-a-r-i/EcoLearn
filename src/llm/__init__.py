"""One way for new agents to call a language model (the start of ROADMAP M1a).

Everything goes through an OpenAI-compatible chat endpoint, which covers:
* OmniRoute, a self-hosted gateway (default: http://localhost:20128/v1), in
  front of free providers — the setup for the pilot (user decision, 2026-10-02);
* OpenRouter, Groq, or any other OpenAI-compatible service;
* Gemini itself, through Google's OpenAI-compatible endpoint
  (https://generativelanguage.googleapis.com/v1beta/openai), once a paid key
  is bought — a config change, not a code change.

The four older agents (generator, critic, polisher, assessor) still call
google-genai directly; moving them here is the rest of M1a.
"""

from src.llm.client import (
    ChatResult,
    LLMError,
    chat,
    configured_models,
    health,
    is_configured,
    set_usage_sink,
    usage_context,
)

__all__ = ["LLMError", "ChatResult", "chat", "configured_models", "health", "is_configured",
           "set_usage_sink", "usage_context"]
