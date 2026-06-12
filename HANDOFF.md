# EcoLearn — Handoff for the next session

**Read this first**, then `LOG.md` if you need full chronological history.

Memory files (auto-loaded from `C:\Users\murar\.claude\projects\D--Projects-EcoLearn\memory\`) already give the new session: tech-stack preference (Gemini/Gemma, `google-genai` SDK), push-after-sprint reminder, and update-LOG-after-each-request rule. This document covers what those memories don't.

---

## 1. What EcoLearn is

A personalized AI tutor for CBSE/ISC Class 11 physics. The student picks an interest (currently football or gaming), and the system explains concepts by grounding analogies in that domain. Originally a chatbot; **currently being extended into a learning platform** with a structured curriculum spine.

**Architecture (current):**

```
Streamlit UI (app.py)
   │
   ├─ Router (1 cheap LLM call) → TUTOR | CHAT | ASSESS
   │
   ├─ TUTOR  →  Pipeline (src/pipeline.py)
   │             ├─ RAG retrieve  (Chroma, local ONNX embeddings)
   │             ├─ Analogy Generator   (prompts/analogy_generator.txt)
   │             ├─ Pedagogical Critic  (prompts/critic.txt, JSON output)
   │             ├─ (retry on FAIL with feedback)
   │             └─ Polisher (LLM cleanup → ###/bullets/blockquote markdown)
   │
   ├─ ASSESS →  Assessor (src/agents/assessor.py)
   │             ├─ generate_question(concept, interest, level) → JSON
   │             └─ grade_answer(question, expected, student) → JSON
   │
   └─ Mastery tracker in st.session_state.mastery
        { concept: {attempts, best_score, status: mastered|partial|not_yet} }
```

---

## 2. Current git state

```
* extension   e7c3e0e  Laid boiler plate for extension      ← HEAD
  master      e7c3e0e  (identical to extension right now)
```

Both `master` and `extension` point at the same commit. The "curriculum spine" work (Pydantic schema, YAML loader, physics.yaml, tests) is on this commit.

**Pending decision the user paused on**: they want to delete the `extension` branch, reset master back one commit (to `e852392 Handled frequent error popups`), create a fresh new branch with the curriculum work, and force-push master. The exact sequence is documented in the previous turn but not yet executed. They were about to confirm (a) new branch name and (b) consent to force-push master, both still open questions.

---

## 3. File map (only the load-bearing files)

```
app.py                              Streamlit UI + router + polisher + sanitizer
src/pipeline.py                     explain_with_review(): RAG → gen → critic → retry
src/agents/analogy_generator.py     Loads prompts/analogy_generator.txt; sub_interest_facts + curriculum_context params
src/agents/critic.py                Strict-JSON critic, fails open (returns soft PASS on API error)
src/agents/assessor.py              Two-mode (generate_question, grade_answer)
src/rag/ingest.py                   build_index.py uses this to load corpora into Chroma
src/rag/retrieve.py                 retrieve_concept(query, n), retrieve_interest(query, interest, n)
src/curriculum/schema.py            Pydantic: Subject → Unit → Chapter → Concept (BloomLevel enum)
src/curriculum/loader.py            load_subject(path); teaching_order; resolve_prerequisites; validate_ordering
data/curriculum/physics.yaml        9 concepts of Motion in a Straight Line; the curriculum source of truth
src/data/curriculum/*.md            RAG corpus — Class 11 physics passages (kinematics, work-energy)
src/data/interests/*.md             RAG corpus — football, gaming (20 passages each)
prompts/analogy_generator.txt       Heavy guardrails against Gemma 4 scratchpad leakage
prompts/critic.txt                  3-axis rubric (science, pedagogy, integrity), JSON, examples
prompts/assessor.txt                Two-mode prompt; JSON for both modes
tests/test_*.py                     Per-agent smoke tests
tests/benchmark_v3.py / .md         RAG-fed 10-case benchmark
LOG.md                              Dated entries with Changed / Why / Learned per work session
iterate.py                          Single-case CLI for cheap prompt iteration
chroma_db/                          Local vector store (gitignored, rebuildable)
.env                                GEMINI_API_KEY, GEMINI_MODEL, GEMINI_MAX_OUTPUT_TOKENS
```

---

## 4. Models in use (today's reality)

```
GEMINI_MODEL=gemma-4-31b-it          (generator, .env)
CRITIC_MODEL=gemini-2.5-flash-lite   (default in src/agents/critic.py; QUOTA EXHAUSTED today)
POLISHER_MODEL=gemini-2.5-flash-lite (default in app.py; QUOTA EXHAUSTED today)
ROUTER_MODEL=gemma-4-31b-it          (default in app.py)
ASSESSOR_QUESTION_MODEL=gemma-4-31b-it  (default in src/agents/assessor.py)
ASSESSOR_GRADE_MODEL=gemma-4-31b-it     (default in src/agents/assessor.py)
```

The critic and polisher fall back gracefully when quota is exhausted — critic returns soft PASS; polisher returns input unchanged.

---

## 5. Key pattern decisions (don't re-debate these)

- **Gemma 4 31B leaks scratchpad.** The prompt has heavy guardrails, but the **polisher LLM** (`_polish_explanation` in app.py) is the actual reliable cleanup. Sanitizer regex is the first line; the polisher is the wall.
- **Critic fails open.** On API error or unparseable JSON, returns `{verdict: PASS, error: ...}`. Better to ship an imperfect lesson than to crash the chat.
- **`_generate_reply` returns `(text, ok)`.** Callers (the TUTOR branch in `_handle_new_turn`) only save `last_concept` and offer the quiz when `ok=True`. Avoids phantom quizzes on errored turns.
- **Two-phase button pattern.** Streamlit click handlers never do long work inline. They only flip `processing_action` and `st.rerun()`. The next render runs the work behind a spinner with no buttons visible. Prevents stray-click cancellation.
- **Polisher output is `### Scenario / ### Formal Restatement / ### Self-Check Question`** with bulleted **Mapping:**, `> blockquote` breakdowns and hints, `$$...$$` standalone equations, `**Where:**` symbol glossary, `---` separators. Math is normalized to LaTeX (Unicode → `\theta`, `\approx`, `^2`, etc.) for KaTeX rendering.
- **Chat router has three modes**: TUTOR (real pipeline), ASSESS (quiz), CHAT (quick reply). "I understood" routes to ASSESS. ASSESS without a `last_concept` redirects with "tell me what to teach first."
- **Mastery ledger**: `st.session_state.mastery[concept] = {attempts, best_score, status}`. Score 0–3 → status `not_yet` / `partial` / `mastered` via `_status_from_score`. Best score across attempts (not last score) — a student who finally nails it has demonstrably learned.
- **Sidebar mastery badges**: green `#2e7d32` (mastered), amber `#ef6c00` (partial), grey `#757575` (not_yet). Rendered as HTML pills via `_mastery_badge`.

---

## 6. Known issues / gotchas

- **`gemini-2.5-flash` and `gemini-2.5-flash-lite` daily quotas (20 req/day) are exhausted** on the user's API key for today. Gemma quota is roomy. All Gemini-Flash-dependent paths fail open; Gemma takes over.
- **Free-tier quotas are per-model.** Swapping `GEMINI_MODEL` to a Gemma variant is the fastest unblock when Gemini quota is hit.
- **`gemma-3-27b-it` returns 404 on this API key.** Only `gemma-4-31b-it` works for Gemma generation. (Documented in earlier failure.)
- **Gemma 4 default `max_output_tokens=1024` is too small** — assessor was empty-responding until bumped to 2048. Already fixed.
- **Streamlit auto-reloads on file change.** When editing, look for the "Source file changed — Rerun" banner top-right.
- **chroma_db/ is gitignored.** Anyone cloning needs to run `python src/rag/build_index.py` once to rebuild the vector store (~30 s, no API).

---

## 7. Open work the user is interested in

1. **Branch cleanup** (immediate, paused): see section 2.
2. **Local-LLM migration** (next big task): switch the whole stack to Ollama-served local models on a friend's mid-tier laptop (RTX 3050, 6–8 GB VRAM). Plan documented in last turn — Qwen 2.5 7B for generator, Phi 3.5 Mini for critic/polisher/router/grader. Refactor centres on adding `src/llm/client.py` and replacing every `google.genai` call with an `openai`-package call against `http://localhost:11434/v1`.
3. **Curriculum platform extension** (in progress, on `extension` branch): just shipped the schema + YAML + loader spine. Natural next moves: a lesson planner that walks `teaching_order()`, a recommendation system that uses `resolve_prerequisites(..., transitive=True)`, a Streamlit UI for browsing units/chapters, a CLI that validates every YAML in `data/curriculum/`.

---

## 8. User preferences worth carrying forward

- **Beginner-friendly explanations.** Explain the *why* alongside any tricky pattern. They asked for this in onboarding and have been consistent about it.
- **Don't auto-commit.** The user pushes themselves. Each closing reply should include a 📌 push reminder.
- **Update LOG.md after every directory-touching request.** Append a dated entry with **Changed / Why / Learned** sub-sections. Memory file documents this.
- **Use Gemini/Gemma via `google-genai`.** Tech-stack memory documents this; don't propose other providers without being asked.
- **Honest critique > polite vibes.** When asked to review work, name what's wrong specifically. The user has explicitly preferred this kind of feedback.
- **Push reminder after each sprint.** Memory file documents this.

---

## 9. How to verify the new session has loaded context cleanly

After loading this file in a new session, the new Claude should be able to answer (without asking):

- Which model is the generator? → `gemma-4-31b-it`
- What happens when "Internal error" appears in the chat? → critic or polisher 429, but they fail open now
- Where do new concepts get added? → `data/curriculum/physics.yaml`, no code change
- What pattern prevents stray-click button races in Streamlit? → two-phase: flip `processing_action`, `st.rerun()`, work in next render
- Why is the polisher prompt so elaborate about LaTeX? → Streamlit `st.markdown` renders KaTeX; the model emits mixed Unicode/LaTeX which renders inconsistently
- What's on the `extension` branch right now? → `Subject/Unit/Chapter/Concept` Pydantic schema + 9-concept physics.yaml + loader with prerequisite-respecting teaching order

If any of those need re-derivation, the handoff didn't carry enough context — flag back.

---

## 10. Quick start commands (sanity-check the new session can run)

```
# Validate curriculum spine (no API calls)
D:\Projects\EcoLearn\venv\Scripts\python.exe D:\Projects\EcoLearn\tests\test_curriculum.py

# Rebuild RAG index if chroma_db missing
D:\Projects\EcoLearn\venv\Scripts\python.exe D:\Projects\EcoLearn\src\rag\build_index.py

# Start the chat
D:\Projects\EcoLearn\venv\Scripts\streamlit.exe run D:\Projects\EcoLearn\app.py --server.headless true
```

Streamlit is currently running in the background on port 8501.

---

**The two things the user was paused on when this session ended:**
1. Confirming the new branch name (for the curriculum work to be moved to)
2. Confirming consent to `git push --force origin master` to reset master back one commit

When the new session starts: re-read this file, then ask the user those two questions before running any git operations.
