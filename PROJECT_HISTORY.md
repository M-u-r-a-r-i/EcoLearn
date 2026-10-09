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
> Repo: github.com/Niranjan-207/EcoLearn, branch `main` (fresh history from 2026-09-21; the
> original 44 commits in §8 live in the teammate's repo).
>
> **How to read this file.** §1–§8 describe the project as it stood on **2026-09-21** and are partly
> out of date (e.g. "football or gaming", "auth in progress", "34 lessons"). **§9 onwards is a
> dated log, newest last, through 2026-10-02 (§9zj)** — that, plus `AGENTS.md` §2 (current state,
> next steps, open threads), is the truth. §10–§14 (decisions, lessons, gotchas, conventions) still
> hold.

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

## 9l. Scope decided + a self-running batch workflow for the next session (2026-09-22)

**Changed.**
- *User decision:* **14 chapters × 5 interests, "explain" first (target 2026-09-28), then
  "challenge" + "misconception" (target 2026-10-06).** Chapters: the "most important" set (A).
  Interests: the user asked for the best fit; for set A that is **cricket, football, gaming,
  smartphones, motorsport** — motorsport replaces music, whose strength (waves) has no chapter in
  the set. The other 15 chapters and 5 interests come after the finals.
- `data/content_scope.yaml` — the decision as data (chapters, interests, phases with targets).
- `scripts/batch_status.py` — reads the scope, counts lesson files on disk, prints per-phase
  progress and the next batch (`--all` lists every batch); `--brief` fills in
  `content/BATCH_BRIEF.md` for that batch: model lessons from the same chapter, the chapter's
  reusable figures, whether the scene exists, the interest's facts, matching famous images, and a
  fit note when the chapter's domain isn't one of the interest's strong domains.
- `content/BATCH_BRIEF.md` — the standard sub-session prompt (generalised from the two batches).
- `src/curriculum/interests.py` + `data/interests.yaml` — optional `facts:` per interest; filled for
  the 5 in scope (Laws of Cricket / IFAB Laws of the Game figures, standard voltages and bands).
- `tests/test_content_spine.py` → 47 checks (the scope file: 7 + 7 chapters, 5 registered
  interests with facts, the two phases).
- `AGENTS.md` — the scope decision, a 7-step "How to run a lesson batch" procedure (usage check →
  `batch_status.py` → brief → background sub-session → review → commit/push → promote interests),
  and the new commands in §6. `ROADMAP.md` §0 decision rows updated.

**Why.** The user will continue in a new session. Everything the next session needs — what to write,
in what order, how to brief a writer, how to review and when to stop for usage — is now in the repo,
and progress is derived from the disk, so there is no checklist to fall out of date.

**Learned.** Progress that is *computed* (files on disk vs the scope) can't drift; progress that is
*written down* (a checklist) always does. Same for briefs: a template filled from data gives every
batch the same instructions, where hand-written prompts slowly diverge.

## 9m. Four explain batches in parallel (2026-09-22)

**Changed.**
- 38 explain lessons, each batch written by its own background sub-session from its unchanged
  `batch_status.py --brief --batch …` output, all running at once on *different* chapters:
  - Units and Measurement × gaming (8)
  - Motion in a Straight Line × cricket (11)
  - Motion in a Plane × cricket (10)
  - Laws of Motion × cricket (9; `second_law` already existed)
- New scenes: `scenes/gaming/units_measurement.svg`, `scenes/cricket/motion_straight_line.svg`,
  `scenes/cricket/motion_plane.svg`.
- About 30 new interest-neutral figures and graphs under `data/media/figures/` for the three
  kinematics/dynamics chapters, which later interests will reuse. Plus one gaming-specific graph,
  `measurement_uncertainty/reaction-time-readings`.
- Review:
  - Every new image was rendered with headless Edge and tiled into grids with PIL.
  - Answer keys and distractors were re-derived in 8 of the most numeric lessons.
  - Two fixes: a label on `circular_motion_dynamics/banked-road-forces.svg` overlapped the `mg`
    arrow; the slope labels on `velocity/out-slow-back-fast-xt.graph.yaml` sat on the wrong segment.
  - Validator 98/98; the phase-1 count is 6/70 batches.

**Why.** The user asked for the next batches using several sessions at once.

**Learned.**
- **Parallel cost:** four batches together moved the 5-hour window **20% → 63%** (about 11% per
  batch) and the weekly limit **53% → 59%** (about 1.5% per batch). Three of the four were a
  chapter's first interest and had to draw its figures. So about 4 batches fit in one 5-hour window
  with room left for review.
- **Parallel sessions see each other's work:** while they ran, the validator flagged other
  sessions' graph specs that weren't rendered yet as errors. Each sub-session correctly left them
  alone, and the final run was clean. A validator error during a parallel run needs a re-run once
  all sessions have finished before anyone acts on it.
- Tiling rendered PNGs into one grid image makes reviewing 10+ figures one image read instead of
  ten.

**Follow-up, the same day: two more batches, run in parallel.**
- Units and Measurement × smartphones (8) and Motion in a Straight Line × football (11). Both
  reused the chapter's figures, so each drew only its scene.
- The smartphones batch added one interest-neutral graph,
  `measurement_uncertainty/repeated-thickness`.
- Validator 117/117; phase 1 is at 8/70 batches.
- Both batches together moved the 5-hour window **63% → 79%**, about 8% per batch when figures are
  reused against about 11% when they're drawn.
- *Fix:* the kilogram photo `famous/us-prototype-kilogram-k20.jpg` shows an **exact display
  replica** of K20, per its Commons description, not K20 itself. The manifest title and credit and
  the 4 captions that use it now say so. A sub-session spotted the `_replica` in the source
  filename.
- **Learned:** read a famous image's Commons description, not just its title. The filename said
  "replica", and three batches had captioned it as the real object.

## 9n. Frontend auth + the breaking flip + chapter picker (2026-09-22)

**Changed.**
- *The breaking flip (one commit, as ROADMAP §5 requires):*
  - `api/main.py`: `/api/roadmap`, `/api/next-lesson`, `/api/assessment` and `/api/help` now take
    the student from `Depends(get_current_student_id)`. `student_id` is gone from their contracts,
    and `POST /api/student` (unauthenticated, name-based) is deleted.
  - `tests/test_api_auth.py` → 42 checks: 401 without a session on all four endpoints, a spoofed
    `?student_id=` doesn't stand in for a session, `/api/student` is gone, and roadmap/next-lesson
    return 200 with a session.
  - Streamlit is unaffected: it calls `src/platform_api.py` directly.
- `web/lib/api.ts` rewritten:
  - One `request()` wrapper: `credentials: "include"`, `ApiError(status, detail)` parsed from
    FastAPI's `{detail}`, and timeouts of 15 s (90 s for the live help/grade calls).
  - A 401 hook `setUnauthorizedHandler` and `friendlyMessage()`, so users are never shown
    `localhost:8000`.
  - Functions `register`/`login`/`logout`/`getMe`/`updateProfile`/`changePassword`/
    `getChapters`/`getInterests`. No function takes a student id any more.
- `components/auth-provider.tsx` replaces `student-provider.tsx`: a `loading | authenticated |
  unauthenticated` state, hydrated from `GET /api/auth/me`, so a refresh no longer logs anyone out.
- `components/require-auth.tsx` + `app/(app)/layout.tsx`: roadmap, lesson and assessment moved into
  the `(app)` route group (URLs unchanged). It is a client guard; the API's `Depends` is the real
  boundary.
- `/login` (safe `?next=` redirect) and `/signup` (2-step: account → interest + class; one
  register call).
  - Signup replaces `/onboarding`, which is deleted.
  - `components/interest-level-fields.tsx` reads interests from `GET /api/interests` as a
    wrapping grid, so it works at 20 interests.
  - `components/auth-card.tsx` holds the shared form pieces.
- Chapter picker:
  - `lib/use-chapter.ts` keeps the chapter in `?chapter=`.
  - `components/chapter-picker.tsx` is a native `<select>` grouped by class · unit over all 29
    chapters.
  - Lesson and assessment also accept `?concept=`, and links carry the chapter.
- `lib/use-fetch.ts`: page loads are keyed by their inputs, so the loading state is derived, not
  set inside an effect.
- `components/site-nav.tsx`: a client component showing Log in / Get Started, or Roadmap, the
  student's name and Log out.
- Verified: `tsc --noEmit`, `npm run lint` and `npm run build` are clean; all deterministic tests
  pass.
- **Not yet verified in a browser.** Deferred because the 5-hour window was at 88%.

**Why.** The next step on sprint day 3–5 is real accounts in the web app. Until the flip, anyone
could read or change any student's progress by sending their id.

**Learned.**
- React's `react-hooks/set-state-in-effect` lint rule rejects the classic
  `setLoading(true)`-then-fetch effect. Keying the result by its request and deriving `loading`
  satisfies it, and also drops stale answers for free.
- In PowerShell, `R` is an alias for `Invoke-History`. Never name a helper function `R`.

## 9o. Seven explain batches in one window (2026-09-22)

**Changed.**
- 67 explain lessons from 7 parallel sub-sessions, each on a different chapter:
  - Units and Measurement × motorsport (8). This finishes the chapter for all 5 interests.
  - Motion in a Straight Line × gaming (11)
  - Motion in a Plane × football (10)
  - Laws of Motion × football (10)
  - **Work, Energy and Power × cricket (11)**, **Gravitation × cricket (8)** and
    **Thermodynamics × cricket (9)**: the first interest for each of these chapters.
- The 3 new chapters drew about 40 interest-neutral figures and graphs between them. There are
  also 7 new scenes, and two motorsport graphs (`repeated-lap-times`,
  `stopping-distance-vs-speed`).
- Review:
  - Every new image was checked in PIL grids, and the answer keys and distractors of 6 numeric
    lessons were re-derived.
  - Fixes: `heat_work_internal_energy/two-routes-same-state.svg` (text crossed an arc and
    overflowed its boxes); `thermodynamic_processes/four-processes-pv` (legend over the axis label
    → shorter labels, upper right).
  - Validator 184/184; phase 1 at **15/70 batches**.
- Sub-sessions now receive a one-line prompt telling them to run
  `batch_status.py --brief --batch …` and follow its output. The brief is the same text, but it no
  longer passes through (and bloats) the main session.

**Why.** The user asked for the next batches once the window reset.

**Learned.**
- **Cost:** 7 batches plus review took the 5-hour window from **1% to 85%** (about 12% per batch)
  and the weekly limit from **4% to 14%** (about 1.4% per batch). So a fresh window holds about
  **7 batches**, and the week about 60–65.
- The remaining 55 phase-1 batches need about 8 windows. That's feasible by 2026-09-28 at two
  windows a day.
- Pending with the user: the Thermodynamics session suggests a Clausius or Kelvin portrait for the
  second-law lesson, which needs download approval.

**Follow-up, the same day (frontend, while the window reset):**
- Every roadmap concept card is now a link to `/lesson?chapter=…&concept=…`. Nothing is locked, so
  any concept can be opened.
- New `app/(app)/settings/page.tsx` with two independent forms:
  - profile: name, plus interest and class through `InterestLevelFields` →
    `PATCH /api/profile`;
  - password: current, new and confirm → `POST /api/auth/change-password`.
- The nav gains a Settings link.
- `tsc`, lint and build are clean. **Still not browser-tested**; it was deferred with the rest of
  §9n because the window was at 93%.

## 9p. Seven more explain batches, one left partial (2026-09-22)

**Changed.**
- Six complete batches (60 lessons):
  - Motion in a Straight Line × smartphones (11)
  - Motion in a Plane × gaming (10)
  - Laws of Motion × gaming (10)
  - Work, Energy and Power × football (11)
  - Gravitation × football (8)
  - **Electrostatic Potential and Capacitance × cricket (10)**, the chapter's first interest and
    the first Class 12 chapter.
- **Electric Charges and Fields × cricket is partial (9/11).** The session ended before its
  sub-session finished. The two Gauss's-law lessons are missing, but their figures are drawn. The
  batch is resumable: rerun its brief and it skips the existing files.
- New images:
  - 6 scenes;
  - about 25 Class 12 electrostatics figures, several computed from exact formulas (dipole field
    lines, equipotentials, the conductor in a field);
  - 4 football graphs for Work, Energy and Power, and 2 gravitation diagrams (Kepler's unequal
    half-years, dish elevation against latitude).
- Review:
  - All 38 new images checked in grids, with no fixes needed.
  - Numbers re-derived across capacitors, Coulomb, Gauss, superposition, satellite-dish angles and
    energy graphs; 3 answer keys plus the drag explanation in satellite energy checked.
  - Validator: 253/253 valid.
- `content/AUTHORING_GUIDE.md` §7a: shared figures must not print batch-specific numbers.

**Why.** The user asked for the next batches after the window reset.

**Learned.**
- **Neutral figures need neutral numbers.** Several cricket graphs for Work, Energy and Power print
  "0.16 kg ball" and "24 m/s" in their titles and legends. The football session rightly redrew
  four of them rather than confuse students. That was lost reuse, so the guide now says to label
  the shape of the physics and keep the numbers in the lesson text.
- **Cost:** 7 batches took the window from 4% to about 80% and the weekly limit from 16% to 26%.
  That's consistent with §9o's figures (about 11% of a window per batch).
- A session ending mid-batch loses nothing that was written, because writing is resumable.
  Check for `[part]` in `batch_status.py --all` at the start of a session.
- *Follow-up:*
  - The last two Gauss's-law lessons were written (batch 11/11, commit `6f34558`).
  - **Famous image approved by the user:** `famous/rudolf-clausius.jpg` (Commons `File:Clausius.jpg`,
    PD-old, 275×326 px, 12 KB). It has a manifest entry and is placed after the Clausius statement in
    `thermodynamics/second_law_thermodynamics/cricket__explain.md`.
  - Chosen over Kelvin: the lesson's figure contrasts both statements, but Clausius's heat-flow
    statement is the one students remember, and he later named entropy.

## 9q. MCQ grading with no LLM, and a lesson page that hides the workings (2026-09-23)

**Changed.** Three problems the user found by running the site:

1. *Grading called a cloud model.* `submit_assessment` now takes the option letter and grades it
   against the authored lesson's answer key — `_grade_multiple_choice` in `src/platform_api.py`.
   Correct → 3 (mastered), wrong → 0, feedback is the lesson's own explanation plus, for a wrong
   pick, that option's misconception. No model, no API key, no latency, and the answer key never
   leaves the server. Legacy JSON lessons keep the Assessor path, so Streamlit still works.
   A bad letter raises `EcoLearnError` (400) and leaves progress untouched.
2. *The page showed everything, including the sanity check.* `get_next_lesson` now adds
   `lesson.sections` and `lesson.check` (from `student_view`) next to the legacy fields.
   The lesson page renders section by section and puts **Worked example** and **Where the picture
   breaks** inside `<details>` — one click away, keyboard- and screen-reader-friendly by default.
3. *Worked examples were too dense.* `content/AUTHORING_GUIDE.md` §7 now requires few, round,
   picturable numbers, one quantity per step and a plain-sentence sanity check, for lessons from
   2026-09-23 on. Existing lessons are left alone.

- `web/lib/api.ts`: `LessonSection` / `LessonCheck` types, `correct` / `selected_option` /
  `correct_option` on the result.
- `web/app/(app)/assessment/page.tsx`: a radio group of options (falling back to the textarea for
  legacy lessons); the result shows "you chose A; the right answer is D" instead of a score out of 3.
- `tests/test_mcq_grading.py` — 24 checks: no answer key or misconception reaches the browser,
  right/wrong scoring, the misconception in the feedback, and rubbish input refused without
  recording an attempt.
- `.claude/launch.json`: a `web` entry on **3000** (3100 broke the session cookie — CORS allows
  only 3000) and an `api` entry for uvicorn.

**Verified in a browser** (the click-through owed since §9n): signup → roadmap (29 chapters) →
lesson → collapsed sections → wrong answer shows the misconception → retry, correct answer →
roadmap shows "Best 3/3 · 2 attempts". The whole check answered in about 2 s including page work,
with no LLM call.

**Why.** The user's own decisions from 2026-09-21 (MCQ grading, no live call for grading) were
written into the lesson files but never wired up, so the site still used the old free-text path.

**Learned.**
- Content and UI can drift apart silently: the MCQ data was authored into 250 lessons for days
  before anything read it. When a decision changes the *data*, wire up one consumer immediately,
  even a crude one, or nobody notices the gap.
- The desktop app's browser can't deliver clicks while the window is minimized ("could not get the
  tab ready for input"). Driving the page with `javascript_tool` works, and reading
  `document.querySelector('main').innerText` is a cheap way to verify a flow without screenshots.

## 9r. All five in-scope interests are offered, with real coverage (2026-09-23)

**Changed.** The user saw only football and gaming at signup, while cricket — the largest set — was
hidden because `data/interests.yaml` still calls it a draft.

- `src/curriculum/scope.py` (new): a tiny reader for `data/content_scope.yaml`, so the boundary can
  use the agreed scope that only `scripts/batch_status.py` read before.
- `src/content/lesson_service.py`: `chapters_with_lessons(interest)` — one glob, returns the chapter
  ids that have lessons for an interest.
- `src/platform_api.py`: `list_interests()` now offers the **five in-scope interests** in scope
  order, each with `chapters_ready` / `chapters_total`. `active_only=False` still returns the whole
  registry. Registration already accepted any registered interest, so nothing else had to change.
- `web`: `Interest` carries the two counts, and each card shows "10 of 14 chapters ready" (or
  "All chapters ready").
- `tests/test_api_auth.py` → 44 checks (five interests offered, coverage counts present and real).

**Verified in the browser:** the picker lists cricket 10/14, football 6/14, gaming 4/14,
smartphones 2/14, motorsport 1/14; switching the demo student to cricket in settings saved, and
`/api/next-lesson` for Thermodynamics then served the cricket lesson with its sections and options.

**Why.** The registry's active flag is a yes/no for "every chapter written", which is the wrong
question at this stage: it hid the best content and offered two interests that were no more
complete. Coverage is a number, so the UI now shows the number and lets the student choose.

**Learned.** A flag that encodes a *policy* ("only offer finished interests") ages badly while the
content is still being written. Publishing the underlying measurement instead — how many chapters
are ready — let the same data serve both the student's choice and our own progress tracking.

## 9s. The last five chapters get their cricket lessons (2026-09-23)

**Changed.** Cricket now has lessons in **all 14 chapters in scope**, so every chapter has its
interest-neutral figures and the remaining four interests can reuse them.

- Current Electricity 12/12, Moving Charges and Magnetism 12/12, Electromagnetic Induction 7/7,
  Ray Optics 11/11, Dual Nature 6/6 — 48 lessons, about 45 new figures.
- These are the first batches written under the new §7 worked-example rules, and the difference is
  visible: the thin-lens example runs 20 cm → 30 cm → 60 cm in three steps, each with a physical
  comparison ("a little less than the width of the wicket", "catch it on a sheet of paper").
- Review: all 21 newly drawn images checked in grids (no fixes needed), answer keys re-derived for
  thin lenses, the cyclotron and de Broglie, plus the potentiometer and mutual-inductance numbers.
  Validator 302/302.

**Interrupted twice.** The first five sub-sessions all died on the Pro session limit mid-run
(commit `4275f33` preserved 25 lessons of partial work); the relaunched Ray Optics session wrote
all 11 lessons but stalled before reporting, which `batch_status.py` revealed as `[done]`.

**Learned.**
- **Check the disk, not the agent's exit status.** A sub-session that fails or stalls may already
  have finished its work; `batch_status.py --all` is the truth. Treating a failure as "nothing
  happened" would have rewritten 11 good lessons.
- **The weekly limit is now the binding constraint**, not the 5-hour window: these batches took it
  from 31% to 43%. At ~1.4% a batch, the ~45 remaining phase-1 batches need ~63% — more than one
  week holds alongside the frontend. A scope decision is with the user (drop the two thinnest
  interests, or accept slipping past 2026-09-28).

**Famous images the sessions asked for** (none downloaded; each needs the user's approval):
Poggendorff (potentiometer), de Broglie and Davisson–Germer (dual nature), Ørsted and Ampère
(moving charges).

## 9t. Football and gaming batches, and the first physics error caught (2026-09-23)

**Changed.** 39 lessons across four batches, all reusing existing figures (one new scene each):
Thermodynamics × football (9), Work Energy and Power × gaming (11), Gravitation × gaming (8),
Electric Charges and Fields × football (11). Coverage is now cricket 14/14, football 8, gaming 6.
Validator 341/341; phase 1 at 31/70 batches.

**The first real physics error since batching began.** The Gravitation × gaming session was killed
by the usage limit moments after reporting "found an arithmetic slip, fixing it" — so the fix may
never have landed. A dedicated audit sub-session recomputed every number in all 8 lessons with
Python and found it: an escape-speed option read $5.6$ km/s ($11.2/2$) while its misconception
describes $11.2/\sqrt{2} = 7.9$ km/s, breaking the mirror with the $15.8$ option. Fixed, and
`escape_speed`'s "Delhi to Mumbai in under two minutes" corrected to "about two minutes" (125 s).

**Interruptions, again.** Five parallel sub-sessions all stalled with *nothing* written (600 s
watchdog), burning ~50% of a 5-hour window for no output; two later runs died on the session limit.
Two or three at a time has been reliable.

**Learned.**
- **Cap parallel sub-sessions at 2–3.** Five stalled outright. The failure is expensive because the
  usage is spent whether or not anything is written.
- **A session that reports a problem and then dies leaves the problem behind.** "Found a slip,
  fixing it" plus a rate-limit death equals a wrong answer key on disk that the validator cannot
  see (it checks format, not arithmetic). Any batch cut off mid-thought now gets an audit pass,
  not just a completion pass.
- Sub-sessions are now told to write each lesson to disk as it is finished, so a kill leaves
  complete lessons rather than none.

## 9u. Gaming finished at 14/14, on a fresh clone (2026-09-24)

**Changed.** 56 explain lessons across five batches, completing the **gaming** interest:
Electrostatic Potential and Capacitance (8, finishing the batch left partial in `9t`), Current
Electricity (12), Moving Charges and Magnetism (12), Electromagnetic Induction (7), Ray Optics (11),
Dual Nature (6). Five new chapter scenes and **no new figures** — every chapter in scope already had
its interest-neutral set, exactly as `9l` predicted, so the batches only added a scene each. Two
existing famous portraits (Ohm, Poggendorff, Ørsted, Ampère, Davisson–Germer) were reused; nothing
was downloaded and the manifest is untouched. Coverage is now cricket 14/14, **football 14/14,
gaming 14/14**, smartphones 2, motorsport 1. Validator 477/477; phase 1 at 45/70 batches,
435/680 lessons. Commits `7acd816`, `ed8e163`, `b9556d5`, `834adf0`.

**Why the partial batch came first.** `batch_status.py` pointed at motorsport as "next", but
`potential_capacitance:gaming` was sitting at `[part] 2/10` from a run that died mid-batch. Under
§4a that is *unverified*, not merely unfinished, so it was audited before anything new was written:
every worked-example number and answer key in both lessons recomputed in Python, every distractor
checked against the misconception it names. **Both were correct; nothing changed.** This is the
first audit to find nothing — worth recording, because it shows the procedure's cost is sometimes
zero while still being the only thing that could catch the `9t` class of error.

**Weak-domain handling, recorded because it worked.** Magnetism and induction are not strong gaming
domains. Rather than forcing analogies, those lessons teach through *real devices from that world* —
Hall-effect thumbsticks, haptic coils, flipper solenoids, fan motors, wireless charging pads, panel
meters — and each *Where the picture breaks* says plainly that gaming is the setting, not the
analogy. Two limits were stated rather than glossed: a real claw solenoid has an iron plunger, so
its back-emf exceeds the 20 V the air-core formula gives; and the moiré fence used for the
"two comparable spacings" rule is a sampling beat, not wave interference.

**Learned.**
- **A fresh clone validates lessons but silently skips the maths.** `validate_lessons.py` shells out
  to KaTeX through `web/package.json`, so before `npm install` it prints a *warning* that KaTeX
  could not run and still reports every lesson valid. The line "421/421 lessons valid" means
  format only until `web/node_modules` exists. Run `npm install` in `web/` before trusting a clean
  validator on a new machine.
- **Push access is per-account, not per-clone.** The clone succeeded and every local commit worked,
  but `git push` returned 403 — the machine's stored credential was a different GitHub account
  without write access. Test `git push` early on a new machine, not after a window's work is
  already committed; a clone that reads fine can still be unable to write.
- Three parallel sub-sessions on different chapters ran to completion again (~35% of a 5-hour
  window for three batches), confirming the 2–3 cap from `9t`.

## 9v. Five motorsport chapters, on a teammate's machine (2026-09-24)

*Logged after the fact on 2026-09-25 from the commit messages; the batches were run and pushed by
a teammate (GitHub `M-u-r-a-r-i`) and carry their own review notes.*

**Changed.** 50 explain lessons across five motorsport batches: Motion in a Straight Line (11),
Motion in a Plane (10), Laws of Motion (10), Gravitation (8), Work, Energy and Power (11), each
with its chapter scene in `data/media/scenes/motorsport/`. Every existing figure was reused; the
approved Principia title page was reused in the two Newton lessons. **Two new interest-neutral
figures** in Work, Energy and Power: `kinetic_energy/ke-ratio-vs-speed-ratio` and
`mechanical_energy_conservation/energy-and-speed-down-a-drop`. Motorsport is now 6/14 chapters;
phase 1 at 50/70 batches, 485/680 lessons. Commits `9e183be`, `c9c22b3`, `1b18d5a`, `dbfbe12`,
`809294a`.

**Why two new figures.** The old ones broke `AUTHORING_GUIDE.md` §7a (shared figures must not carry
batch-specific numbers): `ke-vs-speed` is titled "0.16 kg ball" and `ke-pe-vs-height` labels
"Height above the bat". The replacements plot pure ratios (K/K₀ vs v/v₀; energy and speed as
fractions of a drop), so any interest can reuse them. The old figures were *not* removed — the
cricket, football and gaming lessons still point at them — so the §7a breach remains there until
those lessons are repointed.

**Weak-domain handling, again.** Gravitation has no native racing story, so, as with gaming
magnetism in `9u`, it teaches through real things in that world (satellite passes over a hill
climb, a weighbridge at altitude, an uplink dish) and each *Where the picture breaks* says
motorsport is the setting, not the analogy. Projectile range vs angle runs as a radio-controlled
long-jump contest, because no real car is launched near 45°. Where the school model is genuinely
incomplete (tyre friction isn't a clean `μN`; downforce raises N without raising m) the lessons say
so rather than gloss it. "Jeep" became "tow vehicle" — no trademarks.

**Figures that disagree with their examples.** In Motion in a Straight Line, three shared figures
carry illustrative numbers that differ from the worked example beside them. Instead of redrawing a
figure other interests depend on, the text says the figure teaches the shape and the example
carries the arithmetic.

**Learned.**
- **Two machines can work the same batch list.** The teammate pushed ten commits while this
  machine still held stale drafts of two of those files, untracked. `git pull` refuses to overwrite
  untracked files, so the drafts had to be compared with the pushed versions (they were earlier,
  unfinished drafts) and removed before fast-forwarding. **Fetch before starting a batch**, and
  agree who runs which batches, or two sessions will write the same lesson.

## 9w. Three more explain batches: smartphones mechanics, motorsport thermodynamics (2026-09-25)

**Changed.** 29 explain lessons in three parallel batches, each on a different chapter:
Thermodynamics × motorsport (9, `41e8db3`), Motion in a Plane × smartphones (10, `a651589`), Laws
of Motion × smartphones (10). Three chapter scenes and **one new interest-neutral figure**,
`free_body_diagrams/body-on-incline-against-stop.svg` (a body held on a smooth slope by a stop,
with its free-body diagram; no numbers printed). Coverage: motorsport 7/14, smartphones 4/14.
Phase 1 at 53/70 batches, 514/680 lessons. Validator 556/556.

**Review.** Every new image was rendered and read. Nine lessons were re-derived by hand, three per
batch (the most numeric ones): gas work, engine efficiency, AC coefficient of performance;
projectile off a desk, centripetal acceleration, 2-D relative velocity; connected bodies, static
friction, maximum speed on a level curve. All answer keys and all distractor→misconception
mappings were correct. **Nothing needed fixing.**

**Weak-domain handling** (mechanics is a weak fit for smartphones) followed the `9u`/`9v` pattern:
real phone features and gadgets as the setting (auto-rotate, sensor apps, GPS speed, a robot
vacuum, a power bank dangling by its cable, a maps-app curve warning), with the model's limits
stated. For example, an accelerometer senses the support force, not gravity, and some g-meter apps
draw the arrow outward.

**Learned.**
- **The §7a workaround is spreading.** Shared figures that print another batch's numbers
  (trajectories-by-angle at 28 m/s, resultant-vs-angle 3/4, the momentum, impulse and friction
  figures, the thermodynamics engine and fridge bars) are now being handled batch by batch with
  "divide by 16" / "drawn for a different impact" captions. It works, but each new interest adds
  another caption to explain. Redrawing those figures number-free, as `9v` did for kinetic energy,
  and repointing the existing lessons would remove the problem at the source. That's a post-Phase-1
  cleanup.
- Three parallel batches took 9–11 minutes each and about 150k sub-session tokens apiece.

## 9x. Smartphones reaches 8/14: four more explain batches (2026-09-25 → 2026-09-28)

**Changed.** 39 explain lessons for smartphones in four batches: Work, Energy and Power (11,
`ccc71a9`, 2026-09-25), then one parallel round on 2026-09-28: Gravitation (8, `6daeec1`),
Electric Charges and Fields (11, `931cff3`) and Thermodynamics (9). A chapter scene each; no new
figures; no famous images requested. Coverage: smartphones 8/14, motorsport 7/14. Phase 1 at
57/70 batches, 553/680 lessons. Validator 595/595.

**Review.** Every new scene was rendered and read. Three lessons per batch were re-derived by hand:
the vertical circle on a lanyard, 2-D sticking collision, power (`Fv`); orbital speed ∝ 1/√r,
satellite energy (U = 2E), g at height vs depth (d = 2h); Coulomb's-law scaling, perpendicular
superposition (40/30/50 µN at 37°), a line charge's 1/r field; the first-law signs (−50 J), p ΔV
with mL (20 J), and heat-engine efficiency. **All answer keys and distractor mappings were
correct; nothing needed fixing.** The sub-sessions' own write-then-recheck step caught and fixed
several slips before review. The gravitation batch had first claimed phones never use
geostationary-height satellites for positioning, which is false for some systems, and corrected it
itself.

**The §7a problem now changes content, not just captions.** The electrostatics batch left out
`point-charge-e-vs-r` and `shell-e-vs-r` altogether because they print another batch's charges
(5 nC, 40 nC). So students in that interest now see *fewer* figures. With 9w's list, that makes a
redraw pass (number-free versions, as `9v` did for kinetic energy) the most valuable content
cleanup after Phase 1.

**Learned.**
- **The weekly limit, not the 5-hour window, set the pace here.** On 2026-09-28 the window was at
  2% but the weekly limit was already at 92% before any batch ran (it had been 75% at the end of
  09-25, so other use of the account in between counts too). Read *both* numbers before planning a
  round.
- Parallel round timings: 8–13 minutes and about 130–150k sub-session tokens per batch. This is
  consistent with `9w`.

## 9y. Smartphones reaches 12/14, run to the weekly limit (2026-09-28)

**Changed.** 40 explain lessons for smartphones in four batches, run on the user's instruction to
use the weekly limit up to 100%: Electrostatic Potential and Capacitance (10, `8d30e9e`), Current
Electricity (12, `87cb2c0`), Moving Charges and Magnetism (12, `b5c7a3d`) and Dual Nature (6). A
scene each; no new figures. Portraits reused: Poggendorff, Ørsted, Ampère, Davisson–Germer.
Smartphones 12/14, motorsport 7/14. Phase 1 at 61/70 batches. Left: smartphones ×
{electromagnetic_induction, ray_optics}, and motorsport × the seven Class 12 chapters.

**Review.** Scenes read, three or four lessons per batch re-derived (capacitor networks and energy,
qEd; the Kirchhoff two-cell circuit, the Wheatstone bridge, drift velocity, parallel cells; the
cyclotron, forces between parallel wires, the loop field on its axis; the photoelectric equation,
de Broglie scaling). **No errors found.** The sub-sessions' own write-then-recheck caught six
slips before review: a rice grain swapped for a 1 g paper clip, phone-signal wavelengths, "15 MHz a
little below FM" (it is shortwave), a story/example distance mismatch, a doubtful claim about
pulsing cable currents, and a floating fitness band in a scene.

**Safety wording checked by hand.** The swollen power bank (current electricity) is opened by an
adult, with gloves, on a fire-proof mat, for disposal only, with "nobody should try it at home".
The laser-on-a-pixel-grid story (Davisson–Germer) says never to point a laser at eyes.

**Learned.**
- **Parallel batches can make the full validator fail for a while, and that's harmless.** A
  batch writes its lessons first and its scene last, so a *sibling* batch that finishes earlier sees
  "missing scene" errors in the full run. Validate with `--chapter` when committing one batch while
  others are still running, and run the full validator once they have all landed.
- **A scene preview can be older than the SVG.** The magnetism preview still showed a stray disc
  that the final SVG no longer had. Compare timestamps, or re-render, before flagging a scene.
- The existing `galvanometer-construction.svg` caption calls its field arrows "straight across the
  gap" instead of radial. It predates this batch and is left for the figure cleanup pass.

*Addendum:* the last batch of that run, Electromagnetic Induction × smartphones (7 lessons,
`f8a9cfe`), landed just before the weekly limit hit 100%. It was reviewed the same way (Faraday
2 V, self-inductance ×4 for ×2 turns, a coin warming 20 K on a pad) with no errors. Smartphones
13/14; phase 1 at 62/70.

## 9z. Teacher tools, and the API no longer dies with the doubt chat (2026-10-02)

The user paused lesson writing ("continue later, now improve the project") and chose the order:
**teacher tools → pilot metrics → robustness & polish.** This entry is the first of the three.

**Changed.**
- `src/progress/store.py`: new `teachers` and `classes` tables, plus a nullable `students.class_id`
  column. All additive: CREATE TABLE IF NOT EXISTS, and ADD COLUMN behind `PRAGMA table_info`.
  New functions: `username_exists` (checks both tables), teacher CRUD, `create_class`,
  `list_classes` / `get_class` (with student counts), `save_students_bulk` (one transaction, all or
  nothing), and `list_class_students`, which aggregates the progress table in SQL into
  mastered / attempted / last active.
- `src/auth/credentials.py` (new): usernames from names ("Aarav Kumar" → `aarav.k`, then
  `aarav.k2`; accents folded; "Li" → `li.student`; Devanagari-only → `student`), and typeable
  passwords "word-word-NN" from 256 words, about 5.9 M combinations, using `secrets`.
- `src/platform_api.py` §1b: `create_teacher` (server-only), `authenticate_teacher`,
  `change_teacher_password`, `create_class`, `add_students_to_class`, `list_teacher_classes`,
  `get_class_detail` and `reset_student_password`. Rosters are one name per line, with an optional
  ", interest"; 60 at most; errors name the line. `register_student` now also refuses a teacher's
  username.
- `api/security.py`: `get_current_teacher_id` and `get_current_account`. `api/main.py`:
  `GET /api/auth/session` (role + profile) and `/api/teacher/{login, me, change-password, classes,
  classes/{id}, classes/{id}/students, students/{id}/reset-password}`. Every response that carries
  a generated password is `Cache-Control: no-store`.
- `scripts/create_teacher.py` (new): asks for the password with getpass, never takes it as an
  argument.
- Web: `lib/api.ts` (session and teacher calls). `auth-provider` is now role-aware (`role`,
  `teacher`, `teacherLogin`, `HOME`). `RequireAuth role=…` sends the wrong role to its own home
  and keeps the query string in `?next=`. The site nav has teacher links and is `print:hidden`.
  The login page links to the teacher login. New pages: `/teacher/login`, and behind the
  `(dashboard)` route group `/teacher` (classes + create class), `/teacher/class?id=` (students,
  progress, two-step password reset, add students) and `/teacher/account`.
  `components/teacher-ui.tsx` holds the shared controls and the **credentials sheet**: a
  show-once warning, a table, and print-only cut-out slips, two per row.
- **`ask_help` imports `src.pipeline` lazily** (see Learned).
- `tests/test_teacher.py` (new): **60 checks**. Namespace, login, roster parsing, nothing written
  on a bad roster, progress summary, ownership (another teacher's class or student → NotFound for
  view / add / reset; self-registered students can't be reset), reset invalidates the old
  password, HTTP role separation, no-store, and a 45-student class in under 8 s.

**Why these shapes.**
- **A separate `teachers` table, not a role flag on students.** A teacher id (`tch_…`) fails
  `get_student_profile`, so every existing student endpoint refuses a teacher's session with no new
  check anywhere. A role column would have needed an `if` on every endpoint, now and in the
  future.
- **No teacher signup over HTTP.** A teacher can reset students' passwords, so becoming one must
  need access to the server, not a button.
- **Passwords exist in plaintext only in the response that made them.** The store keeps bcrypt
  hashes, as for self-registered students. A lost slip means a reset, never a lookup, and the UI
  says so before the teacher leaves the screen.
- **Another teacher's class answers 404, not 403**, so a guessed id reveals nothing.
- **A reset doesn't end the student's existing sessions.** In a classroom, the student who forgot
  their password is usually logged out anyway. Revoking sessions would need a token version per
  account, which is noted as a later hardening step.

**Verified in the browser** (local dev DB, a demo teacher created with the new script's function):
teacher login → empty dashboard with real coverage counts → a three-name class (usernames
`aarav.k`, `meera.i`, `kabir.s`; the per-line interest honoured) → the credentials sheet; print
rules present (`print:grid` slips, `print:hidden` nav) → class page → two-step reset → the
student logs in with the new password and lands on `/roadmap` → that student opening `/teacher`
is sent back to `/roadmap`. `tsc`, lint, build and all 12 test scripts are clean.

**Learned.**
- **Windows Application Control blocked `grpc`'s native DLL** (`cygrpc…pyd`, dated 2026-09-21),
  and because `platform_api` imported the doubt-chat pipeline at module load (chromadb → grpc),
  **the whole API failed to import**: login, lessons and grading, plus `tests/test_api_auth.py`.
  Nothing in our code had changed; a Windows security policy had. Fixed in code by importing
  `src.pipeline` inside `ask_help`, which now turns an import failure into a friendly 503. Only the
  chat goes down. **The chat itself is still broken on this machine** until the policy allows the
  DLL, or `grpcio` is reinstalled from a wheel the policy trusts. That's a machine setting for the
  user, not something to change from code. *Rule: a live-LLM feature's dependencies must never be
  imported on the path every request takes.*
- **bcrypt in threads gives about 3×, not 16×.** One hash is about 0.36 s here, so a 45-student
  roster took ~16 s serially and ~5.5 s on 4 threads; 8 or 16 threads were no faster. The web
  call uses the long timeout and the button says "a few seconds".
- **A freshly added route folder can 404 in `next dev`** even though `npm run build` lists it.
  Restarting the dev server fixed it. Don't run `npm run build` while `next dev` is up: both write
  `.next`, and that is the likely cause.
- JSX dropped the space in `</strong> For` inside a wrapped paragraph. An explicit `{" "}` is the
  reliable fix.

*End of session, same day:* the user reported being unable to log in as a student. The API was
checked directly and works: login 200 with a cookie, CORS allowed, `/session` correct. The cause
is still open, waiting for the message the user sees. The likely causes are listed under "Open
threads" in `AGENTS.md` §2. The user asked for everything to be stored so a new session can pick
up from the folder alone. That's `AGENTS.md` §2 (open threads) plus this file.

## 9za. Pilot metrics and the misconception dashboard (2026-10-02)

Second of the user's three improvement steps (teacher tools → **pilot metrics** → polish). The
user also set the finals context: **HackAStone 2026, theme "Agentic AI for Education"**, final at
the *AI for Education Holland* conference (VU Amsterdam, 29–30 Oct 2026; organising committee
includes NTU Singapore; conference theme "Research meets Practice"), **15-minute presentation**.

**Changed.**
- `src/progress/store.py`: three new tables, created in `_connect()` (additive):
  `lesson_views` (open time + active seconds), `answers` (every MCQ pick, attempt number, the
  misconception its option names), `lesson_ratings` (one 👍/👎 per student × concept × interest).
  Each row records the student's interest *at the time*. Functions: `create_lesson_view`,
  `set_lesson_view_seconds` (MAX, never lowers), `record_answer`, `set/get_lesson_rating`,
  `get_activity`, `list_all_students`.
- `src/progress/metrics.py` (new): `class_insights()`, a pure function over rows → summary,
  misconceptions (grouped by concept × interest × option, counted in *students*, share out of
  those who answered), concepts hardest-first, per interest, per student.
- `src/platform_api.py` §4b: `start_lesson_view`, `record_lesson_time` (clamped to time since
  opening and 30 min), `rate_lesson`, `get_class_insights` (own classes only; includes question,
  chosen and right option text), `pilot_report` (all classes, students → S001…, classes → C01…).
  `_grade_multiple_choice` logs every pick and returns `attempt_no`.
- `api/main.py`: `POST /api/lesson-views`, `POST /api/lesson-views/{id}/time`,
  `POST /api/lesson-ratings` (student session), `GET /api/teacher/classes/{id}/insights`.
- `scripts/pilot_report.py` (new): the cross-class "admin" view — prints the headline numbers,
  top misconceptions, hardest concepts and per-interest table; `--csv DIR` exports pseudonymised
  rows for analysis. Read-only, server-only.
- Web: `lib/use-lesson-view.ts` (active-time tracker), a "Did the cricket explanation work for
  you?" 👍/👎 on the lesson page, `components/class-insights.tsx` (tiles, "What your class is
  getting wrong", concepts hardest first, by interest) on `/teacher/class`, and *Reading* and
  *Right first time* columns in the student table.
- `tests/test_pilot_metrics.py` (new): **56 checks**.

**Why these shapes.**
- **First-try accuracy is the headline, not "mastered".** After a wrong pick the app reveals the
  right answer, so a retry is nearly free; `progress.best_score` would make every class look
  brilliant. `answers.attempt_no == 1` is the honest measure.
- **Active time, not open time.** The tracker counts 5-second ticks only while the tab is visible
  and the student has scrolled/typed/touched in the last 2 minutes; the server clamps every view to
  the time since it opened and to 30 minutes. A tab left open over lunch can't become "an hour of
  reading" — the number has to survive a sceptical judge.
- **The time report is `fetch(keepalive)` with `text/plain`**, a CORS "simple request": no
  preflight, which a closing page wouldn't wait for. The endpoint parses the JSON itself.
- **The view starts after 2 s on screen.** Skips accidental opens and makes React's dev
  double-mount harmless (verified: one `POST /api/lesson-views` per open).
- **Insights load separately from the class list**, so a failing query never hides the password
  reset button a teacher may urgently need.
- **The export is pseudonymised at the boundary**, because the pilot is on minors and the data
  will be analysed by people outside the school.

**Verified in the browser** against the running dev servers with a throwaway teacher
(`metrics.check`) and class ("Metrics check 11-A", three students) in the local DB: one view per
lesson open, heartbeat and leave-page time reports (no OPTIONS preflight), 👍 saved, wrong then
right answers logged with attempt numbers, and the class page showing 3/3 active, 33% right first
time, 67% helpful, the cricket misconception "2 of 2 students" with the question in KaTeX, and the
per-interest split. Student login on `localhost:3000` worked with a class account. `tsc`, lint and
all 13 test scripts are clean; `npm run build` was skipped because the user's `next dev` was
running.

**Learned.**
- The `answers` table should have existed from the day MCQ grading landed (§9q): `progress` keeps
  only the best score, so every wrong pick made before today is gone. Metrics that matter for the
  pitch need raw events, not just the current state.
- `form_input` on a visually hidden (`sr-only`) radio sets the DOM value but not React's state;
  clicking the visible option label is the reliable way to drive it.
- `tests/test_auth.py` crashes with `UnicodeEncodeError` when stdout is redirected on Windows (it
  prints `→` in cp1252). Not a test failure; run with `PYTHONIOENCODING=utf-8`.

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

## 9zb. The chapter picker only offers what is written (2026-10-02)

**Changed.** The picker listed all 29 chapters for every student. For an interest with gaps
(motorsport: 7 of 14), most chapters opened onto concepts with no lesson, and the student saw
"…Generate it with the lesson factory": developer text.
- `src/content/lesson_service.py`: `concepts_with_lessons(interest)`, the serving rule (an
  "explain" lesson or legacy JSON) for the whole syllabus in two globs.
- `src/path/engine.py`: `concept_ids_by_chapter()`.
- `src/platform_api.py`: `list_chapters(interest=None)` adds `lessons_ready` per chapter (the
  interest is validated against the registry, since it becomes a glob pattern);
  `get_roadmap` adds `has_lesson` per concept; `get_next_lesson` skips an unwritten concept to
  the next unmastered one that is written; the `lesson_missing` reason is now written for students.
- `api/main.py`: `GET /api/chapters?interest=`.
- Web: `use-chapter` loads chapters for the student's interest (cached per interest); the picker
  disables chapters with no lessons ("— coming soon"), labels part-written ones
  ("8 of 11 lessons ready") and says "7 of 29 chapters have lessons for Motorsport so far";
  the roadmap shows unwritten concepts as non-clickable "Coming soon" cards, and an empty chapter
  shows one clear message instead of a progress bar and dead links.
- `tests/test_chapter_coverage.py` (new): 13 checks, on a temporary lessons directory.

**Why disabled, not hidden.** Showing the whole syllabus with "coming soon" is honest about where
the content is and shows the curriculum's breadth; hiding chapters would make the product look
smaller than it is, and a shared link to a hidden chapter would look like a bug.

**Verified in the browser** as a motorsport student: 22 chapters disabled, Ray Optics shows the
"still being written" message and no progress bar, Gravitation shows its 8 lessons and Continue.

**Learned.** `chapters_with_lessons` (used for the signup counts) counts *any* format, but only
"explain" is served. Coverage and serving must use the same rule, or the UI promises a lesson
that the server can't deliver.

## 9zc. The teacher agent (2026-10-02)

The HackAStone theme is **"Agentic AI for Education"**, and until now no agent was visible in
the product. The user asked for a teacher-facing agent built on the §9za data.

**Changed.**
- `src/agents/teacher_agent.py` (new): a tool-calling loop. Five read-only tools over one class
  (`get_class_overview`, `list_misconceptions`, `get_concept`, `get_lesson_takeaway`,
  `list_students`); the model decides what to read, at most 8 turns (tools off on the last), and
  must return five fixed Markdown sections. `GeminiModel` wraps google-genai (manual loop, so every
  call is recorded as a step); `rules_plan` writes the same sections by fixed rules;
  `plan_class` tries each model, then the rules.
- `prompts/teacher_agent.txt` (new): how to investigate, and the rules (only tool numbers, students
  only as `[S#]`, physics only from the lesson's key takeaway, say so when data is thin).
- `src/progress/store.py`: `class_plans` table (markdown with aliases, the alias→student map, the
  trace, source, model, note).
- `src/progress/metrics.py`: misconceptions carry `student_ids`; `pilot_report` aliases them.
- `src/platform_api.py` §4c: `get_class_plan`, `generate_class_plan` (ownership checked; a plan
  under 60 s old is reused). `api/main.py`: `GET`/`POST /api/teacher/classes/{id}/plan`.
- Web: `components/teaching-assistant.tsx` on `/teacher/class`: "Plan my next lesson", a progress
  line while it works, the plan, "How the assistant worked (N steps)", and a privacy line.
  Also fixed a page-wide horizontal scroll on narrow screens: the students table's `sr-only`
  header is absolutely positioned and escaped its non-positioned scroll box (`relative` fixes it).
- `tests/test_teacher_agent.py` (new): **28 checks**, with a scripted stand-in model, no network.

**Why these shapes.**
- **Names never reach the model.** Tools speak in S1…Sn (numbered by account creation, so stable);
  the map is stored with the plan and names are filled in only for that class's teacher. The test
  records everything sent to the model and asserts no name, username or id is in it. That's the
  answer to "you're sending children's data to an AI?"
- **Physics comes from reviewed lessons**, via `get_lesson_takeaway`, not from the model.
- **Read-only tools**, so the worst failure is poor advice that a teacher reads before acting.
- **A rules fallback, clearly labelled**, because a demo on stage or a teacher on a Monday morning
  must never get an empty card. It is honest about being rules, not AI.
- **An amendment to non-negotiable 3**, written into AGENTS.md: teacher-triggered, low-volume, never
  on a student's path.

**Verified.** All 15 test scripts, `tsc` and lint are clean. The adapter was exercised against a stub
client (5 tool declarations sent; history replayed as user/model/user; tool results and the nudge in
one turn; tools off on the last turn). In the browser the card produced a plan from the class's
real data, with names filled in. It was the **rules plan**, because Gemini rejected the key.

**Not verified: a live Gemini run.** The `GEMINI_API_KEY` in `.env` returns 401 both as an AI
Studio key and as a Vertex express key (it starts `AQ.`; AI Studio keys start `AIza`). The same
failure explains the doubt chat on this machine, on top of the blocked `grpc` DLL. A working key
is the user's to add, then one click on "Plan my next lesson" confirms the live path.

**The product vision, as stated by the user (2026-10-02).** *"During signup the student takes an
assessment that tells us their knowledge, interests and hobbies; we then generate specialised
content for them, and personalise the chapters based on their interaction with the app."* This
reverses the sprint's "no live generation" decision, so it was put back to the user as three
layers rather than built:
1. **A signup diagnostic** (no AI needed): 8–10 MCQs drawn from existing lesson checks, whose wrong
   options already map to misconceptions, plus interests and hobbies. This produces a starting
   estimate per concept. Instant and free. (ROADMAP M3.)
2. **Personalised chapters from interaction** (no AI needed): mark known concepts, insert a
   prerequisite lesson when a misconception shows up, spaced review. "Reorder, not regenerate".
   (M4/M5.)
3. **Generated content**, three options:
   - (a) the pre-written library only;
   - (b) **a hybrid, recommended:** the reviewed lesson stays the backbone, and an agent writes only
     a short personal story opening and one analogy for the student's own hobby. It is checked by
     a critic agent, cached per student × concept, and falls back to the nearest pre-written
     interest;
   - (c) whole lessons generated per student, which risks unreviewed physics for minors, plus cost
     and latency.

   (b) and (c) need a working, probably paid, Gemini key: the free tier's ~20 calls a day per model
   (§6) can't serve a class.

**Learned.**
- Check the credentials before designing around a live feature. The "doubt chat is broken by
  Windows" diagnosis in §9z was true but incomplete: the key was also dead, and only a direct
  call showed it.
- An absolutely positioned child (`sr-only`) inside `overflow-x-auto` escapes the scroll box unless
  the box is positioned, and widens the whole page. Measure with `scrollWidth` vs `clientWidth`.

## 9zd. Personalisation layers 1 and 2: the starting check and the learning plan (2026-10-02)

*User decision:* option **(b)** for generated content (a personal story and analogy per hobby on
top of the reviewed lesson; layer 3, not built yet), and **layers 1 and 2 first**.

**Changed.**
- `data/diagnostic.yaml` (new): the starting check as content. There are 8 concepts per class,
  chosen for *understanding* rather than arithmetic, since many misconception texts are slips like
  "Divides…" rather than beliefs. A Class 12 student also gets one Class 11 foundation
  (`second_law`). The file also lists the questions' source-interest order and 20 hobbies.
- `src/learner/diagnostic.py` (new): picks each question from a **different interest's** lesson
  than the student's own, so they never meet the same question again in their lesson and its
  first-try number stays honest. Grades by answer key; "not sure" is a real answer; validates
  hobbies (listed ids plus up to 2 own labels of at most 24 letters, so nothing sentence-like
  about a child is stored).
- `src/learner/plan.py` (new): `learner_state` builds likely-known concepts (right in the check)
  and open mix-ups (wrong in the check or in a lesson; closed once cleared). `personal_next`
  works on top of the unchanged engine: a review it wants stands; otherwise it skips likely-known
  concepts and brushes up a direct prerequisite that has a mix-up first, across chapters.
  `you_might` turns "Thinks X. <correction>" into "You might think X." (first sentence only, so
  the roadmap doesn't give away the lesson). `annotate_roadmap` adds known/focus notes.
- `src/progress/store.py`: `learner_profiles` (hobbies, check completed) and
  `diagnostic_answers`, kept apart from lesson `answers` so the baseline doesn't muddy the
  lesson numbers.
- `src/platform_api.py`: `get_diagnostic`, `submit_diagnostic` (once only, since it's the pilot's
  baseline), `get_learning_plan` (focus, known, suggested start, preferring the student's own
  class). A `_recommend` helper is now shared by `get_next_lesson` and `get_roadmap`, which gain
  `personal`, `personal_note` and `recommended`. `pilot_report` includes the starting check,
  pseudonymised.
- `api/main.py`: `GET`/`POST /api/diagnostic`, `GET /api/learning-plan`.
- `src/path/engine.py`: **`_load_subject` is cached** by path, mtime and size. One request parsed
  the 249-concept YAML up to 11 times. Measured before → after: roadmap 1330 → 75 ms, learning
  plan 2211 → 47 ms, chapters 791 → 44 ms. This was the latent issue listed in §2 since September.
- Web: `/start` (intro → hobbies → one question at a time with "I'm not sure yet" → the plan),
  and signup now lands there. `components/learning-plan.tsx` has the summary and a roadmap card
  ("Take the 5-minute starting check", or "Your plan · N mix-ups to fix" with "Fix this" links and
  a suggested start). Roadmap concepts get "Know it?" / "Focus" badges with the note; "Next up"
  follows the server's `recommended`. Roadmap status lines no longer say "Best 3/3", since checks
  are right/wrong only.
- `tests/test_learner_plan.py` (new): **48 checks**.

**Why this way.**
- **No AI in layers 1–2**, on purpose. The lesson checks already encode misconceptions, so a
  diagnostic is a lookup, which is instant, free and testable. That leaves the AI budget for
  layer 3, where it adds something a lookup can't.
- **A student who skips the check sees exactly the old behaviour**, wording included; a test
  pins it. Personalisation only adds, and nothing is ever locked.
- **The check is taken once**: it is the "before" picture for the pilot. A later post-test
  would be a separate feature, not a retake.

**Verified in the browser:** a new cricket Class 11 student, signed up through the API (the app
window was minimised, so the page was driven with JS clicks). /start went intro → 3 hobbies (one
typed) → 8 questions (3 right, 3 wrong, 2 not sure) → plan: 3 known, 3 mix-ups in the second
person, "Start with Motion in a Straight Line". The roadmap showed the plan card, "Know it?" on
Displacement, "Focus" on Acceleration, and "Next up" on Position.

**Learned.**
- The YAML-reparse cost had been invisible for weeks because each endpoint paid it a few times.
  New code that calls the engine more made it 1–2 s per request. Profile before guessing: one
  `cProfile` run named the culprit at once.
- JSX dropped the space in `{n} quick questions` again (same as §9z). An explicit `{" "}` fixes it.
- Test data: student `start.check` (Class 11, cricket) in the local DB, from this verification.

## 9ze. Layer 3: personal stories, and a provider layer for free models (2026-10-02)

*User decisions:* show the personal story first, with the lesson's pre-written story "in a
drop box" (collapsible); use **OmniRoute and free models for now**, and buy a Gemini key once
it works as planned.

**Changed.**
- `src/llm/` (new; the start of ROADMAP M1a): `chat()` over any **OpenAI-compatible** endpoint
  using httpx (no new dependency). It has a fallback chain, Bearer key, tool calls and
  `parse_json_object` for chatty free models. Configured by `LLM_BASE_URL` (default OmniRoute,
  `http://localhost:20128/v1`), `LLM_API_KEY`, `LLM_MODEL`, `LLM_FALLBACK_MODELS`,
  `LLM_CRITIC_MODEL` and `LLM_TIMEOUT_SECONDS`, read from the environment or `.env`. With
  `LLM_MODEL` unset the layer is off and every feature uses its non-AI fallback. Gemini later is a
  config change (Google's OpenAI-compatible URL). `.env.example` documents both setups.
- `src/learner/personal_story.py` (new) plus `prompts/personal_story_{writer,critic}.txt`:
  - picks a hobby that fits the concept's domain (`fits` and `interest` added to the hobbies in
    `data/diagnostic.yaml`; never the student's own lesson interest; own hobbies go to the writer,
    which may decline);
  - the writer gets the lesson's "The physics" and "Key takeaway" plus the student's open mix-up
    (first sentence), and no identity;
  - deterministic guards run next: JSON, word limits, **no digits at all**, no links or maths;
  - a critic call follows, strict and fail-closed, with one retry that feeds back the problems;
  - results are stored per student × concept, tied to a hash of the lesson text, and errors wait
    30 minutes before a retry;
  - generation runs on a 2-thread pool, for the opened lesson and the next two.
- `src/progress/store.py`: `personal_stories` table.
- `src/platform_api.py`: `get_next_lesson` adds `lesson.personal_story` (ready / pending / none)
  and starts the next two; `get_personal_story` for polling. `api/main.py`:
  `GET /api/personal-story`.
- `src/agents/teacher_agent.py`: `OpenAICompatModel`. The assistant now tries the src/llm models
  (OmniRoute) first, then Gemini direct, then rules. Tool-call ids are carried through the loop,
  since the OpenAI format needs them.
- Web: `components/personal-story.tsx`:
  - **ready:** a "Your story" card (story, "In badminton terms", "Where the comparison stops", and
    an AI-written-and-checked label), with the original under "Read the original Cricket story";
  - **pending:** the original as usual plus "Writing a badminton version…", polling every 3 s for
    about a minute;
  - **none:** exactly as before.
- `tests/test_personal_story.py` (new): **35 checks**, including the HTTP client and the teacher
  agent against `httpx.MockTransport` playing OmniRoute.

**Why these shapes.**
- **One OpenAI-compatible client instead of an OmniRoute-specific one.** OmniRoute, OpenRouter,
  Groq and Gemini all speak it, so "free now, paid Gemini later" costs no code.
- **Fail closed here, unlike the older judges.** Availability doesn't matter for a story, because
  the reviewed one is always there; correctness for a minor's lesson does.
- **No digits, enforced in code.** An invented number is the cheapest way for a model to slip in
  wrong physics; banning numbers outright is easy to check and costs the story nothing.
- **Background generation and prefetching** keep the lesson instant. Free models can take tens of
  seconds per call.

**Verified.** All 17 test scripts, `tsc`, lint and the validator are clean. In the browser, a story
row was seeded by hand for the test student `start.check` (OmniRoute isn't installed here, so
nothing can be generated live). The lesson showed "Your story · 🏸 Badminton" (cricket skipped as
the lesson interest), the analogy, the limit and the label, with "Read the original Cricket story"
closed; opening it showed the cricket story. A lesson without a story looked exactly as before.
**Not verified:** a live generation through OmniRoute, and the "being written…" polling state in
the browser.

**Rules amended (AGENTS.md):** non-negotiable 3 gains a second exception (personal stories:
background-only, never blocking, fallback always shown). Non-negotiable 8: OmniRoute through
`src/llm/` was the user's explicit request; new agents use `src/llm/`, while the four older
agents still call google-genai until the rest of M1a.

**A caution recorded for the user.** OmniRoute's "keyless" free pools include web-scraping
providers (e.g. `duckduckgo-web`). Those are unreliable and of doubtful terms. Prefer connecting
real free tiers inside OmniRoute: an AI Studio key, Groq, or OpenRouter's free models.

**Learned.** A long multi-heredoc shell command failed to parse and ran nothing; for prose, write
it to a file first.

## 9zf. Reviewing personal stories: a report button and the teacher's story view (2026-10-02)

The user asked for the two review pieces left open in §9ze, and to be reminded to set up
OmniRoute later. The reminder is in the assistant's memory and in AGENTS.md's machine issues.

**Changed.**
- `src/progress/store.py`: `personal_stories` gains `hidden`, `hidden_by` (student / teacher),
  `report_reason` and `reported_at`, added the additive way (`PRAGMA table_info` + `ADD COLUMN`).
  New: `list_personal_stories`, `set_story_visibility`.
- `src/learner/personal_story.py`: `view()` treats a hidden story as "none", so the student gets
  the reviewed story. It stays "current", so the same lesson never rewrites it.
- `src/platform_api.py`:
  - `report_personal_story`, with **fixed reasons only** (wrong physics, confusing, not
    appropriate, something else) and no free text, since a child's typed comment is personal data;
  - `list_class_stories`: the full text of every story in the class, reported first, plus counts
    including attempts that failed the checks;
  - `set_class_story_hidden`: the teacher hides or restores. A report stays on record even if the
    story is restored. Ownership is checked like password resets, with one NotFound for every
    "not yours".
  - `pilot_report` adds the stories, pseudonymised.
- `api/main.py`: `POST /api/personal-story/report` (student), `GET /api/teacher/classes/{id}/stories`,
  `POST /api/teacher/stories/{student}/{concept}/visibility` (teacher).
- `scripts/pilot_report.py`: a "Personal stories" line (written / reported / hidden / not written)
  and `personal_stories.csv`.
- Web:
  - `components/personal-story.tsx`: "Something wrong with this story?" opens the four reasons.
    Choosing one hides the story at once, with a thank-you note and the original story.
  - `components/class-stories.tsx` on `/teacher/class`: counts, then each story with student,
    concept, hobby, a status chip, the student's reason, the full text (open by default when
    reported and hidden), and "Hide this story" / "Show it to X again".
- `tests/test_story_review.py` (new): **21 checks**.

**Why.** Two checks before any AI story stays in front of a child: the critic agent before it's
shown, and people after it's shown. The student is the first to notice a confusing story, the
teacher the best judge of it. Hiding on report, before review, is the safe default: the reviewed
story is always there to fall back on.

**Verified in the browser** (stories seeded by hand, since OmniRoute isn't installed):
- as `test.t`: the report button showed the four reasons; "The physics seems wrong" swapped in the
  thank-you note and the original story, and it stayed hidden after a reload;
- as teacher `metrics.check`: "1 written · 0 showing · 1 reported", with the reason and the full
  text; "Show it to Test again" moved it to "Reported · shown again". Page width fits.

All 18 test scripts, `tsc`, lint and **`npm run build`** are clean (13 routes). The user's servers
had stopped, so the API and web were restarted from `.claude/launch.json`; the API now runs on
`venv`.

**Learned.** Restoring a reported story must not erase the report: the pilot needs to know how often
students flag AI text, whatever the teacher decided afterwards.

## 9zg. Robustness, part 1: login rate limiting, error pages, the logout redirect (2026-10-02)

The user started the robustness and polish list. Order chosen for a real classroom: rate
limiting → error pages → toasts and dark mode → a 30-student load test.

**Changed.**
- `api/ratelimit.py` (new): an in-memory `LoginLimiter`, built around the fact that **a whole
  class shares one school IP**:
  - per account, 8 wrong passwords in 15 min lock that username for 10 min;
  - per IP, a much higher cap of 100 failures in 15 min stops spraying;
  - unknown usernames count the same (no enumeration), and a right password clears the count;
  - tunable with `ECOLEARN_LOGIN_*`.
- `api/main.py`: `_check_password_attempt` wraps student and teacher login and both
  change-password endpoints. A locked attempt answers **429 with Retry-After without checking the
  password**, so a lock can't confirm a guess. A teacher's password reset clears the student's
  lock.
- Web: `app/not-found.tsx` (any unknown URL, with the nav; a real 404 status), `app/error.tsx`
  (Next 16's `unstable_retry`, "Your progress is saved", a reference digest) and
  `app/global-error.tsx` (self-contained `<html>`/`<body>`, inline styles; only if the root layout
  fails).
- **The logout redirect bug** (found in §9za): `RequireAuth` reacted to the signed-out state before
  the nav's redirect and sent the user to `/login?next=<the page they were on>`. On a shared
  classroom computer, that hands the next student the previous one's page. `auth-provider` now
  records `loggedOutOnPurpose`, so a deliberate logout goes to the plain login page; an expired
  session still keeps `?next=`.
- `tests/test_rate_limit.py` (new): **13 checks**, with a fake clock.

**Limits written into the code, not hidden.** The counts are per process (lost on restart; several
workers would need a shared store such as Redis). Behind a proxy the client IP must come from its
header. A classmate who knows a username can lock it for 10 minutes; the short lockout and the
teacher reset keep that small.

**Verified.** All 19 test scripts, `tsc` and lint are clean. In the browser, `/no-such-page` showed
the new page with the nav and returned 404. Logging out from a lesson landed on `/login` with no
`next`.

## 9zh. Robustness, part 2: a 30-student load test, and making it pass (2026-10-02)

**Changed.**
- `scripts/load_test.py` (new): starts its own API on a temporary DB (the real `progress.db` is
  never touched), creates a teacher and a class of N, and runs every student through a lesson **at
  the same moment**: login → session → chapters → roadmap → learning plan → starting check → next
  lesson → open it → reading time → answer → rate → roadmap. Meanwhile the teacher refreshes
  insights, stories and the class page. The AI is switched off for the run. It reports p50/p95/max
  per endpoint and fails on any error or a p95 above 2 s.
- `src/file_cache.py` (new): `cached_parse(path, parse)`. A file is parsed once per (path, mtime,
  size), so edits are picked up with no restart; the result is shared and read-only. Used for
  lesson files (`authored.parse_lesson_file`), `data/interests.yaml`, `data/diagnostic.yaml` and
  `.env`.
- `src/content/lesson_service.py`:
  - one lesson **index** (a single directory walk) replaces a glob per lookup;
  - the "which concepts or chapters have lessons" scans are cached for 30 s;
  - **a miss is never trusted from the cache**: it gets a direct look on disk, so a lesson written
    a moment ago is found at once.
- `src/progress/store.py`: the schema (about 20 CREATE/PRAGMA/ALTER statements) is checked **once
  per DB file per process** instead of on every connection, and again if the file has vanished.
  `sqlite3.connect(..., timeout=15)` waits for the write lock rather than failing.
- `src/llm/client.py` / `src/agents/teacher_agent.py`: **a variable set in the environment wins
  even when empty**. Before, `GEMINI_API_KEY=` fell through to `.env`, and the load test's rules
  plan made real calls to Google with the dead key: **26 s**.

**Results (30 students, one process, this laptop):**

| | first run | after |
|---|---|---|
| whole class | 52.4 s | 10.6 s |
| p50 | 1106 ms | 455 ms |
| p95 | 4694 ms | 1176 ms |
| starting-check submit p95 | 6022 ms | ~940 ms |
| teacher plan | 26551 ms | 41 ms |
| errors | 0 | 0 |

45 students: 14.6 s, p95 1614 ms, 0 errors. Single-journey CPU went from 1.4 s to 0.13 s; one
`cProfile` run per step pointed at each fix in turn (YAML re-parsing, then SQL schema checks, then
globs).

**Why it mattered.** One Python process serves the whole class, so CPU time per request queues up.
A student waiting 6 s after "See my plan" in front of a teacher reads as "it's broken". None of this
showed in single-user testing.

**Learned.**
- **Load-test before the pilot, not after.** Every one of these costs was invisible to one user and
  obvious at thirty.
- An empty environment variable must mean "off", or switching a feature off in one place quietly
  switches it back on from another.
- Caching "not found" is the dangerous part of a file cache. Cache hits, re-check misses.

## 9zi. Robustness, part 3: dark mode, toasts, accessible colours (2026-10-02)

**Changed.**
- `web/app/globals.css`: a real dark palette, slate with the brand colours. Indigo `#818CF8` with
  dark button text (`--primary-foreground`), because no single indigo passes both "white text on
  it" and "as text on a dark card". Components now use `text-primary-foreground` /
  `text-success-foreground`, never `text-white`.
- **Light mode accessibility fix:** amber `#F59E0B` and green `#10B981` were 2.2:1 and 2.5:1 on
  white, below WCAG AA for the small labels that use them. They are now `#B45309` / `#047857`
  (4.8–5.5:1).
- `components/theme-toggle.tsx`: device → light → dark in the nav, saved in localStorage (in a
  try/catch); `THEME_BOOT_SCRIPT` in `<head>` applies the choice before first paint (no flash);
  `suppressHydrationWarning` on `<html>`. Markdown gains `dark:prose-invert`. Lesson figures stay
  on white cards on purpose, because they were drawn for white.
- `components/toast.tsx`: a small toast system with no dependency and a polite live region. Used
  where an action had no visible confirmation: a teacher hiding or restoring a story, and the
  teaching assistant returning a plan (new, reused, or rules-made).
- Nav at 375 px overflowed by 15 px once the toggle was added: the wordmark text now hides below
  400 px (still read by screen readers) and the gaps are tighter.

**Verified in the browser** (computed styles):
- dark: Continue button 6.0:1, amber labels 8.3:1;
- light: labels 4.8:1, button 6.3:1;
- the theme is applied before React loads, with no hydration warnings;
- the toast appeared on hide;
- no horizontal scroll at 375 px on the roadmap, lesson and teacher class pages.

All test scripts, `tsc`, lint and `npm run build` are clean.

*Session paused here:* the Pro 5-hour window reached 100% (weekly 24%). Robustness list done:
rate limiting, error pages, logout, load test, dark mode, toasts. Skeletons were already present on
every data page.

## 9zj. "I can't log in, the page just refreshes": opening the app at 127.0.0.1 (2026-10-02)

**The bug** (the open thread from §9z, finally reproduced). Opened at `http://127.0.0.1:3000`
instead of `localhost:3000`, two separate things broke:
1. **`next dev` refuses its dev scripts to any host but the one it started on** (localhost). The
   page rendered from the server, but none of its JavaScript ran, so "Log in" and signup fell back
   to a plain HTML form submit: the page reloaded and nothing happened. Console:
   `WebSocket connection to 'ws://127.0.0.1:3000/_next/webpack-hmr' failed`, and no React on the
   form.
2. Even with scripts running, a page on `127.0.0.1` calling the API on `localhost` is a
   **different site**: the `SameSite=Lax` session cookie isn't sent, so a successful login
   bounced back to the login page. CORS also allowed only `localhost:3000`.

**Changed.**
- `web/next.config.ts`: `allowedDevOrigins: ["127.0.0.1"]` (see
  `node_modules/next/dist/docs/.../allowedDevOrigins.md`).
- `web/lib/api.ts`: `API_URL` follows the page's host when both are loopback names, so the API is
  always same-site with the page.
- `api/main.py`: CORS allows `http://127.0.0.1:3000` too.

**Verified in the browser on both hosts.** On `127.0.0.1:3000`: login → roadmap; signup step 1 →
step 2 → `/start`; a refresh keeps the session. On `localhost:3000`: the same account logs in.
`test_api_auth`, `test_teacher`, `test_rate_limit`, `test_story_review`, `tsc` and lint are clean.
The user's web dev server was restarted to read the new config (Next reads it only at startup).
Test account `loop.check` was added to the local DB.

**Learned.** "The page just refreshes" on a form means the client JavaScript never ran. Check
whether React is attached to the form (`__react*` keys) before suspecting the API.

## 9zk. Handoff: everything a new session needs, in the folder (2026-10-02)

The user is continuing in another session. **Changed:**
- `AGENTS.md` §1–§2 rewritten from the actual state, replacing a pile of crossed-out steps:
  - what a student and a teacher can do today;
  - a "where things live" table (file → history entry);
  - the decisions as they now stand (three live-AI exceptions, OmniRoute now / Gemini key later,
    personal story first with the original in a collapsible box);
  - an honest "not built or not verified" list and four candidate next steps for the user to
    choose from;
  - machine issues, including the OmniRoute reminder the user asked for;
  - local test accounts (no passwords in the repo) and the questions still open with the user.
- `PROJECT_HISTORY.md` header: how to read it (§1–§8 are the 2026-09-21 snapshot; §9+ is the
  dated log).

Nothing needed for the next session lives outside the folder, apart from the gitignored local
pieces listed in AGENTS.md §6 (`.env`, `data/progress.db`, `venv/`, `.claude/launch.json`).

## 9zl. The end check: the pilot's "after" (2026-10-02)

*User request:* first of the finals priorities, set against the judging criteria the user shared
(Innovation 30, Technology readiness 20, Commercial 15, Education significance 15, Presentation 10,
Demo 10). A pilot with only a starting check can show usage, not learning.

**Changed.**
- `src/learner/diagnostic.py`: **two counterbalanced forms.** For each starting-check concept,
  form 0 and form 1 are the checks of two *different* interests' lessons, never the student's own.
  `form_for(student_id)` (a SHA-256 bit, stable) picks which a student gets at the start; the end
  check (`choose_end_questions`) asks each concept from an interest that is neither their own nor
  the one used at the start, built from the stored starting-check rows so the pairs survive config
  changes. `compare()` gives one student's before → after: right / mix-up / not sure, `fixed`
  (mix-up → right), `learned` (not sure → right), `slipped` (right → not right), and `studied` per
  concept. Grading is shared (`grade_chosen`, `present`).
- `src/progress/store.py`: `end_check_answers` table (same shape as `diagnostic_answers`),
  `learner_profiles.end_check_completed_at`, `classes.end_check_opened_at`, all additive.
  `get_learner_profile` and class dicts carry the new fields.
- `src/progress/metrics.py`: `studied_concepts` (lesson opened or answered *before* the end check)
  and `check_gains` (class before → after over paired answers, studied vs not studied, per concept).
- `src/platform_api.py` §2c: `get_end_check` / `submit_end_check` (status `not_open` |
  `needs_start` | `open` | `taken`; once only), `get_class_checks`, `set_class_end_check`. The
  starting check now uses the student's form. `pilot_report` adds `end_check` rows (pseudonymised)
  and `check_gains`. `api/main.py`: `GET/POST /api/end-check`, `GET
  /api/teacher/classes/{id}/checks`, `POST /api/teacher/classes/{id}/end-check`.
- `scripts/pilot_report.py`: a "Starting check → end check" section and two more CSVs.
- Web: `/end-check` (intro → one question at a time → before → after), `components/check-result.tsx`,
  a roadmap banner while it's open (`EndCheckCard`), and `components/class-checks.tsx` on
  `/teacher/class` (open/close, tiles, studied vs not studied, per idea, per student). The question
  card is now shared with `/start` (`components/check-question.tsx`).
- `tests/test_end_check.py` (new): **75 checks**. `tests/test_learner_plan.py`: both forms
  checked; grading tests use the student's form (58 checks).

**Why this way.**
- **The teacher opens it**, rather than it appearing after N days: the whole class takes it at the
  same point of the pilot, and the teacher decides when "the end" is. Self-signup students never
  see it, since nobody can open it for them and they aren't in a pilot class.
- **Parallel questions, not the same ones.** Re-asking the starting questions would partly
  measure memory of those questions. The other interests' checks on the same concept were already
  written to catch the same misconceptions, so no new content was needed.
- **Counterbalanced**, because the two forms were written independently and one may be easier. With
  half the class on each order, a difference in difficulty cancels on average instead of showing up
  as a fake gain (or a fake loss).
- **Studied vs not studied** is reported next to the headline. Without a control group, it's the
  most honest check available: if concepts students never opened improve as much, the gain isn't
  the lessons' (practice with the format, or school teaching in parallel).
- **A separate table**, so the baseline is never overwritten and the learning plan's meaning
  doesn't change. End-check answers don't feed the plan; that can come later.
- No AI anywhere in it: the same answer-key lookup as every other check.

**Verified in the browser** (at `127.0.0.1:3000`, so the user's `localhost` session wasn't touched):
a seeded class (see AGENTS.md test data). As student `bilal.k`: the roadmap banner → `/end-check` →
8 questions → "You fixed 1 mix-up" with 2 → 5 right, 3 → 1 mix-ups, idea by idea, and "worth
another look". As the teacher: 3 of 3 started, 2 of 3 finished, right answers 25% → 63% over 16
paired answers, mix-ups 6 → 2 (3 fixed, 3 learned, 0 slipped), studied 0% → 100% (2) vs not
studied 29% → 57% (14). All re-derived by hand from the seeded answers. Close/open toggles; no
sideways scroll at 375 px.
The full deterministic suite, the load test (p95 1.2 s, PASS), `tsc --noEmit` and lint pass.
`npm run build` was not run: a `next dev` from another session was serving `web/`, and both write
`.next` (§13).

**Learned.**
- The forms are not psychometrically matched. That's a limitation to state in the pitch, not to
  hide: counterbalancing protects the class average, not each student's comparison.
- The per-student tallies wrapped one word per line at 375 px; `whitespace-nowrap` per part in a
  `flex-wrap` keeps "3 mix-ups" together.
- Git Bash heredocs mangle `\n` inside Python patch scripts. Write the script to a file instead.

## 9zm. "My mix-ups" and "How sure are you?" (2026-10-03)

*User request:* items 1 and 2 of the pre-pilot list: both change what the pilot records, so they
had to land before students start.

**Changed.**
- `src/learner/plan.py`: `mix_up_history(start_rows, lesson_rows, end_rows)` (pure). Every concept
  the student got wrong with a named misconception, with a status from the answers after the
  latest wrong one: **fixed** = right on a *different* question (a question is a lesson's check,
  `(concept, interest)`; the starting check's football question *is* the football lesson's
  check); **recheck** = right only on the same question; **active** = nothing right since. "Not
  sure" counts for neither. Also `sure` (latest wrong answer), `times`, where it was found/fixed.
- `src/learner/diagnostic.py`: `CONFIDENCE_LEVELS` (sure | think | guess) and `clean_confidence`.
  `grade_chosen` / `grade` take `confidence` per concept, keep it for a picked option, drop it for
  "not sure".
- `src/progress/store.py`: a `confidence` column on `answers`, `diagnostic_answers` and
  `end_check_answers` (additive); `record_answer(..., confidence)`.
- `src/platform_api.py`: `submit_assessment(..., confidence=None)` stores it and adds a line to the
  feedback when it matters (sure and wrong; guessed and right); `submit_diagnostic` and
  `submit_end_check` take a `confidence` map; `get_mix_ups(student_id)`. `api/main.py`: the three
  request bodies take `confidence` (optional), and `GET /api/mix-ups`.
- `src/progress/metrics.py`: each misconception gets `sure` (students who chose it while sure);
  the summary gets `by_confidence` (first-try accuracy per level) and `sure_but_wrong`.
  `scripts/pilot_report.py` prints them.
- Web: `components/confidence-picker.tsx`, shown in the shared question card and on the lesson
  check once an option is picked; Next / "Check my answer" wait for it. `/mix-ups` (three tiles,
  then To fix / Check again / Fixed with "Open the lesson"), a "Mix-ups" nav link and a link from
  the roadmap's plan card. Teacher insights: "· N sure of it" on each misconception and a "Sure but
  wrong" tile.
- `tests/test_mix_ups.py` (new): **32 checks**.

**Why this way.**
- **"Fixed" needs a different question.** After a wrong pick the lesson check shows the right
  answer, so a correct retry on the same question mostly proves the student read the screen.
  Calling that "fixed" would repeat the "mastered after one answer" overclaim (AGENTS.md's honest
  list). "Check again" is honest and still encouraging, and the end check or another interest's
  lesson can then confirm it.
- **Confidence is required in the UI, optional in the API.** Pilot data with gaps is weak for the
  one question it answers (were they sure when wrong?), and a tap costs a student a second.
  Streamlit and older clients keep working without it.
- **"Not sure" stays a separate option**: it already says how sure the student is, so it is never
  asked twice.
- **Sure-and-wrong is what teachers see first**: it separates a firmly held misconception (worth
  class time) from a guess.
- The learning plan (`learner_state`) is unchanged on purpose: it still closes a mix-up once the
  concept is cleared. The mix-ups page is the stricter, student-facing view.

**Verified in the browser** (at `127.0.0.1:3000`, test student `chitra.n`): the lesson check shows
"How sure are you?" only after an option is picked and keeps "Check my answer" disabled until
then; sure and wrong → the feedback says so; a correct retry with "I think so" → acceleration under
**Check again**, "came up 2 times", "you were sure". The end check gates Next on confidence for an
option but not for "not sure"; afterwards acceleration and projectile motion moved to **Fixed**
(in the end check), Newton's third law stayed **To fix**. No sideways scroll at 375 px with the
extra nav link. Teacher view: "1 of 1 students · 1 sure of it" and the "Sure but wrong" tile.
Full suite, load test (p95 1.1 s), `tsc` and lint pass; `npm run build` not run (a `next dev` from
another session serves `web/`).

**Learned.**
- The retry after a wrong pick still says "Mastered!": the overclaim this page avoids is still on
  the lesson check itself. That's item 3 on the pre-pilot list (mastery after two separate right
  answers, plus a revision queue).

## 9zn. Mastery needs two questions, a revision queue, and an AI usage log (2026-10-03)

*User request:* items 3 and 4 of the pre-pilot list.

**Changed (mastery, item 3).**
- `src/learner/plan.py`: `_answer_events` (every answer from the starting check, lesson checks,
  end check and revision, by question = interest), shared by `mix_up_history` and the new
  `mastery_evidence`: the questions answered right *without* having got that question wrong
  first. `MASTERY_EVIDENCE = 2`.
- `src/platform_api.py`: a lesson check now scores **3 (mastered) only with two pieces of
  evidence**; a right answer otherwise scores **2** ("cleared": the engine moves on, unchanged).
  Results carry `mastery_note`. New `get_revision` (cleared concepts, each with a question from an
  interest the student has never seen, due `ECOLEARN_REVISION_HOURS` (default 20) after its last
  answer), `get_revision_question`, `submit_revision`. `api/main.py`: `GET /api/revision`,
  `GET /api/revision/question`, `POST /api/revision`.
- `src/progress/store.py`: `review_answers` (own table, so first-try metrics keep their meaning),
  `get_concept_answers` (one concept's rows from all four tables on one connection).
- Web: `/review` (ready now / coming up, a fresh question without "not sure", confidence
  required, the result with the mastery note); a roadmap banner when revision is due; roadmap
  line "Right once · one more question to master it"; the lesson-check result says "Right!" plus
  the note instead of "Mastered!"; "Check again" mix-ups link to a new question.
- `tests/test_mastery.py` (new): **33 checks**. `tests/test_mcq_grading.py` now pins the new rule
  (right after being shown the answer = 2, not 3).

**Changed (AI usage log, item 4).**
- `src/llm/client.py`: every call, answered or failed, goes to a usage sink with model, tokens
  (from the response's `usage`), latency and tags. Tags come from `usage_context(feature=...,
  student_id=..., class_id=...)`, a context variable, so no signature changed and the tests'
  fake `chat` functions still work. A failing sink never breaks a call.
- `src/platform_api.py` registers `store.record_llm_call` as the sink; the story writer, the
  critic and the teacher agent tag their calls; the doubt chat logs a row without tokens (its
  pipeline is still google-genai). `pilot_report` adds `ai_usage` and pseudonymised call rows.
- `data/llm_prices.yaml` (new): USD per million tokens and the ₹ rate, **typed from memory and
  marked so**; a reference model (`gemini-2.5-flash`, the paid key the user plans to buy).
- `src/progress/metrics.py`: `ai_usage` — per feature and total: calls, failures, tokens, median
  latency, actual ₹ (unlisted free models cost 0) and ₹ on the reference model; per student and
  per month. `scripts/pilot_report.py` prints it and writes `llm_calls.csv`.
- `tests/test_llm_usage.py` (new): **19 checks** (a mock-transport story run is logged as
  `story_writer` then `story_critic` with tokens; the cost arithmetic re-derived by hand).

**Why this way.**
- **Two different questions.** After a wrong pick the app shows the answer, so a retry proves
  little; and one right answer can be luck (one in four). Two different questions (another
  interest's check on the same concept) is the cheapest honest test of understanding, and needs no
  new content: every concept already has up to five checks.
- **Cleared still moves the path on.** Nothing is locked; only the word "mastered" got stricter.
  The engine's 2-vs-3 split already meant cleared vs mastered, so the engine didn't change.
- **A day's wait, not a lock.** Spacing helps memory, so revision items are "best after" a time,
  but a student can try one at once.
- **The usage log lives in the client, the storage in the boundary**: `src/llm` stays a thin
  client any agent can use, and logging can't take a model call down.
- **Two costs:** free models make the actual cost ₹0, which says nothing about the paid plan. The
  reference price answers "what would this pilot have cost on the Gemini key?"

**Verified in the browser** (`127.0.0.1:3000`, test student `asha.r`): a first-try right lesson
answer → "Right! … One more right answer, on a different question, masters it."; the roadmap line
"Right once · one more question to master it"; `/review` listed Position under "Coming up"; the
fresh question (football's check; no "not sure"; "Check my answer" waits for confidence) answered
right → "Position: mastered!". A dropped space ("masteredonce") was fixed with `{" "}`.

**Load test: red for a while today, for old and new code alike; green on the rerun.** It passed at p95 1.1 s in
§9zm; today `HEAD` (2621d70, before this change) and this change both fail the 2 s p95 bar,
because 30 simultaneous logins (bcrypt, CPU-bound) take ~4 s on both. Measured back to back from a
temporary worktree of `HEAD`. The comparison did find a real cost in this change: assessment p50
went from 480–700 ms to 840–1020 ms, because scoring read the student's whole activity over four
connections. `store.get_concept_answers` (one connection, one concept) brought it back to
580–770 ms vs 680–830 ms for `HEAD`. **Rerun later, with the machine quieter: PASS** (logins 0.6 s, all requests p95 1.4 s).

**Learned.**
- When a timing check fails, run the previous commit beside it before blaming either: here both
  failed, and the comparison still caught the real 300 ms regression the threshold alone wouldn't
  have pinned on this change.
- JSX dropped the space after `</span>` at a line end again (third time; §9z, §9zd): use `{" "}`.

## 9zo. Handoff for a new session (2026-10-03)

The user is continuing in another session. **Changed:** `AGENTS.md` §2: the current commit, what
was done since the last handoff (§9zl–§9zn), the user's stated order (OmniRoute first, then the
pre-pilot cleanup), next candidates ranked by the judging weights, machine notes (two API servers,
load-test timing, the pane's `localhost` session), two more test students, and the unreproduced
"Something went wrong" report (open thread 3).

**Learned.** The user has an **RTX 3090 (24 GB)**, the GPU behind M1a's self-hosted plan. Any
OpenAI-compatible local server (Ollama, llama.cpp, vLLM) plugs into `src/llm` with two `.env`
values, so a local backend needs no code.

## 9zp. "How the AI decided" (2026-10-03)

*User request:* the first item of the next-steps list (Innovation is 30% of the judging, and the
conference theme includes responsible AI).

**Changed.**
- `src/learner/personal_story.py`: `generate` records a **decision trail**: one entry per step,
  `{attempt, step, passed, problems, model}`, with steps `format` (readable JSON), `fit` (the writer
  declined), `rules` (`guard_problems`), `critic` (the second model's verdict) and `model` (a
  failed call). Saved with every outcome (ready, failed, no_fit, error).
- `src/progress/store.py`: `personal_stories.trail` (additive JSON column; old rows read as `[]`),
  `list_class_plans`.
- `src/platform_api.py`: `get_class_ai_decisions(teacher_id, class_id)`: story guardrail counts
  (attempted, shown, first draft, rewritten, blocked, declined, errors, reported, hidden by the
  teacher, rule-check and critic rejections), teaching-assistant plans by source with the latest
  fallback note, model calls for this class (by the class id or its students' ids) and a decision
  log with names, plain-words outcomes and trails. `api/main.py`:
  `GET /api/teacher/classes/{id}/ai-decisions`.
- Web: `components/ai-decisions.tsx` on `/teacher/class`, below the stories: the pipeline
  (writer → rule checks → AI critic → shown, with counts), four tiles (safe fallbacks, human
  review, teaching assistant, model calls), and the log, where each story expands into its steps
  with the reasons quoted.
- `tests/test_ai_decisions.py` (new): **17 checks**.

**Why this way.**
- **The trail is written where the decision is made** (inside `generate`), not reconstructed
  later: before this, a story that passed on its second draft kept no record of what the first
  draft got wrong, which is exactly the evidence that guardrails work.
- **Outcomes in plain words** ("Blocked: the student saw the reviewed lesson story"): the point for
  a teacher is what the *student* saw, not the status code.
- The teaching assistant's own tool calls were already listed under each plan (§9zc), so this
  panel only counts its plans by source rather than repeating them.

**Verified in the browser** (`127.0.0.1:3000`, test teacher `endcheck.teacher`): a scripted story
run for `asha.r` (draft 1 had a number → rule checks sent it back; draft 2's analogy said force is
"used up" → the critic rejected it as the very misconception the lesson corrects → blocked) shows
as pipeline counts 1 / 1 / 1 / 0, "Safe fallbacks 1", and an expandable log entry with both
reasons quoted. No sideways scroll at 375 px. **`npm run build` passed** for the first time this
session (all 18 routes, incl. `/end-check`, `/mix-ups`, `/review`): the dev server was this
session's own, so it could be stopped first.
Load test: red on the first run (p95 4.6 s); back to back against `HEAD` in a temporary
worktree, this change matched or beat it both rounds and its second round passed (p95 1.37 s vs
2.07 s for `HEAD`): the machine's load again, as in §9zn.

**Learned.**
- `MAX_ATTEMPTS` is 2, so a story is either right first time, rewritten once, or blocked. The test's
  first scenario assumed three drafts.

## 9zq. Handoff refresh (2026-10-03)

The user is continuing in another session. `AGENTS.md` §2 now points at `e920f30` and lists
§9zp as done. Next candidates are unchanged (demo dataset, doubt chat without grpc, landing page,
dev-only error detail, local GPU backend); the user's own order is still OmniRoute (or the 3090),
then the pre-pilot cleanup.

## 9zr. Demo dataset (2026-10-03)

**Changed.**
- `scripts/seed_demo.py`: fills a *separate* database (`data/demo.db`, gitignored) with a fictional
  class: teacher `demo.teacher`, "Class 11-B Physics", 25 students (cricket 9, football 8, gaming 8),
  all with one shared throwaway password (a constant in the script). 23 took the starting check, 20
  the end check; ~200 lesson checks, ~70 revision answers, ~11 personal stories with decision
  trails, a rules-based teaching-assistant plan. Refuses to write to `data/progress.db`;
  `--reset` rebuilds; fixed seed, so the same class every time.
- `tests/test_seed_demo.py`: refusal, class shape, before < after, studied gains > unstudied,
  labels, empty usage log, determinism.

**Why this way.**
- It calls the real code (`submit_diagnostic`, `_grade_multiple_choice`, `submit_revision`,
  `submit_end_check`), then moves timestamps back over three weeks in SQL. So mastery, the mix-up
  list, the revision queue and every dashboard number come from the real rules, not painted rows.
- Student behaviour is a small model: an ability per student, a per-concept difficulty, a favoured
  wrong option per question (so some mix-ups are common), "sure/think/guess" tied to ability, and
  students study the ideas their check flagged first. End-check answers depend on the starting
  answer (known stays known, studied-and-wrong mostly fixed, unstudied-and-wrong mostly not).

**Honesty.** Everything is invented. Story texts are placeholders marked `[Demo placeholder]`, model
`demo-seed`. **No AI usage is invented**: the usage log (tokens, cost) stays empty, and the
decision panel shows 0 model calls. Don't quote these numbers as pilot results.

**Learned.**
- First version drew every answer independently, so "ideas not studied" got *worse* between checks
  (regression to the mean: the unstudied ones were the ones they already knew). Answers have to
  depend on the earlier state or the control group looks broken.
- `MAX_ATTEMPTS` is 2, so a blocked story has two drafts, not three.

Use: `venv\Scripts\python.exe scripts\seed_demo.py --reset`, then start the API with
`$env:ECOLEARN_PROGRESS_DB = "data\demo.db"`.

## 9zt. Done ticks, concepts open in order, only a teacher sets the class (2026-10-03)

**Changed.**
- **P3, the roadmap tick.** One right answer is "cleared" (partial) since §9zn, and the roadmap
  still said "Available". Now: green ✓ **Done** ("a new question tomorrow (Review) masters it"),
  gold ✓ **Mastered**, and the header reads "N of M concepts done · K mastered".
- **P2, locks (user decision).** Chapters stay open. Inside a chapter concepts open in order
  (`platform_api._concept_locks`): the first written concept is open; the next opens when the one
  before is passed (right once, mastered, or the starting check says they know it). Already-tried
  concepts and concepts with a mix-up from the check stay open (the plan sends students there).
  "Coming soon" concepts never block. The roadmap rows carry `locked` / `locked_reason`; the
  lesson fetch refuses a locked concept with "Finish X first." (the UI shows a Lock row).
- **Class 11 / 12 is the teacher's.** The chapter picker lists only the student's class; the API
  refuses another class's chapter (`_require_chapter_for_level`); Settings shows the class
  read-only; `PATCH /api/profile` answers 403 if a different level is sent (re-sending the same
  one is fine); new `set_student_level` + `POST /api/teacher/students/{id}/level`, and a Class
  dropdown in the teacher's students table. A Class 12 student defaults to Current Electricity.
- Tests: new `tests/test_concept_locks.py` (24 checks); `test_chapter_coverage` now uses a Class
  11 empty chapter and `test_story_review` records an attempt before opening a concept directly.

**Why.** Students saw progress move without a tick; the user wants a game-like path (milestones)
but not a wall: so the lock is per concept, the starting check can open things, and a teacher can
move a student up. **This replaces the old rule "nothing is ever locked" (2026-09-22) for concepts**;
chapters are still never locked.

**Learned / caveats.**
- A student who is wrong repeatedly isn't stuck: after a wrong pick the right answer is shown, so a
  retry clears the concept. A lucky guess on the starting check opens the concept after it.
- Self-signup students still pick their class at signup (and can't change it after).
- The demo dataset (§9zr) was seeded straight through the grading code, so its students have
  out-of-order progress: some concepts are open ahead of unfinished ones. That's fine for a demo.
- Existing students' changed level keeps their answers; the starting check isn't re-taken.

## 9zu. The roadmap as a level map (2026-10-04)

**Changed.**
- `web/components/roadmap-path.tsx` (new) + `web/app/(app)/roadmap/page.tsx` (rewritten): the path is
  now a winding level map. Big round nodes in six states (Mastered gold, Done green, Next up with a
  pulsing ring and a bobbing START tag, Open, Locked, Coming soon), a dotted line ahead and a
  green line behind finished steps. Tap a step (node or label) to select it; a slim sheet at the
  bottom says what it is and offers the one action (Start / Try again / Review / Locked). A header
  card with a progress ring (green = done, gold = mastered), chips ("2 done", "4 to unlock") and the
  interest's emoji and accent. A "Nice work! X is done" banner and a node pop when a step became
  done since the student last looked (sessionStorage per tab; if storage is blocked nothing pops).
- `globals.css`: "Roadmap motion" keyframes, plain CSS, off under `prefers-reduced-motion`. **No new
  dependency** (no Framer Motion): CSS covers pulse, bob, pop, shake and slide-in.
- `learning-plan.tsx`: the Revision card read "6 ideas areready": the text was split into flex items
  and the space collapsed. Wrapped in a span.

**Why.** The user wants a more interactive, game-like UI (a Replit-style polish) and chose to build
it here, one screen at a time, starting with the roadmap. Nothing in the API changed: it still reads
the same `getRoadmap` rows (`locked`, `locked_reason`, `progress_status`, `personal`).

**Verified** in the browser on the demo class (`aarav.k`, Laws of Motion): header, ring, path, a
locked step's sheet, the phone width (375 px: no sideways scroll). **Not checked:** the "pop"
banner (needs a step to finish between two visits), screen readers, light theme.

**Learned.** A fixed row height (112 px) makes the connecting curve one SVG with no measuring.
A zero-length SVG arc with a round cap still draws a dot: render the arc only when it has length.
After `npm run build`, delete `web/.next` before `next dev`, or the dev server answers 404 for real
routes (the §7 gotcha, hit again).

## 9zv. The lesson as steps (2026-10-04)

**Changed.**
- `web/components/lesson-stepper.tsx` (new, knows nothing about physics) and the rewritten
  `web/app/(app)/lesson/page.tsx`: an authored lesson is now a run of steps: The story, The idea,
  Try an example, Where it breaks, Remember this, Check yourself. A segmented progress bar under
  the site bar (every segment is a button: nothing is locked, you can jump anywhere; finished
  steps turn green), Back / Next at the bottom that names the next step, ← / → keys (ignored while
  typing in the "I'm stuck" box), a slide-in per step, the step scrolled into view, and "Show
  everything on one page" for people who'd rather scroll.
- The worked example waits behind a "Show the worked example" button ("have a go first"); the
  takeaway is highlighted amber; the caveat is marked. The last step holds the check question,
  the 👍/👎 and the way to /assessment. A lesson with no sections (old format) keeps the single
  page. The personal story, the report button, reading time and rating are unchanged.
- `globals.css`: slide-in keyframes, same reduced-motion guard as the roadmap.

**Why.** One idea per screen is the interactive, game-like feel the user asked for, and it makes
a long lesson less daunting on a phone. Nothing in the API changed.

**Verified** in the browser on the demo class (`aarav.k`, Linear momentum, phone-width pane):
steps via click and keyboard, progress turning green, the worked-example reveal (16 equations
rendered), a jump to the last step (skipped steps stay grey), one-page mode. **Not checked:** a
lesson with a ready personal story in this step layout, screen readers, light theme, a real
phone. `tsc`, lint and `npm run build` are clean.

**Learned.** The browser tool's screenshot can lag one action behind: read the DOM state
(`aria-current`, text) before concluding a click did nothing.

## 9zw. The check page, interactive (2026-10-04)

**Changed.**
- `web/app/(app)/assessment/page.tsx` (rewritten) + `web/components/check-feedback.tsx` (new).
  Question screen: big option cards that lift on hover and select, A-D (or 1-4) keys to pick,
  "How sure are you?" slides in once an option is picked, a sticky bar says what's still
  needed ("Pick an answer", "Now say how sure you are", "Ready. Press Enter") and holds the one
  button; Enter submits.
- Result screen (multiple choice): right = confetti (12 CSS pieces), a popping tick (a gold trophy
  for mastered), "Right!"; wrong = a lightbulb and "Not quite, and that's useful", never a red
  failure. Both replay the question with the student's pick (red, cross) and the right answer
  (green, tick), each labelled in words too, then "Why" (the server's feedback), and for a right
  answer the **road to mastered** (Right once → New question tomorrow → Mastered), so the
  two-question rule explains itself. Wrong answers get Try again + Re-read the lesson.
- Older free-text lessons keep the plain form and result.
- `globals.css`: confetti keyframes; the pieces are `display:none` unless motion is welcome.
- No API change: same `submitAssessment` result fields.

**Why.** The check is the moment that decides whether a student feels clever or stupid; the
user wanted it interactive. The wrong-answer screen is deliberately about "what to fix", in line
with the mix-up design.

**Verified** in the browser on the demo class (Linear momentum): keyboard pick and Enter, wrong
then right, the red/green replay, the track, 12 confetti pieces in the DOM, 375 px (no sideways
scroll). The demo DB was reseeded afterwards (the test wrote answers into it). **Not checked:** the
"mastered" gold screen (needs a second right answer a day later), screen readers, light theme,
reduced motion on a real setting, the free-text legacy path.

**Learned.** A keyboard shortcut handler must not treat a radio as a text field: after clicking an
option, focus is on its radio, so Enter did nothing until radios were excluded from "typing".

## 9zx. The starting check, interactive (2026-10-04)

**Changed.**
- `web/app/(app)/start/page.tsx` (rewritten). Intro: three "what to expect" tiles (about 5 minutes,
  no marks, your own roadmap). Hobbies: a grid of tiles (emoji, label, a tick that pops), "N of 8
  picked", the own-hobby box kept; the button says "Skip this" when none are picked. Questions:
  a segmented progress bar (green answered, indigo here), a short cheer ("No marks. Honest answers
  help most.", "Halfway there.", "Last one!"), a slide between questions, a sticky Back / Next bar
  with a hint, and keys: **A-D / 1-4** pick, **U / 0** "not sure", **S / T / G** how sure, **Enter**
  next (finish on the last). Plan reveal: confetti, and the three tiles count up
  (`web/components/count-up.tsx`, new; shows the number outright under reduced motion).
- Notes that can contain maths ("squared terms can't balance a product like $as$") were printed as
  raw LaTeX in the plan, `/mix-ups` and the roadmap sheet; they now go through `<Markdown>`
  (KaTeX). A pre-existing bug, found while testing.
- No API change; the check is still taken once, answers sent at the end.

**Why.** First impressions: the starting check is the first thing a student does after signup.

**Verified** in the browser on the demo class (a not-yet-started student, then a second one at
375 px): hobby tiles, the whole 8-question run by keyboard (including U and the S/T/G keys), the
"Last one!" button and Enter to submit, the plan reveal (1 known, 5 mix-ups, 2 not sure = 8 answers),
confetti pieces present, KaTeX rendering, the "already taken" guard, no sideways scroll. The demo DB
was reseeded afterwards. **Not checked:** screen readers, light theme, the confetti and count-up
under a real reduced-motion setting, the signup-to-start hand-off with a brand-new account.

**Learned.**
- JSX in this build drops the space in `{n} quick questions` (an expression followed by text on the
  same line): write `{n}{" "}quick`. The old code already did, and my rewrite re-introduced "8quick".
- Several clicks fired in one JS tick all read the same stale `value`; real users can't, but a
  scripted test must pause between clicks.


## 9zy. Replit design adopted as the house style: `ecolearn-style` skill (2026-10-08)

**Changed.**
- New project skill `.claude/skills/ecolearn-style/`: `SKILL.md` (tokens, component recipes, motion,
  screen blueprints, porting rules, checklist) plus `reference/` (unmodified copies of the Replit
  app's `index.css`, `screen-styles.css`, `ui-kit`, `experience`, student/study/teacher screens,
  favicon).
- `.gitignore`: `.claude/` became `.claude/*` + `!.claude/skills/`, so the skill is shared with the
  teammate; launch.json and local permissions stay ignored.

**Why.** The user designed the UI in Replit (`EcoLearn-Physics-Tutor.zip`, mock data only) and wants
the whole product to follow that style. A skill makes every later session reuse the same tokens and
classes instead of re-deriving the look.

**Learned.** The Replit app is plain global CSS classes (warm green "field notes", dark default,
per-interest `data-interest` accent), not Tailwind utilities; the current `web/` is indigo shadcn, so
adopting it is a restyle screen by screen, not a patch. The zip itself is untracked; do not commit it.


## 9zz. The whole web UI restyled to the Replit house style (2026-10-08)

**Changed.** UI only, in `web/` (nothing under `src/`, `api/`, `tests/`, `data/`, `scripts/`; `lib/api.ts` untouched).
- Tokens: `app/globals.css` maps shadcn variables onto the warm green palette, adds per-interest accents
  (`html[data-interest]`, lighter in dark mode) and imports the new class-based `app/ecolearn.css`
  (`@import ... layer(components)` so utilities still win). System fonts replace Inter.
- Primitives restyled in place: `ui/button` (pressable), `card`, `badge`, `input`, `progress`, `dialog`.
- New `components/ui-kit.tsx`; rewritten `site-nav.tsx` (top bar + mobile bottom nav), landing `app/page.tsx`,
  `auth-card.tsx` (two-column auth), `interest-level-fields.tsx`, roadmap page (welcome strip, chapter map, side
  cards), `roadmap-path.tsx`/`learning-plan.tsx`/`chapter-picker.tsx` colours and cards, lesson page + stepper +
  personal-story, assessment/start/review/mix-ups/settings/teacher pages via a class codemod plus hand edits.
- `auth-provider.tsx` sets `data-interest` on `<html>` (presentation only). Deleted unused `section-heading.tsx`.
- `.gitignore` tracks `.claude/skills/` (skill `ecolearn-style`, see 9zy).

**Why.** The user wants the whole product to look like their Replit design.

**Verified.** `tsc --noEmit`, `npm run lint`, `npm run build` clean. In the browser on the demo DB: landing, signup,
login, roadmap (desktop + 375 px), lesson (375 px), assessment question + wrong-answer result (light theme), mix-ups,
review, settings, start (already-taken), teacher home and class dashboard. **Not checked:** end-check page, the
teacher account page, error/404 pages, print slips, every dark/light pair, a screen reader.

**Learned.**
- An unlayered global stylesheet beats Tailwind's layered utilities; import house CSS into a lower layer.
- A grid with no `grid-template-columns` sizes its implicit column to content: the roadmap aside overflowed until
  it got `minmax(0,1fr)`.
- `.dark`-less hard-coded light colours in ported CSS (e.g. `.continue-card .tag`) need dark twins.


## 9zzz. Login lands on the starting check; the roadmap is a tree (2026-10-09)

**Changed.** UI only (`web/`).
- `lib/landing.ts` + `app/login/page.tsx`: after a student logs in, the page is the starting check (`/start`, hobbies
  first) until it is taken, then an open end check (`/end-check`), otherwise the `?next=` page or the roadmap. The
  "already logged in" redirect no longer races the submit.
- New `components/roadmap-tree.tsx`; `roadmap/page.tsx` uses it instead of the chapter dropdown and the winding map:
  chapters (solid rail, grouped by unit) > concepts (dashed orange branch) > lesson parts (dotted purple twig, each
  opens `/lesson?...&step=N`). `lesson-stepper.tsx` takes `initialStep`. Removed `chapter-picker.tsx`, `PathMap`,
  `StepSheet`.

**Why.** User report (2026-10-08): login skipped the hobby step and landed on the assessment/roadmap; the dropdown of
chapters felt wrong. Asked for chapters first, expanding into sub sections and sub-sub sections in different styles.

**Not reproduced: reset password.** After a teacher's reset the new password was said not to work (only the demo one).
`reset_student_password` + `authenticate_student` verified end to end on a temp DB (new works, old rejected). Likely
causes: two API servers/databases at once (reset hit one, login the other), or the browser's saved-password autofill
filling the old one. Open.

**Learned.** A stale `.next` left by `npm run build` makes the next `next dev` 404 real routes: delete `.next`.


## 9zzzz. "Skip for now" is remembered; accent paints before auth loads (2026-10-09)

**Changed.** UI only. `lib/landing.ts`: a student who pressed "Skip for now" on `/start` is not sent back to it at every
login (remembered per student in localStorage; the roadmap card still invites them). `auth-provider.tsx` +
`theme-toggle.tsx` boot script remember the interest so the accent colour is right on the first paint.
**Checked in the browser:** skip-then-login lands on the roadmap, a fresh student still lands on `/start`; end-check
("needs start" state), 404, teacher account. **Not checked:** the credentials sheet and printed slips (it only appears
after a password reset, and the demo class holds real accounts), the error page (needs a crash), end-check questions.


## 9zzzzz. Teacher class dashboard redesign (2026-10-09)

**Changed.** UI only. `teacher/(dashboard)/class/page.tsx` is now four tabs (Overview, Insights, Stories & AI,
Students) instead of one 10,000 px scroll. Metric cards with icons and tones (`.dash-metric`), a before/after bar chart
per idea in `class-checks.tsx` (the table moved into a collapsed "Idea by idea"), ranked misconceptions with share bars,
per-interest cards, the AI guardrail pipeline as four stage cards, the teaching plan on a soft panel with a step
timeline, and a student table with avatars, a mastered meter, coloured accuracy and card layout under 768 px
(`.dtable`). New `.dash-*` / `.dbar*` / `.dmix*` / `.dpipe` / `.dtable` rules at the end of `app/ecolearn.css`
(11 px minimum text, unlike the Replit original's 8-10 px).

**Checked** in the browser on the demo class (desktop and 375 px): all four tabs. **Not checked:** the credentials sheet
after a reset, an open end-check being toggled, the empty state of a brand-new class.
