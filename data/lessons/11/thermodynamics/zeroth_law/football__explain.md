---
concept_id: zeroth_law
interest: football
format: explain
title: Two recovery tubs and one thermometer
check:
  question: |-
    After training, a physio dips her thermometer into a large recovery tub and waits until the reading stops changing: $12\,^\circ\text{C}$. She dries it, dips it into a small tub, and waits again: $12\,^\circ\text{C}$. The large tub holds four times as much water. What can she conclude?
  options:
    A: |-
      The large tub is colder, because it holds four times as much chilled water.
    B: |-
      Heat will flow from the large tub to the small one until the two hold equal internal energy.
    C: |-
      Both tubs are at the same temperature, so connecting them would give no net flow of heat.
    D: |-
      Nothing can be concluded, because the thermometer only ever shows its own temperature.
  answer: C
  explanation: |-
    Each tub is in thermal equilibrium with the same thermometer at the same reading, so by the zeroth law the two tubs are in thermal equilibrium with each other: same temperature, no net heat flow. How much water each holds makes no difference.
  misconceptions:
    A: |-
      Treats "cold" as a substance a body stores, so more water means more cold. Temperature does not depend on how much there is; the large tub holds more internal energy at the very same temperature.
    B: |-
      Confuses temperature with internal energy. Heat flows because of a temperature difference, and equal temperatures already mean no net flow; equilibrium never requires equal amounts of internal energy.
    D: |-
      Misses what the zeroth law buys you. The thermometer does read its own temperature, but once the reading has stopped changing it is in equilibrium with the water, so that is the water's temperature too.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A training ground on a hot day: a board reading 36 degrees Celsius, an ice box of drinks, a player inflating a ball with a hand pump, and a mower with a hot exhaust](scenes/football/thermodynamics.svg "A 36 °C session. Everything in this picture is quietly swapping energy with everything else.")

The board at the training ground says $36\,^\circ\text{C}$, and the session has just finished. Behind the goal stand two recovery tubs, both filled that morning from the same chilled-water tank: a big blue barrel and a small round tub beside it.

Rohit gets to the barrel first. "Bigger tub, more cold water," he tells Sana. "This one's colder. You're getting the warm one."

Meenakshi, the physio, doesn't argue. She takes the digital probe from her bag, drops it into the barrel and waits. The numbers climb the other way: 31, 24, 17, 13, 12. They stop. She wipes the probe, drops it into the small tub, and waits again. 12.

Rohit stares at it. "That thing was in your bag two minutes ago. It can only know how hot *it* is. So how does it know anything about my water — and why did we have to stand here waiting?"

## The physics

Put two bodies in **thermal contact**, so heat can pass between them, and heat flows from the hotter to the colder. The hotter cools, the colder warms, and the flow eventually stops. The pair are then in **thermal equilibrium**: their measurable properties — pressure, volume, a probe's reading — stop changing with time.

The **zeroth law of thermodynamics** says:

> Two systems that are each in thermal equilibrium with a third system are in thermal equilibrium with each other.

![Three steps: A in contact with C, then B in contact with C, and finally A and B in contact with no net heat flow](figures/zeroth_law/equilibrium-through-a-third-body.svg "If A and B each match C, they match each other. That shared property is what we call temperature.")

It sounds like something you could prove by pure logic, but you cannot: it is a fact about nature, established by experiment. It is also exactly what makes a thermometer possible.

The law tells us there is one property that is the same for all bodies in thermal equilibrium with one another. We call that property **temperature**. Two bodies are at the same temperature if and only if they are in thermal equilibrium, and heat flows from higher temperature to lower.

Now map it onto the tubs. The barrel is body A, the small tub is body B, and the probe is the third body C. While the reading falls, heat is still flowing out of the probe, so it is **not** yet in equilibrium and its number is not the water's temperature. When the reading settles, probe and water are in equilibrium and share a temperature: $12\,^\circ\text{C}$. That is why Meenakshi waits. And because both tubs settled the probe at the same reading, the zeroth law says they would be in equilibrium with each other — Rohit's barrel is not one degree colder than Sana's tub.

## Worked example

**Given:** the probe settles at $12\,^\circ\text{C}$ in both tubs, and at $36\,^\circ\text{C}$ in a water bottle that was left on the touchline in the sun.
**Find:** which way heat flows when the sealed bottle is dropped into the small tub, and the temperature difference in kelvin.

The bottle is at the higher temperature, so heat flows **from the bottle into the tub water**, and keeps flowing until they reach one common temperature between $12\,^\circ\text{C}$ and $36\,^\circ\text{C}$.

Convert with $T = t + 273.15$:

$$12\,^\circ\text{C} \approx 285\,\text{K}, \qquad 36\,^\circ\text{C} \approx 309\,\text{K}$$

The difference is $309 - 285 = 24\,\text{K}$ — the same size as the $24\,^\circ\text{C}$ difference, because a kelvin and a degree Celsius are the same size of step; only the zero is moved.

**Sanity check:** nothing about the amount of water entered the reasoning, and it never should — only the two temperatures decide which way heat goes.

## Where the picture breaks

Real tubs are not perfectly uniform: the water near the top is warmer than the water at the bottom, which is why physios stir a tub before reading it. The zeroth law describes the final equilibrium only; it says nothing about how *long* reaching it takes, which is why a probe in still water needs longer than a probe in stirred water. And "feeling cold" is not a temperature reading at all: your skin senses how fast heat leaves it, so water at $12\,^\circ\text{C}$ feels far colder than air at $12\,^\circ\text{C}$, even though a thermometer settles at the same number in both.

## Key takeaway

Two bodies each in thermal equilibrium with a third are in thermal equilibrium with each other. The property they share is temperature, which is why a thermometer that has stopped changing reads the temperature of whatever it is touching. Heat flows only when temperatures differ — never because one body is bigger.
