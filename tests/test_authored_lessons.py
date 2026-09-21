"""Authored-lesson test: parsing, serving, and the validator.

What this verifies:
    1. A well-formed Markdown lesson parses, validates clean, and KaTeX renders
       its maths.
    2. The validator REJECTS each kind of broken lesson: a missing section,
       sections out of order, a wrong MCQ answer key, a missing misconception, a
       backslash in a double-quoted YAML string (control character), leaked
       drafting text, maths KaTeX can't render, unbalanced '$', a file in the
       wrong place, an unknown interest, and a body that is too short.
    2b. Images: a lesson with no image, a missing file, missing alt text or
       caption, an external URL, an unsafe SVG (script / event handler /
       external link), and a famous image whose caption omits its licence.
    3. lesson_service serves the authored "explain" lesson in the legacy shape
       and falls back to legacy JSON when no authored lesson exists.
    4. The answer never leaks: neither the legacy adapter nor the student view
       contains the answer key, the explanation or the misconceptions.

Runs locally against a temp lessons directory — no LLM calls.
"""

from __future__ import annotations

import os
import shutil
import sys
import tempfile
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT))

_TMP = Path(tempfile.mkdtemp(prefix="ecolearn_lessons_"))
_MEDIA = Path(tempfile.mkdtemp(prefix="ecolearn_media_"))
os.environ["ECOLEARN_LESSONS_DIR"] = str(_TMP)  # before importing lesson_service

from src.content import lesson_service  # noqa: E402
from src.content.authored import parse_lesson_text, student_view, to_legacy_lesson  # noqa: E402
from src.content.validate import validate_files  # noqa: E402

_checks = 0


def check(condition: bool, label: str) -> None:
    global _checks
    assert condition, f"FAIL: {label}"
    _checks += 1
    print(f"  ok  {label}")


_PARA = ("A batter who swings harder gives the ball a bigger push for the same "
         "brief contact, and the ball leaves the bat faster. The same idea runs "
         "through every push and pull in this lesson: force changes motion, and "
         "the heavier the object, the more force the same change needs. ")

GOOD = """---
concept_id: second_law
interest: cricket
format: explain
title: Why a bouncer needs a strong shoulder
check:
  question: |-
    A bowler doubles the net force on a ball of fixed mass. What happens to its acceleration?
  options:
    A: |-
      It stays the same
    B: |-
      It doubles, since $a = F/m$
    C: |-
      It halves
    D: |-
      It becomes four times as large
  answer: B
  explanation: |-
    With $m$ fixed, $a = F/m$ is directly proportional to $F$.
  misconceptions:
    A: |-
      Thinks acceleration depends only on mass.
    C: |-
      Inverts the relation between force and acceleration.
    D: |-
      Squares the force, confusing it with kinetic energy.
author: claude-code/opus-5
written: 2026-09-21
---
## The story

![A batter drives a cricket ball back past the bowler](scenes/cricket/laws_of_motion.svg "One swing, one millisecond.")

{p}

## The physics

Newton's second law says $\\vec{{F}}_{{net}} = m\\vec{{a}}$. {p}

## Worked example

A $0.16\\,\\text{{kg}}$ ball gains $30\\,\\text{{m/s}}$ in $0.1\\,\\text{{s}}$:

$$a = \\frac{{\\Delta v}}{{\\Delta t}} = \\frac{{30}}{{0.1}} = 300\\,\\text{{m/s}}^2, \\qquad F = ma = 48\\,\\text{{N}}$$

{p}

## Where the picture breaks

{p}

## Key takeaway

{p}
""".format(p=_PARA)

GOOD_PATH = ("11", "laws_of_motion", "second_law", "cricket__explain.md")


def write(text: str, parts: tuple[str, ...] = GOOD_PATH) -> Path:
    path = _TMP.joinpath(*parts)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


def errors_for(text: str, parts: tuple[str, ...] = GOOD_PATH, media: Path | None = None) -> list[str]:
    path = write(text, parts)
    report = validate_files([path], _TMP, media_root=media)
    path.unlink()
    return [i.message for i in report.errors]


