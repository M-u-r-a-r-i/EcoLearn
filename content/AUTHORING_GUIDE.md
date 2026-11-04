# EcoLearn lesson authoring guide

> **Read this whole file before writing a single lesson.** Every authoring session starts from
> zero; this guide plus the approved gold examples are what keep 7,470 lessons consistent.
> There is **no automatic physics check** on what you write — the validator only checks format.
> If the physics is wrong, a student learns it wrong. Section 6 is the most important part.

---

## 1. What you are writing

EcoLearn teaches CBSE and ISC Class 11–12 Physics to Indian students aged 15–18, through the
student's own interest. Every concept is written **three times** (three formats) **for each of
10 interests**.

- Concepts: `data/curriculum/physics.yaml` (id, name, prerequisites, `learning_objective`,
  `bloom_target`, `boards`). Human-readable view: `content/CURRICULUM.md`.
- Interests: `data/interests.yaml` (`label`, `description`, `strong_domains`).
- Gold examples to imitate: `data/lessons/11/laws_of_motion/second_law/` and
  `data/lessons/12/current_electricity/ohms_law/` (cricket and music, all three formats).

**The lesson must achieve the concept's `learning_objective`.** Read it first. If the objective
says "calculate", the lesson must show a calculation; if it says "explain why", it must explain why.

**Every lesson opens with a story and includes pictures** (user decision, 2026-09-21): a short
narrative that sparks curiosity before any explaining starts (§4a), and at least one image — the
chapter's scene illustration, a graph or diagram, and a famous historical image where one fits (§7a).

## 2. A batch, step by step

One batch = **one chapter × one interest** = every concept in the chapter × 3 formats (~20–33 files).

1. Read this guide, then the gold examples in full.
2. Read the chapter's concepts in `physics.yaml`, and the interest's entry in `interests.yaml`.
3. Check the fit: is the chapter's `domain` in the interest's `strong_domains`? If yes, analogies
   should come easily. If not, see §5.3 — do not force it.
4. Check the images you'll need (§7a): the chapter × interest scene, and the concept's graphs
   and diagrams. Create any that don't exist yet, then run
   `venv\Scripts\python.exe scripts\render_graphs.py` for new graph specs.
5. Write the files, one concept at a time, all three formats before moving on.
6. Run the self-check (§9) on each file **before** saving it.
7. Run the validator and fix every error:
   `venv\Scripts\python.exe scripts\validate_lessons.py --chapter <chapter_id> --interest <interest_id>`
8. Touch nothing outside your batch's folders (and `data/media/` for the images you add). Never edit `physics.yaml` or `interests.yaml` —
   if a concept looks wrong, say so in your report instead.

## 3. The file

**Location:** `data/lessons/{grade}/{chapter_id}/{concept_id}/{interest}__{format}.md`
e.g. `data/lessons/12/current_electricity/ohms_law/music__explain.md`.

**Format:** a YAML header between `---` lines, then Markdown.

```markdown
---
concept_id: ohms_law
interest: music
format: explain
title: Why your headphones sound quieter on a phone
check:
  question: |-
    The question text. Maths is fine: $V = IR$.
  options:
    A: |-
      First option
    B: |-
      Second option
    C: |-
      Third option
    D: |-
      Fourth option
  answer: C
  explanation: |-
    Why C is right, in one or two sentences.
  misconceptions:
    A: |-
      The specific wrong idea that makes a student pick A.
    B: |-
      ...
    D: |-
      ...
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A music desk with a phone and studio headphones](scenes/music/current_electricity.svg "What the student should notice in this picture.")

...
```

**Every text field in the header uses `|-` followed by the text on the next line, indented.**
Never put text in `"double quotes"`: in YAML double quotes a backslash is an escape, so
`"\frac{a}{b}"` silently becomes a form-feed character and broken maths. The validator catches
this, but it's easier not to do it.

