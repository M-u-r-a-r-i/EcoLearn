---
concept_id: refrigerators_heat_pumps
interest: gaming
format: explain
title: The air conditioner that makes more heat than it removes
check:
  question: |-
    In one second, a practice room's air conditioner takes $900\,\text{J}$ of heat out of the room air and releases $1200\,\text{J}$ to the air outside. What is its coefficient of performance?
  options:
    A: |-
      $\alpha = 0.33$
    B: |-
      $\alpha = 3$
    C: |-
      $\alpha = 4$
    D: |-
      $\alpha = 0.75$
  answer: B
  explanation: |-
    Energy conservation gives the work: $W = Q_1 - Q_2 = 1200 - 900 = 300\,\text{J}$. For a refrigerator the useful effect is the heat removed, so $\alpha = Q_2/W = 900/300 = 3$.
  misconceptions:
    A: |-
      Inverts the ratio, computing $W/Q_2$ as though it were an efficiency that has to be below 1. The coefficient of performance is heat removed *per joule of work*, and it is routinely greater than 1.
    C: |-
      Uses $Q_1/W = 1200/300$. That is the coefficient of performance of a *heat pump*, whose useful output is the heat delivered to the warm side, not the heat taken from the cold side.
    D: |-
      Computes $Q_2/Q_1$, as if the machine were an engine being judged on what fraction it passes on. A refrigerator's cost is the work put in, not the heat coming out of the hot side.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A gaming desk at night: a monitor showing GPU and CPU temperatures, a tower PC with a heat sink and fans, hot air leaving the top and cool air drawn in, a can of compressed-air duster, a mini fridge under the desk and a backup generator outside the window](scenes/gaming/thermodynamics.svg "Under the desk, the mini fridge: cold at the front, warm at the back, always both at once.")

The summer tournament is in a small first-floor room with eight machines in it, and by the second hour it is unbearable. Vidya, who organised the thing, gets the building's air conditioner switched on and props the door shut.

It works. Within twenty minutes the room is pleasant and the players stop complaining.

Then she goes out to the balcony to make a call, and walks straight into a wall of hot air. The outdoor unit is bolted to the wall out there, and the air coming off it is hotter than the room ever got — much hotter than the day.

Her friend Karthik joins her. "So it's moving the heat outside," he says. "Fine. But that's way hotter than the room was. Where is the *extra* coming from? And if it can push heat from a cool room into a hot balcony, why does a fridge need a plug at all? Heat could just... go."

Inside, the room is still getting cooler. Outside, the balcony is still getting hotter. Something is being paid for, and Vidya wants to know what.

## The physics

Heat flows naturally from hot to cold. A **refrigerator** — and an air conditioner is one — makes it go the other way: it takes heat out of a cold space and dumps it somewhere hotter. That requires work. A refrigerator is a **heat engine run in reverse**:

- the working substance, the **refrigerant**, absorbs heat $Q_2$ from the cold space at temperature $T_2$ (the room);
- external work $W$ is done on it, by the electric compressor;
- it releases heat $Q_1$ to the hot surroundings at $T_1$ (the balcony, through the outdoor unit).

![Energy flow in a refrigerator: heat Q2 taken from the cold inside, electrical work W put in, and heat Q1 equal to Q2 plus W released to the warm surroundings](figures/refrigerators_heat_pumps/refrigerator-energy-flow.svg "Everything taken from the cold side, plus every joule of work paid for, leaves at the hot side. Widths to scale for Q2 = 600, W = 300 and Q1 = 900.")

The refrigerant runs in a cycle, so $\Delta U = 0$ each cycle and energy conservation gives

$$Q_1 = Q_2 + W$$

The heat delivered to the hot side is always *more* than the heat removed from the cold side, by exactly the work put in. That is Karthik's "extra": the electricity the compressor used, which ends up as heat like everything else.

A refrigerator's job is to remove $Q_2$, and what it costs is $W$, so its performance is measured by the **coefficient of performance**:

$$\alpha = \frac{Q_2}{W}$$

$\alpha$ is not an efficiency, and it is usually greater than 1 — *moving* heat can cost far less work than the amount of heat moved. It can never be infinite, though: some work is always needed, $W \neq 0$, and the second law of thermodynamics says exactly why.

A **heat pump** is the same machine used for the opposite purpose — warming a building by pumping heat in from the colder outdoors. Its useful output is $Q_1$, so its coefficient of performance is $Q_1/W$, which is larger by exactly 1.

## Worked example

**Given (illustrative):** in one second the air conditioner removes $Q_2 = 800\,\text{J}$ from the room air, using $W = 200\,\text{J}$ of electrical work.
**Find:** its coefficient of performance and the heat delivered to the balcony.

The coefficient of performance compares what you want with what you pay:

$$\alpha = \frac{Q_2}{W} = \frac{800}{200} = 4.0$$

Four joules shifted out of the room for every joule of electricity — which is why cooling a room costs less than a heater of the same strength would.

Now the balcony side. Nothing is stored, so everything that went in must come out:

$$Q_1 = Q_2 + W = 800 + 200 = 1000\,\text{J}$$

So the building as a whole gains $200\,\text{J}$ every second — the electrical work — even while the room loses $800\,\text{J}$. Picture it as a bucket chain: the room's heat is carried out, and the compressor's own energy is thrown on the same pile.

**Sanity check:** the hot side must always deliver more than the cold side gives up, and $1000\,\text{J}$ is more than $800\,\text{J}$ by exactly the $200\,\text{J}$ that was paid for.

## Where the picture breaks

An air conditioner genuinely cools a room, but only because its hot side is *outside* — put the same machine entirely inside the room, as with the mini fridge under a desk, and the room warms, because $Q_1$ and $Q_2$ both land in it. A real refrigerant also boils and condenses as it goes round, so the cycle involves changes of phase that this energy accounting does not show; the accounting still holds exactly. Real rooms leak heat through walls and doorways too, so $Q_2$ in practice includes heat that has just wandered back in, which is why a propped-open door ruins the cooling. And the tournament is only the setting — the physics is the same in any kitchen.

## Key takeaway

A refrigerator is a heat engine in reverse: it uses work $W$ to move heat $Q_2$ out of a cold space, and releases $Q_1 = Q_2 + W$ into hotter surroundings. Its coefficient of performance is $\alpha = Q_2/W$, which can exceed 1 but can never be infinite. A heat pump is the same cycle judged on $Q_1$ instead, giving $Q_1/W$.
