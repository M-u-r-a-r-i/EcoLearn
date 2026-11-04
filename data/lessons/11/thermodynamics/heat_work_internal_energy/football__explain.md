---
concept_id: heat_work_internal_energy
interest: football
format: explain
title: The warm match ball nobody could tell apart
check:
  question: |-
    Two identical match balls start at the same temperature. Ball P lies in the sun and absorbs $40\,\text{J}$ of heat, with no work done on it. Ball Q is used for shooting practice: $60\,\text{J}$ of work is done in squashing and reshaping it, and it loses $20\,\text{J}$ of heat to the moving air. Which statement is correct?
  options:
    A: |-
      Both balls end with the same internal energy, $40\,\text{J}$ above where they started.
    B: |-
      Ball Q has the greater internal energy, because $60\,\text{J}$ of work was done on it.
    C: |-
      Ball P now holds more heat than ball Q, because only P was heated.
    D: |-
      Their internal energies cannot be equal, because the transfers were so different.
  answer: A
  explanation: |-
    Energy conservation: P gains $40\,\text{J}$; Q gains $60 - 20 = 40\,\text{J}$. Both reach the same state with the same internal energy. Heat and work are energy in transit, so neither ball "holds" heat or work afterwards.
  misconceptions:
    B: |-
      Counts the work done on Q but forgets the $20\,\text{J}$ that left it as heat. What changes the internal energy is the net of the two transfers.
    C: |-
      Treats heat as something a body stores. Once it has crossed the boundary, heat becomes internal energy, and nothing in the ball records how it arrived.
    D: |-
      Thinks internal energy depends on the route taken. It is a state variable: the same state always carries the same internal energy, whatever mixture of heat and work produced it.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A training ground on a hot day: a board reading 36 degrees Celsius, an ice box of drinks, a player inflating a ball with a hand pump, and a mower with a hot exhaust](scenes/football/thermodynamics.svg "One ball out on the hot touchline, another being hammered at the goal: two ways to warm the same object.")

Bhavna, who runs the kit for a district academy, sets up a small argument on purpose. She takes two brand-new balls out of the same box. One she leaves lying on the touchline in the sun. The other she throws to Arjun with one instruction: twenty minutes of shooting, as hard as he likes.

At the end of it she points the infrared thermometer at both. The readings are within a tenth of a degree of each other.

Zoya, watching from the bench, has a theory ready. "Easy. The touchline ball is full of heat. Arjun's ball is full of work. Same temperature, different stuff inside."

Bhavna turns her back, swaps the balls between her hands a few times, and holds them out. "Then tell me which is which. Cut them open if you want."

Zoya squeezes both, smells the leather, frowns. Is there anything inside a ball that remembers how it got warm?

## The physics

A ball is made of molecules that jiggle, stretch and pull on each other. The total kinetic and potential energy of all those molecules, measured in the frame where the ball as a whole is at rest, is its **internal energy** $U$. A ball flying at $20\,\text{m/s}$ has kinetic energy too, but that belongs to the ball's motion as a whole, not to $U$. Only the random, internal jiggling counts.

There are two ways to push energy across the boundary into the ball:

- **Heat** $Q$: energy transferred because of a temperature difference. The sun is vastly hotter than the ball, so energy flows in.
- **Work** $W$: energy transferred by a force acting through a distance. Arjun's boot squashes the ball by several centimetres on every strike and it springs back — but not perfectly. Some of the work spent deforming the casing and the air inside stays behind as molecular jiggling.

Energy is conserved, so the change in internal energy equals the heat that flowed in plus the work done on the ball. (You will meet this shortly as the first law, written with a sign convention.)

![Two routes from State 1 to State 2: left in the sun with 60 J of heat in and no work; rubbed hard with 80 J of work done and 20 J of heat lost; both give a change in internal energy of 60 J](figures/heat_work_internal_energy/two-routes-same-state.svg "Different amounts of heat and work, the same change in internal energy. Only U belongs to the state.")

Here is the distinction that Zoya is missing:

- $U$ is a **state variable**. It depends only on the ball's present condition — its temperature, pressure, volume — and not at all on its history. Same state, same $U$.
- $Q$ and $W$ are **not** state variables. They describe a *process*: energy crossing the boundary. Once across, both become internal energy, indistinguishable from each other. Saying a ball "contains heat" or "contains work" means nothing, the same way a bank balance does not remember which notes were cash and which were transfers.

So no test can separate the two balls. They are in the same state, so they have the same internal energy.

## Worked example

**Given:** going from the morning's cool state to the state both balls are in now is a rise of $60\,\text{J}$ in internal energy (illustrative). A third ball reaches that same state by being kicked about in a cool evening breeze, during which it loses $15\,\text{J}$ of heat to the air.
**Find:** the work done on that third ball.

Because $U$ is a state variable, the same two end states mean the same change, whatever the route:

$$\Delta U = +60\,\text{J}$$

Energy conservation says that change is the net of what came in and what left:

$$\Delta U = Q_\text{in} + W_\text{on} \quad\Rightarrow\quad 60 = (-15) + W_\text{on}$$

So $W_\text{on} = 60 + 15 = 75\,\text{J}$. The kicking had to supply the $60\,\text{J}$ that stayed *and* replace the $15\,\text{J}$ the breeze carried off.

**Sanity check:** the breeze is working against you, so the kicking must do more than $60\,\text{J}$ — and $75\,\text{J}$ is more. About $75\,\text{J}$ is also roughly the energy of one firmly struck ball in flight, so a few dozen kicks losing a small share each is the right size of effect.

## Where the picture breaks

Most of the work your boot does on a ball goes into its flight, not into warming it; only the part lost to internal friction in the casing and the air stays as internal energy. The numbers here are illustrative for that reason. Real balls are also never quite identical — a used ball's leather is scuffed differently — and both balls keep exchanging heat with the air throughout, so neither route is as clean as the diagram. None of that touches the principle: reach the same state, and the internal energy is the same.

## Key takeaway

Internal energy $U$ is the random molecular energy a body holds, and it is a state variable. Heat and work are two ways of *transferring* energy across a boundary, not things a body stores, and each depends on the route taken. Energy conservation ties them together: $\Delta U$ is the net heat in plus the net work done on the body.
