---
concept_id: first_law_thermodynamics
interest: smartphones
format: explain
title: The phone pouch that puffed up in the sun
check:
  question: |-
    A phone sealed in a waterproof pouch is carried from the hot sun into an air-conditioned car. The air inside the pouch gives out $70\,\text{J}$ of heat, and as the pouch shrinks, the outside air does $20\,\text{J}$ of work on it. Using $\Delta Q = \Delta U + \Delta W$, what is the change in internal energy of the air in the pouch?
  options:
    A: |-
      $-90\,\text{J}$
    B: |-
      $-70\,\text{J}$
    C: |-
      $-50\,\text{J}$
    D: |-
      $+90\,\text{J}$
  answer: C
  explanation: |-
    Heat leaves the air, so $\Delta Q = -70\,\text{J}$; work is done on the air, so the work done by it is $\Delta W = -20\,\text{J}$. Then $\Delta U = \Delta Q - \Delta W = -70 - (-20) = -50\,\text{J}$: the air loses internal energy and cools.
  misconceptions:
    A: |-
      Gets the sign of the work wrong, taking $\Delta W = +20\,\text{J}$. In $\Delta Q = \Delta U + \Delta W$, $\Delta W$ is the work done *by* the gas, which is negative when the gas is compressed.
    B: |-
      Ignores the work, as if all the change in internal energy came from heat. The outside air squeezing the pouch adds energy to the air inside, partly making up for the heat lost.
    D: |-
      Treats heat given out as positive, taking $\Delta Q = +70\,\text{J}$. Heat supplied to the system is positive; heat leaving it is negative.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A sunny room: a phone sealed in a puffed-up waterproof pouch on a windowsill, a phone charging on a desk seen through a clip-on thermal camera, an icy can of compressed air, and a wall air conditioner controlled from a phone app](scenes/smartphones/thermodynamics.svg "On the windowsill: a sealed pouch, puffed tight by nothing but sunshine.")

It's the monsoon, and Farhan is off on a college trek to a waterfall near Lonavala. He has sealed his phone inside a clear waterproof pouch, the kind with a roll-top and a clip, and left a pocket of air inside so it would float if he dropped it in the stream.

At the lunch stop the clouds part. He leaves the pouch on a flat rock in the sun while he eats. Twenty minutes later it has puffed up like a pillow, tight enough to drum on.

"The sun blew it up," says his friend Gauri.

"The sun heated the air inside," says Farhan. "That's different."

"Is it? The sun gave the air some energy. The air used it to push the pouch out. So where is the energy now: in the air, or in the push?"

By evening, in the cool shade of the bus, the pouch has gone limp again. Where did the energy go then?

## The physics

The **first law of thermodynamics** is energy conservation applied to heat, work and internal energy. For a system such as the air in the pouch, in NCERT's form:

$$\Delta Q = \Delta U + \Delta W$$

- $\Delta Q$ is the **heat supplied to** the system: positive when heat flows in, negative when heat flows out.
- $\Delta U$ is the **change in internal energy** of the system: positive if it increases.
- $\Delta W$ is the **work done by** the system on its surroundings: positive when the gas expands and pushes, negative when the gas is compressed (work is done on it).

![A cylinder of gas: heat supplied to the gas is Delta Q greater than zero; work done by the gas as it expands is Delta W greater than zero; Delta Q equals Delta U plus Delta W](figures/first_law_thermodynamics/sign-convention.svg "Heat in and work out are positive. Reverse either direction and flip its sign.")

In words: the heat supplied is shared between raising the internal energy and doing work. Rearranged, $\Delta U = \Delta Q - \Delta W$.

Two facts make the law powerful. First, $\Delta U$ depends only on the start and end states: $\Delta Q$ and $\Delta W$ each depend on the path, but their difference does not. Second, for an ideal gas, $U$ depends only on temperature, so the sign of $\Delta U$ tells you whether the gas warmed or cooled.

Some books write the law as $\Delta U = Q + W$ with $W$ the work done **on** the gas. It is the same physics with the opposite sign for work. Pick one convention and keep it; mixing the two is the most common way to get these problems wrong.

So Gauri and Farhan are both partly right. In the sun, heat flows into the air ($\Delta Q > 0$). Part of it goes into pushing the pouch outward against the atmosphere ($\Delta W > 0$), and the rest stays as extra jiggling of the air molecules, a warmer gas ($\Delta U > 0$). In the shade the whole thing runs the other way.

## Worked example

**Given (illustrative):** in the sun, the air in the pouch absorbs $35\,\text{J}$ of heat and does $10\,\text{J}$ of work pushing the pouch out against the atmosphere. In the evening shade it gives out the same $35\,\text{J}$ of heat, and the atmosphere does $10\,\text{J}$ of work squeezing it back.
**Find:** the change in the air's internal energy, in the sun and in the shade.

**Step 1: the signs in the sun.** Heat comes in, so $\Delta Q = +35\,\text{J}$. The air expands and pushes, so $\Delta W = +10\,\text{J}$. That $10\,\text{J}$ is what it takes to push back the atmosphere by about $100\,\text{mL}$, half a cup, which is how much the pouch swelled.

**Step 2: in the sun.**

$$\Delta U = \Delta Q - \Delta W = 35 - 10 = +25\,\text{J}$$

The air keeps $25\,\text{J}$ as internal energy, so it is warmer.

**Step 3: in the shade.** Heat leaves, so $\Delta Q = -35\,\text{J}$; the air is squeezed, so $\Delta W = -10\,\text{J}$:

$$\Delta U = -35 - (-10) = -25\,\text{J}$$

**Sanity check:** the air ends the day back where it started, cool and limp, and the two changes in internal energy cancel exactly, as they must for a return to the same state.

## Where the picture breaks

A real pouch is not a perfect gas cylinder. Its plastic stretches a little, so the pressure inside rises slightly instead of staying at exactly atmospheric; some of the energy goes into the plastic, and the phone and the plastic warm up too. The sunlight heats the pouch unevenly, and water vapour in monsoon air can condense on the inside, which moves energy in a way this simple model ignores. The numbers are round and illustrative, chosen to be consistent with about a litre of air warming by roughly $30\,^\circ\text{C}$; they are not measurements of any real pouch.

## Key takeaway

The first law, $\Delta Q = \Delta U + \Delta W$, says heat supplied to a gas is shared between raising its internal energy and the work it does. Heat in and work done *by* the gas are positive; heat out and work done *on* the gas are negative. Keep the signs straight and the rest is arithmetic.
