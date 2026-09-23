---
concept_id: work_constant_force
interest: gaming
format: explain
title: Why the flatter pull moves the crate further
check:
  question: |-
    In a puzzle game a robot pushes a crate $8\,\text{m}$ along a level floor with a steady horizontal force of $30\,\text{N}$, while friction of $10\,\text{N}$ opposes the motion. How much work does **friction** do on the crate?
  options:
    A: |-
      $+80\,\text{J}$
    B: |-
      $-240\,\text{J}$
    C: |-
      $-80\,\text{J}$
    D: |-
      $+160\,\text{J}$
  answer: C
  explanation: |-
    Friction points opposite to the displacement, so $\theta = 180^\circ$ and $W = fd\cos 180^\circ = -(10)(8) = -80\,\text{J}$. The minus sign says friction takes $80\,\text{J}$ out of the crate's motion.
  misconceptions:
    A: |-
      Gets the size right but ignores the direction; a force acting against the displacement does negative work, because $\cos 180^\circ = -1$.
    B: |-
      Uses the pushing force ($30\,\text{N}$) in place of the friction force; the question asks for the work done by friction alone, so only the friction force goes into $W = Fd\cos\theta$.
    D: |-
      Works out the *net* work from the net force, $(30 - 10) \times 8$; that is the total work done by all forces together, not the work done by friction.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A gaming desk at night: a monitor shows a physics sandbox with a spring launcher, a kart at the top of a loop and a crate being dragged by a rope, beside a force-feedback racing wheel and a controller](scenes/gaming/work_energy_power.svg "On the right of the screen, a crate is dragged by a rope that pulls upwards at an angle, not straight along the floor.")

Aarav and his cousin Simran are two hours into a co-op survival game, hauling supply crates from a crashed cargo plane back to base. Each drag costs stamina, and the bar is nearly empty.

Simran holds the rope high, almost over her shoulder, because it "feels stronger". Aarav crouches low so his rope runs nearly flat along the ground. Same crate, same distance, same pull strength set by the game — and Aarav's crate reaches the base with a quarter of the stamina bar still green, while Simran's character is gasping.

Simran is not convinced. "You pulled with the same force. How can holding the rope differently change anything?"

Aarav can feel that it does. But *why* should the angle of a rope decide how much of a pull actually counts?

## The physics

In physics, **work** is done on a body when a force acts on it *and* the body moves. For a constant force $\vec{F}$ causing a displacement $\vec{d}$:

$$W = \vec{F} \cdot \vec{d} = Fd\cos\theta$$

where $\theta$ is the angle between the force and the displacement. Work is a scalar, measured in **joules**: $1\,\text{J} = 1\,\text{N}\,\text{m}$.

Only the component of the force *along* the displacement, $F\cos\theta$, does work. That is Simran's problem: with the rope at a steep angle, most of her pull tries to lift the crate instead of sliding it, and the crate never moves upwards, so that part does nothing.

![Three panels: a force at an angle theta to the displacement does positive work; weight and the normal force, perpendicular to the displacement, do zero work; friction, opposite to the displacement, does negative work](figures/work_constant_force/work-sign-cases.svg "Compare each force with the displacement. Along it: positive work. Perpendicular to it: none at all. Against it: negative.")

The sign follows $\cos\theta$:

- $\theta < 90^\circ$ — **positive** work; the force feeds energy into the motion.
- $\theta = 90^\circ$ — **zero** work. The crate's weight and the floor's normal force are both perpendicular to a horizontal slide, so neither does any work, however heavy the crate.
- $\theta > 90^\circ$ — **negative** work; the force takes energy out. Friction always does this.

Two conditions: the force must be constant, and $\vec{d}$ is the displacement of the point where the force acts. If the crate does not move, $W = 0$ no matter how hard anyone pulls — straining against an immovable crate is exhausting, but it is not work in the physics sense.

## Worked example

**Given** (illustrative game values): the rope pulls the crate with $F = 50\,\text{N}$ at $60^\circ$ above the floor, and the crate slides $d = 10\,\text{m}$. The floor drags back on it with a steady friction force of $20\,\text{N}$.
**Find:** the work done by the rope, by friction, and by all forces together.

**Step 1 — the rope.** Only the horizontal part of the pull counts:

$$W_\text{rope} = Fd\cos\theta = 50 \times 10 \times \cos 60^\circ = 50 \times 10 \times 0.5 = 250\,\text{J}$$

Half the pull is wasted upwards, so the rope delivers $250\,\text{J}$, not $500\,\text{J}$.

**Step 2 — friction.** It acts against the motion, so $\theta = 180^\circ$:

$$W_\text{friction} = 20 \times 10 \times (-1) = -200\,\text{J}$$

Friction takes back $200\,\text{J}$ of the $250\,\text{J}$ the rope put in.

**Step 3 — everything together.** Weight and the normal force are perpendicular to the slide, so they contribute nothing:

$$W_\text{net} = 250 - 200 + 0 = 50\,\text{J}$$

Only $50\,\text{J}$ is left in the crate's motion — about the energy of a cricket ball thrown gently.

**Sanity check:** the numbers say most of the effort went sideways into the rope's angle and into friction, which matches Simran's empty stamina bar.

## Where the picture breaks

A stamina bar is not energy. Games drain stamina by rules chosen to feel fair, and your muscles burn fuel even while holding a crate perfectly still — which is zero work in physics. Real dragging is also messier than this: lifting part of the crate's weight with a steeper rope reduces how hard the floor presses back, so friction falls a little as the rope angle rises. Here friction was given as fixed, and the force was taken as constant over the whole $10\,\text{m}$; a real pull jerks and varies.

## Key takeaway

Work done by a constant force is $W = \vec{F} \cdot \vec{d} = Fd\cos\theta$, measured in joules. Only the part of the force along the displacement counts, so a perpendicular force does no work at all, and a force opposing the motion does negative work. No displacement means no work, however great the force.
