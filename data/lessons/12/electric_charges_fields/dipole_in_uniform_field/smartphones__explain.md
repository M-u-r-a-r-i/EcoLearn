---
concept_id: dipole_in_uniform_field
interest: smartphones
format: explain
title: How a screen twists molecules without pushing them
check:
  question: |-
    An electric dipole is placed in a **uniform** electric field with its dipole moment at $60^\circ$ to the field. Which statement is correct?
  options:
    A: |-
      There is a net force on it along the field, but no torque
    B: |-
      The net force and the net torque are both zero, since the two charges feel equal and opposite forces
    C: |-
      There is a net force along the field and also a torque
    D: |-
      The net force is zero, but a torque turns $\vec{p}$ towards the direction of $\vec{E}$
  answer: D
  explanation: |-
    In a uniform field the forces $+q\vec{E}$ and $-q\vec{E}$ are equal and opposite, so the net force is zero. But they act at different points, along lines $2a\sin\theta$ apart, so they form a couple with torque $\tau = pE\sin\theta$ that turns $\vec{p}$ towards $\vec{E}$.
  misconceptions:
    A: |-
      Thinks the positive end is pulled harder than the negative end is pushed. In a uniform field both charges feel forces of exactly the same size, $qE$.
    B: |-
      Thinks equal and opposite forces always cancel completely. They cancel as forces, but when they act along different lines they still form a couple that turns the body.
    C: |-
      Carries over the result for a non-uniform field, where the two ends feel different field strengths. In a uniform field there is only the turning effect.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A desk by a sunny window with a solar power bank on the sill, an opened phone box with foam beads clinging to the new phone, a film being peeled off a screen with dust jumping up to it, and a phone on a stand running a field-line app](scenes/smartphones/electric_charges_fields.svg "The + and − on the app's screen are a dipole. Today's question: what does a steady field do to one?")

Rohan has new polarised sunglasses, and he has found something strange. When he turns his old phone sideways, its screen goes almost black. Turn it back upright and the picture returns.

His sister Pallavi, who is studying electronics, explains. "That phone has a liquid-crystal screen. Behind every pixel there's a thin layer of long, rod-shaped molecules. Apply a voltage across the layer and they turn, and that changes the light coming out. Your glasses just happen to block the light from the screen when it's sideways."

Rohan is stuck on one word: *turn*. The voltage makes an electric field across the layer, and the field is the same all the way through. The molecules don't slide across the screen; if they did, the picture would smear. They just rotate, in place. How can a field twist something without pushing it anywhere?

## The physics

Put a dipole ($+q$ and $-q$, separation $2a$, moment $p = q \times 2a$) in a **uniform** field $\vec{E}$, with $\vec{p}$ at angle $\theta$ to $\vec{E}$.

**Net force: zero.** The positive charge feels $q\vec{E}$ along the field; the negative charge feels $-q\vec{E}$, opposite. The field is the same at both, so the two forces are equal and opposite, and they add to zero. The dipole's centre does not accelerate.

**Torque: not zero.** The two forces act at different points, along parallel lines a perpendicular distance $2a\sin\theta$ apart. Such a pair is a **couple**, and its torque is
$$\tau = qE \times 2a\sin\theta = pE\sin\theta, \qquad \vec{\tau} = \vec{p} \times \vec{E}$$
with SI unit N m. The torque turns $\vec{p}$ **towards** the direction of $\vec{E}$.

![A dipole at angle theta to a uniform field pointing right; the force qE on plus q points right and on minus q points left; their lines of action are 2a sin theta apart and they turn p towards E](figures/dipole_in_uniform_field/dipole-torque.svg "Equal and opposite forces: no net push, but a twist. The torque turns p towards the direction of E.")

- $\theta = 0^\circ$: $\vec{p}$ lies along $\vec{E}$, $\tau = 0$. This is **stable equilibrium**: nudge it and the torque brings it back.
- $\theta = 90^\circ$: $\tau = pE$, the **largest** turning effect.
- $\theta = 180^\circ$: $\tau = 0$ again, but **unstable**: the slightest nudge and it flips round.

If the field is **not** uniform, the two ends feel different forces, so there is a net force as well as a torque. That is why a charged comb pulls bits of paper towards it: its field is far from uniform.

In Rohan's screen, the field across each pixel's thin layer is close to uniform, so the molecules are twisted into line with it but not dragged sideways.

## Worked example

**Given (illustrative, a model dipole):** charges $\pm 2.0\,\text{nC}$ held $5.0\,\text{mm}$ apart, in a uniform field $E = 2.0 \times 10^4\,\text{N/C}$, with $\vec{p}$ at $30^\circ$ to $\vec{E}$.
**Find:** the net force and the torque.

**Step 1 — each force.** $qE = 2.0 \times 10^{-9} \times 2.0 \times 10^4 = 4.0 \times 10^{-5}\,\text{N}$, one along $\vec{E}$ and one against it. Net force: zero.

**Step 2 — the dipole moment.** $p = 2.0 \times 10^{-9} \times 5.0 \times 10^{-3} = 1.0 \times 10^{-11}\,\text{C m}$.

**Step 3 — the torque at $30^\circ$.**
$$\tau = pE\sin 30^\circ = 1.0 \times 10^{-11} \times 2.0 \times 10^4 \times 0.50 = 1.0 \times 10^{-7}\,\text{N m}$$
It turns $\vec{p}$ towards $\vec{E}$, closing the $30^\circ$ gap.

**Step 4 — at its strongest.** Held at $90^\circ$, $\sin\theta = 1$ and the torque doubles to $2.0 \times 10^{-7}\,\text{N m}$.

**Sanity check:** the torque should also equal one force times the gap between the lines of action: $4.0 \times 10^{-5} \times (5.0 \times 10^{-3} \times 0.50) = 1.0 \times 10^{-7}\,\text{N m}$, the same.

## Where the picture breaks

Real liquid-crystal molecules are not two fixed charges on a stick. Their response comes mainly from charge being *shifted* inside them by the field (an induced dipole), their neighbours hold them in a preferred direction, and the layer relaxes back when the voltage is removed. The rigid dipole explains the key fact, a turning effect with no net drag in a uniform field, but not the details. Not every phone screen works this way either: many newer screens make their own light pixel by pixel and have no liquid-crystal layer at all.

## Key takeaway

In a uniform field a dipole feels **no net force**, because $+q\vec{E}$ and $-q\vec{E}$ cancel, but it does feel a **torque** $\tau = pE\sin\theta$ (vector form $\vec{\tau} = \vec{p} \times \vec{E}$) that turns $\vec{p}$ towards $\vec{E}$: zero when aligned (stable), largest at $90^\circ$. Only a non-uniform field adds a net force.
