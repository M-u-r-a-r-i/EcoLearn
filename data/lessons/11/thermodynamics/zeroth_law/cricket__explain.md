---
concept_id: zeroth_law
interest: cricket
format: explain
title: How the physio's thermometer knows your temperature
check:
  question: |-
    During a hot training session, the physio dips a thermometer into water bottle A and waits until the reading is steady: $31\,^\circ\text{C}$. She then dips it into water bottle B and waits: $31\,^\circ\text{C}$ again. Bottle A holds twice as much water as B. What happens if the two bottles are now pressed together, side by side, with thin walls touching?
  options:
    A: |-
      Heat flows from A to B, because A holds more water and so more heat.
    B: |-
      There is no net flow of heat between them; they are already in thermal equilibrium.
    C: |-
      Nothing can be predicted, because the thermometer only ever showed its own temperature.
    D: |-
      Heat flows between them until A and B hold equal amounts of internal energy.
  answer: B
  explanation: |-
    A and B are each in thermal equilibrium with the same thermometer, so by the zeroth law they are in thermal equilibrium with each other: same temperature, no net heat flow. The amount of water does not matter.
  misconceptions:
    A: |-
      Treats heat as something a body stores, so a bigger body "has more heat" to give. Heat flows because of a temperature difference, not because of size.
    C: |-
      Misses the point of the zeroth law: the thermometer reads its own temperature, but once it is in equilibrium with a body, that is the body's temperature too.
    D: |-
      Confuses temperature with internal energy. Equilibrium means equal temperatures; the larger bottle has more internal energy even at the same temperature.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A hot afternoon at a cricket ground: blazing sun, a board showing 38 degrees, a bowler polishing the ball, a generator with hot exhaust and an ice box of drinks](scenes/cricket/thermodynamics.svg "A 38 °C afternoon at the ground: everything here is swapping energy with everything else.")

It's the second session of an under-19 camp, and the board says $38\,^\circ\text{C}$. Ishita, an opening batter, walks off feeling dizzy. The team physio, Farhan, sits her in the shade and slips a digital thermometer under her tongue. "Keep your mouth shut. Wait for the beep."

Ishita waits, and watches the numbers creep up: 35.2, 36.1, 36.8, 37.1. Then they stop, and the beep comes. "Normal," says Farhan. "Just the heat. Drink water."

Ishita is still curious. "That little sensor was in your bag a minute ago. It can only know how hot *it* is. So how does it know how hot *I* am? And why did we have to wait for the number to stop moving?"

It's a sharper question than it sounds. The answer is a law so basic that physicists only noticed they needed it after the first and second laws had already been numbered.

## The physics

When two bodies are put in **thermal contact** — so that heat can pass between them — heat flows from the hotter to the colder. The hotter one cools, the colder one warms, and eventually the flow stops. The two are then in **thermal equilibrium**: their macroscopic properties (pressure, volume, the sensor's reading) no longer change with time.

The **zeroth law of thermodynamics** says:

> Two systems that are each in thermal equilibrium with a third system are in thermal equilibrium with each other.

![Three steps: A in contact with C, then B in contact with C, and finally A and B in contact with no net heat flow](figures/zeroth_law/equilibrium-through-a-third-body.svg "If A and B each match C, they match each other. That shared property is what we call temperature.")

It sounds obvious, but it is not a matter of logic; it is a fact about nature, found by experiment. And it is exactly what makes a thermometer possible.

The zeroth law tells us there is a single property that is equal for all bodies in thermal equilibrium with one another. That property is **temperature**. Two bodies have the same temperature if and only if they are in thermal equilibrium; heat flows from higher to lower temperature.

Now map it onto the story. Ishita is body A. The thermometer is the third body C. While the reading climbs, heat is flowing into the sensor, so it is **not** yet in equilibrium with her and its reading is not her temperature. When the reading stops changing, sensor and mouth are in equilibrium, so they are at the same temperature: $37.1\,^\circ\text{C}$. That is why you wait for the beep. And because every body in equilibrium with a thermometer showing $37.1\,^\circ\text{C}$ is at the same temperature, the number means the same thing for every player Farhan tests.

## Worked example

**Given:** Farhan's thermometer settles at these readings (illustrative): a bottle from the ice box, $4\,^\circ\text{C}$; a can from the same ice box, $4\,^\circ\text{C}$; a towel lying in the sun, $45\,^\circ\text{C}$.
**Find:** what happens when (a) the bottle and can touch, and (b) the can is wrapped in the towel. Express each temperature in kelvin.

(a) Bottle and can are each in equilibrium with the thermometer at the same reading, so by the zeroth law they are in equilibrium with each other: **no net heat flow**, even though their materials and masses differ.

(b) The towel is at a higher temperature than the can, so heat flows **from the towel to the can** until they reach a common temperature somewhere between the two.

In kelvin, $T = t + 273.15$: the ice-box drinks are at $277.15\,\text{K}$ and the towel at $318.15\,\text{K}$, a difference of $41\,\text{K}$, the same as $41\,^\circ\text{C}$.

**Sanity check:** only the temperatures decided the direction of heat flow in both cases; nothing about size or material was needed.

## Where the picture breaks

Real contact is never perfect. A thermometer under the tongue also loses a little heat to the air, so its reading can sit slightly below core body temperature; that is a measurement issue, not a failure of the law. The zeroth law is about the final equilibrium state: it says nothing about how *fast* equilibrium is reached, which is why different thermometers need different waiting times. And the story's "feeling hot" is not a temperature reading at all: your skin senses the rate of heat flow, which is why a metal bench in the sun feels hotter than a wooden bat lying on it, even at the same temperature.

## Key takeaway

Two bodies each in thermal equilibrium with a third are in thermal equilibrium with each other. That shared property is temperature, so a thermometer that has come to equilibrium with a body reads that body's temperature. Heat flows only when temperatures differ.
