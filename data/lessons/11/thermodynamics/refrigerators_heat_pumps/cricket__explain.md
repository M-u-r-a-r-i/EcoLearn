---
concept_id: refrigerators_heat_pumps
interest: cricket
format: explain
title: The drinks fridge that heated the dressing room
check:
  question: |-
    The dressing-room drinks fridge removes $600\,\text{J}$ of heat from its inside while using $200\,\text{J}$ of electrical work. What is its coefficient of performance, and how much heat does it release into the room?
  options:
    A: |-
      $\alpha = 0.33$; $800\,\text{J}$ released
    B: |-
      $\alpha = 3$; $400\,\text{J}$ released
    C: |-
      $\alpha = 3$; $800\,\text{J}$ released
    D: |-
      $\alpha = 4$; $800\,\text{J}$ released
  answer: C
  explanation: |-
    $\alpha = Q_2/W = 600/200 = 3$. Energy conservation: the heat released is $Q_1 = Q_2 + W = 600 + 200 = 800\,\text{J}$.
  misconceptions:
    A: |-
      Inverts the ratio, computing $W/Q_2$ as if it were an efficiency that must be below 1. The coefficient of performance is heat removed per unit of work, and it can exceed 1.
    B: |-
      Thinks the work is used up or subtracted, $Q_1 = Q_2 - W$. The electrical work also ends up as heat in the room, so $Q_1 = Q_2 + W$.
    D: |-
      Uses $Q_1/W = 800/200 = 4$, which is the coefficient of performance of a heat pump. For a refrigerator the useful effect is the heat removed from the cold space, $Q_2$.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A hot afternoon at a cricket ground: blazing sun, a board showing 38 degrees, a bowler polishing the ball, a generator with hot exhaust and an ice box of drinks](scenes/cricket/thermodynamics.svg "Cold drinks on a 38 °C day. Inside the pavilion, a fridge is working hard to keep them that way.")

A 38-degree afternoon, and the dressing room's air conditioner has broken down. The players come in at the drinks break, dripping with sweat. Joseph, the kit manager, has an idea. He props open the door of the big drinks fridge in the corner. "There. Free air conditioning. Cold air will pour out and cool the room."

Nandini, the team's video analyst, isn't so sure. She has noticed something about that fridge: the grille at the back is always hot, and the wall behind it is warm to the touch. She reaches behind it now. It's hotter than ever, because with the door open, the fridge is running flat out.

"The front breathes cold," she says, "and the back breathes hot. So which one wins?"

Half an hour later, the room feels warmer, not cooler. Joseph can't understand it. A machine whose whole job is making things cold, and it's heating the room?

## The physics

Heat flows naturally from hot to cold. A **refrigerator** makes it go the other way, taking heat out of a cold space and dumping it somewhere hotter, and that needs work. A refrigerator is a **heat engine run in reverse**:

- the working substance (the **refrigerant**) absorbs heat $Q_2$ from the cold space at temperature $T_2$ (inside the fridge);
- external work $W$ is done on it (by the electric compressor);
- it releases heat $Q_1$ to the hot surroundings at $T_1$ (the room, through the grille at the back).

![Energy flow in a refrigerator: heat Q2 taken from the cold inside, electrical work W put in, and heat Q1 equal to Q2 plus W released to the room](figures/refrigerators_heat_pumps/refrigerator-energy-flow.svg "Everything the fridge takes from inside, plus all the work it uses, comes out at the back. Widths to scale for Q2 = 600, W = 300, Q1 = 900.")

The refrigerant runs in a cycle, so $\Delta U = 0$ each cycle, and energy conservation gives

$$Q_1 = Q_2 + W$$

The heat released to the room is always *more* than the heat removed from inside.

A refrigerator's job is to remove $Q_2$, and what it costs is $W$, so its performance is measured by the **coefficient of performance**:

$$\alpha = \frac{Q_2}{W}$$

$\alpha$ is not an efficiency and is often greater than 1: moving heat can take less work than the amount of heat moved. $\alpha$ can never be infinite, though: some work is always needed ($W \neq 0$), and the second law of thermodynamics, coming next, says why.

A **heat pump** is the same machine used for the opposite purpose: to warm a building by pumping heat in from the colder outdoors. Its useful output is $Q_1$, so its coefficient of performance is $Q_1/W$.

## Worked example

**Given (illustrative):** in one minute, the drinks fridge removes $Q_2 = 600\,\text{J}$ from its inside using $W = 300\,\text{J}$ of electrical work.
**Find:** its coefficient of performance, the heat released at the back, and what happens to the room with the door open.

$$\alpha = \frac{Q_2}{W} = \frac{600}{300} = 2.0$$

$$Q_1 = Q_2 + W = 600 + 300 = 900\,\text{J}$$

With the door open, the "inside" *is* the room. Each minute the fridge takes $600\,\text{J}$ out of the room air at the front and puts $900\,\text{J}$ back at the back. Net: the room gains $300\,\text{J}$, exactly the electrical work. Joseph's plan heats the room.

Used as a heat pump, the same machine would deliver $Q_1/W = 900/300 = 3.0$ joules of heat for every joule of work.

**Sanity check:** $Q_1 - Q_2 = 900 - 600 = 300\,\text{J} = W$, as energy conservation requires.

## Where the picture breaks

An air conditioner does cool a room, but only because it dumps $Q_1$ *outside* through a unit on the outer wall; the drinks fridge dumps it into the same room. A real fridge's refrigerant also changes between liquid and vapour, and the fridge loses some heat through its walls; the energy accounting above still holds. The dressing room only sets the scene: this physics is the same in any kitchen.

## Key takeaway

A refrigerator is a heat engine in reverse: it uses work $W$ to take heat $Q_2$ from a cold space and releases $Q_1 = Q_2 + W$ to hotter surroundings. Its coefficient of performance is $\alpha = Q_2/W$, which can exceed 1 but never be infinite. A heat pump uses the same cycle to deliver $Q_1$, with coefficient of performance $Q_1/W$.