- `title`: short, specific, interest-flavoured, no clickbait, no colon-subtitles. Plain text (no maths).
- `author`: `claude-code/opus-5` (or the model you are).
- `written`: today's date.
- **No `# ` heading in the body** — the title comes from the header.

## 4. The three formats

Section headings must be **exactly** these, in this order (the validator enforces it).
Target 500–800 words of body including the story; the hard limits are 250–1100.
**All three formats open with `## The story`** (§4a).

### `explain` — a story first, then the physics

| Section | What goes in it |
|---|---|
| `## The story` | The curiosity hook (§4a), with the scene illustration. Ends on the question the physics answers. |
| `## The physics` | The concept stated properly — definitions, the law/equation, symbols defined, units, conditions of validity. Map it back to the scene explicitly ("the bat's push is $F$…"). |
| `## Worked example` | One problem set in the interest (§7). |
| `## Where the picture breaks` | Where the scene or analogy stops matching the physics, and what the idealisation leaves out. Honest and specific — this is what stops the analogy from teaching a misconception. |
| `## Key takeaway` | 2–4 sentences. The one idea to remember, in plain words, plus the equation if there is one. |

### `challenge` — a puzzle first, the concept as the answer

| Section | What goes in it |
|---|---|
| `## The story` | The curiosity hook (§4a): characters run into the puzzle. |
| `## The challenge` | A puzzle set in the interest with a definite answer the student can reason towards. State the numbers needed. |
| `## Think first` | Invite a guess and name the tempting wrong answers ("Twice as hard? Four times?") without revealing which is right. Short. |
| `## The reveal` | The answer, reasoned step by step from the physics. Say why the tempting wrong answers fail. |
| `## The physics` | The concept stated properly, generalised beyond the puzzle. |
| `## Worked example` | *Optional.* A second problem if the puzzle didn't already show the full method. |
| `## Key takeaway` | As above. |

### `misconception` — a wrong intuition, taken apart

| Section | What goes in it |
|---|---|
| `## The story` | The curiosity hook (§4a): a character voices the wrong intuition, or runs into it. |
| `## The common belief` | A real, common student misconception about this concept, voiced through the interest. Pick one documented in physics-education practice, not a strawman. |
| `## Why it feels right` | Treat the belief with respect: the everyday experience that makes it convincing. Often part of it *is* true — say which part. |
| `## What actually happens` | The correct picture, shown in the same scene, with the decisive reasoning or evidence. |
| `## The physics` | The concept stated properly, including exactly where the misconception goes wrong. |
| `## Worked example` | *Optional.* A problem where the misconception would give a wrong number. |
| `## Key takeaway` | As above. |

The three formats should feel different, not like one lesson rearranged. Use different stories
from the interest for each format — different characters, different moments.

## 4a. The story — spark curiosity first

The student should *want* the answer before they get it. The story is not the explanation; it is
the reason to care about the explanation.

- **80–180 words.** A real moment in the interest's world, told as a scene: a named character
  (Indian names, varied across lessons), a place, something happening.
- **Tension or surprise:** something unexpected, an argument, a bet, a prediction about to be
  tested, a thing that "shouldn't" work but does.
- **End on an open question** — stated or implied — that the physics will answer. Do **not**
  answer it in the story, and don't put equations in it (a number or two is fine).
- **Put the chapter's scene illustration at the top of the story** (§7a).
- Everything in the story must still be physically possible and true to the interest (§5).
- Good openings: *"Ishaan saved for eight months to buy studio headphones…"*, *"It's 1 a.m., the
  concert is over, and Irfan has one job left…"*. Avoid: "Imagine you are…", "Have you ever
  wondered…", or a textbook sentence dressed as a story.

## 5. Using the interest

### 5.1 Fidelity
The scene must be something that really happens in that interest, described the way a fan would
recognise it. A student who loves cricket will notice a wrong field position.

### 5.2 No invented facts
- **Never state a statistic about a real person, team, product or event** (a named bowler's top
  speed, a specific stadium's floodlight wattage, a phone model's battery capacity). You cannot
  check it, and a wrong one destroys trust.
