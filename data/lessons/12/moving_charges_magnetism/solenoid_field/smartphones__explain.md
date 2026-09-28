---
concept_id: solenoid_field
interest: smartphones
format: explain
title: The coil inside a phone-controlled door lock
check:
  question: |-
    A long solenoid for a phone-controlled lock carries a steady current and has a field $B$ inside it. Without changing the number of turns or the current, the coil is **stretched to twice its length**, with its turns spread out evenly. What is the field inside now, well away from the ends?
  options:
    A: |-
      $B$, unchanged, because the number of turns and the current are the same
    B: |-
      $2B$
    C: |-
      $B/2$
    D: |-
      $B/4$
  answer: C
  explanation: |-
    Inside a long solenoid $B = \mu_0 n I$, where $n$ is the number of turns **per unit length**. The same turns over twice the length give half the turns per metre, so $n$ halves and so does $B$.
  misconceptions:
    A: |-
      Thinks the field depends on the total number of turns. It depends on how closely they are packed — turns per metre, $n = N/L$ — so spreading the same turns out weakens the field.
    B: |-
      Thinks a longer coil must make a bigger field. Length alone does not add strength: at a point inside, what matters is how many turns carry current past each metre of the coil.
    D: |-
      Uses an inverse-square idea, as if the field fell with the square of the length. $B = \mu_0 N I / L$ is inversely proportional to $L$, not to $L^{2}$.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A desk with a phone lying on a charging cable showing a swung compass arrow, a wireless charging pad with its coil exposed, a flip-cover case with a small magnet in its flap, and a speaker and a small cylinder-shaped vibration motor taken apart](scenes/smartphones/moving_charges_magnetism.svg "Each gadget here turns a current into a magnetic field. A lock does the same thing, with a long coil instead of a flat one.")

Aditi has built her first real gadget: a lock for her bedroom door that opens from an app on her phone. A tiny board receives the command from her phone over a short-range radio link and switches a current through a small **solenoid** — a long, tight coil of wire wrapped round a hollow plastic tube, with a steel bolt sitting inside.

Tap the app, and the bolt snaps back into the coil with a sharp click. Release, and a spring pushes it out again.

Her cousin Kunal inspects it. "Your coil is tiny. Wind a coil twice as long with twice as many turns and it'll be twice as strong."

Aditi isn't sure. Twice the turns sounds like twice the field — but each of those extra turns sits further along the tube, away from the middle. Does length help, or not? What actually sets the field inside a coil like this?

## The physics

A **solenoid** is a long wire wound in a tight helix, so that it forms many circular loops side by side. Each loop makes a field like the one in the last lesson; stacked together, their fields add up along the axis.

![A long solenoid in cross-section, with current out of the page along the top turns and into the page along the bottom, a uniform field inside, almost none outside, and a rectangular Amperian loop with one side inside and one outside](figures/solenoid_field/solenoid-field-and-amperian-rectangle.svg "Inside, the loops' fields add to a strong, uniform field along the axis. Outside, they almost cancel. The rectangle is the Amperian loop that turns this picture into a formula.")

For a **long** solenoid, the field inside is uniform and parallel to the axis, and the field outside is nearly zero. With those facts, Ampere's law gives the field quickly.

Take the rectangular Amperian loop in the figure, with one long side of length $h$ inside the solenoid and the opposite side outside:

- **Inside side:** $\vec{B}$ is along the path, so it contributes $Bh$.
- **Outside side:** $B \approx 0$, so it contributes nothing.
- **The two short ends:** inside, $\vec{B}$ is at right angles to them; outside, $B \approx 0$. Nothing from either.

So $\oint \vec{B}\cdot d\vec{l} = Bh$. If the solenoid has $n$ turns **per unit length**, the loop encloses $nh$ turns, each carrying $I$, so $I_\text{enc} = nhI$. Ampere's law gives $Bh = \mu_0 nhI$, and $h$ cancels:

$$B = \mu_0 n I$$

This depends on the **turns per metre** and the current, not on the radius or the total length — as long as the solenoid is long compared with its width. The direction follows the right-hand rule for loops: curl your fingers with the current, and your thumb points along $\vec{B}$ inside.

## Worked example

**Given:** a coil with $1000$ turns wound evenly along $10\,\text{cm}$, carrying $I = 0.50\,\text{A}$ (illustrative values; an empty tube, no iron inside).
**Find:** the field inside, and what Kunal's longer coil would give.

**Step 1 — turns per metre.**

$$n = \frac{N}{L} = \frac{1000}{0.10\,\text{m}} = 1.0\times10^{4}\ \text{turns/m}$$

**Step 2 — the field.**

$$B = \mu_0 n I = (4\pi\times10^{-7})(1.0\times10^{4})(0.50) = 2\pi\times10^{-3}\,\text{T} \approx 6.3\,\text{mT}$$

That is over a hundred times the Earth's field, uniform through the middle of a tube you could hold in one hand.

**Step 3 — Kunal's coil.** Twice as many turns ($2000$) over twice the length ($20\,\text{cm}$) is still $1.0\times10^{4}$ turns per metre. The field inside is the **same**, $6.3\,\text{mT}$ — a longer uniform region, not a stronger one.

**Sanity check:** if Aditi wants a stronger field, she has to pack the turns tighter or raise the current, both of which raise $\mu_0 n I$ directly.

## Where the picture breaks

A lock's solenoid is short and fat, not "long". The formula is then only a rough guide: the field weakens near the ends (to about half the middle value right at an end of a long coil) and leaks outside.

The steel bolt matters enormously, too. Iron-like materials inside a coil can make the field hundreds of times stronger than $\mu_0 n I$ — you will meet that in *Magnetism and Matter*. Our number is for an empty tube.

And the bolt is pulled in because a magnetised piece of steel is drawn towards the stronger field inside the coil. The formula tells you how strong that field is, not directly how hard the bolt is pulled.

## Key takeaway

Inside a long solenoid, the magnetic field is uniform, along the axis, and equal to $B = \mu_0 n I$, where $n$ is the number of turns **per unit length**. Outside it is nearly zero. Ampere's law with a rectangular loop gives this in a few lines. More turns per metre or more current make it stronger; a longer coil with the same packing does not.
