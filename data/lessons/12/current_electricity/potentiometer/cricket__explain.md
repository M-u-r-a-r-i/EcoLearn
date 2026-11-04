---
concept_id: potentiometer
interest: cricket
format: explain
title: Why a slider on a wire beats the lab's best voltmeter
check:
  question: |-
    In a potentiometer experiment a cell of emf $1.2\,\text{V}$ balances at $60\,\text{cm}$ from end A. A second cell, measured straight afterwards with the driver circuit untouched, balances at $75\,\text{cm}$. The emf of the second cell is:
  options:
    A: |-
      $1.5\,\text{V}$
    B: |-
      $0.96\,\text{V}$
    C: |-
      $1.2\,\text{V}$
    D: |-
      $0.90\,\text{V}$
  answer: A
  explanation: |-
    The potential gradient is the same for both readings, so $\varepsilon = k\,l$ gives $\varepsilon_2 = \varepsilon_1\dfrac{l_2}{l_1} = 1.2 \times \dfrac{75}{60} = 1.5\,\text{V}$.
  misconceptions:
    B: |-
      Turns the ratio upside down, calculating $1.2 \times 60/75$. A longer stretch of wire carries a larger potential difference, so a longer balance length means a *stronger* cell, not a weaker one.
    C: |-
      Assumes the balance length only locates the cell on the wire and says nothing about its size. With a fixed gradient, length is directly proportional to emf — that is the whole point of the instrument.
    D: |-
      Uses the wire's full $100\,\text{cm}$ instead of the first cell's $60\,\text{cm}$, as if $1.2\,\text{V}$ were spread over the whole wire. The gradient must be worked out from the known cell's own balance length.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A cricket ground at dusk with floodlights, an electronic scoreboard, glowing stumps and an umpire holding a light meter](scenes/cricket/current_electricity.svg "Everything electrical on this ground runs off cells — and nobody can say how strong any of them still are.")

Thursday evening at the nets. Aditi has the bowling machine on its slowest setting, and Imran, padded up, wants it quicker. She gives the speed dial a quarter turn, and the next ball hurries him into a late, ugly defensive push.

Afterwards he unscrews the control box, expecting electronics. There is almost nothing inside: a curved strip of grey resistive track with a metal wiper pressed against it, turning with the knob. The supply itself never changes. All the dial does is choose how far along the track the wiper sits — and so what fraction of the supply's voltage reaches the motor.

Their physics teacher, locking up next door, glances at it and says something strange. Stretch that same idea into a metre of straight wire, read it against a ruler, and you get an instrument that measures a cell's emf more accurately than any voltmeter in her lab.

A slider on a wire, beating a meter. How?

## The physics

A **potentiometer** is a long uniform wire AB carrying a steady current from a separate **driver cell**, with a key and a rheostat in series to set that current.

Because the wire is uniform, every centimetre of it has the same resistance, so the potential falls *steadily* along it. If the potential difference across the whole wire of length $L$ is $V_{AB}$, then the pd between A and a point a distance $l$ from A is

$$V = k\,l, \qquad k = \frac{V_{AB}}{L}$$

where $k$ is the **potential gradient**, in volts per centimetre. That is exactly the bowling machine's dial: tap the track part-way along and you get part of the supply's voltage.

![A potentiometer circuit: a driver cell, key and rheostat sending a steady current through a long uniform wire, with a cell under test connected through a galvanometer to a jockey at the balance point](figures/potentiometer/potentiometer-principle.svg "The driver circuit sets up a steady fall of potential along the wire; the jockey picks the length whose pd exactly matches the test cell.")

Now connect the cell you want to measure with its **+ terminal to A** — the same polarity as the driver cell — and its other terminal through a galvanometer to a sliding contact, the **jockey**. Slide the jockey until the galvanometer reads exactly zero. At this **balance point** the pd across the length $l$ exactly opposes the cell, so

$$\varepsilon = k\,l$$

