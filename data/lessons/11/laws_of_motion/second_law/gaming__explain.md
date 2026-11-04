---
concept_id: second_law
interest: gaming
format: explain
title: More engine or less weight in the racing game garage
check:
  question: |-
    A $1000\,\text{kg}$ car in a racing game with realistic physics has a net forward force of $3000\,\text{N}$ on it. A lightweight upgrade reduces its mass to $750\,\text{kg}$, with the same net force. Its acceleration becomes:
  options:
    A: |-
      $3.0\,\text{m/s}^2$
    B: |-
      $2.25\,\text{m/s}^2$
    C: |-
      $0.25\,\text{m/s}^2$
    D: |-
      $4.0\,\text{m/s}^2$
  answer: D
  explanation: |-
    For constant mass, $a = \dfrac{F_\text{net}}{m} = \dfrac{3000\,\text{N}}{750\,\text{kg}} = 4.0\,\text{m/s}^2$. The same force on a smaller mass gives a larger acceleration.
  misconceptions:
    A: |-
      Keeps the old acceleration ($3000/1000$), as if mass had no effect once the force is fixed. Acceleration is inversely proportional to mass.
    B: |-
      Scales the acceleration by the mass ratio the wrong way ($3.0 \times 0.75$), as if less mass meant less acceleration. Halving the mass doubles the acceleration.
    C: |-
      Inverts the formula and computes $m/F$. The second law is $a = F/m$; check the units: N/kg gives m/s².
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A gaming desk at night: a racing game on the monitor and a zero-gravity game on a tablet](scenes/gaming/laws_of_motion.svg "Every frame, the game works out how the net force on the kart changes its velocity.")

Priya has saved up enough in-game credits for exactly one upgrade before tonight's online race. In the garage menu, two cards glow at her.

*Engine tune: +20% drive force.*
*Carbon chassis: −20% mass.*

"Same thing," says her friend Arjun over voice chat. "Twenty per cent either way. Just pick the cheaper one."

Priya hovers over the cheaper card, the engine tune. Then she stops. The game claims its physics is realistic, and she remembers her cousin, who plays with modding tools, saying the engine literally calculates a new speed for every car sixty times a second from the forces on it.

If that's true, then the two upgrades are just two numbers going into the same calculation. So are they really the same? And if not, which one launches her faster off the start line?

## The physics

**Newton's second law** says the net external force on a body equals the rate of change of its momentum:

$$\vec{F}_\text{net} = \frac{d\vec{p}}{dt}$$

For a body whose mass stays constant, $\vec{p} = m\vec{v}$ and $\dfrac{d\vec{v}}{dt} = \vec{a}$, so this becomes the familiar

$$\vec{F}_\text{net} = m\vec{a}$$

- $\vec{F}_\text{net}$ is the **vector sum of all forces** on the body, in newtons; $m$ in kg; $\vec{a}$ in m/s². One newton is the net force that gives $1\,\text{kg}$ an acceleration of $1\,\text{m/s}^2$.
- The acceleration points in the direction of the **net** force.
- $F = ma$ holds for constant mass in an inertial frame. When mass changes, as with a rocket burning fuel, use the momentum form.

For Priya's car, the net force is the drive force from the road on the tyres minus air drag and rolling resistance. The acceleration it produces is $a = F_\text{net}/m$. That is exactly what a physics engine does: each step of $1/60\,\text{s}$, it adds $\dfrac{F_\text{net}}{m} \times \dfrac{1}{60}\,\text{s}$ to the car's velocity.

![Two graphs: at fixed mass, acceleration rises in a straight line with force; at fixed force, acceleration falls along a curve as mass increases](figures/second_law/force-mass-acceleration.svg "Left: acceleration is proportional to net force. Right: for the same force it falls along a curve as mass grows, so it is inversely proportional to mass, not decreasing in a straight line.")

The graphs show why the two upgrades differ. Multiplying $F$ by $1.2$ multiplies $a$ by $1.2$. But multiplying $m$ by $0.8$ multiplies $a$ by $\dfrac{1}{0.8} = 1.25$. Cutting mass by 20% helps a little more than adding 20% force.

## Worked example

**Given (illustrative values):** Priya's car has $m = 800\,\text{kg}$ and a net forward force of $4000\,\text{N}$ off the start line, assumed constant. The engine updates $60$ times per second.
**Find:** (a) the acceleration; (b) the speed gained per physics step and after $3.0\,\text{s}$ from rest; (c) the acceleration with each upgrade.

(a) $a = \dfrac{F_\text{net}}{m} = \dfrac{4000\,\text{N}}{800\,\text{kg}} = 5.0\,\text{m/s}^2$.

(b) Per step: $\Delta v = a\,\Delta t = 5.0 \times \dfrac{1}{60} \approx 0.083\,\text{m/s}$. After $3.0\,\text{s}$: $v = at = 5.0 \times 3.0 = 15\,\text{m/s} = 54\,\text{km/h}$.

(c) Engine tune: $F = 1.2 \times 4000 = 4800\,\text{N}$, so $a = \dfrac{4800}{800} = 6.0\,\text{m/s}^2$.
Carbon chassis: $m = 0.8 \times 800 = 640\,\text{kg}$, so $a = \dfrac{4000}{640} = 6.25\,\text{m/s}^2$.

The chassis wins, by a small margin.

**Sanity check:** use the momentum form. In $3.0\,\text{s}$ the car's momentum rises from $0$ to $800 \times 15 = 12\,000\,\text{kg m/s}$, so $\dfrac{\Delta p}{\Delta t} = \dfrac{12\,000}{3.0} = 4000\,\text{N}$, the force we started with ✓. Also $3.0\,\text{s}$ is $180$ steps, and $180 \times 0.083 \approx 15\,\text{m/s}$ ✓.

## Where the picture breaks

A real net force is not constant: air drag grows with speed, and a car's drive force depends on its gear. Real tyres can also only push as hard as their grip allows; a lighter car presses less on the road, so it may have less grip to use, and the menu's "20% lighter" might cost you somewhere else. Game designers may also tune cars with extra rules that aren't physics at all. And the engine's small time steps approximate smooth change; they give the exact answer here only because we assumed the force was constant.

## Key takeaway

The net force on a body equals its rate of change of momentum, $\vec{F}_\text{net} = d\vec{p}/dt$; for constant mass this is $\vec{F}_\text{net} = m\vec{a}$. Acceleration is proportional to the net force and inversely proportional to the mass, and it points along the net force.
