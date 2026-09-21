---
concept_id: ohms_law
interest: music
format: challenge
title: Is the amp's pilot lamp obeying Ohm's law
check:
  question: |-
    A student measures a component from an amplifier and plots a V–I graph ($V$ on the vertical axis, $I$ on the horizontal). It is a straight line through the origin with a slope of $220\,\text{V/A}$. What does this show?
  options:
    A: |-
      The component is non-ohmic, because its voltage keeps rising with current.
    B: |-
      The component is ohmic, with a resistance of $220\,\Omega$.
    C: |-
      The component is ohmic, with a resistance of $1/220\,\Omega$.
    D: |-
      The component's resistance increases as the current increases.
  answer: B
  explanation: |-
    A straight line through the origin means $V \propto I$ — ohmic behaviour. With $V$ on the vertical axis, the slope $V/I$ is the resistance: $220\,\Omega$.
  misconceptions:
    A: |-
      Mistakes "voltage rises with current" for non-ohmic behaviour; in fact a proportional rise is exactly what Ohm's law describes.
    C: |-
      Inverts the slope, as if the graph had $I$ on the vertical axis.
    D: |-
      Confuses voltage rising with resistance rising; along a straight line through the origin, $V/I$ is the same everywhere.
author: claude-code/opus-5
written: 2026-09-21
---
## The story

![A desk with a guitar, an effects pedal and a guitar amplifier](scenes/music/current_electricity.svg "An old amplifier, a spare lamp, and a question.")

Tanvi's uncle gives her his old guitar amplifier from the 1970s. It still works, and when she switches it on, a tiny lamp on the front glows orange — the pilot lamp that tells you the amp is on.

In the box she finds a spare lamp, and her physics brain switches on too. She clips it to her school's bench power supply and takes two readings. At $1.0\,\text{V}$ the lamp barely glows and draws $50\,\text{mA}$. At $6.0\,\text{V}$ it glows bright white.

"Ohm's law," she thinks. "Six times the voltage, so six times the current — it should draw $300\,\text{mA}$." The meter says something else entirely. Before reading on: what do you think the meter showed, and why?

## The challenge

An old valve guitar amplifier has a little lamp on the front that glows when it's switched on — its pilot lamp. A curious guitarist takes a spare lamp of the same kind and tests it on a bench power supply:

| Voltage across lamp | Current through lamp |
|---|---|
| $1.0\,\text{V}$ | $50\,\text{mA}$ |
| $6.0\,\text{V}$ | $150\,\text{mA}$ |

Does the lamp obey Ohm's law? And if you had predicted the current at $6.0\,\text{V}$ from the first reading alone, what would you have got?

## Think first

Voltage went up six times. Did the current go up six times? What would that mean? Before reading on, work out the resistance at each reading — or at least decide whether you expect it to stay the same.

## The reveal

Work out the resistance at each point using $R = V/I$ (converting mA to A first):

$$R_{1\,\text{V}} = \frac{1.0}{0.050} = 20\,\Omega, \qquad R_{6\,\text{V}} = \frac{6.0}{0.150} = 40\,\Omega$$

The resistance **doubled**. If the lamp were ohmic, $R$ would stay at $20\,\Omega$, and at $6.0\,\text{V}$ the current would have been

$$I = \frac{V}{R} = \frac{6.0}{20} = 0.30\,\text{A} = 300\,\text{mA}$$

— twice what was measured. So the lamp is **non-ohmic**.

![A V–I graph: a straight blue line through the origin for a 20 ohm resistor, and a red curve bending upwards for a filament lamp](figures/ohms_law/vi-ohmic-vs-lamp.svg "Tanvi's lamp is the red curve: 20 Ω when barely warm, 40 Ω when white-hot. An ohmic 20 Ω resistor would follow the blue line to 300 mA at 6 V.")

The reason is temperature. At $6.0\,\text{V}$ the thin filament glows white-hot, and a metal's resistance rises as it heats: its vibrating atoms get in the way of the drifting electrons more often. Ohm's law only promises proportionality **at constant temperature** — and the filament's temperature is anything but constant.

## The physics

The resistance of any component at any moment is defined as $R = V/I$. **Ohm's law** says that for a metallic conductor under constant physical conditions, especially temperature, $R$ stays constant, so

$$V = IR \quad \text{and} \quad I \propto V$$

To test a component, plot its V–I graph:

- **Ohmic**: a straight line through the origin. With $V$ on the vertical axis, the slope is $R$.
- **Non-ohmic**: a curve. A filament lamp bends towards the voltage axis as it heats (its resistance rises); a diode conducts in one direction only.

## Worked example

A resistor inside a guitar pedal is tested:

| $V$ | $1.0\,\text{V}$ | $2.0\,\text{V}$ | $3.0\,\text{V}$ |
|---|---|---|---|
| $I$ | $2.0\,\text{mA}$ | $4.0\,\text{mA}$ | $6.0\,\text{mA}$ |

$$R = \frac{1.0}{0.0020} = \frac{2.0}{0.0040} = \frac{3.0}{0.0060} = 500\,\Omega$$

The ratio is constant, so this resistor is ohmic over this range, with $R = 500\,\Omega$ — and its V–I graph would be a straight line through the origin with slope $500\,\text{V/A}$.

## Key takeaway

Resistance is always $R = V/I$ at a given moment, but a component obeys **Ohm's law** only if that ratio stays constant — a straight-line V–I graph through the origin. Filament lamps heat up and become non-ohmic; Ohm's law holds only at constant temperature.
