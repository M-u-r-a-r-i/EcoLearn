"""Teacher agent: turns a class's pilot data into a plan for the next lesson.

WHAT MAKES IT AN AGENT
----------------------
The model is not handed one big prompt with everything in it. It gets a set
of read-only tools over its class's data (overview, misconceptions, concept
details, lesson takeaways, students) and decides what to look at, in what
order, until it can write a plan. Every tool call is recorded, so the teacher
can open "How the assistant worked" and see the investigation behind the plan.

THE GUARDRAILS (why it's safe to show a teacher, and to put in front of judges)
* **No names leave the server.** Tools describe students as S1, S2, …; the
  boundary keeps the map and fills names back in only when showing the plan
  to that class's own teacher.
* **No invented physics.** The physics comes from the lesson's own "Key
  takeaway" (written and reviewed with the lesson), fetched through a tool.
* **No invented data.** Tools return the only numbers it may use; the
  prompt (prompts/teacher_agent.txt) says so, and the output is checked for
  its five sections before it is accepted.
* **Bounded.** At most `MAX_STEPS` model turns; the last one has tools off.
* **Never a blank screen.** If no model is configured or every model fails,
  `rules_plan` writes the same five sections from the same data, by fixed
  rules, and the plan says which one the teacher is reading.

Read-only by design: no tool changes anything, so the worst a bad model
output can do is give poor advice — which the teacher reads before acting.

Gemini only (user decision), through google-genai. Model per env var
TEACHER_AGENT_MODEL (default gemini-2.5-flash), with gemini-2.5-flash-lite as
fallback. Both accept tools and a system prompt; we still put the prompt in
the first user message, which works for every model (Gemma has no system role
— see PROJECT_HISTORY.md §6).
"""

from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Protocol

_PROJECT_ROOT = Path(__file__).resolve().parents[2]
_PROMPT_PATH = _PROJECT_ROOT / "prompts" / "teacher_agent.txt"

MAX_STEPS = 8
DEFAULT_MODELS = ("gemini-2.5-flash", "gemini-2.5-flash-lite")
SECTIONS = (
    "In one line",
    "Tomorrow's 10-minute starter",
    "Who to check in with",
    "What to do next",
    "How sure is this?",
)
# Below this many first-try answers, the plan says the data is too thin.
THIN_DATA_ANSWERS = 5

_ALIAS_RE = re.compile(r"\[S(\d+)\]")


# ---------------------------------------------------------------------------
# The tools
# ---------------------------------------------------------------------------

TOOL_DECLARATIONS: list[dict[str, Any]] = [
    {
        "name": "get_class_overview",
        "description": "Headline numbers for the class: students, how many are active, lessons "
                       "opened, reading time, first-try accuracy, lesson ratings, and the same "
                       "numbers per interest.",
        "parameters": {"type": "object", "properties": {}},
    },
    {
        "name": "list_misconceptions",
        "description": "Wrong answers grouped by the misconception they reveal, most common first. "
                       "Each has the concept, the question, the wrong option chosen, the right "
                       "answer, and which students (as labels like S3) chose it.",
        "parameters": {
            "type": "object",
            "properties": {"limit": {"type": "integer", "description": "How many (default 5)."}},
        },
    },
    {
        "name": "get_concept",
        "description": "One concept: its name, chapter, learning objective, the class's results on "
                       "it, and its prerequisites with the class's results on each.",
        "parameters": {
            "type": "object",
            "properties": {"concept_id": {"type": "string"}},
            "required": ["concept_id"],
        },
    },
    {
        "name": "get_lesson_takeaway",
        "description": "The 'Key takeaway' section of the lesson for a concept, in an interest. "
                       "Use its wording for any physics you explain.",
        "parameters": {
            "type": "object",
            "properties": {
                "concept_id": {"type": "string"},
                "interest": {"type": "string",
                             "description": "Optional; defaults to the class's main interest."},
            },
            "required": ["concept_id"],
        },
    },
    {
        "name": "list_students",
        "description": "Every student as a label (S1, S2, ...) with interest, lessons opened, "
                       "minutes read, first-try results, days since last active and ratings.",
        "parameters": {"type": "object", "properties": {}},
    },
]


