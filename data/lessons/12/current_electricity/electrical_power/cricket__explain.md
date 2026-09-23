---
concept_id: electrical_power
interest: cricket
format: explain
title: What an evening under the practice lights actually costs
check:
  question: |-
    A heating element of constant resistance is marked $100\,\text{W}$ at $230\,\text{V}$. It is connected instead to a $115\,\text{V}$ supply — exactly half the voltage. The power it now dissipates is about:
  options:
    A: |-
      $100\,\text{W}$ — the marking is the element's fixed power
    B: |-
      $50\,\text{W}$
    C: |-
      $200\,\text{W}$
    D: |-
      $25\,\text{W}$
  answer: D
  explanation: |-
    With $R$ constant, $P = V^2/R$, so power goes as the *square* of the voltage. Half the voltage gives a quarter of the power: $100/4 = 25\,\text{W}$.
  misconceptions:
    A: |-
      Reads the wattage as a property of the device alone. A wattage marking is only valid at its marked voltage; what the device really fixes is its resistance.
    B: |-
      Takes power as proportional to voltage. Halving $V$ also halves the current, and power is their product — so it falls twice over.
    C: |-
      Inverts the relationship, as if a lower voltage made a device draw more power to compensate. Nothing in the circuit forces the power to stay up.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A cricket ground at dusk with floodlights, an electronic scoreboard, glowing stumps and an umpire holding a light meter](scenes/cricket/current_electricity.svg "Four lamps, three hours of practice, one electricity bill at the end of the month.")

The club committee has a problem, and it arrives in an envelope. Since the four new practice lights went up, the monthly electricity bill has gone from comfortable to alarming, and someone at the meeting says the words that end most committee meetings: "We'll have to cut the evening sessions."

Farhan, who coaches the under-17s, refuses to accept it without a number. He climbs the stand with a torch and reads the plate riveted to one lamp housing: **400 W, 230 V**.

Divya, keeping the minutes, has just done this chapter at school. "Four hundred watts," she says. "Four lamps. Five hours a week. I can tell you the rupees before we vote."

The committee goes quiet. One number on a metal plate, and she claims she can predict a bill. What does that plate actually tell you — and how does it turn into money?

## The physics

When a charge $Q$ falls through a potential difference $V$, it loses energy $QV$. In a conductor carrying a steady current, charge arrives at the rate $I$, so energy is delivered at the rate

$$P = VI$$

This is **electrical power**, measured in watts ($1\,\text{W} = 1\,\text{J/s}$). It is true for *any* device — a lamp, a motor, a phone charger.

![A resistor with current I through it and potential difference V across it, and the three equivalent expressions for the power it dissipates](figures/electrical_power/power-three-forms.svg "P = VI always holds; the other two come from substituting Ohm's law, so they apply to a resistor.")

If the device is a **resistor** obeying $V = IR$, substitute to get two more forms:

$$P = I^2R \qquad \text{and} \qquad P = \frac{V^2}{R}$$

All three give the same number for a resistor; you pick whichever matches what you know. When the current is fixed — for components in series — $P = I^2R$ shows that the biggest resistance gets hottest. When the voltage is fixed — for things plugged into the same mains — $P = V^2/R$ shows that the *smallest* resistance draws the most power. That reversal catches people out, and it is worth pausing on: which formula is convenient depends on what the circuit holds constant.

In a resistor this energy leaves as heat: **Joule heating**, $H = I^2Rt$.

Finally, energy is power multiplied by time, $E = Pt$. Electricity bills measure it in **kilowatt-hours**: one kilowatt for one hour, so

$$1\,\text{kW\,h} = 1000\,\text{W} \times 3600\,\text{s} = 3.6 \times 10^6\,\text{J}$$

A "unit" on an Indian bill is one kilowatt-hour.

## Worked example

**Given:** one practice lamp marked $400\,\text{W}$, run for $5$ hours in a week, with electricity charged at 8 rupees per unit (illustrative — tariffs vary by state).
**Find:** the energy used and what it costs.

Work in kilowatts, because that is what the bill speaks: $400\,\text{W} = 0.4\,\text{kW}$.

$$E = Pt = 0.4\,\text{kW} \times 5\,\text{h} = 2\,\text{kW\,h}$$

Two units — that is the whole physics answer; the rest is arithmetic. At 8 rupees a unit, one lamp costs 16 rupees a week, and four lamps cost 64 rupees a week, or roughly 260 rupees a month.

**Sanity check:** a lamp of a few hundred watts run for a few hours is a couple of units — about what a ceiling fan uses in a week. The club's alarming bill is not coming from the practice lights.

For interest, the current each lamp draws is $I = P/V = 400/230 \approx 1.7\,\text{A}$, comfortably inside a normal $6\,\text{A}$ socket.

## Where the picture breaks

The lamps are real circuits, not an analogy for anything in the game — no part of cricket behaves like power dissipation, and inventing one would mislead you. The idealisations are elsewhere. A "400 W" rating assumes the supply really is at $230\,\text{V}$; Indian mains sags and swells, and power follows the square of the voltage, so a 10% sag costs about 19% of the light. LED lamps are also not simple resistors — their electronics keep the power roughly constant instead of following $V^2/R$, so use $P = VI$ for them and keep $I^2R$ for the cables. And the plate tells you electrical power in, not light out.

## Key takeaway

Electrical power is $P = VI$, and for a resistor also $P = I^2R = V^2/R$ — the same quantity, chosen to fit what is fixed. Energy is $E = Pt$, billed in kilowatt-hours, where $1\,\text{kW\,h} = 3.6 \times 10^6\,\text{J}$. A device's wattage marking only applies at its marked voltage; what the device really owns is its resistance.
