---
concept_id: ohms_law
interest: gaming
format: explain
title: The arcade lamp that refuses to plot a straight line
check:
  question: |-
    Kabir plots $V$ against $I$ for the arcade cabinet's old filament lamp and gets a curve that bends away from a straight line, with the ratio $V/I$ growing as the current rises. This shows that:
  options:
    A: |-
      the lamp has no resistance, since Ohm's law does not apply to it
    B: |-
      the lamp's resistance is constant and the bend is a measurement error
    C: |-
      the lamp's resistance falls as its filament heats up
    D: |-
      the lamp's resistance rises as its filament heats up, so it is non-ohmic
  answer: D
  explanation: |-
    $V/I$ is the resistance at each point of the graph. A rising $V/I$ means a rising resistance, and the filament's temperature is what rises with it — a metal's resistance increases with temperature.
  misconceptions:
    A: |-
      Confuses "not ohmic" with "no resistance". A conductor always has a resistance $V/I$ at any working point; for a non-ohmic device that value simply is not the same at every point.
    B: |-
      Assumes anything that is not a straight line must be a mistake. The bend is real, repeatable and physical, and the lamp's V-I curve is a standard example in the syllabus.
    C: |-
      Gets the temperature effect backwards. Resistance falling with temperature is what a semiconductor or thermistor does; in a metal filament, resistance rises.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A night gaming desk with a monitor showing a frame counter, a controller charging over a USB cable with current arrows, a USB power meter, and an open PC case](scenes/gaming/current_electricity.svg "Everything lit on this desk is a resistor of some kind — and they do not all behave the same way.")

The robotics room has an arcade cabinet in the corner that has not worked since anyone can remember, and Kabir has volunteered to bring the marquee light back to life. The old filament lamp behind the glass still glows, but it drains the supply; his plan is a strip of LEDs with a small resistor in series instead.

His teacher makes him measure before he solders. So Kabir sets up a variable supply and plots voltage against current, twice — once for the resistor, once for the old lamp.

The resistor is beautifully boring. Double the voltage, double the current, every time; the graph is a straight line through the origin.

The lamp refuses. At low voltages it keeps up, then the line starts bending away, and once the filament is properly glowing he needs far more than double the voltage to get double the current.

Same supply, same meters, same student. Why does one obey and the other not?

## The physics

For many conductors, at a **constant temperature** and under constant physical conditions, the current through them is directly proportional to the potential difference across them. That is **Ohm's law**:

$$V = IR$$

where $V$ is in volts, $I$ in amperes, and the constant of proportionality $R$ is the **resistance**, in ohms ($\Omega$). One ohm is one volt per ampere.

![Portrait of Georg Simon Ohm](famous/georg-simon-ohm-portrait.jpg "Georg Simon Ohm (1789–1854), whose 1827 measurements established the proportionality that carries his name. Public domain, via Wikimedia Commons.")

Two things are worth being careful about, because they are examined.

**Ohm's law is not a universal law of nature.** It is a *property* that some materials happen to have, and only within limits. The definition of resistance, $R = V/I$, always applies; Ohm's law is the extra claim that this ratio stays the same as you change $V$. Materials that keep the promise are called **ohmic**, and give a straight $V$–$I$ line through the origin. Those that do not — a filament lamp, a diode, an LED, a semiconductor — are **non-ohmic**.

![A V-I graph with a straight line for a resistor and a curve for a filament lamp](figures/ohms_law/vi-ohmic-vs-lamp.svg "The straight line is an ohmic resistor; the lamp's line bends because its resistance climbs as the filament heats.")

**The condition of constant temperature is doing real work.** Kabir's lamp disobeys not because the physics changes, but because the lamp does not stay at one temperature. Push more current through and the filament heats to white heat; a metal's resistance rises with temperature; so each extra volt buys less extra current. Slope of the chord from the origin *is* the resistance, and it steepens as you go.

![Two resistors in series on a single loop, with the same current arrow through both](figures/ohms_law/series-circuit-same-current.svg "In a single loop the same current passes through every component — so the resistor and the LED in series always carry equal currents.")

In Kabir's new circuit, the resistor and the LED sit in one loop, so they carry the same current, and the resistor's job is to set that current at a safe value.

## Worked example

**Given:** Kabir's current-limiting resistor has $3.0\,\text{V}$ across it and carries $15\,\text{mA}$. Later, with a tired supply, the voltage across it falls to $2.4\,\text{V}$.
**Find:** the resistance, and the new current. Treat the resistor as ohmic and at a steady temperature.

Convert first: $15\,\text{mA} = 0.015\,\text{A}$.

$$R = \frac{V}{I} = \frac{3.0}{0.015} = 200\,\Omega$$

Two hundred ohms — an ordinary small resistor, the kind that is a few millimetres long.

Now the new current, with $R$ unchanged:

$$I = \frac{V}{R} = \frac{2.4}{200} = 0.012\,\text{A} = 12\,\text{mA}$$

The LED gets a fifth less current, so it looks a little dimmer.

**Sanity check:** the voltage fell to $80\%$ of its value and the current fell to $80\%$ of its value — proportional, which is exactly what an ohmic resistor promises.

## Where the picture breaks

The resistor's straight line is itself an idealisation. Run enough current through it and it too warms up and drifts off the line; "ohmic" always means *within a range*.

The LED is the bigger warning. It is not merely a bendy version of a resistor — below a threshold voltage it passes almost nothing, and above it the current shoots up for a tiny extra voltage. Writing $R = V/I$ for an LED gives a number, but a different number at every brightness, so you can never use one value of $R$ to predict another point. That is precisely why the circuit needs the resistor: the resistor, being ohmic and predictable, is what actually decides the current, and the LED just goes along with it.

## Key takeaway

Resistance is defined by $R = V/I$ for anything. **Ohm's law** is the stronger statement that $V = IR$ with $R$ constant, and it holds only for ohmic conductors at constant temperature. A straight $V$–$I$ line through the origin means ohmic; a bending line, like a filament lamp's, means the resistance is changing — usually because the device is heating up.
