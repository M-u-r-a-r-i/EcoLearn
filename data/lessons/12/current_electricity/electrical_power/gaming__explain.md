---
concept_id: electrical_power
interest: gaming
format: explain
title: What a month of evening gaming adds to the bill
check:
  question: |-
    A $10\,\Omega$ fan and a $20\,\Omega$ fan are connected **in parallel** across the same $5\,\text{V}$ supply. Which dissipates more power?
  options:
    A: |-
      the $10\,\Omega$ fan, because at a shared voltage $P = V^2/R$ is larger for the smaller resistance
    B: |-
      the $20\,\Omega$ fan, because $P = I^2R$ is larger for the larger resistance
    C: |-
      neither — they share the same supply, so they dissipate equally
    D: |-
      the $20\,\Omega$ fan, because a larger resistance draws a larger current
  answer: A
  explanation: |-
    In parallel both fans have the same $5\,\text{V}$ across them, so the useful form is $P = V^2/R$: $25/10 = 2.5\,\text{W}$ against $25/20 = 1.25\,\text{W}$.
  misconceptions:
    B: |-
      Picks the form that matches the wrong shared quantity. $P = I^2R$ compares fairly only when the *current* is common — that is, in series. Here the voltage is common.
    C: |-
      Assumes equal voltage means equal power. Power is $VI$, so the currents matter too, and they are different.
    D: |-
      Has the current backwards. At a fixed voltage, $I = V/R$, so the larger resistance draws the *smaller* current.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A night gaming desk with a monitor showing a frame counter, a controller charging over a USB cable with current arrows, a USB power meter, and an open PC case](scenes/gaming/current_electricity.svg "The fans, the LED strip, the graphics card and the monitor are all turning electrical energy into something else, every second they are on.")

The bill arrives on a Tuesday and Devansh's mother puts it on the table without saying anything, which is worse than saying something. It is higher than last month by a noticeable amount, and the only new thing in the house is the PC he built over the holidays.

His father's theory is the LED strip inside the case, because it is the part you can actually see glowing. His younger sister's theory is the router, because it never gets switched off. Devansh's private theory is the air conditioner, but he is not going to say that out loud.

Nobody has a number. The power supply has **650 W** printed on it in large type, which sounds damning — until he borrows a plug-in socket meter and finds the whole machine drawing nothing remotely like 650 while he plays.

One appliance, three theories, one bill in rupees. How do you turn watts into money?

## The physics

**Power** is the rate at which energy is transferred. When a charge $Q$ falls through a potential difference $V$, it gives up energy $QV$; dividing by the time gives

$$P = VI$$

with $P$ in watts (W), $V$ in volts and $I$ in amperes. This form is completely general — it works for a motor, a lamp, a charging cell, anything.

For a component that obeys $V = IR$, substitute and you get two more forms of the same statement:

$$P = VI = I^2R = \frac{V^2}{R}$$

![Three ways of writing electrical power — as VI, as I squared R, and as V squared over R — shown on one resistor](figures/electrical_power/power-three-forms.svg "All three are the same physics; choose the one whose quantities you actually know and that stay fixed in the comparison you are making.")

Choosing between them is where marks are won. Use $I^2R$ when the **current** is the shared quantity (components in series): the bigger resistance then gets hotter. Use $V^2/R$ when the **voltage** is shared (components in parallel): now the *smaller* resistance gets hotter. Both are right; picking the wrong one for the situation is the usual mistake.

The $I^2R$ form also names the villain of the previous lesson: a cable's own resistance turns some of the energy into heat on the way, and that loss grows as the *square* of the current.

**Energy.** Over a time $t$ at steady power, the energy transferred is

$$E = Pt$$

in joules when $P$ is in watts and $t$ in seconds. Electricity bills use a bigger unit: the **kilowatt-hour**, one kilowatt for one hour, which is the "unit" on your bill.

$$1\,\text{kW\,h} = 1000\,\text{W} \times 3600\,\text{s} = 3.6 \times 10^{6}\,\text{J}$$

And the "650 W" on the power supply is a **maximum**, not a consumption: it says what the supply can deliver if everything inside demands it at once, which while playing it does not.

## Worked example

**Given:** Devansh's meter shows the PC and monitor together drawing about $250\,\text{W}$ while he plays (illustrative), and he plays about $4$ hours a day. Take electricity at 8 rupees per unit — tariffs vary by state.
**Find:** the energy used in a month and what it costs.

Work in kilowatts, because that is the language of the bill: $250\,\text{W} = 0.25\,\text{kW}$.

$$E = Pt = 0.25\,\text{kW} \times 4\,\text{h} = 1\,\text{kW\,h}$$

Exactly one unit a day — a tidy number worth remembering.

Over a 30-day month that is 30 units, and at 8 rupees a unit, about **240 rupees a month**.

**Sanity check:** a ceiling fan is around 75 W, so the whole setup is about three fans running — real, but not the reason a bill jumps. An air conditioner is nearer 1500 W, twenty fans, and it would add that much in a couple of evenings.

## Where the picture breaks

The worked example treats the draw as a steady 250 W, and it is nothing of the kind. A PC's consumption swings second by second with what the graphics card is being asked to do, drops to a trickle at a menu, and is not zero when "off" if it is only sleeping. The 250 W is an average, and the honest way to get one is to read a meter over a long session rather than trust any printed rating.

Two more cautions. The socket meter reads what the wall supplies, which is more than the components receive, because the power supply itself wastes some as heat. And $P = I^2R$ and $P = V^2/R$ are shortcuts that assume $V = IR$; for a motor, a charging battery or an LED, only $P = VI$ survives, because those devices are not simple resistors.

## Key takeaway

Electrical power is $P = VI$ always, and $P = I^2R = V^2/R$ for anything obeying Ohm's law — use $I^2R$ when the current is shared and $V^2/R$ when the voltage is shared. Energy is $E = Pt$, billed in kilowatt-hours, where one unit is $3.6 \times 10^6\,\text{J}$. A rating printed on a device is a ceiling, not a bill.
