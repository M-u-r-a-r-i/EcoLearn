---
concept_id: resistors_combination
interest: cricket
format: explain
title: One dead bulb and the whole boundary rope goes dark
check:
  question: |-
    A $6.0\,\Omega$ resistor and a $3.0\,\Omega$ resistor are connected in parallel. Their equivalent resistance is:
  options:
    A: |-
      $9.0\,\Omega$
    B: |-
      $2.0\,\Omega$
    C: |-
      $4.5\,\Omega$
    D: |-
      $0.50\,\Omega$
  answer: B
  explanation: |-
    $\dfrac{1}{R_p} = \dfrac{1}{6.0} + \dfrac{1}{3.0} = \dfrac{1}{2.0}$, so $R_p = 2.0\,\Omega$ — smaller than either resistor, as a parallel combination must be.
  misconceptions:
    A: |-
      Adds the resistances, which is the series rule. In parallel the current has two routes, so the combination is easier to push current through, not harder.
    C: |-
      Takes the average of the two values. Averaging happens to work only when the resistors are equal; the reciprocal rule is the general one.
    D: |-
      Stops at $1/R_p = 0.50$ and reports that as the resistance, forgetting the final reciprocal. The units give it away: $0.50$ there is in $\Omega^{-1}$.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A cricket ground at dusk with floodlights, an electronic scoreboard, glowing stumps and an umpire holding a light meter](scenes/cricket/current_electricity.svg "Two lighting circuits at the same ground, wired in two different ways.")

For the club's night tournament, Ishita and Manav are given two jobs. Ishita strings small lamps along the boundary rope. Manav wires up two big work lamps on the practice pitch so the ground staff can finish the covers.

Halfway through the first match, one lamp on the boundary rope fails — and the entire rope goes dark, all the way round. Ishita has to walk the whole circle with a torch, testing bulbs one at a time, to find the one that died.

That same evening a work lamp blows on the practice pitch. The other one carries on, perfectly bright, and Manav doesn't even notice until he goes to switch off.

Same ground, same evening, two failures, two completely different outcomes. Ishita wants to know exactly what Manav did differently — and why his pair of lamps also pulls far more current from the same battery than hers.

## The physics

**In series**, components sit one after another on a single path. There is nowhere for charge to leave, so the **current through each is the same**, and the supply's potential difference is shared out between them: $V = V_1 + V_2 + \dots$. Substituting $V_i = IR_i$ and dividing by $I$,

$$R_s = R_1 + R_2 + \dots$$

**In parallel**, components are connected across the same two points, so the **potential difference across each is the same**, and the current splits between them: $I = I_1 + I_2 + \dots$. Substituting $I_i = V/R_i$ and dividing by $V$,

$$\frac{1}{R_p} = \frac{1}{R_1} + \frac{1}{R_2} + \dots$$

![Two resistors in series sharing the same current, and the same two in parallel sharing the same potential difference](figures/resistors_combination/series-and-parallel.svg "In series the current is shared by nobody and the voltage is shared out; in parallel it is the other way round.")

Two checks that catch most mistakes. A series combination is always **larger** than the largest resistor in it. A parallel combination is always **smaller** than the smallest. If your answer breaks either rule, you have gone wrong somewhere — most often by forgetting the final reciprocal.

For a **complicated network**, work inwards: find groups that are purely series or purely parallel, replace each by one equivalent resistor, redraw, and repeat. All of this assumes the connecting wires have negligible resistance.

That settles the boundary rope. Ishita's lamps were in series, so one broken filament breaks the only path and every lamp goes out. Manav's were in parallel: each has its own route to the battery, so losing one leaves the other untouched.

## Worked example

**Given:** two lamps behaving as resistors of $4\,\Omega$ and $12\,\Omega$, connected to a $12\,\text{V}$ battery — first in series, then in parallel.
**Find:** the current drawn from the battery in each case.

**Series.** The resistances add:

$$R_s = 4 + 12 = 16\,\Omega$$

$$I = \frac{V}{R_s} = \frac{12}{16} = 0.75\,\text{A}$$

**Parallel.** Take reciprocals:

$$\frac{1}{R_p} = \frac{1}{4} + \frac{1}{12} = \frac{3}{12} + \frac{1}{12} = \frac{4}{12}$$

so $R_p = 3\,\Omega$ — less than the smaller lamp, as promised.

$$I = \frac{V}{R_p} = \frac{12}{3} = 4\,\text{A}$$

The same two lamps and the same battery draw **more than five times the current** when wired in parallel. That is why Manav's pair is bright and drains his battery fast, while Ishita's rope is dim and lasts all night.

**Sanity check:** in parallel each lamp gets the full $12\,\text{V}$, drawing $3\,\text{A}$ and $1\,\text{A}$, which add to the $4\,\text{A}$ we found.

## Where the picture breaks

The lamps are a real circuit, not a cricketing analogy — there is no fielding pattern that behaves like a parallel combination, and stretching for one would teach you nothing true. The physics idealisations are the usual ones: real lamps are not fixed resistors, since a filament's resistance rises sharply as it heats, so "4 Ω" only describes it at its working temperature; real batteries have internal resistance, so drawing $4\,\text{A}$ would drop the terminal voltage below $12\,\text{V}$ (the next concept); and real connecting wire has a small resistance of its own, which matters over a boundary-length run.

## Key takeaway

In series the current is common and resistances add, $R_s = R_1 + R_2$; in parallel the potential difference is common and reciprocals add, $1/R_p = 1/R_1 + 1/R_2$. Series always gives more than the largest resistor, parallel always less than the smallest. Break any network into series and parallel groups and replace them one at a time.