def expect_error(label: str, text: str, needle: str, parts: tuple[str, ...] = GOOD_PATH,
                 media: Path | None = None) -> None:
    errs = errors_for(text, parts, media)
    check(any(needle in e for e in errs), f"{label} -> flagged ({needle!r})")


def test_good_lesson() -> None:
    print("\n[1] a well-formed lesson")
    lesson = parse_lesson_text(GOOD)
    check(lesson.format.value == "explain" and len(lesson.sections) == 5, "parses into 5 sections")
    check(next(iter(lesson.sections)) == "The story", "opens with the story")
    path = write(GOOD)
    report = validate_files([path], _TMP)
    for i in report.issues:
        print("     ", i.level, i.message)
    check(report.katex_checked, "KaTeX actually rendered the maths")
    check(report.valid == 1 and not report.errors, "validates with no errors")


def test_broken_lessons() -> None:
    print("\n[2] broken lessons are rejected")
    expect_error("missing story opening", GOOD.replace("## The story", "## The scene"),
                 "missing required section '## The story'")
    expect_error("missing section", GOOD.replace("## Where the picture breaks", "## Limits"),
                 "missing required section '## Where the picture breaks'")
    swapped = GOOD.replace("## The story", "## TMP").replace("## Key takeaway", "## The story") \
                  .replace("## TMP", "## Key takeaway")
    expect_error("sections out of order", swapped, "out of order")
    expect_error("answer not an option", GOOD.replace("  answer: B", "  answer: E"),
                 "not one of the options")
    expect_error("misconception missing", GOOD.replace(
        "    D: |-\n      Squares the force, confusing it with kinetic energy.\n", ""),
        "misconceptions must cover exactly the wrong options")
    expect_error("backslash in double-quoted YAML", GOOD.replace(
        "title: Why a bouncer needs a strong shoulder", 'title: "Force \\frac{a}{b} in cricket"'),
        "control character")
    expect_error("leaked drafting text", GOOD.replace("## Key takeaway\n\n", "## Key takeaway\n\nLet me check the numbers. "),
                 "drafting text")
    expect_error("maths KaTeX can't render", GOOD.replace("\\frac{\\Delta v}", "\\frac{\\Delta v"),
                 "KaTeX cannot render")
    expect_error("unbalanced dollar", GOOD.replace("{p}".format(p=_PARA)[:20], "It cost $5. " + _PARA[:20], 1),
                 "unbalanced '$'")
    expect_error("wrong folder", GOOD, "wrong location",
                 parts=("12", "laws_of_motion", "second_law", "cricket__explain.md"))
    expect_error("unknown interest", GOOD.replace("interest: cricket", "interest: chess"),
                 "not in data/interests.yaml",
                 parts=("11", "laws_of_motion", "second_law", "chess__explain.md"))
    short = GOOD.split("## The story")[0] + "\n".join(
        f"## {h}\n\nShort." for h in ("The story", "The physics", "Worked example",
                                      "Where the picture breaks", "Key takeaway"))
    expect_error("body too short", short, "at least")


