---
concept_id: second_law
interest: motorsport
format: explain
title: The same engine, one hundred and fifty kilograms lighter
check:
  question: |-
    A car of mass $1200\,\text{kg}$ slows steadily from $30\,\text{m/s}$ to rest in $6.0\,\text{s}$ under braking. What is the average net force on it?
  options:
    A: |-
      $6000\,\text{N}$, directed backwards
    B: |-
      $6000\,\text{N}$, directed forwards
    C: |-
      $36\,000\,\text{N}$, directed backwards
    D: |-
      $5.0\,\text{N}$, directed backwards
  answer: A
  explanation: |-
    The acceleration is $a = \Delta v/\Delta t = 30/6.0 = 5.0\,\text{m/s}^2$ backwards, so $F_\text{net} = ma = 1200 \times 5.0 = 6000\,\text{N}$, backwards — the same way as the acceleration.
  misconceptions:
    B: |-
      Gets the size right but points the force the way the car is moving. Net force points along the *acceleration*, and a slowing car accelerates backwards.
    C: |-
      Calculates the change in momentum, $1200 \times 30 = 36\,000\,\text{kg m/s}$, and calls it a force. Force is the change in momentum *per second*, so divide by the $6.0\,\text{s}$.
    D: |-
      Works out the acceleration, $5.0\,\text{m/s}^2$, and writes it down with the unit newton. Acceleration only becomes a force after multiplying by the mass.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A race car in a braking zone with glowing brake discs, a skid mark and tyre smoke, a tyre barrier along the wall and a marshal with a yellow flag](scenes/motorsport/laws_of_motion.svg "Hard braking and hard acceleration are the same law read in two directions.")

On a club test day at a small circuit, Vikram is the junior mechanic, and his job is the stopwatch. His driver, Fatima, pulls in after six laps and says the car feels lazy out of the last corner — "like someone's sitting on the back."

The team check the engine anyway. Same boost, same throttle trace, same tyres, same corner. Then the chief mechanic points at the car instead of the engine. It has been running in a heavier class all morning, with lead ballast plates bolted under the seat and the tank brimmed for a long run.

They unbolt the plates and drain the tank to a quarter. About $150\,\text{kg}$ lighter, the same car, on the same corner, with the same throttle, fires out of the exit noticeably harder, and the stopwatch agrees.

Nothing about the push changed. So why did the motion change — and by exactly how much?

## The physics

Newton's second law links force to the change it makes in motion. In its general form:

$$\vec{F}_\text{net} = \frac{d\vec{p}}{dt}$$

The **net force** on a body equals the rate of change of its **momentum** $\vec{p} = m\vec{v}$. When the mass stays constant, $m$ comes outside the derivative and $d\vec{v}/dt$ is the acceleration, giving the familiar form:

$$\vec{F}_\text{net} = m\vec{a}$$

Three things worth reading slowly:

- It is the **net** force — the vector sum of everything acting on the body. Out of a corner that means the road's forward push on the driven tyres *minus* air drag and rolling resistance.
- Force and acceleration point the **same way**. Under braking the net force points backwards, which is why the car slows.
- For a given net force, more mass means less acceleration: $a = F_\text{net}/m$. Mass is exactly the measure of how stubbornly a body resists being accelerated, so removing $150\,\text{kg}$ changes the car's response even though the engine is untouched.

![Two graphs: with the mass fixed, acceleration rises in a straight line as the net force grows; with the force fixed, acceleration falls along a curve as the mass grows](figures/second_law/force-mass-acceleration.svg "Left: same mass, so acceleration is proportional to net force. Right: same force, so doubling the mass halves the acceleration. The numbers are small for clarity; the shapes are what matter.")

The SI unit of force is defined by this law: $1\,\text{N} = 1\,\text{kg}\,\text{m/s}^2$, the force that gives a one-kilogram body an acceleration of one metre per second squared. Newton set the law down in 1687, writing that the change of motion is proportional to the force impressed and happens in the direction of that force. By "motion" he meant momentum.

![The Latin title page of Newton's Principia Mathematica, printed in London in 1687](famous/newton-principia-title-page.jpg "Newton's three laws of motion were published in the Principia in 1687. Public domain, via Wikimedia Commons.")

## Worked example

**Given:** the net forward force on the car is $F_\text{net} = 6000\,\text{N}$ and is taken as constant over a short burst (illustrative). Mass with ballast and a full tank, $m_1 = 750\,\text{kg}$; after stripping $150\,\text{kg}$, $m_2 = 600\,\text{kg}$.
**Find:** the acceleration in each case, and the time each version takes to gain $20\,\text{m/s}$ of speed.

*Heavy car.*

$$a_1 = \frac{F_\text{net}}{m_1} = \frac{6000}{750} = 8.0\,\text{m/s}^2$$

That means the car picks up $8\,\text{m/s}$ of speed every second — nearly $29\,\text{km/h}$ per second.

*Light car.*

$$a_2 = \frac{6000}{600} = 10\,\text{m/s}^2$$

A quarter more acceleration, from exactly the same push.

*Time to gain $20\,\text{m/s}$* (that is $72\,\text{km/h}$), using $t = \Delta v / a$:

$$t_1 = \frac{20}{8.0} = 2.5\,\text{s} \qquad t_2 = \frac{20}{10} = 2.0\,\text{s}$$

**Sanity check:** half a second saved on every corner exit is exactly the sort of gain a driver feels, and $8$–$10\,\text{m/s}^2$ is about the acceleration of gravity, which is a believable figure for a car with racing tyres.

## Where the picture breaks

We held the net force fixed while the mass fell, and that is the idealisation. A lighter car presses less hard on the road, so the maximum grip its tyres can give also drops — part of the gain is given back. The real driving force is not constant either: it changes with gear and engine speed, and air drag grows quickly with speed, so a steady $6000\,\text{N}$ is only a short-burst average. And $\vec{F}_\text{net} = m\vec{a}$ assumes constant mass. A car burning fuel loses mass slowly enough that this is harmless lap by lap, but for something like a rocket you must go back to $\vec{F}_\text{net} = d\vec{p}/dt$.

## Key takeaway

The net force on a body equals its rate of change of momentum, $\vec{F}_\text{net} = d\vec{p}/dt$, which for constant mass becomes $\vec{F}_\text{net} = m\vec{a}$. Acceleration points along the net force and is inversely proportional to mass, so taking weight out of a car makes it accelerate and brake harder with no change to the engine at all.
