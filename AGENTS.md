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
2 chapters, 17 concepts, 34 pre-generated lessons, all committed and working. The plan scales this
to the full Class 11 + 12 syllabus × 15–20 interests, generated on a self-hosted GPU (§2).

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
   `stash drop` or `clean` them.** The previous instance never commits (the user does), so the
   latest work may exist only in the working tree.
3. **Run the deterministic suite (§6).** All of it should pass. If anything fails, stop and tell
   the user before building on top — something changed since the handoff.
4. **Tell the user, in a few sentences, what you understood** — where the project is, the next
   action, and anything that looked inconsistent. Let them correct you before you start.
5. Then begin the next action below.

### The goal

The user has set three scale-up goals (2026-09-21):

- **Full Class 11 + Class 12 Physics** — 28 chapters, ~250 concepts (today: 2 chapters, 17).
- **15–20 interests** (today: 2). Which ones is still the user's call (decision I1).
- **Generation on a self-hosted LLM running on a GPU**, instead of a paid API tier.

Together: ~250 concepts × 20 interests × 5 formats ≈ **25,000 lessons**, against 34 today. That
scale-up is already planned and woven into the milestones (§3 and `ROADMAP.md` §1). It is **not**
the immediate next action — Milestone 0 is in flight and finishes first.

### Current state

**Branch:** `auth-and-ux`. Work here. **Milestone 0 (accounts, auth & UX foundation) is in
progress: the backend auth core is DONE and TESTED; the HTTP layer and all frontend work are NOT
started.**

**Done and verified** (see `ROADMAP.md` §5 for the detail): `src/errors.py`,
`src/auth/passwords.py`, the additive `students` migration + credential functions in
`src/progress/store.py`, the five account functions in `src/platform_api.py`
(`register_student`, `authenticate_student`, `get_student_profile`, `update_student_profile`,
`change_password`), and `NotFoundError` for unknown chapters in `src/path/engine.py`.

**Proof it works:** `venv\Scripts\python.exe tests\test_auth.py` → **60 checks pass**, covering
the migration from an old-shape DB, bcrypt's 72-byte cliff, every error branch, and the two
backwards-compatibility contracts. Run it first — if it's green, the foundation under you is
sound and you can build straight on top. The other deterministic tests pass too.

> Don't re-derive or rewrite that layer. It is finished. Start at the next action below.

**→ YOUR NEXT ACTION:** `api/security.py` — PyJWT HS256, claims `{sub, iat, exp}`, ~7-day TTL,
secret from `ECOLEARN_JWT_SECRET`, httpOnly + `samesite="lax"` cookie, and a
`get_current_student_id(request)` dependency that 401s. Then the new endpoints and exception
handlers in `api/main.py`. `ROADMAP.md` §5 lists everything remaining in order, including the
frontend work and the atomic "breaking flip".

Keep every change **additive** until that flip, so Streamlit and the current web app keep working.

**Two forward-looking constraints on M0** (details in `ROADMAP.md` §5):
- Build the web chapter picker for **28 chapters grouped class → unit**, not a flat list of 2 —
  M1 enriches `GET /api/chapters` with `unit_id`, `unit_name` and `grade`.
- Build the interest picker for **~20 interests**, not 2 big cards — read them from one typed list
  (`lib/interests.ts`) shaped like the future `GET /api/interests`, which M1 introduces.

### ⛔ Checkpoint after Milestone 0

**When M0's acceptance criteria pass, stop and ask the user every decision marked "After M0" in
`ROADMAP.md` §15 before starting M1 or M1a.** That is currently **S1, S2, I1, I3, L0, L1, L3, L4**:

| | Decision |
|---|---|
| S1, S2 | Concept ordering scheme; one physics subject vs one per class |
| I1, I3 | Which 15–20 interests; how interest corpora are sourced |
| L0 | **The GPU facts** — which GPU and how much VRAM, where it runs, when it's available |
| L1, L3, L4 | Always-on vs batch-only; serving stack; keep the Gemini API as a fallback |

They are the user's calls, not yours. Put the recommended default for each in front of them (most
can be accepted in one line), record the answers in `ROADMAP.md`, then start. The other decisions
(S3, S4, I2, I4, L2) are asked later, at the milestone that needs them — the "Ask when" column
says exactly when.

---

## 3. The phases, in the order they must be done

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
   (`submit_assessment`). Everything else is served from pre-generated cache. **This is the entire
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
11. **Never commit or push.** See §5.

---

## 5. How the user works (match this)

- **Never auto-commit or push.** The user runs every commit themselves. Stage nothing on their
  behalf without asking; propose the commit command instead. For any change to `master`, suggest a
  feature branch first.
- **Remind them to push** after a successful chunk of work — it's easy to forget and the remote is
  the only backup.
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
python -m venv venv                          # Windows: venv\Scripts\Activate.ps1
pip install -r requirements.txt               # macOS/Linux: source venv/bin/activate
cp .env.example .env                          # then paste your own GEMINI_API_KEY
python src/rag/build_index.py                 # rebuild the vector index (needed for the doubt chat)
cd web && npm install                         # Node 18+
echo NEXT_PUBLIC_API_URL=http://localhost:8000 > .env.local
```

`venv/`, `chroma_db/`, `data/progress.db`, `node_modules/` and `.env` are all gitignored and
regenerable. If you received this folder with a `venv/` built on Windows (`venv/Scripts/`) and
you're on macOS or Linux, delete it and recreate. **If a `.env` came with the folder, rotate that
API key.**

**`.claude/launch.json`** (gitignored, local preview config) contains **absolute Windows paths**
(`D:\Projects\EcoLearn\...`). If the project lives anywhere else on your machine, update or
recreate it before using the preview tools — it will otherwise point at a directory that doesn't
exist.

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
- Nothing committed or pushed — hand the user the commit command and remind them to push.
