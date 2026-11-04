---
concept_id: zeroth_law
interest: smartphones
format: explain
title: How a phone knows its own battery is too hot
check:
  question: |-
    Kiran switches off her phone and her tablet and leaves them on a table. She presses the probe of a digital thermometer against the back of the phone and waits until the reading stops changing: $31\,^\circ\text{C}$. She then does the same on the tablet: $31\,^\circ\text{C}$ again. The tablet is much bigger and heavier than the phone. She now stacks the phone on the tablet. What happens?
  options:
    A: |-
      Heat flows from the tablet to the phone, because the bigger tablet holds more heat.
    B: |-
      There is no net flow of heat between them; they are already in thermal equilibrium.
    C: |-
      Heat flows between them until the phone and the tablet hold equal internal energy.
    D: |-
      Nothing can be predicted, because the probe only ever showed its own temperature.
  answer: B
  explanation: |-
    The phone and the tablet are each in thermal equilibrium with the same probe at the same steady reading, so by the zeroth law they are in thermal equilibrium with each other: same temperature, no net heat flow. Their sizes do not matter.
  misconceptions:
    A: |-
      Treats heat as something a body stores, so a bigger body "has more heat" to give away. Heat flows only because of a temperature difference, not because one body is bigger.
    C: |-
      Confuses temperature with internal energy. Equilibrium means equal temperatures; the tablet has more internal energy than the phone even at the same temperature.
    D: |-
      Misses the point of the zeroth law: the probe reads its own temperature, but once it has stopped changing it is in equilibrium with the body, so that is the body's temperature too.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A sunny room: a phone sealed in a puffed-up waterproof pouch on a windowsill, a phone charging on a desk seen through a clip-on thermal camera, an icy can of compressed air, and a wall air conditioner controlled from a phone app](scenes/smartphones/thermodynamics.svg "A room full of gadgets that are all, quietly, measuring or moving heat.")

It's a May afternoon in Jaipur. Tanvi has left her phone on the car's dashboard for an hour while she and her father, Suresh, bought groceries. Back in the car she plugs it in. For a minute it charges happily; then a message appears: *Charging paused. Battery temperature is high.*

"It knows it's hot," says Tanvi. "Clever phone."

Her father, who repairs phones for a living, isn't impressed. "There's a tiny sensor stuck to the battery, a chip whose resistance changes with temperature. That's all."

"So it measures the battery."

"Does it? Think about it. That little chip can only ever report its *own* temperature. It has no idea what the battery is doing. And a minute ago it was happy to charge."

Tanvi frowns at the screen. If a sensor only ever knows itself, how can the phone trust it with the battery's temperature? And why did it change its mind?

## The physics

When two bodies are in **thermal contact**, so that heat can pass between them, heat flows from the hotter to the colder. The hotter one cools, the colder one warms, and eventually the flow stops. The two are then in **thermal equilibrium**: their measurable properties (the sensor's resistance, a gas's pressure) no longer change with time.

The **zeroth law of thermodynamics** says:

> Two systems that are each in thermal equilibrium with a third system are in thermal equilibrium with each other.

![Three steps: A in contact with C, then B in contact with C, and finally A and B in contact with no net heat flow](figures/zeroth_law/equilibrium-through-a-third-body.svg "If A and B each match C, they match each other. That shared property is what we call temperature.")

It sounds too obvious to need saying, but it is a fact about nature found by experiment, not a piece of logic. And it is exactly what makes a thermometer possible.

The law tells us there is one property that is equal for all bodies in thermal equilibrium with each other. That property is **temperature**. Two bodies have the same temperature exactly when they are in thermal equilibrium, and heat flows from higher to lower temperature.

Now map it onto the phone. The battery is body A, and the sensor chip is the third body C. The chip is pressed against the battery, so heat flows between them until they are in equilibrium. Only then does the chip's own temperature equal the battery's. When the phone was first plugged in, the chip had not yet caught up with a battery still heating from the sun, so its reading lagged behind. A few minutes later chip and battery matched, and the phone knew the truth. Any other thermometer that settles against the same battery at the same reading is, by the zeroth law, at the same temperature too, so every reading can be compared with every other.

## Worked example

**Given (illustrative):** after the dashboard, the phone's battery sensor settles at $40\,^\circ\text{C}$. A thermometer probe taped to the power bank beside it also settles at $40\,^\circ\text{C}$. A glass of water on the kitchen counter settles at $25\,^\circ\text{C}$.
**Find:** what happens when (a) the phone touches the power bank, and (b) the phone is laid against the glass. Then give the temperatures in kelvin.

(a) Phone and power bank are each in equilibrium with a thermometer at the same reading, so by the zeroth law they are in equilibrium with each other: **no net heat flow**.

(b) The phone is hotter than the water, so heat flows **from the phone into the water** until both settle at one temperature in between.

In kelvin, $T = t + 273.15$: the phone and power bank are at $313.15\,\text{K}$, and the water at $298.15\,\text{K}$. The gap is $15\,\text{K}$, the same as the gap of $15\,^\circ\text{C}$, because the two scales have the same step size.

**Sanity check:** only the temperatures decided which way heat flowed; nothing about what was inside the phone or the power bank was needed, which is exactly what the zeroth law promises.

## Where the picture breaks

A phone is not one temperature all the way through. While it charges, the charging chip and the battery can be several degrees apart, and the back glass can differ from both; that is why many phones carry more than one sensor. The chip reads the temperature of the battery right where it touches it. And a phone switched on keeps producing heat inside, so it is never quite in equilibrium with the room; its "steady" reading is only steady for a while. None of this breaks the law; it only means real equilibrium is local and temporary. Finally, the zeroth law says nothing about how *fast* equilibrium comes, which is why the sensor lagged at first.

## Key takeaway

Two bodies each in thermal equilibrium with a third are in thermal equilibrium with each other. That shared property is temperature, so a sensor or thermometer that has stopped changing reads the temperature of whatever it is in equilibrium with. Heat flows only when temperatures differ, never because one body is bigger.
