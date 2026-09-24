---
concept_id: potentiometer
interest: gaming
format: explain
title: Sorting a drawer of dead cells with a metre of wire
check:
  question: |-
    A cell's emf is measured with a potentiometer and, immediately afterwards, with a good voltmeter. The voltmeter's reading is slightly lower. Why?
  options:
    A: |-
      the potentiometer wire warms up, which exaggerates the balance length
    B: |-
      a voltmeter must draw some current to deflect, so it reads the terminal pd, which is less than the emf
    C: |-
      the voltmeter's scale is less precisely calibrated than the potentiometer's ruler
    D: |-
      a cell's emf drops as soon as it is connected to anything
  answer: B
  explanation: |-
    At balance the test cell delivers no current, so nothing is lost across its internal resistance and the reading is the true emf. Any voltmeter passes a small current, so it reads $V = \varepsilon - Ir$, a little below $\varepsilon$.
  misconceptions:
    A: |-
      Invents an instrument fault. The shortfall is in the voltmeter, not the wire, and it appears even with a cool, perfectly uniform potentiometer.
    C: |-
      Blames calibration. A perfectly calibrated voltmeter still reads low, because drawing current is what causes the shortfall, not the markings on the scale.
    D: |-
      Confuses emf with terminal pd. The emf is set by the cell's chemistry and does not change when you connect something; the terminal pd falls, by $Ir$.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A night gaming desk with a monitor showing a low controller battery, a controller charging over a USB cable, a USB power meter, and an open PC case](scenes/gaming/current_electricity.svg "A cell that reads healthy on a meter and a cell that can actually run a controller are not always the same cell.")

Gaurav's wireless controller eats AA cells, and the drawer beside the console has become a graveyard: twenty-odd cells, some fresh, some finished, none of them labelled.

He does the sensible thing and tests every one with the multimeter. Almost all of them read about $1.5\,\text{V}$. He sorts out the best two, loads them into the controller — and it dies in forty minutes.

The next pair, which read exactly the same on the meter, last all weekend.

His sister, who is preparing for her practical exam, tells him the meter was never going to tell him what he wanted to know. The apparatus that will is on the lab bench: a metre of wire, a ruler and a galvanometer. And it works, she says, by arranging for the cell under test to do nothing at all.

Making a cell do nothing, in order to find out what it can do. How does that help?

## The physics

A **potentiometer** is a long uniform wire AB carrying a steady current from a separate **driver cell**, with a key and a rheostat in series to set that current.

Because the wire is uniform, every centimetre has the same resistance, so the potential falls *steadily* along it. If the potential difference across the whole wire of length $L$ is $V_{AB}$, then between A and a point a distance $l$ from A,

$$V = k\,l, \qquad k = \frac{V_{AB}}{L}$$

where $k$ is the **potential gradient**, in volts per centimetre.

![A potentiometer circuit: a driver cell, key and rheostat sending a steady current through a long uniform wire, with a cell under test connected through a galvanometer to a jockey at the balance point](figures/potentiometer/potentiometer-principle.svg "The driver circuit lays a steady slope of potential along the wire; the jockey finds the length whose pd exactly matches the test cell.")

Now connect the cell you want to measure with its **+ terminal to A** — the same polarity as the driver — and its other terminal through a galvanometer to a sliding contact, the **jockey**. Slide until the galvanometer reads exactly zero. At this **balance point** the pd across the length $l$ exactly opposes the cell, so

$$\varepsilon = k\,l$$

What matters is what *is not* happening. At balance the test cell drives no current at all, so nothing is lost across its internal resistance and you read its true **emf**, not its terminal pd. A voltmeter can never manage this: it must draw current to deflect, so it always reads slightly low.

**Comparing two emfs.** Balance each cell in turn without touching the driver circuit, so $k$ is the same for both:

$$\frac{\varepsilon_1}{\varepsilon_2} = \frac{l_1}{l_2}$$

You never need to know $k$ — it cancels.

**Internal resistance.** Balance the cell alone to get $l_1$, which measures $\varepsilon$. Then close a key that puts a known resistance $R$ across the cell. Now it *is* delivering current, so the balance measures its terminal pd $V = \varepsilon R/(R+r)$, giving a shorter length $l_2$. Since $\varepsilon/V = l_1/l_2 = (R+r)/R$,

$$r = R\,\frac{l_1 - l_2}{l_2}$$

![The same potentiometer with a known resistance and a key across the cell under test, showing a long balance length with the key open and a shorter one with it closed](figures/potentiometer/potentiometer-internal-resistance.svg "How far the balance point retreats when the cell starts delivering current is a measure of its internal resistance.")

Conditions: the wire must be uniform, the driver current must stay steady between readings (do not nudge the rheostat), and the driver's pd across AB must be **larger** than any emf you measure — otherwise there is no balance point anywhere on the wire and the galvanometer deflects the same way all along it.

![Portrait photograph of an elderly bearded man](famous/johann-christian-poggendorff.jpg "Johann Christian Poggendorff (1796–1877), who devised this null method: balanced against a length of wire, the cell delivers no current. Public domain, via Wikimedia Commons.")

## Worked example

**Given:** one of Gaurav's cells balances at $l_1 = 80\,\text{cm}$ on its own. A known $R = 6.0\,\Omega$ is then switched across it, and the new balance is at $l_2 = 60\,\text{cm}$.
**Find:** the cell's internal resistance.

The balance retreated from $80$ to $60\,\text{cm}$ — to three-quarters of its length — so once the cell is delivering current, only three-quarters of its emf reaches the outside world. The missing quarter is being spent inside the cell.

$$r = R\,\frac{l_1 - l_2}{l_2} = 6.0 \times \frac{20}{60} = 2.0\,\Omega$$

Two ohms is a lot for a cell. This is one of the tired ones: run it into a controller and a serious fraction of its push disappears inside it as heat.

**Sanity check:** a quarter of the emf should be lost inside, and $\dfrac{r}{R+r} = \dfrac{2}{8} = 0.25$ — a quarter. The two routes agree.

## Where the picture breaks

The lab bench is the physics; the drawer of cells is only the reason to care. Two honest limits on what the measurement means.

First, $r$ is not a fixed property. The potentiometer measures it at whatever small current $R$ allows, and a cell's internal resistance is higher when it is cold, higher as it empties, and not the same under a controller's rumble-motor surges as under a gentle test current. The number is a fair comparison between cells, not a promise about battery life.

Second, a rested cell recovers: leave a tired one alone for an hour and both its emf and its measured $r$ look better than they did at the end of a session. That is exactly why Gaurav's multimeter kept lying to him.

Practically, too: tap the jockey rather than dragging it, and keep the driver current off between readings so the wire does not warm.

## Key takeaway

A potentiometer converts a voltage measurement into a length measurement: a steady current through a uniform wire gives a potential gradient $k$, and a cell balanced against it satisfies $\varepsilon = k\,l$. Because the cell delivers no current at balance, you get its true emf, so emfs compare as $\varepsilon_1/\varepsilon_2 = l_1/l_2$, and switching a known $R$ across the cell gives $r = R\,(l_1 - l_2)/l_2$.
