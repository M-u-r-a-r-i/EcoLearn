"""Deterministic lesson validator — checks FORMAT, never physics.

There is no LLM critic on authored lessons (sprint decision, 2026-09-21), so
this is the automatic safety net. It catches everything mechanical that would
break or embarrass a lesson in front of a student:

  - the file is in the right place, and its ids match the curriculum, the
    interest registry and its own filename;
  - the YAML header parses and the MCQ is consistent (four options, a valid
    answer, one misconception per wrong option);
  - every required section for the format is present, in order, non-empty;
  - the length is sensible;
  - every maths expression renders in KaTeX, and `$` delimiters balance;
  - no control characters (the tell-tale of `\\frac` inside a double-quoted
    YAML string, where `\\f` silently becomes a form-feed);
  - no leaked drafting text ("Let me…", "<think>", "TODO");
  - at least one image, and every image is a local file under data/media/
    (figures/, scenes/ or famous/) with alt text and a caption; SVGs are
    well-formed and safe (no scripts, event handlers or external links);
    famous images have a licence entry in data/media/famous/manifest.yaml and
    show their licence in the caption.

It cannot tell whether the physics is right. That is what the authoring
guide's self-check, the 2% review sample and human reading are for.

Functions:
    validate_files(paths, lessons_root, media_root=None) -> ValidationReport
    check_media_library(media_root=None)                -> list[Issue]
    coverage(lessons_root)                               -> per-chapter present/expected counts
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

import yaml

from src.content.authored import LessonParseError, parse_lesson_file
from src.content.lesson_schema import FORMAT_SECTIONS, AuthoredLesson, LessonFormat
from src.curriculum.interests import load_interests
from src.curriculum.loader import all_concepts, load_subject

_PROJECT_ROOT = Path(__file__).resolve().parents[2]
_CURRICULUM = _PROJECT_ROOT / "data" / "curriculum" / "physics.yaml"
_KATEX_SCRIPT = _PROJECT_ROOT / "scripts" / "katex_check.mjs"
DEFAULT_MEDIA_ROOT = _PROJECT_ROOT / "data" / "media"

# Images: ![alt text](figures/ohms_law/vi-graph.svg "Caption")
_IMAGE = re.compile(r'!\[([^\]]*)\]\(\s*([^)\s]+)(?:\s+"([^"]*)")?\s*\)')
MEDIA_DIRS = ("figures", "scenes", "famous")
IMAGE_TYPES = {".svg", ".png", ".jpg", ".jpeg", ".webp"}
MAX_IMAGE_BYTES = 600_000
MIN_IMAGES = 1
MIN_ALT_CHARS = 10
OPEN_LICENSES = ("public domain", "cc0", "cc by", "cc-by")

MIN_WORDS = 250
MAX_WORDS = 1100

_CONTROL = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")
_DRAFTING = [
    re.compile(p, re.IGNORECASE | re.MULTILINE)
    for p in (
        r"^\s*(let me|let's see|okay,? so|now i|first,? i)\b",
        r"\bas an ai\b",
        r"</?think",
        r"\bself[- ]rating\b",
        r"\bword count\b",
        r"^\s*draft\s*:",
        r"\bTODO\b",
        r"\bFIXME\b",
        r"\[insert",
        r"lorem ipsum",
    )
]
_DISPLAY_MATH = re.compile(r"\$\$(.+?)\$\$", re.DOTALL)
_INLINE_MATH = re.compile(r"(?<![\\$])\$(?!\$)([^$\n]+?)(?<!\\)\$(?!\$)")
_CODE = re.compile(r"`[^`]*`")


@dataclass
class Issue:
    path: Path
    level: str      # "error" | "warning"
    message: str


@dataclass
class ValidationReport:
    files: int = 0
    valid: int = 0
    issues: list[Issue] = field(default_factory=list)
    katex_checked: bool = False

    @property
    def errors(self) -> list[Issue]:
        return [i for i in self.issues if i.level == "error"]


class _Context:
    """Curriculum + registry + media lookups, loaded once per run."""

    def __init__(self, media_root: Path | None = None) -> None:
        subject = load_subject(_CURRICULUM)
        self.concepts = {c.id: c for c in all_concepts(subject)}
        self.chapters = [ch for u in subject.units for ch in u.chapters]
        self.interests = {i.id for i in load_interests()}
        self.media_root = media_root or DEFAULT_MEDIA_ROOT
        self.famous = _load_famous_manifest(self.media_root)
        self._svg_cache: dict[Path, list[str]] = {}

    def svg_problems(self, path: Path) -> list[str]:
        if path not in self._svg_cache:
            self._svg_cache[path] = _svg_problems(path)
        return self._svg_cache[path]


def _load_famous_manifest(media_root: Path) -> dict[str, dict]:
    path = media_root / "famous" / "manifest.yaml"
    if not path.exists():
        return {}
    raw = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return {entry["file"]: entry for entry in raw.get("images", []) if "file" in entry}


def _svg_problems(path: Path) -> list[str]:
    """Well-formed, has a viewBox, and nothing executable or external."""
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as exc:
        return [f"SVG does not parse: {exc}"]
    problems = []
    if not root.tag.endswith("svg"):
        problems.append("file is not an SVG document")
    if "viewBox" not in root.attrib:
        problems.append("SVG has no viewBox, so it won't scale on phones")
    for el in root.iter():
        name = el.tag.rsplit("}", 1)[-1]
        if name in ("script", "foreignObject"):
            problems.append(f"SVG contains <{name}> — not allowed")
        for attr, value in el.attrib.items():
            local = attr.rsplit("}", 1)[-1]
            if local.lower().startswith("on"):
                problems.append(f"SVG has an event handler ({local}) — not allowed")
            if local == "href" and re.match(r"^(https?:)?//", value.strip()):
                problems.append(f"SVG links to an external resource ({value}) — not allowed")
    return sorted(set(problems))


def _check_images(lesson: AuthoredLesson, ctx: _Context, add) -> None:
    images = []
    for label, text in _texts(lesson).items():
        images += [(label, *m.groups()) for m in _IMAGE.finditer(text)]
    if len(images) < MIN_IMAGES:
        add("error", f"no images — every lesson needs at least {MIN_IMAGES} "
                     "(a scene, a graph or diagram, or a famous image)")
    for label, alt, src, caption in images:
        where = f"{label}: image {src!r}"
        if re.match(r"^[a-z]+:|^/", src, re.IGNORECASE):
            add("error", f"{where} must be a local path under data/media/, not a URL or absolute path")
            continue
        parts = Path(src).parts
        if ".." in parts or not parts or parts[0] not in MEDIA_DIRS:
            add("error", f"{where} must start with one of {', '.join(MEDIA_DIRS)}/")
            continue
        path = ctx.media_root / src
        if path.suffix.lower() not in IMAGE_TYPES:
            add("error", f"{where} has an unsupported type (use {', '.join(sorted(IMAGE_TYPES))})")
            continue
        if len((alt or "").strip()) < MIN_ALT_CHARS:
            add("error", f"{where} needs alt text describing it (at least {MIN_ALT_CHARS} characters)")
        if not (caption or "").strip():
            add("error", f'{where} needs a caption: ![alt]({src} "Caption")')
        if not path.exists():
            spec = path.with_suffix(".graph.yaml")
            hint = " — run scripts/render_graphs.py" if spec.exists() else ""
            add("error", f"{where} does not exist{hint}")
            continue
        if path.stat().st_size > MAX_IMAGE_BYTES:
            add("error", f"{where} is {path.stat().st_size // 1000} KB — keep images under "
                         f"{MAX_IMAGE_BYTES // 1000} KB")
        if path.suffix.lower() == ".svg":
            for problem in ctx.svg_problems(path):
                add("error", f"{where}: {problem}")
        if parts[0] == "famous":
            entry = ctx.famous.get(path.name)
            if entry is None:
                add("error", f"{where} has no entry in data/media/famous/manifest.yaml")
            else:
                license_ = str(entry.get("license", ""))
                if not license_.lower().startswith(OPEN_LICENSES):
                    add("error", f"{where} has licence {license_!r} — only public domain / CC0 / CC BY allowed")
                if license_.lower() not in (caption or "").lower():
                    add("error", f"{where}: the caption must state the licence ({license_!r})")


def _texts(lesson: AuthoredLesson) -> dict[str, str]:
    """Every student-visible string in the lesson, labelled for messages."""
    out = {"title": lesson.title, "body": lesson.body,
           "check.question": lesson.check.question,
           "check.explanation": lesson.check.explanation}
    out.update({f"check.options.{k}": v for k, v in lesson.check.options.items()})
    out.update({f"check.misconceptions.{k}": v for k, v in lesson.check.misconceptions.items()})
    return out


def _math_items(label: str, text: str) -> tuple[list[tuple[str, str, bool]], bool]:
    """Extract (label, tex, display) items; also report whether `$` balance."""
    text = _CODE.sub("", text)
    items: list[tuple[str, str, bool]] = []
    for m in _DISPLAY_MATH.finditer(text):
        items.append((label, m.group(1).strip(), True))
    rest = _DISPLAY_MATH.sub(" ", text)
    for m in _INLINE_MATH.finditer(rest):
        items.append((label, m.group(1).strip(), False))
    leftover = _INLINE_MATH.sub(" ", rest).replace("\\$", "")
    return items, "$" not in leftover


def _check_sections(lesson: AuthoredLesson, add) -> None:
    spec = FORMAT_SECTIONS[lesson.format]
    allowed = [name for name, _ in spec]
    required = [name for name, req in spec if req]
    headings = [h for h in lesson.sections if h]

    if "" in lesson.sections:
        add("error", "text before the first '## ' section (the title belongs in the header)")
    if re.search(r"^# ", lesson.body, re.MULTILINE):
        add("error", "an H1 ('# ') in the body — the title comes from the header")
    for h in headings:
        if h not in allowed:
            add("error", f"unknown section '## {h}' for format {lesson.format.value} "
                         f"(allowed: {', '.join(allowed)})")
    for name in required:
        if name not in headings:
            add("error", f"missing required section '## {name}'")
    known = [h for h in headings if h in allowed]
    if known != sorted(known, key=allowed.index):
        add("error", f"sections out of order — expected: {', '.join(allowed)}")
    for h in headings:
        if not lesson.sections[h].strip():
            add("error", f"section '## {h}' is empty")


def _validate_one(path: Path, root: Path, ctx: _Context, report: ValidationReport,
                  math: list[tuple[str, str, bool]]) -> None:
    def add(level: str, message: str) -> None:
        report.issues.append(Issue(path, level, message))

    try:
        lesson = parse_lesson_file(path)
    except (LessonParseError, UnicodeDecodeError) as exc:
        add("error", f"cannot parse: {exc}")
        return

    # --- location and identity -------------------------------------------
    try:
        rel = path.resolve().relative_to(root.resolve()).parts
    except ValueError:
        rel = ()
    concept = ctx.concepts.get(lesson.concept_id)
    if concept is None:
        add("error", f"unknown concept_id {lesson.concept_id!r}")
    if lesson.interest not in ctx.interests:
        add("error", f"interest {lesson.interest!r} is not in data/interests.yaml")
    expected_name = f"{lesson.interest}__{lesson.format.value}.md"
    if path.name != expected_name:
        add("error", f"filename should be {expected_name!r} to match the header")
    if concept is not None:
        want = (str(concept.grade), concept.chapter_id, concept.id)
        if len(rel) != 4 or tuple(rel[:3]) != want:
            add("error", f"wrong location — expected lessons/{'/'.join(want)}/{expected_name}")
    if lesson.written > date.today():
        add("error", f"'written' date {lesson.written} is in the future")

    # --- structure --------------------------------------------------------
    _check_sections(lesson, add)
    _check_images(lesson, ctx, add)
    words = len(re.findall(r"\S+", lesson.body))
    if words < MIN_WORDS:
        add("error", f"body is {words} words — at least {MIN_WORDS} expected")
    elif words > MAX_WORDS:
        add("error", f"body is {words} words — at most {MAX_WORDS} expected")

    # --- text hygiene and maths ------------------------------------------
    for label, text in _texts(lesson).items():
        if _CONTROL.search(text):
            add("error", f"{label}: control character — a backslash inside a double-quoted "
                         "YAML string? Use a '|-' block scalar for text fields")
        for pattern in _DRAFTING:
            if pattern.search(text):
                add("error", f"{label}: looks like leaked drafting text ({pattern.pattern!r})")
                break
        items, balanced = _math_items(label, text)
        if not balanced:
            add("error", f"{label}: unbalanced '$' — every maths span needs an opening and "
                         "closing '$' (never use '$' for money)")
        math.extend((f"{path}::{lbl}", tex, disp) for lbl, tex, disp in items)


def _katex(math: list[tuple[str, str, bool]], report: ValidationReport) -> None:
    node = shutil.which("node")
    if not node or not _KATEX_SCRIPT.exists() or not math:
        if math:
            report.issues.append(Issue(Path("."), "warning",
                                       "maths not rendered: node or scripts/katex_check.mjs missing"))
        return
    payload = [{"id": f"{i}", "tex": tex, "display": disp} for i, (_, tex, disp) in enumerate(math)]
    proc = subprocess.run([node, str(_KATEX_SCRIPT)], input=json.dumps(payload),
                          capture_output=True, text=True, encoding="utf-8", check=False)
    if proc.returncode != 0:
        report.issues.append(Issue(Path("."), "warning", f"KaTeX check failed to run: {proc.stderr[:200]}"))
        return
    report.katex_checked = True
    for failure in json.loads(proc.stdout or "[]"):
        label, tex, _ = math[int(failure["id"])]
        file_part, field_part = label.split("::", 1)
        report.issues.append(Issue(Path(file_part), "error",
                                   f"{field_part}: KaTeX cannot render ${tex}$ — {failure['error']}"))


def validate_files(paths: list[Path], lessons_root: Path,
                   media_root: Path | None = None) -> ValidationReport:
    ctx = _Context(media_root)
    report = ValidationReport()
    math: list[tuple[str, str, bool]] = []
    for path in sorted(paths):
        report.files += 1
        _validate_one(path, lessons_root, ctx, report, math)
    _katex(math, report)
    # A file is valid exactly when no error names it.
    bad = {i.path for i in report.errors}
    report.valid = sum(1 for p in paths if p not in bad)
    return report


def check_media_library(media_root: Path | None = None) -> list[Issue]:
    """Library-wide media checks, independent of any lesson: every famous
    image has a manifest entry (and every entry a file), and every graph spec
    has been rendered."""
    root = media_root or DEFAULT_MEDIA_ROOT
    issues: list[Issue] = []
    famous_dir = root / "famous"
    manifest = _load_famous_manifest(root)
    if famous_dir.exists():
        for f in sorted(famous_dir.iterdir()):
            if f.suffix.lower() in IMAGE_TYPES and f.name not in manifest:
                issues.append(Issue(f, "error", "famous image has no manifest entry (source + licence)"))
    for name, entry in manifest.items():
        if not (famous_dir / name).exists():
            issues.append(Issue(famous_dir / name, "error", "manifest entry has no file"))
        for key in ("title", "source", "license", "credit"):
            if not str(entry.get(key, "")).strip():
                issues.append(Issue(famous_dir / name, "error", f"manifest entry is missing {key!r}"))
    for spec in sorted(root.glob("figures/**/*.graph.yaml")):
        svg = spec.with_name(spec.name.replace(".graph.yaml", ".svg"))
        if not svg.exists() or svg.stat().st_mtime < spec.stat().st_mtime:
            issues.append(Issue(spec, "error", "graph not rendered (or stale) — run scripts/render_graphs.py"))
    return issues


def coverage(lessons_root: Path) -> list[dict]:
    """Per chapter: how many of the expected concept × interest × format files
    exist. Existence only — run validate_files for correctness."""
    ctx = _Context()
    n_formats = len(LessonFormat)
    rows = []
    for ch in ctx.chapters:
        expected = len(ch.concepts) * len(ctx.interests) * n_formats
        present = sum(
            1
            for c in ch.concepts
            for i in ctx.interests
            for f in LessonFormat
            if (lessons_root / str(ch.grade) / ch.id / c.id / f"{i}__{f.value}.md").exists()
        )
        rows.append({"grade": ch.grade, "chapter_id": ch.id, "chapter": ch.name,
                     "present": present, "expected": expected})
    return rows
