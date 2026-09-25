---
concept_id: connected_bodies
interest: smartphones
format: explain
title: The power bank that dragged the phone off the desk
check:
  question: |-
    A $0.30\,\text{kg}$ phone lies on a smooth desk. Its cable runs over the smooth edge to a $0.20\,\text{kg}$ power bank hanging freely. Taking $g = 10\,\text{m/s}^2$ and treating the cable as light and inextensible, what is the tension in the cable?
  options:
    A: |-
      $2.0\,\text{N}$
    B: |-
      $0.80\,\text{N}$
    C: |-
      $1.0\,\text{N}$
    D: |-
      $1.2\,\text{N}$
  answer: D
  explanation: |-
    For the pair, $a = \dfrac{m_2 g}{m_1 + m_2} = \dfrac{0.20 \times 10}{0.50} = 4.0\,\text{m/s}^2$. The cable is the only horizontal force on the phone, so $T = m_1 a = 0.30 \times 4.0 = 1.2\,\text{N}$.
  misconceptions:
    A: |-
      Assumes the cable holds up the power bank's full weight, as if it were hanging still. The bank is accelerating downwards, so the tension must be *less* than its weight.
    B: |-
      Uses the power bank's mass in $T = ma$ ($0.20 \times 4.0$). On the desk side, the cable is what accelerates the phone, so it is the phone's mass that belongs there.
    C: |-
      Splits the hanging weight equally between the two bodies. The weight is shared in proportion to the masses, and the phone is three-fifths of the total, not half.
author: claude-code/opus-5
written: 2026-09-25
---
## The story

![A study room at night: a camera drone hovers pushing air down, a phone tumbles off a shelf towards the tiles, and a power bank dangles off a desk by its cable](scenes/smartphones/laws_of_motion.svg "On the right, a power bank has slipped over the edge of the desk. Its cable is now dragging the phone.")

It's past midnight and Varun is revising at his study desk with the phone charging from a power bank beside it. He nudges the power bank with his elbow, and it drops over the edge of the desk. It doesn't hit the floor. It dangles by the charging cable, swinging, and the phone starts to slide — slowly at first, then faster — towards the edge.

He grabs the phone just before it follows the power bank over.

His roommate Sameer, who saw the whole thing, has a theory. "The cable was holding up the whole power bank. So it pulled the phone with the power bank's whole weight."

Varun isn't sure. If the cable were pulling the phone with the full weight of the power bank, and also holding the power bank up with that same force, then the power bank shouldn't have fallen at all — it would just hang there. But it was falling, and speeding up. So how hard was the cable really pulling?

## The physics

When bodies are joined, treat them **one body at a time**, with a free-body diagram for each, and let the connection tie the equations together.

For a **light, inextensible** string (or cable) running over a **smooth** edge or light pulley:

- the **tension** $T$ has the same size all along it;
- it can't stretch, so every body on it has the **same size of acceleration** $a$.

![A body on a smooth horizontal surface tied by a string over a pulley at the edge to a hanging body, with separate free-body diagrams: normal force, weight and tension on one; tension up and a longer weight arrow on the other](figures/connected_bodies/block-and-hanging-mass.svg "Varun's desk exactly: the phone on the table, the power bank hanging. The hanging weight arrow is longer than the tension, which is why the power bank speeds up downwards.")

Call the phone $m_1$ and the power bank $m_2$. For the phone, the only horizontal force is the cable: $T = m_1 a$. For the power bank, taking down as positive: $m_2 g - T = m_2 a$. Adding the two makes $T$ vanish:

$$a = \frac{m_2 g}{m_1 + m_2}, \qquad T = m_1 a = \frac{m_1 m_2}{m_1 + m_2}\,g$$

The tension is always **less** than the hanging weight $m_2 g$, because the power bank is accelerating downwards, and that needs a net downward force on it. Sameer's number would be right only if nothing moved.

## Worked example

**Given:** a $0.20\,\text{kg}$ phone on a smooth desk and a $0.20\,\text{kg}$ power bank hanging over the edge (illustrative). Take $g = 9.8\,\text{m/s}^2$.
**Find:** the acceleration, and the tension in the cable.

1. *Acceleration.* The hanging weight, $0.20 \times 9.8 = 1.96\,\text{N}$, has to accelerate both gadgets:
$$a = \frac{1.96}{0.20 + 0.20} = 4.9\,\text{m/s}^2$$
Exactly half of $g$ — the power bank falls, but at only half the rate of a free drop.

2. *Tension.* On the phone:
$$T = m_1 a = 0.20 \times 4.9 = 0.98\,\text{N} \approx 1.0\,\text{N}$$
Half the power bank's weight, not all of it.

**Sanity check:** on the power bank, $m_2 g - T = 1.96 - 0.98 = 0.98\,\text{N}$, and $m_2 a = 0.20 \times 4.9 = 0.98\,\text{N}$ — both equations agree.

## Where the picture breaks

A real desk is not smooth. Friction on the phone opposes the slide, so the acceleration is less than $4.9\,\text{m/s}^2$, and for a heavy phone and a light power bank it might not slide at all — you'll decide that with $f = \mu N$ in the lesson on friction. The desk edge is not a smooth pulley either: the cable rubs on it, so the tension is a little different on the two sides. Real charging cables also stretch a bit and have their own mass. And the dangling power bank swings, which adds a sideways part to the motion. The method — one body at a time, shared tension, shared acceleration — survives all of that.

## Key takeaway

For bodies joined by a light, inextensible string over a smooth pulley, use one tension and one size of acceleration for all of them, and write $F_\text{net} = ma$ for each body separately. For a body on a smooth table pulled by a hanging one, $a = \dfrac{m_2 g}{m_1 + m_2}$ and $T = \dfrac{m_1 m_2 g}{m_1 + m_2}$ — always less than the hanging weight while the system accelerates.
