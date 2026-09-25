---
concept_id: zeroth_law
interest: motorsport
format: explain
title: Why the tyre engineer waits for the probe to settle
check:
  question: |-
    In the garage, a tyre engineer pushes her probe thermometer into tyre P and waits until the reading is steady: $80\,^\circ\text{C}$. She then probes tyre Q and waits: $80\,^\circ\text{C}$ again. Tyre Q is a wider rear tyre with much more rubber than P. The two tyres are now stacked so that they press against each other. What happens?
  options:
    A: |-
      Heat flows from Q to P, because the wider tyre holds more rubber and so more heat.
    B: |-
      Nothing can be predicted, because the probe only ever showed its own temperature.
    C: |-
      There is no net flow of heat between them; they are already in thermal equilibrium.
    D: |-
      Heat flows between them until P and Q hold equal amounts of internal energy.
  answer: C
  explanation: |-
    P and Q are each in thermal equilibrium with the same probe, so by the zeroth law they are in thermal equilibrium with each other: same temperature, no net heat flow. The amount of rubber does not matter.
  misconceptions:
    A: |-
      Treats heat as something a body stores, so a bigger body "has more heat" to give. Heat flows only because of a temperature difference, not because of size.
    B: |-
      Misses the point of the zeroth law: the probe reads its own temperature, but once it is in equilibrium with a tyre, that is the tyre's temperature too.
    D: |-
      Confuses temperature with internal energy. Equilibrium means equal temperatures; the bigger tyre has more internal energy even at the same temperature.
author: claude-code/opus-5
written: 2026-09-25
---
## The story

![A pit lane in the afternoon sun: a stack of tyres in electric tyre blankets with a probe thermometer, a race car with a glowing front brake disc and a hot exhaust, and a compressed-air bottle feeding a wheel gun](scenes/motorsport/thermodynamics.svg "On the left: tyres cooking in their blankets, and the probe that says how hot they really are.")

Twenty minutes before qualifying, and Nandini, a tyre engineer in her first season, is doing her rounds. Each set of tyres sits wrapped in an electric blanket, warming up so the driver has grip from the first corner. Her job: check that every tyre is at the target temperature before it goes on the car.

Her trainee, Aarav, watches her push the needle of a probe thermometer into a tyre's tread. The display climbs: 41, 58, 69, 76, 79, 80. Then it stops. Only then does Nandini write the number down.

"Why wait?" Aarav asks. "It showed 76 ages ago. Close enough."

"Not close enough," says Nandini. "Tell me this, then. That little needle was cold in my pocket ten seconds ago. It can only ever know its own temperature. So how can it tell me anything about the tyre?"

Aarav opens his mouth, then closes it again.

## The physics

When two bodies are in **thermal contact**, so that heat can pass between them, heat flows from the hotter to the colder. The hotter one cools, the colder one warms, and eventually the flow stops. The two are then in **thermal equilibrium**: their measurable properties (pressure, volume, the probe's reading) no longer change with time.

The **zeroth law of thermodynamics** says:

> Two systems that are each in thermal equilibrium with a third system are in thermal equilibrium with each other.

![Three steps: A in contact with C, then B in contact with C, and finally A and B in contact with no net heat flow](figures/zeroth_law/equilibrium-through-a-third-body.svg "If A and B each match C, they match each other. That shared property is what we call temperature.")

It sounds too obvious to need saying, but it is a fact about nature found by experiment, not a piece of logic. And it is what makes a thermometer possible.

The law tells us there is one property that is equal for all bodies in thermal equilibrium with each other. That property is **temperature**. Two bodies have the same temperature exactly when they are in thermal equilibrium, and heat flows from higher to lower temperature.

Now map it onto the pit garage. The tyre is body A, and the probe is the third body C. While the display climbs, heat is still flowing from the rubber into the needle, so the two are **not** in equilibrium and the number is not yet the tyre's temperature. That is why $76\,^\circ\text{C}$ was not good enough. When the reading stops changing, needle and tyre are in equilibrium, so they share a temperature: $80\,^\circ\text{C}$. And because every tyre that brings the same probe to the same steady reading is at the same temperature, Nandini's numbers can be compared across all four corners of the car.

## Worked example

**Given (illustrative):** the probe settles at $80\,^\circ\text{C}$ in a front tyre and at $80\,^\circ\text{C}$ in a rear tyre, both fresh from their blankets. A spare tyre left in the shade settles at $35\,^\circ\text{C}$.
**Find:** what happens when (a) the front and rear tyres touch, and (b) the spare is stacked on the front tyre. Then give the temperatures in kelvin.

(a) Both tyres are in equilibrium with the probe at the same reading, so by the zeroth law they are in equilibrium with each other: **no net heat flow**, even though the rear tyre is bigger.

(b) The front tyre is hotter than the spare, so heat flows **from the front tyre into the spare** until they settle at one temperature somewhere in between.

In kelvin, $T = t + 273.15$: the warm tyres are at $353.15\,\text{K}$ and the spare at $308.15\,\text{K}$. The gap is $45\,\text{K}$, exactly the same as the gap of $45\,^\circ\text{C}$, because the two scales have the same step size.

**Sanity check:** only the temperatures decided which way heat flowed; nothing about the tyres' size was needed, which is exactly what the zeroth law promises.

## Where the picture breaks

A real tyre is not one temperature all the way through. The surface, the inner tread and the side of the tyre can differ by several degrees, which is why engineers probe more than one spot. The probe's reading is the temperature of the rubber right around the needle. And while Nandini waits, the tyre, now out of its blanket, is already losing heat to the air, so the "steady" reading is steady only for a short while. None of this breaks the law; it only means real equilibrium is local and temporary. Finally, the zeroth law says nothing about how *fast* equilibrium comes, which is why different probes need different waits.

## Key takeaway

Two bodies each in thermal equilibrium with a third are in thermal equilibrium with each other. That shared property is temperature, so a thermometer that has stopped changing reads the temperature of whatever it is in equilibrium with. Wait for the reading to settle. Heat flows only when temperatures differ.