def _pct(value: float | None) -> str:
    return "n/a" if value is None else f"{round(value * 100)}%"


@dataclass
class ClassToolbox:
    """Read-only views over one class's data, with students as aliases.

    Built by the boundary (src/platform_api.py) from `class_insights` output,
    so the agent and the dashboard read exactly the same numbers.
    """

    class_info: dict[str, Any]
    insights: dict[str, Any]
    alias_of: dict[str, str]  # student_id -> "S3"
    concept_lookup: Callable[[str], dict[str, Any] | None]
    takeaway_lookup: Callable[[str, str], str | None]
    days_since: Callable[[str | None], int | None]
    calls: list[dict[str, Any]] = field(default_factory=list)

    # -- helpers ------------------------------------------------------------
    def main_interest(self) -> str | None:
        rows = self.insights.get("interests") or []
        if not rows:
            return None
        return max(rows, key=lambda r: (r["students"], r["lessons_opened"]))["interest"]

    def _concept_stats(self, concept_id: str) -> dict[str, Any] | None:
        return next((c for c in self.insights["concepts"] if c["concept_id"] == concept_id), None)

    # -- the tools ----------------------------------------------------------
    def get_class_overview(self) -> dict[str, Any]:
        s = self.insights["summary"]
        return {
            "class": self.class_info.get("name"),
            "level": self.class_info.get("level"),
            "students": s["students"],
            "active_students": s["active_students"],
            "lessons_opened": s["lessons_opened"],
            "active_minutes": s["active_minutes"],
            "median_minutes_per_lesson": s["median_minutes_per_lesson"],
            "first_try": f"{s['first_try_correct']} of {s['first_try_answers']} right "
                         f"({_pct(s['first_try_accuracy'])})",
            "first_try_answers": s["first_try_answers"],
            "ratings": f"{s['thumbs_up']} helpful, {s['thumbs_down']} not helpful",
            "by_interest": [
                {"interest": i["interest"], "students": i["students"],
                 "first_try": _pct(i["first_try_accuracy"]), "helpful": _pct(i["approval"])}
                for i in self.insights["interests"]
            ],
            "enough_data": s["first_try_answers"] >= THIN_DATA_ANSWERS,
        }

    def list_misconceptions(self, limit: int = 5) -> dict[str, Any]:
        limit = max(1, min(int(limit or 5), 10))
        items = []
        for m in self.insights["misconceptions"][:limit]:
            items.append({
                "concept_id": m["concept_id"],
                "concept": m["concept_name"],
                "interest": m["interest"],
                "misconception": m["misconception"],
                "students": f"{m['students']} of {m['students_answered']} who answered "
                            f"({_pct(m['share'])})",
                "chosen_by": sorted(
                    (self.alias_of[s] for s in m.get("student_ids", []) if s in self.alias_of),
                    key=lambda a: int(a[1:]),
                ),
                "question": m["question"],
                "wrong_option": m["option_text"],
                "right_answer": m["correct_text"],
            })
        return {"misconceptions": items, "total": len(self.insights["misconceptions"])}

    def get_concept(self, concept_id: str) -> dict[str, Any]:
        concept = self.concept_lookup(concept_id)
        if concept is None:
            return {"error": f"No concept {concept_id!r}. Use a concept_id from another tool."}
        stats = self._concept_stats(concept_id)
        prerequisites = []
        for pid in concept.get("prerequisites", []):
            p = self.concept_lookup(pid) or {"name": pid}
            p_stats = self._concept_stats(pid)
            prerequisites.append({
                "concept_id": pid,
                "name": p.get("name", pid),
                "class_first_try": _pct(p_stats["first_try_accuracy"]) if p_stats else "not attempted",
            })
        return {
            "concept_id": concept_id,
            "name": concept["name"],
            "chapter": concept.get("chapter_name"),
            "learning_objective": concept.get("learning_objective"),
            "class_results": (
                {"opened_by": stats["students_opened"], "answered": stats["students_answered"],
                 "first_try": _pct(stats["first_try_accuracy"]),
                 "median_minutes": stats["median_minutes"]}
                if stats else "no activity yet"
            ),
            "prerequisites": prerequisites,
        }

    def get_lesson_takeaway(self, concept_id: str, interest: str | None = None) -> dict[str, Any]:
        interest = (interest or self.main_interest() or "").lower()
        text = self.takeaway_lookup(concept_id, interest) if interest else None
        if not text:
            return {"error": f"No lesson takeaway for {concept_id!r} in {interest or 'this class'}."}
        return {"concept_id": concept_id, "interest": interest, "key_takeaway": text}

    def list_students(self) -> dict[str, Any]:
        rows = []
        for st in self.insights["students"]:
            alias = self.alias_of.get(st["student_id"])
            if alias is None:
                continue
            rows.append({
                "student": alias,
                "interest": st.get("interest"),
                "lessons_opened": st["lessons_opened"],
                "minutes_read": st["active_minutes"],
                "first_try": f"{st['first_try_correct']} of {st['answered']}",
                "days_since_active": self.days_since(st.get("last_active")),
                "ratings": f"{st['thumbs_up']} up, {st['thumbs_down']} down",
            })
        rows.sort(key=lambda r: int(r["student"][1:]))
        return {"students": rows}

    # -- dispatch -----------------------------------------------------------
    _SUMMARY = {
        "get_class_overview": "Looked at the class overview",
        "list_misconceptions": "Read the most common misconceptions",
        "get_concept": "Looked up a concept and its prerequisites",
        "get_lesson_takeaway": "Read the lesson's key takeaway",
        "list_students": "Reviewed each student's activity",
    }

    def call(self, name: str, args: dict[str, Any] | None) -> dict[str, Any]:
        """Run one tool. Unknown tools and bad arguments come back as an error
        the model can read and recover from, never as an exception."""
        args = dict(args or {})
        method = getattr(self, name, None) if name in self._SUMMARY else None
        if method is None:
            result: dict[str, Any] = {"error": f"Unknown tool {name!r}."}
        else:
            try:
                result = method(**args)
            except TypeError as exc:
                result = {"error": f"Bad arguments for {name}: {exc}"}
        summary = self._SUMMARY.get(name, f"Tried an unknown tool ({name})")
        if name in ("get_concept", "get_lesson_takeaway") and "concept_id" in args:
            concept = self.concept_lookup(str(args["concept_id"]))
            if concept:
                summary += f": {concept['name']}"
        self.calls.append({"tool": name, "args": args, "summary": summary,
                           "ok": "error" not in result})
        return result


# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------

@dataclass
class ModelTurn:
    text: str
    calls: list[dict[str, Any]]  # [{"name": ..., "args": {...}}]
    raw: Any = None  # the provider's own message, replayed verbatim


class Model(Protocol):
    name: str

    def step(self, messages: list[dict[str, Any]], allow_tools: bool) -> ModelTurn: ...


class GeminiModel:
    """One Gemini model behind the `Model` interface (google-genai SDK)."""

    def __init__(self, name: str, api_key: str):
        from google import genai  # imported here: only the agent path needs it

        self.name = name
        # AI Studio keys start "AIza"; Vertex AI express-mode keys start "AQ.".
        self._client = (genai.Client(vertexai=True, api_key=api_key)
                        if api_key.startswith("AQ.") else genai.Client(api_key=api_key))

    def step(self, messages: list[dict[str, Any]], allow_tools: bool) -> ModelTurn:
        from google.genai import types

        contents = []
        for m in messages:
            if m["role"] == "user":
                contents.append(types.Content(role="user", parts=[types.Part.from_text(text=m["text"])]))
            elif m["role"] == "model":
                contents.append(m["raw"])
            else:  # tool results (plus, near the step limit, a nudge to finish)
                parts = [types.Part.from_function_response(name=r["name"], response=r["response"])
                         for r in m["results"]]
                if m.get("nudge"):
                    parts.append(types.Part.from_text(text=m["nudge"]))
                contents.append(types.Content(role="user", parts=parts))
        config = types.GenerateContentConfig(
            temperature=0.3,
            max_output_tokens=4096,
            automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True),
        )
        if allow_tools:
            config.tools = [types.Tool(function_declarations=[
                types.FunctionDeclaration(name=t["name"], description=t["description"],
                                          parameters_json_schema=t["parameters"])
                for t in TOOL_DECLARATIONS
            ])]
        response = self._client.models.generate_content(
            model=self.name, contents=contents, config=config
        )
        calls = [{"name": c.name, "args": dict(c.args or {})} for c in (response.function_calls or [])]
        text = "" if calls else (response.text or "")
        raw = response.candidates[0].content if response.candidates else None
        return ModelTurn(text=text, calls=calls, raw=raw)


