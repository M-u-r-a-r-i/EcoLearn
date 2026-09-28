---
concept_id: moving_coil_galvanometer
interest: smartphones
format: explain
title: One meter, two jobs at the repair stall
check:
  question: |-
    A galvanometer has a coil resistance of $100\,\Omega$ and gives full-scale deflection at $1.0\,\text{mA}$. A repair technician wants to turn it into a voltmeter that reads up to $10\,\text{V}$, to check chargers. What must she add?
  options:
    A: |-
      $9900\,\Omega$ in parallel with the galvanometer
    B: |-
      $9900\,\Omega$ in series with the galvanometer
    C: |-
      $10\,000\,\Omega$ in series with the galvanometer
    D: |-
      About $0.010\,\Omega$ in parallel with the galvanometer
  answer: B
  explanation: |-
    At full scale, $10\,\text{V}$ must drive exactly $1.0\,\text{mA}$ through the meter, so its total resistance must be $10/(1.0\times10^{-3}) = 10\,000\,\Omega$. The coil already provides $100\,\Omega$, so a series resistance of $10\,000 - 100 = 9900\,\Omega$ is needed.
  misconceptions:
    A: |-
      Gets the right value but puts it in parallel. A resistance in parallel lets current bypass the coil, which is how you make an *ammeter*; a voltmeter needs a large resistance in **series** to limit the current.
    C: |-
      Forgets that the galvanometer's own coil is part of the total resistance. The series resistor plus the coil must add to $10\,000\,\Omega$, so the resistor is $9900\,\Omega$.
    D: |-
      Mixes up the two conversions. A tiny resistance in parallel (a shunt) makes an ammeter; used as a voltmeter across a charger, it would draw a huge current.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A desk with a phone lying on a charging cable showing a swung compass arrow, a wireless charging pad with its coil exposed, a flip-cover case with a small magnet in its flap, and a speaker and a small cylinder-shaped vibration motor taken apart](scenes/smartphones/moving_charges_magnetism.svg "Each gadget here uses a current and a magnet to make something move. A meter needle is the same idea, made to measure.")

Farhan's aunt, Zainab, has run a phone repair stall in the market for twenty years. On her bench, among the digital gadgets, sits one old analogue meter with a needle and a big round selector knob.

A customer's phone won't charge. Zainab clips the meter across the charger's output: the needle swings to about 5 on the "DC V" scale. Charger fine. She turns the knob, rewires the meter into the cable itself, and now the same needle swings across a scale marked in **amperes**, showing how much current the phone is actually drawing.

Farhan has taken the meter apart once. Inside there is only one moving part: a tiny coil on a pivot, a spiral spring and a magnet. No separate voltmeter, no separate ammeter.

How can the same small coil measure volts one minute and amperes the next — and what does the knob actually switch?

## The physics

The heart of both meters is a **moving coil galvanometer**: a rectangular coil of $N$ turns and area $A$, free to turn between the poles of a magnet, with a spiral spring resisting the turning.

![The inside of a moving coil galvanometer: a coil on a soft iron core between curved pole pieces, with a spiral spring and a pointer, and the scale seen from outside](figures/moving_coil_galvanometer/galvanometer-construction.svg "The curved pole pieces and the soft iron core make the field in the gap radial, so the coil's plane always lies along the field and the torque never depends on its angle.")

A current $I$ in the coil gives a torque $\tau = NIAB\sin\theta$ (last lesson). The pole pieces are curved and a soft iron cylinder sits inside the coil, which makes the field **radial**: whichever way the coil turns, its plane lies along the field, so $\sin\theta = 1$ and $\tau = NIAB$.

The spring twists back with a torque $k\phi$, where $\phi$ is the angle turned and $k$ is the spring's torsional constant. The coil stops where the two balance:

$$NIAB = k\phi \qquad\Longrightarrow\qquad \phi = \left(\frac{NAB}{k}\right) I$$

So **the deflection is proportional to the current**, and the scale is evenly spaced. $\phi/I = NAB/k$ is the **current sensitivity**. A galvanometer is very sensitive: its full-scale current $I_g$ is often only a milliampere or less.

**Ammeter: add a small shunt in parallel.** To measure a current $I$ much bigger than $I_g$, a small resistance $S$ (a **shunt**) is joined in parallel so that most of the current bypasses the coil. The coil and the shunt have the same voltage across them, so $I_g G = (I - I_g)S$, giving

$$S = \frac{I_g G}{I - I_g}$$

The ammeter is joined in **series** with the circuit, and its resistance is very small, so it barely changes the current it measures.

**Voltmeter: add a large resistance in series.** To measure a voltage $V$, a large resistance $R$ goes in series with the coil, so that $V$ drives exactly $I_g$ at full scale:

$$R = \frac{V}{I_g} - G$$

The voltmeter is joined in **parallel** across the component, and its resistance is very large, so it barely draws any current.

![On the left, a galvanometer with a small shunt in parallel making an ammeter in series with the circuit; on the right, a galvanometer with a large resistance in series making a voltmeter across a component](figures/moving_coil_galvanometer/ammeter-and-voltmeter.svg "Same galvanometer, two jobs. A tiny shunt in parallel makes an ammeter; a large resistance in series makes a voltmeter. Zainab's knob just switches between them.")

## Worked example

**Given:** a galvanometer with coil resistance $G = 50\,\Omega$ and full-scale current $I_g = 1.0\,\text{mA} = 1.0\times10^{-3}\,\text{A}$ (illustrative values).
**Find:** the resistance needed to read up to $5.0\,\text{V}$ (a USB charger), and the shunt needed to read up to $1.0\,\text{A}$.

**Step 1 — the voltmeter.**

$$R = \frac{V}{I_g} - G = \frac{5.0}{1.0\times10^{-3}} - 50 = 5000 - 50 = 4950\,\Omega \text{ in series}$$

**Step 2 — the ammeter.**

$$S = \frac{I_g G}{I - I_g} = \frac{(1.0\times10^{-3})(50)}{1.0 - 0.001} \approx 0.050\,\Omega \text{ in parallel}$$

Only one thousandth of the current goes through the coil; the other $999$ parts flow through a shunt that is little more than a short, thick strip of metal.

**Sanity check:** the voltmeter's resistance is about a hundred thousand times the ammeter's, which is exactly what the two jobs need — one must hardly draw current, the other must hardly block it.

## Where the picture breaks

A digital meter, like most of Zainab's newer gadgets, has no coil and no spring. It measures a voltage electronically and computes the rest. The shunt and series-resistor idea survives inside it, but the moving coil does not.

No meter is perfect, either. The ammeter's small resistance lowers the current slightly; the voltmeter's finite resistance draws a little current and lowers the voltage it is measuring. Good design only makes these effects small.

And the spring's $k\phi$ law holds only for small twists; the maker chooses the full-scale angle so that it stays true.

## Key takeaway

A **moving coil galvanometer** turns a current into a steady deflection: in a radial field the coil feels a torque $NIAB$, balanced by the spring's $k\phi$, so $\phi \propto I$. A small **shunt in parallel** converts it into an **ammeter** (joined in series, very low resistance); a large **resistance in series** converts it into a **voltmeter** (joined in parallel, very high resistance).
