---
concept_id: drift_velocity
interest: gaming
format: explain
title: The electrons in your mouse cable move slower than a snail
check:
  question: |-
    A cable inside a gaming PC carries $2\,\text{A}$ while the machine idles. When the graphics card is loaded, the current in that same cable rises to $4\,\text{A}$. The drift velocity of the electrons in it becomes:
  options:
    A: |-
      twice as large
    B: |-
      unchanged — drift velocity is fixed by the metal
    C: |-
      half as large
    D: |-
      four times as large
  answer: A
  explanation: |-
    From $I = neAv_d$, with $n$, $e$ and $A$ all unchanged, $v_d$ is directly proportional to $I$. Doubling the current doubles the drift velocity.
  misconceptions:
    B: |-
      Confuses drift velocity with the random thermal speed of the electrons, which really does depend only on the metal and its temperature. Drift velocity is set by the current the circuit is pushing through the wire.
    C: |-
      Reads $I = neAv_d$ as though $v_d$ were in the denominator. $I$ and $v_d$ are on opposite sides of the equation, so they rise and fall together.
    D: |-
      Squares the change, probably recalling $P = I^2R$. Current enters $I = neAv_d$ to the first power only.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A night gaming desk with a monitor showing a frame counter, a controller charging over a USB cable with current arrows, a USB power meter, and an open PC case](scenes/gaming/current_electricity.svg "The cables on this desk carry signals that arrive in nanoseconds — and electrons that crawl.")

Rhea's team loses a close round and, as always, somebody blames the hardware. The new player is certain his mouse "feels slower" than his old one, because its cable is longer — two metres now instead of one.

Rhea is not having it. She has the club's high-speed capture running, and the gap between her click and the shot appearing on screen is one frame, sometimes two. At 60 frames a second that is under $34\,\text{ms}$ in total, and most of it belongs to the game and the display, not the wire.

Their physics teacher, passing with a mug of tea, adds something that sounds like a wind-up. The electrons inside that mouse cable, she says, move slower than a snail — about a tenth of a millimetre every second. At that rate one electron would need most of a day to travel from the mouse to the PC.

Both things cannot be true. So what is crawling, and what is arriving in time for the next frame?

## The physics

Inside a metal, the free electrons are already flying about at enormous random speeds, of order $10^5\,\text{m/s}$, colliding constantly with the vibrating metal ions. That motion is random — as much one way as the other — so it carries no charge anywhere.

Close the circuit and an electric field $\vec{E}$ appears along the whole length of the wire almost at once. Between one collision and the next, each electron is accelerated a little (backwards along the field, since it is negative), and the next collision wipes that gain out. What survives is a tiny steady average velocity laid on top of the random motion: the **drift velocity** $v_d$.

![An electron's fast zigzag path between collisions inside a wire, with a small steady net drift opposite to the electric field](figures/drift_velocity/drift-velocity-zigzag.svg "The zigzag is fast and random; the slow creep it adds up to is the drift velocity.")

**Mobility** $\mu$ says how much drift you get per unit field:

$$\mu = \frac{v_d}{E}$$

with units $\text{m}^2\,\text{V}^{-1}\text{s}^{-1}$.

Now tie drift to current. Let the wire have cross-sectional area $A$ and $n$ free electrons per unit volume, each of charge magnitude $e$. In a time $t$, every electron within a distance $v_d t$ of a chosen cross-section gets across it. That slab has volume $A v_d t$, so it holds $nAv_dt$ electrons, carrying

$$Q = neAv_d t$$

![A wire with a marked cross-section and the charge crossing it each second](figures/electric_current/current-as-charge-flow.svg "Count the charge in the slab that reaches the cross-section in time t; divide by t and you have the current.")

Divide by $t$, using $I = Q/t$:

$$\boxed{I = neAv_d}$$

This holds for a metallic conductor of uniform cross-section carrying a steady current. And it settles Rhea's argument: what races down the cable is the **field**, which sets electrons moving all along it at once. The electrons themselves only creep.

## Worked example

**Given:** a wire of cross-section $A = 1.0\,\text{mm}^2$ carrying $I = 1.6\,\text{A}$, in a metal with about $n = 1.0 \times 10^{29}$ free electrons per cubic metre (illustrative, but the right size for copper). Take $e = 1.6 \times 10^{-19}\,\text{C}$.
**Find:** the drift velocity, and how far an electron drifts during one frame at 60 fps.

Put the area into SI units first: $1.0\,\text{mm}^2 = 1.0 \times 10^{-6}\,\text{m}^2$.

$$v_d = \frac{I}{neA} = \frac{1.6}{(1.0 \times 10^{29})(1.6 \times 10^{-19})(1.0 \times 10^{-6})}$$

The denominator works out to $1.6 \times 10^{4}$ — that is the free charge, in coulombs, sitting in every metre of this wire. So

$$v_d = 1.0 \times 10^{-4}\,\text{m/s} = 0.1\,\text{mm/s}$$

One frame at 60 fps lasts about $16.7\,\text{ms}$, so in that time an electron shifts

$$d = v_d t = (1.0\times10^{-4})(0.0167) \approx 1.7 \times 10^{-6}\,\text{m}$$

Under two micrometres — a human hair is roughly $0.07\,\text{mm}$ across, so about forty of those steps would fit across one hair. Meanwhile the electrical signal, travelling at a large fraction of the speed of light, crosses a two-metre cable in around ten nanoseconds: something like a *million* times less than one frame.

**Sanity check:** a wire holds a colossal amount of free charge, so even a couple of amperes needs only a crawl — a tiny drift speed is exactly the right size.

## Where the picture breaks

The word "velocity" oversells it: $v_d$ is an average over a wildly random motion, not the speed of any one electron, and no electron travels in the neat straight line the symbol suggests. Nothing here is a gaming analogy either — input lag is dominated by the game engine, the display and the polling rate, not by anything in this equation, so do not let the story become an explanation of lag. Also $n$ is not yours to choose: for a given metal it is fixed by its atoms. And in a semiconductor both electrons and positive holes carry current, so $I = neAv_d$ needs a second term there — that comes later.

## Key takeaway

A field inside a wire gives the randomly moving free electrons a tiny average velocity, the drift velocity $v_d$, with mobility $\mu = v_d/E$. Counting the charge crossing a cross-section gives $I = neAv_d$. The drift is slower than a snail; circuits respond instantly because the field, not the electrons, travels the length of the wire.
