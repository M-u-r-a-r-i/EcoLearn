"""Where the lesson-writing plan stands, and what to write next.

    venv\\Scripts\\python.exe scripts\\batch_status.py            # progress + the next batch
    venv\\Scripts\\python.exe scripts\\batch_status.py --all      # every batch with its status
    venv\\Scripts\\python.exe scripts\\batch_status.py --brief    # the next batch's filled-in brief
    venv\\Scripts\\python.exe scripts\\batch_status.py --brief --batch ray_optics:gaming:explain

Reads the agreed scope (`data/content_scope.yaml`), counts which lesson files
already exist, and works out progress from the disk alone — so there is no
hand-maintained checklist to drift out of date. `--brief` fills in
`content/BATCH_BRIEF.md` for a batch; pass its output, unchanged, as the prompt
of the sub-session that writes the lessons.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path

import yaml

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT))

from src.content.lesson_schema import LessonFormat  # noqa: E402
from src.curriculum.interests import load_interests  # noqa: E402
from src.curriculum.loader import load_subject  # noqa: E402

SCOPE = _ROOT / "data" / "content_scope.yaml"
BRIEF = _ROOT / "content" / "BATCH_BRIEF.md"
LESSONS = _ROOT / "data" / "lessons"
MEDIA = _ROOT / "data" / "media"
GOLD = [
    "data/lessons/11/laws_of_motion/second_law/*.md",
    "data/lessons/12/current_electricity/ohms_law/*.md",
]


@dataclass
class Batch:
    phase: str
    formats: list[str]
    chapter: object       # curriculum Chapter
    interest: object      # registry Interest
    present: int
    expected: int

    @property
    def key(self) -> str:
        return f"{self.chapter.id}:{self.interest.id}:{self.phase}"

    @property
    def done(self) -> bool:
        return self.present >= self.expected

    def missing_files(self) -> list[Path]:
        return [p for p in self.all_files() if not p.exists()]

    def all_files(self) -> list[Path]:
        return [
            LESSONS / str(self.chapter.grade) / self.chapter.id / c.id / f"{self.interest.id}__{f}.md"
            for c in self.chapter.concepts
            for f in self.formats
        ]


def load_scope() -> tuple[dict, list[Batch]]:
    scope = yaml.safe_load(SCOPE.read_text(encoding="utf-8"))
    subject = load_subject(_ROOT / "data" / "curriculum" / "physics.yaml")
    chapters = {ch.id: ch for u in subject.units for ch in u.chapters}
    interests = {i.id: i for i in load_interests()}
    valid_formats = {f.value for f in LessonFormat}

    unknown = [c for c in scope["chapters"] if c not in chapters] + \
              [i for i in scope["interests"] if i not in interests] + \
              [f for p in scope["phases"] for f in p["formats"] if f not in valid_formats]
    if unknown:
        raise SystemExit(f"content_scope.yaml names unknown ids: {unknown}")

    batches = []
    for phase in scope["phases"]:
        for cid in scope["chapters"]:
            for iid in scope["interests"]:
                b = Batch(phase["id"], phase["formats"], chapters[cid], interests[iid], 0, 0)
                files = b.all_files()
                b.expected = len(files)
                b.present = sum(p.exists() for p in files)
                batches.append(b)
    return scope, batches


def _rel(p: Path) -> str:
    return p.relative_to(_ROOT).as_posix()


def fill_brief(b: Batch) -> str:
    ch, it = b.chapter, b.interest
    concept_ids = [c.id for c in ch.concepts]

    # Models: lessons of the same formats already written for this chapter.
    same_chapter = sorted(
        p for f in b.formats
        for p in (LESSONS / str(ch.grade) / ch.id).glob(f"*/*__{f}.md")
        if not p.name.startswith(f"{it.id}__")
    )
    if same_chapter:
        by_interest: dict[str, list[Path]] = {}
        for p in same_chapter:
            by_interest.setdefault(p.name.split("__")[0], []).append(p)
        best = max(by_interest.values(), key=len)
        models = (f"the {len(best)} existing lesson(s) for this same chapter in another interest — "
                  + ", ".join(f"`{_rel(p)}`" for p in best[:12])
                  + (" …" if len(best) > 12 else ""))
    else:
        models = ("the approved gold lessons " + ", ".join(f"`{g}`" for g in GOLD)
                  + " and `data/lessons/11/units_measurement/*/cricket__*.md`")

    figures = sorted(p for cid in concept_ids for p in (MEDIA / "figures" / cid).glob("*.svg"))
    existing_figures = (", ".join(f"`{p.relative_to(MEDIA).as_posix()}`" for p in figures)
                        if figures else
                        "**none yet** — this is the first batch for this chapter, so draw what "
                        "each concept needs (interest-neutral, so later interests reuse them).")

    scene = MEDIA / "scenes" / it.id / f"{ch.id}.svg"
    if scene.exists():
        scene_note = f"reuse `{scene.relative_to(MEDIA).as_posix()}` (already drawn)."
    else:
        styles = sorted((MEDIA / "scenes" / it.id).glob("*.svg")) or sorted((MEDIA / "scenes").glob("*/*.svg"))
        style = f" in the style of `{styles[0].relative_to(MEDIA).as_posix()}`" if styles else ""
        scene_note = (f"draw ONE new scene `scenes/{it.id}/{ch.id}.svg` (flat vector, viewBox "
                      f"0 0 800 450){style} showing {it.label} moments that fit this chapter.")

    manifest = yaml.safe_load((MEDIA / "famous" / "manifest.yaml").read_text(encoding="utf-8"))
    famous = [e for e in manifest.get("images", []) if set(e.get("concepts", [])) & set(concept_ids)]
    famous_note = (", ".join(f"`famous/{e['file']}` ({e['title']})" for e in famous)
                   if famous else "none for this chapter yet")

    strong = {d.value for d in it.strong_domains}
    fit = (f"that is one of {it.label}'s strong domains, so analogies should come naturally."
           if ch.domain.value in strong else
           f"that is NOT one of {it.label}'s strong domains — follow guide §5.3: use real devices "
           f"and situations from its world, or teach directly; never force an analogy.")
    facts = ("\n".join(f"- {f}" for f in it.facts) if it.facts
             else "- (none listed for this interest — use only general, checkable facts)")

    values = {
        "CHAPTER_ID": ch.id, "CHAPTER_NAME": ch.name, "GRADE": str(ch.grade),
        "INTEREST": it.id, "INTEREST_LABEL": it.label,
        "FORMATS": " + ".join(f"`{f}`" for f in b.formats),
        "LESSON_COUNT": str(len(b.missing_files())),
        "CONCEPTS": ", ".join(concept_ids),
        "MODEL_LESSONS": models, "DOMAIN": ch.domain.value, "FIT_NOTE": fit,
        "FACTS": facts, "EXISTING_FIGURES": existing_figures, "SCENE_NOTE": scene_note,
        "FAMOUS": famous_note, "TODAY": date.today().isoformat(),
    }
    text = BRIEF.read_text(encoding="utf-8")
    text = text[text.index("-->") + 3:].lstrip() if text.startswith("<!--") else text
    for k, v in values.items():
        text = text.replace("{" + k + "}", v)
    return text


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--all", action="store_true", help="list every batch")
    parser.add_argument("--brief", action="store_true", help="print the filled-in brief")
    parser.add_argument("--batch", help="chapter:interest:phase instead of the next batch")
    args = parser.parse_args()

    scope, batches = load_scope()
    if args.batch:
        chosen = next((b for b in batches if b.key == args.batch), None)
        if chosen is None:
            raise SystemExit(f"No batch {args.batch!r}. Keys look like ray_optics:gaming:explain")
    else:
        chosen = next((b for b in batches if not b.done), None)

    if args.brief:
        if chosen is None:
            print("Everything in scope is written.")
            return 0
        print(fill_brief(chosen))
        return 0

    print(f"Scope decided {scope['decided']}: {len(scope['chapters'])} chapters × "
          f"{len(scope['interests'])} interests ({', '.join(scope['interests'])})\n")
    for phase in scope["phases"]:
        pb = [b for b in batches if b.phase == phase["id"]]
        done = sum(b.done for b in pb)
        present = sum(b.present for b in pb)
        expected = sum(b.expected for b in pb)
        print(f"Phase {phase['id']:<14} formats {'+'.join(phase['formats']):<24} "
              f"batches {done:>3}/{len(pb):<3}  lessons {present:>4}/{expected:<4}  "
              f"target {phase['target']}")
    if args.all:
        print()
        for b in batches:
            mark = "done" if b.done else ("part" if b.present else "todo")
            print(f"  [{mark}] {b.key:<50} {b.present:>3}/{b.expected}")
    print()
    if chosen is None:
        print("NEXT: nothing — everything in scope is written.")
    else:
        print(f"NEXT BATCH: {chosen.key}  — {chosen.chapter.name} × {chosen.interest.label}, "
              f"{len(chosen.missing_files())} lesson(s) to write")
        print("Brief:      venv\\Scripts\\python.exe scripts\\batch_status.py --brief")
    return 0


if __name__ == "__main__":
    sys.exit(main())
