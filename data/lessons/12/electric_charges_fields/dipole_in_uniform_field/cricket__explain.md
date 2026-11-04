---
concept_id: dipole_in_uniform_field
interest: cricket
format: explain
title: What the canteen microwave does to water
check:
  question: |-
    An electric dipole of moment $3.0 \times 10^{-9}\,\text{C m}$ sits in a uniform electric field of $2.0 \times 10^{4}\,\text{N/C}$, with its dipole moment at $30^\circ$ to the field. What are the torque on it and the net force on it?
  options:
    A: |-
      Torque $5.2 \times 10^{-5}\,\text{N m}$; net force zero
    B: |-
      Torque $6.0 \times 10^{-5}\,\text{N m}$; net force zero
    C: |-
      Torque $3.0 \times 10^{-5}\,\text{N m}$; net force along the field
    D: |-
      Torque $3.0 \times 10^{-5}\,\text{N m}$; net force zero
  answer: D
  explanation: |-
    $\tau = pE\sin\theta = 3.0 \times 10^{-9} \times 2.0 \times 10^{4} \times \sin 30^\circ = 3.0 \times 10^{-5}\,\text{N m}$. In a uniform field the forces $+q\vec{E}$ and $-q\vec{E}$ are equal and opposite, so the net force is zero.
  misconceptions:
    A: |-
      Uses $\cos\theta$ instead of $\sin\theta$. The torque depends on the perpendicular distance between the two forces' lines of action, $2a\sin\theta$, so it is largest at $90^\circ$ and zero when aligned.
    B: |-
      Uses $pE$ without the angle factor, which is the maximum torque, reached only when the dipole is at right angles to the field.
    C: |-
      Thinks a field must pull a dipole along as well as turn it. In a uniform field the forces on $+q$ and $-q$ cancel exactly; only a non-uniform field gives a net force.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A storm over a cricket ground: dark clouds, distant lightning, players walking off, groundstaff dragging a plastic cover and a team bus waiting](scenes/cricket/electric_charges_fields.svg "Another rain delay. The only busy place at the ground is the canteen.")

It's the third rain delay of the day, and the pavilion canteen is packed with players reheating cold samosas and cups of chai in the microwave.

Vikram, the team's twelfth man, reads the sticker on the oven door while he waits. It says the oven works by making the electric field inside it switch direction billions of times a second.

"So the field heats the food?" he asks the canteen owner, who shrugs.

Vikram has just learned that water molecules are electric dipoles: one end slightly positive, the other slightly negative, with no net charge. Something doesn't add up. If the field pushes the positive end one way, it pushes the negative end the other way, equally hard. The pushes should cancel. So how can an electric field do anything at all to a neutral water molecule, never mind heat a samosa?

## The physics

Place a dipole, charges $\pm q$ separated by $2a$, in a **uniform** field $\vec{E}$, with its dipole moment $\vec{p}$ at angle $\theta$ to the field.

**Net force.** The force on $+q$ is $q\vec{E}$, along the field. The force on $-q$ is $-q\vec{E}$, against it. They are equal and opposite, so

$$\vec{F}_\text{net} = q\vec{E} - q\vec{E} = 0$$

Vikram was right about that: a uniform field doesn't push a dipole anywhere.

**Torque.** But the two forces don't act along the same line. They form a **couple**, and a couple twists. The perpendicular distance between their lines of action is $2a\sin\theta$, so the torque has magnitude

$$\tau = qE \times 2a\sin\theta = pE\sin\theta$$

In vector form, $\vec{\tau} = \vec{p} \times \vec{E}$. The torque tries to rotate $\vec{p}$ into line **with** $\vec{E}$.

![A dipole at angle theta to a uniform field pointing right; the force qE on plus q points right and on minus q points left; their lines of action are 2a sin theta apart and they turn p towards E](figures/dipole_in_uniform_field/dipole-torque.svg "Equal and opposite forces: no net push, but a twist. The torque turns p towards the direction of E.")

- $\theta = 0^\circ$: $\tau = 0$. The dipole is aligned; nudge it and the torque brings it back: **stable equilibrium**.
- $\theta = 90^\circ$: $\tau = pE$, the **maximum** torque.
- $\theta = 180^\circ$: $\tau = 0$ again, but nudge it and it swings right round: **unstable equilibrium**.

So the field in Vikram's microwave doesn't drag water molecules anywhere; it *twists* them. Each time the field reverses, the torque reverses, and the molecules are wrenched back and forth billions of times a second. Jostling against their neighbours, they turn that motion into random thermal motion: the food heats up.

**In a non-uniform field**, the forces on $+q$ and $-q$ are no longer equal, so there's a net force as well as a torque. A dipole aligned with the field is pulled towards the stronger-field region. This is how a charged comb attracts neutral scraps of paper.

## Worked example

**Given:** a model dipole with $q = 4.0\,\text{nC}$ and separation $2a = 3.0\,\text{cm}$, in a uniform field $E = 5.0 \times 10^{4}\,\text{N/C}$, with $\vec{p}$ at $\theta = 30^\circ$ to $\vec{E}$ (illustrative values).
**Find:** the torque, the net force, and the largest possible torque.

$$p = q(2a) = 4.0 \times 10^{-9} \times 0.030 = 1.2 \times 10^{-10}\,\text{C m}$$

$$\tau = pE\sin\theta = 1.2 \times 10^{-10} \times 5.0 \times 10^{4} \times 0.50 = 3.0 \times 10^{-6}\,\text{N m}$$

Net force: zero, since the field is uniform.

Maximum torque, at $\theta = 90^\circ$: $pE = 6.0 \times 10^{-6}\,\text{N m}$.

**Check a second way:** each force is $qE = 4.0 \times 10^{-9} \times 5.0 \times 10^{4} = 2.0 \times 10^{-4}\,\text{N}$. The lines of action are $2a\sin 30^\circ = 0.030 \times 0.50 = 0.015\,\text{m}$ apart. Torque of the couple $= 2.0 \times 10^{-4} \times 0.015 = 3.0 \times 10^{-6}\,\text{N m}$. The two methods agree.

For a single water molecule in the same field, the maximum torque is $pE = 6.2 \times 10^{-30} \times 5.0 \times 10^4 = 3.1 \times 10^{-25}\,\text{N m}$: tiny, but acting on a tiny molecule.

## Where the picture breaks

The formula $\tau = pE\sin\theta$ is for a steady, uniform field and a rigid dipole. Inside a microwave oven the field changes billions of times a second and varies from place to place (that's why ovens have turntables), and water molecules are bound to their neighbours in the liquid, so they never simply swing into line. How the twisting turns into heat needs more physics than this chapter has. What carries over exactly is the core idea: a uniform field exerts zero net force but a torque $\vec{p} \times \vec{E}$ on a dipole.

## Key takeaway

In a uniform field, the forces on a dipole's two charges cancel, so the net force is zero, but they form a couple with torque $\vec{\tau} = \vec{p} \times \vec{E}$, of magnitude $pE\sin\theta$. The torque turns $\vec{p}$ towards $\vec{E}$: zero at $0^\circ$ (stable) and $180^\circ$ (unstable), maximum $pE$ at $90^\circ$.
