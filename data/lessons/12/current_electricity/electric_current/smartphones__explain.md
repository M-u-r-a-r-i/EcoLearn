---
concept_id: electric_current
interest: smartphones
format: explain
title: What the milliamp-hours on a power bank are counting
check:
  question: |-
    A phone charger delivers a steady $2.0\,\text{A}$ through its cable. How much charge passes any cross-section of the cable in $5$ minutes?
  options:
    A: |-
      $10\,\text{C}$
    B: |-
      $600\,\text{C}$
    C: |-
      $150\,\text{C}$
    D: |-
      $2.0\,\text{C}$
  answer: B
  explanation: |-
    Current is charge per second, so $Q = It$ with the time in seconds: $5$ minutes is $300\,\text{s}$, and $Q = 2.0 \times 300 = 600\,\text{C}$.
  misconceptions:
    A: |-
      Multiplies by the time in minutes instead of seconds. An ampere is a coulomb per *second*, so the time must be converted to seconds before substituting.
    C: |-
      Divides the time by the current, $Q = t/I$. Rearranging $I = Q/t$ gives $Q = It$: more current or more time both mean more charge.
    D: |-
      Treats the current as if it were the charge itself. Two amperes is a *rate* — two coulombs every second — so the total keeps growing for as long as the charger runs.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A charging corner: a phone on a wall charger, a power bank charging an earbuds case through a small USB meter, and a smartwatch on its charging puck, with current arrows on the cables](scenes/smartphones/current_electricity.svg "Every cable here carries a current — and the arrows drawn on the cables point the opposite way to the electrons inside them.")

The overnight train to Chennai has one working socket per compartment, and Meera has claimed it. Her phone is on the wall charger; her power bank sits in her lap, charging her brother's earbuds.

Her brother Nikhil is reading the power bank's label with a torch. "Ten thousand mAh," he announces. "Milli-amp-hours. What is that even measuring? It's not volts, it's not watts."

"It's how much electricity is in it," says Meera.

"Then why is an *amp* in it? Amps are what the charger says — two amps. You can't store a speed."

He has a point. Between them there is a tiny USB meter, plugged into the earbuds' cable, flickering $0.5\,\text{A}$. Something is flowing, at a rate, through that cable. What exactly is flowing — and which way is it going?

## The physics

The copper inside a charging cable is already full of **free electrons** darting about at random in every direction. That random motion is not a current: as many cross any point one way as the other. A current exists only when there is a *net* flow of charge past a point.

**Electric current** is the rate of flow of charge:

$$I = \frac{Q}{t}$$

where $Q$ is the charge, in coulombs (C), crossing a chosen cross-section in time $t$, in seconds. The unit is the **ampere**: $1\,\text{A} = 1\,\text{C/s}$. If the flow is not steady, the current at an instant is $I = \dfrac{dQ}{dt}$.

![A wire with a marked cross-section: electrons drift one way while the conventional current arrow points the other](figures/electric_current/current-as-charge-flow.svg "Choose one cross-section and count the net charge crossing it each second — that count is the current.")

So Nikhil's instinct was right: an ampere is a rate, like a speed. And an ampere multiplied by a time is no longer a rate — it is an amount of charge. That is what a **milliamp-hour** is: the charge delivered by $1\,\text{mA}$ flowing for one hour, $0.001\,\text{A} \times 3600\,\text{s} = 3.6\,\text{C}$. The label on the power bank is a charge rating.

Current is a **scalar**, even though we draw it with an arrow. The arrow shows the **conventional direction**: the way *positive* charge would flow — out of the source's positive terminal, through the device, and back to the negative terminal. In copper the carriers are electrons, which are negative, so they drift the *opposite* way. The convention was fixed before the electron was discovered, and every circuit rule is written for it.

## Worked example

**Given:** Meera's phone draws a steady $I = 2.0\,\text{A}$ from the wall charger for half an hour.
**Find:** the charge that passes through the cable, in coulombs and in mAh.

Half an hour is $t = 30 \times 60 = 1800\,\text{s}$.

$$Q = It = 2.0\,\text{A} \times 1800\,\text{s} = 3600\,\text{C}$$

Three thousand six hundred coulombs of charge have gone round the circuit — and not a single one was used up; they all came back to the charger.

Now in the label's unit. One mAh is $3.6\,\text{C}$, so

$$Q = \frac{3600\,\text{C}}{3.6\,\text{C per mAh}} = 1000\,\text{mAh}$$

Half an hour at two amps moves a thousand milliamp-hours — a tenth of the power bank's printed rating.

**Sanity check:** $2\,\text{A}$ for half an hour is the same as $1\,\text{A}$ for a full hour, which is $1\,\text{Ah} = 1000\,\text{mAh}$ directly — the same answer.

## Where the picture breaks

The train compartment is a real setting, not an analogy, but three honest limits apply.

First, a real charging current is not steady. It stays high while the cell is low and tapers off as the cell fills, so "$2.0\,\text{A}$ for half an hour" is an idealisation; the true charge is the area under a falling current–time curve.

Second, "how much electricity is in it" is misleading. Charge is never stored up and emptied like water in a tank: the same electrons circulate round the loop. The mAh number tells you how much charge the battery can *push round the circuit* before it is flat; what it really holds is chemical energy.

Third, a mAh rating says nothing about the voltage at which that charge is pushed, so on its own it is not an energy rating — you will need the volts too, in the lesson on power.

## Key takeaway

Current is the rate of flow of charge, $I = Q/t$, measured in amperes, with $1\,\text{A} = 1\,\text{C/s}$. Its conventional direction is the way positive charge would move — opposite to the electrons' drift in a metal. Multiply a current by a time and you get charge, which is exactly what a battery's mAh rating counts.
