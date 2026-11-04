# Finals deck (HackAStone, 2026-10-29)

The deck lives as a private Claude artifact (Slides type) on the user's account:
**"EcoLearn: learning that fits the learner"**, https://claude.ai/artifact/3God2ijuzU5px8kk1nyL5E (9 slides, speaker notes in each).
This folder is a backup copy of its source, taken 2026-10-28, so the deck can be rebuilt or edited from a new session.

- `deck.json` + `slides/*.html`: the deck's own files, in the Slides type's format (one `<section>` per slide, inline styles,
  the `<aside>` is the speaker notes). Images in the slides are `/_blob/<id>` assets stored inside that artifact.
- `diagrams/`: sources of the two diagram images (slides 5 and 6). Edit the SVG, render it to PNG with headless Edge
  (`msedge --headless=new --force-device-scale-factor=2 --window-size=1600,660 --screenshot=out.png file:///.../architecture.svg`;
  1600x720 for `ecosystem.svg`), then upload the PNG as an asset of the deck.
- The five lesson illustrations on the title slide are renders of `data/media/scenes/<interest>/laws_of_motion.svg`.

Slide order: title, learning today (self-learning), problem statement (the user's exact sentence), solution, how it works
(architecture diagram), agent system (ecosystem diagram), technology readiness (no internal counts, by the user's request),
commercial viability + USPs, thank you.

Placeholders still to fill: team names (slides 1 and 9), contact or link (slide 9).

Older decks (kept, not in use): "EcoLearn finals pitch" (21 slides) and "EcoLearn: physics in a student's language" (9 slides,
https://claude.ai/artifact/6cuss6ceJT4uk6t3M58ASa). Style rules: `docs/design/slide-style-guide.md`.
