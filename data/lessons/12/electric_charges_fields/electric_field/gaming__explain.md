---
concept_id: electric_field
interest: gaming
format: explain
title: The probe that kept changing the answer
check:
  question: |-
    In Yash's sandbox, a test charge of $+3.0\,\text{nC}$ placed at a point feels an electric force of $1.2 \times 10^{-4}\,\text{N}$ to the right. He deletes it and drops a $-6.0\,\text{nC}$ charge at exactly the same point. What is the electric field at that point now?
  options:
    A: |-
      $8.0 \times 10^{4}\,\text{N/C}$ to the right
    B: |-
      $4.0 \times 10^{4}\,\text{N/C}$ to the right
    C: |-
      $4.0 \times 10^{4}\,\text{N/C}$ to the left
    D: |-
      $2.0 \times 10^{4}\,\text{N/C}$ to the left
  answer: B
  explanation: |-
    $E = F/q_0 = 1.2 \times 10^{-4} / 3.0 \times 10^{-9} = 4.0 \times 10^{4}\,\text{N/C}$ to the right. The field is made by the source charges, so swapping the test charge changes the force on it but leaves the field exactly as it was.
  misconceptions:
    A: |-
      Thinks the field scales with the test charge, doubling when the probe is doubled. A bigger probe feels a bigger force, but $F/q_0$ is unchanged.
    C: |-
      Thinks the field reverses when a negative charge is placed there. It is the *force* on that charge that points left; the field still points right.
    D: |-
      Divides the old force by the new charge, mixing two different situations, and then flips the direction because the new charge is negative.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A gaming desk at night during a PC build: a monitor running a field sandbox with two charges, a plasma globe, an antistatic bag sparking to a fingertip, and an open PC case with a graphics card going in](scenes/gaming/electric_charges_fields.svg "The sandbox on the screen draws an arrow at every point of empty space. What is the arrow a picture of?")

Yash spent his holidays building a tool nobody asked for: a physics sandbox where you drop charges on a grid and the screen fills with little arrows showing which way things get pushed.

He posts it to his club's channel and gets one reply within the hour. *Your field is broken. Pick the 1 nC probe and the arrows are tiny. Pick the 10 nC probe and they're ten times bigger. The charges on the grid didn't change, so which reading is the real one?*

Yash checks. The reply is right: every arrow he draws is the force on whatever probe is selected, and a bigger probe gets shoved harder. He can feel there is something wrong with the question all the same. Nothing about the grid changed when he swapped probes — only what he poked it with.

So is there a way to describe what the space around a charge is *doing*, without dragging the probe's own size into the answer?

## The physics

A charge does not reach across space and grab another charge. It fills the space around itself with an **electric field**, and any charge placed in that space feels a force from the field **at its own location**.

**Definition.** The electric field $\vec{E}$ at a point is the force per unit positive charge on a small test charge $q_0$ placed there:

$$\vec{E} = \frac{\vec{F}}{q_0}$$

Its SI unit is the newton per coulomb, $\text{N/C}$. Dividing by $q_0$ is precisely the fix Yash needs: the probe's charge cancels out, and what is left belongs to the grid alone.

The test charge must also be **small**, so that it does not shove the source charges around and change the very field it is measuring. Strictly, $\vec{E}$ is the limit of $\vec{F}/q_0$ as $q_0 \to 0$.

The key idea, worth saying twice: **$\vec{E}$ depends on the source charges and on the position, not on the test charge.** Double $q_0$ and the force doubles, but the ratio $\vec{F}/q_0$ does not budge.

**Field of a point charge.** Feeding Coulomb's law into the definition, the field at a distance $r$ from a point charge $Q$ is

$$\vec{E} = \frac{1}{4\pi\varepsilon_0}\,\frac{Q}{r^2}\,\hat{r}$$

with $\hat{r}$ pointing away from $Q$. For positive $Q$ the field points **away** from the charge; for negative $Q$, **towards** it. Its size falls as $1/r^2$.

![Field arrows around a positive charge pointing outwards and around a negative charge pointing inwards, with the arrows at twice the distance drawn a quarter as long](figures/electric_field/field-vectors-point-charges.svg "The field has a direction at every point: away from +Q, towards −Q. At twice the distance the arrow is a quarter as long.")

**Using the field.** Once you know $\vec{E}$ at a point, the force on *any* charge $q$ put there is

$$\vec{F} = q\vec{E}$$

A positive charge is pushed along $\vec{E}$, a negative one the opposite way. That is what Yash should draw: one set of arrows for the field, and the force on the probe worked out from them.

## Worked example

**Given (illustrative):** a small sphere carrying $Q = +5.0\,\text{nC}$.
**Find:** the field at $r = 0.30\,\text{m}$, the force on an electron placed there, and the field at $0.60\,\text{m}$.

**Step 1 — the field.** With $Q = 5.0 \times 10^{-9}\,\text{C}$:

$$E = \frac{9.0 \times 10^9 \times 5.0 \times 10^{-9}}{(0.30)^2} = \frac{45}{0.090} = 5.0 \times 10^{2}\,\text{N/C}$$

pointing away from the sphere. A few hundred newtons per coulomb is an ordinary static-electricity field — far below the roughly $3 \times 10^6\,\text{N/C}$ it takes to make air spark.

**Step 2 — the force on an electron there.** Using $F = |q|E$ with $e = 1.6 \times 10^{-19}\,\text{C}$:

$$F = 1.6 \times 10^{-19} \times 500 = 8.0 \times 10^{-17}\,\text{N}$$

The electron is negative, so this force points **towards** the sphere, against $\vec{E}$.

**Step 3 — twice as far away.** Doubling $r$ divides $E$ by $4$:

$$E = \frac{500}{4} = 125\,\text{N/C}$$

![A graph of field strength against distance for a 5.0 nC point charge, falling steeply from the axis, marked 500 N/C at 0.30 m and 125 N/C at 0.60 m](figures/electric_field/point-charge-e-vs-r.svg "The inverse-square fall-off: double the distance and only a quarter of the field is left.")

**Sanity check:** working it out directly, $45/(0.60)^2 = 45/0.36 = 125\,\text{N/C}$, so the shortcut and the formula agree.

## Where the picture breaks

An arrow grid is a picture, not the thing itself: the field is defined at *every* point, not only where the tool happens to draw an arrow, and an arrow's length on screen is whatever scale the programmer chose.

The definition also hides a quiet idealisation. A real probe always has some size and some charge, so it always disturbs the sources a little; $\vec{E} = \vec{F}/q_0$ is exact only in the limit of a vanishingly small probe. And everything here is for charges at rest — fields that change with time behave very differently, and that is a later chapter.

## Key takeaway

The electric field at a point is the force per unit positive test charge, $\vec{E} = \vec{F}/q_0$, measured in $\text{N/C}$. It belongs to the source charges, not to whatever you probe it with. A point charge's field is $E = \dfrac{1}{4\pi\varepsilon_0}\dfrac{Q}{r^2}$, pointing away from a positive charge and towards a negative one, and any charge $q$ placed there feels $\vec{F} = q\vec{E}$.
