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

## 2026-06-07: Curriculum and interest corpora

### Changed
- `src/data/curriculum/physics_kinematics.md` — 12 NCERT-aligned Class 11 passages: position, displacement, distance, velocity, speed, acceleration, average vs instantaneous, equations of motion, projectile motion, relative velocity (1D and 2D), free fall.
- `src/data/curriculum/physics_work_energy.md` — 10 passages: work by constant force, work-energy theorem, KE, PE, conservation of energy, power, work by variable force, energy loss to friction, conservative vs non-conservative forces, real-world examples.
- `src/data/interests/football.md` — 20 short (50–100 word) physics-relevant passages: sprint speeds (Mbappé 38 km/h), pass and shot speeds, interception geometry, free-kick trajectory (Magnus + knuckleball), Roberto Carlos 1997, Alonso 2006, friction on dry/wet/snow pitches, positions, set pieces.
- `src/data/interests/gaming.md` — 20 passages: racing-game accel + top speed (Forza, Asphalt 9, iRacing), FPS hitscan vs ballistic, physics engines (Havok, PhysX), MOBA mana, Souls stamina, Asphalt 9 nitro + drift, Angry Birds projectile motion, frame rate, hit detection, pathfinding.

### Why
The Analogy Generator needs trustworthy domain detail it can ground its scenarios in, rather than relying on whatever the LLM half-remembers. Two corpora — academic (curriculum) and personal (interest) — were the cleanest split.

### Learned
- Authoring corpora is the most undervalued step in a RAG app. Half of "the model is hallucinating" is "the corpus didn't contain the right fact"; a 200-word, accurate passage beats hours of prompt engineering.
- Headings (`## Heading`) double as chunk boundaries for the eventual ingestor — write the corpus so every section is a self-contained chunk and ingestion gets simpler.

## 2026-06-08: RAG ingestion and retrieval

### Changed
- `requirements.txt` — confirmed `chromadb` is installed (1.5.9).
- `src/rag/__init__.py` — package marker.
- `src/rag/ingest.py` — `ingest_corpus(corpus_dir, collection_name)`: walks .md files, splits by `## ` headings (falls back to 250-token windows with 50-token overlap for oversized sections), attaches metadata `{source_file, heading, corpus_type, interest}`, embeds via Chroma's default `all-MiniLM-L6-v2` (ONNX, local — no API).
- `src/rag/build_index.py` — runs `ingest_corpus` twice (curriculum + interests) and prints chunk counts.
- `src/rag/retrieve.py` — `retrieve_concept(query, n)` and `retrieve_interest(query, interest_name, n)` returning `[{text, metadata, distance}, ...]`. The interest retriever uses Chroma's `where={"interest": ...}` filter so football queries never return gaming passages.
- `tests/test_retrieval.py` — 4 sample queries; sanity-checked the top hits manually.
- `.gitignore` — added `chroma_db/` (regenerable from corpora; ~90 MB of binary index).

### Why
The pipeline needed a fast, local source of authoritative passages to feed into both the generator (as context) and any future judging or analysis steps.

### Learned
- Chroma's default embedding (`all-MiniLM-L6-v2` via onnxruntime) is shipped inside chromadb and runs without internet after the first model download. No API key, no cost, no quota.
- 384-dimensional embeddings + cosine distance + 60 chunks fit comfortably in RAM on a laptop; no need to think about scale until corpora cross thousands of pages.
- Embedding ranking can surprise — gaming "Racing top speed" lost to "60 fps vs 30 fps" for the query "racing game acceleration physics" because the latter contained more explicit speed-distance math. Always spot-check.

## 2026-06-09: RAG fed into the pipeline (benchmark v3)

### Changed
- `src/agents/analogy_generator.py` — added `curriculum_context: Iterable[str] | None` parameter; `_build_user_message` now renders labelled `CURRICULUM CONTEXT` and `INTEREST CONTEXT` blocks when provided. Kept `sub_interest_facts` for backwards compatibility; the pipeline passes the retrieved interest passages there.
- `prompts/analogy_generator.txt` — new "PROVIDED CONTEXT — source of truth" section: when context is present, equations and figures from `CURRICULUM CONTEXT` override prior knowledge; named examples from `INTEREST CONTEXT` are preferred. Do not quote the context verbatim; weave it in.
- `src/pipeline.py` — `explain_with_review` now calls `retrieve_concept(concept, 3)` and `retrieve_interest(concept + " " + interest, interest, 3)` BEFORE the first generate, then passes both lists into every (re)generation. Result dict includes `curriculum_context` and `interest_context` for inspection.
- `tests/benchmark_v3.py` + `tests/benchmark_v3_output.md` — 10-case benchmark that runs `generate_explanation` with RAG context (no critic), saving both the retrieved passages AND the explanation per case so the diff vs `benchmark_output.md` (v2) is auditable.

