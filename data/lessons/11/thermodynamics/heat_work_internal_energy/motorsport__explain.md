---
concept_id: heat_work_internal_energy
interest: motorsport
format: explain
title: Two hot brake discs and the question of which one holds heat
check:
  question: |-
    Two identical brake discs start at the same temperature. Disc X is warmed in a workshop oven: it absorbs $300\,\text{kJ}$ of heat and no work is done on it. Disc Y is on a car: the brake pads' friction does $500\,\text{kJ}$ of work on it, and it loses $200\,\text{kJ}$ of heat to the cooling air. Which statement is correct?
  options:
    A: |-
      Both gained $300\,\text{kJ}$ of internal energy; heat and work describe the transfers, not what the discs contain.
    B: |-
      Disc Y has more internal energy than X, because $500\,\text{kJ}$ of work went into it.
    C: |-
      Disc X now contains more heat than disc Y, because only X was heated.
    D: |-
      Their internal energies cannot be equal, because the heat and work were so different.
  answer: A
  explanation: |-
    Energy conservation: X gains $300\,\text{kJ}$; Y gains $500 - 200 = 300\,\text{kJ}$. Both reach the same state with the same internal energy. Heat and work are energy in transit, so neither disc "contains" heat or work.
  misconceptions:
    B: |-
      Counts the work done on Y but forgets the $200\,\text{kJ}$ that Y lost as heat; only the net energy gained changes the internal energy.
    C: |-
      Treats heat as something stored inside a body. Once transferred, heat becomes internal energy, and nothing in the disc records how it arrived.
    D: |-
      Thinks internal energy depends on the route taken. It is a state variable: the same state always has the same internal energy.
author: claude-code/opus-5
written: 2026-09-25
---
## The story

![A pit lane in the afternoon sun: a stack of tyres in electric tyre blankets with a probe thermometer, a race car with a glowing front brake disc and a hot exhaust, and a compressed-air bottle feeding a wheel gun](scenes/motorsport/thermodynamics.svg "In the middle: a brake disc glowing after hard braking. Nothing burned; the car's motion did that.")

At a track-day workshop, the chief mechanic, Joseph, sets two identical iron brake discs on the bench. One has just come off a car after five hard laps. The other has been sitting in the paint-curing oven at the back of the workshop.

He points an infrared thermometer at each. Both read exactly the same.

Riya, who has come along to watch her brother drive, is sure she can explain it. "The oven one is full of heat. The car one is full of work, because the brake pads were rubbing on it. Same temperature, different stuff inside."

Joseph grins, puts on thick gloves, and swaps the two discs behind his back. "Then tell me which is which. Weigh them, measure them, test them any way you like."

Riya looks at the two discs. Is there *anything* inside a lump of iron that remembers how it got hot?

## The physics

Every body is made of molecules that jiggle, vibrate and pull on each other. The total of their kinetic and potential energies, measured in the frame where the body as a whole is at rest, is its **internal energy** $U$. A disc spinning on a moving car also has kinetic energy as a whole, but that is not part of $U$; the random jiggling of its atoms is.

Energy can be added to a body in two different ways:

- **Heat** $Q$: energy transferred because of a temperature difference. The oven's air is hotter than the disc, so energy flows in.
- **Work** $W$: energy transferred by other means, such as a force acting through a distance. The pads press on the spinning disc, and their friction force acts through a distance along its surface; that turns the car's motion into atomic jiggling.

Energy is conserved, so the change in internal energy equals the heat that came in plus the work done on the body. (You will soon meet this as the first law, with a sign convention.)

![Two routes from State 1 to State 2: left in the sun with 60 J of heat in and no work; rubbed hard with 80 J of work done and 20 J of heat lost; both give a change in internal energy of 60 J](figures/heat_work_internal_energy/two-routes-same-state.svg "Different amounts of heat and work, the same change in internal energy. Only U belongs to the state.")

Here is the key distinction:

- $U$ is a **state variable**. It depends only on the body's present condition (its temperature, pressure, volume and so on), not on its history. Same state means same $U$.
- $Q$ and $W$ are **not** state variables. They describe a *process*: energy crossing the boundary. Once across, both simply become internal energy, and the body keeps no record of the route. Saying a disc "contains heat" or "contains work" is meaningless, the way a fuel tank does not remember which pump filled it.

That answers Riya. The two discs are in the same state, so they have the same internal energy, and no test can reveal which route each one took.

## Worked example

**Given (illustrative):** in the oven, a disc takes in $300\,\text{kJ}$ of heat with no work done on it, and ends in a hot state we'll call State 2. A second, identical disc starts at the same temperature and is heated on track: the pads do $400\,\text{kJ}$ of work on it, and it ends in exactly State 2.
**Find:** the heat that flowed between the on-track disc and the air.

**Step 1: the change in internal energy.** $U$ is a state variable and both discs go from the same start to the same finish, so for both,

$$\Delta U = 300\,\text{kJ}$$

**Step 2: the heat.** Energy conservation says $\Delta U = Q_\text{in} + W_\text{on}$, so

$$Q_\text{in} = \Delta U - W_\text{on} = 300 - 400 = -100\,\text{kJ}$$

The minus sign means the heat flowed *out*: the disc lost $100\,\text{kJ}$ to the rushing air while the pads were pumping in $400\,\text{kJ}$. That lost heat is why racing brakes have cooling ducts.

**Sanity check:** the oven route $(Q, W_\text{on}) = (300, 0)$ and the track route $(-100, 400)$ each add up to $300\,\text{kJ}$: the heat and the work changed, their sum did not.

## Where the picture breaks

The numbers are illustrative, not measured on any real car. On track, a disc's heating is not one clean step: it heats sharply at every braking zone and cools on every straight. Friction heats the pads as well as the disc, so not all of the pads' work ends up in the disc. And a brake disc worn by a race is not quite identical to a fresh one, because a little material has been ground away. The principle survives all of this: bodies in the same state have the same internal energy, whatever route got them there.

## Key takeaway

Internal energy $U$ is the energy of a body's jiggling molecules, and it is a state variable. Heat and work are two ways of *transferring* energy, not things a body holds, and their amounts depend on the route. Energy conservation links them: $\Delta U$ equals the net heat in plus the net work done on the body.
