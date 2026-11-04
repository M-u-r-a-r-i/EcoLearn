---
concept_id: electric_current
interest: gaming
format: explain
title: What the little USB meter is actually counting
check:
  question: |-
    A USB meter reads $1.5\,\text{A}$ while a controller charges. Inside the cable's copper power conductor, the free electrons drift from the controller back towards the charger. The conventional current in that conductor is:
  options:
    A: |-
      from the controller to the charger, because a current *is* the flow of electrons
    B: |-
      zero, because the electron flow and the conventional current cancel out
    C: |-
      from the charger to the controller, opposite to the electrons' drift
    D: |-
      from the charger to the controller, carried by electrons moving that way
  answer: C
  explanation: |-
    Conventional current is defined as the direction in which *positive* charge would flow — out of the source's positive terminal and into the device. The actual carriers in a metal are electrons, which are negative, so they drift the opposite way.
  misconceptions:
    A: |-
      Takes the electrons' direction to *be* the current's direction. The arrow we draw for current was fixed before the electron was discovered, and every circuit rule is written for that convention, not for the electron flow.
    B: |-
      Treats the conventional current and the electron drift as two separate flows that could cancel. They are one and the same flow, described twice; there is nothing to add up.
    D: |-
      Gets the direction right but the reason wrong. The conventional direction is correct, but in a metal it is electrons that move, and they drift *against* it.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A night gaming desk with a monitor showing a frame counter and a low controller battery, a controller charging over a USB cable with current arrows, a USB power meter, and an open PC case](scenes/gaming/current_electricity.svg "Every cable on this desk is carrying something the meter can count — and the arrows on the cable are not pointing the way the electrons go.")

The computer club's LAN evening runs off one four-port charger, and Aarav has spent twenty minutes with a tiny USB power meter — a dongle with a green display — plugged between the charger and each cable in turn.

Every port shows the same 5.0 V. The currents refuse to agree: the headset reads 0.5, his controller reads 1.5, the little desk fan reads 0.2.

Sanya, waiting for her turn on the good chair, asks the awkward question. "Same charger, same five volts. So what is that meter counting when it says 1.5?"

"Electricity," says Aarav, and knows at once that it is not an answer.

Then Sanya makes it worse. Which way is the 1.5 going — out of the charger or into it? And do the electrons in the cable agree?

Two fair questions, and nobody in the room can answer either.

## The physics

A copper wire is already full of **free electrons** moving about randomly in every direction, all the time. That is not a current. A current exists only when there is a *net* flow of charge past a point.

**Electric current** is the rate of flow of charge:

$$I = \frac{Q}{t}$$

where $Q$ is the charge, in coulombs (C), crossing a chosen cross-section of the conductor in time $t$, in seconds. The unit is the **ampere**: $1\,\text{A} = 1\,\text{C/s}$. When the flow is not steady, the current at an instant is $I = \dfrac{dQ}{dt}$.

![A wire with a marked cross-section: electrons drift one way while the conventional current arrow points the other](figures/electric_current/current-as-charge-flow.svg "Pick one cross-section and count the charge crossing it each second — that number is the current.")

So the meter's "1.5" is a *rate*: one and a half coulombs of charge slipping past every second. The "5.0 V" is something else entirely — how hard each coulomb is pushed — and you meet it properly in the next few lessons.

Current is a **scalar**, even though we draw it with an arrow. The arrow shows the **conventional direction of current**: the direction in which *positive* charge would flow — out of the charger's positive terminal, along the cable, through the controller, and back. In copper the carriers are electrons, which are negative, so they drift the *opposite* way. That mismatch is a historical accident from before the electron was known, and we keep it because every circuit rule you will learn is written for it.

That answers Sanya's second question: the arrow points into the controller, and the electrons go the other way.

## Worked example

**Given:** the controller charges at a steady $I = 1.5\,\text{A}$, and the monitor beside it is running at $60$ frames per second.
**Find:** the charge delivered in one minute, and the charge delivered during a single frame.

In one minute, $t = 60\,\text{s}$:

$$Q = It = 1.5\,\text{A} \times 60\,\text{s} = 90\,\text{C}$$

Ninety coulombs a minute — an enormous amount of charge by electrostatic standards, quietly going round without a single spark.

Now one frame. At $60$ frames per second each frame lasts $t = \dfrac{1}{60}\,\text{s}$, about $16.7\,\text{ms}$:

$$Q = 1.5 \times \frac{1}{60} = 0.025\,\text{C} = 25\,\text{mC}$$

Twenty-five millicoulombs in the time it takes one image to appear and be replaced.

**Sanity check:** a minute holds $3600$ frames, and $3600 \times 25\,\text{mC} = 90\,\text{C}$ — the two answers agree, so the arithmetic is sound.

## Where the picture breaks

The desk is the setting, not an analogy. There is no "gaming" version of charge, and pretending a current is like players joining a lobby would teach you something false.

Three honest limits. First, a real charging current is not steady: it starts high and tapers off as the cell fills, so $1.5\,\text{A}$ is a snapshot, and $I = Q/t$ with a fixed $I$ is an idealisation over a short stretch. Second, the meter measures at the charger's end; a little of what leaves never reaches the cell, because the cable and the charging circuit warm up on the way. Third, and most important: charge is never used up. The same electrons circulate endlessly. What the charger supplies is *energy*, not charge that disappears into the controller.

## Key takeaway

Current is the rate of flow of charge, $I = Q/t$, measured in amperes — one ampere is one coulomb per second. It is a scalar, and its conventional direction is the direction positive charge would move, which in a metal is opposite to the electrons' actual drift. A meter reading amperes is telling you how fast charge is passing, not how much energy is being delivered.
