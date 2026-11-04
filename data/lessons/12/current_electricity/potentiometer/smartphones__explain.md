---
concept_id: potentiometer
interest: smartphones
format: explain
title: Testing tracker-tag coin cells without taking any current
check:
  question: |-
    A coin cell is balanced on a potentiometer. Without changing anything else, the rheostat in the driver circuit is turned so that the **driver current increases**. To balance the same cell again, the jockey must now be placed:
  options:
    A: |-
      further along the wire, at a longer balance length
    B: |-
      at the same point, because the cell's emf has not changed
    C: |-
      closer to the start of the wire, at a shorter balance length
    D: |-
      nowhere, because the wire can no longer be balanced
  answer: C
  explanation: |-
    More driver current means a larger pd across the wire, so a larger potential gradient $k$. Since $\varepsilon = k\,l$ with $\varepsilon$ fixed, a larger $k$ needs a shorter $l$.
  misconceptions:
    A: |-
      Inverts the relation, as if more current meant each centimetre carried less potential. A bigger current makes the potential fall *faster* along the wire, so fewer centimetres are needed.
    B: |-
      Forgets that the balance length depends on the potential gradient as well as on the emf. The emf is unchanged, but $l = \varepsilon/k$ changes whenever $k$ does.
    D: |-
      Mixes this up with the real failure condition, which is a driver pd *smaller* than the emf. Increasing the driver current makes the pd across the wire larger, so a balance point still exists.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A charging corner: a phone on a wall charger, a power bank charging an earbuds case through a small USB meter, and a smartwatch on its charging puck, with current arrows on the cables](scenes/smartphones/current_electricity.svg "A meter that draws even a little current changes what it is trying to measure.")

Harsh's family uses little Bluetooth tracker tags on everything — keys, a school bag, the scooter. Each runs on a flat lithium coin cell, rated $3\,\text{V}$, and the spares live in a jar where fresh and used cells have got hopelessly mixed.

Harsh tests them all with a multimeter. Almost every one reads close to $3\,\text{V}$. He puts one back in the scooter's tag — and it dies within a week.

He takes the jar to his physics lab, where Ms. Fernandes listens and points to a board with a long wire, a ruler and a galvanometer. "Your meter has to take a little current to show a reading. So you never saw the cell's true emf, and you never saw how tired it was inside."

"This thing," she says, "measures a cell while it delivers *no current at all*." How can a measurement that takes nothing from a cell tell you how worn out it is?

## The physics

A **potentiometer** is a long uniform wire AB carrying a steady current from a separate **driver cell**, with a key and a rheostat to set that current. Because the wire is uniform, the potential falls steadily along it. If the pd across the whole length $L$ is $V_{AB}$, the pd across a length $l$ from A is

$$V = k\,l, \qquad k = \frac{V_{AB}}{L}$$

where $k$ is the **potential gradient**, in volts per centimetre.

![A potentiometer circuit: a driver cell, key and rheostat sending a steady current through a long uniform wire, with a cell under test connected through a galvanometer to a jockey at the balance point](figures/potentiometer/potentiometer-principle.svg "The driver circuit lays a steady slope of potential along the wire; the jockey finds the length whose pd exactly matches the test cell.")

Connect the test cell with its $+$ terminal to A, the same side as the driver's $+$, and its other terminal through a galvanometer to the **jockey**. Slide until the galvanometer reads zero. At this **balance point** the pd along $l$ exactly opposes the cell, so no current flows through it and

$$\varepsilon = k\,l$$

With no current, nothing is lost across the internal resistance: you measure the true **emf**, which no voltmeter can do.

**Comparing emfs.** Balance two cells in turn with the driver circuit untouched; $k$ cancels:

$$\frac{\varepsilon_1}{\varepsilon_2} = \frac{l_1}{l_2}$$

**Internal resistance.** Balance the cell alone at $l_1$. Then connect a known resistance $R$ across it with a key; now it delivers current, the balance measures its terminal pd, and the length shrinks to $l_2$. Since $l_1/l_2 = (R + r)/R$,

$$r = R\,\frac{l_1 - l_2}{l_2}$$

![The same potentiometer with a known resistance and a key across the cell under test](figures/potentiometer/potentiometer-internal-resistance.svg "How far the balance point retreats once the cell starts delivering current measures its internal resistance.")

The driver's pd across the wire must be larger than any emf you measure, and the driver current must stay steady between readings.

![Portrait photograph of an elderly bearded man](famous/johann-christian-poggendorff.jpg "Johann Christian Poggendorff (1796–1877), who devised this null method of balancing a cell against a length of wire. Public domain, via Wikimedia Commons.")

## Worked example

**Given:** on a $4\,\text{m}$ potentiometer wire, a reference cell of emf $1.5\,\text{V}$ balances at $150\,\text{cm}$, and one of Harsh's coin cells at $270\,\text{cm}$. With $R = 40\,\Omega$ across the coin cell, its balance moves to $240\,\text{cm}$ (illustrative values).
**Find:** the coin cell's emf and internal resistance.

The reference cell shows the gradient is $1.5\,\text{V}$ per $150\,\text{cm}$, so the coin cell's emf is

$$\varepsilon = 1.5 \times \frac{270}{150} = 2.7\,\text{V}$$

Already below its rated $3\,\text{V}$ — a used cell.

With the $40\,\Omega$ connected, the balance retreats by $30\,\text{cm}$:

$$r = R\,\frac{l_1 - l_2}{l_2} = 40 \times \frac{30}{240} = 5\,\Omega$$

Five ohms inside a cell whose job is to deliver short bursts of current: this one belongs in the recycling box.

**Sanity check:** with $r = 5\,\Omega$, the terminal pd is $2.7 \times \dfrac{40}{45} = 2.4\,\text{V}$, which at $0.01\,\text{V/cm}$ is exactly the $240\,\text{cm}$ balance measured.

## Where the picture breaks

The tracker tags are the reason, not the physics. A coin cell's internal resistance is not a fixed property: it depends on temperature, on how much charge is left, and on the current drawn, so $5\,\Omega$ is a comparison between cells, not a promise about battery life. A used cell also recovers a little after resting, which is part of why Harsh's multimeter misled him.

On the bench: tap the jockey rather than dragging it, and switch off the driver current between readings so the wire does not warm.

## Key takeaway

A potentiometer turns a voltage measurement into a length measurement: a steady current through a uniform wire gives a potential gradient $k$, and a balanced cell satisfies $\varepsilon = k\,l$. Because the cell delivers no current at balance, you get its true emf: emfs compare as $\varepsilon_1/\varepsilon_2 = l_1/l_2$, and a known $R$ across the cell gives $r = R\,(l_1 - l_2)/l_2$.
