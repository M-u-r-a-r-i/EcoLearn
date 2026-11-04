---
concept_id: refrigerators_heat_pumps
interest: football
format: explain
title: The ice machine that keeps warming the medical room
check:
  question: |-
    An ice machine removes $900\,\text{J}$ of heat from the water it is freezing while using $300\,\text{J}$ of electrical work. What is its coefficient of performance, and how much heat does it release into the room?
  options:
    A: |-
      $\alpha = 0.33$; $1200\,\text{J}$ released
    B: |-
      $\alpha = 3$; $600\,\text{J}$ released
    C: |-
      $\alpha = 4$; $1200\,\text{J}$ released
    D: |-
      $\alpha = 3$; $1200\,\text{J}$ released
  answer: D
  explanation: |-
    $\alpha = Q_2/W = 900/300 = 3$. Energy conservation over a cycle gives $Q_1 = Q_2 + W = 900 + 300 = 1200\,\text{J}$ released at the back.
  misconceptions:
    A: |-
      Inverts the ratio, computing $W/Q_2$ as though it were an efficiency that has to be less than 1. The coefficient of performance is heat removed per joule of work, and it is normally greater than 1.
    B: |-
      Thinks the work is used up or subtracted, giving $Q_1 = Q_2 - W$. The electrical work does not disappear: it comes out at the back as heat too, so $Q_1 = Q_2 + W$.
    C: |-
      Uses $Q_1/W = 1200/300 = 4$, which is the coefficient of performance of a *heat pump*. For a refrigerator the useful effect is the heat removed from the cold space, $Q_2$.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A training ground on a hot day: a board reading 36 degrees Celsius, an ice box of drinks, a player inflating a ball with a hand pump, and a mower with a hot exhaust](scenes/football/thermodynamics.svg "That ice box came from a machine — and the machine has to put the cold somewhere it can take it from.")

The medical room at the club is small, and on match days it holds a treatment couch, two crates of water and the ice machine that feeds the recovery tubs.

Farida, the physio, has had enough of it. "Move that thing out. This room is warmer than the corridor every single afternoon."

Imran, in his first season as her assistant, thinks she has it backwards. "It makes *ice*," he says. "Buckets of it. It should be the coldest room in the building."

Farida points him round the back. He puts a hand near the black grille and pulls it away fast — it is hot, hotter than the wall behind it, and it is blowing warm air into a room with one small window.

He opens the front: a tray of fresh ice, cold enough to hurt.

Cold at the front, hot at the back, all from one machine that is plugged into the wall. Which one wins for the room — and is there any way to get the cold without the heat?

## The physics

Heat flows by itself from hot to cold. A **refrigerator** forces it the other way: it takes heat out of a cold space and dumps it somewhere warmer. That does not happen for free — it needs work. A refrigerator is a **heat engine run in reverse**:

- the working substance (the **refrigerant**) absorbs heat $Q_2$ from the cold space at temperature $T_2$ — the freezing tray;
- external work $W$ is done on it, by the electric compressor;
- it releases heat $Q_1$ to the warmer surroundings at $T_1$ — the medical room, through that grille.

![Energy flow in a refrigerator: heat Q2 taken from the cold inside, electrical work W put in, and heat Q1 equal to Q2 plus W released to the room](figures/refrigerators_heat_pumps/refrigerator-energy-flow.svg "Everything taken from inside, plus all the work put in, comes out at the back. Widths to scale for Q2 = 600, W = 300, Q1 = 900.")

The refrigerant runs in a cycle, so $\Delta U = 0$ each cycle and energy conservation gives

$$Q_1 = Q_2 + W$$

The heat released into the room is always *more* than the heat taken out of the cold space. That is Imran's answer before any numbers: the back always beats the front.

A refrigerator's job is to remove $Q_2$, and its cost is $W$, so its performance is measured by the **coefficient of performance**

$$\alpha = \frac{Q_2}{W}$$

$\alpha$ is not an efficiency and is usually greater than $1$ — moving heat can cost less work than the amount of heat moved, because the work is not what the heat is *made of*. But $\alpha$ can never be infinite: some work is always needed, $W \neq 0$, and the second law of thermodynamics, next, says why.

A **heat pump** is the same machine used for the opposite purpose — warming a building by pumping heat in from the colder outdoors. Its useful output is $Q_1$, so its coefficient of performance is $Q_1/W$.

## Worked example

**Given (illustrative):** in one minute the ice machine removes $Q_2 = 800\,\text{J}$ from the water it is freezing, using $W = 200\,\text{J}$ of electrical work.
**Find:** its coefficient of performance, the heat delivered to the room, and what the room gains overall.

$$\alpha = \frac{Q_2}{W} = \frac{800}{200} = 4$$

Four joules of heat shifted for every joule of electricity: good value, and the reason fridges are worth plugging in.

$$Q_1 = Q_2 + W = 800 + 200 = 1000\,\text{J}$$

So each minute the grille delivers $1000\,\text{J}$ into the medical room, while the tray inside loses $800\,\text{J}$. If that ice is later left to melt in the same room, it takes its $800\,\text{J}$ back, and the room is left with $200\,\text{J}$ — exactly the electrical work. Farida is right: over an afternoon, the machine can only warm her room.

Used as a heat pump instead, the same machine would deliver $Q_1/W = 1000/200 = 5$ joules of heat per joule of work.

**Sanity check:** $Q_1 - Q_2 = 1000 - 800 = 200\,\text{J} = W$, as energy conservation demands.

## Where the picture breaks

The ice does leave the room, of course — it goes out to the recovery tubs — so in practice the medical room keeps the $1000\,\text{J}$ and sends the cold outside, which is the whole point of the machine. An air conditioner works the same way but puts its grille on the *outer* wall, which is the only reason it can cool a room at all. A real refrigerator's refrigerant also boils and condenses as it goes round, rather than staying a gas, and the cabinet leaks a little heat through its walls; neither changes the energy accounting above. Football is only the setting here: the same physics runs in every kitchen.

## Key takeaway

A refrigerator is a heat engine in reverse: work $W$ is used to take heat $Q_2$ from a cold space, and $Q_1 = Q_2 + W$ is released to warmer surroundings. Its coefficient of performance is $\alpha = Q_2/W$, which can be greater than 1 but never infinite. A heat pump is the same cycle judged by its heat output, with coefficient $Q_1/W$.
