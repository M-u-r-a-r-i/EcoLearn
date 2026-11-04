---
concept_id: work_constant_force
interest: motorsport
format: explain
title: Why a high tow rope makes the pushing harder
check:
  question: |-
    A tow rope drags a stalled kart $30\,\text{m}$ along a level pit road. The tension in the rope is a steady $100\,\text{N}$ and the rope is held at $60^\circ$ to the road. How much work does the rope do on the kart?
  options:
    A: |-
      $3000\,\text{J}$
    B: |-
      $1500\,\text{J}$
    C: |-
      $2600\,\text{J}$
    D: |-
      $0\,\text{J}$
  answer: B
  explanation: |-
    Only the component of the tension along the motion does work: $W = Fd\cos\theta = 100 \times 30 \times \cos 60^\circ = 100 \times 30 \times 0.5 = 1500\,\text{J}$.
  misconceptions:
    A: |-
      Uses $W = Fd$ and ignores the angle. The full $100\,\text{N}$ is not pointing along the road, so only part of it counts.
    C: |-
      Uses $\cos 30^\circ$ — the angle measured from the vertical instead of from the displacement. In $W = Fd\cos\theta$, $\theta$ is always the angle between the force and the displacement.
    D: |-
      Confuses "at an angle to the motion" with "perpendicular to the motion". Only a force at exactly $90^\circ$ does no work; at $60^\circ$ half of it still pulls the kart forward.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A race track scene: a car coasts down a hill road onto the circuit, a second car speeds along the straight with a velocity arrow, a third brakes with glowing red discs, and two people push a kart in the foreground](scenes/motorsport/work_energy_power.svg "The two people pushing the kart in front are doing the most honest work in this picture.")

Practice ends at the karting club and one kart will not restart. It is stuck at the far end of the circuit, and the recovery tractor has gone home, so Bhaskar and Rukmini get a rope and start dragging it back.

Bhaskar loops the rope over his shoulder and leans forward, so the rope runs steeply up from the kart's nose to his chest. "Higher is better," he says. "You get your weight into it."

Twenty metres later he is gasping. Rukmini takes over, and instead crouches so the rope runs almost flat along the ground. Same rope, same kart, same speed — and it feels distinctly easier.

Bhaskar is unimpressed. "You're pulling with the same force I was. The kart moves the same distance. How can it possibly be easier?"

## The physics

When a **constant force** $\vec{F}$ acts on a body that undergoes a displacement $\vec{d}$, the **work** done by that force is the scalar product

$$W = \vec{F} \cdot \vec{d} = Fd\cos\theta$$

where $\theta$ is the angle between the force and the displacement. Work is a **scalar**. Its SI unit is the **joule** ($1\,\text{J} = 1\,\text{N}\,\text{m}$), and one joule is roughly the work of lifting a $100\,\text{g}$ apple by one metre.

Read the $\cos\theta$ carefully, because it is the whole lesson:

- $\theta < 90^\circ$ — the force has a part along the motion, so $W$ is **positive**: that force is feeding energy into the body.
- $\theta = 90^\circ$ — the force is perpendicular to the motion and $W$ is **exactly zero**, no matter how large the force is.
- $\theta > 90^\circ$ — the force opposes the motion and $W$ is **negative**: that force is taking energy out.

![Three panels: a block pulled by a force at angle theta does positive work; weight and normal force perpendicular to the displacement do zero work; friction opposite to the displacement does negative work](figures/work_constant_force/work-sign-cases.svg "Compare each force's direction with the displacement. Along it: positive work. Perpendicular: none. Against it: negative.")

That middle case is worth a moment. As the kart rolls along level ground, its **weight** points straight down and the road's **normal force** points straight up, while the displacement is horizontal. Both are at $90^\circ$ to the motion, so both do **zero work** — a force can be enormous and still do nothing, if it never points where the body is going.

Bhaskar's steep rope is the first case, badly used. With the rope at $60^\circ$ the useful component is $F\cos 60^\circ$, only half the tension; the rest is pulling the kart's nose upwards, doing nothing to move it forward. Rukmini's flatter rope puts far more of the same tension along the road.

Two conditions: this formula needs the force to be **constant** in magnitude and direction, and the displacement to be a **straight line**. If either changes, you must break the motion into small pieces — which is the next concept.

## Worked example

**Given:** the rope tension is $F = 200\,\text{N}$, held at $\theta = 60^\circ$ to the road; the kart is dragged $d = 20\,\text{m}$ along a level pit road; rolling resistance opposes the motion with a steady $50\,\text{N}$ (illustrative values).
**Find:** the work done by the rope, by the resistance, by the weight, and the net work.

*The rope.* The angle between the tension and the displacement is $60^\circ$, and $\cos 60^\circ = 0.5$:

$$W_\text{rope} = 200 \times 20 \times 0.5 = 2000\,\text{J}$$

Half the pull is wasted lifting the nose; only $100\,\text{N}$ of the $200\,\text{N}$ works along the road.

*The rolling resistance.* It points exactly backwards, so $\theta = 180^\circ$ and $\cos 180^\circ = -1$:

$$W_\text{res} = 50 \times 20 \times (-1) = -1000\,\text{J}$$

Negative — this force is draining energy away as the tyres and bearings warm up.

*The weight and the normal force.* Both are vertical, the motion is horizontal, so $\cos 90^\circ = 0$ and each does $0\,\text{J}$.

*Net work:* $2000 - 1000 + 0 + 0 = 1000\,\text{J}$.

**Sanity check:** $2000\,\text{J}$ is about what you spend lifting a $20\,\text{kg}$ sack of rice ten metres up a staircase — a real effort, but not an impossible one, which matches twenty metres of dragging a kart.

## Where the picture breaks

Real rope-pulling is not this tidy. The tension wobbles as you walk, the angle changes as you move away from the kart, and the pit road is never perfectly level — so $W = Fd\cos\theta$ is an average over the pull, not an exact account. Rolling resistance is only roughly constant; it changes with tyre pressure and with speed. The formula also says nothing about how *tired* you get: holding a heavy load still, or pushing against a kart that will not budge, does zero physical work by this definition while your muscles burn energy anyway. Physics work and everyday work are different words that happen to be spelled the same.

## Key takeaway

The work done by a constant force is $W = \vec{F} \cdot \vec{d} = Fd\cos\theta$, measured in joules. Its sign comes entirely from the angle between force and displacement: positive when the force helps the motion, zero when it is perpendicular, negative when it opposes. A force perpendicular to the motion — like weight on a level road — does no work at all.