### Why
v2 outputs invented numbers and generic examples; v3 should ground every claim in the authored corpora.

### Learned
- RAG was a clear factual win: v3 outputs name Mbappé at 10 m/s, iRacing, Kerbal Space Program, Roberto Carlos 1997, 25 m/s lofted passes — all lifted from the corpora.
- Adding 6 retrieved passages to the user message triggered Gemma 4 to "plan more out loud": the longer the user message, the more aggressively the model spilled scratchpad. RAG and discipline pull in opposite directions; downstream cleanup is necessary regardless of prompt tightening.

## 2026-06-10: Streamlit chat app + math polishing

### Changed
- `app.py` — Streamlit front-end with onboarding + chat views. Profile (name, interest, level/class, subject) lives in `st.session_state.profile`; chat history in `st.session_state.messages`. Used `st.form` for onboarding to batch input, `st.chat_message` + `st.chat_input` for the chat, custom CSS to right-align user bubbles, and `st.empty()` for live in-bubble status updates.
- `src/pipeline.py` — added optional `on_status: Callable[[str], None]` so the UI can show "EcoLearn is retrieving context → generating → asking the critic → polishing" as a live line inside the assistant bubble.
- Sanitizer + polisher pass (in `app.py`): a fast regex pre-clean (`_sanitize_explanation`) that slices between `1. SCENARIO` and `[ANALOGY_QUALITY: N]`, and falls back to paragraph-level stripping when those markers are missing. A second cheap LLM call (`_polish_explanation`, default `gemini-2.5-flash-lite`) extracts the final three-section answer regardless of how badly Gemma 4 dumped its scratchpad.
- Polisher rewritten to normalise math: convert all Unicode (`θ`, `≈`, `²`, `√`, `×`) to LaTeX (`\theta`, `\approx`, `^2`, `\sqrt`, `\times`), wrap inline math in `$...$` and standalone equations in `$$...$$`, units inside `\text{}`. Streamlit's `st.markdown` renders these via KaTeX automatically.

### Why
The pipeline produced strong content but Gemma 4 leaked planning notes into the bubble, and equations rendered inconsistently (half-Unicode, half-LaTeX). Both problems blocked actually using the app.

### Learned
- Regex cleanup is a losing race against an LLM that keeps inventing new scratchpad labels (`*Previous Error N:*`, `*Drafting:*`, `*Word count check:*`). A small LLM polisher with a clear extraction instruction wins where regex fails — and runs on a separate quota bucket from the generator.
- Streamlit's `st.markdown` renders KaTeX automatically from `$...$` and `$$...$$`. Equation appeal depends entirely on whether the LLM emits proper LaTeX consistently; mixed Unicode/LaTeX looks broken even when both forms are valid.
- For long-running steps inside an `st.chat_message`, use `st.empty()` placeholders + callback so the user sees what's happening, not just a generic spinner.

## 2026-06-11: Assessor agent (question generation + grading)

### Changed
- `prompts/assessor.txt` — single system prompt dispatching on a `Mode:` line:
  - `generate_question` → strict JSON `{question, expected_concepts, difficulty_level: recall|apply|analyze}`.
  - `grade_answer` → strict JSON `{score 0-3, mastery_signal: mastered|partial|not_yet, feedback, missing_concepts}`.
  - Three worked examples (one PASS, one science-FAIL, one analogy-integrity-FAIL).
- `src/agents/assessor.py` — `generate_question(concept, interest, level)` at temperature 0.4, `grade_answer(question, expected_concepts, student_answer)` at temperature 0.1. JSON parse + one retry; sentinel dict on permanent failure. Models configurable via `ASSESSOR_QUESTION_MODEL` / `ASSESSOR_GRADE_MODEL`; both default to `gemma-4-31b-it` once `gemini-2.5-flash-lite` quota was exhausted.
- `tests/test_assessor.py` — generates one question on "work-energy theorem" + football, then grades three answers (GREAT / PARTIAL / WRONG).
- Bumped `_DEFAULT_MAX_OUTPUT_TOKENS` from 1024 to 2048 after the first run came back empty (Gemma 4 burned the budget on scratchpad before emitting JSON). Added a `finish_reason` print on empty responses.

