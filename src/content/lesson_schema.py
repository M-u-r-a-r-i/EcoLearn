"""Pydantic schema for a pre-generated offline lesson.

A Lesson is one (concept, interest) pair that has been run through the full
generate → critique pipeline and saved to disk. The three body fields map
directly to the analogy generator's three output sections:

    body           — the analogy scenario (generator section 1: SCENARIO)
    worked_example — formal restatement with equations (section 2)
    check_question — the self-check question (section 3)
"""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel


class LessonMetadata(BaseModel):
    generated_at: datetime
    critic_passed: bool
    critic_verdict: str   # "PASS" / "FAIL" / "ERROR"
    attempts: int
    critic_feedback: str = ""


class Lesson(BaseModel):
    concept_id: str
    interest: str
    body: str
    worked_example: str
    check_question: str
    metadata: LessonMetadata
