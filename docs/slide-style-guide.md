# EcoLearn pitch deck: slide style guide

For whoever builds or continues the finals deck (HackAStone, 2026-10-29, 15 minutes). It translates the app's house style
(`.claude/skills/ecolearn-style/SKILL.md`, taken from the approved Replit design) into PowerPoint / Google Slides terms, so the
deck and the live demo look like one product. Written 2026-10-27.

**The feeling in one line:** calm, warm, a little playful. A well-kept field-notes notebook a sports club would pin up:
paper-cream backgrounds, deep forest green, gold and peach accents, soft shadows, generous rounded corners, small uppercase
labels over big tight headings. Never neon, never glassy, never dense grey "enterprise" slides.

---

## 1. Slide size and grid

- **16:9**, 13.33 x 7.5 in (PowerPoint "Widescreen").
- **Margins:** 0.6 in left and right, 0.5 in top, 0.5 in bottom. Keep everything inside them.
- **Grid:** 12 columns. Text blocks usually span 6 to 7 columns; a screenshot or chart the other 5 to 6.
- **One idea per slide.** If a slide needs two headings, it is two slides.

## 2. Colours

Use the **light theme for content slides** (it projects well in a bright hall) and the **dark theme for the title, section
dividers and the closing slide** (the app's own default is dark, so these feel like the product).

| Role | Light slides | Dark slides | Use |
|---|---|---|---|
| Background | `#F4F3ED` | `#17231F` | the slide itself |
| Card / surface | `#FFFEF9` | `#202E29` | cards, panels, screenshot frames |
| Soft fill | `#EBEAE1` | `#293A33` | chips, tracks, quiet boxes |
| Text (ink) | `#202A27` | `#F1F2E7` | headings and body |
| Muted text | `#747C73` | `#A2AEA4` | captions, sources, footers |
| Lines / borders | `#DEDFD4` | `#394940` | card borders, dividers, table rules |
| **Brand green** | `#26745D` | `#79C29B` | eyebrows, key numbers, the "us" bar in charts, links |
| Brand green, darker | `#1B5B48` | `#A5D7B6` | pressed or emphasised brand |
| Lime accent | `#D4EF7A` | same | small highlights, a single underline |
| Orange accent | `#E99B61` | same | a second series, warm callouts |
| Gold accent | `#E6BD4D` | same | "mastered", awards, the one thing to remember |
| Danger / wrong | `#BD594E` | `#F18579` | wrong answers, risks, "what we don't claim" |

**Pastel tiles** (icon backgrounds, small banners), each with its dark twin:
sage `#E3ECDD` / `#2A4033`, sand `#F5EDDA` / `#403B2A`, peach `#F5E6DC`, lavender `#EBE3F2`, sky `#D9EAF0`.

**The five interests** each have an accent. Use them only when a slide is about that interest (for example a row of five
lesson thumbnails):

| Interest | Chip colour | Accent on light slides | Accent on dark slides |
|---|---|---|---|
| Cricket 🏏 | `#EFB45B` | `#96691F` | `#E0AE62` |
| Football ⚽ | `#84BE89` | `#3F7A4C` | `#84C690` |
| Gaming 🎮 | `#BD9CE2` | `#7551A0` | `#BDA0E6` |
| Smartphones 📱 | `#78B9C7` | `#3D7C89` | `#7FC0CD` |
| Motorsport 🏎️ | `#EB9170` | `#B65A3D` | `#EC9575` |

**Rules:**
- A selected or highlighted thing is **brand-tinted surface + brand border**, never a new colour.
- Right / wrong keep their meaning everywhere: green = right, `#BD594E` = wrong. Never use red for decoration.
- No other blues, purples or greys. If a colour isn't in these tables, don't use it.
- Text contrast: body text is always ink on surface or background. Muted text only for captions, never for a key point.

## 3. Fonts

| Role | Font | Fallback (if missing on the presenting laptop) |
|---|---|---|
| Headings, big numbers | **Trebuchet MS** (bold, tight) | Segoe UI Semibold |
| Body, captions | **Avenir Next** | Segoe UI, then Calibri |

Avenir Next is not installed on most Windows laptops. **Embed fonts** (PowerPoint: File > Options > Save > "Embed fonts in
the file") or set Segoe UI as the body font from the start. Check on the laptop you will present from.

**Sizes on a 16:9 slide:**

| Element | Size | Weight / style |
|---|---|---|
| Eyebrow (small label above a heading) | 12 to 14 pt | bold, ALL CAPS, letter spacing +12%, brand green |
| Slide heading | 36 to 44 pt | Trebuchet bold, letter spacing about -4%, ink |
| Hero number ("22 of 25", "+12 points") | 72 to 110 pt | Trebuchet bold, brand green (or gold for the single headline result) |
| Body | 18 to 22 pt | regular, ink, line spacing 1.3 |
| Caption / source | 12 to 14 pt | regular, muted |

At most **about 30 words of body text per slide**. If you need more, it belongs in the speaker notes.

## 4. Shapes, cards and decoration

- **Cards:** rounded rectangles, corner radius about 10% (PowerPoint "Rounded Rectangle" with the adjustment handle pulled
  in a little), fill = surface, 1 pt border in the line colour, a very soft shadow (outer, 0 offset x, 6 pt down, 20 pt blur,
  8% black). Never a hard drop shadow.
- **Chips / pills:** fully rounded ends, soft fill, 12 to 14 pt text.
- **Buttons in mock-ups:** brand fill, white text, rounded, with a darker 4 pt "ledge" underneath (the app's pressable look).
- **Icon tiles:** a 0.6 in rounded square in a pastel, a simple line icon inside. Use one icon family only (the app uses
  **Lucide**: lucide.dev, free; same stroke width everywhere).
- **The motif:** a small `✳` (asterisk spark) in muted colour, used sparingly: a section corner, an empty state. A faint dotted
  grid or dashed orbit ring behind a hero image is fine at 10 to 15% opacity.
- **Screenshots of the app:** always inside a card with the 1 pt border and rounded corners, never floating raw. Take them from
  the demo data (logins in `AGENTS.md`) at 1280 px wide; crop to the part you talk about.

## 5. Charts

- Bars and lines in **brand green for EcoLearn / treatment**, **muted `#A2AEA4` (or soft fill) for the baseline / control**.
  A third series, if you must: orange `#E99B61`.
- No 3-D, no gradients, no gridlines heavier than the line colour. Label values on the bars; drop the y-axis if the labels are there.
- **Always show the uncertainty** for the pilot comparison: the 95% interval as a thin bar or bracket. If it crosses 0, the
  slide must say so.
- Rounded bar ends are fine (the app's progress bars are round).

## 6. Slide types

| Type | Layout |
|---|---|
| **Title** (dark) | Product name large, one-line promise under it ("Physics, through the thing you love"), team names small at the bottom, a faint orbit ring motif to the right |
| **Section divider** (dark) | Eyebrow (e.g. "THE AGENTS") + a 44 pt heading, nothing else |
| **Problem / insight** | Eyebrow + heading + one sentence; a single image or quote on the right |
| **Big number** | Eyebrow, the hero number, one line of what it means, source in muted text at the bottom |
| **Product screen** | Heading left (5 columns), screenshot card right (7 columns), one or two callouts with thin brand-green leader lines |
| **How it works / agents** | A left-to-right flow of 3 to 5 cards (writer, checker, rules, teacher approves...), arrows in muted colour, the human step highlighted in gold |
| **Comparison / evidence** | Two columns or a bar chart with the interval; a short "what we do NOT claim" line in danger colour at the bottom |
| **Responsible AI** | A 2 x 3 grid of small cards (no names to the AI, AI switch per student, nothing stored from the chat, teacher approves, two AIs check practice questions, data export and erase) |
| **Business** | One table or three cards (cost per student, price, margin) from `docs/unit-economics.html`; numbers in brand green |
| **Closing** (dark) | The one-line ask, the product name, a QR code or link in a white card |

## 7. Writing on slides

- **Voice:** plain, warm, specific. "A student who is often sure of a wrong answer gets a nudge to re-read" beats
  "AI-driven metacognitive intervention".
- **Headings say the point**, not the topic: "Every answer reveals a mix-up", not "Assessment".
- Sentence case everywhere, except the uppercase eyebrows.
- No exclamation marks in headings. Emoji only for the five interests.

## 8. Honesty rules (these protect the pitch; judges will check)

- **Never quote the demo dataset's numbers** (for example "58% to 77%"). They are invented test data.
- **Never say the lessons were "written and reviewed by people".** Say "prepared in advance, with AI help, and checked"
  (a validator and audits; a person has not read all 642).
- **The pilot comparison is a designed first look**, not proof (`docs/pilot-experiment.md`). Show the interval; if it includes
  0, say "no effect shown either way". If the pilot hasn't produced numbers yet, show the design, not results.
- **AI runs in exactly five places**, each with a non-AI fallback; graded checks never use AI. Don't imply more.
- Name what is not done yet if asked (`AGENTS.md` handoff lists it). Credibility scores higher than polish.

## 9. Suggested 15-minute structure (by the judging weights)

| Minutes | Slides | Weighs on |
|---|---|---|
| 0:00 to 1:30 | Title, the problem (students switch off when every concept is explained the same way) | Education significance 15% |
| 1:30 to 4:30 | The idea: same physics, a different door in (interests, mix-ups found by the starting check, personal stories) | Innovation 30% |
| 4:30 to 8:00 | **Live demo** (student: starting check, lesson, check, About me, practice; teacher: insights, coaching action approved) | Demo 10%, Technology readiness 20% |
| 8:00 to 10:00 | The agents and how each is kept safe (two AIs check each other, teacher approves, the AI switch) | Innovation 30%, Technology readiness |
| 10:00 to 11:30 | Evidence: the pre-registered comparison and the pilot plan | Education significance, "Research meets Practice" |
| 11:30 to 13:00 | Business: cost per student, who pays, how it scales | Commercial viability 15% |
| 13:00 to 15:00 | What's next, the ask, thanks | Presentation 10% |

**Have a recorded backup of the demo** on the laptop, in case the Wi-Fi or the live AI fails on stage.

## 10. Checklist before presenting

- [ ] Only the colours in section 2; no stray blues or greys.
- [ ] Every content slide: eyebrow + heading that says the point + at most about 30 words.
- [ ] Fonts embedded, or the Segoe UI fallback set; checked on the presenting laptop.
- [ ] Screenshots in bordered rounded cards, taken from the demo data.
- [ ] Charts: brand green vs muted, values labelled, intervals shown.
- [ ] No demo-dataset numbers, no "reviewed by people", no claimed effect without an interval.
- [ ] Dark title, divider and closing slides; light content slides.
- [ ] The recorded demo video is on the laptop and plays offline.
