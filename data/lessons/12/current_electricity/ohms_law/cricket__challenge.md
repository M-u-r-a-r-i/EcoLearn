---
concept_id: ohms_law
interest: cricket
format: challenge
title: Which scoreboard resistor draws more current
check:
  question: |-
    A resistor in an umpire's light meter carries $30\,\text{mA}$ when $6.0\,\text{V}$ is across it. It is ohmic and stays at the same temperature. What voltage across it gives a current of $45\,\text{mA}$?
  options:
    A: |-
      $4.0\,\text{V}$
    B: |-
      $9.0\,\text{V}$
    C: |-
      $13.5\,\text{V}$
    D: |-
      $6.0\,\text{V}$ — the resistor adjusts itself to let more current through
  answer: B
  explanation: |-
    $R = 6.0/0.030 = 200\,\Omega$, which stays constant. For $45\,\text{mA}$: $V = IR = 0.045 \times 200 = 9.0\,\text{V}$. Current and voltage rise in proportion.
  misconceptions:
    A: |-
      Treats current and voltage as inversely related, so more current seems to need less voltage.
    C: |-
      Squares the current ratio ($6.0 \times 1.5^2$), as if voltage depended on the square of the current.
    D: |-
      Thinks the current can change on its own at the same voltage; for an ohmic conductor, a different current requires a different voltage.
author: claude-code/opus-5
written: 2026-09-21
---
## The story

![A cricket ground at dusk with an electronic scoreboard and floodlights](scenes/cricket/current_electricity.svg "Two hours to the toss, and the scoreboard is flickering.")

Two hours before a big local match, the ground's old scoreboard starts misbehaving: two indicator lights keep flickering. Mr. Pillai, the ground's electrician, climbs up with his toolbox. Inside, each light is protected by a resistor, and two of them have burnt out.

His apprentice, Faiz, hands him the only spares in the box. One is marked $200\,\Omega$, the other $400\,\Omega$. "Take the $400$," Faiz says confidently. "Bigger resistor, bigger number — it'll let more current through and make the light brighter."

Mr. Pillai just raises an eyebrow and hands Faiz a pencil. "Work it out first," he says. "The supply is $12\,\text{V}$." Is Faiz right?

## The challenge

A stadium's old electronic scoreboard has indicator lights, each protected by a resistor. A technician tests two of those resistors, one at a time, on the same $12\,\text{V}$ supply:

- resistor P: $200\,\Omega$
- resistor Q: $400\,\Omega$

Which one draws more current, and by how much? Then a design question: what resistance would limit the current to exactly $40\,\text{mA}$ on this supply?

## Think first

Q has the bigger number. Does a "bigger" resistor pull more current, or less? Twice as much? Half? And for the design question — do you need more resistance or less than P to get a smaller current than P gives? Decide before reading on.

## The reveal

Both resistors have the same voltage across them, so use Ohm's law in the form $I = V/R$:

$$I_P = \frac{12}{200} = 0.060\,\text{A} = 60\,\text{mA}, \qquad I_Q = \frac{12}{400} = 0.030\,\text{A} = 30\,\text{mA}$$

Resistor **P** draws more — twice as much. A larger resistance opposes the drift of charge more strongly, so for the same voltage it lets **less** current through. Current is inversely proportional to resistance when the voltage is fixed.

For the design question, rearrange Ohm's law for $R$:

$$R = \frac{V}{I} = \frac{12}{0.040} = 300\,\Omega$$

Sensibly, $300\,\Omega$ sits between P and Q, and so does its current: $40\,\text{mA}$ lies between $60\,\text{mA}$ and $30\,\text{mA}$.

## The physics

The resistance of a conductor is defined as $R = V/I$. **Ohm's law** says that for a metallic conductor at constant temperature, $R$ is constant, so

$$V = IR$$

Read the same law three ways, depending on what's held fixed:

- same resistor, more voltage → proportionally more current ($I \propto V$);
- same voltage, more resistance → proportionally less current ($I \propto 1/R$);
- to get a chosen current from a known voltage, pick $R = V/I$.

![A V–I graph: a straight blue line through the origin for a 20 ohm resistor, and a red curve bending upwards for a filament lamp](figures/ohms_law/vi-ohmic-vs-lamp.svg "A resistor's V–I graph is a straight line through the origin; its slope is the resistance. A steeper line means more resistance and less current for the same voltage.")

It applies to ohmic conductors only — straight-line V–I graphs through the origin. It doesn't hold for a filament lamp as it heats up, or for a diode.

## Key takeaway

For the same voltage, current is inversely proportional to resistance: double the resistance, half the current. Ohm's law, $V = IR$, lets you find any one of $V$, $I$ and $R$ from the other two — for an ohmic conductor at constant temperature.
