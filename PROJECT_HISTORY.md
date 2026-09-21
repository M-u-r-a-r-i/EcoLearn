# EcoLearn — Project History

> **What this file is.** The single record of everything EcoLearn is and how it got here:
> current state, architecture as actually built, every commit explained, the decisions behind
> the design, and the lessons that cost real time to learn. It replaces the separate working
> log, AI-context brief, handoff notes, gap analysis, and presentation dump that used to live
> at the repo root.
>
> **Companion file:** [`ROADMAP.md`](ROADMAP.md) — everything still to be done (the v2 plan).
> **Evaluator-facing overview:** [`README.md`](README.md).
>
> History closes at: **2026-09-21**. Repo: github.com/Niranjan-207/EcoLearn, branch `main` (fresh
> history from 2026-09-21; the original 44 commits in §8 live in the teammate's repo).

---

## 1. What EcoLearn is

A **personalised AI tutor for CBSE/ISC Class 11 Physics (Kinematics)**. A student picks an
interest — **football** or **gaming** — and every concept is taught through analogies grounded
in that interest, with the physics kept correct by an automated critic.

It began as a Streamlit chatbot, became a data-driven platform behind a clean service boundary,
and is now a full-stack app: **FastAPI + Next.js**, with **Streamlit kept as a legacy UI** over
the same backend.

The single most important architectural fact:

> **All logic lives behind one module — `src/platform_api.py` — which returns plain
> JSON-serializable dicts. Every frontend calls only that boundary.**

That is why adding the entire web stack required **zero changes to business logic**.

**On the name:** the project is a *physics* tutor despite "EcoLearn" (eco). The name is a
historical holdover from an abandoned sustainability-education concept. Not worth renaming.

---

## 2. Where the project stands today

| Area | Status |
|---|---|
| Curriculum spine (YAML → Pydantic, global ordering, prereq validation) | ✅ Complete, tested |
| Learning path engine (static prereq gating + spaced review) | ✅ Complete, tested |
| SQLite progress store | ✅ Complete, tested |
| Offline lesson factory (generate → critic → retry → polish) | ✅ Complete |
| Multi-agent live pipeline + RAG | ✅ Complete |
| Content: 2 chapters, 17 concepts, **34 lessons** (football + gaming) | ✅ Committed to the repo |
| Service boundary (`platform_api`, 6 functions) | ✅ Complete |
| FastAPI layer (health + 5 endpoints) | ✅ Working (`list_chapters` not exposed) |
| Next.js web app (landing → onboarding → roadmap → lesson → assessment) | ✅ Full journey verified end-to-end |
| Streamlit legacy UI | ✅ Complete |
| Accounts / auth | 🟡 **In progress** — backend core done + tested, HTTP layer and UI not started (§9) |
| Learner model (per-skill mastery, misconceptions) | 🔴 Not started — the v2 core |
| Adaptive sequencing | 🔴 Static only today |
| Multi-format lessons | 🔴 One fixed template today |

**Known gaps as of this writing:**
- Student identity lives in in-memory React Context — **lost on a hard refresh** (progress
  itself is safe in the DB, keyed by `student_id`).
- Chapter is **hardcoded** `motion_straight_line` in three web pages, so the already-built
  Chapter 2 (`motion_plane`) is unreachable from the web UI.
- Dark mode in the web app is untouched shadcn neutral defaults — the brand tokens
  (`--brand-accent`, `--success`) aren't redefined for `.dark`.
- `web/lib/api.ts` repeats its fetch/error boilerplate five times and leaks
  `localhost:8000` into user-facing error text.
- CORS is dev-only (`localhost:3000`). No auth on any endpoint.
- The analogy generator has no model fallback chain (assessor and polisher do).

**Latent issues that only bite at scale** (found by the 2026-09-21 scale-up audit; each is
scheduled in `ROADMAP.md` §6–§6c):
- 🔴 **Duplicate concept ids silently overwrite.** `_by_id()` in `src/curriculum/loader.py` is a
  dict comprehension — last one wins, no error. With lessons named
  `{concept_id}__{interest}.json`, a duplicate also silently overwrites a lesson file. Harmless at
  17 concepts; likely at 250.
- The path engine **ignores the student's `level`** — it only reaches the generator — so nothing
  distinguishes Class 11 from Class 12 content. The schema has no grade field.
- `_load_subject()` in `src/path/engine.py` **re-reads and re-validates the YAML on every call**
  (no caching), several times per request.
- `retrieve_concept()` in `src/rag/retrieve.py` searches the **whole** curriculum collection with
  no chapter filter — fine for kinematics, ambiguous across 28 chapters.
- **The interest corpora are 100% mechanics.** `football.md` and `gaming.md` hold 20 passages each
  on speeds, trajectories and friction — nothing that could ground an electricity, optics or
  thermodynamics analogy.
- Both few-shot examples in `prompts/analogy_generator.txt` are mechanics.
- The lesson factory's CLI hardcodes chapter 1 and both interests; pacing sleeps (13 s per step,
  5 s per lesson) are hardcoded for the free tier.
- **There is no interest registry.** Interest is free text, checked only for being non-blank, and
  `football`/`gaming` are hardcoded separately in the web onboarding page, the Streamlit
  onboarding, and the factory CLI. An interest that exists in one place but not another silently
  gets `lesson_missing` on every concept.
- **There is no shared LLM layer.** Each of the four agents imports `google.genai`, builds its own
  client, and applies Gemini-only options inline (`response_mime_type` for JSON,
  `thinking_config`). Changing provider means editing four copies of the same logic.

---

## 3. Architecture as built

```
  🐍 Streamlit UI                    ⚛️ Next.js UI (web/)
  app.py · pages/ · src/ui                 │  fetch() over HTTP (JSON)
        │                                   ▼
        │                        🚪 FastAPI (api/main.py)  ── thin HTTP wrapper
        │                                   │
        └──────────── both call ───────────┴────────────▶  src/platform_api.py
                                                                   │ orchestrates
             ┌──────────────┬──────────────┬───────────────┬──────────────┐
             ▼              ▼              ▼               ▼              ▼
        path engine     progress        lesson       live pipeline   curriculum
        (what next)      store         service      (gen→critic→      (YAML →
                        (SQLite)       (cached)       retry→polish)   typed objs)
```

### The two content paths (deliberate)

- ⚡ **Cached lessons** — pre-generated offline, critic-vetted once, served instantly from disk
  with **no LLM call**. Covers the roadmap, the lesson body, and the check question.
- 🔴 **Live pipeline** — **only** for "ask for help" (the doubt chat) and **grading on submit**.
  These are the only slow/online calls; help has been measured at ~2 minutes.

This split is the entire cost/quota strategy. Preserve it.

### The AI pipeline

```
RAG retrieve (ChromaDB) → Analogy Generator (Gemma) → Critic (Gemini, strict JSON)
   → on FAIL feed feedback back & regenerate → Polisher (Gemini → clean markdown/KaTeX)
Assessor (Gemma): generates and grades the self-check question.
```

---

## 4. The service boundary — `src/platform_api.py`

Every return value is plain dict/list/primitive. **No Pydantic objects cross this line.**

| Function | Returns |
|---|---|
| `create_or_load_student(name, interest, level)` | `{student_id, name, interest, level, created_at}` |
| `list_chapters()` | `[{id, name}, ...]` |
| `get_roadmap(student_id, chapter_id)` | `[{concept_id, name, order, status, progress_status, best_score, attempts, missing_prerequisites}, ...]` |
| `get_next_lesson(student_id, chapter_id, concept_id=None)` | `{status(new\|review\|done\|blocked\|lesson_missing), reason, concept_id, concept_name, lesson\|null}` |
| `submit_assessment(student_id, concept_id, answer)` | `{concept_id, score(0-3), mastery_signal, feedback, missing_concepts, graded_question, mastery{...}}` — **raises** on grader failure rather than writing a fake 0 |
| `ask_help(student_id, concept_id, question)` | `{concept_id, concept_name, answer(markdown), verdict, attempts}` — the live pipeline |

