<!--
  The standard brief for a lesson-writing sub-session. `scripts/batch_status.py --brief`
  fills in every {PLACEHOLDER} for the next batch and prints the result — pass that text,
  unchanged, as the sub-session's prompt. Edit this template to change every future batch.
-->
You are writing a batch of lessons for EcoLearn, a CBSE/ISC Class 11–12 physics tutor for Indian students (15–18) that teaches every concept through the student's own interest. Project: D:\Projects\EcoLearn (Windows; use `venv\Scripts\python.exe`). Work efficiently — the user is on a limited plan — but never trade away physics correctness.

## Your batch
Chapter **`{CHAPTER_ID}`** ({CHAPTER_NAME}, Class {GRADE}) × interest **`{INTEREST}`** ({INTEREST_LABEL}) × format(s) **{FORMATS}** = **{LESSON_COUNT} lessons**.
Concepts in teaching order: {CONCEPTS}.
Files: `data/lessons/{GRADE}/{CHAPTER_ID}/{concept_id}/{INTEREST}__{format}.md`.

**Resumable:** before writing each file, check whether it exists; if it does, skip it. Write in the order above so an interruption leaves complete, valid work behind.

## Read first, in full
1. `content/AUTHORING_GUIDE.md` — the complete rules. Follow them exactly (story first, images, no invented facts, physics correctness §6, MCQ design §8, self-check §9).
2. Your models for depth, structure and image use: {MODEL_LESSONS}. Match their standard, but write **entirely new {INTEREST_LABEL} stories, characters, scenarios and numbers** — never paraphrase another interest's lesson.
3. The chapter's concept entries in `data/curriculum/physics.yaml` (search `id: {CHAPTER_ID}`); every lesson must achieve its concept's `learning_objective`.
4. The `{INTEREST}` entry in `data/interests.yaml`. This chapter's domain is `{DOMAIN}`; {FIT_NOTE}

## Facts you may use
{FACTS}
Use only general, checkable facts like these. **Never** state statistics about real people, teams, tournaments or products, and never use real names. Mark other numbers as illustrative.

## Images (guide §7a)
- Figures already drawn for this chapter (interest-neutral — **reuse them wherever they fit**): {EXISTING_FIGURES}
- If a concept has no suitable figure yet, draw it under `data/media/figures/{concept_id}/`, interest-neutral so later interests reuse it; graphs only as `.graph.yaml` specs rendered with `venv\Scripts\python.exe scripts\render_graphs.py <spec>`.
- Scene: {SCENE_NOTE} Put it at the top of every lesson's `## The story`.
- Check every new drawing with headless Edge (command in guide §7a) and fix overlaps.
- Famous images available (public domain, in `data/media/famous/manifest.yaml`): {FAMOUS}. Captions must contain "Public domain, via Wikimedia Commons." **Never download anything or edit the manifest** — name any famous image you'd want in your report instead.

## Process
Plan all stories first (varied named Indian characters and moments). Write one concept at a time, running the guide's self-check on each. Spread MCQ answers evenly across A/B/C/D. `author: claude-code/opus-5`, `written: {TODAY}`. Then validate and fix until clean:
`venv\Scripts\python.exe scripts\validate_lessons.py --chapter {CHAPTER_ID} --interest {INTEREST}`
Only create files under `data/lessons/{GRADE}/{CHAPTER_ID}/` and `data/media/`; never modify existing files. No git.

## Final report (under 300 words)
Files created (lesson count + new image paths), the final validator line, the answer-letter distribution, which existing figures you reused, any physics point you were unsure of, and any weak fit and how you handled it.
