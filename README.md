<div align="center">

# 🌱 EcoLearn

### A personalized AI physics tutor that teaches Class 11 Physics through what you love

*Pick **football** or **gaming** — every concept is taught by grounding its analogies in your interest.*

<br>

![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.58-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini%20%2F%20Gemma-4F46E5?style=for-the-badge&logo=googlegemini&logoColor=white)
![ChromaDB](https://img.shields.io/badge/ChromaDB-RAG-F59E0B?style=for-the-badge)
![SQLite](https://img.shields.io/badge/SQLite-progress-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

![Architecture](https://img.shields.io/badge/architecture-multi--agent%20%2B%20RAG-10B981?style=flat-square)
![Frontend](https://img.shields.io/badge/UI-multi--page%20Streamlit-1E293B?style=flat-square)
![Status](https://img.shields.io/badge/status-Phases%201–7%20complete-4F46E5?style=flat-square)

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
curriculum spine  →  learning-path engine  →  service API  →  multi-page UI
                        (lessons pre-generated offline, served instantly)
```

> [!IMPORTANT]
> **On the name:** "EcoLearn" is a holdover from an earlier
> sustainability-education concept. The codebase, curriculum, and content are
> entirely a **physics tutor** — the name was kept only to preserve git history.

---

## 2. 🧰 Tech stack — everything used, and why

| Layer | Technology | Why it's here |
|---|---|---|
| 🐍 Language / runtime | **Python 3.10** | Project baseline; fully type-annotated. |
| 🖥️ Web UI | **Streamlit 1.58** (multi-page) | Fastest way to ship a data app in pure Python. *(trade-offs in [§7](#7--known-limitations--trade-offs-honest))* |
| 🔌 LLM SDK | **`google-genai`** | Current Google GenAI SDK (the older `google-generativeai` is deprecated). |
| ✍️ Generation model | **Gemma `gemma-4-31b-it`** | Creative analogy generation; separate free-tier quota from Gemini Flash. |
| ⚖️ Critic / Polisher | **Gemini `gemini-2.5-flash-lite`** | Cheap, fast, strict-JSON judgement & markdown cleanup. |
| 📝 Assessor (grading) | **Gemma `gemma-4-31b-it`** *(+ fallback chain)* | Generates & grades the self-check question. |
| 🧠 Embeddings (RAG) | **`all-MiniLM-L6-v2`** (ONNX, local) | Bundled in ChromaDB — **no API, no key, no quota**. |
| 🗂️ Vector store | **ChromaDB** | Local RAG index over curriculum + interest corpora. |
| 🧾 Curriculum schema | **Pydantic** | Parse-don't-validate: YAML → typed objects at load. |
| 🗒️ Curriculum authoring | **PyYAML** | Non-programmer-friendly source of truth. |
| 💾 Progress store | **SQLite** (stdlib) | Durable per-student mastery + profiles; zero-setup. |
| 🔐 Config / secrets | **`python-dotenv`** | Loads `GEMINI_API_KEY` etc. from `.env`. |
| 🎛️ Prompts | **plain `.txt` files** | Tunable without code changes, reviews, or rebuilds. |

---

## 3. 🏗️ Architecture

```
  ┌─────────────────────────────────────────────┐
  │  Multi-page Streamlit UI                      │
  │  app.py · pages/ · src/ui design system       │
  └───────────────────────┬─────────────────────┘
                          │  calls ONLY
                          ▼
  ┌─────────────────────────────────────────────┐
  │  src/platform_api.py   ── the service boundary │
  └───────────────────────┬─────────────────────┘
                          │ orchestrates
        ┌─────────────┬───┴────┬─────────────┬──────────────┐
        ▼             ▼        ▼             ▼              ▼
   path engine   progress   lesson      live pipeline   curriculum
   (what next)    store     service   (gen→critic→      (YAML →
                 (SQLite)  (cached)    retry→polish)    typed objs)
```

**Two content paths, by design:**

- ⚡ **Cached lessons** — pre-generated offline, vetted once by the critic, served
  **instantly with no LLM call**. This delivers the stable curriculum.
- 🔴 **Live pipeline** — used **only** for *"I'm stuck — ask for help"* and for
  grading an assessment on submit. The only expensive/online calls in the app.

### 🚪 The service boundary — `src/platform_api.py`

The entire UI imports **exactly one** module for data: `platform_api`. It never
reaches into the engine, store, or pipeline directly, and every return value is
**plain JSON-serializable data**. That single rule is what makes a future
Next.js/React frontend a pure presentation swap. The six functions:

| Function | Purpose |
|---|---|
| `create_or_load_student(name, interest, level)` | Idempotent; `student_id` is a slug of the name. |
| `list_chapters()` | For the chapter picker. |
| `get_roadmap(student_id, chapter_id)` | Each concept tagged `mastered` / `available` / `locked` + prereqs. |
| `get_next_lesson(student_id, chapter_id, concept_id=None)` | What to teach next (or re-serve a concept). |
| `submit_assessment(student_id, concept_id, answer)` | Grades the answer against the lesson's check question. |
| `ask_help(student_id, concept_id, question)` | Live, grounded tutor answer (the only expensive call). |

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
🎨 Presentation
├─ app.py                         Onboarding / landing (multi-page entry)
├─ pages/1_Roadmap.py             Visual roadmap (status-coloured concepts)
├─ pages/2_Lesson.py              Lesson + persistent "ask for help" box
├─ pages/3_Assessment.py          Self-check question → grade → next-step choice
├─ ui_common.py                   Session guards + UI constants (no domain imports)
├─ src/ui/theme.py                Design system: palette, tokens, inject_global_css()
├─ src/ui/components.py           Reusable themed components (cards, nodes, badges)
└─ .streamlit/config.toml         Pinned LIGHT base theme + palette

🧩 Domain
├─ src/platform_api.py            THE service boundary (6 functions)
├─ src/curriculum/                Pydantic schema + YAML loader (teaching order, validation)
├─ src/path/engine.py             next_concept, get_roadmap, list_chapters
├─ src/progress/store.py          SQLite progress + students
├─ src/content/                   lesson schema · read service · offline factory
├─ src/agents/                    generator · critic · assessor · polisher (+ fallbacks)
├─ src/pipeline.py                explain_with_review: RAG→gen→critic→retry
└─ src/rag/                       ingest · build_index · retrieve (ChromaDB)

📦 Data & content
├─ data/curriculum/physics.yaml   Curriculum source of truth (2 chapters · 17 concepts)
├─ data/lessons/*.json            34 pre-generated, polished lessons (committed)
└─ prompts/*.txt                  System prompts (generator / critic / assessor)

📚 Misc
├─ legacy_chat_app.py             The original single-page chatbot, preserved
├─ tests/                         Deterministic + LLM-backed suites
└─ LOG.md                         Dated dev log (Changed / Why / Learned)
```

> [!NOTE]
> Not in the repo (created locally): `venv/`, `.env`, `chroma_db/`
> (rebuildable), `data/progress.db` (runtime state). The 34 cached lessons
> **are** committed, so the core experience works on first run.

---

## 5. ▶️ Running it yourself (step by step)

> Works on **Windows**, **macOS**, and **Linux**. Commands shown for both
> PowerShell (Windows) and bash (macOS/Linux).

### 🔹 Step 0 — Prerequisites
- **Python 3.10+** on your PATH (`python --version`)
- **git**
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

### 🔹 Step 3 — Install dependencies
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

### 🔹 Step 6 — Run the app 🚀
```bash
streamlit run app.py
```
Streamlit prints a local URL (default **http://localhost:8501**). Open it,
enter a name, pick an interest, and you land on your roadmap.

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
defaults (see `.env.example`).

| Variable | Required? | Default | Purpose |
|---|:---:|---|---|
| `GEMINI_API_KEY` | for live calls | — | Your Google AI Studio key. |
| `GEMINI_MODEL` | no | `gemma-3-27b-it` | Generator/assessor model. Dev key uses `gemma-4-31b-it`. |
| `GEMINI_MAX_OUTPUT_TOKENS` | no | `2048` | Output cap (Gemma needs headroom past its scratchpad). |
| `GEMINI_THINKING_BUDGET` | no | unset | Only applies to `gemini-2.5-flash*` models. |
| `CRITIC_MODEL` | no | `gemini-2.5-flash-lite` | Critic model. |
| `POLISHER_MODEL` | no | `gemini-2.5-flash-lite` | Polisher model. |
| `ECOLEARN_PROGRESS_DB` | no | `data/progress.db` | SQLite path (tests use a temp file). |
| `ECOLEARN_REVIEW_DAYS` | no | `7` | Days before a mastered concept resurfaces for review. |

---

## 7. ⚠️ Known limitations & trade-offs (honest)

This section is deliberately candid — real shortcomings, each with reasoning and
mitigation.

<details open>
<summary><b>🖌️ Streamlit was the right tool, but fought us on polish</b></summary>

- **Default look is generic.** We added a full custom **design system**
  (`src/ui/theme.py`) that injects global CSS — pinned palette, Inter typeface,
  hidden Streamlit chrome, restyled buttons/sidebar/inputs, constrained
  max-width — to reach a premium, calm, Brilliant.org-style register. It's a
  workaround, not native support: it depends on Streamlit's internal
  `data-testid` selectors, which can change between versions.
- **Theming pitfalls we hit (and fixed):** a global font override clobbered
  Streamlit's Material-Symbols **icon font** (icons rendered as literal text like
  `keyboard_double_arrow_left`); and on a dark-mode OS Streamlit defaulted to a
  dark base theme, making custom-coloured text invisible. Both fixed (icon-font
  exception + a pinned light base in `.streamlit/config.toml`).
- **Reactive-rerun model.** Streamlit re-runs the whole script on every
  interaction. Long work must never live in a click handler; we use
  state-flip-then-rerun and pin results in `session_state`. State is per-session
  and resets on a hard browser reload.
- **Not a production web framework.** No real auth, client-side routing, or
  component encapsulation. The `platform_api` boundary exists precisely so the UI
  can later be swapped for Next.js with zero backend changes.
</details>

<details>
<summary><b>📉 Free-tier LLM quota is the binding constraint</b></summary>

Every Gemini/Gemma model has its own ~20 requests/day free-tier bucket. Heavy
live grading/help **will** hit limits. Mitigations: lessons are pre-generated and
cached (no LLM at view time); judges **fail open** (a failed critic/polisher
degrades quality, not availability); the assessor/polisher have **multi-model
fallback chains**. `gemma-4-31b-it` also shows intermittent `500 INTERNAL`s.
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

## 8. 🧭 Engineering principles (the "why")

- **One source of truth, two representations** — YAML for authoring, Pydantic for
  runtime; the loader is the only boundary that reads YAML.
- **The engine invents no pedagogy** — ordering/prereqs from the curriculum,
  mastery from the store; the engine only joins them.
- **Plain-data returns at the boundary** — the precondition for a non-Python
  frontend.
- **Fail open on judges, fail loud on inputs** — a failed critic shouldn't blank
  a lesson; a missing key or unknown student must surface immediately.
- **Pre-generate offline, serve cached** — pay the multi-agent cost once; quota
  exhaustion delays *authoring*, never the *product*.
- **Prompts live in `.txt`, not code** — tunable without a review or rebuild.

---


<div align="center">
<br>
<sub>Built with a multi-agent pipeline, grounded in RAG, served from a clean API boundary.</sub>
</div>
