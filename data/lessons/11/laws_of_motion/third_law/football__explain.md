---
concept_id: third_law
interest: football
format: explain
title: Who pushed harder in the shoulder-to-shoulder challenge?
check:
  question: |-
    A $50\,\text{kg}$ winger and an $80\,\text{kg}$ defender collide shoulder to shoulder while chasing a ball. During the contact, the force on the winger by the defender is:
  options:
    A: |-
      larger than the force on the defender by the winger, because the defender is heavier
    B: |-
      larger than the force on the defender by the winger, because the winger is knocked further off course
    C: |-
      equal and opposite to the force on the defender, so the two forces cancel and neither player's motion changes
    D: |-
      equal in size and opposite in direction to the force on the defender by the winger
  answer: D
  explanation: |-
    By Newton's third law the two forces are equal in size and opposite in direction at every instant. They act on different players, so they don't cancel: each changes the motion of the player it acts on.
  misconceptions:
    A: |-
      Thinks the heavier or stronger body exerts the bigger force. The forces are always equal; the heavier player just accelerates less.
    B: |-
      Judges the force by its effect. The winger is knocked further because his mass is smaller, so the same size of force gives him a larger acceleration.
    C: |-
      Adds the two forces as if they acted on one body. They act on different bodies, so each one changes the motion of its own body; they never cancel.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![Under floodlights, a striker follows through after a shot while the ball flies towards the goalkeeper](scenes/football/laws_of_motion.svg "Every touch in football is a pair of forces: boot on ball and ball on boot, player on player.")

A long ball is played into the channel, and two players chase it: Mohan, the club's slight, quick winger, and Joel, a centre-back who is built like a door. They arrive together and meet shoulder to shoulder. There's a thud. Mohan is knocked sideways and stumbles two metres off his line. Joel barely wobbles, and takes the ball.

On the touchline, Mohan's friend Divya is outraged. "Foul! He shoved Mohan much harder than Mohan shoved him. Look where they both ended up."

Her classmate Arjun has just done Newton's third law in physics. "Can't be," he says. "Every action has an equal and opposite reaction. Same force both ways."

"Then they'd cancel," says Divya, "and nobody would have moved. But Mohan went flying."

Both of them sound half right. Who is?

## The physics

**Newton's third law:** whenever body A exerts a force on body B, body B exerts a force on body A that is equal in size and opposite in direction.

$$\vec{F}_\text{AB} = -\vec{F}_\text{BA}$$

Here $\vec{F}_\text{AB}$ means the force *on A by B*. The two forces are an **action–reaction pair**, and they always:

- are **equal in size and opposite in direction**, whatever the masses and however the bodies are moving;
- act **at the same instant**; "action" and "reaction" are just labels, and neither comes first;
- are the **same kind** of force (here, both contact forces);
- act on **different bodies**. This is the key.

So Arjun is right about the sizes: Joel pushed Mohan exactly as hard as Mohan pushed Joel. Divya's mistake is thinking equal and opposite forces must cancel. Forces cancel only when they act on the **same** body and you add them to find that body's net force. Joel's push acts on Mohan; Mohan's push acts on Joel. To see how Mohan moves, add up only the forces **on Mohan**.

Divya's evidence, that Mohan moved more, is real, but it is about **acceleration**, not force. By the second law, $a = F/m$. The same force on a smaller mass gives a bigger acceleration.

![Body A and body B drawn slightly apart: a red arrow on B points right, labelled force on B by A, and an equal red arrow on A points left, labelled force on A by B](figures/third_law/action-reaction-pair.svg "Think of A as Mohan and B as Joel. The two forces are equal, but each sits on a different player, so they can never cancel.")

Two more pairs from the same match:

- **Sprinting.** Your studs push the ground backwards; the ground pushes you forwards. That forward push from the ground is what accelerates you.
- **Kicking.** Your boot pushes the ball forward; the ball pushes your foot back. That is why kicking a heavy, waterlogged ball hurts your foot.

## Worked example

**Given:** during the challenge, the average contact force between the players is $600\,\text{N}$ (illustrative). Mohan's mass is $50\,\text{kg}$, Joel's $80\,\text{kg}$. Consider only this contact force, ignoring the ground.
**Find:** the force on each player and the acceleration it gives each.

*Third law.* Force on Mohan by Joel: $600\,\text{N}$, pointing away from Joel. Force on Joel by Mohan: $600\,\text{N}$, pointing away from Mohan.

*Effects,* applying $a = F/m$ to each player separately:

$$a_\text{Mohan} = \frac{600}{50} = 12\,\text{m/s}^2 \qquad a_\text{Joel} = \frac{600}{80} = 7.5\,\text{m/s}^2$$

Equal forces, unequal effects: Mohan's acceleration is $1.6$ times Joel's, the mass ratio $80/50 = 1.6$.

**Sanity check:** $50 \times 12 = 600\,\text{N}$ and $80 \times 7.5 = 600\,\text{N}$: the same force, as the third law demands ✓.

## Where the picture breaks

Real players are not free bodies. Both are standing on the ground, and their studs push on it, so the ground's friction also acts on each player. A heavier player can plant his feet, and that friction, not a bigger push, helps him stay on his line. The accelerations above are what the contact force alone would give. The contact force also rises and falls during the thud; the third law holds at every instant, not only on average. And a real referee judges a charge by other things too, such as the use of arms, that physics doesn't decide.

## Key takeaway

Forces come in pairs: if A pushes B, then B pushes A with a force equal in size and opposite in direction, $\vec{F}_\text{AB} = -\vec{F}_\text{BA}$. The two forces act on different bodies, so they never cancel. The lighter body moves more not because it is pushed harder but because the same force gives a smaller mass a larger acceleration.
