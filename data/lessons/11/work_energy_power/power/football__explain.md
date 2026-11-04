---
concept_id: power
interest: football
format: explain
title: Two power numbers for one sprint
check:
  question: |-
    In a sled drill, a player keeps the sled moving at a steady $3.0\,\text{m/s}$ with a strap force of $250\,\text{N}$ along the direction of motion. What power does the strap deliver to the sled, in horsepower? ($1\,\text{hp} = 746\,\text{W}$)
  options:
    A: |-
      $1.0\,\text{hp}$
    B: |-
      $750\,\text{hp}$
    C: |-
      $0.11\,\text{hp}$
    D: |-
      $5.6 \times 10^{5}\,\text{hp}$
  answer: A
  explanation: |-
    With force and velocity in the same direction, $P = Fv = 250 \times 3.0 = 750\,\text{W}$, and $750/746 \approx 1.0\,\text{hp}$.
  misconceptions:
    B: |-
      Calculates $P = Fv = 750$ correctly, but that number is in watts; it has not been converted to horsepower, a unit 746 times larger.
    C: |-
      Divides force by speed ($250/3.0 \approx 83\,\text{W}$) instead of multiplying; power is force times velocity, because work is force times distance.
    D: |-
      Multiplies by 746 instead of dividing; converting to a bigger unit must give a smaller number.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A football training ground by day: a player drags a weighted sled on a strap, a striker lofts the ball in a high arc, and the goalkeeper dives to catch it](scenes/football/work_energy_power.svg "Sprints, sled drills and long kicks: every one of them is about how fast work gets done.")

Pooja plays on the wing for her state's under-19 team, and this season every player trains in a vest with a GPS tracker between the shoulder blades. After a sprint drill, the fitness coach, Anand, shows her the app on his tablet.

One flat-out burst from a standing start, about two seconds long. Two numbers sit next to it: **average power 1.0 kW** and **peak power 2.1 kW**.

"Peak is double the average?" Pooja asks. "It was one sprint. I didn't do anything different in the second half of it."

Her teammate Nandini leans over. "And what's a kilowatt in horsepower? Are you stronger than a motorbike engine now?"

Anand laughs and hands them each a water bottle. Why can a single two-second sprint have two different power numbers, one twice the other? And what exactly does a power rating measure?

## The physics

**Power** is the rate of doing work, or how fast energy is transferred.

The **average power** over a time $t$ is

$$P_\text{avg} = \frac{W}{t}$$

The **instantaneous power** is the limit as the time interval shrinks: $P = \dfrac{dW}{dt}$.

The SI unit is the **watt**: $1\,\text{W} = 1\,\text{J/s}$. An older unit, still used for engines and motors, is the **horsepower**: $1\,\text{hp} = 746\,\text{W}$. Power is a scalar.

**Power from force and velocity.** In a short time $dt$, a force $\vec{F}$ moves its point of application by $d\vec{r}$ and does work $dW = \vec{F} \cdot d\vec{r}$. Divide by $dt$:

$$P = \vec{F} \cdot \vec{v} = Fv\cos\theta$$

This explains Pooja's two numbers. If the force pushing her forwards stays about the same, the power $Fv$ grows as her speed grows. Near the start, when she is slow, the power is small; at the end of the burst, when she is fastest, it is largest. The average sits in between.

![Work done against time for a sprinter speeding up steadily: the work curve bends upwards, a dashed chord from the origin shows the average power of 1040 watts, and a red tangent at 2 seconds shows the instantaneous power of 2080 watts](figures/power/work-vs-time-curve.svg "Power is the slope. The chord's slope is the average power; the tangent's slope at the end is the instantaneous power, twice as steep.")

## Worked example

**Given** (illustrative): Pooja's mass $m = 65\,\text{kg}$; she speeds up uniformly from rest to $8.0\,\text{m/s}$ in $2.0\,\text{s}$ on level ground; ignore air resistance.
**Find:** the average power, the instantaneous power at $1.0\,\text{s}$ and at $2.0\,\text{s}$, each in W and hp.

Acceleration $a = 8.0/2.0 = 4.0\,\text{m/s}^2$, so the net forward force is $F = ma = 65 \times 4.0 = 260\,\text{N}$.

All the work goes into kinetic energy:

$$W = \tfrac{1}{2}mv^2 = \tfrac{1}{2} \times 65 \times 8.0^2 = 2080\,\text{J}$$

$$P_\text{avg} = \frac{2080}{2.0} = 1040\,\text{W} = \frac{1040}{746} \approx 1.4\,\text{hp}$$

Instantaneous power, $P = Fv$, with force and velocity in the same direction:

$$\text{at } 1.0\,\text{s } (v = 4.0\,\text{m/s}): \quad P = 260 \times 4.0 = 1040\,\text{W}$$

$$\text{at } 2.0\,\text{s } (v = 8.0\,\text{m/s}): \quad P = 260 \times 8.0 = 2080\,\text{W} \approx 2.8\,\text{hp}$$

The peak is twice the average, just like the app, because the speed and hence $Fv$ rise steadily from zero.

**Sanity check:** the distance covered is $\tfrac{1}{2} \times 4.0 \times 2.0^2 = 8.0\,\text{m}$, and $W = Fd = 260 \times 8.0 = 2080\,\text{J}$, the same.

## Where the picture breaks

These numbers count only the useful mechanical work of speeding up Pooja's body. Muscles are inefficient: most of the chemical energy they burn becomes heat, so her body consumed several times more power than this. Her push also isn't constant; it is largest in the first strides and comes in pulses, one per foot strike. Air drag, her arms and the up-and-down bounce of running all take extra power. A GPS vest estimates power from speed changes, so its figures are models too. As for Nandini's joke, power ratings of engines are sustained for hours; Pooja's peak lasts a fraction of a second.

## Key takeaway

Power is the rate of doing work: $P_\text{avg} = W/t$, and at any instant $P = \vec{F} \cdot \vec{v}$. It is measured in watts ($1\,\text{W} = 1\,\text{J/s}$), with $1\,\text{hp} = 746\,\text{W}$. For the same force, the faster a body moves, the more power that force delivers.
