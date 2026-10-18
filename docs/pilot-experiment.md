# EcoLearn pilot: a randomised comparison (pre-registration)

Written 2026-10-18, **before the pilot starts and before any pilot data exists.** The point of writing it down now is
that the question, the outcome and the analysis can't drift to fit whatever the numbers turn out to be. If anything
here changes after the pilot begins, add a dated note at the bottom saying what changed and why; don't edit the text
above it.

## The question

EcoLearn notices when a student is often **sure of an answer that turns out wrong** (a firm mix-up, which feels true).
For those students it does two things: a short line on lesson checks ("Before you pick: read each option once more.
The wrong ones are written to feel right."), and those ideas come back for revision in half the usual time.

**Does that help them fix those mix-ups?** We think so, but it is our own rule, and nothing yet shows it works.

## Design

| | |
|---|---|
| Unit | The student |
| Arms | **Treatment**: the nudge as above (the normal product). **Control**: the nudge is never shown and revision timing is unchanged. Everything else (lessons, checks, stories, the help chat, the teacher's view) is the same for both |
| Assignment | When the account is made, balanced within each class (the arm with fewer students so far; a tie decided by a hash of the student id). It never changes. Code: `src/learner/experiments.py`, config: `data/experiments.yaml` (`sure_wrong_nudge`) |
| Blinding | Students and teachers are not told the arm. The arm is not shown anywhere in the app. Only the operator's pilot report has it |
| Eligible for the primary outcome | Students who meet the rule in EITHER arm: 3 or more answers marked "sure", 2 or more of them wrong, and a third or more wrong. The rule is computed the same way in both arms, so the groups are comparable |
| Analysis set | Intent to treat: every assigned student stays in their arm, including a treatment student who pressed "That's not me" (the report counts those) |

## Outcomes

**Primary.** For each eligible student: of the concepts they answered wrong while sure, the share now **fixed**
(answered right later on a *different* question; a right answer to the same question just after the explanation does
not count). Compared as the difference of means, treatment minus control.

**Secondary.** (1) End-check gain for every student who took both checks: right answers after minus before, over
the same concepts. (2) First-try accuracy at lesson checks.

## Analysis (decided now)

- Run `venv\Scripts\python.exe scripts\pilot_report.py` at the end of the pilot. The experiment section prints both
  arms, the difference and a **95% bootstrap interval** (2,000 resamples of students within each arm, fixed seed, so
  the same data always gives the same interval). `--csv DIR` writes `experiment_arms.csv` (pseudonymised) for a second
  look by anyone.
- **Read the interval, not the estimate.** If it includes 0, the pilot did not show an effect either way.
- **Expect too few students.** A class or two gives perhaps 5 to 15 eligible students per arm. That can only show a
  very large difference. The report says so on its own when either arm has fewer than 10 eligible students. In the
  pitch, describe it as a designed first look, with the interval, never as proof.
- No other outcome is promoted to "primary" afterwards, and no subgroup is reported as a finding unless it is labelled
  exploratory.

## Ethics and consent

- The control arm loses only a reminder line and an earlier revision date. Lessons, quizzes, marks, the teacher's view
  and every safety feature are the same. The risk of withholding it is low, and we don't know that it helps.
- The consent note (Part B) tells families that one small feature is switched on for half the students, chosen at
  random. The school decides whether that needs anything more (for example its own ethics sign-off).
- A family that says no to the AI parts (the per-student AI switch) is unaffected: this feature is rules, not AI.
- To stop the experiment early (for example if a teacher sees it cause confusion), set `enabled: false` in
  `data/experiments.yaml`: everyone then gets the treatment. The arms already given stay for the analysis. An operator
  can also switch every experiment off at once with `ECOLEARN_EXPERIMENTS=off`.

## What we will NOT claim

- That the survey-driven adaptations help (they are not part of this comparison).
- That the AI features help learning (also not compared).
- Any effect, if the interval includes 0.

## Changes after the pilot starts

(none yet)