### Why
The pipeline could *explain*; it couldn't *check whether the student got it*. The Assessor closes that gap.

### Learned
- Two-mode prompts are economical: one system prompt + one parser + one retry pattern, dispatched on a `Mode:` header. Cuts prompt-management overhead in half compared with two separate agents.
- Even a "good" answer can score 0 if it doesn't answer THIS question — the grader is doing the right thing, my test answers just weren't tuned to the assessor-generated scenario. Lesson: test answers should be written *after* seeing the question.
- "Internal error" feedback for the WRONG answer ("you confused work-energy with momentum") is gold for tutoring. It's the kind of feedback a real teacher gives, and the grader produced it naturally with a clear rubric.

## 2026-06-12: Intent router + lightweight chat

### Changed
- `app.py` — added `_classify_intent(user_text, profile)`: one cheap LLM call returns `{mode: TUTOR|CHAT, concept, chat_reply}`. The full pipeline only fires when `mode == TUTOR`; `mode == CHAT` returns the router's prewritten reply in 1–2 seconds. Examples in the prompt cover greetings, thanks, off-topic, vague follow-ups, explicit concept requests.
- Tagged each user message in `st.session_state.messages` with `mode` and `concept` so the sidebar counter can ignore chitchat.
- Sidebar's `Concepts explored` switched to counting unique concepts from TUTOR-mode messages only.

### Why
Running the 30–60 s multi-agent pipeline for "hi" or "thanks" was both slow and quota-burning.

### Learned
- A small router is the right pre-filter for any LLM app where the action is expensive: one $0.0001 call protects a $0.01 call. The ROI is huge.
- Combining classify + chat_reply into one structured-output call saves a second LLM round trip when the answer is chitchat.
- Fail-open on the router: if it errors, treat the message as TUTOR. The router can only make the app *more* responsive than it was, never less.

## 2026-06-13: Quiz flow, mastery tracking, race-condition fix

### Changed
- `app.py` — added a third router mode `ASSESS` (e.g. "I understood", "test me", "quiz me on momentum"). The handler generates a question via the Assessor and arms `st.session_state.awaiting_answer`; the next user message is graded.
- After a TUTOR turn: `st.session_state.pending_action = "offer_quiz"` triggers a transient "Want to try a quick question? [Yes, quiz me] [Not yet]" bubble below the chat history.
- After a graded answer: `pending_action = "post_grade"` triggers "[Try another question] [Move on]".
- `st.session_state.mastery: dict[concept, {attempts, best_score, status}]` updated after each grade. Status derived from best_score (3 = mastered, 2 = partial, ≤1 = not_yet).
- Sidebar gained a Mastery panel with colour-coded pills (green / amber / grey) per concept and a `Quizzes taken` metric.
- Race-condition fix: clicks now use a two-phase pattern. Phase 1 (button handler) flips `processing_action` and `st.rerun()`s in microseconds. Phase 2 (next render) runs `_do_pending_work` behind a spinner with NO buttons visible, so a stray click on a stale "Not yet" can't cancel an in-flight question generation. Chat input is also disabled while `processing_action` is set.

### Why
The chat flow needed to be a real teach → check → grade → move-on loop, not just one-shot explanations. And the user found a real bug: pressing two buttons in quick succession was cancelling the work mid-flight.

### Learned
- **Never put long-running work inside a Streamlit button handler.** A click handler should be atomic: flip state, rerun. The work happens in the next render when no clickable elements exist. Anything else races.
- Streamlit's `disabled=` on `chat_input` is defense-in-depth — even if no button is visible, blocking the input prevents a typed-message race.
- Mastery as `{concept: {attempts, best_score, status}}` is the minimum useful shape — fewer fields and it's not useful, more fields and it overfits to a UI that hasn't been designed yet. Take the *best* score across attempts: a student who finally nails it has demonstrably learned.

## 2026-06-14: Pipeline error handling, soft-PASS critic, scannable layout