class OpenAICompatModel:
    """A model behind any OpenAI-compatible endpoint, via src/llm (OmniRoute,
    OpenRouter, or Gemini's OpenAI-compatible URL)."""

    def __init__(self, name: str):
        self.name = name

    def step(self, messages: list[dict[str, Any]], allow_tools: bool) -> ModelTurn:
        from src import llm

        out: list[dict[str, Any]] = []
        for m in messages:
            if m["role"] == "user":
                out.append({"role": "user", "content": m["text"]})
            elif m["role"] == "model":
                out.append({"role": "assistant", **{k: v for k, v in m["raw"].items() if k != "role"}})
            else:
                for r in m["results"]:
                    out.append({"role": "tool", "tool_call_id": r.get("id") or r["name"],
                                "content": json.dumps(r["response"], ensure_ascii=False)})
                if m.get("nudge"):
                    out.append({"role": "user", "content": m["nudge"]})
        tools = [{"type": "function", "function": t} for t in TOOL_DECLARATIONS] if allow_tools else None
        result = llm.chat(out, models=[self.name], tools=tools, temperature=0.3, max_tokens=2000)
        return ModelTurn(text="" if result.tool_calls else result.text,
                         calls=result.tool_calls, raw=result.message)


def default_models() -> list[Model]:
    """The configured model chain: the src/llm models (OmniRoute or any
    OpenAI-compatible endpoint) first, then Gemini direct if a key is set.
    [] when neither is configured."""
    from src import llm

    chain: list[Model] = [OpenAICompatModel(m) for m in llm.configured_models()]
    chain += _gemini_models()
    return chain


def _gemini_models() -> list[Model]:
    # Same rule as src/llm: a variable set in the environment wins even when
    # empty, so GEMINI_API_KEY= switches Gemini off without touching .env.
    from src.llm.client import _env
    key = _env("GEMINI_API_KEY")
    if not key:
        return []
    names = [os.getenv("TEACHER_AGENT_MODEL") or DEFAULT_MODELS[0]]
    names += [n for n in DEFAULT_MODELS if n not in names]
    try:
        return [GeminiModel(n, key) for n in names]
    except Exception:  # noqa: BLE001 — SDK missing or unloadable: fall back to rules
        return []


# ---------------------------------------------------------------------------
# The loop
# ---------------------------------------------------------------------------

def _valid_plan(text: str) -> bool:
    return all(f"## {s}" in text for s in SECTIONS)


def run_agent(toolbox: ClassToolbox, model: Model, max_steps: int = MAX_STEPS) -> str:
    """Let the model investigate with the tools, then return its Markdown plan.

    Raises:
        RuntimeError: the model never produced a plan with the five sections.
    """
    prompt = _PROMPT_PATH.read_text(encoding="utf-8")
    messages: list[dict[str, Any]] = [{
        "role": "user",
        "text": f"{prompt}\n\nInvestigate this class with the tools, then write the plan.",
    }]
    for step in range(max_steps):
        last = step == max_steps - 1
        turn = model.step(messages, allow_tools=not last)
        if turn.calls and not last:
            messages.append({"role": "model", "text": turn.text, "calls": turn.calls, "raw": turn.raw})
            results = {"role": "tool", "results": [
                {"id": c.get("id"), "name": c["name"],
                 "response": toolbox.call(c["name"], c["args"])}
                for c in turn.calls
            ]}
            if step == max_steps - 2:
                # Riding in the same turn as the results: two user turns in a
                # row is something not every model accepts.
                results["nudge"] = ("That's enough investigating. Write the plan now, "
                                    "with the five sections.")
            messages.append(results)
            continue
        text = (turn.text or "").strip()
        if _valid_plan(text):
            return text
        raise RuntimeError("The model's answer was missing required sections.")
    raise RuntimeError("The model ran out of steps without writing a plan.")


