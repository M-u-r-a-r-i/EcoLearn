---
concept_id: electric_field
interest: football
format: explain
title: The meter that stopped the match on a clear evening
check:
  question: |-
    A test charge of $+2.0\,\text{nC}$ is placed at a point and feels a force of $1.0\,\mu\text{N}$ towards the east. It is then removed and a $+4.0\,\text{nC}$ charge is put at the same point instead. What is the electric field at that point?
  options:
    A: |-
      $500\,\text{N/C}$ east — the same as before.
    B: |-
      $1000\,\text{N/C}$ east — twice as big, because the charge is twice as big.
    C: |-
      $250\,\text{N/C}$ east — half as big, because the charge is twice as big.
    D: |-
      $500\,\text{N/C}$ west.
  answer: A
  explanation: |-
    $E = F/q$ is force **per unit charge**: $1.0 \times 10^{-6}/2.0 \times 10^{-9} = 500\,\text{N/C}$. Doubling the test charge doubles the force too, so the ratio — and the field — is unchanged.
  misconceptions:
    B: |-
      Thinks the field belongs to the charge you place there. The bigger charge does feel twice the force, but the field is force *per unit charge*, so it stays the same.
    C: |-
      Inverts the definition, dividing the original field by the new charge instead of dividing the new force by it.
    D: |-
      Reverses the direction convention. The field points the way a *positive* test charge is pushed, so field and force share a direction here.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A floodlit ground as a storm arrives: lightning above the stand, rain falling, a player peeling off a crackling nylon bib, and two players heading for the metal-roofed dugout](scenes/football/electric_charges_fields.svg "The storm is still kilometres away. Something at ground level already knows it is coming.")

Nikita is the safety officer at the district ground, and the box she watches on match days does only one thing: it measures the strength of the electric field in the air just above the pitch, and sounds when that strength crosses a set value.

Twelve minutes into the second half, on an evening with no rain and only a grey smudge of cloud over the hills, it sounds. Nikita signals the referee. Players walk off to a chorus of complaints from the stand.

Four minutes later the first flash comes down over the hills.

Tara, the captain, corners her afterwards. "There was nothing overhead. The box isn't connected to anything up there. What exactly did it feel?"

Nikita taps the display, which still shows a number. Not a force — nothing was being pushed. A number with units of newtons per coulomb, measured in air that was, as far as anyone could see, empty. What is the thing that meter was reading?

## The physics

A charge does not have to touch anything to push another charge. The modern way to say this is that a charge changes the **space around it**, and any other charge simply responds to the space it sits in. That change is the **electric field**.

Put a small positive **test charge** $q_0$ at a point and measure the force $\vec{F}$ on it. The electric field at that point is

$$\vec{E} = \frac{\vec{F}}{q_0}$$

- **Units:** newtons per coulomb, $\text{N/C}$.
- **A vector:** its direction is the direction of the force on a *positive* test charge. A negative charge placed there is pushed the opposite way.
- **Independent of the test charge:** double $q_0$ and the force doubles, so the ratio does not change. The field was already there; the test charge only reveals it. (It must be *small*, or its own field would shift the charges you were trying to study.)

Turn the definition round and you get the rule you will use most: a charge $q$ in a field $\vec{E}$ feels

$$\vec{F} = q\vec{E}$$

For a single **point charge** $Q$, Coulomb's law gives the field at distance $r$:

$$E = \frac{1}{4\pi\varepsilon_0}\frac{|Q|}{r^2}$$

pointing **away** from $Q$ if $Q$ is positive and **towards** it if negative.

![Field vectors around a positive charge point outwards and around a negative charge point inwards; at twice the distance they are a quarter as long](figures/electric_field/field-vectors-point-charges.svg "The field has a direction at every point: away from +Q, towards −Q. At twice the distance it is a quarter as strong.")

Because several charges' forces add as vectors, so do their fields: $\vec{E}_\text{net} = \vec{E}_1 + \vec{E}_2 + \dots$ at every point.

## Worked example

**Given (illustrative):** a small charged object carrying $Q = +5.0\,\text{nC}$, with $k = 9.0 \times 10^9\,\text{N m}^2\,\text{C}^{-2}$.
**Find:** the field $0.30\,\text{m}$ away, and the force on a $+2.0\,\text{nC}$ charge placed there.

**Step 1 — the field.** $Q = 5.0 \times 10^{-9}\,\text{C}$ and $r^2 = 0.090\,\text{m}^2$:

$$E = \frac{9.0 \times 10^9 \times 5.0 \times 10^{-9}}{0.090} = \frac{45}{0.090} = 500\,\text{N/C}$$

directed away from $Q$, because $Q$ is positive. Note that no second charge appears anywhere in that calculation — the field is there whether or not anything is present to feel it.

![A graph of field strength against distance for a 5.0 nC charge, falling steeply: 500 N/C at 0.30 m and 125 N/C at 0.60 m](figures/electric_field/point-charge-e-vs-r.svg "The inverse-square fall-off: double the distance, a quarter of the field.")

**Step 2 — the force on a charge placed there.**

$$F = qE = (2.0 \times 10^{-9})(500) = 1.0 \times 10^{-6}\,\text{N}$$

a micronewton, pushed directly away from $Q$ — about the weight of a tenth of a milligram, far too small to see without a thread and a lot of patience.

**Sanity check:** moving out to $0.60\,\text{m}$ doubles $r$, so $E$ should fall to a quarter: $125\,\text{N/C}$, which is where the graph sits. Units check too — $\text{N/C}$ times $\text{C}$ gives $\text{N}$.

## Where the picture breaks

The field meter's reading is not the field of one neat point charge: the storm cloud is an enormous, shifting distribution of charge kilometres up, and the ground below it carries an induced charge of its own. "Empty air" also isn't empty — it is full of molecules, and above roughly $3 \times 10^6\,\text{N/C}$ it stops insulating altogether and a spark jumps. The field idea itself is exact and does the real work here; it is the tidy single-charge formula that does not apply to a storm.

## Key takeaway

The electric field is the force per unit positive test charge, $\vec{E} = \vec{F}/q_0$, measured in $\text{N/C}$ — a property of the space itself, the same whatever you put there to test it. A point charge makes a field $E = \dfrac{1}{4\pi\varepsilon_0}\dfrac{|Q|}{r^2}$, pointing away from a positive charge, and any charge sitting in a field feels $\vec{F} = q\vec{E}$.