### Changed
- `src/agents/critic.py` — critic now **fails open**: on any API exception (e.g. 429 from the exhausted Lite quota), it returns a soft-PASS verdict with the error reason in an `error` field, so the pipeline keeps shipping a (possibly imperfect) explanation instead of crashing.
- `app.py` `_generate_reply()` now returns `(text, ok)` and uses `_explain_pipeline_error()` to produce specific, friendly messages for rate-limit, empty-response, model-not-found, and generic failures. Callers respect the `ok` flag.
- TUTOR branch in `_handle_new_turn`: only sets `last_concept` and `pending_action = "offer_quiz"` when `ok == True`. Failed turns are logged as `mode: "CHAT"` so the sidebar's "Concepts explored" stays honest and no phantom quiz is offered.
- `_handle_answer` wraps `grade_answer` in try/except and detects an `error` key on the verdict dict. Failed grades show a friendly retry message and DO NOT update mastery (no fake "not_yet" entries).
- Polisher prompt rewritten to emit visually scannable markdown: `### Scenario` / `### Formal Restatement` / `### Self-Check Question` H3 headers, bulleted **Mapping:** list, `> blockquote` for the breakdown sentence and the hint, a `**Where:**` bulleted symbol glossary under the standalone equation, and `---` horizontal rules between sections.

### Why
Three bugs the student reported in one message: pipeline frequently said "Internal error"; the quiz offer appeared after errors (no concept had been taught); the explanation was a wall of prose.

### Learned
- "Fail open" beats "fail loud" for non-critical agents in an interactive chat. The critic is a quality gate, not a correctness gate — a failed critic should not blank the student's lesson.
- Returning `(text, ok)` from a reply generator is cleaner than special-casing error strings downstream. The caller decides what to do with failure; the function just reports it.
- Markdown layout dramatically improves perceived quality even when the underlying content is unchanged. `###` headers + bullets + blockquotes turn a 600-word wall of text into a 10-second skim.

## 2026-06-15: Curriculum spine (data-driven curriculum)

### Changed
- `src/curriculum/__init__.py` — package marker.
- `src/curriculum/schema.py` — Pydantic models `Subject → Unit → Chapter → Concept`. `Concept` fields: `id`, `name`, `chapter_id`, `prerequisites: list[str]`, `learning_objective`, `bloom_target` (a `BloomLevel` Enum), `order: int >= 1`. Parent ids are stamped on children by the loader, not authored by hand.
- `src/curriculum/loader.py` — `load_subject(path)`, `all_concepts(subject)`, `teaching_order(subject)` (sorted by `order`), `resolve_prerequisites(concept_id, subject, transitive=)` (direct or recursive), `validate_ordering(subject)` (catches "concept before its prereq" AND cycles in one pass). `_inject_parent_ids` walks the YAML tree and copies `subject_id`/`unit_id`/`chapter_id` onto children so authors don't repeat themselves.
- `data/curriculum/physics.yaml` — Subject "Physics" → Unit "Kinematics" → Chapter "Motion in a Straight Line" with 9 concepts (position → distance/displacement → speed/velocity → average-vs-instantaneous + acceleration → equations of motion + relative velocity 1D). Each concept has a prereq list, an observable-action learning objective in my own words, and a Bloom target.
- `tests/test_curriculum.py` — loads physics.yaml, prints the teaching order with prereqs and objectives, verifies prereqs are respected, and spot-checks `resolve_prerequisites` (direct vs transitive) for `equations_of_motion`.
- `requirements.txt` — added `pyyaml` explicitly (was already a transitive dep via chromadb, but worth pinning).

### Why
EcoLearn is becoming a learning platform, not just a chatbot. A platform needs a stable, queryable curriculum spine that the rest of the system (lesson planner, mastery tracker, recommendations) can build on. YAML lets non-programmers author content; Pydantic guards the schema; the loader translates that into typed Python objects with prereq-respecting ordering.

### Learned
- **One source of truth, two representations.** YAML for authoring, Pydantic for runtime. The loader is the single boundary; nothing else in the codebase reads YAML directly. This is the "parse, don't validate" pattern: catch every authoring error at startup, then everyone downstream gets typed objects with no `dict[str, Any]` surprises.
- **A correct simple check beats a clever broken one.** I initially wrote a stack-based cycle detector and it false-positived on the first run. Realised the existing "no concept before its prereq in the declared order" loop already catches cycles transitively — in any cycle, at least one node will be reached before its prereq is seen. Deleted the bespoke detector; the simple check covers it.
- **Inject parent ids in the loader, not in YAML.** Forcing the author to repeat `chapter_id: motion_straight_line` on every concept under a chapter is noisy and error-prone. Letting the loader walk the tree and stamp ids keeps the YAML clean and the Pydantic schema strict.
- **Bloom targets stay strings (Enum), not numbers.** A learning objective expressed as `apply` reads cleanly; `5` doesn't. Pydantic's `BloomLevel(str, Enum)` accepts strings, validates them, and renders them back as strings. Best of both worlds.

