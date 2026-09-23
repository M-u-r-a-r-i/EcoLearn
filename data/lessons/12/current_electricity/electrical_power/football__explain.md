---
concept_id: electrical_power
interest: football
format: explain
title: The bill that arrived after a month of evening training
check:
  question: |-
    A heating element of resistance $20\,\Omega$ carries a current of $3.0\,\text{A}$. The power it dissipates is:
  options:
    A: |-
      $9.0\,\text{W}$
    B: |-
      $180\,\text{W}$
    C: |-
      $60\,\text{W}$
    D: |-
      $0.45\,\text{W}$
  answer: B
  explanation: |-
    With the current and the resistance known, use $P = I^2R = (3.0)^2 \times 20 = 180\,\text{W}$.
  misconceptions:
    A: |-
      Squares the current and stops there. $I^2$ on its own is not a power — the resistance still has to multiply it.
    C: |-
      Computes $IR$, which is the potential difference across the element in volts, not its power in watts.
    D: |-
      Uses $I^2/R$, dividing by the resistance instead of multiplying. Dividing by $R$ belongs to the *voltage* form, $P = V^2/R$.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A floodlit football ground at night with two lit pylons, an electronic scoreboard, a fourth official holding a glowing LED substitution board, and a pitch-side distribution box with cables running to the lights](scenes/football/current_electricity.svg "Four pylons, a scoreboard and a changing-room geyser — and one meter counting for all of them.")

The club moved training to evenings in November, because nobody could face the afternoon heat. In December the electricity bill arrived and the treasurer, Mr Mathew, put it face-down on the table before he would let anyone speak.

"The floodlights," he said. "We cannot afford the floodlights."

The coach disagreed, loudly. The lamps are the new LED kind. The real thief, he said, is the water geyser in the changing room, which somebody switches on at five and nobody ever switches off.

Neeti, who is in Class 12 and keeps the accounts book because her handwriting is neat, points out that they are arguing about the wrong thing. Everyone is comparing how *bright* or how *hot* something is. But the bill is not charging them for brightness, and it is not charging them for watts either.

The meter has been counting something else entirely. What?

## The physics

When a charge $Q$ falls through a potential difference $V$, it gives up energy $QV$. Divide by the time taken, and since $I = Q/t$, the rate at which the device converts electrical energy is

$$P = VI$$

measured in watts, where $1\,\text{W} = 1\,\text{J/s}$. This form is completely general: it applies to any device across which there is a pd $V$ carrying a current $I$.

If the device is a **resistor**, Ohm's law lets you rewrite it. Substituting $V = IR$ gives $P = I^2R$; substituting $I = V/R$ gives $P = V^2/R$:

$$P = VI = I^2R = \frac{V^2}{R}$$

![A resistor with current I through it and potential difference V across it, and the three equivalent expressions for the power it dissipates](figures/electrical_power/power-three-forms.svg "P = VI always holds; the other two forms come from substituting Ohm's law, so they are for a resistor.")

Pick whichever form matches what you were given. The two resistor forms also say something useful: at a *fixed current*, a bigger resistance wastes more ($I^2R$) — which is why a long thin extension lead gets warm. At a *fixed voltage*, a bigger resistance draws less ($V^2/R$).

**Energy.** Power is a rate; energy is the rate multiplied by the time:

$$E = Pt$$

In joules, if $P$ is in watts and $t$ in seconds. But an electricity meter does not count joules — it counts **kilowatt-hours**, the energy used by a $1\,\text{kW}$ device in one hour. One unit on the bill is one kilowatt-hour, and

$$1\,\text{kW\,h} = 1000\,\text{W} \times 3600\,\text{s} = 3.6 \times 10^{6}\,\text{J}$$

That is Neeti's point. The bill charges for **energy**, so a device's rating in watts is only half the story — the hours matter just as much. A quiet $2\,\text{kW}$ geyser left on all evening can beat lamps that look far more impressive.

## Worked example

**Given:** the club's lamps come to $2\,\text{kW}$ in total, and they are on for $3$ hours a night, $20$ nights in the month. Electricity costs ₹8 per unit.
**Find:** the month's lighting bill.

Take one night first, and keep the power in kilowatts and the time in hours — that way the answer lands straight in the units the meter uses:

$$E_\text{night} = P\,t = 2 \times 3 = 6\,\text{kW\,h}$$

Six units a night. Now the month:

$$E = 6 \times 20 = 120\,\text{kW\,h}$$

At ₹8 a unit, that is $120 \times 8 = $ ₹960 for the month's floodlighting — about ₹48 a night to light the whole pitch.

**Sanity check:** a thousand rupees a month to light a pitch four nights a week is believable; a few rupees, or a lakh, would have meant a slip in the units.

## Where the picture breaks

Football is the setting, not an analogy — there is nothing on the pitch that behaves like power. The physics idealisations are in the numbers: "$2\,\text{kW}$ of lamps" is the rating, and a real lamp draws its rated power only at its rated voltage, so a sagging mains supply changes it. The three formulas are also not interchangeable for everything. $P = VI$ always works, but $P = I^2R$ and $P = V^2/R$ assume the device is an ohmic resistor. For a motor or an LED driver, most of the energy leaves as motion or light rather than heat, and there is no single $R$ to put in the formula.

## Key takeaway

Electrical power is $P = VI$, which becomes $I^2R$ or $V^2/R$ for a resistor. Energy is $E = Pt$, and the electricity meter counts it in kilowatt-hours, where $1\,\text{kW\,h} = 3.6 \times 10^6\,\text{J}$. A device's bill depends on its power *and* on how long it is left on.
