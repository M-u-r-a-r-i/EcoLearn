"""Pydantic schemas for lessons.

Two kinds of lesson live on disk:

1. **Legacy factory lessons** — `Lesson`, one JSON file per (concept, interest)
   at `data/lessons/{concept_id}__{interest}.json`, produced by the old
   generate → critique → polish pipeline. The three body fields map to the
   generator's output sections:

       body           — the analogy scenario
       worked_example — formal restatement with equations
       check_question — the self-check question

2. **Authored lessons** — `AuthoredLesson`, one Markdown file per
   (concept, interest, format) at
   `data/lessons/{grade}/{chapter_id}/{concept_id}/{interest}__{format}.md`,
   written directly by Claude Code sessions (sprint decision, 2026-09-21).
   Their check question is multiple-choice, with every wrong option mapped to
   the misconception it reveals, so grading needs no LLM call.

The UIs still consume the legacy shape; `src/content/authored.py` adapts an
authored lesson to it until the multi-format UI lands.
"""

from __future__ import annotations

from datetime import date, datetime
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field, model_validator


class LessonMetadata(BaseModel):
    generated_at: datetime
    critic_passed: bool
    critic_verdict: str   # "PASS" / "FAIL" / "ERROR" / "NOT_RUN" (authored)
    attempts: int
    critic_feedback: str = ""
    source: str = "factory"  # "factory" (legacy JSON) or "authored" (Markdown)


class Lesson(BaseModel):
    concept_id: str
    interest: str
    body: str
    worked_example: str
    check_question: str
    metadata: LessonMetadata


# ---------------------------------------------------------------------------
# Authored lessons
# ---------------------------------------------------------------------------

class LessonFormat(str, Enum):
    """The three pedagogical shapes every concept is written in."""

    EXPLAIN = "explain"              # interest scene -> physics -> worked example
    CHALLENGE = "challenge"          # interest puzzle first, reveal afterwards
    MISCONCEPTION = "misconception"  # a wrong intuition, then why it's wrong


# Required H2 section headings for each format, in the order they must appear.
# `optional` headings may appear at their listed position or be left out.
# Every format opens with "The story": a short narrative that sparks curiosity
# before any explaining starts (user decision, 2026-09-21).
FORMAT_SECTIONS: dict[LessonFormat, list[tuple[str, bool]]] = {
    LessonFormat.EXPLAIN: [
        ("The story", True),
        ("The physics", True),
        ("Worked example", True),
        ("Where the picture breaks", True),
        ("Key takeaway", True),
    ],
    LessonFormat.CHALLENGE: [
        ("The story", True),
        ("The challenge", True),
        ("Think first", True),
        ("The reveal", True),
        ("The physics", True),
        ("Worked example", False),
        ("Key takeaway", True),
    ],
    LessonFormat.MISCONCEPTION: [
        ("The story", True),
        ("The common belief", True),
        ("Why it feels right", True),
        ("What actually happens", True),
        ("The physics", True),
        ("Worked example", False),
        ("Key takeaway", True),
    ],
}

OPTION_KEYS = ("A", "B", "C", "D")


class MCQCheck(BaseModel):
    """A multiple-choice check question with diagnosable wrong answers.

    `answer`, `explanation` and `misconceptions` are server-side only — they
    must never be sent to the browser, or the answer is one network-tab away.
    """

    model_config = ConfigDict(extra="forbid")

    question: str = Field(..., min_length=1)
    options: dict[str, str]
    answer: str
    explanation: str = Field(..., min_length=1, description="Why the answer is right.")
    misconceptions: dict[str, str] = Field(
        ..., description="For each WRONG option: the misconception that choosing it reveals."
    )

    @model_validator(mode="after")
    def _consistent(self) -> "MCQCheck":
        if tuple(self.options) != OPTION_KEYS:
            raise ValueError(f"options must be exactly {', '.join(OPTION_KEYS)}, in order")
        if any(not v.strip() for v in self.options.values()):
            raise ValueError("every option needs text")
        if len({v.strip().lower() for v in self.options.values()}) != len(self.options):
            raise ValueError("options must all be different")
        if self.answer not in self.options:
            raise ValueError(f"answer {self.answer!r} is not one of the options")
        wrong = set(self.options) - {self.answer}
        if set(self.misconceptions) != wrong:
            raise ValueError(
                f"misconceptions must cover exactly the wrong options {sorted(wrong)}, "
                f"got {sorted(self.misconceptions)}"
            )
        if any(not v.strip() for v in self.misconceptions.values()):
            raise ValueError("every misconception needs text")
        return self


class AuthoredLesson(BaseModel):
    """One (concept, interest, format) lesson written straight to Markdown."""

    model_config = ConfigDict(extra="forbid")

    concept_id: str
    interest: str
    format: LessonFormat
    title: str = Field(..., min_length=1)
    check: MCQCheck
    author: str = Field(..., min_length=1)
    written: date
    body: str = Field(..., description="The Markdown after the front matter.")
    sections: dict[str, str] = Field(
        default_factory=dict, description="H2 heading -> section Markdown, parsed from body."
    )