## 2026-06-12: Phase 2 — offline lesson generation (content factory)

### Changed
- `src/content/lesson_schema.py` — `Lesson` Pydantic model: `concept_id`, `interest`, `body`, `worked_example`, `check_question`, and a `LessonMetadata` sub-model (`generated_at`, `critic_passed`, `critic_verdict`, `attempts`, `critic_feedback`).
- `src/content/generate_lessons.py` — `generate_all_lessons(chapter_id, interests, level, max_retries, skip_existing)`: for every concept × interest in a chapter, runs the existing `explain_with_review` pipeline (RAG → analogy generator → critic → retry), then saves `data/lessons/{concept_id}__{interest}.json`. On a non-passing critic verdict the lesson is still saved but `critic_passed=False`.
- Made the run **resumable and idempotent**: `skip_existing=True` skips any pair already on disk; `flagged.jsonl` and the run summary are **rebuilt from disk** (`_rebuild_flagged_log`, `_summarize_from_disk`) at the end instead of appended per-run, so partial/interrupted runs never produce duplicate flag entries or miscounts.
- Per-pair pipeline exceptions are now caught and skipped (one hung/disconnected generate call no longer kills the whole batch).

### Why
EcoLearn is moving from live per-student generation to a pre-generated content library. Generating offline lets every lesson be vetted by the critic once, cached, and served instantly — instead of paying 30–60 s and quota on every student view.

### Learned
- **Idempotent batch jobs beat fragile ones.** First run got interrupted by a hanging Gemma generate call; rather than restart from zero, making the job skip-existing + rebuild-state-from-disk turned a 6-hour-of-quota job into something you can stop and resume freely.
- **Rebuild derived state from the source of truth, don't append.** Appending to `flagged.jsonl` per-run accumulated duplicates across runs. Scanning the saved JSONs and rewriting the log makes it always consistent with what's actually on disk.
- **Critic quota exhaustion silently degrades quality, not availability.** Because the critic fails open (soft-PASS), the factory keeps producing lessons — but they're unvetted. Recording `critic_passed=False` for soft-passes preserves the distinction so a later re-vet pass can target exactly those.
- **The Gemma generation endpoint hangs intermittently.** Two separate generate calls stalled with no response / "Server disconnected". Per-pair exception handling is essential for an unattended batch.

### Run status (this session)
- 9/18 lessons saved for Motion in a Straight Line (football + gaming): 2 passed (position ×2), 7 flagged (critic quota was exhausted), 9 still missing. Critic quota reset partway through. Resume planned ~3 hrs later when quota is fresh.

## 2026-06-13: Lesson factory — the missing polisher (critical fix)

### Changed
- **Found a serious bug in the Phase 2 factory.** `generate_lessons.py` saved the *raw* generator output straight into `Lesson.body` — full Gemma scratchpad (drafts, "Word count: ~350, I need to expand", revised versions) — with `worked_example` and `check_question` empty. The factory called `explain_with_review()` (which returns raw text) but never ran the **polisher** that `app.py` uses to clean live replies. Every one of the first 18 lessons was unservable.
- `src/agents/polisher.py` (new) — extracted `polish_explanation` + the extractor system prompt out of `app.py` into a shared module. `app.py` now imports it (kept the `_polish_explanation` alias for existing call sites). Single source of truth for polishing across the live app and the offline factory.
- `src/content/generate_lessons.py` — `_build_lesson` now polishes before `_parse_sections`, so future runs split cleanly into the three fields. Added `repolish_existing()`: an idempotent, resumable repair pass that polishes lessons saved with raw bodies in place (detects them via empty worked_example/check_question), re-splits, and rewrites — skipping ones already clean and leaving raw bodies untouched on a polish fail-open so a later run retries. Added `_strip_trailing_rule` to drop the dangling `---` the section split left behind, applied to both freshly-split and already-clean lessons. New `repolish` CLI subcommand.

### Why
The whole point of the project's three-layer anti-leak defence is that **layer 3 (the LLM polisher) is the only one that reliably works**. The factory shipped without it and reintroduced exactly the scratchpad-leak problem the project spent days solving. The repair pass fixes the 18 already-generated lessons without paying to regenerate them — the raw bodies on disk already contain all the content.

