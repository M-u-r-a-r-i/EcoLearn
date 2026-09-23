# EcoLearn — Agent Briefing

> **You are picking up an in-flight project. Read this file fully before writing any code.**
> It is short on purpose; it tells you what this is, where we stopped, what to do next, and the
> rules that will break the project if you ignore them. Depth lives in two files:
>
> | File | What it holds | When to read it |
> |---|---|---|
> | **[`PROJECT_HISTORY.md`](PROJECT_HISTORY.md)** | What exists today, architecture as built, all 44 commits explained, every design decision + why, hard-won lessons, gotchas | **Read now, in full**, before your first change |
> | **[`ROADMAP.md`](ROADMAP.md)** | The v2 plan: target architecture, data model, Milestones 0–9 in order with per-milestone files + acceptance criteria | **Read now**, then re-read the milestone you're on |
> | [`README.md`](README.md) | Evaluator/user-facing overview | Only if editing user-facing docs |
>
> Those three plus the code are the complete picture. There is no external context you are missing.

---

## 1. What this is, in one paragraph

**EcoLearn is a personalised AI tutor for CBSE/ISC Class 11 Physics (Kinematics).** A student
picks an interest — today football or gaming — and every concept is taught through analogies
grounded in that interest, with the physics kept correct by an automated critic. It is full-stack:
**FastAPI + Next.js** (primary) with **Streamlit** kept as a legacy UI over the same backend.
The curriculum spans the full Class 11 + 12 syllabus for CBSE and ISC (29 chapters, 249 concepts).
Lessons are being written for an agreed subset — **14 chapters × 5 interests**, "explain" format
first — batch by batch (§2, `data/content_scope.yaml`).

The one architectural fact everything depends on:

> **All logic lives behind `src/platform_api.py`, which returns plain JSON-serializable dicts.
> Every frontend calls only that boundary.**

