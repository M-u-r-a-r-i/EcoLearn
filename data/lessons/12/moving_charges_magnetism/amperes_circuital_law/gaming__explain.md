---
concept_id: amperes_circuital_law
interest: gaming
format: explain
title: Why magnetism refuses to fade
check:
  question: |-
    Two long straight cables run side by side from a battery bank: one carries $100\,\text{A}$ out to the inverter, the other carries the same $100\,\text{A}$ back. You draw one Amperian loop that encloses **both** cables. What is $\oint \vec{B}\cdot d\vec{l}$ around that loop, and is $\vec{B}$ zero on it?
  options:
    A: |-
      $\mu_0 \times 200\,\text{A}$, because both cables pass through the loop.
    B: |-
      $\mu_0 \times 100\,\text{A}$, because only the cable carrying current outwards should be counted.
    C: |-
      Zero, and $\vec{B}$ is zero at every point of the loop as well.
    D: |-
      Zero, even though $\vec{B}$ is not zero anywhere on the loop.
  answer: D
  explanation: |-
    $I_\text{enclosed}$ is the **net** current threading the loop, and the two cables carry equal currents in opposite senses: $+100 - 100 = 0$. Each cable still has its own field all around it; what cancels is the sum of $\vec{B}\cdot d\vec{l}$ once you go right round.
  misconceptions:
    A: |-
      Adds the sizes of the currents and ignores their directions. Currents threading a loop in opposite senses subtract, they do not add.
    B: |-
      Counts only the current flowing the "useful" way. Both conductors pass through the loop and both must be counted — with opposite signs.
    C: |-
      Reads "the integral is zero" as "the field is zero". Move a compass anywhere along that loop and it will feel something; only the total around the closed path vanishes.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A gaming workbench with a bartop arcade cabinet, a cutaway of a pinball flipper coil, a controller with its shell off, a PC case fan, and a phone on a power cable showing a swung compass needle](scenes/gaming/moving_charges_magnetism.svg "A CRT paints its picture by steering electrons — so a stray field from a nearby cable shows up on the screen as a tilt.")

The retro corner at the college gaming fest has six CRT cabinets, borrowed and carried in that morning, and Sunita has spent an hour lining them up along the back wall. The hall's supply is unreliable, so the whole corner runs off a battery bank standing in the angle of the wall, with two thick single leads going from the batteries to the inverter.

The organiser tells her to move the end cabinet. Sunita points out that the leads are insulated, taped down and touching nothing. He switches the bank on anyway. On the end cabinet the picture leans: straight edges tilt and a white box picks up faint colour in one corner. The other five are perfect.

She drags it half a metre clear and the picture straightens. Then, curious, she pulls it back to a quarter of a metre — expecting the tilt to be four times worse.

It is only twice as bad. Why is magnetism so reluctant to fade?

## The physics

Because of a law with a shape you can carry in your head. **Ampère's circuital law** says: take any closed loop you like, imaginary, any shape, anywhere. Walk once round it, adding up the component of $\vec{B}$ along your path at every step. The total depends on nothing but the current threading *through* the loop:

$$\oint \vec{B}\cdot d\vec{l} = \mu_0 I_\text{enclosed}$$

Currents outside the loop contribute nothing to the total, however large they are, and it makes no difference where inside the loop the current runs.

![A circular Amperian loop around a wire carrying current out of the page, with B the same size all round and tangent to the circle; and a second loop enclosing no current](figures/amperes_circuital_law/amperian-loop-long-wire.svg "Choose the loop to match the symmetry of the field, and the integral becomes B × (2πr).")

By itself that is a statement, not a calculating tool. It becomes one when the field is symmetric enough that you can guess its shape and pull $B$ out of the sum. For a long straight wire you already know the shape from Oersted: circles round the wire. So choose your loop to *be* one of those circles, of radius $r$:

- $\vec{B}$ is tangent to the path at every point, so $\vec{B}\cdot d\vec{l} = B\,dl$ all the way round;
- by symmetry $B$ has the same size everywhere on the circle, so it comes out of the sum;
- what is left of the sum is the circumference, $2\pi r$.

$$B\,(2\pi r) = \mu_0 I \qquad\Longrightarrow\qquad B = \frac{\mu_0 I}{2\pi r} \qquad\text{with}\qquad \frac{\mu_0}{2\pi} = 2\times10^{-7}$$

There is Sunita's answer, sitting in the denominator: $r$, not $r^{2}$. A single current element does fall off as $1/r^{2}$, as Biot–Savart says — but as you back away from a long wire, more and more of its length gets close enough to matter, and that extra length almost makes up for the extra distance. What survives is a $1/r$ law. Double your distance from a long cable and you halve its field; you do not quarter it.

The law holds for steady currents. The shortcut only works where the symmetry lets you pull $B$ out of the integral.

![Engraved portrait of a man in early nineteenth-century dress](famous/andre-marie-ampere-1825.jpg "André-Marie Ampère (1775–1836), engraved in 1825. Within weeks of hearing of Ørsted's discovery he had turned it into the law that carries his name. Public domain, via Wikimedia Commons.")

## Worked example

**Given:** the lead from the battery bank to the inverter carries about $100\,\text{A}$ (an illustrative value for a bank of that size).
**Find:** the field it makes at $25\,\text{cm}$, and at $50\,\text{cm}$.

**Step 1 — at $25\,\text{cm}$.**

$$B = \frac{\mu_0 I}{2\pi r} = \frac{(2\times10^{-7})(100)}{0.25} = 8\times10^{-5}\,\text{T}$$

Eighty microtesla — not far off twice the Earth's own magnetic field, and pointing sideways instead of north. That is plenty to pull a CRT's electron beam off its aim.

**Step 2 — at $50\,\text{cm}$.** Twice the distance, and $B \propto 1/r$, so simply half:

$$B = 4\times10^{-5}\,\text{T}$$

About the size of the Earth's field — which every CRT ever built already has to live with, and is set up to ignore.

**Sanity check:** the cabinet was fine at half a metre and bad at a quarter, and the numbers say the field there was roughly double. A rule that says "twice as close, twice as bad" matches exactly what Sunita saw on the screen.

## Where the picture breaks

"Long straight wire" is an idealisation. Near the ends of a cable, or near a bend, the field lines are not neat circles and the shortcut collapses — although the law itself is still perfectly true; it has just stopped being *useful*.

It also matters enormously that the battery leads run **separately**. In an ordinary extension lead the go and return conductors sit side by side inside one sheath, their enclosed currents cancel, and the field a short distance away is almost nothing. That is why the hall's other cabling did nothing to the cabinets, and why the one place with separated single conductors was the one place with a problem.

The tilt on the screen is also only the beginning of the story. What the stray field really does is push sideways on the electrons crossing the tube, which is the lesson before last; Ampère's law only tells you how strong that stray field is.

Finally, this form of the law is for **steady** currents. When currents change, a term has to be added — you will meet it in a later chapter.

## Key takeaway

Ampère's circuital law says $\oint \vec{B}\cdot d\vec{l} = \mu_0 I_\text{enclosed}$ for **any** closed loop: only the net current threading the loop matters. Choose a loop that matches the symmetry and it becomes a fast way to find $B$ — for a long straight wire, $B = \dfrac{\mu_0 I}{2\pi r}$, falling off as $1/r$ and not as $1/r^{2}$.
