---
concept_id: electric_field
interest: cricket
format: explain
title: How the ground knows a storm is coming
check:
  question: |-
    A small test charge of $+2.0\,\text{nC}$ placed at a point near the pavilion feels an electric force of $6.0 \times 10^{-5}\,\text{N}$ towards the east. It is replaced by a charge of $-4.0\,\text{nC}$ at the same point. What is the electric field at that point now?
  options:
    A: |-
      $3.0 \times 10^{4}\,\text{N/C}$ towards the east
    B: |-
      $1.5 \times 10^{4}\,\text{N/C}$ towards the west
    C: |-
      $3.0 \times 10^{4}\,\text{N/C}$ towards the west
    D: |-
      $6.0 \times 10^{4}\,\text{N/C}$ towards the east
  answer: A
  explanation: |-
    $E = F/q_0 = 6.0 \times 10^{-5} / 2.0 \times 10^{-9} = 3.0 \times 10^{4}\,\text{N/C}$ east. The field is set up by the source charges, not the test charge, so swapping the test charge changes the force on it, but not the field.
  misconceptions:
    B: |-
      Thinks the field depends on the test charge, recalculating it with the new charge and flipping it with the sign, as if $E$ belonged to the charge placed there.
    C: |-
      Thinks the field reverses when a negative charge is placed there. It is the force on the negative charge that points west; the field still points east.
    D: |-
      Thinks the field doubles because the new charge is twice as large; a bigger test charge feels a bigger force, but $F/q$ stays the same.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A storm over a cricket ground: dark clouds, distant lightning, players walking off, groundstaff dragging a plastic cover and a team bus waiting](scenes/cricket/electric_charges_fields.svg "The sky looks threatening, but the umpires need more than a feeling to stop play.")

The sky over the ground has turned the colour of a bruise, but it isn't raining yet. Karthik, crouched behind the stumps, is itching to bowl out the last two overs before the weather arrives.

Then the umpires confer, and one walks towards the pavilion. The ground manager is on the boundary, holding up a tablet. Some venues keep a lightning warning monitor, a sensor box near the ground that measures the electric field in the air, and this one's readings are climbing fast. Players off.

"There's been no lightning yet!" Karthik protests.

"Not yet," says the manager. "But the cloud's charge is already reaching us."

Karthik looks up. The cloud base is maybe a kilometre above him. Nothing connects the cloud to the little box on the ground. So what, exactly, is the box measuring, and how can a charge a kilometre away make itself felt down here?

## The physics

A charge doesn't reach out and grab other charges directly. It sets up an **electric field** in the space around it, and any other charge placed in that space feels a force from the field *at its own location*. The storm cloud's charge has already created a field at ground level, and that is what the monitor detects.

**Definition.** The electric field $\vec{E}$ at a point is the force per unit positive charge on a small test charge $q_0$ placed there:

$$\vec{E} = \frac{\vec{F}}{q_0}$$

Its SI unit is the newton per coulomb, $\text{N/C}$. The test charge must be small, so that it doesn't push the source charges around and change the very field being measured. Strictly, $\vec{E}$ is the limit of $\vec{F}/q_0$ as $q_0 \to 0$.

The key idea: **$\vec{E}$ depends on the source charges and on the position, not on the test charge.** Double $q_0$ and the force doubles, but $\vec{F}/q_0$ is unchanged.

**Field of a point charge.** Putting Coulomb's law into the definition, the field at distance $r$ from a point charge $Q$ is

$$\vec{E} = \frac{1}{4\pi\varepsilon_0}\,\frac{Q}{r^2}\,\hat{r}$$

where $\hat{r}$ points away from $Q$. For positive $Q$ the field points **away** from the charge; for negative $Q$ it points **towards** it. Its size falls as $1/r^2$.

![Field vectors around a positive charge point outwards and around a negative charge point inwards; at twice the distance they are a quarter as long](figures/electric_field/field-vectors-point-charges.svg "The field has a direction at every point: away from +Q, towards −Q. At twice the distance it is a quarter as strong.")

**Using the field.** Once you know $\vec{E}$ at a point, the force on *any* charge $q$ placed there is

$$\vec{F} = q\vec{E}$$

A positive charge is pushed along $\vec{E}$; a negative charge is pushed the opposite way.

Even on a fine day there's a weak field of roughly $100\,\text{N/C}$ near the ground, pointing downwards. Under a thundercloud it can grow to several thousand $\text{N/C}$, and a rapidly rising field is the warning sign the monitor looks for.

## Worked example

**Given:** a small sphere carrying $Q = +5.0\,\text{nC}$ (illustrative).
**Find:** (a) the field at $r = 0.30\,\text{m}$; (b) the force on an electron placed there; (c) the field at $0.60\,\text{m}$.

(a) $Q = 5.0 \times 10^{-9}\,\text{C}$:

$$E = \frac{9.0 \times 10^9 \times 5.0 \times 10^{-9}}{(0.30)^2} = \frac{45}{0.090} = 5.0 \times 10^{2}\,\text{N/C}$$

pointing away from the sphere.

(b) $F = |q|E = 1.6 \times 10^{-19} \times 500 = 8.0 \times 10^{-17}\,\text{N}$. The electron is negative, so the force points **towards** the sphere, opposite to $\vec{E}$.

(c) Doubling $r$ divides $E$ by 4: $E = 500/4 = 125\,\text{N/C}$. Check directly: $45/(0.60)^2 = 45/0.36 = 125\,\text{N/C}$.

![A graph of field strength against distance for a 5.0 nC charge, falling steeply: 500 N/C at 0.30 m and 125 N/C at 0.60 m](figures/electric_field/point-charge-e-vs-r.svg "The inverse-square fall-off: double the distance, a quarter of the field.")

**Sanity check:** $E$ has units $\text{N m}^2\,\text{C}^{-2} \times \text{C} / \text{m}^2 = \text{N/C}$. Correct.

## Where the picture breaks

A storm cloud is not a point charge. It holds large regions of positive and negative charge at different heights, and the ground below responds by building up induced charge of its own. So $kQ/r^2$ won't give you the field under a real cloud; you'd need to add the contributions of all its charges. And a monitor reports how the field changes over time, whereas this chapter treats charges at rest. The story shows why a field is real and measurable; the formula is for point charges.

## Key takeaway

The electric field at a point is the force per unit positive test charge, $\vec{E} = \vec{F}/q_0$, measured in N/C. It belongs to the source charges, not the test charge. A point charge's field is $E = \dfrac{1}{4\pi\varepsilon_0}\dfrac{Q}{r^2}$, pointing away from a positive charge and towards a negative one, and any charge $q$ there feels $\vec{F} = q\vec{E}$.
