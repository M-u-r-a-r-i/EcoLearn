---
concept_id: zeroth_law
interest: gaming
format: explain
title: Why the probe on your heat sink has to stop climbing
check:
  question: |-
    Rehan tapes a probe thermometer to his PC's heat sink and watches the reading: $31$, $44$, $52$, $58$, $61$, $61$, $61\,^\circ\text{C}$. Which statement is correct?
  options:
    A: |-
      Because the probe was touching the sink the whole time, every reading on the way up was the heat sink's temperature too.
    B: |-
      The steady reading is an average of the probe's temperature and the sink's, so the sink is really hotter than $61\,^\circ\text{C}$.
    C: |-
      Only the steady reading is the heat sink's temperature: while it was climbing, probe and sink were not yet in thermal equilibrium.
    D: |-
      A probe can only ever show its own temperature, so $61\,^\circ\text{C}$ tells you nothing about the heat sink.
  answer: C
  explanation: |-
    A thermometer reads a body's temperature only once the two have stopped exchanging net heat — that is, once they are in thermal equilibrium. The zeroth law says they then share one property, temperature, which is what the steady reading gives you.
  misconceptions:
    A: |-
      Assumes contact alone is enough. Contact only starts the heat flow; until the flow stops, the probe is at its own lower temperature and its reading is nobody's temperature but its own.
    B: |-
      Imagines the reading settles halfway between the two bodies. At equilibrium there is no "halfway": both bodies are at one common temperature, and that is what the probe shows.
    D: |-
      Denies the zeroth law. It is true that the probe shows its own temperature — but once probe and sink are in equilibrium, that *is* the sink's temperature.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A gaming desk at night: a monitor showing GPU and CPU temperatures, a tower PC with a heat sink and fans, hot air leaving the top and cool air drawn in, a can of compressed-air duster, a mini fridge under the desk and a backup generator outside the window](scenes/gaming/thermodynamics.svg "Every number about temperature on this desk came from something touching something else and waiting.")

Rehan's new PC has been running a racing game for an hour, and the overlay in the corner of the screen says the graphics chip is at $78\,^\circ\text{C}$. His cousin Meghna is not impressed. "That's a number the software invented. Put your hand on the case. It's barely warm."

So Rehan opens the side panel, tapes the tip of a cheap kitchen probe thermometer flat against the metal heat sink, and restarts the game. The probe reads 31. Then 44. Then 52, 58, 61.

Then it stops. It sits at $61\,^\circ\text{C}$ and will not move.

"See," says Meghna. "Your software says 78. Your probe says 61. One of them is lying."

"They're touching different things," says Rehan.

Meghna is stuck on something else, and it is the better question. That probe can only ever know how hot *the probe* is. So how does it tell you how hot anything else is — and why did they have to sit there waiting for the number to stop climbing?

## The physics

Put two bodies in **thermal contact**, so heat can pass between them, and heat flows from the hotter to the colder. The hot one cools, the cold one warms, and after a while the flow stops. The two are then in **thermal equilibrium**: their measurable properties — pressure, volume, a sensor's reading — stop changing with time.

The **zeroth law of thermodynamics** says:

> Two systems that are each in thermal equilibrium with a third system are in thermal equilibrium with each other.

![Three steps: A in contact with C, then B in contact with C, and finally A and B in contact with no net heat flow](figures/zeroth_law/equilibrium-through-a-third-body.svg "If A and B each settle at the same reading on C, they settle with each other too. That shared property is what we call temperature.")

This sounds too obvious to need stating, but it is not a matter of logic — it is a fact about nature, established by experiment. It is also exactly what makes a thermometer possible.

The law tells us there is a single property shared by all bodies that are in thermal equilibrium with one another. We call that property **temperature**. Two bodies are at the same temperature if and only if they are in thermal equilibrium, and heat flows from higher temperature to lower.

Now map it onto Rehan's desk. The heat sink is body A; the probe is the third body, C. While the reading climbs, heat is still flowing into the probe, so it is **not** yet in equilibrium with the sink, and $44\,^\circ\text{C}$ is the probe's temperature and nothing else's. When the reading stops moving, probe and sink are in equilibrium, so they share one temperature: $61\,^\circ\text{C}$. That is why you wait. And because every body in equilibrium with a probe reading $61\,^\circ\text{C}$ is at the same temperature, the number means the same thing on the next machine Rehan tests.

## Worked example

**Given (illustrative):** at a gaming café, the same probe is left on PC A until steady — $40\,^\circ\text{C}$ — and then on PC B until steady — $40\,^\circ\text{C}$ again. PC A's case is far bigger than PC B's. A can taken from the mini fridge settles at $10\,^\circ\text{C}$.
**Find:** what happens when (a) the two cases are pushed together, and (b) the can is stood on PC B; and give both temperatures in kelvin.

(a) Each case was separately in equilibrium with the probe at the same reading. By the zeroth law they are therefore in equilibrium with each other: **no net heat flows** when they touch. The difference in size makes no difference at all.

(b) The can is colder, so heat flows **from the case into the can**, until both reach a common temperature somewhere between $10\,^\circ\text{C}$ and $40\,^\circ\text{C}$.

In kelvin, $T = t + 273.15$, so the cases are at $313.15\,\text{K}$ and the can at $283.15\,\text{K}$ — a gap of $30\,\text{K}$, the same size as a gap of $30\,^\circ\text{C}$.

**Sanity check:** only the two temperatures decided which way heat went. Nothing about how big or how heavy anything was ever entered the argument, which is what you would expect if temperature alone sets the direction.

## Where the picture breaks

Tape and a probe tip make imperfect contact, with a thin film of air in the gap, so a real probe usually settles a little below the surface it is measuring. That is a measurement problem, not a failure of the law. The law also says nothing about *how long* equilibrium takes — a heavy heat sink takes minutes, a thin wire takes seconds. And the $78\,^\circ\text{C}$ on screen is not a rival reading: it comes from a sensor built into the silicon, a different body a few millimetres away with heat flowing steadily through the gap between them. Bodies with heat flowing between them are not in equilibrium, so there is no reason for them to match. Finally, "the case feels barely warm" is not a temperature measurement at all — your skin senses how fast heat enters it, which is why bare metal at $40\,^\circ\text{C}$ feels far hotter than the plastic beside it.

## Key takeaway

Two bodies each in thermal equilibrium with a third are in thermal equilibrium with each other. The property they share is temperature, so a thermometer that has come to equilibrium with a body reads that body's temperature — and only then. Heat flows only when temperatures differ.