What matters is what *isn't* happening. At balance the test cell drives no current, so nothing is lost to its internal resistance and you read its true **emf**, not the terminal pd. A voltmeter can never manage that: it must draw some current to deflect, so it always reads a little low.

**Comparing two emfs.** Balance each cell in turn without touching the driver circuit, so $k$ is the same for both:

$$\frac{\varepsilon_1}{\varepsilon_2} = \frac{l_1}{l_2}$$

You never need to know $k$ — it cancels.

**Internal resistance.** Balance the cell alone to get $l_1$, which measures $\varepsilon$. Then close a key that puts a known resistance $R$ across the cell. Now it is delivering current, so the balance measures its terminal pd $V = \varepsilon R/(R+r)$, giving a shorter length $l_2$. Since $\varepsilon/V = l_1/l_2 = (R+r)/R$,

$$r = R\,\frac{l_1 - l_2}{l_2}$$

![The same potentiometer with a known resistance and a key connected across the cell under test, showing a long balance length with the key open and a shorter one with it closed](figures/potentiometer/potentiometer-internal-resistance.svg "Closing the key makes the cell deliver current; how far the balance point retreats is a measure of the cell's internal resistance.")

For example, with $R = 4.0\,\Omega$, $l_1 = 60\,\text{cm}$ and $l_2 = 48\,\text{cm}$: $r = 4.0 \times 12/48 = 1.0\,\Omega$.

Conditions: the wire must be uniform, the driver current must stay steady between readings (don't nudge the rheostat), and the driver's pd across AB must be **larger** than any emf you measure — otherwise there is no balance point anywhere and the galvanometer deflects the same way all along.

![Portrait photograph of an elderly bearded man](famous/johann-christian-poggendorff.jpg "Johann Christian Poggendorff (1796–1877), who devised this method: balanced against a length of wire, the cell delivers no current. Public domain, via Wikimedia Commons.")

## Worked example

**Given:** a standard cell of emf $\varepsilon_1 = 1.0\,\text{V}$ balances at $l_1 = 50\,\text{cm}$. The club's cell, measured immediately afterwards with the same driver circuit, balances at $l_2 = 60\,\text{cm}$.
**Find:** the emf of the club's cell.

The club's cell needs $60/50 = 1.2$ times as much wire to be held at zero — so it is pushing 1.2 times as hard as the standard cell.

$$\varepsilon_2 = \varepsilon_1\,\frac{l_2}{l_1} = 1.0 \times \frac{60}{50} = 1.2\,\text{V}$$

**Sanity check:** a single cell is worth around a volt and a half when fresh, so $1.2\,\text{V}$ is a sensible answer for a cell that has done some work — a few millivolts or twenty volts would have meant a slip.

## Where the picture breaks

The dial and the instrument are the same component used in opposite ways, and the difference is the lesson. The machine's dial has to *deliver* current to the motor, and the moment it does, the voltage at the wiper is no longer a clean fraction of the supply — the load drags it down. The measuring potentiometer is accurate precisely because at balance it delivers nothing.

Beyond that, cricket is only the setting; the physics belongs to the apparatus. No real wire is perfectly uniform, and the driver cell is assumed to hold its current steady while you take both readings — a cell running down shifts every balance length. Tap the jockey rather than drag it, and keep the current off between readings, or the wire wears and warms. And the gradient has to be chosen sensibly: make $k$ too large and the balance crowds into the first few centimetres, too small and it runs off the end of the wire.

## Key takeaway

A potentiometer turns a voltage measurement into a length measurement: a steady current through a uniform wire gives a potential gradient $k$, and a cell balanced against it satisfies $\varepsilon = k\,l$. Because no current flows from the cell at balance, you measure its true emf rather than its terminal pd — so emfs compare as $\varepsilon_1/\varepsilon_2 = l_1/l_2$, and a known $R$ switched across the cell gives $r = R(l_1 - l_2)/l_2$.
