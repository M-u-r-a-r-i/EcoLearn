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

**EcoLearn is a personalised AI tutor for CBSE/ISC Class 11 and 12 Physics.** A student picks an
interest (cricket, football, gaming, smartphones, motorsport) and their hobbies, and takes a
five-minute **starting check**. Every concept is taught through a **pre-written, reviewed lesson**
in their interest. The check's answers reveal **misconceptions**, so the roadmap skips what they
know and points at what to fix. **AI agents** add a short **personal story** around one of their
hobbies on top of the reviewed lesson, and help **teachers** plan the next class from the data.
It is full-stack: **FastAPI + Next.js** (primary), with **Streamlit** kept as a legacy UI over the
same backend. The curriculum is the full Class 11 + 12 syllabus for both boards (29 chapters, 249
concepts); lessons exist for an agreed subset, **14 chapters × 5 interests** (`data/content_scope.yaml`).

The one architectural fact everything depends on:

> **All logic lives behind `src/platform_api.py`, which returns plain JSON-serializable dicts.
> Every frontend calls only that boundary.**

*(The project is a physics tutor despite the "EcoLearn" name, a holdover. Don't rename ids or the
repo; whether to change the display name for the finals is an open question for the user.)*

---

## 2. Where we are right now

### Your first session — do these in order, before writing any code

1. **Read `PROJECT_HISTORY.md` §9 onwards (newest last) and `ROADMAP.md` §0.** This file is the
   summary; those are the substance. (`PROJECT_HISTORY.md` §1–§7 describe the project as of
   2026-09-21 and are partly out of date; trust §9+ and this file.)
2. **Check the handoff state:** `git pull --ff-only`, then `git status` and `git log --oneline -5`.
   **If there are uncommitted changes you didn't make, they are the handoff — never `reset`,
   `checkout .`, `stash drop` or `clean` them.**
3. **Run the deterministic suite (§6).** All of it should pass. If anything fails, stop and tell
   the user before building on top.
4. **Remind the user about the OmniRoute setup** (they asked to be reminded; see "Machine issues").
5. **Tell the user, in a few sentences, what you understood** — where the project is, the choices
   for the next step (below), anything inconsistent — and let them pick before you start.

### The goal

**HackAStone 2026 finals: 2026-10-29**, at the *AI for Education Holland* conference (VU
Amsterdam, 29–30 Oct; NTU Singapore is on the organising committee; conference theme "Research
meets Practice": evidence, responsible AI, classroom adoption). **Contest theme: "Agentic AI for
Education". The final is a 15-minute presentation.** Judging criteria (a slide the user shared on
2026-10-02, marked "to be firmed"): **Innovation 30% · Technology readiness 20% · Commercial
viability 15% · Education significance 15% · Presentation 10% · Demo 10%.** Before
that, a **pilot with real school students in October**, whose numbers go in the pitch. (The original
build deadline, 2026-09-30, has passed; work continues toward the pilot and the finals.)

### User decisions — don't re-litigate them

- **Accounts: username + password, no email** (the pilot is on minors — minimal PII). Password
  resets go through the student's teacher.
- **Content scope (2026-09-22):** **14 chapters** (7 Class 11 + 7 Class 12) × **5 interests**
  (cricket, football, gaming, smartphones, motorsport), in `data/content_scope.yaml`. Phase 1 the
  `explain` format; phase 2 `challenge` + `misconception`. The rest comes after the finals.
  Students are on **CBSE and ISC** — every concept carries `boards`.
- **Chapters are never locked; concepts open in order** (revised 2026-10-03, §9zt): the next concept
  opens once the one before is done (or the starting check says they know it). Prerequisites and
  recommendations are still only hints. **Only a teacher moves a student between Class 11 and 12.**
- **Every lesson opens with a story and has images.** **Never download an image without the
  user's approval**; every famous image needs a manifest entry (`content/AUTHORING_GUIDE.md` §4a, §7a).
- **Static lessons are written by Claude Code sessions straight to files** — no LLM API for them.
  Quality: the authoring guide + gold examples, a deterministic validator, audits of interrupted
  batches, human reading of pilot chapters.
- **Check questions are multiple choice**, each wrong option mapped to a misconception, graded with
  **no LLM call**.
- **Live AI is allowed in exactly three places** (2026-10-02): the doubt chat (`ask_help`), the
  **teacher agent** (`generate_class_plan`) and **personal stories** (background only). Each has a
  non-AI fallback. Anything else stays pre-generated (non-negotiable 3).
