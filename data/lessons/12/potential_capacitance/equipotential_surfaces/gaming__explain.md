---
concept_id: equipotential_surfaces
interest: gaming
format: explain
title: The contour lines hiding inside every electric field
check:
  question: |-
    In a region of uniform field, equipotential surfaces drawn $30\,\text{V}$ apart turn out to be $2.0\,\text{cm}$ apart. A charge of $+5.0\,\text{nC}$ is carried $6.0\,\text{cm}$ along one of these surfaces. How much work does this take?
  options:
    A: |-
      $4.5 \times 10^{-7}\,\text{J}$
    B: |-
      Zero.
    C: |-
      $1.5 \times 10^{-7}\,\text{J}$
    D: |-
      It is not zero, and the value depends on which route across the surface is taken.
  answer: B
  explanation: |-
    Every point on one equipotential surface is at the same potential, so $\Delta V = 0$ and $W = q\,\Delta V = 0$ — no matter how far the charge travels along it.
  misconceptions:
    A: |-
      Treats the $6.0\,\text{cm}$ as a distance moved *along* the field, computing $E = 30\,\text{V}/0.020\,\text{m} = 1500\,\text{V/m}$ and then $W = qEd$. Motion along an equipotential is perpendicular to the field, so the field does no work.
    C: |-
      Reads "$30\,\text{V}$ apart" as the potential difference actually crossed, giving $W = q \times 30\,\text{V}$. The charge never leaves its own surface, so it crosses no potential difference at all.
    D: |-
      Thinks electrostatic work depends on the path. The electrostatic force is conservative, so the work depends only on the start and end potentials — here they are equal, so the work is zero by every route.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A gaming desk with a monitor showing rings of equal potential around a charge, a phone with a fingertip on its screen, an old picture tube on the bench and an opened power supply with two big capacitors](scenes/gaming/potential_capacitance.svg "Look at the rings on the monitor. Nothing about them is an arrow, and yet they tell you which way things will move.")

Arjun is building the minimap for a hill-climb racing game, and he has just turned on contour lines — thin loops drawn through all the points at the same height. Sneha, who does the driving, leans over.

"Those are useless," she says. "I need to know which way the slope goes. Draw me arrows."

Arjun taps the screen where the loops bunch up tightly near a ridge. "It's already there. Where the lines crowd together the hill is steep. Where they spread out it's gentle. And downhill is always straight across a line, never along it."

Sneha isn't convinced until she drives it. She takes a corner along a contour and the car neither gains nor loses speed. Then she cuts straight across four lines and drops like a stone.

On the monitor behind them, a physics demo is drawing a set of rings around a charge, and they look exactly like Arjun's contours. Does the same trick work for an electric field — and if it does, why should "straight across" be the special direction there too?

## The physics

An **equipotential surface** is a surface on which the electrostatic potential has the same value at every point. It is the electric field's contour map.

**No work along one.** Move a charge $q$ from a point $A$ to a point $B$ on the same equipotential. The work needed is

$$W = q\,(V_B - V_A) = 0$$

because $V_A = V_B$. This is the whole idea in one line: *you can slide a charge around an equipotential for free.*

**Always perpendicular to the field lines.** This follows from the line above. The work done by the field over a small displacement $\vec{d\ell}$ is $\vec{F} \cdot \vec{d\ell} = qE\,d\ell\cos\theta$. If that work is zero for *every* displacement along the surface, and neither $E$ nor $d\ell$ is zero, then $\cos\theta = 0$ — the field must meet the surface at $90°$. If it did not, the field would have a component along the surface, that component would push the charge sideways, and the potential could not stay constant.

![Three panels: concentric circles around a point charge with radial field lines; parallel planes at 50, 40, 30, 20, 10 V in a uniform field; distorted circles and a zero-potential midline for a dipole](figures/equipotential_surfaces/equipotentials-three-cases.svg "In every case the field lines (purple) cross the equipotentials (orange) at right angles. The dipole's midline is the V = 0 surface.")

**The three standard cases**, all in the figure: around an isolated point charge the equipotentials are **concentric spheres** (since $V = kq/r$ depends only on $r$); in a uniform field they are **parallel planes** perpendicular to the field; for a dipole they are distorted closed surfaces, with the plane midway between the charges at $V = 0$.

**Crowding means strength.** Draw the surfaces at equal potential steps $\Delta V$, and their spacing $\Delta r$ obeys

$$E \approx \frac{\Delta V}{\Delta r}$$

So closely packed equipotentials mean a strong field — exactly Sneha's steep ridge. Two different equipotential surfaces can never touch or cross, because a point cannot hold two values of $V$ at once.

## Worked example

Two large parallel plates are $5.0\,\text{cm}$ apart with $100\,\text{V}$ across them. Treat the field between them as uniform.

**Find:** how far apart the equipotential surfaces are if you draw one every $20\,\text{V}$.

**Step 1 — the field.**

$$E = \frac{\Delta V}{d} = \frac{100\,\text{V}}{0.050\,\text{m}} = 2000\,\text{V/m}$$

That is the same everywhere between the plates, so the contour spacing will be even.

**Step 2 — the spacing.**

$$\Delta r = \frac{\Delta V}{E} = \frac{20\,\text{V}}{2000\,\text{V/m}} = 0.010\,\text{m} = 1.0\,\text{cm}$$

So you get flat sheets at $20$, $40$, $60$ and $80\,\text{V}$, each one centimetre from the next — five even steps across a five-centimetre gap, like the rungs of a ladder.

**Sanity check:** $100\,\text{V}$ split into five $20\,\text{V}$ steps across $5\,\text{cm}$ has to give $1\,\text{cm}$ per step. The arithmetic and the picture agree.

## Where the picture breaks

A hill's contour map and an equipotential map look alike because gravitational potential energy near the ground really does go as height — but the resemblance has limits. Height is a property of the ground, while potential is a property of *space*: the electric equipotentials are surfaces filling three dimensions, not lines on a sheet, and the rings you see on a screen are only one slice through them. Arjun's contours are also always positive, while potential is happily negative around a negative charge. And a car coasting along a contour keeps its speed only if you ignore friction, whereas the zero-work result for an equipotential is exact, not an idealisation — it follows from the definition of potential itself.

## Key takeaway

An equipotential surface joins all the points at the same potential, so moving a charge along it takes **no work at all**. That forces the field to be perpendicular to the surface everywhere — a sideways component would do work. Spheres around a point charge, parallel planes in a uniform field; and where the surfaces crowd together, $E \approx \Delta V/\Delta r$ is large.
