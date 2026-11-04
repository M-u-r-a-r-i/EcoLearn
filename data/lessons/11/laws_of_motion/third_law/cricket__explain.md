---
concept_id: third_law
interest: cricket
format: explain
title: If the ball pushes back on the bat, why does it fly?
check:
  question: |-
    During a drive, the bat pushes the ball towards the boundary. At the same instant, the ball exerts a force on the bat that is:
  options:
    A: |-
      smaller than the bat's push, because the ball is much lighter than the bat
    B: |-
      zero, because the ball is moving away from the bat
    C: |-
      equal in size and opposite in direction, and it acts on the bat
    D: |-
      equal in size and opposite in direction, and it acts on the ball, cancelling the bat's push
  answer: C
  explanation: |-
    By Newton's third law the two forces are equal and opposite, but they act on different bodies: one on the ball, one on the bat. Forces on different bodies can never cancel each other.
  misconceptions:
    A: |-
      Thinks the heavier or "stronger" body exerts the bigger force. The forces are always equal; the lighter ball just accelerates more because of its smaller mass.
    B: |-
      Thinks a body can only push back if it is resisting or at rest. While in contact, the ball pushes on the bat however it is moving.
    D: |-
      Puts both forces of the pair on the same body. If they acted on the ball they would cancel and it could never move; they don't, because the reaction acts on the bat.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A batter drives the ball back past the bowler in a floodlit stadium](scenes/cricket/laws_of_motion.svg "In the instant of contact, the bat pushes the ball and the ball pushes the bat.")

Physics period is over but the argument has followed Nisha and Siddharth to the school nets.

"Newton's third law," Siddharth says, tapping his bat on the crease. "Every action has an equal and opposite reaction. So when I hit the ball, the ball hits my bat back just as hard."

"Fine," says Nisha, running in to bowl.

He drives her full ball back past her, all along the ground. "See? But that's my problem. If the bat pushes the ball forward and the ball pushes back just as hard, the two pushes are equal and opposite. They should cancel. So why did the ball go anywhere at all?"

Nisha picks the ball up at the fence and doesn't have an answer. The law is supposed to be right. The ball definitely moved. What has Siddharth got wrong?

## The physics

**Newton's third law:** whenever body A exerts a force on body B, body B exerts a force on body A that is equal in size and opposite in direction.

$$\vec{F}_\text{AB} = -\vec{F}_\text{BA}$$

Here $\vec{F}_\text{AB}$ means the force *on A by B*. The two forces are called an **action–reaction pair**. They have these properties:

- They are **equal in size and opposite in direction**, always, whatever the masses and whether the bodies are moving, speeding up or at rest.
- They act **at the same instant**. "Action" and "reaction" are just labels; neither comes first.
- They are the **same kind** of force (here both are contact forces).
- They act on **different bodies**. This is the key.

Siddharth's mistake is in the last point. Forces cancel only when they act on the *same* body and you add them to find that body's net force. The bat's push acts on the ball. The ball's push acts on the bat. To decide how the ball moves, you look only at forces **on the ball**, and the bat's push is by far the biggest of those. So the ball accelerates towards the boundary. The ball's push on the bat belongs in a different sum, the one for the bat, where it slows the bat's swing a little.

![Body A and body B drawn slightly apart: a red arrow on B points right, labelled force on B by A, and an equal red arrow on A points left, labelled force on A by B](figures/third_law/action-reaction-pair.svg "Here A is the bat and B is the ball. Each force sits on a different body, so the pair can never cancel.")

Two more pairs on the same field:

- **Running between the wickets.** Your spikes push the ground backwards; the ground pushes you forwards. That forward push from the ground is what accelerates you.
- **The ball resting on the pitch.** Earth pulls the ball down (its weight); the ball pulls Earth up with an equal force. That is one pair. The ball presses down on the pitch; the pitch pushes the ball up (the normal force). That is a *different* pair. Weight and normal force are equal here, but they are **not** an action–reaction pair: they act on the same body, the ball, and are different kinds of force.

## Worked example

**Given:** during a drive the average force of the bat on the ball is $6.0 \times 10^{3}\,\text{N}$ towards the bowler (illustrative). Ball mass $0.16\,\text{kg}$; bat mass about $1.2\,\text{kg}$.
**Find:** the force of the ball on the bat, and the acceleration each force alone would give its body.

*Third law.* The force on the bat by the ball is $6.0 \times 10^{3}\,\text{N}$, directed back towards the batter.

*Effects,* using $a = F/m$ for each body separately:

$$a_\text{ball} = \frac{6.0 \times 10^{3}}{0.16} = 3.75 \times 10^{4}\,\text{m/s}^2$$

$$a_\text{bat} = \frac{6.0 \times 10^{3}}{1.2} = 5.0 \times 10^{3}\,\text{m/s}^2$$

Equal forces, very different effects: the ball's acceleration is $7.5$ times the bat's, exactly the mass ratio $1.2/0.16 = 7.5$.

**Sanity check:** the product $m \times a$ is the same for both: $0.16 \times 3.75 \times 10^{4} = 6.0 \times 10^{3}$ and $1.2 \times 5.0 \times 10^{3} = 6.0 \times 10^{3}$. ✓

## Where the picture breaks

The bat is not a free body: the batter's hands push on it throughout the swing, so its real acceleration is set by the net force of the hands *and* the ball, not by the ball alone. The $a_\text{bat}$ above is only what the ball's push would do by itself. Real contact forces also rise and fall within about a millisecond; the third law holds at every instant of that, not just on average. And we've drawn the bat and ball apart for clarity; in reality they touch, which is exactly when the forces exist.

## Key takeaway

Forces come in pairs: if A pushes B, then B pushes A with a force equal in size and opposite in direction, $\vec{F}_\text{AB} = -\vec{F}_\text{BA}$. The two forces act on different bodies, so they never cancel. To find how one body moves, add up only the forces acting on that body.
