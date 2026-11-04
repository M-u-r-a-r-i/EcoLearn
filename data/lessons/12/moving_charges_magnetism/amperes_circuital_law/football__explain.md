---
concept_id: amperes_circuital_law
interest: football
format: explain
title: How far from the feeder is far enough
check:
  question: |-
    A long straight cable carries a steady current. At $10\,\text{cm}$ from its axis the magnetic field is $200\,\mu\text{T}$. What is the field at $40\,\text{cm}$ from the axis?
  options:
    A: |-
      $50\,\mu\text{T}$
    B: |-
      $12.5\,\mu\text{T}$
    C: |-
      $25\,\mu\text{T}$
    D: |-
      $200\,\mu\text{T}$ — unchanged, because the same current is still enclosed.
  answer: A
  explanation: |-
    For a long straight wire $B = \dfrac{\mu_0 I}{2\pi r}$, so the field falls as $1/r$. Four times the distance means a quarter of the field: $200/4 = 50\,\mu\text{T}$.
  misconceptions:
    B: |-
      Applies the $1/r^{2}$ of a single current element to the whole wire. Adding up every element of a long straight wire turns the inverse square into an inverse first power.
    C: |-
      Uses an inverse-cube law, which belongs to the distant field of a small loop or a dipole, not to a straight wire.
    D: |-
      Reads Ampère's law as "same enclosed current, same field". What stays the same is the *integral* $\oint \vec{B}\cdot d\vec{l}$; on a bigger loop that total is spread over a longer path, so $B$ itself is smaller.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A football ground with a coil traced around the goal frame, a pop-up sprinkler on a solenoid valve, an electric line-marking machine and a horn speaker on a pole with a compass lying on its supply cable](scenes/football/moving_charges_magnetism.svg "Everything on this ground draws its power through one heavy feeder cable buried under the touchline.")

Two hours before kick-off, Pooja — the ground's electrician for eleven years — walks the length of the touchline and makes the broadcast crew unhappy.

They have set their camera control boxes down in the neatest possible line, tucked against the wall of the tunnel, out of everybody's way. Pooja makes them shift the whole lot a metre out into the open, where people will trip over the cables all evening.

Her reason sounds like superstition: the main feeder to the floodlights runs inside that wall. Nobody is touching it. It is insulated, buried and perfectly safe. The crew ask what harm an insulated cable can possibly do to a box that isn't plugged into it.

Pooja says only this: a metre makes it ten times better. Ten times better than *what* — and how does she know it is ten?

## The physics

She knows because the field around a long straight wire obeys a law with a shape you can carry in your head.

**Ampère's circuital law** says: take any closed loop in space — an imaginary one, drawn wherever you like — and add up the component of $\vec{B}$ along it, all the way round. The total depends on nothing except the current threading through that loop:

$$\oint \vec{B} \cdot d\vec{l} = \mu_0 I_\text{enc}$$

$I_\text{enc}$ is the **net** current passing through the loop; currents outside it contribute nothing to the total, however strong they are.

![A circular Amperian loop around a wire carrying current out of the page, with B the same size all round and tangent to the circle; and a second loop enclosing no current](figures/amperes_circuital_law/amperian-loop-long-wire.svg "Choose the loop to match the symmetry of the field, and the integral becomes B × (2πr).")

By itself that is a statement, not a calculating tool. It becomes one when the field is **symmetric** enough that you can guess its shape and pull $B$ out of the sum. For a long straight wire you already know the shape from Oersted: circles round the wire. So choose the loop to be one of those circles, of radius $r$:

- $\vec{B}$ is tangent to the loop at every point, so $\vec{B} \cdot d\vec{l} = B\,dl$ everywhere;
- by symmetry $B$ has the same size all the way round, so it comes out of the sum;
- what is left of the sum is the circumference, $2\pi r$.

$$B \times 2\pi r = \mu_0 I \qquad \Longrightarrow \qquad B = \frac{\mu_0 I}{2\pi r}$$

That $1/r$ is Pooja's ten. Ten times the distance, a tenth of the field — a gentler fall than the $1/r^{2}$ of a single current element, because the far parts of a long wire keep contributing.

Two conditions: the wire must be long compared with $r$ (so the field really is circular), and the current steady. The law itself is always true; it is only *useful* where there is symmetry to exploit.

## Worked example

**Given:** the feeder carries $I = 100\,\text{A}$ to the floodlights. Take $\dfrac{\mu_0}{2\pi} = 2 \times 10^{-7}\,\text{T}\,\text{m}\,\text{A}^{-1}$.
**Find:** the field at $10\,\text{cm}$ from the cable, and at $1.0\,\text{m}$.

**Step 1 — at $r = 0.10\,\text{m}$.**

$$B = \frac{\mu_0 I}{2\pi r} = \frac{(2 \times 10^{-7})(100)}{0.10} = 2 \times 10^{-4}\,\text{T}$$

Two hundred microtesla — about four times the Earth's field. A box of sensitive electronics sitting in that is sitting in a field bigger than the planet's.

**Step 2 — at $r = 1.0\,\text{m}$.** Ten times the distance, so a tenth of the field: $2 \times 10^{-5}\,\text{T}$, or $20\,\mu\text{T}$ — now smaller than the Earth's own field, and lost in it.

**Sanity check:** one metre takes the crew's equipment from "four times the Earth's field" to "less than the Earth's field". That is a real change, and it explains why Pooja cares about a metre and not about ten.

## Where the picture breaks

A buried feeder is not one wire. It carries its outward and return conductors side by side, and an Amperian loop drawn around both encloses $I - I = 0$. Their fields very nearly cancel a short distance away, so the real cable is a far weaker source than this calculation — which is why a metre is enough, and not ten.

The formula also treats the wire as infinitely long and infinitely thin. Inside a thick conductor the enclosed current is only the fraction the loop contains, and the field there *grows* with $r$ instead of falling.

Finally, floodlights run on alternating current, so the field reverses fifty times a second. The size calculated here is right, but a compass would sit still in it; the broadcast crew's problem is the electrical hum it induces in their cables, not a steady push.

## Key takeaway

Ampère's circuital law, $\oint \vec{B} \cdot d\vec{l} = \mu_0 I_\text{enc}$, says the field added up around any closed loop depends only on the current threading it. Choose a loop that matches the symmetry — a circle around a long straight wire — and it gives $B = \dfrac{\mu_0 I}{2\pi r}$ in one line.