Plus the account functions added in the in-progress auth work (§9).

### HTTP layer — `api/main.py`

Run from the project root so `src` resolves: `uvicorn api.main:app --reload --port 8000`.
Docs at `/docs`. CORS allows `http://localhost:3000`.

| Method + path | → boundary fn |
|---|---|
| `GET /` | health check |
| `POST /api/student` | `create_or_load_student` |
| `GET /api/roadmap` | `get_roadmap` |
| `GET /api/next-lesson` | `get_next_lesson` |
| `POST /api/assessment` | `submit_assessment` |
| `POST /api/help` | `ask_help` |

FastAPI's `jsonable_encoder` converts the `datetime` in `metadata.generated_at` to an ISO
string automatically — so "JSON-serializable via FastAPI" is broader than `json.dumps`-able,
and the boundary needed no change.

---

## 5. Data model and the mastery rules

**Curriculum** — `data/curriculum/physics.yaml`: Physics → Kinematics → 2 chapters.
`motion_straight_line` (concepts order 1–9) and `motion_plane` (order 10–17, with
cross-chapter prerequisites back into chapter 1).

> **`order` is GLOBAL across the subject**, not per-chapter. A new chapter must continue the
> numbering (18, 19, …) or the global teaching-order sort interleaves chapters and
> `validate_ordering` rejects the cross-chapter prerequisites.

**Lessons** — `data/lessons/{concept_id}__{interest}.json`, schema `concept_id, interest, body,
worked_example, check_question, metadata{generated_at, critic_passed, critic_verdict, attempts,
critic_feedback}`. Bodies are markdown with KaTeX math (polisher output).
`data/lessons/flagged.jsonl` is the critic audit trail, rebuilt from disk on each factory run.

**Progress** — SQLite at `data/progress.db` (gitignored; override with `ECOLEARN_PROGRESS_DB`).
Two tables: `students` and `progress` (one row per student × concept).

**The mastery split (a real design decision):**
- **`cleared`** = `best_score >= 2` → drives **progression** and unlocks dependent concepts.
- **`mastered`** = `3/3` → the gold badge and spaced-repetition review.
- A 2/3 therefore offers a *choice* ("move on" vs "practise again") instead of a dead end.
- Roadmap status ∈ `mastered` / `available` / `locked`.

---

## 6. Models and the quota reality (the binding constraint)

`.env` sets `GEMINI_MODEL=gemma-4-31b-it`; everything else uses code defaults.

| Role | Model | Notes |
|---|---|---|
| Generator | `gemma-4-31b-it` | temp 0.7 |
| Critic | `gemini-2.5-flash-lite` | strict JSON; **fails open** (soft-PASS carrying the error) |
| Polisher | `gemini-2.5-flash-lite` | clean markdown; **fallback chain** |
| Assessor | `gemma-4-31b-it` | **fallback chain** |
| Embeddings | `all-MiniLM-L6-v2` (ONNX, local) | no API, no quota |

Facts learned the hard way: each model has its **own ~20/day free-tier bucket**;
`gemma-3-27b-it` 404s on the dev key (only `gemma-4-31b-it` works); `gemma-4-31b-it` shows
intermittent `500 INTERNAL` and occasionally **hangs outright**. Fallback chains plus
judges-fail-open keep the app alive. The whole pre-generate-and-cache design exists because
of this constraint.

> ### ⚠️ Gemma API constraint — do not "clean this up"
> **Gemma models do not accept `system_instruction` or `thinking_config`.** The agents therefore
> **prepend the system prompt to the user message** instead of passing it as a separate field
> (see `src/agents/analogy_generator.py` and `src/agents/assessor.py`). This looks like an
> oversight and is not: re-adding those config fields silently breaks generation on Gemma.
> `GEMINI_THINKING_BUDGET` is likewise applied *only* when the model id starts with
> `gemini-2.5-flash`. Check model compatibility before touching any `genai` call config.

---

## 7. Repo map

```
BACKEND (shared)
  src/platform_api.py            the service boundary
  src/errors.py                  EcoLearnError/NotFoundError/ConflictError/AuthError
  src/auth/passwords.py          bcrypt hashing + the 72-byte guard
  src/curriculum/{schema,loader}.py   Pydantic models + YAML loader (global order, validation)
  src/path/engine.py             next_concept, get_roadmap, list_chapters, find_concept
  src/progress/store.py          SQLite: students + progress (+ account columns)
  src/content/{lesson_schema,lesson_service,generate_lessons}.py   cached lessons + factory
  src/agents/{analogy_generator,critic,assessor,polisher}.py
  src/pipeline.py                explain_with_review (RAG → gen → critic → retry)
  src/rag/{ingest,build_index,retrieve}.py    ChromaDB, local embeddings
  src/data/{curriculum,interests}/*.md        the RAG corpora (source text)
  prompts/{analogy_generator,critic,assessor}.txt

WEB API
  api/main.py                    thin FastAPI over the boundary

NEXT.JS (web/)  — the primary frontend
  app/{page,layout,globals.css} + app/{onboarding,roadmap,lesson,assessment}/page.tsx
  components/{site-nav,page-container,section-heading,primary-button,markdown,
              help-widget,student-provider}.tsx + components/ui/* (shadcn)
  lib/{api,utils}.ts

STREAMLIT (legacy)
  app.py, pages/{1_Roadmap,2_Lesson,3_Assessment}.py, ui_common.py, src/ui/theme.py
  .streamlit/config.toml

DATA / CONTENT
  data/curriculum/physics.yaml   2 chapters, 17 concepts
  data/lessons/*.json            34 pre-generated lessons + flagged.jsonl

TESTS (standalone scripts, NOT pytest)
  tests/test_{curriculum,path_engine,edge_states,scale_chapter2,persistence}.py   deterministic
  tests/test_{platform_api,analogy,critic,assessor,pipeline,retrieval}.py         live LLM
  tests/benchmark_{analogy,v3}.py                                                prompt benchmarks

DEV TOOLS
  iterate.py                     single-case pipeline runner for prompt tuning

NOT IN GIT (local only): venv/, .env, web/node_modules/, web/.env.local,
  chroma_db/ (rebuild: python src/rag/build_index.py), data/progress.db
```

---

## 8. Development history — all 44 commits explained

Many commit messages are `.`, `Updated Readme`, or misleading. This table reconstructs what
each commit actually changed, from its diff. Branches: `master` (full stack),
`streamlit-version` (preserved Streamlit-only state), `ui-improvements`, `auth-and-ux` (current).

### Phase 1 — Setup and the first agent (May 22 – Jun 4)

| Commit | Date | What it actually did |
|---|---|---|
| `fbe087a` | 05-22 | Project skeleton: venv layout, `requirements.txt`, `.env` template, `.gitignore`, README, empty package markers for `src/agents`, `src/data/{curriculum,interests}`, `prompts`, `tests`. |
| `bf7113c` | 06-01 | **Provider switch: Anthropic Claude → Google Gemini.** A two-line diff (requirements + README) but the decision that shaped everything after it. |
| `571eb75` | 06-01 | `src/test_api.py` — first live API call, a "does my key work" script. |
| `444387d` | 06-01 | `prompts/analogy_generator.txt` (115 lines) — **the prompt was written before any agent code.** Structural-mapping discipline: element correspondence, relation preservation, honest breakdown, required mapping table, self-rating, two few-shot examples. |
| `82e7912` | 06-04 | `src/agents/analogy_generator.py` + `tests/test_analogy.py` + a 10-case benchmark harness with 429 retry. Env-configurable model/tokens/thinking-budget. |
| `f3a23f1` | 06-04 | Refreshed benchmark output after prompt tuning. |

### Phase 2 — Critic, pipeline, RAG (Jun 6 – Jun 7)

