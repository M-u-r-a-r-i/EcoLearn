# EcoLearn — Session Handoff (context restore)

**Purpose:** paste this into a new session to restore full context. It captures
everything built through Phase 7, the current git state, the one pending action,
and all the decisions/gotchas that aren't obvious from the code.

Auto-memory (loaded automatically each session from
`C:\Users\murar\.claude\projects\D--Projects-EcoLearn\memory\`) already gives:
Gemini/Gemma + `google-genai` stack, "push after each sprint" reminder,
"update LOG.md after every directory-touching request" rule. This doc covers the rest.

---

## 0. ⚠️ IMMEDIATE PENDING ACTION — branch consolidation (not finished)

The user wants **everything in a single branch: `master`**. This is mid-flight.

**Git state right now:**
- On `master` @ `53733fc` ("." commit — it only added `HANDOFF.md` + a small LOG entry). `master` == `origin/master`.
- `curriculum` @ `eeb72ce` — has ALL the real work (Phases 1–7), committed. `origin/curriculum` is at `5c09fba`; local is 1 ahead (`eeb72ce`, the LOG commit).
- The two branches **diverged** at `e852392`: `curriculum` has all the work; `master` has only the `.`/HANDOFF commit. Neither contains the other.

**The plan the user approved:**
1. Merge `curriculum` → `master` (`git merge --no-ff curriculum`).
2. It **conflicts on `LOG.md`** (both sides edited it). Resolve as a **union**: keep curriculum's full LOG (~336 lines, all session entries) via `git checkout --theirs -- LOG.md`, optionally re-add master's small "2026-06-12: Branch cleanup" entry. No other files conflict (master's only extra file, HANDOFF.md, isn't on curriculum, so it just stays / will be overwritten by this doc).
3. `git add LOG.md` then commit the merge.
4. Delete `curriculum` **locally only** (`git branch -d curriculum`).
5. **Do NOT push** — the user pushes themselves (they'll push `master` and delete `origin/curriculum`).

**Caution:** a previous merge attempt got aborted externally mid-conflict (briefly left a gutted LOG.md). Nothing was lost — curriculum's LOG is safe in history. When redoing, resolve LOG.md deliberately (`--theirs` + `git add`), and verify the merged `LOG.md` has all Phase 2–7 entries before committing.

---

## 1. What EcoLearn is

A personalized AI tutor for CBSE/ISC **Class 11 Physics**. The student picks an
interest (**football** or **gaming**); the system teaches concepts by grounding
analogies in that interest. Started as a chatbot, now a **data-driven learning
platform**: curriculum spine → path engine → service API → multi-page UI, with
lessons pre-generated offline and served instantly.

---

## 2. Architecture

```
Multi-page Streamlit UI (app.py + pages/)  ── calls ONLY ──▶  src/platform_api.py
                                                                     │
   platform_api orchestrates:
     • path engine    (src/path/engine.py)    what to learn next
     • progress store (src/progress/store.py) SQLite mastery + students
     • lesson service (src/content/lesson_service.py) read cached lessons
     • live pipeline  (src/pipeline.py) generate→critic→retry→polish
     • curriculum     (src/curriculum/)  YAML→typed objects
```

**Two paths:** cached lessons (offline-generated, instant, no LLM) for the stable
curriculum; the live pipeline only for `ask_help` (assessor grades on submit).

---

## 3. The service boundary — `src/platform_api.py` (ONLY thing the UI imports)

Every return value is **plain JSON-serializable data** (dicts/lists) — this is what
makes a Next.js swap a pure presentation change. Functions:

1. `create_or_load_student(name, interest, level) -> profile dict` — idempotent; `student_id` = slug of name.
2. `list_chapters() -> [{id, name}, ...]` — for the chapter picker.
3. `get_roadmap(student_id, chapter_id) -> [ {concept_id,name,order,status,progress_status,best_score,attempts,missing_prerequisites}, ... ]` — status ∈ mastered/available/locked.
4. `get_next_lesson(student_id, chapter_id, concept_id=None) -> {status,reason,concept_id,concept_name,lesson}` — status ∈ new/review/done/blocked/lesson_missing. `concept_id` override re-serves a specific concept (for "practise again").
5. `submit_assessment(student_id, concept_id, answer) -> {score,mastery_signal,feedback,missing_concepts,graded_question,mastery}` — grades the answer against the lesson's `check_question`; RAISES on grader failure (does NOT write a fake score-0).
6. `ask_help(student_id, concept_id, question) -> {concept_id,concept_name,answer,verdict,attempts}` — live pipeline, grounded in the concept (query framed as "{concept} — student asks: {question}"), polished. The only expensive/live call.

---

## 4. "cleared" vs "mastered" (the 2/3 choice)

- **mastered** = 3/3 → gold badge, drives spaced-repetition review.
- **cleared** = score ≥ 2 (partial or mastered) → the **progression bar**: engine
  advances past cleared concepts and unlocks dependents when prereqs are cleared.
- A 2/3 lets the student **choose**: "Move on to next lesson" (engine advances) or
  "Practise this again" (sets `st.session_state["practise_concept"]` → pages pass it
  as `concept_id` to `get_next_lesson`).
- Store: `get_mastered_concepts` (status==mastered), `get_cleared_concepts` (best_score≥2).
- Assessment page uses RESULT vs QUESTION **mode split** (pinned `active_grade` in
  session) so passing always navigates to the next **LESSON**, not the next assessment.
  Don't re-derive the result from `get_next_lesson`.

---

## 5. Models + quota reality (THE binding constraint)

`.env` only sets `GEMINI_MODEL=gemma-4-31b-it`; everything else uses code defaults.

| Role | Model | Notes |
|---|---|---|
| Generator | `gemma-4-31b-it` (`GEMINI_MODEL`) | temp 0.7 |
| Critic | `gemini-2.5-flash-lite` (`CRITIC_MODEL`) | JSON; fails open (soft-PASS w/ `error`) |
| Polisher | `gemini-2.5-flash-lite` (`POLISHER_MODEL`) | clean markdown; **fallback chain** |
| Assessor | `gemma-4-31b-it` | **fallback chain** |
| Embeddings | `all-MiniLM-L6-v2` (ONNX local) | no API/quota |
| Router | `gemma-4-31b-it` | legacy chat only |

**Fallback chains added this session ("portfolio of models"):**
- `assessor.py`: `_FALLBACK_MODELS = (gemini-2.5-flash-lite, gemini-flash-latest)` (gemma threw 500s).
- `polisher.py`: `_FALLBACK_MODELS = (gemini-2.5-flash, gemini-flash-latest, gemma-4-31b-it)`; ALSO broadened thinking-disable to `gemini-flash*` (flash-latest alias is a thinking model that wasted its budget → ~287-char garbage that won't parse).

**Quota facts:** each model has its own ~20/day free-tier bucket; flash-lite is
exhausted fast by factory runs (critic+polish per lesson). `gemma-3-27b-it` → 404 on
this key (only `gemma-4-31b-it` works). `gemma-4-31b-it` has intermittent `500 INTERNAL`.
Fallback chains / model swaps keep the app alive.

---

## 6. Content: lessons + curriculum

- **Curriculum:** `data/curriculum/physics.yaml` — Physics → Kinematics → 2 chapters:
  `motion_straight_line` (9 concepts, order 1–9), `motion_plane` (8 concepts, order
  10–17, cross-chapter prereqs into ch1). **`order` is GLOBAL** (teaching_order sorts the
  whole subject) — new chapters must continue numbering, or `validate_ordering` rejects
  cross-chapter prereqs.
- **Lessons:** `data/lessons/{concept_id}__{interest}.json` — **34 total, all polished**
  (18 ch1 + 16 ch2 × football/gaming). Schema (`src/content/lesson_schema.py`):
  `concept_id, interest, body, worked_example, check_question, metadata{...}`.
  body=Scenario+Mapping, worked_example=Formal Restatement, check_question=self-check
  (section headers stripped on parse; lesson page re-adds them).
- **Factory:** `src/content/generate_lessons.py` — `generate_all_lessons(chapter_id,
  interests, skip_existing=True)` (idempotent/resumable), `repolish_existing()`
  (idempotent; fail-open preserves raw). CLI: `python -m src.content.generate_lessons
  [repolish]`. A lesson is "raw" if worked_example/check_question empty (polish failed
  open) → needs repolish. `flagged.jsonl` rebuilt from disk each run.

---

## 7. Progress store — `src/progress/store.py` (SQLite)

- DB: `data/progress.db` (gitignored). Override via env `ECOLEARN_PROGRESS_DB` (read
  lazily → tests use a temp file).
- Tables: `progress(student_id,concept_id,status,best_score,attempts,last_seen)`,
  `students(student_id,name,interest,level,created_at)`.
- `status_from_score`: ≥3 mastered, ≥2 partial, else not_yet (mirrors app.py).
- Functions: get_progress, update_progress (attempts+1, best=max), mark_reviewed,
  get_mastered_concepts, get_cleared_concepts, get_student, save_student.
- Persistence verified across separate processes.

---

## 8. File map (load-bearing)

```
src/platform_api.py             THE boundary (6 functions)
src/curriculum/schema.py        Pydantic Subject→Unit→Chapter→Concept (BloomLevel)
src/curriculum/loader.py        load_subject, teaching_order (GLOBAL), resolve_prerequisites, validate_ordering
src/path/engine.py              next_concept, get_roadmap, list_chapters, find_concept; cleared vs mastered
src/progress/store.py           SQLite progress + students
src/content/lesson_schema.py    Lesson model
src/content/generate_lessons.py offline factory + repolish
src/content/lesson_service.py   get_lesson(concept_id, interest)
src/agents/analogy_generator.py generator (prompts/analogy_generator.txt) — NO fallback yet
src/agents/critic.py            critic, fails open (prompts/critic.txt)
src/agents/assessor.py          generate_question + grade_answer + fallback chain (prompts/assessor.txt)
src/agents/polisher.py          polish_explanation + fallback chain (shared by app + factory)
src/pipeline.py                 explain_with_review: RAG→gen→critic→retry
src/rag/retrieve.py             retrieve_concept / retrieve_interest (Chroma, local)
app.py                          Onboarding landing (multi-page entry)
pages/1_Roadmap.py              roadmap (mastered green / available blue / locked grey)
pages/2_Lesson.py               lesson + persistent "ask for help" box
pages/3_Assessment.py           check question → grade → 2/3 choice (RESULT/QUESTION modes)
ui_common.py                    presentation only: setup_page, require_student, chapter_selector, badges/cards
legacy_chat_app.py              OLD single-page chatbot, preserved
.claude/launch.json             preview server (streamlit, port 8502)
data/curriculum/physics.yaml    curriculum source of truth (2 chapters)
data/lessons/*.json             34 pre-generated lessons
LOG.md                          dated Changed/Why/Learned
.env                            GEMINI_API_KEY, GEMINI_MODEL=gemma-4-31b-it, GEMINI_MAX_OUTPUT_TOKENS=2048
chroma_db/                      local vector store (gitignored; rebuild: python src/rag/build_index.py)
```

---

## 9. Decisions / patterns (don't re-debate)

- **UI imports ONLY `platform_api`** for data; `ui_common` imports nothing from internals. Plain-dict returns → frontend-swappable.
- **Engine invents no pedagogy** — ordering+prereqs from curriculum, mastery from store; it just combines them. The `reason` string is emitted by the deciding code path, so it can't lie.
- **Fail open on judges** (critic/polisher); **fail loud on missing inputs** (no API key, unknown student).
- **Polish, then parse** — the LLM polisher is the only reliable scratchpad-stripper; regex alone loses.
- **Pre-generate offline, serve cached** — pay multi-agent cost + critic vetting once; quota exhaustion delays authoring, not the product.
- **Factory is parameterized by chapter_id** — adding a chapter is content + a factory run, no code change.
- **No long work in a Streamlit click handler; pin results** so navigation stays correct.

---

## 10. How to run / verify

```
# venv python: D:\Projects\EcoLearn\venv\Scripts\python.exe
# Deterministic tests (NO LLM):
venv\Scripts\python.exe tests\test_curriculum.py
venv\Scripts\python.exe tests\test_path_engine.py
venv\Scripts\python.exe tests\test_persistence.py seed   # then: ... verify
venv\Scripts\python.exe tests\test_edge_states.py
venv\Scripts\python.exe tests\test_scale_chapter2.py
# LLM test (slow, quota): tests\test_platform_api.py
# Run app:
venv\Scripts\streamlit.exe run app.py --server.headless true --server.port 8502
# Rebuild RAG index: venv\Scripts\python.exe src\rag\build_index.py
# Regen/repolish lessons: venv\Scripts\python.exe -m src.content.generate_lessons [repolish]
```

Phases 1–7 DONE and tested. Streamlit/preview gotchas: forms need the native
value-setter + dispatched `input` event to register; baseweb dropdowns won't switch via
automation (click manually); a hard browser reload resets `st.session_state`.

---

## 11. Open work after consolidation

1. **Finish the branch merge** (§0) — the active task.
2. **Subject-level scaling** — engine/platform_api assume one subject (physics.yaml path
   is a constant); a `chemistry.yaml` needs a subject param/selector (same shape as the
   chapter selector). Schema is already subject-agnostic.
3. **Generator fallback** — analogy generator has no model fallback yet (only assessor +
   polisher do); add one for unattended factory runs when gemma 500s.
4. Optional: chapter-relative `order`; re-vet flagged lessons when flash-lite resets.

---

## 12. User preferences

- Beginner-friendly explanations; explain the *why* behind tricky patterns.
- **Don't auto-commit / don't push — the user pushes themselves.** End replies with a 📌 push reminder.
- Update LOG.md after every directory-touching request (Changed/Why/Learned).
- Gemini/Gemma via `google-genai` only unless told otherwise.
- Honest, specific critique > polite vibes.
- Token-conscious: don't over-poll background tasks (you're notified on completion); don't re-verify what's already proven.
