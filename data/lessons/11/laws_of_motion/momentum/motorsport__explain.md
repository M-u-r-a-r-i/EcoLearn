---
concept_id: momentum
interest: motorsport
format: explain
title: Two cars at walking pace, one of them unstoppable
check:
  question: |-
    A $250\,\text{kg}$ single-seater rolls forwards at $4\,\text{m/s}$ into a tyre barrier and bounces straight back at $1\,\text{m/s}$. What is the magnitude of its change in momentum?
  options:
    A: |-
      $250\,\text{kg m/s}$
    B: |-
      $750\,\text{kg m/s}$
    C: |-
      $1000\,\text{kg m/s}$
    D: |-
      $1250\,\text{kg m/s}$
  answer: D
  explanation: |-
    Taking "forwards" as positive, the momentum goes from $+1000\,\text{kg m/s}$ to $-250\,\text{kg m/s}$, so $\Delta p = -250 - 1000 = -1250\,\text{kg m/s}$, of size $1250\,\text{kg m/s}$.
  misconceptions:
    A: |-
      Quotes only the momentum after the bounce. A change is final minus initial, so the starting momentum has to be in the calculation too.
    B: |-
      Subtracts the two momenta as if both pointed the same way ($1000 - 250$). The rebound reverses the direction, so the magnitudes add instead.
    C: |-
      Counts only bringing the car to rest and forgets that the barrier also has to send it back the other way.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A race car in a braking zone with glowing brake discs, a skid mark and tyre smoke, a tyre barrier along the wall and a marshal with a yellow flag](scenes/motorsport/laws_of_motion.svg "How hard a moving car is to stop depends on two things, not one.")

The college's student-formula car is finished at last, and the team is pushing it out of the workshop for a photograph. Ananya, walking beside the nose, is surprised at how light it feels: the car rolls along at a slow walking pace and she can bring it to a stop with one hand on the front wing.

Sameer, who has been lugging batteries about all morning, is unimpressed. So they try the same thing with the team's ancient support hatchback, out of gear, rolling across the same flat yard at the same slow walk. Sameer plants both hands on the boot and leans in. It shoves him back three steps before it finally stops.

"Same speed," he says, shaking out his wrists. "Exactly the same speed. Why is one of them a toy and the other one a truck?"

Then the yard's slight slope takes over, and the hatchback begins rolling back the other way at that same walking pace. Ananya looks at it and asks the sharper question: has anything about its motion actually changed?

## The physics

Speed on its own does not tell you how hard a moving body is to stop. Mass matters too. Newton put the two together in one quantity, the **linear momentum**:

$$\vec{p} = m\vec{v}$$

- $m$ is the mass in kilograms and $\vec{v}$ the velocity in metres per second.
- The SI unit is the kilogram metre per second, $\text{kg m/s}$, which is the same as the newton second, $\text{N s}$.
- Momentum is proportional to mass **and** to velocity: double either one and it doubles.

That already answers Sameer. At the same speed, the hatchback's much larger mass gives it much larger momentum, and momentum is what a pair of hands has to take away.

**Momentum is a vector.** Mass is a positive scalar, so $m\vec{v}$ points exactly along the velocity. Along a straight line you handle this with signs: pick a positive direction and anything travelling the other way has negative momentum.

So when the yard's slope sends the hatchback rolling back the other way at the same walking pace, its motion has *not* stayed the same. Its momentum has reversed, and reversal is the biggest change you can make at that speed.

![A body arriving at 25 m/s with momentum −4.0 kg m/s, then driven back at 25 m/s with momentum +4.0 kg m/s, giving a change of 8.0 kg m/s](figures/momentum/momentum-is-a-vector.svg "The body drawn here is a small ball, but the rule is general: same speed, opposite arrows, and the change in momentum is double — not zero.")

Speed matters just as much. That same $250\,\text{kg}$ single-seater at $60\,\text{m/s}$, a little over $200\,\text{km/h}$, carries $250 \times 60 = 15\,000\,\text{kg m/s}$ — thirty times what it had in the yard.

## Worked example

**Given:** the single-seater, $m_1 = 250\,\text{kg}$, and the hatchback, $m_2 = 1000\,\text{kg}$ (illustrative), each rolling at $v = 2.0\,\text{m/s}$, a slow walk.
**Find:** each car's momentum, and the change in the hatchback's momentum when it rolls back at the same speed.

*Momenta.* Take the direction they were pushed as positive.

$$p_1 = 250 \times 2.0 = 500\,\text{kg m/s} \qquad p_2 = 1000 \times 2.0 = 2000\,\text{kg m/s}$$

The hatchback carries **four times** the momentum at the same speed — the same factor as its mass. That is the whole of Sameer's complaint.

*Reversal.* Rolling back, the hatchback's momentum is $-2000\,\text{kg m/s}$.

$$\Delta p = (-2000) - (+2000) = -4000\,\text{kg m/s}$$

**Sanity check:** the same answer comes from $\Delta p = m\,\Delta v = 1000 \times (-4.0) = -4000\,\text{kg m/s}$, and the minus sign correctly points back down the yard.

## Where the picture breaks

"Hard to stop" is really two ideas wearing one coat. Momentum decides how big a push is needed to stop a body in a given time, but how much the stop *hurts* also depends on how quickly it happens — that is impulse, next — and on where the energy goes. A real car in a yard is not an isolated body either: rolling resistance and a sloping surface change its momentum all by themselves. And we have used plus and minus signs because everything moved along one line; on a race track, where a car changes direction as well as speed, momentum needs full vector components.

## Key takeaway

Linear momentum is mass times velocity, $\vec{p} = m\vec{v}$, measured in $\text{kg m/s}$. It is a vector pointing along the velocity, so a body whose direction reverses undergoes a large change in momentum even though its speed never changed. A heavy car at walking pace can carry far more momentum than a light one going faster.