def test_images() -> None:
    print("\n[2b] images")
    scene = "![A batter drives a cricket ball back past the bowler](scenes/cricket/laws_of_motion.svg \"One swing, one millisecond.\")"
    assert scene in GOOD

    expect_error("no image at all", GOOD.replace(scene, ""), "no images")
    expect_error("image file missing", GOOD.replace("laws_of_motion.svg", "nope.svg"), "does not exist")
    expect_error("no alt text", GOOD.replace("[A batter drives a cricket ball back past the bowler]", "[]"),
                 "needs alt text")
    expect_error("no caption", GOOD.replace(' "One swing, one millisecond."', ""), "needs a caption")
    expect_error("external URL", GOOD.replace("scenes/cricket/laws_of_motion.svg",
                                              "https://example.com/pic.png"), "not a URL")
    expect_error("outside the media folders", GOOD.replace("scenes/cricket/", "../secrets/"),
                 "must start with one of")

    # Unsafe SVGs, in a throwaway media root.
    (_MEDIA / "scenes" / "cricket").mkdir(parents=True, exist_ok=True)
    (_MEDIA / "famous").mkdir(parents=True, exist_ok=True)
    unsafe = {
        "script": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10"><script>alert(1)</script></svg>',
        "handler": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10" onload="alert(1)"/>',
        "external link": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10"><image href="https://evil.example/x.png"/></svg>',
        "no viewBox": '<svg xmlns="http://www.w3.org/2000/svg" width="10" height="10"/>',
        "broken XML": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10"><g></svg>',
    }
    needles = {"script": "<script>", "handler": "event handler", "external link": "external resource",
               "no viewBox": "no viewBox", "broken XML": "does not parse"}
    for label, svg in unsafe.items():
        (_MEDIA / "scenes" / "cricket" / "laws_of_motion.svg").write_text(svg, encoding="utf-8")
        expect_error(f"SVG with {label}", GOOD, needles[label], media=_MEDIA)

    # A famous image must state its licence in the caption.
    shutil.copy(_ROOT / "data" / "media" / "famous" / "manifest.yaml", _MEDIA / "famous")
    shutil.copy(_ROOT / "data" / "media" / "famous" / "georg-simon-ohm-portrait.jpg", _MEDIA / "famous")
    shutil.copy(_ROOT / "data" / "media" / "scenes" / "cricket" / "laws_of_motion.svg",
                _MEDIA / "scenes" / "cricket" / "laws_of_motion.svg")
    famous = GOOD.replace(scene, "![A portrait of Georg Simon Ohm](famous/georg-simon-ohm-portrait.jpg \"Georg Simon Ohm.\")")
    expect_error("famous image without its licence in the caption", famous, "must state the licence",
                 media=_MEDIA)
    ok = famous.replace('"Georg Simon Ohm."', '"Georg Simon Ohm. Public domain, via Wikimedia Commons."')
    check(not errors_for(ok, media=_MEDIA), "famous image with licence in caption passes")
    (_MEDIA / "famous" / "unlisted.jpg").write_bytes(b"x")
    from src.content.validate import check_media_library
    lib = [i.message for i in check_media_library(_MEDIA)]
    check(any("no manifest entry" in m for m in lib), "an unlisted famous image is flagged library-wide")


def test_serving() -> None:
    print("\n[3] serving")
    check(lesson_service.get_lesson("second_law", "cricket") is None, "no lesson -> None")

    write(GOOD)
    legacy = lesson_service.get_lesson("second_law", "Cricket")  # case-insensitive interest
    check(legacy is not None and legacy.metadata.source == "authored",
          "authored explain lesson is served in the legacy shape")
    check(legacy.metadata.critic_verdict == "NOT_RUN" and not legacy.metadata.critic_passed,
          "metadata says honestly that no critic ran")
    check(lesson_service.available_formats("second_law", "cricket") == ["explain"],
          "available_formats lists what exists")

    shutil.copy(_ROOT / "data" / "lessons" / "position__football.json", _TMP)
    old = lesson_service.get_lesson("position", "football")
    check(old is not None and old.metadata.source == "factory", "falls back to legacy JSON")


def test_answer_never_leaks() -> None:
    print("\n[4] the answer never leaks")
    lesson = parse_lesson_text(GOOD)
    legacy = to_legacy_lesson(lesson).model_dump_json()
    view = str(student_view(lesson))
    for label, blob in (("legacy lesson", legacy), ("student view", view)):
        check("answer" not in blob.lower().replace("answer_", ""), f"{label}: no answer key")
        check("proportional" not in blob, f"{label}: no explanation")
        check("kinetic energy" not in blob, f"{label}: no misconceptions")


def main() -> None:
    try:
        test_good_lesson()
        test_broken_lessons()
        test_images()
        test_serving()
        test_answer_never_leaks()
    finally:
        shutil.rmtree(_TMP, ignore_errors=True)
        shutil.rmtree(_MEDIA, ignore_errors=True)
    print(f"\nALL {_checks} CHECKS PASSED")


if __name__ == "__main__":
    main()
