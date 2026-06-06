# EcoLearn — Working Log

## 2026-05-22: Project setup
- Created Python 3.10 virtual environment, folder structure (src/agents, src/data, prompts, tests), requirements.txt, .env template, .gitignore, and README.
- Learned: virtual environments isolate project dependencies; .gitignore prevents secrets and bloat from entering version control.

## 2026-06-06: Multi-agent pipeline built and tightened

### Built (catching the log up since setup)
- Switched LLM stack to Google Gemini/Gemma via the `google-genai` SDK (the old `google-generativeai` is deprecated).
- `src/agents/analogy_generator.py` — Analogy Generator. Loads system prompt from `prompts/analogy_generator.txt`. Configurable via env: `GEMINI_MODEL`, `GEMINI_MAX_OUTPUT_TOKENS`, `GEMINI_THINKING_BUDGET` (the last applied only when model starts with `gemini-2.5-flash`). Accepts a `prior_feedback` parameter so the pipeline can fold critic feedback into a regen.
- `prompts/analogy_generator.txt` — analogy-discipline prompt: structural mapping with three explicit tests (element correspondence, relation preservation, honest breakdown), required mapping table, self-rating, two few-shot examples (football/relative velocity, gaming/work-energy theorem).
- `src/agents/critic.py` — Pedagogical Critic returning strict JSON `{verdict, scientific_correctness, pedagogical_fit, analogical_integrity, feedback}`. Uses cheaper model via `CRITIC_MODEL` (default `gemini-2.5-flash-lite`), temperature 0.1, JSON-mime mode for Gemini, parse-retry fallback for other models.
- `prompts/critic.txt` — three-axis rubric with "DO NOT fail for X" calibration and three worked examples (one PASS, one science-FAIL, one analogical-integrity-FAIL).
- `src/pipeline.py` — `explain_with_review()`: generate → critique → on FAIL feed feedback back into the next generate, repeat up to `max_retries`. Returns explanation + verdict + attempt history.
- Tests: `tests/test_analogy.py` (3-case smoke), `tests/test_critic.py` (good vs broken physics), `tests/test_pipeline.py` (5-case e2e), `tests/benchmark_analogy.py` (10-case benchmark with 429 retry).
- `iterate.py` — single-case CLI for cheap prompt iteration during tuning.

### Tuned today
- `.env`: switched `GEMINI_MODEL` from `gemini-2.5-flash` (hit its 20/day free-tier ceiling) to `gemma-4-31b-it` for the generator, which sits on a separate, much larger quota bucket. Commented out `GEMINI_THINKING_BUDGET` since Gemma doesn't expose that knob.
- `prompts/analogy_generator.txt`: added two explicit "output only the final answer" blocks — one in OUTPUT FORMAT, one in SELF-RATING. Without them, Gemma 4 was leaking its planning notes, length checks, and scoring reasoning into the student-facing response.

### Learned
- Each model on Gemini API has its own free-tier daily quota bucket; swapping `GEMINI_MODEL` is the fastest way to recover from a daily-cap 429 without waiting for reset. Gemma models share none of Gemini Flash's quota.
- Reasoning-capable open models like Gemma 4 dump their internal monologue into the response by default. They need explicit "do not show scratch work" instructions or downstream parsing (and the student) gets the wrong artifact.
- Splitting strict-JSON critic from creative generator is a robust pattern: lower temperature + smaller/cheaper model + schema-enforced output makes the loop reliable while halving spend per retry sequence.
- Keep prompts in `.txt`, not Python. Today's tuning was a 2-line text edit — no code change, no review, easy to revert.