*(The project is a physics tutor despite the "EcoLearn" name — a holdover. Don't rename it.)*

---

## 2. Where we are right now

### Your first session — do these in order, before writing any code

1. **Read `PROJECT_HISTORY.md` and `ROADMAP.md` in full.** This file is the summary; those two
   are the substance.
2. **Check the handoff state:** `git status` and `git log --oneline -5`. **If there are
   uncommitted changes you didn't make, they are the handoff — never `reset`, `checkout .`,
   `stash drop` or `clean` them.** Work is normally committed and pushed at the end of each chunk
   (§5), but the latest work may still exist only in the working tree.
3. **Run the deterministic suite (§6).** All of it should pass. If anything fails, stop and tell
   the user before building on top — something changed since the handoff.
4. **Tell the user, in a few sentences, what you understood** — where the project is, the next
   action, and anything that looked inconsistent. Let them correct you before you start.
5. Then begin the next action below.

### The goal — a 10-day sprint (set by the user, 2026-09-21)

**Hackathon finals (HackAStone, Amsterdam): 2026-10-29. The build must be finished by
2026-09-30** so it can be pilot-tested on real school students in October. The sprint plan of
record is **`ROADMAP.md` §0** — it supersedes the milestone order below wherever they conflict.

User decisions (2026-09-21) — don't re-litigate them:

- **Accounts: username + password, no email** (the pilot is on minors — minimal PII). The
  auth backend was switched from email to username on 2026-09-21. No email means password
  resets go through a teacher/admin tool.
- **Content scope (decided 2026-09-22, replaces "all 7,470 lessons"):** the full matrix doesn't fit
  the user's **Claude Pro** plan before the finals. The agreed subset lives in
  **`data/content_scope.yaml`**: **14 chapters** (7 Class 11 + 7 Class 12, the "most important" set)
  × **5 interests** (cricket, football, gaming, smartphones, motorsport). **Phase 1: the `explain`
  format only** — 70 batches, 680 lessons, target **2026-09-28**. **Phase 2: `challenge` +
  `misconception`** for the same set, target **2026-10-06**. The other 15 chapters and 5 interests
  come after the finals. Students are on **CBSE and ISC** — every concept carries `boards`.
- **Nothing is ever locked.** Prerequisites are "brush up first" hints, never gates.
- **Every lesson opens with a story and has images** — scene illustration per chapter × interest,
  graphs/diagrams per concept, famous images (public domain / CC only). **Never download an image
  without the user's approval**; every famous image needs a manifest entry. See
  `content/AUTHORING_GUIDE.md` §4a and §7a.
- **Lessons are written by Claude Code sessions (Opus 5) straight to files — no LLM API, no GPU,
  and no LLM critic** for static content. Quality comes from a shared authoring guide + approved
  gold examples, a deterministic validator (format only), a random 2% review sample, and full
  human reading of the pilot chapters.
- **Check questions are multiple-choice** with each wrong option mapped to a misconception, so
  grading needs **no live LLM call**.
- **The doubt chatbot is the only live LLM feature: Gemini only.** The RTX 3090 backend is a
  later feature — leave a placeholder, don't build it.
- **Run locally first**; cloud hosting comes after the sprint.

### Current state

**Repo:** github.com/Niranjan-207/EcoLearn, branch **`main`** (a fresh history: the user
re-initialised it with one "Initial Commit" on 2026-09-21; the older 44-commit history described
in `PROJECT_HISTORY.md` §8 lives in the teammate's repo). Everything below is committed and
pushed; the working tree is normally clean.

**The app works end to end, and has been clicked through in a browser** (2026-09-23): sign up →
roadmap → pick a chapter → open any concept → read the lesson → answer the multiple-choice check →
the roadmap shows it mastered → refresh keeps you logged in → settings → log out.

**Backend / boundary**
- Accounts are **username + password** (no email): `register_student`, `authenticate_student`,
  `get_student_profile`, `update_student_profile`, `change_password` in `src/platform_api.py`,
  over `src/auth/passwords.py` (bcrypt) and the `students` table in `src/progress/store.py`.
- **The breaking flip is done** (`PROJECT_HISTORY.md` §9n): `/api/roadmap`, `/api/next-lesson`,
  `/api/assessment` and `/api/help` take the student from the session cookie
  (`Depends(get_current_student_id)`); `student_id` is gone from their contracts and
  `POST /api/student` is deleted. Streamlit is unaffected — it calls the boundary directly.
- **Grading is multiple choice with no LLM** (§9q): `submit_assessment` takes the option letter
  and checks it against the answer key in the lesson file. Correct → 3, wrong → 0; feedback is the
  lesson's own explanation plus that option's misconception. The key never reaches the browser.
  Legacy JSON lessons still use the Assessor. `tests/test_mcq_grading.py` (24 checks) pins this.
- `get_next_lesson` also returns `lesson.sections` and `lesson.check` (options, no answer).
- `list_interests()` offers the **five in-scope interests** with `chapters_ready` /
  `chapters_total` (§9r), read from `data/content_scope.yaml` via `src/curriculum/scope.py`.

**Content**
- `data/curriculum/physics.yaml`: 29 chapters / 249 concepts, CBSE 2025-26 + ISC, global sparse
  ordering, `grade` + `domain` + `boards`. Never rename an id.
- **372 authored lessons, all valid** (`scripts/validate_lessons.py`). Phase 1 (`explain`) is at
  **34/70 batches**. Coverage by interest: **cricket 14/14 chapters, football 10, gaming 7,
  smartphones 2, motorsport 1**. Every chapter in scope has its interest-neutral figures, so all
  remaining batches reuse figures and only add a scene.
- `content/AUTHORING_GUIDE.md` is the contract for writing lessons. **§7 changed on 2026-09-23**
  (user feedback: worked examples were "hard to visualize") — few, round, picturable numbers, one
  quantity per step, a plain-sentence sanity check. §7a: shared figures must not print
  batch-specific numbers.
- Famous images live in `data/media/famous/` with a manifest entry each; 8 approved so far.
  **Never download one without asking the user.**

**Frontend (`web/`)**
- `lib/api.ts`: one `request()` wrapper (cookie credentials, `ApiError`, timeouts, 401 hook,
  friendly messages). No function takes a student id.
- `components/auth-provider.tsx` (loading | authenticated | unauthenticated, hydrated from
  `/api/auth/me`), `require-auth.tsx` + the `app/(app)/` route group.
- `/login`, two-step `/signup` (replaces the deleted `/onboarding`), `/settings`.
- Roadmap with a chapter picker over all 29 chapters (`?chapter=`); every concept card opens its
  lesson (`?concept=`).
- The lesson page renders section by section and **collapses the worked example and "Where the
  picture breaks" behind a click** (user feedback, §9q). The check page is a radio group.

**-> YOUR NEXT ACTION: run the next lesson batch** (procedure below). `scripts/batch_status.py`
always knows which one is next; `--all` shows `[done] / [part] / [todo]` for every batch. Between
usage windows, continue the frontend: format tabs (`challenge` / `misconception` once those
lessons exist), dark mode, toasts and error pages, and the teacher tools (reset a password, create
a class from a roster).

**Open with the user, don't decide alone:**
1. **Scope.** Finishing all five interests is ~36 more batches. Claude's recommendation was to
   finish cricket, football and gaming first and leave smartphones and motorsport until after the
   finals; the user has not ruled either way.
2. **Famous images requested but not yet approved:** Volta (electric_potential), Faraday
   (capacitance / dielectrics), Joule (kinetic_energy / power), de Broglie — de Broglie was
   **rejected** on licence grounds (unknown author, 1929, source only "believes" it is PD).
### How to run a lesson batch (the standard procedure)

1. **Check the plan limits** with the `get_usage` tool (ccd session management). One batch costs
   about **2% of the weekly limit and up to ~17% of a 5-hour window**; an explain-only batch roughly
   half that. **Don't start a batch above ~85% of the 5-hour window.** Note the numbers.
2. **Find the next batch:** `venv\Scripts\python.exe scripts\batch_status.py` (progress + next
   batch). Order: phase → chapter (teaching order) → interest, so a chapter's first interest draws
   its figures and the rest reuse them.
3. **Brief the sub-session.** Don't paste the brief into your own context: tell a background
   **general-purpose sub-session** to run
   `venv\Scripts\python.exe scripts\batch_status.py --brief --batch <chapter>:<interest>:<phase>`
   and follow that output exactly. Add these standing instructions (learned the hard way):
   - **at most 2–3 sub-sessions at once, always on different chapters.** Five in parallel stalled
     outright (600 s watchdog) and burned ~50% of a 5-hour window with nothing written;
   - **write each lesson to disk as soon as it is finished**, and **re-check its numbers before
     starting the next one**, so an interruption can never leave an unverified answer key;
   - reuse the chapter's existing figures, never redraw them;
   - follow `AUTHORING_GUIDE.md` §7 (light, round, picturable worked-example numbers);
   - render PNGs into a scratchpad subfolder named after the batch (parallel sessions used to
     overwrite each other's files).
4. **Review when it reports** (keep your own turns few and short — the main session's long context
   is the expensive part):
   - `venv\Scripts\python.exe scripts\validate_lessons.py` → must be all valid;
   - look at every *new* image (headless Edge → PNG in the scratchpad → read it; tiling them into
     one grid with PIL makes it a single image read);
   - re-derive the answer key and numbers in 2–3 of the most numeric lessons;
   - confirm no existing file was modified (`git status` shows only `??` for new files).
4a. **If a batch was cut off mid-run** (usage limit, stall, crash), treat it as *unverified*, not
   merely unfinished. **Check the disk, not the exit status** — `batch_status.py --all` often shows
   `[done]` for a session that died before reporting. Then run an **audit sub-session** over that
   batch's lessons: recompute every worked-example and answer-key number with Python, check each
   distractor really is the mistake its misconception names, fix only what is wrong. This is how
   the one physics error found so far was caught (`PROJECT_HISTORY.md` §9t): a session reported
   "found an arithmetic slip, fixing it" and was killed before the fix landed. **The validator
   checks format, never arithmetic** — nothing else will catch this.
5. **Famous images:** if a sub-session asks for one, check its licence on Commons and **ask the user
   before downloading** (one list per chapter). Never download without approval.
6. **Commit + push** per batch (or per few batches): run the checks in §6, commit with a descriptive
   message, push to `origin main`, report the hash. Read `get_usage` again and note the cost.
7. **Interests are offered by coverage, not by a flag** (since §9r). `list_interests()` returns the
   five in-scope interests with `chapters_ready` / `chapters_total`, and the signup and settings
   pickers print "10 of 14 chapters ready". The registry's `active` / `draft` flag no longer gates
   what students see, so there is nothing to promote by hand — writing lessons is what moves the
   number.

The auth "breaking flip" is **done**; new work no longer has to be additive for its sake. Streamlit
still works because it calls `src/platform_api.py` directly rather than over HTTP — keep it that
way.

---

## 3. The phases, in the order they must be done

> **During the sprint to 2026-09-30, `ROADMAP.md` §0 overrides this table.** The sprint drops
> M1a/M1b (no GPU, no API generation), writes all lessons with Claude Code sessions, and defers
> M2–M5 and M8–M9. The table below is the longer-term plan after the pilot.

Do these in sequence — each unblocks the next. Full specs and acceptance criteria per milestone are
in [`ROADMAP.md`](ROADMAP.md).

| # | Milestone | Why this order |
|---|---|---|
| **0** | **Accounts, auth & UX foundation** ← *you are here* | Profiles must belong to a durable user before any per-student model is worth building |
| ⛔ | **Checkpoint: ask the user the "After M0" decisions** | They shape M1's schema, the interest list, and the GPU setup |
| 1 | **Full content spine: 28 chapters + fine-grained skills + an interest registry** | **Gates the whole data model** — both axes of the content matrix. Skills and chapters edit the same files, so each concept is authored once. 🔴 Starts with a silent duplicate-id bug fix. No LLM used |
| 1a | **LLM provider layer + self-hosted GPU backend** *(parallel with M1)* | Every agent calls models through one layer; a GPU backend; a parity benchmark vs today's output. Must finish before the pilot, so the pilot validates the model that will actually generate |
| 1b | **Class 12 pilot — a go/no-go gate** | Current Electricity × football, gaming + 1–2 new interests, **on the self-hosted model**, human-read. Proves the thesis survives abstract physics, new interests and the new model *before* M2–M6. Measures GPU throughput. **The user makes the call** |
| C | **Track C — content corpora** *(parallel, from M1 onward)* | RAG text for every chapter and interest × physics domain. The long pole — authoring, not code — and independent of M2–M6 |
| 2 | Learner-model data layer (2 tables → ~9) | The profiler needs somewhere to write |
| 3 | Diagnostic assessment (tagged questions, distractor → misconception) | Turns answers into signal; nothing to trace without it |
| 4 | Profiler v1 (EMA + time-decay per skill) | Consumes M3's signal, emits the learner-state dict |
| 5 | Adaptive sequencer | Consumes M4's learner state |
| 6 | Multi-format lesson engine | Needs the profiler to decide *which* format |
| 7 | **Mass lesson generation** (~25,000 lessons) | **Must wait for M6** — generating before the formats exist means regenerating most lessons. GPU-bound: runs on the self-hosted model from M1a |
| 8 | Engagement + metrics | Polish, once the core adapts |
| 9 | Stretch / R&D | Visual diagrams, outcomes study |

**The v2 thesis in one line:** *dynamic means **reorder**, not regenerate.* Content stays
pre-generated and cached; only the path through it adapts. That is what makes v2 affordable.

**The scale-up principle in one line:** *do format-independent work early (structure, the LLM
layer, corpora), de-risk the thesis cheaply (pilot), and generate in bulk only once (after M6).*

The code audit behind the scale-up plan is **done** — every "*Verified*" note in `ROADMAP.md`
§6, §6a, §6b, §6c and §12 was checked against the source on 2026-09-21, naming the exact function.
Re-check line numbers before you edit (code moves), but don't re-run the audit.

---

## 4. Non-negotiables — violating these breaks the project

1. **UIs talk ONLY to `src/platform_api.py`.** Never import engine/store/pipeline/agents from a
   UI. The web app goes `web/lib/api.ts` → FastAPI → boundary.
2. **The boundary returns plain JSON-serializable dicts/lists.** No Pydantic objects cross it.
3. **Cached vs live:** the **only** live LLM calls are the doubt chat (`ask_help`) and grading
   (`submit_assessment`) — and in the sprint, grading becomes multiple-choice with **no** LLM call.
   Static lessons are written by Claude Code sessions, never generated through an API. Everything else is served from pre-generated cache. **This is the entire
   cost, latency and capacity strategy — do not add a live call.** A self-hosted GPU doesn't change
   that: a live lesson would take minutes, and every student would compete for one GPU.
4. **New chapter/subject = content (YAML + a factory run), not engine code.** Concept `order` is
   **global across the subject**; a new chapter must continue the numbering (18, 19, …) or
   prerequisite validation rejects it.
5. **Migrations are additive.** Extend the store inside `_connect()` with `CREATE TABLE IF NOT
   EXISTS` + `PRAGMA table_info` / `ALTER TABLE ADD COLUMN`, and a separate `CREATE UNIQUE INDEX`
   for uniqueness (SQLite rejects `ADD COLUMN … UNIQUE`). Legacy rows and Streamlit must keep working.
6. **Tests are standalone scripts, NOT pytest.** Each sets its own `sys.path` and points
   `ECOLEARN_PROGRESS_DB` at a temp file **before** importing the module under test, then
   prints-and-asserts. Add new tests the same way.
7. **Don't break the pinned contracts.** `_slugify` and `create_or_load_student` must stay as they
   are — `tests/test_platform_api.py` pins `student_id == "journey-student"` and Streamlit depends
   on the name-based path. New accounts use `"stu_" + uuid4().hex` instead (a `_` is impossible in
   a slug, so the two id spaces provably can't collide).
8. **Models and providers.** *Today:* Gemma `gemma-4-31b-it` (generator/assessor), Gemini 2.5
   Flash-Lite (critic/polisher), local `all-MiniLM-L6-v2` embeddings, all via the `google-genai`
   SDK (**not** the deprecated `google-generativeai`). *The plan (user decision):* bulk generation
   moves to a **self-hosted LLM on a GPU** in M1a, with the Gemini API as fallback. **Until M1a,
   don't touch provider code. After M1a, agents call models only through `src/llm/`** — never a
   model SDK directly. Don't add a third provider without asking. Judges fail open; key roles keep
   fallback chains.
9. **⚠️ Gemma accepts neither `system_instruction` nor `thinking_config`.** The agents prepend the
   system prompt to the user message on purpose. It looks like an oversight; it isn't. Re-adding
   those fields silently breaks generation. **This holds when Gemma is self-hosted too** — its chat
   template has no system role. M1a turns it into a per-model capability flag. And never assume one
   model can fill every role: Gemma managed only **2/11** clean polishes. See `PROJECT_HISTORY.md` §6.
10. **Never rename an existing unit, chapter or concept id** (`kinematics`,
    `motion_straight_line`, `motion_plane`, and the 17 concept ids). Lesson filenames
    (`{concept_id}__{interest}.json`), student progress rows and tests are all keyed on them — a
    rename silently orphans all three. New ids must be unique across the **whole subject**, not
    just the chapter.
11. **Commit and push only as §5 describes** — never force-push, never commit secrets.

---

## 5. How the user works (match this)

- **Commit and push to `origin` (github.com/Niranjan-207/EcoLearn, branch `main`) when a chunk of work is complete and every check passes** (user authorisation, 2026-09-21). Never force-push, never rewrite pushed history, never commit secrets (`.env`, keys) or local files (`venv/`, `data/progress.db`, `chroma_db/`).
  Run the full check list (§6) first; a red check means no commit. Write a descriptive message
  (what changed and why), not ".". Report the pushed commit hash to the user.
- *(Before 2026-09-21 the rule was "never commit — the user commits". Superseded.)* For risky or
  experimental work, suggest a feature branch instead of committing straight to `main`.
- **The remote is the only backup** — so push after every successful chunk, and never leave a day's
  work only in the working tree.
- **Log every change.** After any request that adds, modifies or removes something in this
  directory, append an entry to **`PROJECT_HISTORY.md`** with **Changed / Why / Learned**
  (absolute date, terse file-level bullets — the diff is in git, the doc is for narrative
  continuity). Only add to "Hard-won lessons" when the takeaway is genuinely new.
  *There is no `LOG.md` — it was consolidated into `PROJECT_HISTORY.md` on 2026-09-21. Don't
  recreate it.*
- **Explain the why.** Beginner-friendly explanations are appreciated — this is a learning project
  as much as a product. Say what a thing does *and* why it's built that way.
- **Honest, specific critique over vague praise.** If something is wrong, say so plainly and name
  the failure mode.
- **Verify, don't claim.** Run the tests, `curl.exe` the endpoint, check a computed style. The
  screenshot path is unreliable in this environment — prefer `tsc --noEmit`, HTTP status checks and
  `getComputedStyle` over images.

---

## 6. Running it

### First time on a new machine

```bash
git clone https://github.com/Niranjan-207/EcoLearn.git && cd EcoLearn
python -m venv venv                          # Windows: venv\Scripts\Activate.ps1
pip install -r requirements.txt               # macOS/Linux: source venv/bin/activate
cp .env.example .env                          # then paste your own GEMINI_API_KEY (optional, see below)
python src/rag/build_index.py                 # rebuild the vector index (needed for the doubt chat)
cd web && npm install                         # Node 18+
echo NEXT_PUBLIC_API_URL=http://localhost:8000 > .env.local
```

Then run the two servers (§ "Day to day") and open http://localhost:3000. **Check it works** with
`venv\Scripts\python.exe scripts\validate_lessons.py` and the test list below — no API key needed
for any of it.

**You do NOT need a Gemini API key** to write lessons, serve them, or answer check questions:
grading is multiple choice against the lesson file, and lessons are written by Claude Code sessions
straight to disk. The key is only for the doubt chat (`ask_help`), which is the one live LLM
feature. Without it, every other part of the app still works.

**Everything is in git except local, regenerable things.** A fresh clone gives you all lessons,
images, curriculum, code and docs. `venv/`, `chroma_db/`, `data/progress.db` (your local accounts
and progress), `node_modules/`, `.env` and `.claude/` are gitignored and If you received this folder with a `venv/` built on Windows (`venv/Scripts/`) and
you're on macOS or Linux, delete it and recreate. **If a `.env` came with the folder, rotate that
API key.**

**`.claude/launch.json`** (gitignored, local preview config) contains **absolute Windows paths**
(`D:\Projects\EcoLearn\...`), so it does not come with a clone. Recreate it for your own path if
you use the preview tools; the `web` entry must use **port 3000**, because the API's CORS list
allows only `http://localhost:3000` to send the session cookie. It needs three entries: `api`
(`python -m uvicorn api.main:app --reload --port 8000`, cwd = repo root), `web` (`npm run dev --
--port 3000`, cwd = `web/`) and optionally `streamlit`.

**Picking up someone else's work:** read `PROJECT_HISTORY.md` from §9 onwards (newest last) for
what happened and why, then `venv\Scripts\python.exe scripts\batch_status.py --all` for what is
written, part-written and still to do. Those two plus this file are the whole handoff.

### Day to day

```bash
python -m uvicorn api.main:app --reload --port 8000    # terminal 1 — API, docs at /docs
cd web && npm run dev                                   # terminal 2 — http://localhost:3000
streamlit run app.py                                    # legacy UI (optional)
```

### Verify before you call anything done

```bash
# deterministic — no API key needed, these must always pass
venv\Scripts\python.exe tests\test_auth.py
venv\Scripts\python.exe tests\test_curriculum.py
venv\Scripts\python.exe tests\test_path_engine.py
venv\Scripts\python.exe tests\test_edge_states.py
venv\Scripts\python.exe tests\test_scale_chapter2.py
venv\Scripts\python.exe tests\test_persistence.py seed
venv\Scripts\python.exe tests\test_persistence.py verify
venv\Scripts\python.exe tests\test_content_spine.py
venv\Scripts\python.exe tests\test_authored_lessons.py
venv\Scripts\python.exe tests\test_api_auth.py
venv\Scripts\python.exe tests\test_mcq_grading.py         # MCQ grading, no API key needed
venv\Scripts\python.exe scripts\validate_lessons.py        # every authored lesson
venv\Scripts\python.exe scripts\batch_status.py            # lesson plan progress + next batch

# web changes
cd web && npx tsc --noEmit && npm run lint && npm run build
```

`tests/test_platform_api.py` is the live contract canary — it calls real LLMs, is slow, and burns
quota. Run it deliberately, not routinely.

---

## 7. Gotchas that will cost you an hour

- **Next.js 16 is not the Next.js you know.** `middleware` → `proxy`; `error.tsx` uses
  `unstable_retry`, not `reset`. **Read `web/node_modules/next/dist/docs/` before touching
  routing, cookies or error files** (see `web/AGENTS.md`). Do route protection with a **client
  guard, not `proxy.ts`** — the API cookie is on a different origin, so a web-origin proxy never
  sees it. The real boundary is the API's `Depends`.
- **Only ONE `next dev` per project dir** — a second refuses even on another port. Reuse it.
- **Tailwind v4 theme edits need a dev-server restart.** `@theme` / `:root` / `.dark` value
  changes can serve a stale CSS chunk even though JSX hot-reloads.
- **Tailwind v4 has no JS config** — theme and plugins are declared in CSS (`@theme`, `@plugin`).
- **`fetch` does not throw on 4xx/5xx.** Check `response.ok`.
- **CORS:** the browser blocks Next(3000) → FastAPI(8000) unless the origin is allowed. `curl`
  bypasses CORS, so test with an `Origin` header too. `allow_credentials=True` is incompatible
  with `allow_origins=["*"]`.
- **Windows:** in PowerShell `curl` is an alias — use `curl.exe`. A busy port throws
  `[WinError 10013]`, not "address in use".
- **Run uvicorn from the project root** (`api.main:app`) so the `src` package resolves.
- **Docstrings have drifted from the code** in a few places. The code is the source of truth.

Full list: `PROJECT_HISTORY.md` §13.

---

## 8. Definition of done

- Relevant deterministic tests pass; `tsc --noEmit` + `npm run build` clean for web changes.
- `PROJECT_HISTORY.md` updated (Changed / Why / Learned).
- `ROADMAP.md` milestone status updated if you advanced or finished one.
- Committed with a descriptive message and pushed to `origin main`; report the commit hash.
