---
concept_id: spherical_mirrors
interest: gaming
format: explain
title: The mirror in the level editor that kills the player
check:
  question: |-
    In a level editor a mirror is given a radius of curvature of $50\,\text{cm}$ and set to **convex**, facing the incoming laser. Using the Cartesian sign convention, what is its focal length?
  options:
    A: |-
      $-25\,\text{cm}$
    B: |-
      $+25\,\text{cm}$
    C: |-
      $+50\,\text{cm}$
    D: |-
      $-50\,\text{cm}$
  answer: B
  explanation: |-
    The focus lies halfway between the pole and the centre of curvature, so $|f| = R/2 = 25\,\text{cm}$. A convex mirror bulges towards the light, which puts its centre of curvature and its focus *behind* the surface — the direction the light is travelling — so both are positive: $f = +25\,\text{cm}$.
  misconceptions:
    A: |-
      Gets the size right but reasons "convex spreads light out, so its focal length must be negative". The sign records *where* the focus is, not what the mirror does to the rays. A convex mirror's focus is behind the glass, in the positive direction.
    C: |-
      Uses $f = R$ instead of $f = R/2$. The focus sits halfway between the pole and the centre of curvature, so the focal length is always half the radius.
    D: |-
      Both slips together: the radius is not halved, and the sign is taken from "spreading" instead of from the direction of measurement.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A gaming desk at night with a monitor, a coolant reservoir, a cut-away VR headset, a glass prism, a glowing optical cable, a hand lens over a controller board and a wall-mounted dome mirror](scenes/gaming/ray_optics.svg "Look at the monitor: two parallel laser beams hit the curved mirror and leave through one bright point. That point is what this lesson is about.")

Rehan is three weeks into building a puzzle level. The idea is simple: a green laser, a locked door, and a mirror the player can rotate until the beam opens the lock. The engine traces the rays properly, so whatever the mirror does on screen is what the physics would do.

He drops in the curved mirror asset. The inspector panel has one number he does not understand: **radius of curvature, 60**. He shrugs, sets it, and plays the level. The beam hits the dish, folds back on itself and gathers into a single fierce white dot in mid-air a little way in front of the mirror. His test character walks through the dot and the health bar empties.

He pokes at the panel and types a minus sign in front of the 60, on a hunch. Now the same beam leaves the mirror *spreading*, washing the whole corridor in weak green, and the door never opens.

One character typed, and the mirror went from a weapon to a floodlight. What is that sign actually saying?

## The physics

A **spherical mirror** is a piece cut from a hollow sphere and silvered on one side. If the silvered surface is the caved-in side, the mirror is **concave**; if it is the bulging side, it is **convex**. Four names carry everything:

- the **pole** $P$ — the centre of the mirror's surface;
- the **centre of curvature** $C$ — the centre of the sphere the piece was cut from;
- the **radius of curvature** $R$ — the distance $PC$;
- the **principal axis** — the line through $P$ and $C$.

Send in rays parallel to the principal axis and close to it. A concave mirror reflects them so they really cross at a point; a convex mirror reflects them outwards so they only *appear* to spread from a point behind the surface. Either way that point is the **principal focus** $F$, and geometry puts it halfway along $PC$:

$$f = \frac{R}{2}$$

![Two panels: a concave mirror reflecting parallel rays through a real focus in front, and a convex mirror reflecting them so they appear to come from a focus behind the mirror](figures/spherical_mirrors/concave-convex-focus.svg "Same incoming rays, opposite results. In both cases the focus is halfway between the pole and the centre of curvature.")

This holds only for **paraxial rays** — rays close to the axis and nearly parallel to it. Rays striking the outer rim of a wide mirror cross slightly nearer the glass, so a real curved mirror never gives a perfectly sharp point.

Now the sign. Physics fixes it once with the **Cartesian sign convention**, and this lesson uses it throughout: every distance is measured from the pole, light is always drawn travelling left to right, distances measured **along** the direction the light travels are positive and **against** it negative, and heights above the axis are positive.

![A diagram of the Cartesian sign convention: the pole as origin, negative distances to the left, positive to the right, positive heights up and negative down](figures/spherical_mirrors/cartesian-sign-convention.svg "Everything is measured from the pole. A real object always sits in front of the mirror, so u always comes out negative.")

For a **concave** mirror, $C$ and $F$ lie in front of the glass, against the incoming light: $R$ and $f$ are **negative**. For a **convex** mirror they lie behind it: $R$ and $f$ are **positive**. That single sign is the whole difference between Rehan's weapon and his floodlight — and it is why the editor asks for a signed radius rather than a shape.

## Worked example

**Given:** the dish mirror in the level is concave with a radius of curvature of $60\,\text{cm}$. The level's laser sends its beam in parallel to the principal axis.
**Find:** the focal length with its sign, and where the bright point forms.

**Step 1 — the focal length.** The mirror is concave, so its centre of curvature is in front of the surface, against the incoming light: $R = -60\,\text{cm}$. Then

$$f = \frac{R}{2} = \frac{-60}{2} = -30\,\text{cm}$$

**Step 2 — read the sign.** Negative means measured against the light, so $F$ is $30\,\text{cm}$ *in front of* the mirror — about the length of a school ruler out into the corridor. Parallel rays converge exactly there, which is where Rehan's killing dot sat.

**Sanity check:** a concave mirror is the one you can hold a card in front of and catch a bright spot on. The minus sign is the equation saying "out here in the room, not behind the glass".

## Where the picture breaks

A game engine that traces rays is doing real geometry, but it is still a model. Engines usually treat a mirror as a perfect paraxial surface, so the killing dot is a mathematical point; a real dish of this size would smear it into a small blurred patch, because rays from the rim miss the paraxial focus. Real mirrors also absorb a few per cent of the light at every bounce, and the beam would fade after two or three reflections — most engines quietly ignore that.

And do not read the analogy backwards. Light is not a projectile: a laser ray does not lose speed at the mirror, does not care how fast it arrives, and cannot be "aimed harder". Everything that happens is fixed by angles alone.

## Key takeaway

A spherical mirror is described by its pole, centre of curvature and focus, with $f = R/2$ for paraxial rays. Concave mirrors bring parallel light to a real focus in front of the glass; convex mirrors make it diverge from a virtual focus behind. In the Cartesian convention, measured from the pole against the incoming light, a concave mirror has $f$ negative and a convex mirror has $f$ positive — one character in an editor, two completely different levels.