def rules_plan(toolbox: ClassToolbox) -> str:
    """The same five sections, written by fixed rules from the same tools.

    Used when no model is configured or every model failed, so a teacher (or a
    demo) never gets an empty page. Deliberately plain: it states what the data
    shows and makes no attempt at an activity it can't ground.
    """
    overview = toolbox.call("get_class_overview", {})
    misconceptions = toolbox.call("list_misconceptions", {"limit": 3})["misconceptions"]
    students = toolbox.call("list_students", {})["students"]
    top = misconceptions[0] if misconceptions else None
    takeaway = (toolbox.call("get_lesson_takeaway", {"concept_id": top["concept_id"],
                                                      "interest": top["interest"]})
                if top else {})

    lines = ["## In one line"]
    if not overview["enough_data"]:
        lines.append(f"Not enough data yet: {overview['active_students']} of "
                     f"{overview['students']} students have started and there are "
                     f"{overview['first_try_answers']} first-try answers.")
    elif top:
        lines.append(f"The most common misconception is in **{top['concept']}**: "
                     f"{top['students']}.")
    else:
        lines.append(f"First-try accuracy is {overview['first_try']}, with no repeated misconception.")

    lines += ["", "## Tomorrow's 10-minute starter"]
    if top and overview["enough_data"]:
        lines.append(f"Pose the check question from **{top['concept']}** to the class and ask for a "
                     f"show of hands. Students who chose *{top['wrong_option']}* likely think: "
                     f"{top['misconception']}")
        if takeaway.get("key_takeaway"):
            lines += ["", "Resolve it with the lesson's own takeaway:", "",
                      "> " + takeaway["key_takeaway"].strip().replace("\n", "\n> ")]
    else:
        lines.append("Give students ten minutes in class to open their first lesson and answer "
                     "its check, so the next plan has data to work with.")

    lines += ["", "## Who to check in with"]
    flagged = []
    chose_top = set(top["chosen_by"]) if top else set()
    for s in students:
        correct, answered = (int(x) for x in s["first_try"].split(" of "))  # "1 of 3"
        if s["lessons_opened"] == 0 and answered == 0:
            flagged.append(f"- [{s['student']}] hasn't started yet.")
        elif s["student"] in chose_top:
            flagged.append(f"- [{s['student']}] chose the most common misconception.")
        elif answered >= 2 and correct / answered < 0.5:
            flagged.append(f"- [{s['student']}] got {s['first_try']} right first time.")
    lines += flagged[:6] or ["Nobody stands out yet."]

    lines += ["", "## What to do next"]
    if top:
        lines.append(f"Revisit **{top['concept']}** with the students above before moving on.")
    else:
        lines.append("Carry on with the next concept in the chapter.")

    lines += ["", "## How sure is this?",
              f"This plan was made by fixed rules, not the AI assistant, from "
              f"{overview['first_try_answers']} first-try answers by "
              f"{overview['active_students']} students."]
    return "\n".join(lines)


def plan_class(toolbox: ClassToolbox, models: list[Model] | None = None) -> dict[str, Any]:
    """Make a plan: the agent with each model in turn, else the rules.

    Returns {"markdown", "source": "agent"|"rules", "model", "trace", "note"}.
    `trace` is the list of tool calls the successful run made.
    """
    models = default_models() if models is None else models
    failures = []
    for model in models:
        toolbox.calls.clear()
        try:
            markdown = run_agent(toolbox, model)
            return {"markdown": markdown, "source": "agent", "model": model.name,
                    "trace": list(toolbox.calls), "note": None}
        except Exception as exc:  # noqa: BLE001 — any model failure → try the next
            failures.append(f"{model.name}: {type(exc).__name__}")
    toolbox.calls.clear()
    markdown = rules_plan(toolbox)
    note = ("The AI assistant isn't configured on this server, so this plan was made by fixed rules."
            if not models else
            "The AI assistant couldn't be reached, so this plan was made by fixed rules.")
    return {"markdown": markdown, "source": "rules", "model": None,
            "trace": list(toolbox.calls), "note": note, "failures": failures}


def fill_names(markdown: str, names: dict[str, str]) -> str:
    """Replace [S3] with the student's name (server-side, for their own teacher)."""
    return _ALIAS_RE.sub(lambda m: f"**{names.get('S' + m.group(1), 'S' + m.group(1))}**", markdown)


def to_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False)
