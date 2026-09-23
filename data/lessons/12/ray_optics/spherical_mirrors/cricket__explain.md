---
concept_id: spherical_mirrors
interest: cricket
format: explain
title: The two curved mirrors in the players' tunnel
check:
  question: |-
    A concave shaving mirror in the dressing room has a radius of curvature of $40\,\text{cm}$. Using the Cartesian sign convention, what is its focal length?
  options:
    A: |-
      $+20\,\text{cm}$
    B: |-
      $-20\,\text{cm}$
    C: |-
      $-40\,\text{cm}$
    D: |-
      $+40\,\text{cm}$
  answer: B
  explanation: |-
    The focus of a spherical mirror is halfway between the pole and the centre of curvature, so $f = R/2 = 20\,\text{cm}$ in size. For a concave mirror the focus lies in front of the mirror, on the same side as the incoming light, so the sign convention makes it negative: $f = -20\,\text{cm}$.
  misconceptions:
    A: |-
      Gets the size right but assumes "concave converges, so the focal length is positive". The sign comes from the direction of measurement, not from whether the mirror converges: a concave mirror's focus is in front of it, which is the negative direction.
    C: |-
      Uses $f = R$ instead of $f = R/2$. The focus sits halfway between the pole and the centre of curvature.
    D: |-
      Both errors at once: takes $f = R$ and calls it positive.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A sunlit cricket ground with the sun's rays, a broadcast camera with a long lens, a stump camera, a fielder in curved sunglasses, and a small rainbow in the sprinkler spray](scenes/cricket/ray_optics.svg "Almost everything that watches a cricket match is a curved mirror or a lens. Notice how the camera gathers light from a wide patch of the pitch into one small lens.")

Aarav is a net bowler, and the morning session has finished. He walks up the tunnel from the ground, and stops at the big round mirror bolted above the door — the one the ground staff use to see who is coming round the corner. In it the whole tunnel fits: the kit bags, the roller outside, two players behind him, all shrunk to the size of his palm.

Inside the dressing room there is another curved mirror, above the wash basin. He leans in and his own face fills it, twice its normal size, every hair sharp.

Both mirrors are pieces of curved glass. One shrinks an entire corridor; the other blows up one face. Aarav taps them both — the tunnel mirror bulges towards him, the basin mirror caves away from him. That is the only difference he can find. How can which way the glass bends change what you see so completely?

## The physics

A **spherical mirror** is a small piece cut from a hollow sphere and silvered on one side. If the reflecting surface is the hollow, caved-in side, it is **concave**; if it is the bulging side, it is **convex**. The tunnel mirror is convex, the basin mirror concave.

Four names do all the work:

- the **pole** $P$: the centre of the mirror's surface;
- the **centre of curvature** $C$: the centre of the sphere the mirror was cut from;
- the **radius of curvature** $R$: the distance $PC$;
- the **principal axis**: the straight line through $P$ and $C$.

Send in a bundle of rays parallel to the principal axis and close to it. A concave mirror reflects them so that they really cross at one point; a convex mirror reflects them outwards so that they only *appear* to come from one point behind the glass. Either way that point is the **principal focus** $F$, and geometry puts it halfway between the pole and the centre of curvature:

$$f = \frac{R}{2}$$

![Two panels: a concave mirror reflecting parallel rays through a real focus, and a convex mirror reflecting them so they appear to come from a focus behind the mirror](figures/spherical_mirrors/concave-convex-focus.svg "Same incoming rays, opposite results. The focus is always halfway between the pole and the centre of curvature.")

This holds only for **paraxial rays** — rays close to the principal axis and nearly parallel to it. Rays striking the outer edge of a wide mirror cross slightly nearer the mirror, which is why a real curved mirror never gives a perfectly sharp image.

Signs matter, so physics fixes them once and for all with the **Cartesian sign convention**: all distances are measured from the pole, light is always drawn travelling left to right, distances measured along the incoming light are positive and against it negative, and heights above the principal axis are positive.

![A diagram of the Cartesian sign convention, showing the pole as origin, negative distances to the left and positive to the right, positive heights up and negative down](figures/spherical_mirrors/cartesian-sign-convention.svg "Everything is measured from the pole. Because a real object sits in front of the mirror, u always comes out negative.")

For a concave mirror, $F$ and $C$ are in front of the glass, so $f$ and $R$ are **negative**. For a convex mirror they are behind it, so $f$ and $R$ are **positive**. That single sign is the whole difference Aarav felt with his fingers.

## Worked example

**Given:** the tunnel mirror is convex with a radius of curvature of $2.0\,\text{m}$. The basin mirror is concave with a radius of curvature of $0.60\,\text{m}$.
**Find:** where $F$ and $C$ lie for each, with the correct signs.

**Step 1 — the tunnel mirror.** It is convex, so its centre of curvature lies behind the glass, in the positive direction: $R = +2.0\,\text{m}$. Its focus is halfway there:

$$f = \frac{R}{2} = \frac{+2.0}{2} = +1.0\,\text{m}$$

So $F$ sits one metre *behind* the wall — nothing is really there, which is exactly why the reflected rays only seem to spread from it.

**Step 2 — the basin mirror.** It is concave, so $C$ lies in front of the glass, in the negative direction: $R = -0.60\,\text{m}$, and

$$f = \frac{-0.60}{2} = -0.30\,\text{m}$$

$F$ is $30\,\text{cm}$ in front of the mirror — about a hand-span out from the wall, roughly where Aarav's face is when he leans in.

**Sanity check:** the mirror that caves away from you has its focus out in the room where you stand, and the one that bulges towards you has its focus hidden behind the wall. The signs say exactly that.

## Where the picture breaks

The tunnel mirror is not really a piece of a sphere: security mirrors are often shaped to widen the view further, and a genuinely spherical one this wide would blur badly at the edges, because the paraxial condition fails there. Nothing here is special to cricket either — the ground is the setting, not an analogy. Mirrors in a dressing room obey the same rules as mirrors in a bathroom or a car. Treat the cricket detail as a place to hang the physics, not as a likeness to reason from; a "ball bouncing off the pitch" is *not* a good model of light reflecting, because a ball loses energy and spin changes its angle, while a light ray does not.

## Key takeaway

A spherical mirror is described by its pole, centre of curvature and focus, with $f = R/2$ for paraxial rays. Concave mirrors converge light to a real focus in front; convex mirrors make light diverge from a virtual focus behind. In the Cartesian convention, measured from the pole against the incoming light, a concave mirror has $f$ negative and a convex mirror has $f$ positive.
