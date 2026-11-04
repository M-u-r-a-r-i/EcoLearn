---
concept_id: ohms_law
interest: cricket
format: misconception
title: Does doubling the voltage double a resistor's resistance
check:
  question: |-
    A technician tests a scoreboard resistor: $2.0\,\text{V}$ across it gives $10\,\text{mA}$. She raises the voltage to $4.0\,\text{V}$, keeping it at the same temperature. The resistance is now:
  options:
    A: |-
      $400\,\Omega$ — doubling $V$ doubles $R$, since $R = V/I$
    B: |-
      $100\,\Omega$ — the resistance halves to let more current through
    C: |-
      $200\,\Omega$ — unchanged
    D: |-
      $0.20\,\Omega$
  answer: C
  explanation: |-
    $R = 2.0/0.010 = 200\,\Omega$. For an ohmic resistor at constant temperature, doubling $V$ doubles $I$ to $20\,\text{mA}$, and $R = 4.0/0.020$ is still $200\,\Omega$.
  misconceptions:
    A: |-
      Reads $R = V/I$ as "resistance is caused by voltage", forgetting that the current doubles too.
    B: |-
      Thinks a resistor changes its own resistance to suit the circuit; an ohmic resistor's value is set by its material, dimensions and temperature.
    D: |-
      Divides $2.0$ by $10$ without converting milliamperes to amperes — a unit slip, 1000 times too small.
author: claude-code/opus-5
written: 2026-09-21
---
## The story

![A cricket ground at dusk with an electronic scoreboard, floodlights and glowing stumps](scenes/cricket/current_electricity.svg "Between innings, a small argument about a big formula.")

It's the innings break, and Nandini, the ground's technician, is testing a resistor from the scoreboard on her workbench beside the pavilion. Her nephew Arjun, a Class 12 student, is helping — or trying to.

Nandini sets the power supply to $2.0\,\text{V}$ and notes the current. Then she turns it up to $4.0\,\text{V}$. Arjun glances at her clipboard, where she has written $R = V/I$, and announces: "Easy. You doubled $V$, so you've doubled the resistance. It's right there in the formula."

Nandini hands him the meter. "Then tell me what current you expect to see." Arjun hesitates. If the resistance doubled *and* the voltage doubled, what would the current do? Something about his confident answer is starting to feel wrong.

## The common belief

Between innings, a technician checks a resistor from the scoreboard's lighting circuit. A student helping out looks at the formula on her clipboard, $R = V/I$, and says: "So if you double the voltage, you double the resistance. More voltage, more resistance — it's right there in the formula."

## Why it feels right

The formula really does have $V$ on top. If you picture changing only $V$ and leaving $I$ alone, $R$ would double. Students meet many formulas where one quantity really does depend on another in exactly this way, so reading the equation as "this causes that" is a natural habit. And there *are* components whose resistance changes with conditions — a filament lamp's resistance rises as it heats — so resistance changing isn't an absurd idea.

## What actually happens

When the technician doubles the voltage, the current doubles too. The ratio $V/I$ — the resistance — stays exactly the same.

$R = V/I$ is a **definition**: it tells you how to *measure* resistance from a voltage and a current. It doesn't say that voltage *causes* resistance. What decides a resistor's resistance is what it's made of, its length and thickness, and its temperature. Change the voltage across an ohmic resistor, and the current simply follows in proportion, leaving $R$ untouched.

The formula has three quantities, but in an ohmic resistor they aren't free to change independently: $R$ is fixed, and $V$ and $I$ rise and fall together.

## The physics

The resistance of a conductor is defined as $R = V/I$. **Ohm's law** states that for a metallic conductor at constant temperature and other unchanged physical conditions, the current is proportional to the potential difference, so

$$V = IR \quad \text{with } R \text{ constant}$$

That is precisely what the student missed: for an ohmic conductor, $R$ is the constant in the relation, not one of the variables. The V–I graph is a straight line through the origin, and its slope — the resistance — is the same at every point.

![A V–I graph: a straight blue line through the origin for a 20 ohm resistor, and a red curve bending upwards for a filament lamp](figures/ohms_law/vi-ohmic-vs-lamp.svg "The blue line is an ohmic resistor: double V and I doubles too, so the slope V/I — the resistance — never changes. Only the lamp's curve shows resistance changing, and that is because it heats up.")

Where resistance *does* change (a filament lamp heating up, for example), it's because the conditions changed, typically the temperature — and the component is then non-ohmic.

## Worked example

The technician's readings for the resistor, at constant temperature:

| $V$ | $2.0\,\text{V}$ | $4.0\,\text{V}$ | $6.0\,\text{V}$ |
|---|---|---|---|
| $I$ | $10\,\text{mA}$ | $20\,\text{mA}$ | $30\,\text{mA}$ |

$$R = \frac{2.0}{0.010} = \frac{4.0}{0.020} = \frac{6.0}{0.030} = 200\,\Omega$$

Every doubling or tripling of $V$ is matched by the same change in $I$, so $R$ stays at $200\,\Omega$. If the student's idea were right, the resistance at $6.0\,\text{V}$ would be $600\,\Omega$ and the current would have stayed at $10\,\text{mA}$ — which is not what the meter shows.

## Key takeaway

$R = V/I$ defines resistance; it doesn't mean voltage causes resistance. For an ohmic conductor at constant temperature, $R$ is fixed by the material, its dimensions and its temperature — change $V$ and $I$ changes in proportion, leaving $R$ the same.