- Don't name real players, bands, brands or products at all. "A fast bowler", "a guitarist",
  "a phone charger" are enough.
- Use **illustrative, physically plausible numbers**, and say so the first time: "say the ball
  leaves at about $36\,\text{m/s}$". Plausible matters: a cricket ball is about $0.16\,\text{kg}$;
  bat–ball contact lasts about a millisecond; a phone battery is a few volts.
- General facts that are true and checkable are fine (a cricket pitch is 22 yards; sound travels
  at about $343\,\text{m/s}$ in air at room temperature).

### 5.3 When the fit is weak
If the chapter's domain isn't in the interest's `strong_domains`, **do not force an analogy.**
A forced analogy teaches wrong physics. Instead:
- use a **real device or situation** from the interest's world where the physics genuinely
  occurs (the light meter umpires use, the amplifier a band plugs into), and teach the physics
  directly through it; or
- keep the interest as a light frame and say plainly, in `## Where the picture breaks`, that the
  connection is loose.
The gold `ohms_law × cricket` lessons show how.

### 5.4 Audience
Indian students, 15–18. Indian context is welcome (₹, km/h, local settings). Keep it inclusive —
no stereotypes, nothing a school would object to. Warm, direct, second person ("you"), short
paragraphs. No emojis in the body. Bold a key term the first time it's defined, sparingly.

## 6. Physics correctness — the rules that matter most

There is no critic. You are the check.

1. **Re-derive every number.** Work each calculation out step by step, then check it a second
   way (estimate the order of magnitude, or reverse the calculation). Arithmetic slips are the
   most likely error.
2. **Units on every quantity**, SI throughout, converted before substituting (mA → A, g → kg,
   km/h → m/s). Check the answer's units come out right.
