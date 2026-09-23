---
concept_id: dipole_in_uniform_field
interest: football
format: explain
title: The straw that spins but never drifts
check:
  question: |-
    A small dipole is held at $30^\circ$ to a **uniform** electric field, then released. What does it do?
  options:
    A: |-
      It accelerates along the field, because the field pulls the positive charge harder than it pushes the negative one.
    B: |-
      Nothing: the forces on its two charges cancel, so it stays exactly as it was.
    C: |-
      It turns until $\vec{p}$ points opposite to $\vec{E}$, then drifts along the field.
    D: |-
      It turns until $\vec{p}$ lines up with $\vec{E}$, without drifting anywhere.
  answer: D
  explanation: |-
    The two forces are equal and opposite, so there is no net force, but they act along different lines and make a couple. The torque $\tau = pE\sin\theta$ turns $\vec{p}$ towards $\vec{E}$ and vanishes at $\theta = 0$.
  misconceptions:
    A: |-
      Assumes the field is stronger at one charge than the other. In a *uniform* field both charges feel exactly $qE$, so the pull and the push are equal in size.
    B: |-
      Takes "no net force" to mean "no effect". Two equal, opposite forces acting along *different lines* still twist an object — that is what a couple is.
    C: |-
      Gets the turning right but the final position wrong. $\vec{p}$ antiparallel to $\vec{E}$ is an unstable equilibrium: the smallest nudge sends it swinging round to line up with $\vec{E}$.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A floodlit ground as a storm arrives: lightning above the stand, rain falling, a player peeling off a crackling nylon bib, and two players heading for the metal-roofed dugout](scenes/football/electric_charges_fields.svg "Rain stops the football and fills the concourse — where the school physics club has a table.")

The inter-school tournament is rained off for an hour, so the crowd shuffles into the concourse, where Nandini's physics club has a table and nothing better to do than show off.

Her setup is simple: a drinking straw with a scrap of foil taped to each end, charged $+$ at one end and $-$ at the other, balanced across a sewing needle so it can spin freely. On either side, two large metal plates from an old science kit, connected to a small high-voltage supply, make a field in the gap between them.

She switches the supply on. The straw swings round, overshoots, wobbles, and settles pointing straight across the gap.

"It's being pulled to the plate," says a boy at the front.

"Watch the pivot," says Nandini. The straw's centre has not moved a millimetre. It turned, sharply — and it went nowhere.

Both ends carry charge. Both ends are in the field. So why does one thing happen and not the other?

## The physics

Put a dipole $\pm q$, length $2a$, into a **uniform** field $\vec{E}$, with $\vec{p}$ at angle $\theta$ to $\vec{E}$.

**The net force is zero.** The positive charge feels $+q\vec{E}$ and the negative one $-q\vec{E}$: equal in size, opposite in direction, because a uniform field has the same value at both ends.

$$\vec{F}_\text{net} = q\vec{E} + (-q)\vec{E} = 0$$

So the centre of mass does not accelerate. That is why the straw stays on its needle.

**The torque is not zero.** The two forces do not act along the same line. Their lines of action are a perpendicular distance $2a\sin\theta$ apart, so they form a **couple**:

$$\tau = (\text{force}) \times (\text{perpendicular distance}) = qE \times 2a\sin\theta = pE\sin\theta$$

![A dipole at angle theta to a uniform field pointing right; the force qE on plus q points right and on minus q points left; their lines of action are 2a sin theta apart and they turn p towards E](figures/dipole_in_uniform_field/dipole-torque.svg "Equal and opposite forces: no net push, but a twist. The torque turns p towards the direction of E.")

In vector form $\vec{\tau} = \vec{p} \times \vec{E}$, and the torque always turns $\vec{p}$ **towards** $\vec{E}$. Read off the special cases:

- $\theta = 90^\circ$: $\tau = pE$, the maximum.
- $\theta = 0$: $\tau = 0$, and it is **stable** — nudge it and the torque brings it back.
- $\theta = 180^\circ$: $\tau = 0$ as well, but **unstable** — the smallest disturbance flips it all the way round.

**The condition that does all the work is "uniform".** In a non-uniform field the two ends sit in different field strengths, the forces no longer cancel, and there is a net force as well as a torque — which is exactly why a charged straw attracts a stream of water, but a dipole between two large parallel plates only turns.

## Worked example

**Given (illustrative):** the foil ends carry $q = 20\,\text{nC}$, separated by $2a = 0.10\,\text{m}$, in a uniform field $E = 1.0 \times 10^{5}\,\text{N/C}$, at $\theta = 30^\circ$.
**Find:** the torque now, and the largest torque possible.

**Step 1 — the dipole moment.**

$$p = q \times 2a = (2.0 \times 10^{-8})(0.10) = 2.0 \times 10^{-9}\,\text{C m}$$

**Step 2 — the torque at $30^\circ$.** With $\sin 30^\circ = 0.50$:

$$\tau = pE\sin\theta = (2.0 \times 10^{-9})(1.0 \times 10^{5})(0.50) = 1.0 \times 10^{-4}\,\text{N m}$$

**Step 3 — the maximum.** At $\theta = 90^\circ$, $\sin\theta = 1$, so $\tau_\text{max} = 2.0 \times 10^{-4}\,\text{N m}$ — twice as much, and it is reached when the straw lies square across the field.

That $10^{-4}\,\text{N m}$ is about the twist you would get by hanging a $0.2\,\text{g}$ scrap of paper on the end of a $5\,\text{cm}$ arm: minute, but a straw on a needle has almost no friction to overcome.

**Sanity check:** the torque must vanish when the straw is already lined up ($\sin 0 = 0$), and it does. Units: $\text{C m} \times \text{N/C} = \text{N m}$, correct for a torque.

## Where the picture breaks

Between real plates the field is uniform only well inside the gap; near the edges it bulges, and there the straw would feel a genuine sideways pull. The straw is also not a point dipole — the foil ends are extended, and the charge on them shifts as the field turns. And nothing in this analysis explains why the straw *stops*: with no friction it would swing past the lined-up position and oscillate about it forever, like a pendulum. It settles because air resistance and the pivot drain the energy away.

## Key takeaway

In a uniform field the two forces on a dipole are equal and opposite, so the **net force is zero** — but they act along different lines, so they twist it: $\tau = pE\sin\theta$, or $\vec{\tau} = \vec{p} \times \vec{E}$. The torque is greatest at $90^\circ$, vanishes when $\vec{p}$ lines up with $\vec{E}$ (stable) or points against it (unstable), and a net force appears only if the field is non-uniform.
