---
concept_id: ohms_law
interest: cricket
format: explain
title: The circuit that makes the bails light up
check:
  question: |-
    A resistor in an umpire's light meter carries $20\,\text{mA}$ when there is $5.0\,\text{V}$ across it. What is its resistance?
  options:
    A: |-
      $0.25\,\Omega$
    B: |-
      $100\,\Omega$
    C: |-
      $4.0\,\Omega$
    D: |-
      $250\,\Omega$
  answer: D
  explanation: |-
    Convert the current to amperes first: $20\,\text{mA} = 0.020\,\text{A}$. Then $R = V/I = 5.0/0.020 = 250\,\Omega$.
  misconceptions:
    A: |-
      Divides $5.0$ by $20$ without converting milliamperes to amperes — a unit slip that makes the answer 1000 times too small.
    B: |-
      Multiplies voltage by current instead of dividing; $V \times I$ is power, not resistance.
    C: |-
      Inverts the definition, computing $I/V$ (and skipping the unit conversion); resistance is $V/I$.
author: claude-code/opus-5
written: 2026-09-21
---
## The story

![A cricket ground at dusk with floodlights, an electronic scoreboard, glowing stumps and an umpire holding a light meter](scenes/cricket/current_electricity.svg "Dusk at the ground: nearly everything you can see runs on an electric circuit.")

It's the final over of a day-night match, and the light is fading fast. The floodlights hum into life. The scoreboard flickers: six runs needed off six balls. Out in the middle, the umpire pulls a small device from his pocket — a light meter — and checks whether it's still bright enough to play.

First ball: the batter misses, and the stumps and bails **flash with light** as the wicket is broken. The crowd erupts.

Priya, watching with her little cousin, gets the obvious question: "How do the stumps know to light up? Is there a battery inside?" There is — and a small battery can't just be connected straight to a light. Something has to control how much current flows, or the light burns out. That something is a **resistor**, and the rule it obeys is Ohm's law.

Cricket gives us the setting here, not an analogy: we'll look at the physics of the circuit directly.

## The physics

When a potential difference $V$ is applied across a conductor, a current $I$ flows through it. The **resistance** of the conductor is defined as

$$R = \frac{V}{I}$$

and is measured in ohms, where $1\,\Omega = 1\,\text{V/A}$.

**Ohm's law** states that for a metallic conductor kept at constant temperature, with other physical conditions unchanged, the current is directly proportional to the potential difference:

$$V = IR \quad \text{with } R \text{ constant}$$

Such conductors are called **ohmic**; their V–I graph is a straight line through the origin, with slope $R$ when $V$ is plotted vertically. Components whose resistance changes with current or voltage — a filament lamp, which heats up, or a diode, which conducts well in only one direction — are **non-ohmic**, and their V–I graphs are curves.

![A V–I graph: a straight blue line through the origin for a 20 ohm resistor, and a red curve bending upwards for a filament lamp](figures/ohms_law/vi-ohmic-vs-lamp.svg "Ohmic: a straight line through the origin. Non-ohmic (a filament lamp): a curve, because its resistance rises as it heats.")

The law carries the name of **Georg Simon Ohm**, a German schoolteacher who published it in 1827 after painstaking experiments with wires. His work was brushed aside at first; recognition came slowly, and in 1841 the Royal Society in London awarded him its Copley Medal. The unit of resistance is named after him.

![A black-and-white portrait of Georg Simon Ohm in a dark coat](famous/georg-simon-ohm-portrait.jpg "Georg Simon Ohm (1789–1854). Public domain, via Wikimedia Commons.")

Why is there resistance at all? The voltage creates an electric field inside the wire that pushes free electrons into a slow drift. Collisions with the vibrating atoms of the metal keep interrupting that drift. The more the collisions hinder the electrons, the larger the resistance, and the less current a given voltage can drive.

So in the bails, the resistor's job is simple: for the voltage it has across it, it sets the current to $I = V/R$.

## Worked example

**Given:** in the simplified bail circuit, the current-limiting resistor has $1.0\,\text{V}$ across it and carries $10\,\text{mA}$. Later in a long day, the battery weakens and the voltage across the resistor falls to $0.80\,\text{V}$.
**Find:** the resistance, and the new current (assume the resistor is ohmic and stays at the same temperature).

Convert first: $10\,\text{mA} = 0.010\,\text{A}$.

$$R = \frac{V}{I} = \frac{1.0}{0.010} = 100\,\Omega$$

$$I_\text{new} = \frac{V}{R} = \frac{0.80}{100} = 8.0 \times 10^{-3}\,\text{A} = 8.0\,\text{mA}$$

The current falls in proportion to the voltage, so the flash gets dimmer.

**Sanity check:** the voltage dropped to $80\%$ of its value, and so did the current ($10 \to 8.0\,\text{mA}$), as Ohm's law predicts.

## Where the picture breaks

This is a simplified circuit, not a description of any particular product's electronics. The lights in such devices are usually LEDs, which are non-ohmic — they only conduct well above a certain voltage — so Ohm's law describes the resistor in the circuit, not the LED. And the connection to cricket here is only the setting: there is no deep likeness between runs and current. For circuits, it's better to learn the physics directly than to lean on a forced comparison.

## Key takeaway

Resistance is $R = V/I$, measured in ohms. For an ohmic conductor at constant temperature, $R$ stays fixed, so current is proportional to voltage: $V = IR$. Always convert milliamperes to amperes before substituting.
