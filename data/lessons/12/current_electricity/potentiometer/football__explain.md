---
concept_id: potentiometer
interest: football
format: explain
title: The beam balance in the kit room and the wire in the lab
check:
  question: |-
    In a potentiometer experiment a cell balances at $60\,\text{cm}$ on open circuit. With a $5\,\Omega$ resistor connected across it, the balance length falls to $50\,\text{cm}$. Its internal resistance is:
  options:
    A: |-
      $0.83\,\Omega$
    B: |-
      $6.0\,\Omega$
    C: |-
      $1.0\,\Omega$
    D: |-
      $0.50\,\Omega$
  answer: C
  explanation: |-
    Using $r = R\dfrac{l_1 - l_2}{l_2} = 5 \times \dfrac{60 - 50}{50} = 5 \times \dfrac{10}{50} = 1.0\,\Omega$.
  misconceptions:
    A: |-
      Divides the drop in length by $l_1$ instead of $l_2$. The second length measures the cell's *terminal pd*, and it is that shortened length the lost volts must be compared against.
    B: |-
      Uses $R\,l_1/l_2$, the ratio of emf to terminal pd, and calls it the internal resistance. That ratio is $(R+r)/R$, so $R$ still has to be subtracted before you have $r$.
    D: |-
      Divides by the whole $100\,\text{cm}$ of wire rather than by the second balance length. The full wire length never enters — both readings are compared with each other, and the gradient cancels.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A floodlit football ground at night with two lit pylons, an electronic scoreboard, a fourth official holding a glowing LED substitution board, and a pitch-side distribution box with cables running to the lights](scenes/football/current_electricity.svg "Everything electrical here runs off cells, and nobody can say how much push any of them has left.")

Half an hour before kick-off, Meenakshi is doing the pre-match checks on the balls. Each must be the right size and mass — between $410$ and $450$ grams — and the kit room's digital scale has chosen today to show nothing at all.

At the back of a shelf there is an old two-pan beam balance and a wooden case of brass weights. She loads a ball on one pan, adds weights to the other until the pointer sits dead on the centre mark, and writes down 430.

Her friend Tara is unimpressed by the antique. Meenakshi disagrees: a digital scale has to be trusted, and this thing does not. At the moment the pointer settles in the middle, the ball is being compared directly with brass of known mass, and the balance itself contributes nothing to the answer.

When she describes this in physics the next day, her teacher says the best voltage-measuring instrument in the lab works on exactly that principle — and it is a metre of plain wire with a slider on it.

A wire and a ruler, beating a meter. How?

## The physics

A **potentiometer** is a long uniform wire AB carrying a steady current from a separate **driver cell**, with a key and a rheostat in series to set that current.

Because the wire is uniform, every centimetre of it has the same resistance, so the potential falls **steadily** along it. If the potential difference across the whole wire of length $L$ is $V_{AB}$, then the pd between A and a point a distance $l$ from A is

$$V = k\,l, \qquad k = \frac{V_{AB}}{L}$$

where $k$ is the **potential gradient**, in volts per centimetre.

![A potentiometer circuit: a driver cell, key and rheostat sending a steady current through a long uniform wire, with a cell under test connected through a galvanometer to a jockey at the balance point](figures/potentiometer/potentiometer-principle.svg "The driver circuit sets up a steady fall of potential along the wire; the jockey finds the length whose pd exactly matches the cell being tested.")

Now connect the cell you want to measure with its **+ terminal to A** — the same polarity as the driver cell — and its other terminal through a galvanometer to a sliding contact, the **jockey**. Slide the jockey until the galvanometer reads exactly zero. At this **balance point** the pd across the length $l$ exactly opposes the cell, so

$$\varepsilon = k\,l$$

This is Meenakshi's beam balance in electrical form. What matters is what is *not* happening: at balance the test cell drives no current, so nothing is lost inside it to its internal resistance, and you read its true **emf**, not its terminal pd. A voltmeter cannot manage that — it must draw current to deflect, so it always reads a little low.

**Comparing two emfs.** Balance each cell in turn without touching the driver circuit, so $k$ is the same for both:

$$\frac{\varepsilon_1}{\varepsilon_2} = \frac{l_1}{l_2}$$

You never need to know $k$ — it cancels, just as the beam balance never needs the strength of gravity.

**Internal resistance.** Balance the cell on its own to get $l_1$, which measures $\varepsilon$. Then close a key that puts a known resistance $R$ across the cell. Now it *is* delivering current, so the balance measures its terminal pd $V = \varepsilon R/(R + r)$, which gives a shorter length $l_2$. Since $\varepsilon/V = l_1/l_2 = (R + r)/R$,

$$r = R\,\frac{l_1 - l_2}{l_2}$$

![The same potentiometer with a known resistance and a key across the cell under test, showing a long balance length with the key open and a shorter one with it closed](figures/potentiometer/potentiometer-internal-resistance.svg "Closing the key makes the cell deliver current; how far the balance point retreats measures the cell's internal resistance.")

For example, with $R = 6\,\Omega$, $l_1 = 60\,\text{cm}$ and $l_2 = 45\,\text{cm}$: $r = 6 \times 15/45 = 2.0\,\Omega$.

Conditions: the wire must be uniform, the driver current must stay steady between readings, and the driver's pd across AB must be **larger** than any emf you measure — otherwise there is no balance point anywhere, and the galvanometer deflects the same way all along the wire.

![Portrait photograph of an elderly bearded man](famous/johann-christian-poggendorff.jpg "Johann Christian Poggendorff (1796–1877), who devised this null method: balanced against a length of wire, the cell delivers no current. Public domain, via Wikimedia Commons.")

## Worked example

**Given:** a standard cell of emf $\varepsilon_1 = 1.2\,\text{V}$ balances at $l_1 = 40\,\text{cm}$. A second cell, measured straight afterwards with the driver circuit untouched, balances at $l_2 = 50\,\text{cm}$.
**Find:** the emf of the second cell.

Compare the lengths first — that is the whole measurement. The second cell needs $50/40 = 1.25$ times as much wire before it is held at zero, so it pushes $1.25$ times as hard as the standard cell.

$$\varepsilon_2 = \varepsilon_1\,\frac{l_2}{l_1} = 1.2 \times \frac{50}{40} = 1.5\,\text{V}$$

**Sanity check:** a fresh dry cell is worth about one and a half volts, so $1.5\,\text{V}$ is exactly the right size — and it had to come out *larger* than $1.2\,\text{V}$, since it needed the longer stretch of wire.

## Where the picture breaks

The beam balance is a real comparison, but do not push it too far: it compares two *forces* and needs gravity to pull equally on both pans, while the potentiometer compares two *potential differences* and weighs nothing. All the two share is the method — a null reading, in which the instrument's own imperfections drop out of the answer.

Beyond that, football is only the frame; the physics belongs to the apparatus. No real wire is perfectly uniform, and the driver cell is assumed to hold its current steady across both readings, so a driver running down shifts every balance length. Tap the jockey rather than dragging it, or the wire wears thin where you drag.

## Key takeaway

A potentiometer turns a voltage measurement into a length measurement: a steady current through a uniform wire gives a potential gradient $k$, and a cell balanced against it satisfies $\varepsilon = k\,l$. Because the cell delivers no current at balance, you measure its true emf and not its terminal pd — so emfs compare as $\varepsilon_1/\varepsilon_2 = l_1/l_2$, and a known $R$ switched across the cell gives $r = R(l_1 - l_2)/l_2$.
