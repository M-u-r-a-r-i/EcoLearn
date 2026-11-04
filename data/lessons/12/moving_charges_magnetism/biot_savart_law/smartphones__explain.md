---
concept_id: biot_savart_law
interest: smartphones
format: explain
title: Why phone designers keep wires away from the compass chip
check:
  question: |-
    A short piece of copper track on a phone's circuit board carries a steady current. At a point P, this current element produces a field $dB = 4.0\,\mu\text{T}$. Point Q lies in the **same direction** from the element (same angle $\theta$), but **twice as far** away. What field does the same element produce at Q?
  options:
    A: |-
      $2.0\,\mu\text{T}$
    B: |-
      $16\,\mu\text{T}$
    C: |-
      $1.0\,\mu\text{T}$
    D: |-
      $0.50\,\mu\text{T}$
  answer: C
  explanation: |-
    By the Biot–Savart law, $dB = \dfrac{\mu_0}{4\pi}\dfrac{I\,dl\sin\theta}{r^{2}}$. With the same $I$, $dl$ and $\theta$, doubling $r$ divides $dB$ by $2^2 = 4$: $4.0/4 = 1.0\,\mu\text{T}$.
  misconceptions:
    A: |-
      Uses a $1/r$ fall-off, as for the total field of a long straight wire. A single short current element's contribution falls off as $1/r^{2}$.
    B: |-
      Applies the factor of four the wrong way round, as if the field grew with distance. Moving further from the source always weakens its field.
    D: |-
      Uses a $1/r^{3}$ fall-off, as for a small magnet seen from far away. The Biot–Savart law for one current element has $r^{2}$ in the denominator.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A desk with a phone lying on a charging cable showing a swung compass arrow, a wireless charging pad with its coil exposed, a flip-cover case with a small magnet in its flap, and a speaker and a small cylinder-shaped vibration motor taken apart](scenes/smartphones/moving_charges_magnetism.svg "The phone on the cable shows a compass arrow knocked off course. Inside every phone, the designers have to stop the phone's own wiring from doing the same thing.")

Sneha has a summer internship at a company that designs circuit boards for phones. On her second day her mentor, Mr Pillai, opens a board layout on a big screen and points at a tiny square near one corner: the **magnetometer**, the chip behind the compass app.

"Rule one," he says. "No thick power tracks near this chip. Not under it, not beside it."

Sneha looks at the layout. The nearest track carrying battery current is already more than a centimetre away. "But it's just a flat strip of copper," she says. "It carries current for a few millimetres and then turns a corner. How can a bit of track that short, that far away, bother a chip?"

Mr Pillai grins and slides the track one centimetre closer on screen. "Then tell me how much worse that just made it."

To answer him, Sneha needs to know how much field each little piece of a current makes — and how it fades with distance.

## The physics

Oersted showed that currents make magnetic fields. The **Biot–Savart law** says exactly how much field each tiny piece of a current contributes.

Take a very short piece of wire, of length $dl$, carrying current $I$. This is a **current element**, $I\,d\vec{l}$, with $d\vec{l}$ pointing along the current. At a point P a distance $r$ away, it produces a small field

$$d\vec{B} = \frac{\mu_0}{4\pi}\,\frac{I\,d\vec{l}\times\hat{r}}{r^{2}}, \qquad dB = \frac{\mu_0}{4\pi}\,\frac{I\,dl\,\sin\theta}{r^{2}}$$

where $\hat{r}$ points from the element to P, $\theta$ is the angle between $d\vec{l}$ and $\vec{r}$, and $\dfrac{\mu_0}{4\pi} = 10^{-7}\,\text{T m/A}$.

![A short current element dl on a curved wire, the vector r to a point P, the angle theta between them, and the small field dB at P pointing into the page](figures/biot_savart_law/current-element-dB.svg "Each small piece of current contributes a small field at P, perpendicular to both dl and r. The whole wire's field is the sum of all these contributions.")

Read the law piece by piece:

- **$dB \propto I\,dl$** — more current, or a longer piece, gives more field.
- **$dB \propto 1/r^{2}$** — an inverse-square fall-off, like Coulomb's law for a point charge.
- **$dB \propto \sin\theta$** — the element makes **no** field at points along its own line ($\theta = 0$), and the most at right angles to it.
- **Direction:** $d\vec{B}$ is perpendicular to both $d\vec{l}$ and $\vec{r}$, following the right-hand rule for the cross product — the same circling direction as the grip rule.

The field of a whole track, loop or coil is the **vector sum** of the contributions of all its elements.

## Worked example

**Given:** one short piece of track, $dl = 1.0\,\text{mm} = 1.0\times10^{-3}\,\text{m}$, carrying $I = 1.0\,\text{A}$. The chip is $r = 1.0\,\text{cm} = 0.010\,\text{m}$ away, at right angles to the track ($\theta = 90^\circ$). Illustrative values.
**Find:** the field from this element at the chip, and what happens if the chip moves to $2.0\,\text{cm}$ away, or lies along the track's own line.

**Step 1 — the field at 1 cm.**

$$dB = 10^{-7}\times\frac{1.0\times(1.0\times10^{-3})\times1}{(0.010)^{2}} = 10^{-7}\times\frac{10^{-3}}{10^{-4}} = 1.0\times10^{-6}\,\text{T} = 1.0\,\mu\text{T}$$

The Earth's field is a few tens of microtesla, so one millimetre of track already adds a few per cent of it. A track is many millimetres long, and the contributions add.

**Step 2 — twice as far.** $r$ doubles, $r^{2}$ is four times bigger: $dB = 0.25\,\mu\text{T}$, a quarter.

**Step 3 — along the track's line.** $\theta = 0$, $\sin\theta = 0$: no field from this element there at all.

**Sanity check:** so sliding the track from $2\,\text{cm}$ to $1\,\text{cm}$ makes each element's field four times stronger — that is what Mr Pillai just did to the chip.

## Where the picture breaks

A real current cannot flow through an isolated millimetre of copper: it flows round a complete circuit, and only the sum over the whole circuit is ever measured. The Biot–Savart law gives the pieces; the answer is always their total.

A circuit also has a return path. On a phone board the battery current goes out along one track and comes back along another; placed close together, their fields largely cancel. That is the second trick designers use, after keeping distance.

And the law as written is for **steady** currents. A phone's currents change in pulses as the processor and radio switch on and off; for slow changes it still works well, but rapidly changing fields bring in effects you will meet later.

## Key takeaway

The **Biot–Savart law** says a current element $I\,d\vec{l}$ makes a field $dB = \dfrac{\mu_0}{4\pi}\dfrac{I\,dl\sin\theta}{r^{2}}$, perpendicular to both the element and the line to the point. It falls off as $1/r^{2}$ and is zero along the element's own line. The field of any real circuit is the sum of all these small contributions.