- **New agents call models through `src/llm/`**, an OpenAI-compatible client. **For now: OmniRoute
  and free models; the user will buy a Gemini API key once it works as planned** (then it's a
  config change: Gemini's OpenAI-compatible URL).
- **Personal stories are shown first, with the lesson's pre-written story in a collapsible box.**
- **Run locally first**; cloud hosting later.

### Current state (everything committed and pushed; last code commit `e920f30`, 2026-10-03)

**Repo:** github.com/Niranjan-207/EcoLearn, branch **`main`**. A teammate (GitHub `M-u-r-a-r-i`)
also pushes lesson batches — always `git pull --ff-only` first.

**What a student does today** (all verified in a browser):
**first sign-in → `/welcome`: "getting to know you"** (§9zy; a gate sends any student who hasn't
answered it there; fixed options only, every question skippable, taken once) →
sign up (2 steps) → **`/start`: the starting check** (hobbies + 8 questions with "not sure", taken
once, its result a learning plan) → **roadmap** (chapter picker marks "coming soon" chapters;
concepts tagged "Know it?" / "Focus"; "Next up" follows the personal recommendation) → **lesson**
("Your story" for their hobby when one exists, the original story in a box, a "Something wrong with
this story?" report button, 👍/👎, active reading time recorded) → **multiple-choice check**
(misconception feedback) → progress. Plus settings, a dark/light/device theme toggle, error and 404
pages. When the teacher opens it, **`/end-check`**: the same 8 ideas with new questions, and a
before → after (fixed mix-ups, ideas learned since "not sure", what slipped). Every check asks
**"How sure are you?"** after an option is picked, and **`/mix-ups`** lists each misconception as
to fix / check again / fixed (fixed = right on a *different* question about the idea).
**Mastered needs two different questions right** (§9zn): one right answer is "cleared" (the path
moves on), and **`/review`** asks a fresh question (another interest's check) about a day later.

**What a teacher does today:** accounts are created on the server only
(`venv\Scripts\python.exe scripts\create_teacher.py --name "…" --username …`). A teacher creates a
class from pasted names (printable login slips, passwords shown once) and resets passwords (which
also lifts a login lockout). **`/teacher/class`** has:
- the **Teaching assistant**, a tool-calling agent that plans the next lesson; it sees students
  only as S1, S2…, and falls back to a labelled rules plan;
- **insights**: first-try accuracy, the most common misconceptions (counted per student, with how
  many were sure of it), "sure but wrong", concepts hardest-first, and results by interest;
- **starting check → end check**: open/close the end check; before → after right answers and
  mix-ups over paired answers, studied vs not-studied ideas (a rough control), per idea and per
  student;
- **personal stories**: read, hide or restore them, with students' reports first;
- **How the AI decided** (§9zp): the story guardrail pipeline with this class's counts (drafts,
  rule-check rejections, critic rejections, shown), safe fallbacks, human review, teaching-
  assistant plans by AI vs rules fallback, model calls, and a decision log with each story's
  step-by-step trail and reasons;
- the students table.

**Where things live** (each with its `PROJECT_HISTORY.md` entry):

| Area | Files | § |
|---|---|---|
| Boundary (all logic) | `src/platform_api.py` | — |
| **"Getting to know you" survey** (first login: hobbies + depth, focus, how they learn, feelings about physics; drives lesson prefs, story notes, teacher profile) | `data/survey.yaml`, `src/learner/survey.py`, `platform_api.{get_survey,submit_survey,get_class_learner_profiles}`, `web/app/(app)/welcome`, `web/components/{survey-flow,welcome-gate,break-nudge,class-profiles}.tsx` | 9zy |
| Starting check, plan, recommendations | `data/diagnostic.yaml`, `src/learner/{diagnostic,plan}.py` | 9zd |
| Mastery from evidence + revision queue | `learner_plan.mastery_evidence`, `platform_api` §"Mastery from evidence", `web/app/(app)/review` | 9zn |
| "How the AI decided" (decision trails) | `personal_story.generate` (trail), `platform_api.get_class_ai_decisions`, `web/components/ai-decisions.tsx` | 9zp |
| AI usage log + cost per student | `src/llm/client.py` (usage sink), `store.llm_calls`, `metrics.ai_usage`, `data/llm_prices.yaml` | 9zn |
| My mix-ups + "how sure are you?" | `learner_plan.mix_up_history`, `diagnostic.clean_confidence`, `web/app/(app)/mix-ups`, `web/components/confidence-picker.tsx` | 9zm |
| End check (pilot before → after, counterbalanced forms) | `src/learner/diagnostic.py`, `metrics.check_gains`, `web/app/(app)/end-check`, `web/components/class-checks.tsx` | 9zl |
| Personal stories (writer + critic agents) | `src/learner/personal_story.py`, `prompts/personal_story_*.txt` | 9ze, 9zf |
| LLM client (OpenAI-compatible, OmniRoute) | `src/llm/client.py`, `.env.example` (LLM_* vars) | 9ze |
| Teacher agent | `src/agents/teacher_agent.py`, `prompts/teacher_agent.txt` | 9zc |
| Pilot metrics + dashboards | `src/progress/metrics.py`, `scripts/pilot_report.py` | 9za |
| Chapter coverage / coming soon | `lesson_service.concepts_with_lessons` | 9zb |
| Login rate limiting | `api/ratelimit.py` | 9zg |
| Caches (parsed files, scans, schema) | `src/file_cache.py`, `lesson_service`, `store._connect` | 9zh |
| Load test (30 students at once) | `scripts/load_test.py` (p95 ≈ 1.2 s, 0 errors) | 9zh |
| Theme, toasts, error pages | `web/components/{theme-toggle,toast}.tsx`, `web/app/{error,not-found,global-error}.tsx` | 9zg, 9zi |
| 127.0.0.1 vs localhost fix | `web/next.config.ts`, `web/lib/api.ts` (API_URL) | 9zj |

**Content:** `data/curriculum/physics.yaml` (29 chapters / 249 concepts; never rename an id).
**642 authored lessons, all valid.** Phase 1 (`explain`) is at **62/70 batches**: cricket,
football, gaming 14/14 chapters; smartphones 13; motorsport 7. `scripts/batch_status.py` names the
next batch (the batch procedure is below). Famous images: `data/media/famous/`, 8 approved.

**Not built or not verified yet** (honest list):
- **No live AI run has happened.** Personal stories and the teacher agent are tested against mocks
  only. The "being written…" polling state is unverified in a browser.
- The doubt chat is broken on this machine (see below), and takes ~2 min when it works.
- Mastery now needs two different questions right (§9zn), but concepts mastered before
  2026-10-03 under the old one-answer rule keep their status.
- The AI usage log has tokens for `src/llm` calls only; the doubt chat (older google-genai
  pipeline) and the teacher agent's Gemini fallback log no tokens. `data/llm_prices.yaml` was
  typed from memory: verify before quoting a ₹ figure.
- The end check's two forms are different lessons' checks on the same concept, written
  independently, not psychometrically matched. Counterbalancing cancels a difference in difficulty
  on average across a class; it doesn't make one student's two forms equal (§9zl).
- The landing page (`web/app/page.tsx`) is generic and says nothing about physics. `README.md` is
  out of date. Streamlit doesn't have any of the October features.
- Phase 2 lesson formats (`challenge`, `misconception`): 2 of 70 batches.

### -> YOUR NEXT ACTION: ask the user which of these to do (they choose the order)

**Prioritise by the judging weights** (Innovation 30, Technology readiness 20, Commercial 15,
Education 15, Presentation 10, Demo 10). Content volume alone scores little.

**Done since the 2026-10-02 handoff** (the pre-pilot list agreed with the user on 2026-10-02):
end check with counterbalanced forms (§9zl) → "My mix-ups" + "How sure are you?" (§9zm) →
two-question mastery + revision queue + AI usage/cost log (§9zn) → "How the AI decided" (§9zp).

**The user's stated order now:** they set up **OmniRoute** themselves first (they asked to be
reminded), *then* the **pre-pilot cleanup**. Don't start either without them.

Candidates in between or after, by value for the finals (the user picks):
1. ~~"How the AI decided" panel~~ **done 2026-10-03 (§9zp).**
2. ~~**Demo dataset**~~ **done 2026-10-03 (§9zr): `scripts/seed_demo.py --reset`, then run the API with `ECOLEARN_PROGRESS_DB=data\demo.db`.** Original idea: a script filling a *separate* DB (`ECOLEARN_PROGRESS_DB=
   data/demo.db`) with a realistic class (~25 students, starting + end checks, lessons, mix-ups,
   confidence, revision), so the dashboards are full on stage and pilot data stays clean. ~1 day.
3. **Doubt chat without grpc** (Readiness, Demo): it depends on chromadb → grpc, which Windows
   Application Control blocks here, and takes ~2 min. With 249 concepts an in-process numpy
   search over the existing MiniLM embeddings would remove grpc. Moving it onto `src/llm` would
   also give it token counts in the usage log. ~1 day.
4. **Landing page** (`web/app/page.tsx` says nothing about physics). ~½ day.
5. **Dev-only error detail** on `web/app/error.tsx` (show `error.message` when
   `process.env.NODE_ENV === "development"`), see Open threads 3. ~15 min.
6. **Local GPU backend** (the user has an **RTX 3090, 24 GB**): Ollama / llama.cpp / vLLM exposes
   an OpenAI-compatible URL, so `src/llm` needs only `LLM_BASE_URL` + `LLM_MODEL`. A private,
   always-available alternative (or OmniRoute upstream) to free cloud tiers for stories and the
   teaching assistant. The user's call; it's M1a's plan done small.
7. Later: teacher report + "assign concepts", interactive simulations, phone check of every
   student page, the remaining lesson batches (scope question below).

### Machine issues to raise with the user

- **OmniRoute is not installed** (nothing on `localhost:20128`, checked 2026-10-02). **The user
  asked to be reminded to set it up.** Installing a global npm package is their step. Until then
  `LLM_MODEL` is unset and no story is written. Advise connecting real free tiers inside OmniRoute
  (AI Studio key, Groq, OpenRouter free) rather than its keyless web-scraping pools.
- **The `GEMINI_API_KEY` in `.env` is rejected (401)** both as an AI Studio key and as a Vertex
  express key (it starts `AQ.`; AI Studio keys start `AIza`). Never print or commit it.
- **Windows Application Control blocks `grpc`'s DLL**, so the doubt chat answers 503 here (§9z).
  A machine setting or a `grpcio` reinstall: the user's call.
- **The user often starts the API with the system Python** (`WindowsApps\…\Python 3.12`). It works;
  recommend `venv\Scripts\python.exe -m uvicorn api.main:app --reload --port 8000`. The web app works
  at both `localhost:3000` and `127.0.0.1:3000` since §9zj. **On 2026-10-03 two API servers were
  running at once** (one from the venv, one from the system Python; only one can hold port 8000).
  Suggest closing the extra terminal.
- **Load-test timing depends on the machine's state.** On 2026-10-03 it failed for a while on old
  and new code alike (30 bcrypt logins ~4 s), then passed (p95 1.4 s). If it fails, run the
  previous commit beside it from a temporary `git worktree` before blaming a change (§9zn).
- **The browser pane's `localhost` session is the user's own.** Sessions use per-origin cookies, so
  checking as a test account at `127.0.0.1:3000` leaves it untouched (done in §9zl–§9zn).

### Open threads

1. **Local test data in `data/progress.db`** (gitignored, never pushed) — delete before the
   pilot or exclude from its numbers:
   - teachers `demo.teacher` ("Demo 11-B": `aarav.k`, `meera.i`, `kabir.s`) and `metrics.check`
     ("Metrics check 11-A": `test.o`, `test.t`, `test.t2`);
   - teacher `endcheck.teacher` ("End check test": `asha.r`, `bilal.k`, `chitra.n`; the end
     check is open and all three have taken it; `chitra.n` and `asha.r` also answered lesson
     checks, `asha.r` a revision question), from the §9zl–§9zn browser checks;
   - `dev.r` and `esha.r`, also in "End check test" (added 2026-10-03 while reproducing the
     error report in thread 3);
   - a **blocked** personal story for `asha.r` (second_law) written by a scripted stand-in model
     ("scripted-main (UI check)"), the §9zp browser check of the decision log;
   - self-signup students `start.check` and `loop.check`;
   - two hand-seeded personal stories (model "ui-check (seeded by hand)").

   Passwords were never written to the repo. Use `scripts/create_teacher.py` for a fresh teacher,
   and a teacher's "Reset password" for class students. The user's own accounts are `niranjan_207`
   and `demo_student` (self-signup; only a local reset via `store.update_student_password`, with
   their go-ahead).
2. **Two machines:** pull first, and agree with the teammate who takes which lesson batches.
3. **"Something went wrong" after a teacher-created student logged in** (user report,
   2026-10-03, at `localhost:3000`). **Not reproduced:** the same path at `127.0.0.1:3000` (add a
   student → log out → log in through the form) landed on the roadmap, no console errors; `/start`
   and `/roadmap` render for a new class student. Likely a browser tab opened before the day's
   changes (stale dev chunks); a hard refresh should fix it. If it recurs, ask for the red console
   line under the error and the URL. Candidate fix: item 5 in the next-action list.

### Open with the user, don't decide alone

1. **Scope:** finish all five interests (~36 more batches incl. phase 2), or finish cricket,
   football and gaming first and leave smartphones and motorsport until after the finals? Not yet
   ruled on.
2. **Famous images requested, not yet approved:** Volta (electric_potential), Faraday
   (capacitance / dielectrics), Joule (kinetic_energy / power). De Broglie was **rejected** on
   licence grounds.
3. **The display name** "EcoLearn" (reads as sustainability) for the finals: their call.
4. **Agentic features in the demo:** which live AI pieces to show on stage, given the free-model
   setup's reliability.

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
   **One deliberate exception (user request, 2026-10-02): the teacher agent**
   (`generate_class_plan`, §9zc). It is teacher-triggered and low-volume, read-only, never on a
   student's path, reuses a plan less than a minute old, and falls back to a rules-based plan, so
   it costs nothing at student scale and can't take anything down. **Second exception (user
   request, 2026-10-02): personal stories** (§9ze) — written in the background, never blocking a
   page, cached per student × concept, critic-checked, and the reviewed story is always shown when
   anything fails. Any further live call needs the user's say-so.
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
   moves to a **self-hosted LLM on a GPU** in M1a, with the Gemini API as fallback. **`src/llm/`
   exists since 2026-10-02 (§9ze)**: an OpenAI-compatible client (OmniRoute for the free pilot, the
   user's choice; Gemini's OpenAI-compatible URL later). **New agents call models only through
   `src/llm/`**; the four older agents still use google-genai directly until the rest of M1a. Don't add a third provider without asking. Judges fail open; key roles keep
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
straight to disk. Live AI (doubt chat, teacher agent, personal stories) needs a model: `LLM_*` for OmniRoute
(see `.env.example`) or a Gemini key. Without one, every feature falls back and the app still works.

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
venv\Scripts\python.exe tests\test_teacher.py             # teacher tools: classes, resets, roles
venv\Scripts\python.exe tests\test_pilot_metrics.py       # views, answers, 👍/👎, class insights
venv\Scripts\python.exe tests\test_chapter_coverage.py    # picker counts, coming-soon concepts
venv\Scripts\python.exe tests\test_teacher_agent.py       # agent loop, privacy, fallbacks (no network)
venv\Scripts\python.exe tests\test_learner_plan.py        # starting check, learning plan, recommendations
venv\Scripts\python.exe tests\test_personal_story.py      # story agents, llm client, OmniRoute mock
venv\Scripts\python.exe tests\test_story_review.py        # report button, teacher hide/restore
venv\Scripts\python.exe tests\test_rate_limit.py          # login lockouts (fake clock)
venv\Scripts\python.exe tests\test_end_check.py           # end check: forms, access, before -> after
venv\Scripts\python.exe tests\test_mix_ups.py             # my mix-ups, "how sure are you?"
venv\Scripts\python.exe tests\test_mastery.py             # two-question mastery, revision queue
venv\Scripts\python.exe tests\test_llm_usage.py           # AI usage log, cost per student
venv\Scripts\python.exe tests\test_ai_decisions.py        # decision trails, "How the AI decided"
venv\Scripts\python.exe tests\test_concept_locks.py       # concept locks, class level (teacher only)
venv\Scripts\python.exe tests\test_survey.py              # "getting to know you": validation, traits, prefs, HTTP
venv\Scripts\python.exe tests\test_seed_demo.py           # demo dataset builds into a temp DB (~1 min)
venv\Scripts\python.exe scripts\load_test.py              # 30 students at once, own temp server (~15 s)
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
- **Never import a live-LLM feature's dependencies at module top level** in `platform_api.py`.
  chromadb → grpc native DLLs were once blocked by Windows Application Control, and the top-level
  import took the whole API down (§9z).
- **Parsed files and lesson scans are cached** (§9zh, `src/file_cache.py`, `lesson_service`):
  objects they return are shared — never mutate them. Edits to a file are seen at once (mtime);
  the "which concepts have lessons" lists may lag up to 30 s after a writing session adds files.
  An env var set to empty means "off" (it does not fall back to `.env`).
- **A new route folder can 404 in `next dev`** while `npm run build` lists it. Restart the dev
  server, and don't run `npm run build` while `next dev` is running (both write `.next`).

Full list: `PROJECT_HISTORY.md` §13.

---

## 8. Definition of done

- Relevant deterministic tests pass; `tsc --noEmit` + `npm run build` clean for web changes.
- `PROJECT_HISTORY.md` updated (Changed / Why / Learned).
- `ROADMAP.md` milestone status updated if you advanced or finished one.
- Committed with a descriptive message and pushed to `origin main`; report the commit hash.
