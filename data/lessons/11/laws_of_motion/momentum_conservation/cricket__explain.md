---
concept_id: momentum_conservation
interest: cricket
format: explain
title: The bowling machine that rolls backwards
check:
  question: |-
    A bowling machine sits on a trolley with smooth wheels; together they have a mass of $48\,\text{kg}$ and start at rest. The machine fires a $0.16\,\text{kg}$ ball forwards at $30\,\text{m/s}$. Ignoring friction, the trolley moves off at:
  options:
    A: |-
      $0.10\,\text{m/s}$ backwards
    B: |-
      $30\,\text{m/s}$ backwards
    C: |-
      $0\,\text{m/s}$, because the trolley is far heavier than the ball
    D: |-
      $0.10\,\text{m/s}$ forwards
  answer: A
  explanation: |-
    The total momentum starts at zero and stays zero: $0.16 \times 30 + 48\,V = 0$, so $V = -4.8/48 = -0.10\,\text{m/s}$. The minus sign means backwards.
  misconceptions:
    B: |-
      Thinks the two bodies get equal and opposite velocities. It is their momenta that are equal and opposite, so the heavier body moves far more slowly.
    C: |-
      Thinks a heavy body simply "absorbs" the kick and doesn't move. A heavy body recoils slowly, but with no friction its momentum must balance the ball's.
    D: |-
      Gets the size right but loses the sign. For the total to stay zero, the trolley's momentum must point opposite to the ball's.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A batter drives the ball back past the bowler in a floodlit stadium](scenes/cricket/laws_of_motion.svg "Every hit and every catch is a collision, and in every one of them some momentum changes hands.")

The academy has a new bowling machine, and it arrives on a wheeled trolley so the groundstaff can move it between nets. Zoya, the youngest in the squad, is the one who notices something the adults ignore. Every time the machine fires, the whole trolley gives a tiny nudge backwards.

Later, at fielding practice, she sees it again in a different form. Her teammate Aditya, standing at point, jumps straight up to snatch a flat, hard cut. He catches it at the top of his jump — and lands a couple of centimetres behind where he took off.

"The machine went back when the ball went forward," Zoya says. "Aditya went back when the ball came into him. Is that the same thing?"

Nobody pushed the trolley. Nobody pushed Aditya either. So where did their backward motion come from, and could you have predicted exactly how much?

## The physics

For a group of bodies — a **system** — add up all their momenta to get the total momentum. Inside the system, bodies push on one another, but by Newton's third law those internal forces come in equal and opposite pairs, so their impulses cancel in the total. Only **external** forces can change the total momentum.

**Law of conservation of linear momentum:** if the net external force on a system is zero (an **isolated system**), its total momentum stays constant:

$$m_1\vec{u}_1 + m_2\vec{u}_2 = m_1\vec{v}_1 + m_2\vec{v}_2$$

where $u$ are velocities before and $v$ after the interaction. It holds for every kind of interaction, however complicated the forces in between:

- **Recoil and explosions.** The system starts at rest, so the total momentum is zero before and after. The pieces fly apart with equal and opposite momenta. The machine pushes the ball forwards, the ball pushes the machine backwards, and machine plus trolley recoil.
- **Collisions.** When the ball hits a fielder and sticks in his hands, ball and fielder end up moving together with the same velocity. The ball's momentum is now shared by a much bigger mass, so the pair moves slowly.

![Top: a large body and small ball at rest fly apart with equal and opposite momentum arrows. Bottom: a small ball moving into a large body at rest; afterwards they move together with the same total momentum](figures/momentum_conservation/recoil-and-sticking-collision.svg "Recoil (top) and a sticking collision (bottom). In both, the total momentum arrow is the same after as before.")

Note what is conserved: momentum, not velocity. Equal momenta shared between unequal masses give very unequal speeds.

## Worked example

Take the direction the ball travels as positive in both parts.

**Part 1, recoil.** Machine plus trolley: $M = 50\,\text{kg}$, at rest; it fires a $0.16\,\text{kg}$ ball at $25\,\text{m/s}$ (illustrative values; friction on the wheels ignored).

Before: total $p = 0$. After: $0.16 \times 25 + 50\,V = 0$.

$$V = -\frac{4.0}{50} = -0.080\,\text{m/s}$$

The trolley rolls backwards at $8\,\text{cm/s}$.

**Part 2, collision.** Aditya, $m_\text{F} = 64\,\text{kg}$, is at the top of a straight-up jump, so his horizontal velocity is zero. The $0.16\,\text{kg}$ ball arrives horizontally at $30\,\text{m/s}$ and stays in his hands. In the air, no horizontal external force acts (air drag neglected), so horizontal momentum is conserved:

$$0.16 \times 30 + 64 \times 0 = (64 + 0.16)\,V$$

$$V = \frac{4.8}{64.16} \approx 0.075\,\text{m/s}$$

He drifts backwards (in the ball's direction) at about $7.5\,\text{cm/s}$. If he takes about a quarter of a second to drop back down after the catch, that is about $0.075 \times 0.25 \approx 0.02\,\text{m}$, or $2\,\text{cm}$ — the small shift Zoya saw.

**Sanity check:** in Part 1, the ball's momentum is $+4.0\,\text{kg m/s}$ and the trolley's is $50 \times (-0.080) = -4.0\,\text{kg m/s}$; the total is zero. ✓ In Part 2, $64.16 \times 0.075 \approx 4.8\,\text{kg m/s}$. ✓

## Where the picture breaks

Conservation needs zero **net external** force. The trolley's wheels have some friction, and the machine may be braked or pegged down, so a real trolley moves even less or not at all: the ground has joined the system. Aditya's momentum is conserved only while he is in the air; once his feet touch the ground, friction from the turf acts. His catch also isn't instantaneous, and his arms move relative to his body, but none of that changes the total. Vertically, gravity is an external force, so vertical momentum is *not* conserved during the jump; only the horizontal part is.

## Key takeaway

If no net external force acts on a system, its total momentum stays the same: $m_1\vec{u}_1 + m_2\vec{u}_2 = m_1\vec{v}_1 + m_2\vec{v}_2$. In recoil and explosions the total starts at zero, so the pieces get equal and opposite momenta. In a collision the momentum is shared, so a heavy body that is hit moves off slowly.