### Learned
- **A new code path must reuse the proven cleanup, not reinvent it.** I first wrote a regex `_parse_sections` to split raw output — the exact "regex vs an LLM that invents new scratchpad labels" losing race the LOG already warned against. It fell through to its fallback on every lesson. The fix was to run the polisher *first*, then split its clean `###`-headed markdown.
- **Polish, then parse.** Order matters: the parser can only split clean section headers, which only exist after the polisher has extracted them.
- **Gemma is a poor polisher (2/11 success).** With the polisher at temperature 0.0, Gemma-4-31b-it produced cleanly-splittable output for only 2 of 11 lessons (the short `position` pair); the other 9 fail-opened. Confirms flash-lite is the right tool — Gemma leaks even when asked only to extract. (Quota note: flash-lite's 20/day bucket was exhausted by the resume run's critic calls + 6 polishes, which is why the Gemma attempt happened at all.)
- **Idempotent repair beats regenerate.** Re-polishing stored raw bodies costs one cheap polish call each vs a full RAG+generate+critic cycle. Detect-broken-by-signature (empty sections) + skip-clean + fail-open-preserves-raw makes the pass safe to run repeatedly across quota windows.

### Status
- Polisher fix verified working (clean body/worked_example/check_question, proper KaTeX). 9/18 lessons now clean (7 via flash-lite, 2 via Gemma); 9 still raw, blocked on flash-lite daily quota. Finish the remaining 9 by re-running `python -m src.content.generate_lessons repolish` after the flash-lite reset.

## 2026-06-13: Phase 3 — Learning Path Engine + progress store

