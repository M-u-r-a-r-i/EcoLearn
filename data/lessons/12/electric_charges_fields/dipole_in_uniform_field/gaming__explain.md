---
concept_id: dipole_in_uniform_field
interest: gaming
format: explain
title: What a pixel does in a millisecond
check:
  question: |-
    A small dipole sits in a uniform electric field with $\vec{p}$ at $90^\circ$ to $\vec{E}$, where the torque on it is $8.0 \times 10^{-6}\,\text{N m}$. It is then turned until $\vec{p}$ is at $30^\circ$ to $\vec{E}$. What are the torque and the net force on it now?
  options:
    A: |-
      Torque $6.9 \times 10^{-6}\,\text{N m}$; net force zero
    B: |-
      Torque $8.0 \times 10^{-6}\,\text{N m}$; net force zero
    C: |-
      Torque $4.0 \times 10^{-6}\,\text{N m}$; a net force along the field
    D: |-
      Torque $4.0 \times 10^{-6}\,\text{N m}$; net force zero
  answer: D
  explanation: |-
    $\tau = pE\sin\theta$, and the given value is the maximum $pE$ (at $90^\circ$), so at $30^\circ$ the torque is $8.0 \times 10^{-6} \times \sin 30^\circ = 4.0 \times 10^{-6}\,\text{N m}$. In a uniform field the forces $+q\vec{E}$ and $-q\vec{E}$ are equal and opposite, so the net force stays zero at every angle.
  misconceptions:
    A: |-
      Uses $\cos\theta$ instead of $\sin\theta$. The torque comes from the perpendicular separation of the two lines of action, $2a\sin\theta$, so it is largest at $90^\circ$ and zero when $\vec{p}$ is aligned with $\vec{E}$.
    B: |-
      Thinks the torque does not depend on the angle, so the dipole would keep twisting just as hard even once it lined up with the field.
    C: |-
      Thinks a field that turns a dipole must also drag it along. In a *uniform* field the two forces cancel exactly; only a non-uniform field gives a net force.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A gaming desk at night during a PC build: a monitor running a field sandbox with two charges, a plasma globe, an antistatic bag sparking to a fingertip, and an open PC case with a graphics card going in](scenes/gaming/electric_charges_fields.svg "Every image on that monitor is made by switching tiny electric fields on and off inside the panel.")

At the LAN café near his school, Devansh has two machines side by side for the first time: his usual one at 60 Hz, and the new one at 144 Hz. He flicks the mouse across both screens.

The difference is obvious and annoying. On the 60 Hz screen each frame sits there for about 17 milliseconds and a fast flick smears. On the other, everything snaps.

The café owner, who repairs the panels himself, is unimpressed by the argument breaking out. "It isn't only the frame rate," he says. "Inside the panel there are rod-shaped molecules between two transparent electrodes. Put a voltage across a pixel and the molecules swing into line with the field — that's how the pixel changes what it lets through. The swinging takes a few milliseconds, and that's your smear."

Devansh already knows those molecules are electric dipoles: one end slightly positive, one slightly negative, no net charge. Which makes the story sound impossible. If the field pushes the positive end one way, it pushes the negative end the other way, just as hard. The pushes cancel. So how can a field do *anything* to a neutral molecule?

## The physics

Put a dipole — charges $\pm q$ separated by $2a$ — into a **uniform** field $\vec{E}$, with its dipole moment $\vec{p}$ at an angle $\theta$ to the field.

**Net force.** The force on $+q$ is $q\vec{E}$, along the field; the force on $-q$ is $-q\vec{E}$, against it. They are equal and opposite, so

$$\vec{F}_\text{net} = q\vec{E} - q\vec{E} = 0$$

Devansh is right about that part: a uniform field does not push a dipole anywhere.

**Torque.** But the two forces do not act along the same line. They form a **couple**, and a couple twists. The perpendicular distance between their lines of action is $2a\sin\theta$, so