| Commit | Date | What it actually did |
|---|---|---|
| `af2919d` | 06-06 | **The Critic and the pipeline.** `src/agents/critic.py` (strict JSON: verdict + scientific_correctness + pedagogical_fit + analogical_integrity + feedback), `prompts/critic.txt` (three-axis rubric with "DO NOT fail for X" calibration), `src/pipeline.py` → `explain_with_review()` (generate → critique → feed feedback back → regenerate), `iterate.py`, two test scripts. |
| `d354bbf` | 06-06 | *(message: ".")* Anti-scratchpad prompt hardening — two explicit "output only the final answer" blocks, because Gemma was leaking planning notes, length checks and self-scoring into student-facing text. |
| `537ec9f` | 06-06 | Log catch-up + `testremote.py`, a side experiment against a remote Ollama (`llama3.2:3b`) over a Cloudflare tunnel. Abandoned. |
| `6c180d7` | 06-06 | **The corpora** — 22 NCERT-aligned curriculum passages (kinematics + work/energy) and 40 interest passages (football: Mbappé sprint speeds, free-kick Magnus effect, pitch friction; gaming: racing accel, hitscan vs ballistic, physics engines, Angry Birds projectiles). Written so each `##` heading is a self-contained chunk. |
| `189245c` | 06-06 | RAG ingestion — `src/rag/ingest.py` (split on `## ` headings, fall back to 250-token windows with 50 overlap, metadata `{source_file, heading, corpus_type, interest}`) + `build_index.py`. `chroma_db/` gitignored. |
| `fac79f3` | 06-07 | **RAG wired into the pipeline** — `retrieve.py` (`retrieve_concept`, `retrieve_interest` with a `where={"interest": …}` filter so football queries never return gaming passages), generator gains `curriculum_context`, prompt gains a "PROVIDED CONTEXT — source of truth" section, plus a v3 benchmark that saves retrieved passages alongside output so the diff vs v2 is auditable. |

### Phase 3 — Streamlit chatbot (Jun 7 – Jun 11)

| Commit | Date | What it actually did |
|---|---|---|
| `638399a` | 06-07 | `app.py` (375 lines) — Streamlit onboarding + chat, profile and history in `st.session_state`, live status line inside the assistant bubble via `st.empty()` + an `on_status` callback threaded through the pipeline. |
| `9cf2ae5` | 06-07 | **Math normalisation + the polisher idea.** A regex pre-clean plus a second cheap LLM call that extracts the final answer and converts Unicode (`θ ≈ ² √ ×`) to LaTeX, wrapping inline math in `$…$` and equations in `$$…$$` so KaTeX renders consistently. |
| `9038b7f` | 06-08 | **The Assessor** — `prompts/assessor.txt` with a two-mode dispatch (`generate_question` / `grade_answer`) and `src/agents/assessor.py`. Quiz flow in the chat: an `ASSESS` intent, `awaiting_answer` state, mastery ledger, sidebar pills. Max output tokens raised 1024 → 2048 because Gemma burned the budget on scratchpad before emitting JSON. |
| `e852392` | 06-11 | **Resilience pass.** Critic now **fails open** (soft-PASS carrying the error) so an exhausted quota degrades quality, not availability; friendly specific messages for rate-limit / empty-response / model-not-found; `(text, ok)` return so failed turns don't log phantom concepts or offer a quiz for a lesson that never rendered; failed grades don't write mastery. |

### Phase 4 — Becoming a platform (Jun 11 – Jun 14)

