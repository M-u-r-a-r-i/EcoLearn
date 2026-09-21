"""Authored lessons — parse the Markdown files and adapt them for serving.

An authored lesson is one file:

    data/lessons/{grade}/{chapter_id}/{concept_id}/{interest}__{format}.md

    ---
    concept_id: ohms_law
    interest: music
    format: explain
    title: ...
    check:
      question: |-
        ...
      options:
        A: |-
          ...
      answer: B
      explanation: |-
        ...
      misconceptions:
        A: |-
          ...
    author: claude-code/opus-5
    written: 2026-09-22
    ---
    ## The scene
    ...

Markdown rather than JSON because physics text is full of backslashes
(`\\frac`, `\\vec`): in JSON every one must be doubled, and across thousands of
hand-written files some would be missed and render as broken maths. Text fields
in the YAML header use `|-` block scalars, where backslashes are literal.

Functions:
    parse_lesson_text(text)        -> AuthoredLesson   (raises LessonParseError)
    parse_lesson_file(path)        -> AuthoredLesson
    split_sections(body)           -> dict[heading, markdown]
    check_markdown(check)          -> the question + options, WITHOUT the answer
    to_legacy_lesson(lesson)       -> Lesson, the shape today's UIs render
    student_view(lesson)           -> dict safe to send to a browser
"""

from __future__ import annotations

import re
from datetime import datetime, time, timezone
from pathlib import Path
from typing import Any

import yaml
from pydantic import ValidationError

from src.content.lesson_schema import (
    AuthoredLesson,
    Lesson,
    LessonMetadata,
    MCQCheck,
)

_FRONT_MATTER = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n(.*)\Z", re.DOTALL)
_H2 = re.compile(r"^## +(.+?)\s*$", re.MULTILINE)


class LessonParseError(ValueError):
    """A lesson file that can't be read as an AuthoredLesson."""


def split_sections(body: str) -> dict[str, str]:
    """Split Markdown into {H2 heading: section text}. Text before the first
    H2 is kept under the empty-string key so a validator can flag it."""
    sections: dict[str, str] = {}
    matches = list(_H2.finditer(body))
    preamble = body[: matches[0].start()].strip() if matches else body.strip()
    if preamble:
        sections[""] = preamble
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        heading = m.group(1).strip()
        if heading in sections:
            raise LessonParseError(f"section '## {heading}' appears twice")
        sections[heading] = body[m.end():end].strip()
    return sections


def parse_lesson_text(text: str) -> AuthoredLesson:
    """Parse one lesson file's text. Raises LessonParseError with a readable
    message on any structural problem."""
    m = _FRONT_MATTER.match(text.lstrip("﻿"))
    if not m:
        raise LessonParseError("file must start with a '---' YAML header closed by '---'")
    try:
        header = yaml.safe_load(m.group(1))
    except yaml.YAMLError as exc:
        raise LessonParseError(f"YAML header does not parse: {exc}") from exc
    if not isinstance(header, dict):
        raise LessonParseError("YAML header must be a mapping")

    body = m.group(2).strip()
    try:
        return AuthoredLesson.model_validate(
            {**header, "body": body, "sections": split_sections(body)}
        )
    except ValidationError as exc:
        problems = "; ".join(
            f"{'.'.join(str(p) for p in e['loc']) or 'lesson'}: {e['msg']}" for e in exc.errors()
        )
        raise LessonParseError(problems) from exc


def parse_lesson_file(path: str | Path) -> AuthoredLesson:
    return parse_lesson_text(Path(path).read_text(encoding="utf-8"))


def check_markdown(check: MCQCheck) -> str:
    """The question and its options as Markdown — never the answer."""
    lines = [check.question.strip(), ""]
    lines += [f"- **{key})** {text.strip()}" for key, text in check.options.items()]
    return "\n".join(lines)


def to_legacy_lesson(lesson: AuthoredLesson) -> Lesson:
    """Adapt an authored lesson to the legacy `Lesson` shape the current web
    app and Streamlit render (body / worked_example / check_question).

    The whole authored body goes into `body` so no section is lost; the
    check becomes question + options without the answer. The metadata says
    plainly that no critic ran.
    """
    return Lesson(
        concept_id=lesson.concept_id,
        interest=lesson.interest,
        body=f"# {lesson.title}\n\n{lesson.body}",
        worked_example="",
        check_question=check_markdown(lesson.check),
        metadata=LessonMetadata(
            generated_at=datetime.combine(lesson.written, time(0), tzinfo=timezone.utc),
            critic_passed=False,
            critic_verdict="NOT_RUN",
            attempts=0,
            critic_feedback="",
            source="authored",
        ),
    )


def student_view(lesson: AuthoredLesson) -> dict[str, Any]:
    """Everything a browser may see: sections and the question, no answer."""
    return {
        "concept_id": lesson.concept_id,
        "interest": lesson.interest,
        "format": lesson.format.value,
        "title": lesson.title,
        "sections": [
            {"heading": h, "markdown": md} for h, md in lesson.sections.items() if h
        ],
        "check": {
            "question": lesson.check.question,
            "options": dict(lesson.check.options),
        },
    }
