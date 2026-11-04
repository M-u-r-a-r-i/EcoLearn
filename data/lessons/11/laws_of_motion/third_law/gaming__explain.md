---
concept_id: third_law
interest: gaming
format: explain
title: If the pushes cancel, why does the astronaut move
check:
  question: |-
    In a zero-gravity game with realistic physics, a $90\,\text{kg}$ astronaut (with suit) pushes a $30\,\text{kg}$ crate with a force of $60\,\text{N}$. While they are in contact, the force the crate exerts on the astronaut is:
  options:
    A: |-
      $20\,\text{N}$, because the crate has only a third of the astronaut's mass
    B: |-
      $180\,\text{N}$, because the heavier astronaut feels the bigger force
    C: |-
      $60\,\text{N}$, in the opposite direction to the push on the crate
    D: |-
      zero, because only the astronaut is doing the pushing
  answer: C
  explanation: |-
    By Newton's third law, the crate pushes back on the astronaut with a force equal in size and opposite in direction: $60\,\text{N}$. The two bodies accelerate differently because their masses differ, not because the forces differ.
  misconceptions:
    A: |-
      Thinks the lighter body exerts a smaller force. The forces in an action–reaction pair are always equal in size; it is the accelerations that depend on mass.
    B: |-
      Thinks the heavier body receives a bigger force. Mass decides the acceleration a force produces, not the size of the reaction force.
    D: |-
      Thinks only the "active" body exerts a force. Forces always come in pairs: the crate pushes back on the astronaut whenever the astronaut pushes on it.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A gaming desk at night: a racing game on the monitor and a zero-gravity game on a tablet](scenes/gaming/laws_of_motion.svg "On the tablet: the astronaut pushes the crate, and both go flying, in opposite directions.")

Meher is three levels into a zero-gravity puzzle game set inside a wrecked space station. Her astronaut floats beside a supply crate. She presses the push button. The crate glides off towards the airlock, and her astronaut drifts slowly backwards the other way.

Her younger brother Dhruv, who has just learnt Newton's third law at school, frowns at the screen.

"That's wrong," he says. "Every action has an equal and opposite reaction. So when you push the crate, the crate pushes you back just as hard. Equal and opposite forces cancel out. So nothing should move at all."

"But things obviously move," says Meher. "You can't push anything in this game without flying off."

Dhruv folds his arms. He is quoting the law correctly. The game shows both objects moving. Somebody has made a mistake. Who?

## The physics

**Newton's third law:** whenever body A exerts a force on body B, body B exerts a force on body A that is **equal in size and opposite in direction**:

$$\vec{F}_\text{AB} = -\vec{F}_\text{BA}$$

Here $\vec{F}_\text{AB}$ is the force on A by B, and $\vec{F}_\text{BA}$ the force on B by A. Three things are true of every such **action–reaction pair**:

- The two forces act on **different bodies**, one on each.
- They are forces of the **same kind** (both contact pushes here), and they act at the **same time**. Neither is "first"; "action" and "reaction" are just labels.
- They are equal in size **however** the bodies are moving, speeding up or not.

Dhruv's mistake is the first point. Forces can only cancel if they act on the **same** body. To find out how the crate moves, you add up the forces **on the crate**: that is just the astronaut's push. To find out how the astronaut moves, you add up the forces **on the astronaut**: that is just the crate's push back. Each body has one unbalanced force, so each accelerates, in opposite directions.

![Body A and body B drawn slightly apart: a red arrow on B points right, labelled force on B by A, and an equal red arrow on A points left, labelled force on A by B](figures/third_law/action-reaction-pair.svg "Let A be the astronaut and B the crate. The two forces are equal, but each sits on a different body, so they can never cancel.")

Equal forces don't mean equal effects. From $a = F/m$, the lighter body gets the bigger acceleration. That is why the crate shoots off and the heavier astronaut drifts back slowly.

A physics engine has to respect this when two objects touch: it pushes both apart with equal and opposite forces. If it pushed only one, objects could speed themselves up from nothing, and the game world would break.

## Worked example

**Given (illustrative values):** astronaut with suit $m_\text{A} = 90\,\text{kg}$; crate $m_\text{C} = 30\,\text{kg}$; both at rest in zero gravity. She pushes the crate with a steady $60\,\text{N}$ for $0.50\,\text{s}$.
**Find:** the force on the astronaut, each body's acceleration, and each final speed.

*Third law:* the crate pushes the astronaut with $60\,\text{N}$, opposite to her push.

*Second law, each body separately:*

$$a_\text{C} = \frac{60}{30} = 2.0\,\text{m/s}^2 \qquad a_\text{A} = \frac{60}{90} \approx 0.67\,\text{m/s}^2$$

*Speeds after $0.50\,\text{s}$, starting from rest* ($v = at$):

$$v_\text{C} = 2.0 \times 0.50 = 1.0\,\text{m/s} \qquad v_\text{A} = 0.667 \times 0.50 \approx 0.33\,\text{m/s}$$

in opposite directions.

**Sanity check:** the crate has a third of the mass, so it should move three times as fast: $3 \times 0.33 \approx 1.0$ ✓. Notice also that $30 \times 1.0 = 90 \times 0.33 \approx 30\,\text{kg m/s}$: the two bodies end with equal and opposite momenta. That is no accident, and it leads straight to the next idea, conservation of momentum.

## Where the picture breaks

On a game screen you only see motion, never forces, so you have to trust that the engine really applies equal and opposite pushes; some games script motion directly and would fail this test. A real push is not perfectly steady for exactly half a second. And the third law, as stated here, is about contact and gravitational forces between two bodies; there are subtle cases with moving charges and fields that you'll meet much later. For everyday pushes, pulls and collisions it holds exactly.

## Key takeaway

Forces come in pairs: if A pushes B, B pushes A with an equal and opposite force, $\vec{F}_\text{AB} = -\vec{F}_\text{BA}$. The two forces act on different bodies, so they never cancel each other. Each body moves according to the forces on it alone, and with equal forces the lighter body accelerates more.
