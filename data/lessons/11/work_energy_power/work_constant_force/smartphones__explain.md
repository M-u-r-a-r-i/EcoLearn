---
concept_id: work_constant_force
interest: smartphones
format: explain
title: The charging cart and the box of phones
check:
  question: |-
    A tablet charging cart is pulled along a level corridor by a strap angled at $60^\circ$ above the floor. The strap's tension is a steady $30\,\text{N}$ and the cart moves $4.0\,\text{m}$. How much work does the strap do on the cart?
  options:
    A: |-
      $120\,\text{J}$
    B: |-
      $104\,\text{J}$
    C: |-
      $60\,\text{J}$
    D: |-
      $0\,\text{J}$
  answer: C
  explanation: |-
    Only the part of the force along the displacement does work: $W = Fd\cos\theta = 30 \times 4.0 \times \cos 60^\circ = 30 \times 4.0 \times 0.5 = 60\,\text{J}$.
  misconceptions:
    A: |-
      Multiplies force by distance, $30 \times 4.0$, ignoring the angle. That is only right when the force points exactly along the motion; here half of it is lifting, not pulling forward.
    B: |-
      Uses $\sin 60^\circ$ instead of $\cos 60^\circ$. The angle is measured from the displacement, so the part along the motion is $F\cos\theta$; $F\sin\theta$ is the upward part, which does no work.
    D: |-
      Thinks a force does work only if it points exactly along the motion. A slanted force still does work through its component along the displacement; only a force at exactly $90^\circ$ does none.
author: claude-code/opus-5
written: 2026-09-25
---
## The story

![A living room in the evening: a camera drone climbs straight up, a phone falls from a shelf towards a cushion, an earbuds case is whirled on a lanyard in a vertical circle, and a robot vacuum rolls towards a sofa leg](scenes/smartphones/work_energy_power.svg "Things in this room are being pushed, lifted and pulled. Only some of those forces are doing work.")

It is the last period, and Priya and Sameer have been sent to return the class's tablets to the computer lab at the other end of the corridor.

Priya gets the charging cart — a metal cabinet on wheels, full of tablets plugged into their slots. She loops its strap over her shoulder and hauls it along, leaning forward. Sameer gets the spare box of phones for the robotics club, which he carries level in both arms, walking beside her.

By the lab door Sameer's arms are aching. "I did more work than you," he says. "You had wheels."

Priya, who has just read the chapter, laughs. "On that box? You did no work at all."

Sameer is offended. His arms are burning. How can holding something up all the way down a corridor count as *no* work — and how much did Priya's slanted strap actually do?

## The physics

The **work** done by a constant force $\vec{F}$ on a body that moves through a displacement $\vec{d}$ is the scalar product

$$W = \vec{F} \cdot \vec{d} = Fd\cos\theta$$

where $\theta$ is the angle between the force and the displacement. Work is a scalar, measured in **joules**: $1\,\text{J} = 1\,\text{N m}$. Only the component of the force *along* the displacement, $F\cos\theta$, does work.

![Three panels: a force at an angle theta to the displacement does positive work; weight and the normal force, perpendicular to the displacement, do zero work; friction, opposite to the displacement, does negative work](figures/work_constant_force/work-sign-cases.svg "Compare each force with the displacement. Along it: positive work. Perpendicular to it: none. Against it: negative.")

- $0 \le \theta < 90^\circ$: $W > 0$ — the force helps the motion (Priya's strap).
- $\theta = 90^\circ$: $W = 0$ — the force neither helps nor hinders (the cart's weight and the floor's push; Sameer's upward push on the box, which moves sideways).
- $90^\circ < \theta \le 180^\circ$: $W < 0$ — the force takes energy away (friction on the cart's wheels).

Sameer's arms really are working — muscles use energy just to stay tense — but that energy goes into heat inside his body, not into the box. The physics definition asks only what his force does *to the box*.

## Worked example

**Given:** Priya's strap pulls with $F = 20\,\text{N}$ at $\theta = 60^\circ$ above the floor; the cart rolls $d = 10\,\text{m}$ at a steady speed (illustrative numbers).
**Find:** the work done by the strap, and by the rolling resistance.

1. *The strap:* $W_\text{strap} = Fd\cos\theta = 20 \times 10 \times \cos 60^\circ = 20 \times 10 \times 0.5 = 100\,\text{J}$. Only $10\,\text{N}$ of her pull points along the corridor; the upward part of the pull just eases the cart's weight a little and does no work.
2. *The resistance:* at steady speed, the forward pull of $20 \times 0.5 = 10\,\text{N}$ is balanced by $10\,\text{N}$ of resistance pointing backwards ($\theta = 180^\circ$), so $W_\text{res} = 10 \times 10 \times (-1) = -100\,\text{J}$.
3. *Weight and floor:* both vertical, at $90^\circ$ to the motion, so each does $0\,\text{J}$. So does Sameer's upward push on his box.

**Sanity check:** $100\,\text{J}$ is about what it takes to lift a $1\,\text{kg}$ bag of sugar ten metres — a modest job, spread over a corridor, which fits a cart that rolls easily.

## Where the picture breaks

We treated the pull as perfectly steady and the angle as fixed; in real walking both wobble, so $100\,\text{J}$ is an average. A cart also isn't a point: its wheels turn, and some of the "resistance" is losses in the wheel bearings rather than one neat friction force. And the story's lesson about Sameer is about the *physics* meaning of work — his tired arms are real, but that is chemistry and biology, which this definition deliberately leaves out.

## Key takeaway

The work done by a constant force is $W = \vec{F} \cdot \vec{d} = Fd\cos\theta$. It is positive when the force has a component along the motion, zero when the force is perpendicular to the motion, and negative when it opposes the motion.
