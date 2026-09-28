---
concept_id: ohms_law
interest: smartphones
format: explain
title: Why a phone-stand light needs a resistor but the LED is not one
check:
  question: |-
    A small white LED for a phone-stand light passes $2\,\text{mA}$ at $2.7\,\text{V}$ and $20\,\text{mA}$ at $3.0\,\text{V}$. What do these readings show?
  options:
    A: |-
      the LED is non-ohmic: $V/I$ falls from $1350\,\Omega$ to $150\,\Omega$, so no single resistance describes it
    B: |-
      the LED is ohmic, because $V/I$ can still be worked out at each reading
    C: |-
      the LED is ohmic with $R = 150\,\Omega$, the value at its working point of $3.0\,\text{V}$
    D: |-
      the LED is non-ohmic, because its current goes up when the voltage goes up
  answer: A
  explanation: |-
    Ohm's law holds only if $V/I$ stays constant. Here $2.7/0.002 = 1350\,\Omega$ and $3.0/0.020 = 150\,\Omega$: an 11% rise in voltage gives ten times the current, so the $V$–$I$ graph is a curve, not a straight line.
  misconceptions:
    B: |-
      Thinks that being able to calculate $V/I$ means Ohm's law is obeyed. $V/I$ can be calculated for anything; Ohm's law says it stays the *same* as the voltage changes.
    C: |-
      Picks one reading and calls it the resistance. A single point cannot show ohmic behaviour; you need several readings that all give the same $V/I$.
    D: |-
      Right answer, wrong reason. Current rises with voltage in an ohmic resistor too; what makes the LED non-ohmic is that it rises *out of proportion*.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A charging corner: a phone on a wall charger, a power bank charging an earbuds case through a small USB meter, and a smartwatch on its charging puck, with current arrows on the cables](scenes/smartphones/current_electricity.svg "Five volts from a USB port is a fixed push; what current it drives depends entirely on what you plug in.")

Priya's project for the school exhibition is a phone stand with a little white reading light, powered from a USB port. The shop sold her an LED, a resistor and a length of wire.

She tests them on the lab's variable power supply before soldering. The resistor behaves like a textbook: turn the voltage up by half, the current goes up by half. She writes the numbers down in a neat table.

Then the LED. Below about $2.5\,\text{V}$ the meter reads almost nothing, and the LED stays dark. She nudges the knob a little further and the current leaps — $5\,\text{mA}$, then $20\,\text{mA}$, and the LED is suddenly blazing.

Her friend Farah, reading over her shoulder, says the shop told them always to put a resistor in series with an LED, "or it burns out". Priya wants to know why the resistor is so polite and the LED so wild — and why one needs the other.

## The physics

For many conductors — metal wires and ordinary resistors at a steady temperature — the current is directly proportional to the potential difference across them. This is **Ohm's law**:

$$V = IR$$

where $V$ is the potential difference in volts, $I$ the current in amperes, and $R$ the **resistance** in ohms ($1\,\Omega = 1\,\text{V/A}$). The law's content is that $R$ stays **constant** as $V$ changes, for a given conductor at constant temperature and other physical conditions.

A device that obeys this is **ohmic**: its $V$–$I$ graph is a straight line through the origin, and the slope gives the resistance. Priya's resistor is ohmic.

![A V–I graph with a straight line for an ohmic resistor and a curving line for a lamp](figures/ohms_law/vi-ohmic-vs-lamp.svg "A straight line through the origin means one fixed resistance; any bend means the ratio V/I is changing.")

Many useful devices are **non-ohmic**. A filament lamp's line bends because it heats up and its resistance rises. A diode such as an LED is more extreme: almost no current until a threshold voltage, then a steep rise; and reversing the voltage gives almost no current at all. For such devices you can still calculate $V/I$ at any single point, but it is different at every point, so Ohm's law does not describe them.

That is why the resistor is there. It is in series with the LED, so the same current passes through both.

![A single loop with a source, a resistor and a second component in series, the same current through each](figures/ohms_law/series-circuit-same-current.svg "One path means one current: the steady, ohmic resistor sets it, and the LED has to accept it.")

The resistor takes up whatever voltage the LED does not need and fixes the current with its predictable $V = IR$. Without it, a tiny excess of voltage across the LED would drive a huge current.

## Worked example

**Given:** in Priya's table, the resistor passes $I = 0.10\,\text{A}$ when $V = 2.0\,\text{V}$.
**Find:** its resistance, and the current it will pass on a $5.0\,\text{V}$ USB port.

$$R = \frac{V}{I} = \frac{2.0}{0.10} = 20\,\Omega$$

Because the resistor is ohmic, those $20\,\Omega$ stay the same at $5.0\,\text{V}$:

$$I = \frac{V}{R} = \frac{5.0}{20} = 0.25\,\text{A}$$

Two and a half times the voltage, two and a half times the current — exactly what "ohmic" means.

Now try the same trick on the LED: $20\,\text{mA}$ at $3.0\,\text{V}$ gives $V/I = 150\,\Omega$. Predicting its current at $5.0\,\text{V}$ from that number would say about $33\,\text{mA}$; in reality the current would soar far beyond that and destroy it within moments.

**Sanity check:** $0.25\,\text{A}$ is about what a small USB gadget draws, well under what a port can supply — the right size.

## Where the picture breaks

The lab supply and the LED are real; the neat straight line is the idealisation. Even Priya's resistor is only ohmic while its temperature stays steady. Run it hot and its resistance drifts a little.

Ohm's law is not a law of nature like conservation of charge: it is a property that some materials have over a range of conditions. The relation $R = V/I$ is simply a *definition* of resistance at a point, and it holds for everything; "obeying Ohm's law" means that this ratio does not change.

Finally, real LED circuits in phones are driven by dedicated electronics that control the current directly rather than by a single resistor. Priya's resistor is the simplest version of the same idea.

## Key takeaway

Ohm's law, $V = IR$ with $R$ constant, holds for metallic conductors at steady temperature: their $V$–$I$ graph is a straight line through the origin. Non-ohmic devices, such as lamps and LEDs, give a curved graph because $V/I$ changes as the voltage changes.
