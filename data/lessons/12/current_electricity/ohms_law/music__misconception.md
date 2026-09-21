---
concept_id: ohms_law
interest: music
format: misconception
title: Does a long guitar cable use up current
check:
  question: |-
    A $9.0\,\text{V}$ battery in an effects pedal drives current through a $3.0\,\text{k}\Omega$ resistor. An ammeter just before the resistor reads the current going in. Just after the resistor, the current is:
  options:
    A: |-
      The same, $3.0\,\text{mA}$
    B: |-
      Less than $3.0\,\text{mA}$, because the resistor uses some of it up
    C: |-
      Zero, because the resistor absorbs the current
    D: |-
      More than $3.0\,\text{mA}$, because the electrons speed up after squeezing through
  answer: A
  explanation: |-
    Charge is not used up, so the current is the same on both sides: $I = V/R = 9.0/3000 = 3.0\,\text{mA}$. What the resistor takes is energy — the potential drops across it.
  misconceptions:
    B: |-
      Believes current is consumed by a resistor; in fact charge flows through unchanged, and energy is what is transferred.
    C: |-
      Believes a resistor absorbs current entirely, which would leave nothing to complete the circuit.
    D: |-
      Pictures a resistor as a nozzle that speeds up the flow; the current is the same everywhere in a single loop.
author: claude-code/opus-5
written: 2026-09-21
---
## The story

![A guitar plugged through an effects pedal into an amplifier with long cables](scenes/music/current_electricity.svg "A new 10-metre cable, and a theory about where the current went.")

Aditya finally gets to play on a real stage, so he buys a brand-new 10-metre guitar cable to roam around while he plays. At rehearsal, something sounds off to him — a little duller, a little less sparkly than at home with his short cable.

His bandmate Riya has a theory ready. "It's obvious. A long cable has more resistance, so it *uses up* more of the current. By the time the current gets to the amp, there's less of it left."

It sounds reasonable. Aditya nods. But their music teacher, overhearing, smiles and asks one question: "If current gets used up along the way, where do the used-up electrons go?"

Nobody has an answer. Do you?

## The common belief

A guitarist complains that their new 10-metre cable makes the tone dull. "It's the resistance," they say. "A long cable uses up the current, so less of it reaches the amp."

The picture here is that current is like petrol: a resistor, or a long wire, burns some of it, so less comes out of the far end than went in.

## Why it feels right

Something really is lost in a resistor: it gets warm. A long cable does change the signal in real rigs. And the word "consume" is everywhere — we talk about appliances "using electricity". It's natural to think the thing being used up is the current itself.

## What actually happens

The current coming out of a resistor is **exactly the same** as the current going in. Charge is conserved: electrons cannot vanish inside the wire, and they don't pile up either. In a single loop, the same current flows through every part of the circuit at once.

![A circuit: a 9 volt cell, a 1.8 kilo-ohm resistor, and ammeters before and after the resistor both reading 5.0 milliamperes, with a voltmeter across the resistor reading 9.0 volts](figures/ohms_law/series-circuit-same-current.svg "Ammeters on both sides of the resistor read the same current. What drops across the resistor is the voltage.")

What a resistor does is set **how much** current flows in the whole loop, and take **energy** from the charges passing through it. The charges come out with the same flow rate but at a lower electric potential — that drop in potential, $V = IR$, is the energy per unit charge that became heat.

So the petrol picture is wrong about what gets used up. It's not the charge; it's the energy the charge carries. (The long cable's duller tone comes mainly from its capacitance cutting the high frequencies — an AC effect you'll meet later — not from current disappearing.)

## The physics

The resistance of a conductor is defined as $R = V/I$, and **Ohm's law** says that for a metallic conductor at constant temperature $R$ is constant, so

$$V = IR$$

Here $V$ is the potential difference **across** the resistor — the drop in potential from one end to the other — and $I$ is the current **through** it. Both ends carry the same $I$.

The misconception treats $I$ as something that drops across a resistor. It is $V$ that drops; $I$ is the same going in as coming out.

## Worked example

A $9.0\,\text{V}$ pedal battery drives current through a single $1.8\,\text{k}\Omega$ resistor (ignore the battery's internal resistance). Find the current entering and leaving the resistor, and the potential at each end if the battery's negative terminal is at $0\,\text{V}$.

$$I = \frac{V}{R} = \frac{9.0}{1800} = 5.0 \times 10^{-3}\,\text{A} = 5.0\,\text{mA}$$

The current is $5.0\,\text{mA}$ going in **and** $5.0\,\text{mA}$ coming out. The end connected to the positive terminal is at $9.0\,\text{V}$, the other end at $0\,\text{V}$: the full $9.0\,\text{V}$ drops across the resistor. The charge keeps flowing; its potential energy is what's spent.

## Key takeaway

A resistor doesn't use up current. The same current flows in and out; what drops across the resistor is the potential, $V = IR$, and what it takes is energy. Resistance sets how large the current is around the whole loop.
