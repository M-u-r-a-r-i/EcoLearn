---
concept_id: electric_dipole
interest: gaming
format: explain
title: The lopsided molecule that ends the static season
check:
  question: |-
    Far from a small electric dipole, the field at a point on its axis, a distance $r$ from the centre, is $60\,\text{N/C}$. What is the field at a point on the equatorial line, at the same distance $r$?
  options:
    A: |-
      $120\,\text{N/C}$, in the same direction as the axial field
    B: |-
      $60\,\text{N/C}$, opposite in direction to the axial field
    C: |-
      $30\,\text{N/C}$, opposite in direction to the axial field
    D: |-
      $0\,\text{N/C}$, because both charges are the same distance away there
  answer: C
  explanation: |-
    Far from a dipole, $E_\text{axis} \approx 2kp/r^3$ and $E_\text{equatorial} \approx kp/r^3$, so the equatorial field is half the axial one — and it points opposite to $\vec{p}$, while the axial field points along it.
  misconceptions:
    A: |-
      Inverts the factor of two. It is the axial field that is twice the equatorial, not the other way round, and the two point in opposite senses relative to $\vec{p}$.
    B: |-
      Treats the dipole like a point charge, whose field has the same magnitude in every direction at a given distance. A dipole's field depends on direction as well as distance.
    D: |-
      Thinks equal distances mean the two fields cancel. Their components across the axis do cancel, but their components along it add, leaving a field opposite to $\vec{p}$.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A gaming desk at night during a PC build: a monitor running a field sandbox with two charges, a plasma globe, an antistatic bag sparking to a fingertip, and an open PC case with a graphics card going in](scenes/gaming/electric_charges_fields.svg "The spark in this picture is a winter problem. It disappears when the air turns damp.")

January in the practice room is the worst month of Simran's year. Every time she stands up and puts a hand on the metal frame of her rig, she gets a spiteful little shock. Twice she has flinched hard enough to unplug a headset mid-match.

Her team's coach, unbothered, brings in a small humidifier and sets it running in the corner. Within a day the shocks are gone. Nobody has changed a cable, a chair or a carpet — only the amount of water floating in the air.

Simran corners the chemistry teacher about it at lunch. "Water molecules are neutral," he says, "but they're lopsided. The oxygen end sits slightly negative, the hydrogen end slightly positive. That lopsidedness is why water sticks to everything."

She is not satisfied. If a molecule has zero total charge, how can it produce any electric field at all? And if it does, how strong is it, and how fast does it fade with distance?

## The physics

A pair of equal and opposite charges, $+q$ and $-q$, held a distance $2a$ apart, is an **electric dipole**. Its total charge is zero, but the two charges sit in *different places*, so their fields do not cancel except at infinity.

The **dipole moment** is a vector:

$$\vec{p} = q(2a)\,\hat{p}$$

of magnitude $p = q(2a)$, pointing **from $-q$ to $+q$** along the axis. Its unit is the coulomb metre, $\text{C m}$. A water molecule carries a permanent dipole moment of about $6.2 \times 10^{-30}\,\text{C m}$; molecules like this are called **polar**.

![A dipole with minus q on the left and plus q on the right, with a point P on the axis where the net field points along p, and a point Q on the equatorial line where it points opposite to p](figures/electric_dipole/dipole-axial-equatorial.svg "On the axis the nearer charge wins, so E points along p. On the equatorial line the sideways parts cancel and E points opposite to p.")

**On the axis**, at distance $r$ from the centre on the $+q$ side, the near charge is $(r-a)$ away and the far one $(r+a)$:

$$E = \frac{q}{4\pi\varepsilon_0}\left[\frac{1}{(r-a)^2} - \frac{1}{(r+a)^2}\right] = \frac{1}{4\pi\varepsilon_0}\,\frac{2pr}{(r^2 - a^2)^2}$$

pointing **along $\vec{p}$**. When $r \gg a$ this simplifies to $E \approx \dfrac{2p}{4\pi\varepsilon_0 r^3}$.

**On the equatorial line** (the perpendicular bisector), both charges are $\sqrt{r^2 + a^2}$ away, so their fields are equal in size. The components across the axis cancel; the components along it add, both pointing from $+q$ towards $-q$:

$$E = \frac{1}{4\pi\varepsilon_0}\,\frac{p}{(r^2 + a^2)^{3/2}}$$

pointing **opposite to $\vec{p}$**, and for $r \gg a$, $E \approx \dfrac{p}{4\pi\varepsilon_0 r^3}$.

Two facts to carry away. Far from a dipole the field falls as $1/r^3$ — faster than a point charge's $1/r^2$, because the two opposite fields almost cancel. And at the same large distance, the axial field is exactly **twice** the equatorial field.

## Worked example

**Given (illustrative):** a model dipole with charges $\pm 1.0\,\text{nC}$ held $2.0\,\text{cm}$ apart, so $2a = 0.020\,\text{m}$ and $a = 0.010\,\text{m}$.
**Find:** its dipole moment, and its field at $r = 0.20\,\text{m}$ on the axis and on the equatorial line.

**Step 1 — the dipole moment.**

$$p = q(2a) = 1.0 \times 10^{-9} \times 0.020 = 2.0 \times 10^{-11}\,\text{C m}$$

**Step 2 — the axial field.** Here $r = 0.20\,\text{m}$ is twenty times $a$, so $r \gg a$ and the far-field formula is safe:

$$E_\text{axis} = \frac{2kp}{r^3} = \frac{2 \times 9.0 \times 10^9 \times 2.0 \times 10^{-11}}{(0.20)^3} = \frac{0.36}{0.0080} = 45\,\text{N/C}$$

along $\vec{p}$.

**Step 3 — the equatorial field.** Half of that, and pointing the other way:

$$E_\text{eq} = 22.5\,\text{N/C}$$

**Sanity check:** one $1.0\,\text{nC}$ charge on its own would give $225\,\text{N/C}$ at this distance. The dipole manages a fifth of that, because its partner charge nearly cancels it — which is exactly what "the field falls off faster" should mean.

## Where the picture breaks

A water molecule is not two point charges on a stick. Its charge is smeared through electron clouds, and between neighbouring molecules the distances are comparable to the molecule's own size, so $r \gg a$ fails badly and these formulas do not give the forces that make water cling.

The humidifier story has a further twist. Damp air helps mainly because a thin film of water forms on surfaces and lets charge leak away quietly instead of building up for a spark — which is about conduction, not about the field of a single dipole. What the dipole explains is the honest part of the chemistry teacher's answer: a neutral molecule can still have a field, and it can still be pulled and turned by one.

## Key takeaway

An electric dipole is $+q$ and $-q$ separated by $2a$, with dipole moment $p = q(2a)$ pointing from $-q$ to $+q$. On the axis, $E = \dfrac{1}{4\pi\varepsilon_0}\dfrac{2pr}{(r^2-a^2)^2}$ along $\vec{p}$; on the equatorial line, $E = \dfrac{1}{4\pi\varepsilon_0}\dfrac{p}{(r^2+a^2)^{3/2}}$ opposite to $\vec{p}$. Far away both fall as $1/r^3$, and the axial field is twice the equatorial one.