3. **Dimensional sanity**: both sides of every equation have the same dimensions.
4. **Signs and directions**: choose a positive direction, state it, keep it.
5. **Conditions of validity**: state them ("for constant mass", "for an ohmic conductor at
   constant temperature", "ignoring air resistance"). Never present an approximation as exact.
6. **Match NCERT notation and definitions** (e.g. $\vec{F}_\text{net} = \dfrac{d\vec{p}}{dt}$,
   $V = IR$, $g = 9.8\,\text{m/s}^2$ unless the problem says otherwise). If NCERT defines a term,
   use that definition.
7. **Stay in syllabus scope.** Don't use calculus beyond what the concept's prerequisites give,
   and don't depend on a later concept. If a later idea is unavoidable, name it as "you'll meet
   this later" — don't teach it half-way.
8. **Limiting-case check**: ask "what happens if this quantity is zero, or very large?" — does
   the result behave sensibly?
9. **Misconceptions must be real**: the wrong options and the `misconception` format must use
   misconceptions students actually hold — not invented ones.

## 7. Maths and notation

- Inline maths `$…$`, displayed equations `$$…$$` on their own line. Rendered by KaTeX.
- Units upright with a thin space: `$36\,\text{m/s}$`, `$0.16\,\text{kg}$`, `$300\,\Omega$`,
  `$5.0\,\text{mA}$`.
- Vectors `\vec{F}`; subscripts in text `\text{net}`; fractions `\dfrac` in inline maths when tall.
- **Never use `$` for money** — write ₹ or "rupees". A stray `$` breaks the maths (validator error).
- Significant figures: match the data (usually 2–3). Don't write $11{,}200.00\,\text{N}$.

**Worked examples** follow this shape: what's given (with units) → what's asked → the relation
used and why → substitution → the answer with units → a one-line sanity check.

**Keep the numbers few, round and picturable** (user decision, 2026-09-23 — the first worked
examples were "hard to visualize"):

- **Two or three given quantities, not five.** If a fourth is needed to make the story work, state
  it in words rather than adding another symbol to track.
- **Round numbers that divide cleanly.** $10\,\text{m/s}$, $20\,\text{m}$, $0.5\,\text{kg}$ —
  not $17.3\,\text{m/s}$ and $0.436\,\text{kg}$. The student should follow the *method*, not chase
  arithmetic. Realistic-but-ugly values belong in the check question, if anywhere.
- **One quantity per step, and say what it means** before the next line of algebra: "so the ball
  is climbing at half its starting speed — half its upward motion is already gone."
- **Answers a student can picture:** "about the height of a two-storey building", "roughly a
  fast walk". Attach a mental image to at least the final answer.
- **No chains of intermediate values.** If the working needs more than about four numbered steps,
  the example is too big: cut the scenario down, don't shrink the explanation.
- The sanity check stays, but as one plain sentence ("a fielder can't outrun a car, so tens of
  m/s is the right size"), not a second calculation.

*These rules apply to lessons written from 2026-09-23 on. Earlier lessons are denser; they are
being left alone for now, and the lesson page collapses the worked example behind a click.*

## 7a. Images

Every lesson needs **at least one image** — and should have **as many as the concept needs**.
There is no upper limit (user decision, 2026-09-21). Two or three is typical; add more whenever a
picture would teach something the text can't, for example:

- **processes in steps** — a separate diagram for each stage (charging a capacitor, the phases of
  an oscillation, the strokes of a heat engine);
- **cases that differ** — one ray diagram per object position for a mirror or lens; each of the
  isothermal / adiabatic / isobaric / isochoric curves;
- **every important relationship** — a graph for each (V–I, x–t / v–t, binding energy per nucleon);
- **structure you can't describe in words** — field lines, circuits, apparatus, band diagrams;
- **the story itself**, when the chapter's shared scene doesn't show what the story is about (see
  "Story-specific scenes" below).

Every image must still earn its place: if a student wouldn't miss it, leave it out.

Images live under `data/media/` and are referenced by a path relative to it, with alt text **and**
a caption:

```markdown
![A V–I graph: a straight line for a resistor and a curve for a lamp](figures/ohms_law/vi-ohmic-vs-lamp.svg "An ohmic resistor gives a straight line; a lamp's line curves as it heats.")
```

- **Alt text** describes what the image shows, for students using screen readers.
- **Caption** says what to notice — it teaches, it doesn't just label.
- Place each image where the text refers to it.

### The three kinds

| Kind | Where | One per | How it's made |
|---|---|---|---|
| **Scene illustration** | `scenes/{interest}/{chapter_id}.svg` | chapter × interest (shared by the chapter's lessons for that interest) | A flat vector SVG you draw: the interest's setting for that chapter. Goes at the top of `## The story`. |
| **Graph** | `figures/{concept_id}/{name}.graph.yaml` → `.svg` | as the concept needs | A data spec rendered by `scripts/render_graphs.py`. Never hand-draw a graph — the plotted numbers must be the real numbers. |
| **Diagram** | `figures/{concept_id}/{name}.svg` | as the concept needs | An SVG you draw: force diagrams, circuits, ray diagrams, field lines. Interest-neutral where possible, so every interest can reuse it. |
| **Famous image** | `famous/{name}.jpg` | where a genuinely famous one exists | Historical portrait, document or photograph. **Only from `famous/manifest.yaml`** — see below. |

### Story-specific scenes

The shared scene (`scenes/{interest}/{chapter_id}.svg`) is the default. When a story needs a
picture of something that scene doesn't show — a specific moment, device or comparison — draw an
extra one named `scenes/{interest}/{chapter_id}--{short-name}.svg` (e.g.
`scenes/music/current_electricity--headphones.svg`). Diagrams that explain physics stay
interest-neutral in `figures/{concept_id}/` so all ten interests can reuse them.
**Neutral means the numbers too:** don't print a batch-specific mass, speed or story value (e.g.
"0.16 kg ball", "24 m/s") in a shared figure's title, legend or labels. Label the shape of the
physics instead ("K ∝ v²", "doubling v quadruples K", "slope = power"), and put the worked numbers
in the lesson text. Otherwise the next interest has to redraw the figure (this happened with
Work, Energy and Power in 2026-09).

### Rules for drawn images (SVG)

- `viewBox` on the root (e.g. `0 0 800 450` for scenes, `0 0 640 400` for diagrams); a white or
  solid background rect so it reads in dark mode; `font-family="Segoe UI, Arial, sans-serif"`.
- **Physics must be exact.** Arrow directions, relative lengths, sign conventions and labels must
  match the physics. Conventions: **forces red** (`#dc2626`), **velocity blue** (`#2563eb`),
  **acceleration green** (`#16a34a`), currents blue with arrowheads. Circuit symbols follow NCERT
  (zigzag resistor, long plate = + terminal).
- **Never** `<script>`, `<foreignObject>`, `on…` attributes, or links to anything outside the file
  (the validator rejects them). Keep files under 600 KB — hand SVGs are usually under 10 KB.
- No real people's likenesses, no logos, no copyrighted characters, no team kits of real teams.
- Scenes are simple flat illustrations — clarity over detail. Labels only where they teach.
- Look at what you drew before using it. The browser pane often can't open files in folders
  created during the session, so render a PNG with headless Edge and read that:
  `& "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --headless=new --disable-gpu --hide-scrollbars --window-size=820,540 --screenshot="<scratchpad>\shot.png" "file:///D:/Projects/EcoLearn/data/media/<path>.svg"`
- For a chapter's **second and later interests**, reuse the chapter's existing `figures/` — only
  the scene is per interest. Check `data/media/figures/{concept_id}/` before drawing anything.

### Famous images — licensing

Famous images come **only** from Wikimedia Commons, **public domain or CC0 / CC BY / CC BY-SA**,
with an entry in `data/media/famous/manifest.yaml` (file, title, source page, licence, credit).
Adding a new one means checking its licence on its Commons page and **asking the user before
downloading** — never fetch images on your own. Download the ~960px web version, not the original.
The caption must state the licence, e.g. *"Public domain, via Wikimedia Commons."* Use famous
images for real history: Newton's *Principia*, a portrait of Ohm, Faraday's notebook, Rutherford's
apparatus, the first photograph of an atom's spectrum. Never invent history to fit an image.

## 8. The check question

A single multiple-choice question with four options, graded automatically — so it must be
unambiguous.

- Tests the **learning objective**, not trivia about the interest. Set it in the interest.
- **Exactly one** correct option. No "all/none of the above", no "both A and B".
- **Each wrong option is a real misconception** or a typical error (a unit slip, an inverted
  ratio, squaring when it's linear), and `misconceptions` names it precisely — this is what lets
  EcoLearn tell a student *why* they were wrong. "Wrong answer" is not a misconception.
- A "right answer for the wrong reason" distractor is excellent when it fits.
- Options similar in length and style; numbers in a consistent format.
- **Vary the correct letter** across lessons — roughly even A/B/C/D over a batch.
- `explanation`: why the right answer is right, in one or two sentences.

## 9. Self-check before saving each file

- [ ] Does the story make a student want the answer — and not give it away?
- [ ] At least one image, each with alt text and a teaching caption? Scene at the top of the story?
- [ ] Is there any step, case or relationship that a picture would make clearer? If so, add it.
- [ ] Do diagram arrows and labels match the physics exactly? Graphs made from specs, not drawn?
- [ ] Does the lesson achieve the concept's `learning_objective`?
- [ ] Every number re-derived and checked a second way? Units right everywhere?
- [ ] Conditions of validity stated? Nothing approximate presented as exact?
- [ ] Is the scene true to the interest? No invented statistics, no real names?
- [ ] Does `Where the picture breaks` (explain) name the analogy's real limits?
- [ ] Is the MCQ answer definitely correct, and is every distractor definitely wrong?
- [ ] Headings exact and in order (`## The story` first)? All header text in `|-` blocks? No `$` for money?
- [ ] Would a strong Class 11/12 student find it clear, and a teacher find nothing wrong?
