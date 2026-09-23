---
concept_id: biot_savart_law
interest: football
format: explain
title: Adding up a goal frame, centimetre by centimetre
check:
  question: |-
    A short current element contributes a field of magnitude $dB$ at a point $P$ that lies a distance $r$ away, in a direction perpendicular to the element. A second, identical element sits a distance $2r$ from $P$, also perpendicular to the line joining them. What does it contribute at $P$?
  options:
    A: |-
      $dB/2$
    B: |-
      $dB/8$
    C: |-
      $dB/4$
    D: |-
      Nothing — a single element on its own cannot produce a field.
  answer: C
  explanation: |-
    $dB = \dfrac{\mu_0}{4\pi}\dfrac{I\,dl\sin\theta}{r^{2}}$ falls off as the **square** of the distance, so doubling $r$ divides the contribution by four.
  misconceptions:
    A: |-
      Uses the $1/r$ dependence that belongs to a whole long straight wire. That $1/r$ is the *result* of adding up every element; a single element falls off as $1/r^{2}$.
    B: |-
      Applies an inverse-cube law, which belongs to the far field of a magnetic dipole, not to a current element.
    D: |-
      Knows that an isolated steady current element cannot exist and concludes that it contributes nothing. Every element contributes; the law gives its share, and the field of the circuit is the sum of all of them.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A football ground with a coil traced around the goal frame, a pop-up sprinkler on a solenoid valve, an electric line-marking machine and a horn speaker on a pole with a compass lying on its supply cable](scenes/football/moving_charges_magnetism.svg "Look at the thin cable traced around the goal frame: every centimetre of it adds its own bit of magnetic field.")

Harsh has come early to watch the engineers fit out his district's ground for a tournament, and he has found the strangest job of the day: a technician threading a thin cable all the way around the goal frame, up one post, along the crossbar and down the other, and taping it into the groove.

It is not a floodlight cable and it is not a net. It carries a small current and makes a weak magnetic field across the goal mouth, so that a coil hidden in the match ball can tell the system when the whole ball has crossed the line.

Harsh asks the obvious question: how strong is the field in the middle of the goal? The technician laughs and says the design team modelled it — the frame is $7.32\,\text{m}$ wide and $2.44\,\text{m}$ high, and no single formula covers a rectangle of wire.

But there must be *some* rule. A metre of cable up the left post is nowhere near the centre of the goal; a metre of crossbar is right above it. How does one piece of wire know what to contribute?

## The physics

It doesn't have to. The **Biot–Savart law** hands every short piece of the circuit its own share, and the field is the sum of all the shares.

Take a piece of wire so short you can call it $d\vec{l}$, pointing along the conventional current $I$, and a point $P$ a distance $r$ away, with $\theta$ the angle between $d\vec{l}$ and the line to $P$. That piece contributes

$$d\vec{B} = \frac{\mu_0}{4\pi}\,\frac{I\,d\vec{l} \times \hat{r}}{r^{2}}, \qquad dB = \frac{\mu_0}{4\pi}\,\frac{I\,dl\,\sin\theta}{r^{2}}$$

![A short element of a current-carrying wire, the vector r to a point P, the angle theta between them, and the resulting dB into the page at P](figures/biot_savart_law/current-element-dB.svg "One short piece of wire, one contribution. The whole field is the sum over every piece of the circuit.")

Here $\mu_0$ is the **permeability of free space**, $\mu_0 = 4\pi \times 10^{-7}\,\text{T}\,\text{m}\,\text{A}^{-1}$, so the useful combination is $\dfrac{\mu_0}{4\pi} = 10^{-7}\,\text{T}\,\text{m}\,\text{A}^{-1}$.

Four features answer Harsh's question:

- **It falls off as $1/r^{2}$.** The far post contributes far less than the crossbar overhead — four times less at twice the distance.
- **Direction is a cross product.** $d\vec{B}$ is perpendicular to the plane containing $d\vec{l}$ and $\hat{r}$, given by the right hand: fingers along the current, curled towards $\hat{r}$. It is *not* directed along $r$, which is where it parts company with Coulomb's law.
- **Nothing straight ahead.** At a point on the line of the element itself, $\theta = 0$ and $\sin\theta = 0$: a piece of wire sends no field along its own direction.
- **Superposition.** Contributions add as vectors. Every result later in this chapter — the loop, the solenoid, Ampère's law — is this sum, done for a shape neat enough to do it.

The condition of validity: the law is for **steady currents** in a circuit. It also has no meaning for one element alone, because a steady current cannot start and stop in mid-air; the element is a bookkeeping device for a closed loop.

## Worked example

**Given:** a $1.0\,\text{cm}$ length of the goal-frame cable carries $I = 10\,\text{A}$. Point $P$ lies $0.10\,\text{m}$ from it, in the direction perpendicular to that piece of cable ($\theta = 90°$).
**Find:** what that centimetre contributes at $P$, and what a second centimetre pointing straight at $P$ contributes.

**Step 1 — the perpendicular piece.** With $\sin 90° = 1$,

$$dB = \frac{\mu_0}{4\pi}\frac{I\,dl}{r^{2}} = 10^{-7} \times \frac{(10)(0.010)}{(0.10)^{2}} = 10^{-7} \times \frac{0.10}{0.010} = 1.0 \times 10^{-6}\,\text{T}$$

One microtesla — a few per cent of the Earth's own field, from one centimetre of cable.

**Step 2 — the piece pointing at $P$.** Same current, same length, same distance, but now $\theta = 0$, so $\sin\theta = 0$ and it contributes **nothing**. Where a piece of wire points matters as much as how far away it is.

**Sanity check:** one centimetre gives a field far too weak to notice, and the whole frame is over twenty metres of cable — so a measurable field across the goal mouth, built from thousands of tiny contributions, is exactly what you should expect.

## Where the picture breaks

The diagram shows an element in splendid isolation, and you cannot buy one. Current has to arrive and leave, so $d\vec{l}$ is always part of a loop, and only the *total* over a closed circuit is something you can measure. The law is a rule for splitting a real circuit into manageable pieces, not a description of a physical object.

The inverse square invites a comparison with Coulomb's law that only half works. Both fall off as $1/r^{2}$, but an electric field points along $\hat{r}$ while $d\vec{B}$ points at right angles to it, and a current element has a direction while a point charge does not.

And for Harsh's rectangle there is still no tidy formula. Adding up the four straight sides of a goal frame at an arbitrary point is a job for a computer — which is precisely what the design team did.

## Key takeaway

The Biot–Savart law gives the field contributed by a short piece of a current-carrying circuit: $dB = \dfrac{\mu_0}{4\pi}\dfrac{I\,dl\sin\theta}{r^{2}}$, directed perpendicular to both the element and the line to the point. Fields from every element add as vectors, and that sum is where every other formula in this chapter comes from.
