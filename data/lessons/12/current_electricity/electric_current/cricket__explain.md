---
concept_id: electric_current
interest: cricket
format: explain
title: What the battery on the practice floodlight is counting
check:
  question: |-
    A small camera mounted in the stumps draws a steady current of $0.50\,\text{A}$. How much charge passes through it in one minute?
  options:
    A: |-
      $0.0083\,\text{C}$
    B: |-
      $30\,\text{C}$
    C: |-
      $0.50\,\text{C}$
    D: |-
      $1800\,\text{C}$
  answer: B
  explanation: |-
    Current is charge per unit time, so $Q = It = 0.50\,\text{A} \times 60\,\text{s} = 30\,\text{C}$.
  misconceptions:
    A: |-
      Divides the current by the time instead of multiplying. $I = Q/t$ rearranges to $Q = It$, not $Q = I/t$.
    C: |-
      Treats the ampere as an amount of charge. An ampere is one coulomb *per second*, so the time it runs matters.
    D: |-
      Uses $3600\,\text{s}$ — an hour, not a minute. The time must be converted to seconds, but to the right number of them.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A cricket ground at dusk with floodlights, an electronic scoreboard, glowing stumps and an umpire holding a light meter](scenes/cricket/current_electricity.svg "Dusk at the ground: the scoreboard, the stump lights and the floodlights all run on batteries and circuits.")

Winter nets, and it gets dark by six. Nikhil's school buys one portable LED floodlight for the practice pitch — a lamp on a stand with a battery pack bolted underneath. Printed on the pack is a label nobody in the team can read properly: **12 V, 7 Ah**.

"Seven hours," says the captain, Devika, confidently. "It says seven. We can bat till one in the morning."

They switch it on at six. By quarter past nine the lamp browns out and dies. Three and a quarter hours, not seven.

Devika is annoyed — did the shop sell them a dud? Nikhil turns the pack over and finds one more line in small print: the lamp draws about two amperes.

Nothing is faulty. The label was never promising hours; it was promising something else, and the lamp's own appetite decides how many hours that becomes. What exactly is an ampere counting?

## The physics

A metal wire is full of **free electrons** that already move about randomly, in all directions, all the time. That is not a current. A current exists only when there is a *net* flow of charge past a point.

**Electric current** is defined as the rate of flow of charge:

$$I = \frac{Q}{t}$$

where $Q$ is the charge (in coulombs, C) that passes through a cross-section of the conductor in time $t$ (in seconds, s). The unit is the **ampere**: $1\,\text{A} = 1\,\text{C/s}$. When the flow is not steady, the current at an instant is $I = \dfrac{dQ}{dt}$.

![A wire with a marked cross-section: electrons drift to the left while the conventional current arrow points to the right](figures/electric_current/current-as-charge-flow.svg "Pick one cross-section of the wire and count the charge crossing it each second — that number is the current.")

Current is a **scalar**, even though we draw it with an arrow. The arrow tells you the **conventional direction of current**: the direction in which *positive* charge would flow — out of the positive terminal of the cell, round the external circuit, back into the negative terminal. In a metal the actual carriers are electrons, which are negative, so they drift the *opposite* way. That mismatch is a historical accident from before the electron was discovered, and we keep it because every circuit rule is written for it.

So the lamp's "2 A" means two coulombs of charge pass through its LEDs every second. And the pack's "7 Ah" is an amount of *charge*: amperes multiplied by hours. Divide it by how fast the lamp drains charge, and you get the running time.

## Worked example

**Given:** the floodlight draws a steady $2\,\text{A}$; the battery pack stores $7\,\text{A\,h}$ of charge.
**Find:** the charge that flows in the first $5$ minutes, and roughly how long the pack can last.

First put the time in seconds: $5\,\text{minutes} = 300\,\text{s}$.

$$Q = It = 2\,\text{A} \times 300\,\text{s} = 600\,\text{C}$$

Six hundred coulombs have gone round the circuit in five minutes — and *that* is the quantity the battery's rating is a store of.

Now the running time. The pack holds $7\,\text{A\,h}$, and the lamp takes charge at $2\,\text{A}$:

$$t = \frac{7\,\text{A\,h}}{2\,\text{A}} = 3.5\,\text{hours}$$

About three and a half hours — which is what the team actually got. A real pack does a little worse, because its voltage sags as it empties.

**Sanity check:** a lamp twice as hungry should empty the same pack in half the time, and it does — the hours came out as the rating divided by the current, not equal to the rating.

## Where the picture breaks

The cricket ground here is the setting, not an analogy — there is no "cricketing" version of charge, and pretending a current is like fielders running singles would teach you something false. Two honest limits of the model above: an ampere-hour is only an approximate measure of stored charge, because a battery's usable capacity falls when you draw current fast or when it is cold; and the "steady 2 A" is an idealisation, since LEDs draw slightly less as the pack's voltage drops. Also, charge is never used up. The same electrons go round and round; the battery supplies energy, not charge that vanishes into the lamp.

## Key takeaway

Current is the rate of flow of charge, $I = Q/t$, measured in amperes — one ampere is one coulomb per second. Its conventional direction is the direction positive charge would move, which in a metal is opposite to the electrons' actual drift. A battery rated in ampere-hours is telling you how much charge it can push round, so the current drawn decides how long it lasts.
