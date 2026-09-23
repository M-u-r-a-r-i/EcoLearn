---
concept_id: amperes_circuital_law
interest: cricket
format: explain
title: Reading a cable without cutting it
check:
  question: |-
    A long straight wire carries a steady current. You draw a circular Amperian loop nearby that does **not** enclose the wire. Which statement is correct?
  options:
    A: |-
      The magnetic field is zero at every point on that loop.
    B: |-
      $\oint \vec{B}\cdot d\vec{l}$ is not zero, because $\vec{B}$ is not zero on the loop.
    C: |-
      Ampère's law cannot be applied to a loop that misses the wire.
    D: |-
      $\oint \vec{B}\cdot d\vec{l} = 0$, even though $\vec{B}$ is not zero anywhere on the loop.
  answer: D
  explanation: |-
    Ampère's law sets $\oint \vec{B}\cdot d\vec{l} = \mu_0 I_\text{enclosed}$, and this loop encloses no current. The field is still there — the contributions simply cancel as you travel once round.
  misconceptions:
    A: |-
      Reads "the integral is zero" as "the field is zero". A wire's field fills all the space around it; only the *sum* around this particular loop vanishes.
    B: |-
      Assumes a non-zero $\vec{B}$ must give a non-zero integral. $\vec{B}\cdot d\vec{l}$ is positive along part of the loop and negative along the rest, and they cancel exactly.
    C: |-
      Thinks the law only holds for the convenient symmetric loops used in textbooks. It holds for *every* closed loop; symmetry only decides whether it is **useful** for finding $B$.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A cricket ground with an electric roller, a compass lying on a thick power cable, a bowling machine and a loudspeaker on a pole](scenes/cricket/moving_charges_magnetism.svg "The feeder cable to the floodlight tower carries enough current to be read from outside its insulation.")

Two of the four floodlight towers are dimmer than the others, and the club has a night match on Friday. The electrician arrives with a tool Divya has not seen before: something like a pair of tongs with a display on the handle.

She expects him to switch off the supply and open the panel. He does neither. He reaches into the cabinet with the power still on, closes the jaws of the tool loosely around one thick cable — not touching a single bare conductor, not cutting anything — and reads a number off the screen.

"Ninety-eight amps on that phase," he says. "The other one's low."

Divya stares at the jaws. There is a ring of steel around a cable, and nothing else. The current is flowing *inside* the insulation, and the meter never touched it. So what exactly is the ring reading?

## The physics

It is reading the magnetic field that the current cannot help but produce around itself — and the rule connecting that field to the current is **Ampère's circuital law**:

$$\oint \vec{B}\cdot d\vec{l} = \mu_0 I_\text{enclosed}$$

In words: walk once around any closed loop, adding up the component of $\vec{B}$ along your path at every step. The total depends on nothing but the current passing *through* the loop. The shape of the loop, and where the current sits inside it, make no difference at all.

![A circular Amperian loop around a wire carrying current out of the page, with B the same size all round and tangent to the circle; and a second loop enclosing no current](figures/amperes_circuital_law/amperian-loop-long-wire.svg "Choose the loop to match the symmetry of the field, and the integral becomes B × (2πr).")

This is the magnetic twin of Gauss's law, and it is used the same way: not as a formula to substitute into, but as a shortcut when the symmetry is right.

For a long straight wire, the symmetry is perfect. The field lines are circles centred on the wire (the grip rule), so if you choose a circle of radius $r$ as your loop, then at every point $\vec{B}$ is along your path and has the same magnitude $B$. The integral is just $B$ times the length of the path:

$$B\,(2\pi r) = \mu_0 I \qquad\Longrightarrow\qquad B = \frac{\mu_0 I}{2\pi r}$$

That is the result the last two lessons kept borrowing, and it took one line instead of a full Biot–Savart sum. Note the $1/r$: the field of a long wire falls off far more gently than the $1/r^{2}$ of a single element, because a longer stretch of wire comes into play as you move away.

The law holds for steady currents, and the shortcut only works where the symmetry lets you pull $B$ out of the integral.

## Worked example

**Given:** a floodlight feeder cable carries $100\,\text{A}$.
**Find:** the magnetic field $10\,\text{cm}$ from its axis, outside the insulation.

$$B = \frac{\mu_0 I}{2\pi r} = \frac{(4\pi \times 10^{-7})(100)}{2\pi (0.10)} = \frac{(2 \times 10^{-7})(100)}{0.10} = 2 \times 10^{-4}\,\text{T}$$

That is about four times the Earth's own magnetic field — a compass held there would swing hard round to point along the cable's field circle, ignoring north completely.

Because $B \propto 1/r$, stepping back to $20\,\text{cm}$ halves it, to $1 \times 10^{-4}\,\text{T}$.

**Sanity check:** a hundred amps producing a few times the Earth's field a hand's width away is the right size — strong enough for an instrument to read easily, far too weak to feel.

## Where the picture breaks

The clamp meter is not quite doing the integral in the diagram. Its steel ring guides the field around the cable and a winding on that ring senses it, which for alternating current works by induction (the next chapter) and for direct current needs a separate sensor inside the jaws. What Ampère's law explains is the part underneath all of that: the field outside a cable depends only on the current enclosed by the ring.

And this is exactly why the jaws must go around **one** conductor. Close them around the whole flat cable, live and return together, and the enclosed current is $I - I = 0$: the meter reads nothing, however much power the floodlight is drawing. The same cancellation is why the roller's cable barely disturbed a compass in the first lesson of this chapter.

Finally, "long straight wire" is an idealisation. Near the ends of a cable, or near a bend, the field is not a set of neat circles and the shortcut fails — though the law itself is still true.

## Key takeaway

Ampère's circuital law says $\oint \vec{B}\cdot d\vec{l} = \mu_0 I_\text{enclosed}$ for any closed loop: only the current threading the loop matters. Choose a loop that matches the symmetry and it becomes a fast way to find $B$ — for a long straight wire, $B = \dfrac{\mu_0 I}{2\pi r}$.
