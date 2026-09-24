---
concept_id: power
interest: motorsport
format: explain
title: Same engine, different gearing, different car
check:
  question: |-
    A car cruises at a steady $25\,\text{m/s}$ on a level road against a total resistance (drag plus rolling resistance) of $800\,\text{N}$. What power must reach the wheels, and what is that in horsepower, taking $1\,\text{hp} = 746\,\text{W}$?
  options:
    A: |-
      $32\,\text{W}$, about $0.04\,\text{hp}$
    B: |-
      $20\,\text{kW}$, about $27\,\text{hp}$
    C: |-
      $20\,\text{kW}$, about $14\,900\,\text{hp}$
    D: |-
      $0\,\text{W}$, because the speed is not changing
  answer: B
  explanation: |-
    At constant speed the driving force balances the resistance, so $P = Fv = 800 \times 25 = 20\,000\,\text{W} = 20\,\text{kW}$, and $20\,000/746 \approx 27\,\text{hp}$.
  misconceptions:
    A: |-
      Divides force by speed instead of multiplying. Power is force times velocity — the units must come out as $\text{N}\,\text{m/s} = \text{W}$.
    C: |-
      Multiplies by $746$ instead of dividing, and applies it to the $20$ rather than the $20\,000$. One horsepower is $746$ watts, so watts are the *bigger* number and you divide to get horsepower.
    D: |-
      Confuses zero *net* work with zero work. The kinetic energy is constant because the engine's positive work exactly cancels the resistance's negative work — and the engine is still burning fuel to supply it.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A race track scene: a car coasts down a hill road onto the circuit, a second car speeds along the straight with a velocity arrow, a third brakes with glowing red discs, and two people push a kart in the foreground](scenes/motorsport/work_energy_power.svg "Two cars can do the same work getting down this straight and still be nowhere near each other, because one did it faster.")

Two of the club's single-seaters are out together, and on paper they are twins. Same engine, same weight, same tyres. The only difference is in the back axle: Nayan has fitted a shorter final drive to his, so the wheels turn fewer times for each turn of the engine.

Out of the hairpin his car simply leaves the other one. Jyoti, watching from the wall with a stopwatch, has him two car lengths clear before the pit exit.

Then the long back straight arrives, and it all comes back the other way. The other car pulls past and keeps going, and Nayan crosses the line well behind.

In the tent afterwards he is baffled. "Same engine. It can't be stronger at one end of the lap and weaker at the other."

Jyoti thinks the engine is doing exactly the same thing in both cases. What changed is where the cars are spending it.

## The physics

**Power** is the *rate* of doing work — how fast energy is transferred, not how much.

The **average power** over a time interval is

$$P_\text{av} = \frac{W}{t}$$

and the **instantaneous power** is the limit as the interval shrinks:

$$P = \frac{dW}{dt}$$

The SI unit is the **watt**: $1\,\text{W} = 1\,\text{J/s}$. The older unit still stuck to engines is the **horsepower**, with $1\,\text{hp} = 746\,\text{W}$.

![A graph of work done against time: the work curve rises ever more steeply, a dashed chord across the whole interval marks the average power, and a tangent at the final instant marks the instantaneous power](figures/power/work-vs-time-curve.svg "Power is the slope. The dashed chord's slope is the average power over the interval; the tangent's slope is the instantaneous power at that moment.")

Read that graph as the definition made visible: average power is the slope of the **chord**, instantaneous power the slope of the **tangent**. They are equal only when the work is delivered at a steady rate.

Now the form that answers Nayan. In a small time $dt$ a force $\vec{F}$ acting on a body that moves $d\vec{s}$ does work $dW = \vec{F} \cdot d\vec{s}$, so

$$P = \frac{\vec{F} \cdot d\vec{s}}{dt} = \vec{F} \cdot \vec{v} = Fv\cos\theta$$

**Power is force times velocity.** Turn it around: at a given power, $F = P/v$. A shorter final drive multiplies the force at the wheels, so out of the hairpin — where $v$ is small — Nayan has more push. But the same gearing means the engine reaches its limit at a lower road speed, so along the straight there is nothing left. The *power* never changed; only the trade between force and speed did. That trade is the entire reason cars have gearboxes.

Being a scalar product, $P$ is negative when the force opposes the motion: brakes and drag take energy out at a rate of $Fv$ too.

## Worked example

**Given** (illustrative): a club car of mass $m = 1000\,\text{kg}$ accelerates uniformly from rest to $30\,\text{m/s}$ in $10\,\text{s}$ on a level track. Ignore drag and friction, so all the work goes into kinetic energy. Take $1\,\text{hp} = 746\,\text{W}$.
**Find:** the average power over the run, and the instantaneous power at the very end.

*Work done.* Starting from rest, it is the kinetic energy gained:

$$W = \tfrac{1}{2}(1000)(30)^2 = 500 \times 900 = 450\,000\,\text{J}$$

*Average power* over the ten seconds:

$$P_\text{av} = \frac{450\,000}{10} = 45\,000\,\text{W} = 45\,\text{kW} \approx 60\,\text{hp}$$

*Instantaneous power at the end.* The acceleration is $a = 30/10 = 3\,\text{m/s}^2$, so the driving force is $F = ma = 3000\,\text{N}$, and at that final instant the car is doing $30\,\text{m/s}$:

$$P = Fv = 3000 \times 30 = 90\,000\,\text{W} = 90\,\text{kW} \approx 121\,\text{hp}$$

Exactly **twice** the average — because with a steady force the power climbs in step with the speed, starting at zero and finishing at $90\,\text{kW}$, and the average of a straight climb is its midpoint.

**Sanity check:** $45\,\text{kW}$ is about forty-five electric kettles boiling at once. That is a believable amount of energy per second for a small racing car, and reassuringly far more than a person could ever produce.

## Where the picture breaks

The example quietly assumed the car could hold a constant force all the way to $30\,\text{m/s}$, which would mean the power rising steadily to $90\,\text{kW}$. A real engine does the opposite: it has a roughly *fixed* maximum power, so the force at the wheels falls as $P/v$ and acceleration fades as speed builds — the reason the last $20\,\text{km/h}$ always takes so long. Ignoring drag flatters the figures badly, since air resistance grows steeply with speed and the power needed to push through it grows faster still. And "engine power" quoted for a car is measured at the engine; some is lost in the gearbox and driveshafts before it reaches the road, so the number at the wheels is always smaller.

## Key takeaway

Power is the rate of doing work: $P_\text{av} = W/t$ and $P = dW/dt$, measured in watts, with $1\,\text{hp} = 746\,\text{W}$. On a work–time graph it is the slope — chord for average, tangent for instantaneous. The most useful form is $P = \vec{F} \cdot \vec{v}$, which says that at a fixed power, force and speed trade against each other.
