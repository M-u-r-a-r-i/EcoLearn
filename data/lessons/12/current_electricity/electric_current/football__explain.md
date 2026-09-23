---
concept_id: electric_current
interest: football
format: explain
title: What the referee's radio is quietly taking from the pack
check:
  question: |-
    A referee's radio draws a steady current of $0.20\,\text{A}$ while it charges. How much charge flows into it in $5$ minutes?
  options:
    A: |-
      $60\,\text{C}$
    B: |-
      $1.0\,\text{C}$
    C: |-
      $0.20\,\text{C}$
    D: |-
      $300\,\text{C}$
  answer: A
  explanation: |-
    Current is charge per second, so $Q = It$. Put the time in seconds first: $5\,\text{minutes} = 300\,\text{s}$, giving $Q = 0.20 \times 300 = 60\,\text{C}$.
  misconceptions:
    B: |-
      Multiplies by $5$ instead of $300$ — the minutes were never converted to seconds. An ampere is one coulomb per *second*.
    C: |-
      Treats the ampere as a fixed amount of charge, so the time seems not to matter. It is a *rate*: the longer it runs, the more charge passes.
    D: |-
      Uses the time alone, as if one coulomb crossed every second. Only $0.20\,\text{C}$ does, so the seconds must be multiplied by the current.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A floodlit football ground at night with two lit pylons, an electronic scoreboard, a fourth official holding a glowing LED substitution board, and a pitch-side distribution box with cables running to the lights](scenes/football/current_electricity.svg "Everything glowing here is being paid for by charge moving round a circuit.")

Half-time at the inter-school final, and the ground is dark except for the pylons and the scoreboard. Rahul and Simran are running the board from a battery pack on a plastic chair behind the goal.

Simran unplugs nothing, reaches over, and clips the referee's radio onto the same pack to top it up.

"Don't," says Rahul. "You'll flatten it before full time."

"It's a radio," she says. "It's tiny. The scoreboard is the big one."

Rahul borrows the groundsman's clamp meter and reads each cable. The scoreboard: $1.5$. The radio: $0.5$. Simran shrugs — the radio is a third of the board, so it can't matter much. Rahul is not convinced, because he suspects those numbers are not sizes at all. They are *speeds*.

Speeds of what, though? What exactly is an ampere counting?

## The physics

A metal wire is already full of **free electrons**, moving about in all directions all the time. That is not a current — the motion is random, so nothing gets anywhere. A current exists only when there is a *net* flow of charge past a point.

**Electric current** is defined as the rate of flow of charge:

$$I = \frac{Q}{t}$$

where $Q$ is the charge in coulombs (C) that crosses a cross-section of the conductor in a time $t$ in seconds (s). The unit is the **ampere**: $1\,\text{A} = 1\,\text{C/s}$. When the flow is not steady, the current at an instant is $I = \dfrac{dQ}{dt}$.

![A wire with one cross-section marked: electrons drift one way while the conventional current arrow points the other way](figures/electric_current/current-as-charge-flow.svg "Choose any one cross-section and count the charge crossing it each second — that number is the current.")

So Rahul is right. "$0.5$" on the clamp meter is not an amount of charge sitting in the radio; it is half a coulomb *every second*, for as long as it stays plugged in. A small current running for a long time can move more charge than a large one running briefly.

Current is a **scalar**, even though we draw arrows for it. The arrow shows the **conventional direction of current**: the direction in which *positive* charge would flow — out of the positive terminal of the pack, round the external circuit, back in at the negative terminal. In a metal the actual carriers are electrons, which are negative, so they drift the opposite way. That mismatch is a leftover from before the electron was known, and we keep it because every circuit rule in your syllabus is written for it.

## Worked example

**Given:** the radio draws a steady $0.5\,\text{A}$, and half-time lasts $15$ minutes.
**Find:** the charge that flows into it.

First put the time in seconds:

$$t = 15 \times 60 = 900\,\text{s}$$

That is the number that matters, because the ampere is counted per second — not per minute.

$$Q = It = 0.5 \times 900 = 450\,\text{C}$$

Four hundred and fifty coulombs have gone round that branch of the circuit during one team talk. The scoreboard, at $1.5\,\text{A}$, has taken three times as much in the same fifteen minutes.

**Sanity check:** the radio's share is not nothing, but it is a quarter of the total, so Rahul's worry is about the hour still to play rather than the break.

## Where the picture breaks

The ground is the setting here, not an analogy — there is no footballing version of charge, and comparing a current to players streaming through a turnstile would quietly teach you something false, because charge does not queue, arrive or get used up. Two honest limits of the model above: a "steady $0.5\,\text{A}$" is an idealisation, since a charging device tapers its current as it fills; and the electrons themselves are never consumed. The same charge goes round and round the loop. What the pack actually supplies, and eventually runs out of, is energy.

## Key takeaway

Current is the rate of flow of charge, $I = Q/t$, measured in amperes — one ampere is one coulomb per second. Rearranged, $Q = It$, so always convert the time to seconds before substituting. The conventional direction of current is the direction positive charge would move, which in a metal is opposite to the electrons' actual drift.
