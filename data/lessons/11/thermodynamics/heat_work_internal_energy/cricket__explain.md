---
concept_id: heat_work_internal_energy
interest: cricket
format: explain
title: Two warm cricket balls and the question of which one holds more heat
check:
  question: |-
    Two identical cricket balls start at the same temperature. Ball X lies in the sun: it absorbs $50\,\text{J}$ of heat and no work is done on it. Ball Y is polished hard: $70\,\text{J}$ of work is done on it by rubbing, and it loses $20\,\text{J}$ of heat to the air. Which statement is correct?
  options:
    A: |-
      Ball X now contains more heat than ball Y, because only X was heated.
    B: |-
      Ball Y has more internal energy than X, because $70\,\text{J}$ of work went into it.
    C: |-
      Their internal energies cannot be equal, because the heat and work were so different.
    D: |-
      Both gained $50\,\text{J}$ of internal energy; heat and work describe the transfers, not what the balls contain.
  answer: D
  explanation: |-
    Energy conservation: X gains $50\,\text{J}$; Y gains $70 - 20 = 50\,\text{J}$. Both reach the same state with the same internal energy. Heat and work are energy in transit, so neither ball "contains" heat or work.
  misconceptions:
    A: |-
      Treats heat as something stored inside a body. Once transferred, heat becomes internal energy, and nothing records how it arrived.
    B: |-
      Counts the work done on Y but forgets the $20\,\text{J}$ that Y lost as heat; the net gain is what changes internal energy.
    C: |-
      Thinks internal energy depends on the route taken. It is a state variable: the same state always has the same internal energy.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A hot afternoon at a cricket ground: blazing sun, a board showing 38 degrees, a bowler polishing the ball, a generator with hot exhaust and an ice box of drinks](scenes/cricket/thermodynamics.svg "Sun on one ball, a trouser leg on the other: two different ways of warming the same kind of object.")

Afternoon nets, and the coach, Rekha, runs a small experiment. She leaves one new ball lying in the sun on the boundary rope. She hands an identical ball to Kabir, her fast bowler, and tells him to polish it hard on his trousers for five minutes, the way bowlers do to keep one side shiny.

Then she borrows the physio's infrared thermometer. Both balls read exactly the same: a few degrees warmer than when they came out of the box.

Kabir's friend Dev is sure he can explain it. "The sun ball is full of heat. Yours is full of work, Kabir. Same temperature, different stuff inside."

Rekha swaps the balls behind her back and holds them out. "Then tell me which is which. Test them any way you like."

Dev picks them up, turns them over, frowns. Is there *anything* inside a ball that remembers how it got warm?

## The physics

Every body is made of molecules that jiggle, vibrate and pull on each other. The total of their kinetic and potential energies, measured in the frame where the body as a whole is at rest, is its **internal energy** $U$. The ball's speed through the air is not part of $U$; the random jiggling of its molecules is.

Energy can be added to a body in two different ways:

- **Heat** $Q$: energy transferred because of a temperature difference. The sun is far hotter than the ball, so energy flows in.
- **Work** $W$: energy transferred by other means, such as a force acting through a distance. Kabir's rubbing force acts through a distance along the leather, and friction at the surface turns that into molecular jiggling.

Energy is conserved, so the change in internal energy equals the energy that came in as heat plus the energy that came in as work done on the body (you will soon meet this as the first law, with a sign convention).

![Two routes from State 1 to State 2: left in the sun with 60 J of heat in and no work; rubbed hard with 80 J of work done and 20 J of heat lost; both give a change in internal energy of 60 J](figures/heat_work_internal_energy/two-routes-same-state.svg "Different amounts of heat and work, the same change in internal energy. Only U belongs to the state.")

Here is the key distinction:

- $U$ is a **state variable**. It depends only on the body's present condition (temperature, pressure, volume and so on), not on its history. Same state means same $U$.
- $Q$ and $W$ are **not** state variables. They describe a *process*, energy crossing the boundary. Once they have crossed, both become internal energy, and the body keeps no record of which way it came. Saying a body "contains heat" or "contains work" is meaningless, the way a bank balance doesn't remember whether you paid in cash or by transfer.

That answers Dev. The two balls are in the same state, so they have the same internal energy, and no test can tell which route each took.

## Worked example

**Given:** a warming of $60\,\text{J}$ takes the ball from State 1 to State 2 (illustrative). This time Kabir polishes a ball that is also lying in the sun: rubbing does $50\,\text{J}$ of work on it, and it ends in exactly State 2.
**Find:** the net heat that flowed into the ball.

Because $U$ is a state variable, $\Delta U = U_2 - U_1 = 60\,\text{J}$ whatever the route. By energy conservation,

$$\Delta U = Q_\text{in} + W_\text{on} \quad\Rightarrow\quad Q_\text{in} = 60 - 50 = 10\,\text{J}$$

**Sanity check:** the three routes use $(Q, W_\text{on}) = (60, 0)$, $(-20, 80)$ and $(10, 50)$ in joules. Each pair adds to $60\,\text{J}$: the heat and work change from route to route, their sum does not.

## Where the picture breaks

Real balls in the sun and in a bowler's hand exchange heat with the air all the time, so neither route is as clean as the diagram; the numbers are illustrative. Friction heating is subtle: the rubbing force does work at the surface, and some of that energy goes into the trousers, not the ball. Polishing also changes the leather's surface, so the two balls are not perfectly identical in every respect. The principle survives all of this: for the same state, the internal energy is the same.

## Key takeaway

Internal energy $U$ is the molecular energy a body has; it is a state variable. Heat and work are two ways of *transferring* energy, not things a body holds, and they depend on the route. Energy conservation links them: $\Delta U$ equals the net heat in plus the net work done on the body.
