---
concept_id: power
interest: cricket
format: explain
title: Stair sprints and the groundsman's roller
check:
  question: |-
    A motorised pitch roller moves at a steady $1.5\,\text{m/s}$ against a total resistive force of $1200\,\text{N}$. What power does its engine deliver to keep it moving, in horsepower? ($1\,\text{hp} = 746\,\text{W}$)
  options:
    A: |-
      $1800\,\text{hp}$
    B: |-
      $2.4\,\text{hp}$
    C: |-
      $1.1\,\text{hp}$
    D: |-
      $1.3 \times 10^{6}\,\text{hp}$
  answer: B
  explanation: |-
    At steady speed the driving force equals the resistance, so $P = Fv = 1200 \times 1.5 = 1800\,\text{W}$, and $1800/746 \approx 2.4\,\text{hp}$.
  misconceptions:
    A: |-
      Calculates $P = Fv = 1800$ correctly but in watts, then forgets to convert to horsepower; a horsepower is 746 times larger than a watt.
    C: |-
      Divides force by speed ($1200/1.5 = 800\,\text{W}$) instead of multiplying; power is force times velocity, since work is force times distance.
    D: |-
      Multiplies by 746 instead of dividing; converting to a bigger unit must give a smaller number.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A cricket ground by day: a batter watches a ball climb high, a fielder waits under it, a player runs up the stadium steps and a groundsman pushes a roller](scenes/cricket/work_energy_power.svg "Stair sprints in the stands, a roller on the square: both are about how fast work gets done.")

Pre-season fitness day. The coach points at the stadium steps: "Top of the stand, flat out. Twelve metres straight up."

Mohit, the team's burly all-rounder, pounds up in $15\,\text{s}$. Ravi, a wiry opening batter, is lighter and gets there in $10\,\text{s}$.

At the top, gasping, Mohit claims the win. "I'm heavier, so I lifted more. I did more work, so I'm the more powerful one."

Down below, the groundsman is driving the motorised roller slowly across the square. Ravi has seen its engine plate, which gives its rating in "horsepower", and he wonders what that has to do with running up stairs.

Mohit really did do more work. But is doing more work the same as being more powerful? And what exactly does a power rating measure?

## The physics

**Power** is the rate of doing work — how fast energy is transferred.

The **average power** over a time $t$ is

$$P_\text{avg} = \frac{W}{t}$$

The **instantaneous power** is the limit as the time interval shrinks: $P = \dfrac{dW}{dt}$.

The SI unit is the **watt**: $1\,\text{W} = 1\,\text{J/s}$. An older unit, still used for engines and motors, is the **horsepower**: $1\,\text{hp} = 746\,\text{W}$. Power is a scalar.

**Power from force and velocity.** In a short time $dt$, a force $\vec{F}$ moves its point of application by $d\vec{r}$ and does work $dW = \vec{F} \cdot d\vec{r}$. Dividing by $dt$:

$$P = \vec{F} \cdot \vec{v} = Fv\cos\theta$$

That's why a vehicle needs more power to go faster against the same resistance. At steady speed, its driving force equals the resistance $F$, and it must supply $Fv$.

So Mohit's claim confuses work with power. A small job done quickly can need more power than a big job done slowly.

![Work done against gravity plotted against time for two players: the lighter, faster player's line is steeper, so their power is greater even though their total work is smaller](figures/power/work-vs-time-slope.svg "Power is the slope. The red line ends lower (less work) but climbs more steeply (more power).")

A unit to watch: the electricity meter's "unit" is the **kilowatt hour**, $1\,\text{kWh} = 1000\,\text{W} \times 3600\,\text{s} = 3.6 \times 10^{6}\,\text{J}$. It measures energy, not power.

## Worked example

**Given** (illustrative): height $h = 12\,\text{m}$; Mohit $70\,\text{kg}$ in $15\,\text{s}$; Ravi $60\,\text{kg}$ in $10\,\text{s}$; $g = 9.8\,\text{m/s}^2$. The roller moves at a steady $1.0\,\text{m/s}$ against a resistance of $1500\,\text{N}$.
**Find:** each player's average power (in W and hp), and the roller's power.

Work against gravity, $W = mgh$:

$$W_\text{Mohit} = 70 \times 9.8 \times 12 = 8232\,\text{J} \qquad W_\text{Ravi} = 60 \times 9.8 \times 12 = 7056\,\text{J}$$

Average power:

$$P_\text{Mohit} = \frac{8232}{15} \approx 549\,\text{W} \approx 0.74\,\text{hp} \qquad P_\text{Ravi} = \frac{7056}{10} \approx 706\,\text{W} \approx 0.95\,\text{hp}$$

Mohit did more work; Ravi was about 29% more powerful.

Roller, using $P = Fv$ with force and velocity in the same direction:

$$P = 1500 \times 1.0 = 1500\,\text{W} = \frac{1500}{746} \approx 2.0\,\text{hp}$$

**Sanity check:** Ravi's vertical speed is $12/10 = 1.2\,\text{m/s}$, and his weight is $60 \times 9.8 = 588\,\text{N}$. So $P = Fv = 588 \times 1.2 \approx 706\,\text{W}$, the same answer by the other formula.

## Where the picture breaks

These numbers count only the useful work of lifting each body. Human muscles are inefficient: most of the chemical energy burned becomes heat. So the power each player's body actually consumed was several times larger. The players also speed up at the start and move forwards along each step, which our $mgh$ ignores. Their power also rises and falls with every stride, so $W/t$ is only an average. The roller's engine, too, must produce more than $1500\,\text{W}$, because some is lost in its own gears and as heat.

## Key takeaway

Power is the rate of doing work: $P_\text{avg} = W/t$, and instantaneously $P = \vec{F} \cdot \vec{v}$. It is measured in watts ($1\,\text{W} = 1\,\text{J/s}$), with $1\,\text{hp} = 746\,\text{W}$. Doing more work is not the same as being more powerful — what matters is how fast it's done.
