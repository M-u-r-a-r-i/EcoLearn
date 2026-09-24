---
concept_id: emf_internal_resistance
interest: gaming
format: explain
title: The controller that reads full and still cuts out
check:
  question: |-
    A multimeter across a controller's cell reads $3.7\,\text{V}$ with nothing connected, and $3.1\,\text{V}$ while the rumble motors run and the cell delivers $1.2\,\text{A}$. The cell's internal resistance is closest to:
  options:
    A: |-
      $0.6\,\Omega$
    B: |-
      $2.6\,\Omega$
    C: |-
      $3.1\,\Omega$
    D: |-
      $0.5\,\Omega$
  answer: D
  explanation: |-
    The open-circuit reading is the emf, so the volts lost inside are $\varepsilon - V = 3.7 - 3.1 = 0.6\,\text{V}$. That drop is $Ir$, so $r = 0.6/1.2 = 0.5\,\Omega$.
  misconceptions:
    A: |-
      Stops at the lost voltage, $0.6\,\text{V}$, and calls it the resistance. The drop still has to be divided by the current to turn volts into ohms.
    B: |-
      Divides the terminal pd by the current. That gives the resistance of what is connected *outside* the cell, not the resistance inside it.
    C: |-
      Reads the terminal voltage straight off as a resistance. The units alone rule it out — volts are not ohms.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A night gaming desk with a monitor showing a frame counter and a low controller battery, a controller charging over a USB cable, a USB power meter, and an open PC case](scenes/gaming/current_electricity.svg "The battery bar on screen is a guess about charge; it says nothing about how hard the cell can push when something demands current.")

Farhan is three minutes into a boss fight when the controller dies. Not gradually — it simply disconnects, mid-rumble, and the screen throws up a "controller disconnected" prompt. He presses the button, it reconnects instantly, and reports a battery that is nearly full.

It happens again at the next heavy rumble sequence. Again the controller insists it has charge.

His cousin, who repairs phones, opens it with a plastic tool and puts a multimeter across the little lithium cell. With nothing running, it reads about $3.7\,\text{V}$ — a perfectly healthy nominal value. Then he keeps the meter there while the rumble motors kick in, and watches the reading collapse to roughly $3.0\,\text{V}$ before the controller drops out again.

The charge has not gone anywhere. The cell's voltage, apparently, depends on what you ask of it. Where do those volts go?

## The physics

A cell does two things at once, and the trouble comes from treating it as doing only the first.

The **electromotive force**, $\varepsilon$, is the energy the cell gives to each coulomb of charge it drives round the circuit — joules per coulomb, so volts. Despite the name it is not a force. It is the cell's full, honest push, and it is what you measure across the terminals when **no current is flowing**.

But the charge also has to get *through* the cell, past its electrolyte and electrodes, and that path has resistance of its own: the **internal resistance** $r$. It cannot be wired around or switched out — it sits inside the cell, in series with the emf.

![A cell drawn as an emf in series with a small internal resistance r, connected to an external resistance R](figures/emf_internal_resistance/cell-with-internal-resistance.svg "Every real cell is an ideal source plus a resistance you cannot get at — and the current has to cross both.")

With an external resistance $R$ connected, $\varepsilon$ drives the current through $R$ and $r$ in series:

$$I = \frac{\varepsilon}{R + r}$$

Some of the push is used up inside the cell, $Ir$ of it, so what the circuit outside actually receives is the **terminal potential difference**:

$$V = \varepsilon - Ir$$

Three consequences worth holding on to:

- With no current ($I = 0$), $V = \varepsilon$. An open-circuit reading gives the emf — which is exactly what Farhan's cousin measured first.
- The more current you draw, the further $V$ falls below $\varepsilon$, in a straight line of slope $-r$.
- While the cell is being *charged*, the current is pushed backwards through $r$, so the terminal voltage rises above the emf: $V = \varepsilon + Ir$.

![A graph of terminal potential difference against current: a straight line starting at the emf and falling with slope minus r](figures/emf_internal_resistance/terminal-pd-vs-current.svg "Extend the line back to zero current and the intercept is the emf; the steepness of the fall is the internal resistance.")

This assumes $r$ stays constant, which is only roughly true: it grows as a cell ages, and in the cold.

## Worked example

**Given:** a cell of emf $\varepsilon = 3.6\,\text{V}$ and internal resistance $r = 0.6\,\Omega$, driving a controller that behaves as $R = 3.0\,\Omega$ with its rumble motors running.
**Find:** the current, and the terminal potential difference.

The two resistances are in series with the emf, so the circuit's total resistance is $3.0 + 0.6 = 3.6\,\Omega$.

$$I = \frac{\varepsilon}{R+r} = \frac{3.6}{3.6} = 1.0\,\text{A}$$

Now how many volts that current loses inside the cell:

$$Ir = 1.0 \times 0.6 = 0.6\,\text{V}$$

So the controller's electronics actually receive

$$V = \varepsilon - Ir = 3.6 - 0.6 = 3.0\,\text{V}$$

A sixth of the cell's push is spent inside the cell itself — and $3.0\,\text{V}$ is near the level at which the controller decides the battery is flat and shuts down.

**Sanity check:** the volts must account for themselves: $3.0\,\text{V}$ delivered outside plus $0.6\,\text{V}$ lost inside is the full $3.6\,\text{V}$ of emf.

## Where the picture breaks

The gaming setting is real, but the model is tidier than the cell. A lithium cell's internal resistance is not a fixed number: it rises as the cell ages, rises sharply in the cold, and changes with how full the cell is. Treating $r$ as a constant is what makes the straight-line graph possible, and it is an approximation.

The controller is not really a fixed $3.0\,\Omega$ either — a rumble motor's current depends on how fast it is already spinning, and the electronics switch loads on and off far faster than a meter can follow, so the "collapse" Farhan's cousin saw is an average of something jumpier.

Finally, notice what the on-screen battery bar is and is not. It estimates the charge *left*, but the cut-out is caused by the cell's inability to hold its voltage under load. An old cell can be genuinely full and still fail, because $r$ has grown — which is why "it says full but it dies" is a symptom of age rather than of a lie.

## Key takeaway

A real cell is an emf $\varepsilon$ in series with an internal resistance $r$. It drives $I = \varepsilon/(R+r)$, and the outside world only receives the terminal pd $V = \varepsilon - Ir$. The emf is the open-circuit reading; the gap between emf and terminal pd is the price of pushing current through the cell itself, and it grows with the current and with the cell's age.
