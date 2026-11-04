# EcoLearn pilot: a randomised comparison (pre-registration)

First written 2026-10-18; **revised 2026-10-19, before the pilot started and before any pilot data existed** (see the
note at the bottom). The point of writing it down now is that the question, the outcome and the analysis can't drift
to fit whatever the numbers turn out to be. If anything here changes after the pilot begins, add a dated note at the
bottom saying what changed and why; don't edit the text above it.

## The question

Every lesson ends with a multiple-choice check whose wrong options are each written to catch one particular mix-up,
so they *feel* right. **Does a one-line prompt to re-read the options before answering help students get the check
right on the first try?**

The line: *"Before you pick: read each option once more. The wrong ones are written to feel right."*

We think it helps, but it is our own idea, and nothing yet shows it works.

## Design

| | |
|---|---|
| Unit | The student |
| Arms | **Treatment**: the line on every lesson check. **Control**: never. Everything else (lessons, checks, stories, revision timing, the help chat, the teacher's view) is the same for both, including sooner revision for students who are often sure of a wrong answer |
| Assignment | When the account is made, balanced within each class (the arm with fewer students so far; a tie decided by a hash of the student id). It never changes. Code: `src/learner/experiments.py`, config: `data/experiments.yaml` (`check_prompt`) |
| Blinding | Students and teachers are not told the arm. The arm is not shown anywhere in the app. Only the operator's pilot report has it |
| Eligible for the primary outcome | Students who answered at least 3 lesson checks (first tries), in either arm |
| Analysis set | Intent to treat: every assigned student stays in their arm |

Why this design: the line reaches every student on every check, so the whole pilot contributes, not only the
handful of students a narrower rule would pick out. It is still a small pilot (see Analysis).

## Outcomes

**Primary.** For each eligible student: the share of lesson checks they answered right on the **first try**.
Compared as the difference of means, treatment minus control.

**Secondary.** (1) For students with 3 or more answers marked "sure": the share of those that were wrong ("sure but
wrong", which the line is meant to reduce). (2) End-check gain for every student who took both checks: right answers
after minus before, over the same concepts.

## Analysis (decided now)

- Run `venv\Scripts\python.exe scripts\pilot_report.py` at the end of the pilot. The experiment section prints both
  arms, the difference and a **95% bootstrap interval** (2,000 resamples of students within each arm, fixed seed, so
  the same data always gives the same interval). `--csv DIR` writes `experiment_arms.csv` (pseudonymised) for a second
  look by anyone.
- **Read the interval, not the estimate.** If it includes 0, the pilot did not show an effect either way.
- **Expect a small sample.** One or two classes give perhaps 20 to 30 eligible students per arm. That can show only a
  fairly large difference (roughly 10 to 15 points of first-try accuracy or more). The report says "far too few" on its
  own when either arm has fewer than 10 eligible students. In the pitch, describe it as a designed first look, with the
  interval, never as proof.
- No other outcome is promoted to "primary" afterwards, and no subgroup is reported as a finding unless it is labelled
  exploratory.

## Ethics and consent

- The control arm loses only a reminder line. Lessons, quizzes, marks, the teacher's view and every safety feature are
  the same. The risk of withholding it is low, and we don't know that it helps.
- The consent note (Part B) tells families that one small feature is switched on for half the students, chosen at
  random. The school decides whether that needs anything more (for example its own ethics sign-off).
- The per-student AI switch is unaffected: this feature is rules, not AI.
- A control student whom the profile flags as "often sure of a wrong answer" sees that on their About me page with
  only what still happens for them (sooner revision); the page never promises the line.
- To stop the experiment early (for example if a teacher sees it cause confusion), set `enabled: false` in
  `data/experiments.yaml`: everyone then gets the normal product. The arms already given stay for the analysis. An
  operator can also switch every experiment off at once with `ECOLEARN_EXPERIMENTS=off`.

## What we will NOT claim

- That the survey-driven adaptations help (they are not part of this comparison).
- That the AI features help learning (also not compared).
- Any effect, if the interval includes 0.

## Changes

- **2026-10-19 (before the pilot, no pilot data yet):** the first version (2026-10-18) compared the "sure but wrong"
  nudge for flagged students only. In the demo class only 5 of 25 students met that rule, so a real class would give a
  handful per arm: too few to show anything. Replaced by the line for everyone, measured on first-try accuracy. The old
  experiment stays in `data/experiments.yaml`, disabled.