| Commit | Date | What it actually did |
|---|---|---|
| `e7c3e0e` | 06-11 | **The curriculum spine.** `src/curriculum/schema.py` (Pydantic `Subject → Unit → Chapter → Concept`, Bloom enum, `order >= 1`), `loader.py` (`load_subject`, `teaching_order`, `resolve_prerequisites` direct/transitive, `validate_ordering` catching both mis-ordering *and* cycles in one pass, `_inject_parent_ids` so authors don't repeat chapter ids), `data/curriculum/physics.yaml` with chapter 1's 9 concepts. |
| `53733fc` | 06-12 | *(message: ".")* Created `HANDOFF.md` architecture notes. |
| `30c7b89` | 06-13 | **The content factory + the polisher extracted.** `src/content/{lesson_schema,generate_lessons}.py` — resumable and idempotent (`skip_existing`, state rebuilt from disk rather than appended), per-pair exception handling so one hung Gemma call can't kill a batch. First 18 lessons committed. `src/agents/polisher.py` extracted out of `app.py` so the live app and the offline factory share one implementation — **after discovering the factory had shipped raw scratchpad into every lesson body because it never called the polisher.** |
| `c814070` | 06-13 | **Path engine + progress store.** `src/progress/store.py` (SQLite, lazy `ECOLEARN_PROGRESS_DB` resolution so tests can redirect it) and `src/path/engine.py` (`next_concept` policy: spaced review first → first learnable not-mastered concept → done/blocked). `tests/test_path_engine.py` asserts the core invariant at every step: the recommended concept's *transitive* prerequisites are already mastered. |
| `c5ce0aa` | 06-13 | **The service boundary.** `src/platform_api.py` (five functions, plain-dict returns), `src/content/lesson_service.py` (the read side of the factory), a `students` table, `engine.find_concept`, and `tests/test_platform_api.py` — a full journey whose *only* domain import is `platform_api`, which is the proof the boundary works. |
| `c22e453` | 06-13 | **Multi-page Streamlit platform.** `app.py` rewritten as onboarding, `pages/{1_Roadmap,2_Lesson,3_Assessment}.py`, `ui_common.py` shared helpers (no domain imports). The old chatbot preserved verbatim as `legacy_chat_app.py`. |
| `e666b25` | 06-13 | **Resilience + the 2/3 choice flow.** Assessor fallback chain (gemma `500` → flash-lite); no fake score-0 on grader failure; the **`cleared` (≥2) vs `mastered` (3/3)** split so a 2/3 isn't a dead end; `get_next_lesson(concept_id=…)` for "practise this again"; result-mode pinning so advancing lands on the next *lesson*; `tests/test_persistence.py` (two-process close/reopen) and `tests/test_edge_states.py`. |
| `5c09fba` | 06-14 | **Chapter 2 — the scale test.** 8 new concepts (`motion_plane`, order 10–17) with cross-chapter prerequisites, 16 lessons generated → **34 total**. Adding a whole chapter was **content-only for the entire backend**; the only code needed was a chapter *selector* in the UI plus a polisher fallback chain. |
| `eeb72ce` | 06-14 | Log update covering the resilience work and the scale test. |
| `ad59402` | 06-14 | Merge the curriculum branch into `master`, consolidating phases 1–7. |
| `b72e3af` | 06-14 | `.gitignore` update. |
| `8cd5609` | 06-14 | **Stopped tracking `LOG.md`.** This is why the dev log was absent from GitHub — and, indirectly, why commit messages degraded to `.`: the real narrative was going into an ignored file. |
| `f53b7f2` | 06-14 | **Streamlit design system.** `src/ui/theme.py` (palette, radii/shadow/spacing tokens, Inter, 960px max width, global CSS injection) + `.streamlit/config.toml`. Fixed two theming bugs: a global `font-family !important` had clobbered Streamlit's Material-Symbols icon ligatures (rendering `keyboard_double_arrow_left` as text), and a dark-mode OS made custom text invisible until a light base was pinned. |
| `4616fd9`, `df9675b`, `120dc78` | 06-14 | README rewritten as an evaluator-facing document (badges, TOC, ASCII diagrams, per-OS command tables, honest limitations) and `.env.example` added. |

### Phase 5 — FastAPI + Next.js migration (Jun 23 – Jul 2)

| Commit | Date | What it actually did |
|---|---|---|
| `3c26666` | 06-23 | `api/main.py` — thin FastAPI over the unchanged boundary: health check, `POST /api/student`, CORS for `localhost:3000`. Each endpoint is a ~3-line translation because the boundary already returns dicts. |
| `2c401bc` | 06-23 | The remaining four endpoints (roadmap, next-lesson, assessment, help). Reads take query params; writes take JSON bodies. |
| `23bb8a4` | 06-25 | **Next.js scaffold** — App Router, TypeScript, Tailwind v4, Next 16.2.9, React 19, Turbopack; shadcn/ui initialised (radix base, "nova" preset) with button/card/input/dialog/progress/badge. |
| `c09b903` | 06-25 | **Brand theme + layout components.** Brand palette written into shadcn's CSS variables (`--primary #4F46E5`, `--brand-accent #F59E0B`, `--success #10B981`, `--background #FAFAFB`) so every component inherits it; Inter via `next/font`; `site-nav`, `page-container`, `section-heading`, `primary-button`; the landing hero. |
| `d467e84` | 06-25 | **First frontend↔backend connection.** `lib/api.ts` (`createStudent`, `getRoadmap`), `student-provider.tsx` (in-memory React Context), the onboarding form, and the roadmap page as a vertical node path with a progress bar. Data fetched in `useEffect` because the input (`student_id`) is client-only state a Server Component can't read. |
| `eaf19a4` | 06-26 | **Lesson page + markdown stack.** react-markdown + remark-gfm + remark-math + rehype-katex + `@tailwindcss/typography`, wrapped in a reusable `<Markdown>` component. Backend text is markdown with KaTeX, so rendering it raw would have shown literal `**` and `$`. |
| `7bd7ede` | 06-30 | **The help widget** — the live multi-agent pipeline in the UI, with chat bubbles, an animated "Thinking…" state, auto-scroll, and in-place follow-ups. Measured live at ~2m3s for one answer. |
| `f6a345e` | 07-01 | **The assessment flow** — question → textarea → graded result card coloured by tier, with next actions branching on score ≥ 2. Verified live: a strong answer scored 3/3 and the roadmap then showed `position` mastered with `distance` unlocked. |
| `5775f56`, `fbbfd67`, `87da5b2`, `32921af` | 07-01/02 | README refreshed for full-stack status (Next.js promoted to primary, Streamlit demoted to legacy) and a final `.gitignore` tweak. |

*(Also created and later removed: `PROJECT_DEEP_DIVE.md`, an interview-prep technical breakdown.
Its useful findings — docstrings drifting from the code — are folded into this file.)*

---

## 9. In progress: accounts and auth (`auth-and-ux`, 2026-09-20/21)

Backend groundwork written but **not committed**:

- `src/errors.py` — `EcoLearnError(ValueError)` + `NotFoundError` / `ConflictError` / `AuthError`.
  All subclass `ValueError` so existing `except ValueError` callers don't regress, while the HTTP
  layer gains the precision to answer 404/409/401 instead of a flat 400.
- `src/auth/passwords.py` — bcrypt used **directly** (not passlib, which is unmaintained and
  breaks against modern bcrypt). Guards bcrypt's 72-**byte** limit, which bcrypt 5 raises on
  rather than silently truncating; `verify_password` never raises; `dummy_verify` burns an
  equivalent hash on the unknown-email path so login timing isn't an enumeration oracle.
- `src/progress/store.py` — idempotent `students` migration in `_connect()`: `PRAGMA table_info`
  then `ALTER TABLE ADD COLUMN email / password_hash` (nullable) plus a separate
  `CREATE UNIQUE INDEX` (SQLite rejects `ADD COLUMN … UNIQUE`; a unique index still permits many
  NULLs, which legacy rows need). New: `get_student_by_email`, `save_student_with_credentials`,
  `update_student_profile`, `update_student_password`, `get_password_hash`. `get_student` now
  whitelists its fields so `password_hash` can never leak by accident.
- `src/platform_api.py` — `register_student`, `authenticate_student` (one generic message for
  both failure branches), `get_student_profile`, `update_student_profile`, `change_password`.
  New account ids are `"stu_" + uuid4().hex`; `_slugify` can never emit `_`, so account ids are
  **provably disjoint** from legacy slug ids. `_slugify` and `create_or_load_student` are
  deliberately untouched — Streamlit and a pinned contract test depend on them.
- `src/path/engine.py` — unknown chapter now raises `NotFoundError`.
- `pyjwt` installed into the venv (bcrypt 5.0.0 was already present).

**Verified by `tests/test_auth.py` — 60 deterministic checks**, covering the migration from a
synthetic old-shape database (idempotent, legacy rows load with `email = NULL`, duplicate emails
rejected by the index, multiple NULLs coexisting), bcrypt's 72-byte cliff, all five boundary
functions and every error branch, the guarantee that all three login-failure modes return one
identical message, and the two backwards-compatibility contracts (the legacy slug still resolves
to `journey-student`; account ids stay disjoint).

**Still to do** for this milestone — see [`ROADMAP.md`](ROADMAP.md) §Milestone 0.

---

## 9b. Repo consolidation (2026-09-21)

**Changed.** Nine root-level documents collapsed into two: this file and
[`ROADMAP.md`](ROADMAP.md). Deleted `LOG.md`, `AI_CONTEXT.md`, `HANDOFF.md`,
`FEASIBILITY_REPORT.md`, `ADAPTIVE_V2_FEASIBILITY.md`, `PROJECT_REPORT_V2_CONTENT.md`,
`PRESENTATION_DUMP.md` and `V2_AGENT_BRIEF.md` after folding their content in. Also removed
dead weight: `testremote.py` (an abandoned Ollama-over-Cloudflare experiment pointing at a
tunnel that no longer exists), `src/test_api.py` (a key-works scratch script, not a test),
`legacy_chat_app.py` (recoverable via `git show c22e453:legacy_chat_app.py`), three captured
benchmark-output `.md` files that were tracked as if they were docs, ~2 MB of stale
`graphify-out/`, four transient run logs, `data/progress.db.bak`, and all `__pycache__`.
`.claude/launch.json` was untracked (it holds absolute Windows paths). `.gitignore` rewritten by
category, and `app.py` + `README.md` updated so no reference dangles.

**Why.** The root had become nine overlapping documents with real drift between them — and the
most valuable one, `LOG.md`, was gitignored (commit `8cd5609`), so the project's memory existed
on exactly one machine and never reached GitHub. Two tracked files beat nine untracked ones.

**Learned.** Gitignoring the dev log is what let commit messages rot to `.` — when the narrative
goes somewhere git can't see, the part git *can* see stops being maintained. Both consolidated
files are now tracked deliberately, so the history is backed up and a fresh clone is not blind.

### Follow-up — made the directory self-sufficient for a fresh agent

**Changed.** Added `AGENTS.md` at the project root (with `CLAUDE.md` as a one-line `@AGENTS.md`
include, matching the `web/` pattern): the auto-loaded entry point carrying what the project is,
where work stopped, the explicit next action, the milestone order with its gating reasons, the ten
non-negotiables, how the user works, setup-on-a-new-machine, verification commands, and the
expensive gotchas. `requirements.txt` rewritten with `bcrypt` + `pyjwt` added (both were imported
or imminent but undeclared) and a comment per dependency. `.env.example` expanded from 4 to all 9+
environment variables the code actually reads, including the per-role model overrides, the
`ECOLEARN_*` path/behaviour overrides and `ECOLEARN_JWT_SECRET`. The Gemma
`system_instruction`/`thinking_config` constraint written into §6 as a callout.

**Why.** An audit for "could another agent pick this up cold?" found the knowledge was complete but
the *pointer* to it was missing: `AGENTS.md`/`CLAUDE.md` existed only inside `web/`, so nothing
auto-loaded at the root. Three standing conventions (never auto-commit, log every change, the
Gemma constraint) lived only in the assistant's external memory directory, which does not travel
with the folder — the Gemma constraint survived nowhere but two code comments. `requirements.txt`
had also silently gone stale the moment `src/auth/passwords.py` imported bcrypt.

**Learned.** Context stored outside the project directory is context you will lose. Anything a
future agent must know belongs in a file the folder carries — an external memory is a convenience,
not a record. And a dependency list is only as trustworthy as the last import you added: grep the
actual imports rather than trusting the file.

## 9c. Scale-up planning + handoff setup (2026-09-21)

**Changed.** Documentation only — no project code touched. `ROADMAP.md`: Milestone 1 rewritten as
the full 28-chapter curriculum spine plus skills (7 steps, starting with the duplicate-id fix);
new **M1b** (Class 12 pilot, a user-decided go/no-go gate); new **Track C** (RAG corpora, parallel
from M1); M7 rewritten as mass generation after M6, with quota math; four new user decisions
**S1–S4** (ordering scheme, subject structure, diagrams, generation timing); a new
non-negotiable against renaming existing ids; a forward-compatibility note on M0's chapter picker;
and a §1 section showing how the scale-up threads through the milestones. `AGENTS.md`: a
first-session checklist (read, check `git status` without discarding handoff work, run the suite,
summarise understanding back to the user), the Class 11 + 12 goal, a hard checkpoint after M0 to
ask S1–S4, the revised phase table, rule 10 on id stability, and a warning that
`.claude/launch.json` holds absolute paths. This file: the latent at-scale issues added to §2.

**Why.** The user set a new goal — full Class 11 + 12 coverage — and is handing the project to
another Claude Code instance. The scale-up analysis existed only in a chat transcript. It was
turned into milestones with acceptance criteria, and every code claim was verified against the
source and recorded with the function it lives in, so the next instance can act without
re-auditing.

**Learned.** Scaling reveals assumptions nobody wrote down because they were never false: that
concept ids are unique, that the curriculum is small enough to re-parse per call, that "velocity"
means one thing, that every interest analogy is mechanical. None of them are bugs at 17 concepts,
and all of them are at 250. The cheapest place to catch them is before the authoring, which is
why M1 opens with the duplicate-id guard rather than with YAML.

Sequencing lesson: the tempting order for "cover the whole syllabus" is to generate lessons first.
It's the wrong order here, because M6 changes the lesson schema — so the plan front-loads the
format-independent work, buys a cheap pilot to test the thesis, and generates in bulk exactly once.

## 9d. Plan extended: 15–20 interests + a self-hosted GPU LLM (2026-09-21)

**Changed.** Documentation only — no project code touched. The user added two goals: scale from 2
interests to **15–20**, and generate on a **self-hosted LLM on a GPU** instead of a paid API tier.
`ROADMAP.md`: M1 widened to cover both axes of the content matrix, with a new **Step 8 — interest
registry** (`data/interests.yaml`, `active`/`draft` status, validation, `GET /api/interests`); a
new **M1a — LLM provider layer + self-hosted backend** (one `src/llm/` interface, an
OpenAI-compatible backend covering vLLM/Ollama/llama.cpp/TGI, model quirks as capability flags,
backend-spanning fallback, zero pacing and concurrency for local runs, and a parity gate using the
existing benchmark harnesses); the pilot now runs on the self-hosted model with 1–2 new interests
and measures GPU throughput; Track C generalised to N interests with a sparse interest × domain
matrix and a `verified` marker that ingest respects; M6 absorbs the shared-core schema split; M7
reframed from API quota to GPU-hours, with a storage decision. §15 regrouped into curriculum (S),
interests (I1–I4) and LLM hosting (L0–L4) decisions, each with an **"Ask when"** column. The
non-negotiable "don't swap providers" became "until M1a, don't touch provider code; after it, go
only through `src/llm/`". The cached-vs-live rule now says explicitly that a GPU doesn't license
live lesson generation. `AGENTS.md` updated to match, including an explicit post-M0 question list.

**Why.** Both goals multiply the content matrix: ~250 concepts × 20 interests × 5 formats ≈ 25,000
lessons and ~75k–125k LLM calls, which is what makes self-hosting the only affordable route. The
interest multiplier also broke three assumptions that were fine at 2: that interest lists can be
hardcoded, that corpora can be hand-authored, and that regenerating interest-independent text per
interest is harmless.

**Learned.** Measured rather than assumed, and two numbers changed the recommendations: lessons
average **2.8 KB**, so 25,000 is ~69 MB (the storage problem is regeneration churn in git history,
not raw size); and on `position` the formal `worked_example` is interest-independent and ~30% of
each lesson (worth splitting out once M6 reshapes the schema anyway). The history also answered a
question before anyone asked it: Gemma's recorded **2/11** polish success means a self-hosted
setup cannot assume one model for every role — hence per-role configuration and a parity gate
before the pilot, not after it.

## 9e. Sprint to 2026-09-30 + the full content spine (2026-09-21)

**Changed.**
- *Plan:* the user set a 10-day sprint (build done by 2026-09-30, student pilot in October,
  HackAStone finals 2026-10-29) and made new decisions: **username + password** accounts (no
  email), **all Class 11 + 12 concepts × 10 interests × 3 formats** (6,690 lessons) **written by
  Claude Code sessions — no LLM API, no GPU, no LLM critic** — MCQ check questions graded with no
  LLM call, **Gemini only** for the doubt chatbot (3090 backend deferred to a placeholder), local
  hosting first. Recorded as `ROADMAP.md` §0 (overrides the milestone order) and in `AGENTS.md` §2.
- `src/curriculum/schema.py` — `grade` on `Unit` (loader stamps it onto chapters and concepts),
  a `Domain` enum + `domain` on `Chapter`, optional `syllabus_note` on `Concept`, and
  `extra="forbid"` on every model. Fixed the `Concept.order` docstring (order is global).
- `src/curriculum/loader.py` — `validate_unique_ids()` run at load **before** any dict index is
  built (fixes the silent last-one-wins duplicate bug in `_by_id`); grade stamping.
- `data/curriculum/physics.yaml` — **28 chapters, 223 concepts** (Class 11: 119, Class 12: 104),
  NCERT rationalised structure. Sparse global order `chapter_seq*1000 + pos*10`; the original 17
  concepts renumbered (2010…3080) but **no id renamed or moved**. 8 concepts carry a
  `syllabus_note` for the user to keep or drop.
- `data/interests.yaml` + `src/curriculum/interests.py` — the interest registry: 10 interests
  chosen so every physics domain has ≥ 3 natural fits; football and gaming `active`, the rest
  `draft`.
- `scripts/curriculum_report.py` → `content/CURRICULUM.md`, a generated review document.
- `tests/test_content_spine.py` — 27 checks, including fixtures proving the loader **rejects** a
  duplicate concept id, a duplicate chapter id, a key typo, a missing grade, a mis-ordered
  prerequisite and an unknown domain.
- `venv` rebuilt with Python 3.12 — the committed one pointed at another machine's interpreter
  (`C:\Users\murar\…\Python310`) and could not run.

**Why.** The user wants to see and approve the curriculum before any lesson is written, and every
lesson file is keyed on a concept id, so the spine has to be right — and guarded — first.

**Learned.**
- Pydantic's default `extra="ignore"` is a trap for hand-authored data: `prerequisite: [a]`
  (missing "s") would have loaded silently as *no prerequisites*. Forbid unknown keys wherever
  humans type the input.
- Order-encoding the chapter (`15030` = chapter 15, concept 3) makes the number readable and
  leaves gaps everywhere, at the cost of nothing.
- Scaling surfaced a product bug no test could show at 2 chapters: prerequisites across chapters
  **hard-lock** concepts, so a Class 12 student would be blocked behind Class 11. Recorded as an
  open decision rather than silently changed, because a pinned test asserts today's behaviour.

## 9f. Curriculum review applied: both boards, syllabus-verified, nothing locked (2026-09-21)

**Changed.**
- *User decisions:* keep all eight flagged topics (students are on **CBSE and ISC**); write
  lessons in standard school teaching order; **lock nothing**; add missing topics wherever the
  syllabus specifies them.
- `src/curriculum/schema.py` — `Board` enum + `boards` on `Concept` (default both; `[isc]` for
  ISC-only; `[]` for enrichment).
- `data/curriculum/physics.yaml` — checked line by line against the **official CBSE 2025-26
  syllabus** (the NIC-hosted PDF). Added 8 CBSE topics I had missed (`measurement_uncertainty`,
  `motion_graphs`, `calculus_for_motion`, `unit_vectors`, `motion_plane_constant_acceleration`,
  `vertical_circle_motion`, `elastic_potential_energy`, `magnetic_field_oersted`) and 11 ISC-only
  topics (axes theorems, geostationary satellites, metre bridge, potentiometer, cyclotron,
  dispersion, Davisson-Germer, Zener diode, junction transistor, transistor amplifier, logic
  gates). Moved `ac_generator` into Alternating Current. Poisson's ratio turned out to be in CBSE
  2025-26 — its "trimmed" note was wrong and is gone. **242 concepts → 7,260 lessons.**
- `src/path/engine.py` — **nothing is locked**: `next_concept` recommends the first uncleared
  concept in teaching order (brush-up advice in the reason), never `blocked`; `get_roadmap`
  returns only `mastered`/`available`, with `missing_prerequisites` kept as a hint.
- UIs: web roadmap drops the locked style and shows "builds on N earlier concepts"; the
  `ConceptStatus` type loses `locked`. Streamlit roadmap shows "brush up first: …".
- Tests: `test_scale_chapter2.py` rewritten to prove nothing locks and hints clear as prerequisites
  are cleared; `test_persistence.py` and the live `test_platform_api.py` updated;
  `test_content_spine.py` now 41 checks (board tags, the added CBSE topics, unknown-board rejection,
  originals kept in relative order).
- `scripts/curriculum_report.py` — board column, board-specific section.

**Why.** "Keep both" meant students from both boards, which made board a property of each concept
rather than a yes/no on eight topics. "Don't lock anything" removes the cross-class trap found in
§9e at its root instead of special-casing cross-chapter prerequisites.

**Learned.**
- Check the syllabus, not your memory of it. The official 2025-26 text had six topics the
  memory-based draft missed, and one note that was simply wrong (Poisson's ratio). The only way to
  find that was to read the document.
- The official CISCE site refuses automated fetches (403), so ISC topics rest on a third-party
  summary and are labelled as such in the data. Unverified inputs should carry that label with
  them, not only in a chat message.
- `npm run lint` already fails on three pages (setState called synchronously inside `useEffect`) —
  pre-existing, and scheduled to disappear with the frontend `request()`/auth-provider rewrite.

## 9g. Sprint day 2: authored lessons, validator, gold examples, username login (2026-09-21)

**Changed.**
- `data/curriculum/physics.yaml` — **Communication Systems** added as chapter 29 (ISC-only, 7
  concepts, orders 29010–29070). 249 concepts → 7,470 lessons.
- `src/content/lesson_schema.py` — `LessonFormat` (explain / challenge / misconception),
  `FORMAT_SECTIONS` (required H2s per format, in order), `MCQCheck` (exactly A–D, answer among
  them, one misconception per wrong option — validated by the model itself), `AuthoredLesson`;
  `LessonMetadata.source`.
- `src/content/authored.py` — parse the Markdown + YAML header; `to_legacy_lesson()` so today's
  UIs render authored lessons unchanged; `student_view()`; neither ever contains the answer,
  explanation or misconceptions.
- `src/content/lesson_service.py` — serves an authored "explain" lesson first, legacy JSON second;
  `get_authored_lesson`, `available_formats`; lessons dir overridable via `ECOLEARN_LESSONS_DIR`.
- `src/content/validate.py` + `scripts/validate_lessons.py` + `scripts/katex_check.mjs` — the
  deterministic validator (location/ids, MCQ consistency, sections, length, control characters,
  drafting text, `$` balance) and **real KaTeX rendering** via the web app's own `katex` package;
  `--coverage` report.
- `content/AUTHORING_GUIDE.md` — the brief every writing session reads: the three formats, the
  no-invented-facts rule, the weak-fit rule, physics-correctness rules, MCQ design, a self-check.
- **12 gold lessons**: `second_law` (Class 11) and `ohms_law` (Class 12) × cricket and music × 3
  formats. `ohms_law × cricket` demonstrates the weak-fit rule (real devices, no forced analogy).
  All 12 validate.
- **Username login**: `store` gains `username` + `idx_students_username` (the email draft's
  column is left in old DBs, unused); `register_student` / `authenticate_student` take a username
  (3–20 chars, `[a-z0-9_.]`, case-insensitive); interests are validated against the registry on
  register and profile update. `tests/test_auth.py` → 73 checks, including a DB migrated by the
  email draft.
- New `tests/test_authored_lessons.py` (25 checks); `test_content_spine.py` → 42 checks.

**Why.** Day 2 of `ROADMAP.md` §0: nothing can be written at scale until the file format, the
automatic format check and the quality bar exist — and the user approves the bar before 7,458
more lessons copy it.

**Learned.**
- Markdown + YAML block scalars beat JSON for hand-written physics: backslashes stay literal. The
  one remaining trap — a backslash inside a *double-quoted* YAML string — shows up as a control
  character, which the validator now names with the fix.
- Rendering maths with the exact library the browser uses is cheap (one Node process per run)
  and turns "does this formula render?" from a manual check into a test.
- A multiple-choice answer key is a secret: the adapter and the student view are tested to never
  include it, because the browser's network tab would show it otherwise.

## 9h. Gold-lesson feedback: story openings and images (2026-09-21)

**Changed.**
- *User feedback on the gold lessons:* "good, but start with a story that sparks curiosity, then
  explain; include images of scenarios, graphs and famous images related to the concept." Scene
  illustrations: **one per chapter × interest** (user's choice of three offered options).
- `src/content/lesson_schema.py` — every format now opens with a required `## The story`
  (explain's "The scene" is gone).
- **Media library** `data/media/`: `scenes/{interest}/{chapter}.svg` (4 drawn), `figures/{concept}/`
  (2 graph specs rendered to SVG + 2 drawn diagrams), `famous/` (Newton's *Principia* title page
  and a portrait of Ohm — both public domain, downloaded from Wikimedia Commons **with the user's
  approval**, recorded in `famous/manifest.yaml`; the 1.9 MB Principia PNG was converted to a
  268 KB JPEG).
- `scripts/render_graphs.py` — graphs are YAML data specs rendered by matplotlib in one house style
  (`matplotlib` added to `requirements.txt`); a legend can sit below the plot so it never covers data.
- `src/content/validate.py` — image rules: ≥ 1 image per lesson; local paths under
  `figures/ scenes/ famous/` only; alt text + caption required; files exist and are < 600 KB;
  SVGs parse, have a `viewBox`, and contain no `<script>`, `<foreignObject>`, `on…` handlers or
  external links; famous images need a manifest entry with an open licence, stated in the caption.
  `check_media_library()` catches unlisted famous images and stale graphs.
- `api/main.py` — `/media` static route. `web/components/markdown.tsx` — images render with their
  caption on a white card (spans, not `<figure>`, since Markdown wraps images in `<p>`);
  `API_URL` exported from `web/lib/api.ts`.
- All 12 gold lessons rewritten with story openings (named characters, a moment, an open question)
  and 2–3 images each. `content/AUTHORING_GUIDE.md` gains §4a (the story) and §7a (images,
  SVG rules, colour conventions, famous-image licensing).
- `tests/test_authored_lessons.py` → 41 checks (story required; every image rule, including five
  kinds of unsafe SVG).

**Why.** A story makes the student want the answer before it arrives; pictures carry what text
can't — especially graphs and circuit diagrams, which Class 12 depends on.

**Learned.**
- Graphs belong in data, not drawings: a spec rendered by code can't disagree with its own numbers,
  and a hand-drawn curve easily can.
- Look at every image before shipping it. Each of the four scenes had at least one overlap
  (a label running into a drum, a guitar across the headphones, a hat over a scoreboard) that was
  invisible in the SVG source and obvious in the browser pane.
- SVG is code: it can carry scripts and external requests, so "safe SVG" is a validator rule, not a
  hope. A famous image is a licence obligation, so its source and licence live in data the
  validator reads.
- The web app can't display these lessons yet (the lesson page hardcodes chapter 1). The image
  pipeline was verified end to end through the API (`/media` serves every referenced file with the
  right content type and refuses path traversal) and by `tsc`; the visible check waits for the
  chapter picker.

## 9i. More images where needed; commit-and-push authorised (2026-09-21)

**Changed.**
- *User instruction:* "include more images if required in future lessons and concepts", and
  "https://github.com/Niranjan-207/EcoLearn is the GitHub repo — push into it when required."
- `content/AUTHORING_GUIDE.md` §7a — images are now **as many as the concept needs**, no upper
  limit, with guidance on when to add more (processes in steps, differing cases, every important
  relationship, structure words can't describe); **story-specific scenes** allowed as
  `scenes/{interest}/{chapter_id}--{short-name}.svg` when the shared chapter scene doesn't show
  what the story needs; a self-check line asking whether any step would be clearer as a picture.
  No validator change needed — it has never capped the count.
- The standing git rule changed from "never commit — the user commits" to **commit and push to
  `origin main` when a chunk of work is complete and every check passes** — never force-push,
  never commit secrets or local files. Updated in `AGENTS.md` (§2 state, rule 11, §5, §8),
  `ROADMAP.md` (rule 8, §18) and §14 here.
- Repo facts recorded: `origin` = github.com/Niranjan-207/EcoLearn, branch `main`, re-initialised
  by the user with one "Initial Commit" (the 44 commits in §8 live in the teammate's repo).
- First commit under the new rule: all of sprint days 1–2 (content spine, no-lock engine,
  username auth, lesson format + validator, gold lessons with stories and images).

**Why.** The remote is the only backup, and a day of uncommitted work existed only in one working
tree. Pushing at the end of each verified chunk removes that single point of failure.

**Learned.** Before a first push to a new remote, check three things rather than assume them: what
the remote already holds (`git ls-remote` — here it matched local HEAD, so a plain fast-forward),
that secrets and local state are ignored (`git check-ignore` on `.env`, the DB, `venv/`), and that
nothing key-shaped is in the diff.

---

## 9j. Pilot batch + the auth HTTP layer (2026-09-21)

**Changed.**
- **Pilot batch:** Units and Measurement × cricket — 24 lessons (8 concepts × 3 formats) and 15
  images (the chapter scene, 11 diagrams, 2 graphs), written by one Claude Code **sub-session**
  that started cold from `content/AUTHORING_GUIDE.md` and the gold lessons. Two more public-domain
  NIST images were downloaded **with the user's approval** (US prototype kilogram K20, Prototype
  Metre Bar No. 27) and added to the manifest.
- Review by the main session: validator 36/36; every new image rendered and inspected; physics and
  answer keys re-derived in the densest lessons (error propagation 0.63% + 3 × 0.88% ≈ 3.3%; SI
  2019 redefinition dates; ball mass limits). Nothing needed fixing. MCQ answers A/B/C/D 6 each.
- `scripts/render_graphs.py` — crashed on relative paths (`relative_to` on an unresolved path);
  fixed with `.resolve()`. Reported by the sub-session.
- `content/AUTHORING_GUIDE.md` — headless-Edge command for checking drawn SVGs (the browser pane
  can't open folders created mid-session); reuse a chapter's figures for later interests.
- **Auth HTTP layer:** `api/security.py` (HS256 JWT `{sub, iat, exp}`, 7-day TTL, httpOnly +
  SameSite=Lax cookie, Secure in production, pinned algorithm, dev-secret warning / production
  refusal, `get_current_student_id` → 401 incl. tokens for deleted accounts); `api/main.py` gains
  register/login/logout/me/change-password, `PATCH /api/profile`, public `GET /api/chapters`
  (now with unit, grade, domain, concept count) and `GET /api/interests` (active only), error →
  status handlers (404/409/401/400/503) and `allow_credentials=True`. Learning endpoints are
  unchanged until the breaking flip. `platform_api.list_interests()` added.
  `tests/test_api_auth.py` — 34 checks, including cookie flags, token tampering/expiry and CORS.

**Why.** The pilot exists to measure what a batch really costs before committing to ~300 of them.
The auth layer was the plan's parallel track and touched none of the pilot's files.

**Learned.**
- **Measured cost per batch: ~269k tokens, 100 tool calls, 24 minutes** — about 7.5 min reading,
  5 min drawing, then ~30 s per lesson. Lesson writing is not the slow part; setup is, so larger
  batches (a chapter × several interests per session) and figure reuse cut the average.
- **Check the plan before planning the volume.** The account is on Claude **Pro**; after this day's
  work the 5-hour window was at 65% and the weekly at 47%. At pilot cost, 7,470 lessons is roughly
  80M tokens — far beyond Pro in nine days. This should have been checked before the sprint plan
  assumed "Claude Code sessions write everything"; the pilot is what surfaced it, which is its job.
- The sub-session followed the guide well enough that review found nothing to fix — evidence that
  the guide + gold lessons + validator carry quality without a critic.

## 9k. Batch 2 — Units and Measurement × football, and the first exact cost (2026-09-22)

**Changed.**
- 24 lessons `data/lessons/11/units_measurement/*/football__*.md`, written by a sub-session that
  used the cricket batch of the same chapter as its model but wrote new stories and numbers.
- `data/media/scenes/football/units_measurement.svg` (goal 7.32 × 2.44 m, 430 g ball, 0.9 atm,
  match clock) and one new interest-neutral graph
  `figures/measurement_uncertainty/repeated-circumference.graph.yaml` → `.svg`; the chapter's other
  12 figures and both NIST famous images were reused.
- Review: validator 60/60; scene and graph inspected (mean 69.0 cm, mean absolute error 0.12 cm
  re-derived); answer keys re-derived in the three most numeric lessons. Nothing needed fixing.

**Why.** The user postponed the scope decision to 2026-09-22 and asked for the next batch in the
same way; football is an active interest in every scope option, and reusing the chapter's figures
tests how much a second interest saves.

**Learned.**
- **Exact plan cost, measured with a before/after usage reading:** one batch moved the Pro weekly
  limit **48% → 50%** and the 5-hour window **71% → 88%** (the latter includes the main session's
  own, expensive long-context turns). Earlier estimates of 8–20 batches a week were too
  pessimistic: the weekly limit allows roughly **45–50 batches**, the 5-hour window about **5**.
- Reusing figures made the second interest cheaper and faster: ~248k tokens / 16 min vs
  ~269k / 24 min, with 51 tool calls instead of 100.
- Measure, don't estimate: the first estimate was off by a factor of 2–5 because usage was only
  read after the first batch, never before it.

## 10. Key decisions and why

1. **Google Gemini/Gemma via `google-genai`** (not the deprecated `google-generativeai`). Gemma
   for generation (separate quota bucket); Gemini Flash-Lite for cheap JSON judgement and polish.
2. **Multi-agent split** (generator / critic / polisher / assessor). Creative high-temperature
   generation is separated from cheap low-temperature structured judging — more reliable and
   cheaper per retry.
3. **Three-layer anti-scratchpad defence.** Reasoning-trained models leak planning notes. Layer 1
   prompt instructions, layer 2 regex sanitiser, layer 3 an LLM polisher. **Only layer 3 works
   reliably.** Hence the rule: *polish, then parse.*
4. **Prompts in `.txt`, not code** — tunable without a code review or rebuild, trivially revertible.
5. **Curriculum as YAML → Pydantic** ("parse, don't validate"): author in YAML, validate once at
   load, everyone downstream gets typed objects.
6. **The engine invents no pedagogy** — ordering and prerequisites come from the curriculum,
   mastery from the store; the engine only joins them, which keeps all three independently testable.
7. **The boundary returns plain dicts** — the single decision that made the Streamlit → Next.js
   migration a pure presentation swap.
8. **Pre-generate offline, serve cached** — pay the multi-agent + critic cost once; free-tier
   quota then delays *authoring*, never the *product*.
9. **Fail open on judges, fail loud on inputs.** A failed critic/polisher degrades quality, not
   availability; a missing key or unknown student surfaces immediately.
10. **Fallback model chains** on assessor and polisher — any one free-tier bucket can 429/500.
11. **`cleared` (≥2) vs `mastered` (3/3)** — a 2/3 shouldn't be a dead end.
12. **The assessment IS the lesson's self-check** — graded against the concept's pre-generated
    `check_question`, anchored with the concept name and learning objective. One question the
    student actually saw; one grade.
13. **`ask_help` is the only live call in the API**, capped at one critic-driven retry to stay
    responsive.
14. **Brand-once via shadcn tokens** — override shadcn's `:root` so every component inherits the
    palette. Tailwind v4 configures theme in CSS (`@theme`, `@plugin`), not a JS config.

---

## 11. Hard-won lessons

**On LLM behaviour**
- Each model has its own daily free-tier bucket; swapping models is the fastest 429 recovery.
- Reasoning-trained models dump their monologue into the response by default. Regex cleanup is a
  losing race against a model that keeps inventing new scratchpad labels — an LLM polisher wins.
- The longer the user message (e.g. after adding 6 retrieved passages), the *more* aggressively
  the model spills scratchpad. RAG and output discipline pull in opposite directions.
- Gemma is a poor polisher (2/11 success at temperature 0). Flash-Lite is the right tool.
- Strict JSON + low temperature + a small model = a reliable judge. Every judge in this project
  follows that shape.
- Two-mode prompts (dispatch on a `Mode:` header) halve prompt-management overhead.
- A cheap router protects an expensive pipeline: one $0.0001 call guards a $0.01 call.

**On RAG**
- Authoring the corpus is the most undervalued step. Half of "the model is hallucinating" is
  "the corpus didn't contain the fact". A 200-word accurate passage beats hours of prompting.
- Write corpora so every `##` section is a self-contained chunk — ingestion gets simpler.
- Embedding ranking surprises: "racing game acceleration physics" lost to a 60-vs-30fps passage.
  Always spot-check retrieval.

**On architecture**
- A boundary test that imports *only* the boundary is the proof the boundary works.
- Returning Pydantic objects would have leaked the abstraction; `.model_dump()` at the edge is
  what lets an HTTP layer serialize with no custom encoders.
- Scaling is authoring + generation, not engineering. The recurring code costs are presentation
  **selectors** (chapter, then subject) and **quota resilience**.
- Idempotent batch jobs beat fragile ones; rebuild derived state from the source of truth rather
  than appending to it.
- Idempotent *repair* beats regeneration — re-polishing stored raw bodies cost one cheap call
  each instead of a full RAG+generate+critic cycle.
- A correct simple check beats a clever broken one: the bespoke cycle detector was deleted once
  the existing ordering check was shown to catch cycles transitively.
- Lazy env-var config (read inside `_connect()`, not at import) beats threading `db_path=` through
  every function — one `os.environ` line redirects the whole store in a test.

**On UI**
- In a reactive UI, long-running work never lives in a button handler. Flip state, rerun, do the
  work in the next render when nothing is clickable.
- Pin the result; don't re-derive it. Re-calling `get_next_lesson` to render a grade flips the
  page to the next concept the instant the student passes.
- Markdown layout dramatically improves perceived quality even when the content is unchanged.
- A global font override is a blunt instrument — it silently breaks icon fonts that use ligatures.
- Honour the OS colour scheme explicitly, or a dark-mode machine renders your light-theme text
  invisible.
- `fetch` does not throw on 4xx/5xx. Check `response.ok`.
- Verify presentation by computed style, not screenshots.

---

## 12. How to run and verify

```bash
# 0. venv  (Windows: venv\Scripts\Activate.ps1  |  *nix: source venv/bin/activate)
pip install -r requirements.txt

# 1. live features need a key in .env:  GEMINI_API_KEY=...
# 2. the doubt chat needs the RAG index:
python src/rag/build_index.py

# PRIMARY — Next.js + FastAPI (two terminals)
#   one-time: cd web && npm install && echo NEXT_PUBLIC_API_URL=http://localhost:8000 > .env.local
python -m uvicorn api.main:app --reload --port 8000     # terminal 1  (docs at /docs)
cd web && npm run dev                                    # terminal 2  → localhost:3000

# LEGACY — Streamlit
streamlit run app.py                                     # → localhost:8501
```

**Tests are standalone scripts, not pytest.** Each sets its own `sys.path` and points
`ECOLEARN_PROGRESS_DB` at a temp file *before* importing the module under test, then
prints-and-asserts.

```bash
# deterministic (no API key needed)
venv\Scripts\python.exe tests\test_curriculum.py
venv\Scripts\python.exe tests\test_path_engine.py
venv\Scripts\python.exe tests\test_edge_states.py
venv\Scripts\python.exe tests\test_scale_chapter2.py
venv\Scripts\python.exe tests\test_persistence.py seed
venv\Scripts\python.exe tests\test_persistence.py verify

# contract canary (live LLMs, slow; pins student_id == "journey-student")
venv\Scripts\python.exe tests\test_platform_api.py

# web
cd web && npx tsc --noEmit && npm run lint && npm run build
```

---

## 13. Gotchas

- **Windows ports:** starting a server on a busy port throws `[WinError 10013]`, not the usual
  "address in use". Find the holder with `Get-NetTCPConnection -LocalPort <p>`.
- **Only ONE `next dev` per project dir** (Next 16) — a second instance refuses even on another
  port. Reuse the running one.
- **Next.js 16 renamed `middleware` → `proxy`**, and `error.tsx` uses `unstable_retry`, not
  `reset`. **Read `web/node_modules/next/dist/docs/` before touching routing, cookies or error
  files** (per `web/AGENTS.md`).
- **Tailwind v4 theme-token edits need a dev-server restart.** JSX hot-reloads, but `@theme` /
  `:root` value changes can serve a stale CSS chunk.
- **In PowerShell `curl` is an alias for `Invoke-WebRequest`** — use `curl.exe`.
- **CORS:** the browser blocks Next(3000) → FastAPI(8000) unless the origin is in
  `allow_origins`. `curl` bypasses CORS, so always test with an `Origin` header too.
- **Avoid `cmd &` inside a compound Bash command** — it backgrounds the whole `cd && …` in a
  subshell, leaving the parent CWD wrong and an orphaned server on the port.
- **Docstrings have drifted from the code** in places (e.g. `analogy_generator.py` says "Gemini
  2.5 Flash" but runs on Gemma). The code is the source of truth.
- **`data/progress.db` is throwaway dev data** — gitignored, safe to reset.

---

## 14. Working conventions

- **UIs talk ONLY to `src/platform_api.py`.** Never import engine/store/pipeline/agents from a UI.
- **The boundary returns plain JSON-serializable data.** No Pydantic objects cross it.
- **Cached vs live:** only the doubt chat and grading make live LLM calls. Preserve this.
- **New chapter/subject = content (YAML + a factory run), not engine code.** Concept `order` is
  global across the subject.
- **Tests are standalone scripts**, added in the same style as the existing ones.
- **Commit and push to `origin` (github.com/Niranjan-207/EcoLearn, branch `main`) when a chunk of work is complete and every check passes** (user authorisation, 2026-09-21). Never force-push, never rewrite pushed history, never commit secrets (`.env`, keys) or local files (`venv/`, `data/progress.db`, `chroma_db/`). (Until 2026-09-21 the rule was "the human runs commits".)
- Beginner-friendly explanations are appreciated — explain the *why*. Honest, specific critique
  over vague praise.
