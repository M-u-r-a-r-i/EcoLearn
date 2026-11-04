---
concept_id: power
interest: gaming
format: explain
title: Why full power stops feeling fast
check:
  question: |-
    A kart's engine delivers $40\,\text{kW}$ to the wheels. While it is travelling at $20\,\text{m/s}$, what driving force does that power correspond to?
  options:
    A: |-
      $800\,000\,\text{N}$
    B: |-
      $2000\,\text{W}$
    C: |-
      $2000\,\text{N}$
    D: |-
      $40\,000\,\text{N}$
  answer: C
  explanation: |-
    From $P = Fv$, $F = P/v = 40\,000/20 = 2000\,\text{N}$. At a given power, the faster you go the smaller the force you can push with.
  misconceptions:
    A: |-
      Multiplies power by speed instead of dividing ($40\,000 \times 20$); $P = Fv$ rearranges to $F = P/v$, and a force of $800$ kilonewtons on a kart is absurd.
    B: |-
      Gets the arithmetic right but keeps the unit of power; a force is measured in newtons, and watts are joules per second.
    D: |-
      Reads the power figure as if it were a force, ignoring the speed altogether; power only becomes a force once you divide by how fast the point of application is moving.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A gaming desk at night: a monitor shows a physics sandbox with a spring launcher, a kart at the top of a loop and a crate being dragged by a rope, beside a force-feedback racing wheel and a controller](scenes/gaming/work_energy_power.svg "The wheel on the right is the last part of the chain: engine, wheels, track — and how quickly energy moves along it.")

Tanvi has spent two evenings in the garage screen of her racing sim, and she has a complaint.

Out of the first corner her tuned kart is savage — it pins her into the seat and eats the field. But on the long back straight it goes soft. The throttle is still flat on the floor, the engine is at full power, the numbers on the dashboard have not changed, and yet the speed creeps up by ones and twos.

Her friend Gurmeet, who plays with the same setup, says the game is cheating. "They cap you on the straight. Everyone knows."

Tanvi doesn't believe it. She watched the dashboard: nothing dropped. The engine is doing the same job, second after second, the whole way down the straight. So why does the *same* engine at the *same* power throw you forward at the start of a straight and barely push at the end of it?

## The physics

**Power is the rate of doing work.** Average power over a time $t$:

$$P_\text{av} = \frac{W}{t}$$

and the instantaneous power is $P = \dfrac{dW}{dt}$, the slope of a work-against-time graph. The SI unit is the **watt**: $1\,\text{W} = 1\,\text{J/s}$. The older unit still printed on engines is the horsepower, $1\,\text{hp} = 746\,\text{W}$.

![Work done against time for two climbers doing the same job, one in less time: both lines are straight, and the steeper one represents the greater power](figures/power/work-vs-time-slope.svg "Power is the slope of work against time. Same work in less time means a steeper line and more power.")

Now the form that answers Tanvi's question. In a small time $dt$ a force $\vec{F}$ moves its point of application through $d\vec{s}$, doing work $\vec{F} \cdot d\vec{s}$, so

$$P = \frac{\vec{F} \cdot d\vec{s}}{dt} = \vec{F} \cdot \vec{v}$$

For a force along the motion, $P = Fv$, and rearranged, $F = P/v$. **At a fixed power, the driving force falls as the speed rises.** At the corner exit the kart is slow, so all that power arrives as a huge force; at the end of the straight the same power is spread over far more metres each second, and what is left over after air drag is tiny.

Two conditions worth keeping: power is a scalar, and $P = \vec{F} \cdot \vec{v}$ uses the dot product, so a force perpendicular to the motion delivers no power at all.

## Worked example

**Given** (illustrative values): a kart whose engine delivers a steady $P = 60\,\text{kW}$ to the wheels.
**Find:** the driving force at $10\,\text{m/s}$ and at $30\,\text{m/s}$, and the engine's rating in horsepower.

**Step 1 — early in the straight.**

$$F = \frac{P}{v} = \frac{60\,000}{10} = 6000\,\text{N}$$

A big shove: roughly the weight of eight or nine adults standing on the kart.

**Step 2 — late in the straight, at three times the speed.**

$$F = \frac{60\,000}{30} = 2000\,\text{N}$$

Three times the speed, one third of the force — and air drag, which grows with speed, is eating most of what remains. Tanvi's "soft" feeling is real, and no one is capping her.

**Step 3 — in the old unit.**

$$\frac{60\,000\,\text{W}}{746\,\text{W/hp}} \approx 80\,\text{hp}$$

**Sanity check:** the force fell in exactly the ratio the speed rose, which is what $F = P/v$ demands at constant power.

## Where the picture breaks

A real engine does not hold one power at every speed — its power rises and falls across the rev range, which is the whole reason gears exist. Some of the engine's output never reaches the road at all, lost in the gearbox and the tyres as heat. Top speed itself is not set by this equation but by the point where the driving force has fallen to match air drag, so the kart cannot accelerate any more. And a game's "power" slider is a number chosen to feel good on a controller; only a simulator that models drag and gearing makes it the physical watt.

## Key takeaway

Power is how fast work is done: $P_\text{av} = W/t$, and instantaneously $P = \vec{F} \cdot \vec{v}$, measured in watts ($1\,\text{hp} = 746\,\text{W}$). Because $F = P/v$, a fixed power gives a large force at low speed and a small one at high speed — which is why the same engine feels fierce out of a corner and gentle at the end of a straight.
