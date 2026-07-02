<div align="center">

# 🌱 EcoLearn

### A personalized AI physics tutor that teaches Class 11 Physics through what you love

*Pick **football** or **gaming** — every concept is taught by grounding its analogies in your interest.*

<br>

![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.138-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Next.js](https://img.shields.io/badge/Next.js-16-000000?style=for-the-badge&logo=nextdotjs&logoColor=white)
![React](https://img.shields.io/badge/React-19-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini%20%2F%20Gemma-4F46E5?style=for-the-badge&logo=googlegemini&logoColor=white)

![Streamlit](https://img.shields.io/badge/Streamlit-1.58-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![Tailwind](https://img.shields.io/badge/Tailwind-v4-38BDF8?style=flat-square&logo=tailwindcss&logoColor=white)
![shadcn/ui](https://img.shields.io/badge/shadcn%2Fui-black?style=flat-square)
![ChromaDB](https://img.shields.io/badge/ChromaDB-RAG-F59E0B?style=flat-square)
![SQLite](https://img.shields.io/badge/SQLite-progress-003B57?style=flat-square&logo=sqlite&logoColor=white)

![Architecture](https://img.shields.io/badge/architecture-multi--agent%20%2B%20RAG-10B981?style=flat-square)
![Frontends](https://img.shields.io/badge/frontend-Next.js%20(%2B%20Streamlit%20legacy)-1E293B?style=flat-square)
![Status](https://img.shields.io/badge/status-full--stack%20journey%20working-4F46E5?style=flat-square)

</div>

---

> [!NOTE]
> **For evaluators:** this document is the single place to understand *what*
> EcoLearn is, *how* it is built, *why* the key decisions were made, *what its
> limitations are*, and *how to run it*. Want it live right now? Jump to
> **[▶ Running it yourself](#5--running-it-yourself-step-by-step)**.

## 📑 Table of contents

| | Section | | Section |
|---|---|---|---|
| 1 | [What EcoLearn is](#1--what-ecolearn-is) | 6 | [Environment variables](#6--environment-variables) |
| 2 | [Tech stack](#2--tech-stack--everything-used-and-why) | 7 | [Known limitations & trade-offs](#7--known-limitations--trade-offs-honest) |
| 3 | [Architecture](#3--architecture) | 8 | [Engineering principles](#8--engineering-principles-the-why) |
| 4 | [Repository layout](#4--repository-layout-load-bearing-files) | 9 | [Where to read more](#9--where-to-read-more) |
| 5 | [**Running it yourself**](#5--running-it-yourself-step-by-step) | | |

---

## 1. 🎯 What EcoLearn is

EcoLearn is a **personalized AI tutor for CBSE/ISC Class 11 Physics**
(Kinematics). A student picks something they already love — **⚽ football** or
**🎮 gaming** — and every concept is taught by grounding its analogies in that
interest. *"Relative velocity"* is explained through two players closing on a
through-ball; *"work–energy theorem"* through a nitro boost in a racing game.

It began as a single-page chatbot and was deliberately re-architected into a
**data-driven learning platform**:

```
curriculum spine  →  learning-path engine  →  service API  →  UI
                        (lessons pre-generated offline, served instantly)
```

Because all logic sits behind one plain-data **service boundary**, EcoLearn runs
as a modern **full-stack web app** — with a legacy option for convenience:

- ⚛️ **Next.js + FastAPI** *(primary)* — a React/Next.js website talking to a thin
  FastAPI layer over the backend. This is the main product; the full student
  journey works end-to-end. **→ [How to run it](#5--running-it-yourself-step-by-step)**
- 🐍 **Streamlit** *(legacy)* — the original all-in-one Python app, kept as a
  zero-Node reference UI over the exact same backend.

> [!IMPORTANT]
> **On the name:** "EcoLearn" is a holdover from an earlier
> sustainability-education concept. The codebase, curriculum, and content are
> entirely a **physics tutor** — the name was kept only to preserve git history.

---

## 2. 🧰 Tech stack — everything used, and why

### Backend, AI & data

| Layer | Technology | Why it's here |
|---|---|---|
| 🐍 Language / runtime | **Python 3.10** | Project baseline; fully type-annotated. |
| 🔌 LLM SDK | **`google-genai`** | Current Google GenAI SDK (the older `google-generativeai` is deprecated). |
| ✍️ Generation model | **Gemma `gemma-4-31b-it`** | Creative analogy generation; separate free-tier quota from Gemini Flash. |
| ⚖️ Critic / Polisher | **Gemini `gemini-2.5-flash-lite`** | Cheap, fast, strict-JSON judgement & markdown cleanup. |
| 📝 Assessor (grading) | **Gemma `gemma-4-31b-it`** *(+ fallback chain)* | Generates & grades the self-check question. |
| 🧠 Embeddings (RAG) | **`all-MiniLM-L6-v2`** (ONNX, local) | Bundled in ChromaDB — **no API, no key, no quota**. |
| 🗂️ Vector store | **ChromaDB** | Local RAG index over curriculum + interest corpora. |
| 🧾 Curriculum schema | **Pydantic** | Parse-don't-validate: YAML → typed objects at load. |
| 🗒️ Curriculum authoring | **PyYAML** | Non-programmer-friendly source of truth. |
| 💾 Progress store | **SQLite** (stdlib) | Durable per-student mastery + profiles; zero-setup. |
| 🎛️ Prompts | **plain `.txt` files** | Tunable without code changes, reviews, or rebuilds. |

### Frontend (primary) — Next.js + FastAPI

| Layer | Technology | Why it's here |
|---|---|---|
| 🚪 Web API | **FastAPI 0.138** + **Uvicorn** | Thin HTTP layer over `platform_api` — the browser can't import Python. |
| ⚛️ Framework | **Next.js 16** (App Router) + **React 19** | Modern, routable, component-based web frontend. |
| 🔤 Language | **TypeScript** | Typed API client + components. |
| 💅 Styling | **Tailwind CSS v4** + **shadcn/ui** (radix, lucide icons) | Utility-first styling + owned, editable components. |
| 📝 Markdown/Math | **react-markdown** + remark-gfm + **remark-math / rehype-katex** + `@tailwindcss/typography` | Render the backend's markdown & KaTeX lessons beautifully. |

### Frontend (legacy) — Streamlit (all-in-one Python)

| Layer | Technology | Why it's here |
|---|---|---|
| 🖥️ Web UI | **Streamlit 1.58** (multi-page) | The original app; ships a full UI in pure Python with no separate server. *(trade-offs in [§7](#7--known-limitations--trade-offs-honest))* |
| 🎨 Theming | Custom CSS design system + `.streamlit/config.toml` | Premium, calm look over Streamlit's defaults. |

---

## 3. 🏗️ Architecture

Two frontends, **one backend**, joined at a single plain-data boundary:

```
  🐍 Streamlit UI                    ⚛️ Next.js UI (web/)
  app.py · pages/ · src/ui                 │  fetch() over HTTP
        │                                   ▼
        │                        🚪 FastAPI (api/main.py)  ── thin HTTP wrapper
        │                                   │
        └──────────── both call ───────────┴────────────▶  src/platform_api.py
                                                                   │  orchestrates
             ┌──────────────┬──────────────┬───────────────┬──────────────┐
             ▼              ▼              ▼               ▼              ▼
        path engine     progress        lesson       live pipeline   curriculum
        (what next)      store         service      (gen→critic→      (YAML →
                        (SQLite)       (cached)       retry→polish)   typed objs)
```

**Two content paths, by design:**

- ⚡ **Cached lessons** — pre-generated offline, vetted once by the critic, served
  **instantly with no LLM call**. This delivers the stable curriculum.
- 🔴 **Live pipeline** — used **only** for *"I'm stuck — ask for help"* and for
  grading an assessment on submit. The only expensive/online calls in the app.

### 🚪 The service boundary — `src/platform_api.py`

Every UI talks to the platform through **one module** returning **plain
JSON-serializable data** — never reaching into the engine, store, or pipeline
directly. That rule is what let the Next.js frontend be a *pure presentation
swap*: FastAPI serializes the same dicts to JSON with zero custom encoders. The
six functions:

| Function | Purpose |
|---|---|
| `create_or_load_student(name, interest, level)` | Idempotent; `student_id` is a slug of the name. |
| `list_chapters()` | For the chapter picker. |
| `get_roadmap(student_id, chapter_id)` | Each concept tagged `mastered` / `available` / `locked` + prereqs. |
| `get_next_lesson(student_id, chapter_id, concept_id=None)` | What to teach next (or re-serve a concept). |
| `submit_assessment(student_id, concept_id, answer)` | Grades the answer against the lesson's check question. |
| `ask_help(student_id, concept_id, question)` | Live, grounded tutor answer (the only expensive call). |

### 🌐 The HTTP API — `api/main.py`

A thin FastAPI layer maps each endpoint to one boundary function (no logic of its
own). CORS is opened to the Next.js dev origin (`http://localhost:3000`).

| Method + path | Calls | Notes |
|---|---|---|
| `GET /` | — | Health check. |
| `POST /api/student` | `create_or_load_student` | Create/load a student. |
| `GET /api/roadmap` | `get_roadmap` | Query params: `student_id`, `chapter_id`. |
| `GET /api/next-lesson` | `get_next_lesson` | Query params (+ optional `concept_id`). |
| `POST /api/assessment` | `submit_assessment` | Live grade → writes mastery. |
| `POST /api/help` | `ask_help` | Live pipeline (slow, seconds–minutes). |

*(`list_chapters` is not yet exposed over HTTP — the Next.js app currently
targets the first chapter.)*

### ⚛️ The Next.js frontend — `web/`

Routes mirror the journey: `/` (landing) → `/onboarding` → `/roadmap` →
`/lesson` (with the live **"I'm stuck" help widget**) → `/assessment`. A typed
`web/lib/api.ts` client wraps `fetch`; the created student is held in React
Context. Instant screens (roadmap, lesson) render cached data; help & grading
show a "thinking/grading" state because they hit the live pipeline.

### 🤖 The AI design (multi-agent + RAG)

```
 ① RAG retrieve ─▶ ② Analogy Generator ─▶ ③ Critic ──FAIL──┐
   (ChromaDB)         (Gemma)              (Gemini, JSON)    │ feedback
                                              │PASS          │ loops back
                                              ▼              │  to ②
                          ④ Polisher (Gemini) ◀─────────────┘
                          (strip scratch, → LaTeX/KaTeX)
                                              │
                          ⑤ Assessor (Gemma): make & grade the check question
```

1. **RAG retrieval** grounds analogies in real numbers (a striker's sprint
   speed, a game's top speed) instead of hallucinations.
2. **Analogy Generator** writes the interest-grounded explanation.
3. **Pedagogical Critic** grades scientific correctness, pedagogical fit, and
   analogical integrity; on FAIL its feedback drives a regeneration.
4. **Polisher** extracts the clean final answer and normalizes math to KaTeX.
5. **Assessor** generates and grades the self-check question.

> [!TIP]
> **Mastery model:** `cleared` (score ≥ 2/3) drives *progression* and unlocks
> dependent concepts; `mastered` (3/3) earns the gold badge and drives
> spaced-repetition review. A 2/3 lets the student choose *"move on"* or
> *"practise again"*.

---

## 4. 🗺️ Repository layout (load-bearing files)

```text
🧩 Domain (shared by both frontends)
├─ src/platform_api.py            THE service boundary (6 functions)
├─ src/curriculum/                Pydantic schema + YAML loader (order, validation)
├─ src/path/engine.py             next_concept, get_roadmap, list_chapters
├─ src/progress/store.py          SQLite progress + students
├─ src/content/                   lesson schema · read service · offline factory
├─ src/agents/                    generator · critic · assessor · polisher (+ fallbacks)
├─ src/pipeline.py                explain_with_review: RAG→gen→critic→retry
└─ src/rag/                       ingest · build_index · retrieve (ChromaDB)

🌐 Web API (FastAPI)
└─ api/main.py                    Thin HTTP layer over platform_api (health + 5 endpoints)

⚛️ Next.js frontend
├─ web/app/                       Routes: / · /onboarding · /roadmap · /lesson · /assessment
├─ web/lib/api.ts                 Typed fetch client (createStudent, getRoadmap,
│                                  getNextLesson, askHelp, submitAssessment)
├─ web/components/                site-nav · page-container · section-heading ·
│                                  primary-button · markdown · help-widget ·
│                                  student-provider · ui/ (shadcn)
└─ web/.env.local                 NEXT_PUBLIC_API_URL (gitignored)

🐍 Streamlit frontend
├─ app.py                         Onboarding / landing (multi-page entry)
├─ pages/1_Roadmap.py · 2_Lesson.py · 3_Assessment.py
├─ ui_common.py · src/ui/         Session helpers + CSS design system
├─ .streamlit/config.toml         Pinned LIGHT base theme + palette
└─ legacy_chat_app.py             The original single-page chatbot, preserved

📦 Data & content
├─ data/curriculum/physics.yaml   Curriculum source of truth (2 chapters · 17 concepts)
├─ data/lessons/*.json            34 pre-generated, polished lessons (committed)
└─ prompts/*.txt                  System prompts (generator / critic / assessor)

📚 Misc
├─ tests/                         Deterministic + LLM-backed suites
└─ LOG.md                         Dated dev log (Changed / Why / Learned)
```

> [!NOTE]
> Not in the repo (created locally): `venv/`, `.env`, `web/node_modules/`,
> `web/.env.local`, `chroma_db/` (rebuildable), `data/progress.db` (runtime
> state). The 34 cached lessons **are** committed, so the core experience works
> on first run.

---

## 5. ▶️ Running it yourself (step by step)

> Works on **Windows**, **macOS**, and **Linux**. Commands shown for both
> PowerShell (Windows) and bash (macOS/Linux).

### 🔹 Step 0 — Prerequisites
- **Python 3.10+** on your PATH (`python --version`)
- **git**
- **Node.js 18+** and **npm** — *only for the Next.js frontend (Option B below)*
- *(optional — only for live grading & "ask for help")* a free
  **Google AI Studio API key** → https://aistudio.google.com/apikey

### 🔹 Step 1 — Clone the repository
```bash
git clone https://github.com/M-u-r-a-r-i/EcoLearn.git
cd EcoLearn
```

### 🔹 Step 2 — Create & activate a virtual environment
<table>
<tr><th>Windows (PowerShell)</th><th>macOS / Linux (bash)</th></tr>
<tr><td>

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

</td><td>

```bash
python3 -m venv venv
source venv/bin/activate
```

</td></tr>
</table>

### 🔹 Step 3 — Install Python dependencies
```bash
pip install -r requirements.txt
```

### 🔹 Step 4 — Configure your API key *(optional but recommended)*
<table>
<tr><th>Windows (PowerShell)</th><th>macOS / Linux (bash)</th></tr>
<tr><td>

```powershell
Copy-Item .env.example .env
```

</td><td>

```bash
cp .env.example .env
```

</td></tr>
</table>

Then open `.env` and set `GEMINI_API_KEY=<your-key>`.

> [!TIP]
> **You can skip this step** and still run the app: the roadmap and all 34
> cached lessons work with **no key**. Only *grading an assessment* and
> *"ask for help"* make live LLM calls and need a valid key + free-tier quota.

### 🔹 Step 5 — Build the RAG index *(optional)*
Needed **only** for the live "ask for help" pipeline; cached lessons don't need it.
```bash
python src/rag/build_index.py
```

### 🔹 Step 6 — Run it 🚀

#### ⚛️ Option A — Next.js + FastAPI (the main app)

The web app is two programs that run **together**: the **FastAPI backend**
(port 8000) and the **Next.js frontend** (port 3000). You'll use **two terminals**.

**One-time web setup** (installs the frontend deps + points it at the backend):
<table>
<tr><th>Windows (PowerShell)</th><th>macOS / Linux (bash)</th></tr>
<tr><td>

```powershell
cd web
npm install
"NEXT_PUBLIC_API_URL=http://localhost:8000" | Out-File -Encoding utf8 .env.local
cd ..
```

</td><td>

```bash
cd web
npm install
echo "NEXT_PUBLIC_API_URL=http://localhost:8000" > .env.local
cd ..
```

</td></tr>
</table>

**Terminal 1 — backend (from the project root, venv active):**
```bash
python -m uvicorn api.main:app --reload --port 8000
```
Interactive API docs at **http://localhost:8000/docs**.

**Terminal 2 — frontend:**
```bash
cd web
npm run dev
```

Open **http://localhost:3000** → **Get Started** → onboard → roadmap → lesson →
assessment.

> [!IMPORTANT]
> Both servers must be running at once. Keep the frontend on port **3000** —
> that's the origin the backend's CORS allows. (If Next.js says the port is busy
> and switches to 3001, either free 3000 or add the new origin to the CORS list
> in `api/main.py`.)

#### 🐍 Option B — Streamlit (legacy, all-in-one Python)

<details>
<summary>Prefer the original zero-Node UI? Expand.</summary>

```bash
streamlit run app.py
```
Opens at **http://localhost:8501**. No Node.js and no separate backend required —
Streamlit imports `platform_api` directly. Same features, same backend.
</details>

### 🔹 Step 7 — Run the tests *(optional)*
The **deterministic** suites need no API key and prove the core logic:
```bash
python tests/test_curriculum.py
python tests/test_path_engine.py
python tests/test_edge_states.py
python tests/test_scale_chapter2.py
python tests/test_persistence.py seed     # then:
python tests/test_persistence.py verify
```
The **LLM-backed** suites (`test_platform_api.py`, `test_pipeline.py`,
`test_assessor.py`, …) require a key and consume quota.

---

## 6. ⚙️ Environment variables

Only `GEMINI_API_KEY` is required for live features; the rest have sensible code
defaults (see `.env.example`). The one frontend var lives in `web/.env.local`.

| Variable | Where | Required? | Default | Purpose |
|---|---|:---:|---|---|
| `GEMINI_API_KEY` | `.env` | for live calls | — | Your Google AI Studio key. |
| `GEMINI_MODEL` | `.env` | no | `gemma-3-27b-it` | Generator/assessor model. Dev key uses `gemma-4-31b-it`. |
| `GEMINI_MAX_OUTPUT_TOKENS` | `.env` | no | `2048` | Output cap (Gemma needs headroom past its scratchpad). |
| `GEMINI_THINKING_BUDGET` | `.env` | no | unset | Only applies to `gemini-2.5-flash*` models. |
| `CRITIC_MODEL` | `.env` | no | `gemini-2.5-flash-lite` | Critic model. |
| `POLISHER_MODEL` | `.env` | no | `gemini-2.5-flash-lite` | Polisher model. |
| `ECOLEARN_PROGRESS_DB` | `.env` | no | `data/progress.db` | SQLite path (tests use a temp file). |
| `ECOLEARN_REVIEW_DAYS` | `.env` | no | `7` | Days before a mastered concept resurfaces for review. |
| `NEXT_PUBLIC_API_URL` | `web/.env.local` | for Next.js | `http://localhost:8000` | Where the Next.js app finds the FastAPI backend. |

---

## 7. ⚠️ Known limitations & trade-offs (honest)

This section is deliberately candid — real shortcomings, each with reasoning and
mitigation.

<details open>
<summary><b>⚛️ The Next.js frontend is functional but early</b></summary>

- **The full journey works** end-to-end: onboarding → roadmap → lesson → live
  "ask for help" → graded assessment → mastery reflected on the roadmap.
- **The student id lives in in-memory React Context**, so a hard browser refresh
  loses *who you are* (you'd re-onboard). Your *progress* is safe — it's keyed by
  `student_id` in the backend DB. Persisting the id (localStorage) is the next
  hardening step.
- **One chapter, hardcoded.** The web app targets `motion_straight_line`;
  `list_chapters` isn't exposed over HTTP yet, so there's no chapter picker.
- **Dev-only setup:** no auth, and CORS is pinned to `http://localhost:3000`.
- **Streamlit remains the complete reference UI**; the two frontends share the
  exact same backend and behaviour.
</details>

<details>
<summary><b>🖌️ Streamlit was the right tool, but fought us on polish</b></summary>

- **Default look is generic.** We added a full custom **design system**
  (`src/ui/theme.py`) that injects global CSS — pinned palette, Inter typeface,
  hidden Streamlit chrome, restyled buttons/sidebar/inputs, constrained
  max-width — to reach a premium, calm, Brilliant.org-style register. It depends
  on Streamlit's internal `data-testid` selectors, which can change between
  versions. *(Building the Next.js frontend was partly a response to these
  ceilings.)*
- **Theming pitfalls we hit (and fixed):** a global font override clobbered
  Streamlit's Material-Symbols **icon font** (icons rendered as literal text like
  `keyboard_double_arrow_left`); and on a dark-mode OS Streamlit defaulted to a
  dark base theme, making custom-coloured text invisible. Both fixed (icon-font
  exception + a pinned light base in `.streamlit/config.toml`).
- **Reactive-rerun model.** Streamlit re-runs the whole script on every
  interaction. Long work must never live in a click handler; we use
  state-flip-then-rerun and pin results in `session_state`.
</details>

<details>
<summary><b>📉 Free-tier LLM quota is the binding constraint</b></summary>

Every Gemini/Gemma model has its own ~20 requests/day free-tier bucket. Heavy
live grading/help **will** hit limits. Mitigations: lessons are pre-generated and
cached (no LLM at view time); judges **fail open** (a failed critic/polisher
degrades quality, not availability); the assessor/polisher have **multi-model
fallback chains**. `gemma-4-31b-it` also shows intermittent `500 INTERNAL`s. The
live "ask for help" call can take seconds-to-minutes for the same reason.
</details>

<details>
<summary><b>🧹 Reasoning models leak scratch work</b></summary>

Gemma dumps planning notes into responses by default. We fight this in three
layers (prompt instruction → regex sanitizer → LLM polisher); only the LLM
polisher is reliable. A polish failure can leave a lesson "raw" — handled by a UI
guard + an idempotent `repolish` repair pass.
</details>

<details>
<summary><b>📚 Content & scope</b></summary>

- **One subject (Physics), two chapters (17 concepts).** Adding a *chapter* is
  content-only (YAML + a factory run); adding a second *subject* needs a subject
  selector (not yet built).
- **Curriculum `order` is global, not per-chapter** — new chapters must continue
  the numbering or cross-chapter prerequisite validation rejects them.
- **The analogy generator has no model fallback yet** (assessor & polisher do).
- Only two interests (football, gaming) are authored.
</details>

---

<div align="center">
<br>
<sub>Built with a multi-agent pipeline, grounded in RAG, served from a clean API boundary — now with two frontends.</sub>
</div>