### Changed
- `src/progress/store.py` (new) — SQLite progress store. One row per (student_id, concept_id): status, best_score, attempts, last_seen. `get_progress`, `update_progress` (upsert mirroring app.py's `_update_mastery`: attempts+1, best_score=max, status from best), `get_mastered_concepts`, plus `mark_reviewed` (refresh last_seen only, for reviews). Status thresholds (`status_from_score`) identical to app.py so the live session ledger and the persisted store never disagree. DB path is read lazily from `ECOLEARN_PROGRESS_DB` (default `data/progress.db`) so tests can point at a temp file.
- `src/path/engine.py` (new) — the path engine. `next_concept(student_id, chapter_id)` returns a `Recommendation(kind, concept, reason)` where kind ∈ new/review/done/blocked. Policy: (1) spaced repetition — a mastered concept unrevisited for ≥ `ECOLEARN_REVIEW_DAYS` (default 7) is surfaced for review first; (2) else the first not-mastered concept in teaching order whose prerequisites are all mastered; (3) else done (all mastered) or blocked (names the unmet prereqs). `get_roadmap(...)` tags every chapter concept mastered/available/locked with missing-prereq ids and progress detail for the future roadmap UI. Reuses `load_subject`, `teaching_order`, `resolve_prerequisites` from the curriculum spine; mastery from the store.
- `src/progress/__init__.py`, `src/path/__init__.py` — package markers.
- `tests/test_path_engine.py` (new) — three scenarios against a throwaway temp DB: (1) master all 9 concepts one at a time, asserting at every step that the recommended concept's *transitive* prerequisites are already mastered (the core invariant — zero violations); (2) roadmap for a partial student; (3) back-date a mastered concept's last_seen and confirm the review path fires. All pass.
- `.gitignore` — added `data/progress.db` (per-user runtime state, like chroma_db/).

### Why
The platform needed to stop being reactive (student types a concept → we teach it) and become proactive (the system knows what each student should learn next and why). That requires durable per-student progress (the store) and a rule that combines progress with the prerequisite-ordered curriculum (the engine).

### Learned
- **The engine invents no pedagogy.** Ordering and prerequisites come from the curriculum spine; mastery from the store. The engine is purely the rule that joins them — which keeps all three pieces independently testable and means content authors (YAML) change behaviour without touching engine code.
- **Inject `now` for time-dependent logic.** Spaced repetition depends on wall-clock time; passing `now` as a parameter (default `datetime.now`) made the review path deterministically testable without freezing the system clock.
- **Lazy env-var config beats wide function signatures for testability.** Reading `ECOLEARN_PROGRESS_DB` inside `_connect()` (not at import) lets the test redirect the whole store to a temp DB with one `os.environ` line — no `db_path=` threaded through every function.
- **Mirror, don't fork, the status logic.** Re-deriving `status_from_score` in the store with the same 3/2/else thresholds as app.py avoids the classic bug where the persisted "mastered" and the UI "mastered" drift apart. (Worth a later refactor to import one shared function.)

### Status
Phase 3 complete and tested. Not yet wired into app.py — the live UI still uses the in-session `st.session_state.mastery`; connecting it to the persistent store + showing a roadmap is the natural next step.

## 2026-06-13: Phase 4 — platform service layer (the API boundary)

### Changed
- `src/platform_api.py` (new) — the single service boundary every frontend calls. Exactly five functions: `create_or_load_student(name, interest, level)`, `get_roadmap(student_id, chapter_id)`, `get_next_lesson(student_id, chapter_id)`, `submit_assessment(student_id, concept_id, answer)`, `ask_help(student_id, concept_id, question)`. They orchestrate the path engine, lesson read-service, progress store, assessor, and live pipeline internally. **Every return value is plain JSON-serializable data** (dict / list of dict / primitives) — no Pydantic models or dataclasses cross the boundary.
- `src/content/lesson_service.py` (new) — read side of the lesson factory: `get_lesson(concept_id, interest)` loads `data/lessons/{concept_id}__{interest}.json` (lower-cases interest to match factory filenames), `has_lesson`, `lesson_path`.
- `src/progress/store.py` — added a `students` table and `get_student` / `save_student` (upsert; `created_at` preserved across updates). Same DB file as progress, so the `ECOLEARN_PROGRESS_DB` override covers both.
- `src/path/engine.py` — added public `find_concept(concept_id)` so the service layer can fetch concept metadata (name, objective) without re-loading the subject itself.
- `tests/test_platform_api.py` (new) — full student journey through ONLY `src.platform_api` (the sole domain import): create student → roadmap → next lesson → submit assessment (live grade) → ask help (live pipeline) → next lesson. Asserts the contract at each step and that the engine stays prerequisite-correct. **Ran green:** grade scored 3→mastered, the help pipeline did a real FAIL→regenerate→PASS and returned polished markdown, and step 6 advanced position→distance.
- `.gitignore` — added `platform_test.log`.

### Why
The platform had four working subsystems (curriculum, lessons, path engine, live pipeline) but no front door. Without a boundary, a frontend would reach into all of them and couple itself to their internals — making a Streamlit→Next.js move a rewrite. One service layer that returns plain data decouples *what the platform does* from *how any UI renders it*.

### Design decisions (don't re-debate)
- **The assessment IS the lesson's self-check.** `submit_assessment` grades the answer against the concept's pre-generated lesson `check_question` (anchored with the concept name + learning objective as expected concepts), rather than generating a fresh question. One question the student actually saw; one grade.
- **`ask_help` is the only live/expensive call in the API** and runs the full pipeline with `max_retries=1` (one critic-driven retry) to stay responsive. Cached lessons serve everything else instantly.
- **`student_id` is a deterministic slug of the name** (`"Journey Student"` → `journey-student`), so `create_or_load_student` is idempotent — same name reloads the same student, refreshing interest/level.
- **Plain-data returns are a hard rule**, not a style choice — it's what makes the boundary transport-agnostic (see takeaway below).

### Learned
- **A boundary test that imports only the boundary is the proof the boundary works.** `test_platform_api.py` has exactly one domain import (`platform_api`); the fact that a complete journey is expressible through it is the design validated.
- **Returning Pydantic objects would have leaked the abstraction.** Calling `.model_dump()` at the boundary (lessons) and returning dicts everywhere means an HTTP layer can serialize results with `json.dumps` and no custom encoders — the precondition for a non-Python frontend.

### Status
Phases 1–4 complete. The service layer is ready for a frontend; `app.py` still talks to subsystems directly and should be refactored to call `platform_api` (Phase 5-ish), at which point Streamlit and a future Next.js app share identical logic.

## 2026-06-13: Phase 5 — multi-page Streamlit platform

### Changed
- `app.py` — **rewritten** as the onboarding landing page of a multi-page app (was the single-page chatbot). Form (name / interest / level) → `create_or_load_student` → stores `student_id` + `profile` in `st.session_state` → `st.switch_page` to the roadmap. Welcome-back branch with page links + "start over".
- `pages/1_Roadmap.py` — visual roadmap via `get_roadmap`: progress bar + one coloured card per concept (mastered green / available blue / locked grey, left-border colour), missing prereqs on locked cards, "Continue learning" → lesson.
- `pages/2_Lesson.py` — personalised lesson via `get_next_lesson`: Scenario (body) + Formal restatement (worked_example) as markdown/KaTeX, handles done/blocked/lesson_missing states, and a persistent "I'm stuck — ask for help" box that calls `ask_help` and shows the reply inline (stashed in session so it survives reruns) without leaving the page.
- `pages/3_Assessment.py` — shows the lesson `check_question` via `get_next_lesson`, takes an answer, calls `submit_assessment`, shows score/feedback/mastery; persisted grade means the roadmap reflects it.
- `ui_common.py` — shared presentation/session helpers (CSS, `setup_page`, `require_student`, status badges/cards, CHAPTER constants). Imports NOTHING from platform internals — keeps the "UI talks only to platform_api for data" rule clean.
- `legacy_chat_app.py` — the previous single-page chatbot, preserved verbatim (`streamlit run legacy_chat_app.py`) so nothing is lost.
- `.claude/launch.json` — preview-server config for the app (port 8502).

### Why
The platform_api boundary (Phase 4) needed a real frontend that respects it. A multi-page app — onboarding → roadmap → lesson → assessment — is the natural shape, and building it strictly on the five API functions is the proof the boundary is usable.

### Verified
- **Audit:** every UI file's only `src` import is `from src import platform_api as api`; calls used are exactly create_or_load_student / get_roadmap / get_next_lesson / ask_help / submit_assessment. `ui_common` has no domain import.
- **Live walkthrough** (preview MCP, port 8502): onboarding form → submit creates student → switch_page to roadmap (0/9, position available, rest locked with correct prereqs) → lesson (scenario + formal restatement + KaTeX glossary + help box) → assessment (check question + KaTeX hint). All four pages render correctly; sidebar auto-nav lists all pages.
- Live grade hit a transient Gemma `ServerError` twice during the walkthrough; the UI degraded gracefully ("Couldn't grade that right now…") with no crash. The grade path itself is proven by the green `test_platform_api.py` (score 3 → mastered).

### Learned
- **Streamlit multipage = one entry script + a `pages/` dir.** `streamlit run app.py` auto-discovers `pages/*.py` into the sidebar nav, ordered by numeric filename prefix (`1_Roadmap.py` → "Roadmap"). `st.switch_page("pages/..")` navigates programmatically; `st.session_state` is shared across pages within a session, which is what carries `student_id`.
- **Streamlit's React-controlled inputs resist DOM automation.** `preview_fill` / plain selectors didn't register; the working approach was the native value-setter + dispatched `input` event via `preview_eval`. Worth remembering for any future UI automation here.
- **The boundary made the UI thin and dumb — by design.** Each page is ~60-90 lines of "call one or two API functions, render the returned dict." No decisions live in the UI, which is exactly why a Next.js rewrite would touch zero logic.

### Status
Phases 1-5 complete. EcoLearn is now a working multi-page platform over a clean API boundary. The old chatbot lives on as `legacy_chat_app.py`.

## Cross-cutting takeaways (rollup)

Things that keep proving true across this project:

- **Quota is the binding constraint.** Every model on the Gemini API has its own daily bucket. Production-grade reliability on the free tier means a portfolio of models across tasks (Gemma for generation, Gemini-Lite for critique/polish, ONNX-local for embeddings) so a single bucket drying up doesn't take the whole app down.
- **Prompt files (`.txt`) > prompts-in-code.** Every tightening this stretch was a text edit. No code review, no rebuild, trivial revert. The cost of pulling prompts back into Python is paid every iteration; the savings are huge.
- **Reasoning-trained models leak scratch by default.** Three layers fight this: (1) explicit "no scratch" in the system prompt, (2) a regex sanitizer that slices canonical markers, (3) a cheap LLM polisher that extracts the final answer regardless of mess. Layer 3 is the only one that works reliably.
- **Strict JSON + low temperature + small model = reliable judges.** Critic, assessor, router, polisher, intent classifier — all of them. Splitting the creative-large-temperature path from the structured-cheap-judgement path is a free win in cost, latency, and consistency.
- **In a reactive UI, long-running work never lives in a button handler.** State-flip + rerun + worker-in-next-render is the only pattern that survives users clicking twice.
- **Fail open on judges, fail loud on inputs.** A failed critic / grader / polisher shouldn't kill the lesson — degrade gracefully and ship something. A missing API key or invalid model ID, on the other hand, must surface immediately with a clear cause.
