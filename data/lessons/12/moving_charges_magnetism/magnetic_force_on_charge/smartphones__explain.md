---
concept_id: magnetic_force_on_charge
interest: smartphones
format: explain
title: How a flip cover tells your phone it is closed
check:
  question: |-
    Inside a phone's magnetic sensor, an electron ($q = 1.6\times10^{-19}\,\text{C}$) moves at $1.0\times10^{4}\,\text{m/s}$ through a field of $0.020\,\text{T}$. Its velocity makes an angle of $30^\circ$ with the field. What is the size of the magnetic force on it?
  options:
    A: |-
      $3.2\times10^{-17}\,\text{N}$
    B: |-
      $2.8\times10^{-17}\,\text{N}$
    C: |-
      Zero, because the velocity is not at right angles to the field
    D: |-
      $1.6\times10^{-17}\,\text{N}$
  answer: D
  explanation: |-
    $F = qvB\sin\theta = (1.6\times10^{-19})(1.0\times10^{4})(0.020)(\sin 30^\circ) = 3.2\times10^{-17}\times0.5 = 1.6\times10^{-17}\,\text{N}$. Only the part of the velocity across the field counts.
  misconceptions:
    A: |-
      Ignores the angle and uses $F = qvB$ as if the electron crossed the field at right angles. That is the largest the force can ever be, not its value at $30^\circ$.
    B: |-
      Uses $\cos\theta$ instead of $\sin\theta$. The force depends on the velocity component *perpendicular* to $\vec{B}$, which is $v\sin\theta$; $v\cos\theta$ is the part along the field, which feels no force at all.
    C: |-
      Thinks there is a force only at exactly $90^\circ$. The force is zero only when the velocity is exactly along the field ($\theta = 0^\circ$ or $180^\circ$); at any other angle the perpendicular component feels a force.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A desk with a phone lying on a charging cable showing a swung compass arrow, a wireless charging pad with its coil exposed, a flip-cover case with a small magnet in its flap, and a speaker and a small cylinder-shaped vibration motor taken apart](scenes/smartphones/moving_charges_magnetism.svg "Look at the flip cover: a small magnet sits in its flap. When the flap closes, that magnet lands right over one particular spot inside the phone.")

Aarav's new flip cover has a clear window in the flap, and the screen still goes dark the instant he closes it. So it cannot be the light sensor — light gets straight through the window.

His sister Meenal has a theory. She peels the flap open, finds a small hard disc sewn into its corner, and holds a fridge magnet in the same spot over the bare phone. The screen goes dark. She pulls the magnet away; it lights up again. A steel spoon does nothing. Only the magnet works.

So somewhere under that corner, the phone can feel a magnet. But there is no needle inside a phone, nothing that can swing or click. Just a chip, with current running through it.

How does a small, silent chip notice that a magnet has arrived?

## The physics

The chip is a **Hall sensor**: a thin strip of semiconductor with a small current flowing along it. Current is moving charge — and a magnetic field pushes on a **moving** charge. That push is the whole trick.

For a charge $q$ moving with velocity $\vec{v}$ in a magnetic field $\vec{B}$, the magnetic force is

$$\vec{F} = q\,\vec{v}\times\vec{B}, \qquad F = qvB\sin\theta$$

where $\theta$ is the angle between $\vec{v}$ and $\vec{B}$. With $q$ in coulombs, $v$ in m/s and $B$ in tesla (T), $F$ comes out in newtons. In fact this is how the tesla is defined: $1\,\text{T}$ is the field that pushes $1\,\text{N}$ on $1\,\text{C}$ moving at $1\,\text{m/s}$ at right angles to it.

Three features make this force unlike any you met in mechanics:

- **It needs motion.** A charge at rest feels no magnetic force at all.
- **It is zero along the field.** If $\vec{v}$ is parallel to $\vec{B}$, $\sin\theta = 0$. It is largest, $qvB$, at right angles.
- **It is perpendicular to both $\vec{v}$ and $\vec{B}$.** Point the fingers of your right hand along $\vec{v}$, curl them towards $\vec{B}$; the thumb gives $\vec{v}\times\vec{B}$ — the force on a **positive** charge. For a negative charge, such as an electron, the force is the **opposite** way.

![A uniform magnetic field into the page, with a positive charge moving right feeling an upward force, a negative charge moving right feeling a downward force, and a charge moving along the field feeling nothing](figures/magnetic_force_on_charge/force-on-moving-charge.svg "Same field, same direction of motion: the positive charge is pushed one way, the negative charge the other. Along the field, no push at all.")

In the sensor, the cover's magnet pushes the moving charges sideways, towards one edge of the strip. Charge piles up on that edge, and a small voltage appears *across* the strip. The chip reads that voltage and tells the phone "cover closed".

## Worked example

**Given:** an electron drifting along the sensor strip at, say, $v = 1000\,\text{m/s}$ (illustrative). The cover's magnet gives $B = 0.010\,\text{T}$ at the chip, at right angles to the strip.
**Find:** the size of the force on the electron, how it compares with its weight, and which way it points.

**Step 1 — the size.** At right angles, $\sin 90^\circ = 1$:

$$F = qvB = (1.6\times10^{-19})(1000)(0.010) = 1.6\times10^{-18}\,\text{N}$$

**Step 2 — is that big?** The electron's weight is $mg = (9.1\times10^{-31})(9.8) \approx 8.9\times10^{-30}\,\text{N}$. The magnetic push is about $2\times10^{11}$ times bigger. Gravity doesn't matter here at all.

**Step 3 — the direction.** Lay the phone face up. Say the electrons drift to the **right** along the strip, and the magnet's field points **down** into the phone. For a positive charge, $\vec{v}\times\vec{B}$ (right, crossed with down) points towards the **top** edge of the phone. The electron is negative, so its force points towards the **bottom** edge — and that is where electrons pile up.

**Sanity check:** reverse the magnet and the force reverses, so a sensor like this can even tell which pole of the magnet is facing it.

## Where the picture breaks

A real electron in a semiconductor does not glide at a steady $1000\,\text{m/s}$; it jostles and collides constantly, and $v$ is only its average **drift** velocity. The formula applies to that average motion.

The sideways push does not continue forever. As charge piles up on one edge, it makes an electric field across the strip that pushes back. Very quickly the two forces balance and the pile stops growing — that steady voltage is what the chip measures.

And the magnetic force never speeds a charge up or slows it down: it is always at right angles to the motion, so it does no work. The energy for the chip's reading comes from the phone's battery, not from the magnet.

## Key takeaway

A magnetic field pushes on a **moving** charge with $\vec{F} = q\,\vec{v}\times\vec{B}$, of size $F = qvB\sin\theta$. The force is zero for a charge at rest or moving along the field, largest at right angles, and always perpendicular to both $\vec{v}$ and $\vec{B}$ — reversed for a negative charge. A flip cover's magnet uses exactly this to shove electrons sideways in a sensor chip.
