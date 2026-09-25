---
concept_id: power
interest: smartphones
format: explain
title: Same climb, twice the power
check:
  question: |-
    A robot vacuum moves across a carpet at a steady $0.30\,\text{m/s}$. Its wheels push it forward with $6.0\,\text{N}$, just balancing the carpet's drag. What power does the wheels' push deliver?
  options:
    A: |-
      $20\,\text{W}$
    B: |-
      $0.050\,\text{W}$
    C: |-
      $1.8\,\text{W}$
    D: |-
      $0\,\text{W}$
  answer: C
  explanation: |-
    Power delivered by a force is $P = Fv$ when the force is along the motion: $P = 6.0 \times 0.30 = 1.8\,\text{W}$. Every second the push does $1.8\,\text{J}$ of work, which the carpet's drag turns into heat.
  misconceptions:
    A: |-
      Divides force by speed ($6.0/0.30$). Power is work per second, and work per second is force times distance per second — force times speed.
    B: |-
      Divides speed by force ($0.30/6.0$). A bigger push at the same speed must mean more power, not less, so power has to grow with the force: $P = Fv$.
    D: |-
      Thinks no work is done because the net force is zero at steady speed. The *net* work is zero, but the wheels' push on its own does positive work every second; the drag does equal negative work.
author: claude-code/opus-5
written: 2026-09-25
---
## The story

![A living room in the evening: a camera drone climbs straight up, a phone falls from a shelf towards a cushion, an earbuds case is whirled on a lanyard in a vertical circle, and a robot vacuum rolls towards a sofa leg](scenes/smartphones/work_energy_power.svg "The drone on the left is climbing. How much energy it needs depends on the height; how hard its motors work depends on how quickly.")

Zara is filming the Diwali lights on her building for the housing society's group chat, using a small camera drone. The best shot is from twenty metres up, level with the rooftop lamps.

The first time, she lets it rise on the gentle default setting. It drifts upwards, taking its time. Her younger brother Kabir, impatient, grabs the controller for the second take and pushes the climb stick all the way — the drone shoots up in half the time, and the motor note rises to a whine.

"You're wasting battery," Zara says.

"It's the same twenty metres," says Kabir. "Same height, same drone. It has to be the same energy."

They are both partly right. The drone gains the same energy either way. So what, exactly, is different about the fast climb — and how do you put a number on it?

## The physics

**Power** is the rate of doing work — how many joules per second.

The **average power** over a time $t$ is

$$P_\text{avg} = \frac{W}{t}$$

and the **instantaneous power** is $P = \dfrac{dW}{dt}$. Its SI unit is the **watt**: $1\,\text{W} = 1\,\text{J/s}$. The older unit, still used for engines, is the **horsepower**: $1\,\text{hp} = 746\,\text{W}$.

For a force $\vec{F}$ acting on a body moving with velocity $\vec{v}$, the work in a short time $dt$ is $\vec{F} \cdot d\vec{r}$, so

$$P = \vec{F} \cdot \vec{v} = Fv\cos\theta$$

![A graph of work done against time: the work curve rises ever more steeply, a dashed chord across the whole interval marks the average power, and a tangent at the final instant marks the instantaneous power](figures/power/work-vs-time-curve.svg "Power is the slope of work against time. The chord's slope gives the average power; the tangent's slope, the power at one instant. For a drone climbing at a steady speed, the line would simply be straight.")

The same work done in half the time means twice the power. That is Kabir's fast climb: same energy, delivered twice as quickly.

## Worked example

**Given:** drone mass $m = 0.50\,\text{kg}$; it climbs $h = 20\,\text{m}$ at a steady $4.0\,\text{m/s}$, taking $5.0\,\text{s}$ (Kabir's take; illustrative); $g = 9.8\,\text{m/s}^2$; ignore air drag.
**Find:** the work done against gravity, the power, and the power in horsepower.

1. *Work:* the potential energy gained, $W = mgh = 0.50 \times 9.8 \times 20 = 98\,\text{J}$ — the same for either take.
2. *Average power:* $P = W/t = 98 / 5.0 = 19.6\,\text{W} \approx 20\,\text{W}$.
3. *Check with $P = Fv$:* at steady speed the lift from the rotors just balances the weight, $F = mg = 4.9\,\text{N}$, pointing along the motion, so $P = 4.9 \times 4.0 = 19.6\,\text{W}$. Zara's gentle take at $2.0\,\text{m/s}$ needs only half that.
4. *In horsepower:* $19.6 / 746 \approx 0.026\,\text{hp}$ — a tiny fraction of a scooter engine.

**Sanity check:** $20\,\text{W}$ is roughly what one LED tube light draws — a modest amount, reasonable for a small flying machine.

## Where the picture breaks

The drone is a real case, but its motors use far more than $20\,\text{W}$. A hovering drone does **no** work on itself — it isn't moving — yet it drains its battery fast, because the rotors keep throwing air downwards, and that moving air carries energy away. So the $19.6\,\text{W}$ is only the *extra* power that goes into climbing; the battery also pays for hovering, for air drag, and for heat in the motors and electronics. Zara was right that the fast climb costs more battery per second — but the energy stored as height is the same.

## Key takeaway

Power is the rate of doing work: $P_\text{avg} = W/t$, and for a force on a moving body $P = \vec{F} \cdot \vec{v} = Fv\cos\theta$. The same work done faster needs more power. $1\,\text{W} = 1\,\text{J/s}$ and $1\,\text{hp} = 746\,\text{W}$.
