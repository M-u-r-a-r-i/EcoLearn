---
concept_id: resistors_combination
interest: football
format: explain
title: The string of forty lights and the one bulb that killed them all
check:
  question: |-
    Three identical bulbs, each of resistance $12\,\Omega$, are connected in parallel. Their equivalent resistance is:
  options:
    A: |-
      $4\,\Omega$
    B: |-
      $36\,\Omega$
    C: |-
      $12\,\Omega$
    D: |-
      $0.25\,\Omega$
  answer: A
  explanation: |-
    In parallel, $\dfrac{1}{R_p} = \dfrac{1}{12} + \dfrac{1}{12} + \dfrac{1}{12} = \dfrac{3}{12}$, so $R_p = 4\,\Omega$ — for $n$ identical resistors in parallel, $R_p = R/n$.
  misconceptions:
    B: |-
      Adds the resistances. That is the series rule; in parallel the extra paths make it *easier* for charge to get through, so the equivalent resistance must come out smaller than any one branch.
    C: |-
      Assumes identical resistors in parallel behave like one of them, since "they are all the same". Each extra branch carries its own current, so the combination draws three times as much as one bulb would.
    D: |-
      Stops at $\dfrac{1}{R_p} = 0.25$ and reports that number. The parallel formula gives the *reciprocal* of the equivalent resistance, so it must be inverted at the end.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A floodlit football ground at night with two lit pylons, an electronic scoreboard, a fourth official holding a glowing LED substitution board, and a pitch-side distribution box with cables running to the lights](scenes/football/current_electricity.svg "Two lighting circuits at the same ground, wired in two completely different ways.")

The club is sixty years old this season, and somebody has bought a string of forty small lights to run along the top of the clubhouse sign for the opening match. Arjun is up the ladder at four in the afternoon with the string in his hands, and none of the forty is lit.

He checks the plug. He checks the socket by plugging in a fan, which spins happily. Then he starts working along the string, unscrewing bulbs one by one and holding each up to the light. Somewhere in that line is a single broken filament, and until he finds it, all forty stay dark.

Behind him, in the changing room, a tube light flickers out. Nobody even looks up. The other three stay on, the fan keeps turning, and the match is not delayed by a second.

Same building, same supply, one dead component in each. One of them takes down everything; the other takes down only itself. The difference is in how the wires were joined — and it is not a detail, because it also decides how much current the supply has to push out.

## The physics

**In series**, components sit one after another on a single path. There is nowhere else for charge to go, so the **current through each is the same**, and the supply's potential difference is shared out between them. Adding the voltage shares gives

$$R_s = R_1 + R_2 + R_3 + \cdots$$

A series combination always resists *more* than any single member — and if one member breaks, the single path is cut, so nothing works. That is Arjun's string.

**In parallel**, components are connected across the same two points, so the **potential difference across each is the same**, and the total current is shared between the branches. Adding the currents gives

$$\frac{1}{R_p} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3} + \cdots$$

A parallel combination always resists *less* than any single member, because you have opened extra paths. And if one branch breaks, the others still have their own route to the supply. That is the changing room.

![Two resistors in series sharing the same current, and the same two in parallel sharing the same potential difference](figures/resistors_combination/series-and-parallel.svg "Series: one path, so one current and a shared voltage. Parallel: one voltage, so each branch takes the current it wants.")

Two shortcuts worth remembering. For $n$ **identical** resistors of resistance $R$ in parallel, $R_p = R/n$. For just two in parallel,

$$R_p = \frac{R_1R_2}{R_1 + R_2}$$

For a mixed network, do not try to see the answer at once. Reduce it in stages: replace each purely-series or purely-parallel group with its single equivalent, redraw, and repeat. All of this assumes the connecting wires have negligible resistance and the supply is ideal.

## Worked example

**Given:** two lamps of $6\,\Omega$ each, wired in parallel, and a $3\,\Omega$ controller resistor in series with the pair, all across a $12\,\text{V}$ supply.
**Find:** the current drawn from the supply, and the current in each lamp.

**Step 1 — collapse the parallel pair.** Two identical $6\,\Omega$ lamps in parallel:

$$R_p = \frac{6}{2} = 3\,\Omega$$

The two lamps together behave like a single $3\,\Omega$ lamp — easier for the supply than either lamp alone.

**Step 2 — add the series resistor.** Now the circuit is just $3\,\Omega$ and $3\,\Omega$ one after the other:

$$R_s = 3 + 3 = 6\,\Omega$$

**Step 3 — the supply current.**

$$I = \frac{V}{R_s} = \frac{12}{6} = 2\,\text{A}$$

**Step 4 — split it.** The two lamps are identical, so the $2\,\text{A}$ divides equally: $1\,\text{A}$ in each.

**Sanity check:** the two branches carry $1\,\text{A}$ each and they must add up to what the supply sends, and they do.

## Where the picture breaks

The clubhouse is the setting, not an analogy — there is no version of a parallel circuit anywhere in the laws of the game. What the model leaves out is the wiring itself: we treated the connecting wires as having no resistance, which is why the "$12\,\text{V}$" appeared undivided across the combination. In a long string of decorative lights that is not quite true. Real filament lamps are also non-ohmic, so a lamp's "$6\,\Omega$" is its resistance while lit at its working temperature, not a fixed number you can trust as it dims. And a modern lighting string usually cheats: the bulbs are wired in series, but each has a shunt inside that closes when its filament fails, so the rest survive — which is why Arjun's forty going dark at once suggests an old string, or a second fault.

## Key takeaway

In series the current is common and resistances add, $R_s = R_1 + R_2 + \cdots$; one break stops everything. In parallel the potential difference is common and reciprocals add, $1/R_p = 1/R_1 + 1/R_2 + \cdots$; the equivalent is smaller than any branch, and one break leaves the rest working. Reduce a mixed network in stages, and always invert at the end of a parallel calculation.
