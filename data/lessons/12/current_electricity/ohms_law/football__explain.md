---
concept_id: ohms_law
interest: football
format: explain
title: The homemade scoreboard that killed its own lights
check:
  question: |-
    A resistor in a homemade scoreboard has $6.0\,\text{V}$ across it and carries $30\,\text{mA}$. What is its resistance?
  options:
    A: |-
      $0.20\,\Omega$
    B: |-
      $0.18\,\Omega$
    C: |-
      $200\,\Omega$
    D: |-
      $5.0\,\Omega$
  answer: C
  explanation: |-
    Convert the current first: $30\,\text{mA} = 0.030\,\text{A}$. Then $R = V/I = 6.0/0.030 = 200\,\Omega$.
  misconceptions:
    A: |-
      Divides $6.0$ by $30$ without converting milliamperes to amperes — a unit slip that makes the answer $1000$ times too small.
    B: |-
      Multiplies voltage by current instead of dividing. $V \times I$ is the power in watts, not the resistance.
    D: |-
      Inverts the definition and computes $I/V$ (in milliamperes at that). Resistance is volts per ampere, not amperes per volt.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A floodlit football ground at night with two lit pylons, an electronic scoreboard, a fourth official holding a glowing LED substitution board, and a pitch-side distribution box with cables running to the lights](scenes/football/current_electricity.svg "The big board runs on mains; the one Meera built runs on a nine-volt battery.")

The school five-a-side tournament needed a scoreboard, and nobody had one, so Meera built it — a plywood panel, two digits made of LEDs, a nine-volt battery taped to the back.

She soldered the first LED straight across the battery terminals. It lit beautifully, for about a second, and then went a dull grey and stayed that way. She tried a second LED. Same thing: bright, then dead.

Her brother's friend Joel, who repairs inverters, looked at the panel and laughed. "You've given it nothing to push against," he said, and dropped a tiny striped cylinder into her palm. "Put one of these in the wire with each LED."

Meera was annoyed. The battery is nine volts whatever she does. The LED either works or it doesn't. How can adding something *in the way* be what makes the lamp survive?

## The physics

When a potential difference $V$ is applied across a conductor, a current $I$ flows through it. The **resistance** of the conductor is defined as

$$R = \frac{V}{I}$$

measured in ohms, where $1\,\Omega = 1\,\text{V/A}$.

**Ohm's law** states that for a metallic conductor at constant temperature, with its other physical conditions unchanged, the current through it is directly proportional to the potential difference across it:

$$V = IR \quad \text{with } R \text{ constant}$$

Conductors that obey this are called **ohmic**, and their V–I graph is a straight line through the origin. Components whose resistance changes with current or voltage — a filament lamp, which heats up, or an LED, which barely conducts below a certain voltage and then conducts hard — are **non-ohmic**, and their V–I graphs bend.

![A V–I graph with a straight line through the origin for a resistor and an upward-bending curve for a filament lamp](figures/ohms_law/vi-ohmic-vs-lamp.svg "Ohmic: a straight line through the origin. Non-ohmic: a curve, because the component's resistance is not a fixed number.")

That bend is exactly Meera's problem. An LED connected straight across a battery sits on the steep part of its curve, where a small extra voltage lets a large current through — far more than the tiny chip can survive. It does not limit itself.

The resistor does the limiting. Put it in **series** with the LED and the same current must pass through both, because there is only one path for charge to take.

![A circuit loop with a cell and a resistor, and ammeters before and after the resistor reading the same current](figures/ohms_law/series-circuit-same-current.svg "In a single loop the current is the same everywhere — a resistor does not use current up, it sets how much flows.")

So the resistor's own $R = V/I$ fixes the current for the whole loop, and the LED gets whatever that is.

Ohm's law carries the name of **Georg Simon Ohm**, a German schoolteacher who published it in 1827 after years of careful work with wires. It was dismissed at first; recognition came slowly, and the Royal Society awarded him its Copley Medal in 1841.

![A black-and-white portrait of Georg Simon Ohm in a dark coat](famous/georg-simon-ohm-portrait.jpg "Georg Simon Ohm (1789–1854). Public domain, via Wikimedia Commons.")

## Worked example

**Given:** a $9.0\,\text{V}$ battery, an LED that needs $20\,\text{mA}$ and holds about $2.0\,\text{V}$ across itself when it is lit.
**Find:** the resistor Meera should put in series with it.

Start with the voltage, because the loop has to share it out. The battery offers $9.0\,\text{V}$ and the LED takes $2.0\,\text{V}$ of that, so the resistor is left with

$$V_R = 9.0 - 2.0 = 7.0\,\text{V}$$

Seven volts is the resistor's job: it must swallow that much while letting only the wanted current through.

Now convert the current, $20\,\text{mA} = 0.020\,\text{A}$, and use the definition:

$$R = \frac{V_R}{I} = \frac{7.0}{0.020} = 350\,\Omega$$

**Sanity check:** a few hundred ohms is the size of resistor you find in any hobby kit — if the answer had come out as a fraction of an ohm, the milliamperes would not have been converted.

## Where the picture breaks

Football is only the setting here; a scoreboard is not an analogy for anything on the pitch, and there is no useful likeness between goals and current. Inside the circuit, the honest limit is this: Ohm's law describes the **resistor**, not the LED. The LED's "$2.0\,\text{V}$" is not a resistance at all — it is roughly the voltage at which that colour of LED starts conducting, and it barely shifts as the current changes, so you cannot write $R = V/I$ for it and expect a constant. Even the resistor is only ohmic while its temperature holds steady; drive it hard enough to get warm and its resistance creeps up.

## Key takeaway

Resistance is defined as $R = V/I$ and measured in ohms. For an ohmic conductor at constant temperature $R$ is constant, so $V = IR$ and the V–I graph is a straight line through the origin; non-ohmic components like lamps and LEDs give curves. A series resistor does not use current up — it decides how much flows. Always convert milliamperes to amperes before substituting.