$$\tau = qE \times 2a\sin\theta = pE\sin\theta$$

and in vector form $\vec{\tau} = \vec{p} \times \vec{E}$. The torque turns $\vec{p}$ **towards** $\vec{E}$.

![A dipole at an angle to a uniform field pointing right, with the force qE on plus q pointing right and minus qE on minus q pointing left, their lines of action separated by 2a sin theta, turning p towards E](figures/dipole_in_uniform_field/dipole-torque.svg "Equal and opposite forces: no net push, but a twist. The torque turns p towards the direction of E.")

- $\theta = 0^\circ$: $\tau = 0$, and a nudge brings it back — **stable equilibrium**.
- $\theta = 90^\circ$: $\tau = pE$, the **maximum** torque.
- $\theta = 180^\circ$: $\tau = 0$ again, but a nudge sends it swinging right round — **unstable equilibrium**.

So the café owner's account survives: the pixel's field does not drag its molecules anywhere, it *turns* them, and they settle pointing along the field.

**In a non-uniform field**, the forces on $+q$ and $-q$ are no longer equal, so there is a net force as well as a torque, pulling a lined-up dipole towards the stronger-field region. That is why the charged screen in the corner of the room collects dust.

## Worked example

**Given (illustrative):** a model dipole with $q = 2.0\,\text{nC}$ and $2a = 1.0\,\text{cm}$, sitting in a uniform field $E = 1.0 \times 10^{4}\,\text{N/C}$ with $\vec{p}$ at $\theta = 30^\circ$ to $\vec{E}$.
**Find:** the torque on it, the net force, and the largest torque it could feel.

**Step 1 — the dipole moment.**

$$p = q(2a) = 2.0 \times 10^{-9} \times 0.010 = 2.0 \times 10^{-11}\,\text{C m}$$

**Step 2 — the torque.** With $\sin 30^\circ = 0.50$:

$$\tau = pE\sin\theta = 2.0 \times 10^{-11} \times 1.0 \times 10^{4} \times 0.50 = 1.0 \times 10^{-7}\,\text{N m}$$

The net force is **zero**, because the field is uniform — the dipole turns on the spot and goes nowhere.

**Step 3 — the maximum.** At $\theta = 90^\circ$, $\tau = pE = 2.0 \times 10^{-7}\,\text{N m}$: twice what it feels at $30^\circ$.

**Check it a second way:** each force is $qE = 2.0 \times 10^{-9} \times 1.0 \times 10^{4} = 2.0 \times 10^{-5}\,\text{N}$, and their lines of action are $2a\sin 30^\circ = 0.0050\,\text{m}$ apart, giving $2.0 \times 10^{-5} \times 0.0050 = 1.0 \times 10^{-7}\,\text{N m}$. The two routes agree.

**Sanity check:** a torque of a ten-millionth of a newton metre is minute, but so is the thing it turns — and a molecule has almost no rotational inertia to overcome.

## Where the picture breaks

A pixel is not a single dipole in a steady field. The molecules are packed shoulder to shoulder and pull on their neighbours elastically, which is most of why the switch takes milliseconds rather than nanoseconds; the panel drives them with an *alternating* voltage to stop charge building up; and how strongly a given molecule responds depends on the field inducing a dipole in it as well as on any permanent one. Real panels also use several tricks to speed the switch up, none of them in this chapter.

What carries over exactly is the core result: in a uniform field a dipole feels **no net force** and a torque $\vec{p} \times \vec{E}$ that turns it into line.

## Key takeaway

In a uniform field the forces on a dipole's two charges cancel, so the net force is zero — but they form a couple with torque $\vec{\tau} = \vec{p} \times \vec{E}$, of magnitude $pE\sin\theta$. The torque turns $\vec{p}$ towards $\vec{E}$: zero at $0^\circ$ (stable), maximum $pE$ at $90^\circ$, zero again at $180^\circ$ (unstable). A net force appears only in a non-uniform field.
