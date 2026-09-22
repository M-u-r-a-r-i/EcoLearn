---
concept_id: momentum_conservation
interest: football
format: explain
title: Where two players land after a mid-air clash
check:
  question: |-
    A $60\,\text{kg}$ goalkeeper is at the top of a straight-up jump, so she has no horizontal velocity. She catches a $0.40\,\text{kg}$ ball moving horizontally at $30\,\text{m/s}$. Ignoring air drag, keeper and ball then move horizontally at about:
  options:
    A: |-
      $0.20\,\text{m/s}$, in the direction the ball was moving
    B: |-
      $30\,\text{m/s}$, in the direction the ball was moving
    C: |-
      $0\,\text{m/s}$, because the keeper is so much heavier than the ball
    D: |-
      $0.20\,\text{m/s}$, opposite to the direction the ball was moving
  answer: A
  explanation: |-
    In the air there is no horizontal external force, so horizontal momentum is conserved: $0.40 \times 30 = (60 + 0.40)\,V$, giving $V = 12/60.4 \approx 0.20\,\text{m/s}$ in the ball's original direction.
  misconceptions:
    B: |-
      Thinks the velocity is conserved and passed on unchanged. It is the momentum that is conserved, and shared by a mass 150 times bigger it gives a far smaller speed.
    C: |-
      Thinks a heavy body simply absorbs the ball's motion. Momentum can't disappear with no external force; a heavy body moves off slowly, but it does move.
    D: |-
      Gets the size right but the direction wrong. The total momentum pointed along the ball's motion before the catch, so it must point the same way after.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![Under floodlights, a striker follows through after a shot while the ball flies towards the goalkeeper](scenes/football/laws_of_motion.svg "Every catch, clash and throw passes momentum from one body to another.")

A corner swings into the box. Faizan, the striker, runs in and launches himself at it. Jaspreet, the defender marking him, has been standing still and jumps straight up. They meet in mid-air, tangle, and come down together in a heap, a good metre from where Jaspreet took off, both still gripping each other's shirts.

In the video session the next morning, the coach, Mrs D'Souza, freezes the frame at the moment of impact.

"Jaspreet jumped straight up," she says. "Nobody pushed the pair of them sideways once they were in the air. So why did they land a metre away?"

Rohit, at the back, has a different puzzle from the weekend. Standing on his skateboard in the car park, he threw a ball to a friend, and his skateboard rolled slowly backwards though nobody touched it.

Could you have predicted *how fast* in both cases, just from the masses and speeds?

## The physics

For a group of bodies (a **system**), add up their momenta to get the **total momentum**. Inside the system the bodies push on each other, but by Newton's third law those **internal** forces come in equal and opposite pairs, acting for the same time. Their impulses are equal and opposite, so they cancel in the total. Only an **external** force can change the total momentum.

**Law of conservation of linear momentum:** if the net external force on a system is zero, its total momentum stays constant.

$$m_1\vec{u}_1 + m_2\vec{u}_2 = m_1\vec{v}_1 + m_2\vec{v}_2$$

Here $u$ are the velocities before the interaction and $v$ after. The law holds however violent or complicated the forces in between.

- **Recoil and explosions.** The system starts at rest, so the total momentum is zero before and after. The pieces move off with equal and opposite momenta: Rohit's hands push the ball forwards, the ball pushes Rohit backwards.
- **Collisions.** In the mid-air clash, Faizan brings in horizontal momentum and Jaspreet brings none. When they cling together, that momentum is shared by both of them, so the pair drifts in Faizan's direction, more slowly than Faizan was moving.

![Top: a large body and small ball at rest fly apart with equal and opposite momentum arrows. Bottom: a small body moving into a large body at rest; afterwards they move together with the same total momentum](figures/momentum_conservation/recoil-and-sticking-collision.svg "Recoil (top), like Rohit's throw, and a sticking collision (bottom), like the mid-air clash. In both, the total momentum after equals the total before.")

Momentum is what is conserved, not velocity. The same momentum shared by a bigger mass means a smaller speed.

## Worked example

Take the direction of Faizan's run, and of Rohit's throw, as positive.

**Part 1, collision.** Faizan, $m_1 = 70\,\text{kg}$, moving horizontally at $4.0\,\text{m/s}$; Jaspreet, $m_2 = 80\,\text{kg}$, with zero horizontal velocity at the top of his jump (illustrative values). In the air, no horizontal external force acts (air drag neglected), and they move off together.

$$70 \times 4.0 + 80 \times 0 = (70 + 80)\,V$$

$$V = \frac{280}{150} \approx 1.9\,\text{m/s}$$

They drift in Faizan's direction at about $1.9\,\text{m/s}$. In roughly half a second in the air, that is about a metre, the shift the video showed.

**Part 2, recoil.** Rohit plus skateboard: $M = 50\,\text{kg}$, at rest. He throws a $0.43\,\text{kg}$ ball forwards at $10\,\text{m/s}$ (friction on the wheels ignored).

$$0 = 0.43 \times 10 + 50\,V \quad\Rightarrow\quad V = -\frac{4.3}{50} \approx -0.086\,\text{m/s}$$

He rolls backwards at under $9\,\text{cm/s}$.

**Sanity check:** Part 1: $150 \times 1.87 \approx 280\,\text{kg m/s}$ ✓. Part 2: $50 \times (-0.086) = -4.3\,\text{kg m/s}$, equal and opposite to the ball's $+4.3\,\text{kg m/s}$; the total stays zero ✓.

## Where the picture breaks

Conservation needs zero net **external** force, and for the players that is only true horizontally and only while they are airborne. Gravity is external, so their vertical momentum is not conserved. Once their boots touch the turf, friction acts and the momentum of the pair no longer stays fixed. Real players also don't stay perfectly locked together; if they bounced apart, the total momentum would still be conserved but you'd need more information to find each final velocity. Rohit's skateboard wheels have some rolling friction, so he would slow down and stop soon after the throw.

## Key takeaway

If no net external force acts on a system, its total momentum stays constant: $m_1\vec{u}_1 + m_2\vec{u}_2 = m_1\vec{v}_1 + m_2\vec{v}_2$. In recoil, the total starts at zero, so the parts get equal and opposite momenta. In a collision where bodies stick, the momentum is shared, so the combined body moves off more slowly.
