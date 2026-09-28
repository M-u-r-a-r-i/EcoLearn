---
concept_id: amperes_circuital_law
interest: smartphones
format: explain
title: Predicting what the magnetometer app will read
check:
  question: |-
    A phone charging cable contains two wires side by side: one carries $2.0\,\text{A}$ to the phone, the other carries the same $2.0\,\text{A}$ back. Imagine a closed loop drawn around the **whole cable**, enclosing both wires. What is the value of $\oint \vec{B}\cdot d\vec{l}$ around this loop?
  options:
    A: |-
      $\mu_0 \times 4.0\,\text{A}$
    B: |-
      Zero
    C: |-
      $\mu_0 \times 2.0\,\text{A}$
    D: |-
      It depends on the size and shape of the loop
  answer: B
  explanation: |-
    Ampere's law says $\oint \vec{B}\cdot d\vec{l} = \mu_0 I_\text{enc}$, where $I_\text{enc}$ is the **net** current through the loop. The two currents are equal and opposite, so $I_\text{enc} = 2.0 - 2.0 = 0$, and the integral is zero. (That doesn't mean $B$ is zero at every point of the loop — only that the sum around it is.)
  misconceptions:
    A: |-
      Adds the sizes of the two currents and ignores their directions. The enclosed current is a net value: currents in opposite directions through the loop cancel.
    C: |-
      Counts only one of the wires, as if the return wire did not count. Every current that passes through the loop contributes, with its sign.
    D: |-
      Thinks the line integral changes with the loop. For steady currents it depends only on the net current enclosed — any loop around the whole cable gives the same answer.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A desk with a phone lying on a charging cable showing a swung compass arrow, a wireless charging pad with its coil exposed, a flip-cover case with a small magnet in its flap, and a speaker and a small cylinder-shaped vibration motor taken apart](scenes/smartphones/moving_charges_magnetism.svg "The phone on the cable can do more than point north: its magnetometer chip reports the size of the field, in microtesla.")

Mrs Iyer's physics class has discovered that a free sensor app turns their phones into magnetometers: it shows the field at the phone in microtesla, updating many times a second. Lying still on the bench, every phone reads a few tens of microtesla — the Earth's field.

Mrs Iyer stretches a long, straight wire across the lab, with the return wire taken far away round the walls, and connects a supply that holds a steady $2.0\,\text{A}$. Then she writes a challenge on the board: *predict the extra reading at 1 cm from the wire, and at 10 cm, before we switch on.*

Harsh groans. Last week they did the Biot–Savart law — add up the field of every little piece of wire. For a wire several metres long, that is a lot of little pieces.

"There's a shortcut," Mrs Iyer says, "if you know where to walk." What shortcut could possibly replace adding up the whole wire?

## The physics

**Ampere's circuital law** gives a shortcut for situations with enough symmetry. Walk around any closed loop, and at each small step $d\vec{l}$ multiply the length of the step by the component of $\vec{B}$ along it. Add the whole way round. The law says:

$$\oint \vec{B}\cdot d\vec{l} = \mu_0 I_\text{enc}$$

where $I_\text{enc}$ is the **net** current passing through the loop and $\mu_0 = 4\pi\times10^{-7}\,\text{T m/A}$. Currents in one direction count as positive (the direction your right thumb points when your fingers curl along the loop), and currents the other way count as negative. Currents outside the loop add nothing to the total, though they may still affect $B$ at individual points.

The imaginary loop is called an **Amperian loop**. The law holds for any loop, but it is only *useful* when you can choose a loop along which $B$ is constant and parallel to $d\vec{l}$.

**The long straight wire.** By symmetry, the field is the same all the way round a circle centred on the wire, and — from Oersted's experiment — points along the circle. So pick a circle of radius $r$ as the Amperian loop. $\vec{B}$ is parallel to $d\vec{l}$ everywhere, so $\oint \vec{B}\cdot d\vec{l} = B \times 2\pi r$. Then:

$$B(2\pi r) = \mu_0 I \qquad\Longrightarrow\qquad B = \frac{\mu_0 I}{2\pi r}$$

![A circular Amperian loop around a wire carrying current out of the page, with B the same size all round and tangent to the circle; and a second loop enclosing no current](figures/amperes_circuital_law/amperian-loop-long-wire.svg "Choose the loop to match the symmetry: around a straight wire, a circle on which B is the same size everywhere and always along the loop.")

This is valid for a long, straight wire with a steady current, at distances small compared with its length.

![Engraved portrait of a man in early nineteenth-century dress](famous/andre-marie-ampere-1825.jpg "André-Marie Ampère (1775–1836), engraved in 1825. Within weeks of hearing of Ørsted's discovery he began the work that gave us this law. Public domain, via Wikimedia Commons.")

## Worked example

**Given:** $I = 2.0\,\text{A}$ in the long straight wire; the phone's chip at $r = 1.0\,\text{cm} = 0.010\,\text{m}$, then at $r = 10\,\text{cm} = 0.10\,\text{m}$.
**Find:** the wire's field at each distance.

**Step 1 — at 1 cm.**

$$B = \frac{\mu_0 I}{2\pi r} = \frac{(4\pi\times10^{-7})(2.0)}{2\pi(0.010)} = 4.0\times10^{-5}\,\text{T} = 40\,\mu\text{T}$$

That is about as strong as the Earth's field. At a fingertip's distance, a modest current rivals the whole planet.

**Step 2 — at 10 cm.** $B \propto 1/r$, so ten times further away gives one-tenth: $4.0\,\mu\text{T}$ — a small but clear bump on the app.

**Sanity check:** the phone reads the *sum* of the Earth's field and the wire's, so the reading won't simply jump by $40\,\mu\text{T}$; it changes by that amount only if the two fields happen to line up. Turning the phone or the wire changes what you see.

## Where the picture breaks

The magnetometer chip is not a point: it sits a few millimetres inside the phone, so "1 cm from the wire" really means "1 cm from the chip", and at such short distances a small error matters.

The formula needs a **long** straight wire with the return path far away. Most real cables carry the current out and back side by side; around the whole cable the net current is zero, and the field outside is much weaker than either wire alone would give.

And Ampere's law, as written here, is for **steady** currents. When currents or fields change quickly, it needs an extra term — something you will meet with electromagnetic waves.

## Key takeaway

**Ampere's circuital law**: $\oint \vec{B}\cdot d\vec{l} = \mu_0 I_\text{enc}$ — the sum of $\vec{B}$ along any closed loop equals $\mu_0$ times the net current through it. With a loop that matches the symmetry, it gives the field of a long straight wire in one line: $B = \dfrac{\mu_0 I}{2\pi r}$, falling off as $1/r$.
