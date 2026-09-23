---
concept_id: heat_work_internal_energy
interest: gaming
format: explain
title: Two warm laptops and the question of which one holds heat
check:
  question: |-
    While you play, your laptop's battery does $300\,\text{J}$ of electrical work on the chip and its heat sink, and in the same time the fans carry $260\,\text{J}$ of heat away into the room. What happens to the internal energy of the chip and heat sink, and how much heat do they now hold?
  options:
    A: |-
      It rises by $40\,\text{J}$; they hold internal energy, not heat — "heat" only names energy while it is crossing the boundary.
    B: |-
      It rises by $560\,\text{J}$, because the work put in and the heat moved both add to it.
    C: |-
      It falls by $260\,\text{J}$, because heat leaving a body always lowers its internal energy whatever the work does.
    D: |-
      It rises by $40\,\text{J}$, and they now hold $40\,\text{J}$ of heat, which they will give back when you stop playing.
  answer: A
  explanation: |-
    Energy conservation: $\Delta U = W_\text{on} + Q_\text{in} = +300 + (-260) = +40\,\text{J}$. Once that energy is inside, it is simply internal energy; heat is the name for energy in transit because of a temperature difference, not for something a body stores.
  misconceptions:
    B: |-
      Adds the two magnitudes without signs, missing that the $260\,\text{J}$ *left* the system. Energy that has gone into the room cannot also still be in the chip.
    C: |-
      Looks only at the heat and ignores the work. Both transfers count, and here the work in is larger, so the net change is an increase.
    D: |-
      Gets the arithmetic right but keeps the wrong picture: heat as a substance stored inside. Nothing inside the heat sink records whether its energy arrived as heat or as work.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A gaming desk at night: a monitor showing GPU and CPU temperatures, a tower PC with a heat sink and fans, hot air leaving the top and cool air drawn in, a can of compressed-air duster, a mini fridge under the desk and a backup generator outside the window](scenes/gaming/thermodynamics.svg "Sunlight through the window warms one machine; electricity warms the other. Can you tell them apart afterwards?")

Two identical laptops, one hostel room, one hot afternoon.

Sana's is shut and switched off, left on the windowsill where the sun has been on it since noon. Dhruv's is in the shade on his bed, and it has been running a shooter for the last hour with the fan whining.

At five o'clock their friend Ishita borrows the lab's infrared thermometer and points it at both lids. Same reading, to the nearest degree.

Dhruv is delighted. "Mine's full of *work*," he says. "The battery pushed current through the chip. Yours is full of *heat* — the sun poured it in. Same temperature, completely different stuff inside."

Ishita turns both laptops face down so the stickers don't show, shuffles them, and slides them back across the bed. "Fine. Tell me which is which. Open them, weigh them, measure anything you like."

Dhruv picks one up, turns it over, and stops. Is there *anything* inside a warm object that remembers how it got warm?

## The physics

Everything is made of molecules that jiggle, vibrate and pull on one another. Add up all their kinetic and potential energies, measured in the frame where the object as a whole is at rest, and you have its **internal energy** $U$. A laptop sliding off a table has kinetic energy, but that is not part of $U$; the random jiggling inside it is.

Energy can be put into an object in two distinct ways:

- **Heat** $Q$: energy that crosses the boundary *because of a temperature difference*. The sun's surface is far hotter than the lid, so energy flows in.
- **Work** $W$: energy that crosses by any other means — a force acting through a distance, or a battery driving current through a resistance. Dhruv's battery does electrical work on the chip, and the chip's resistance turns that ordered flow into molecular jiggling.

Energy is conserved, so the change in internal energy is the net heat that flowed in plus the net work done on the object. (You will meet this next as the first law, written with a sign convention.)

![Two routes from State 1 to State 2: left in the sun with 60 J of heat in and no work; rubbed hard with 80 J of work done on it and 20 J of heat lost; both give a change in internal energy of 60 J](figures/heat_work_internal_energy/two-routes-same-state.svg "Different heat, different work, identical change in internal energy. Only U belongs to the state; Q and W belong to the journey.")

Here is the distinction that matters:

- $U$ is a **state variable**. It depends only on the object's present condition — its temperature, pressure, volume and so on — not on its history. Same state, same $U$.
- $Q$ and $W$ are **not** state variables. They describe a *process*: energy crossing a boundary. Once across, both are simply internal energy, and the object keeps no record of the route. Saying a body "contains heat" is as meaningless as asking how much of your bank balance arrived in cash.

That settles Ishita's challenge. Both laptops are in the same state, so they have the same internal energy, and no measurement can recover which route each took.

## Worked example

**Given (illustrative):** warming a metal heat sink from State 1 to State 2 raises its internal energy by $\Delta U = 60\,\text{J}$, by any route. A third route is now tried: a small heating element bonded to the sink does $25\,\text{J}$ of electrical work on it, and the sink still ends up in State 2.
**Find:** the net heat that flowed into the sink along this third route.

Because $U$ is a state variable, the change is $60\,\text{J}$ whatever the route. Energy conservation then splits that between the two transfers:

$$\Delta U = Q_\text{in} + W_\text{on}$$

$$60 = Q_\text{in} + 25 \quad\Rightarrow\quad Q_\text{in} = 35\,\text{J}$$

So $35\,\text{J}$ arrived as heat — a little over half the total. Picture the bonded heater doing about two-fifths of the warming, and the warm air around the sink doing the rest.

**Sanity check:** every route has to add up to the same $60\,\text{J}$, and $35 + 25$ does. The split between heat and work changes from route to route; the total does not.

## Where the picture breaks

Two real laptops are never in *exactly* the same state: the sun warms the lid first and the battery warms the chip first, so the temperature is spread differently inside even when the surfaces match. Give them a few minutes and the difference evens out. The infrared thermometer also reads only the lid's surface, not the whole machine. And the sun heats the lid partly by absorbing light, which is radiation rather than contact — still heat, since it crosses because one body is hotter, but it is worth knowing that heat does not require touching. None of this touches the principle: for the same state, the internal energy is the same.

## Key takeaway

Internal energy $U$ is the molecular energy an object has, and it is a state variable — same state, same value. Heat and work are two *ways of transferring* energy, not things an object holds, and each depends on the route taken. Energy conservation ties them together: $\Delta U$ is the net heat in plus the net work done on the object.
