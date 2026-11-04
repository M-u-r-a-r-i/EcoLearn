---
concept_id: resistivity
interest: football
format: explain
title: Why the far floodlight is dim on the end of a long lead
check:
  question: |-
    A cable is replaced by one of the same material and the same length, but with **twice the diameter**. Its resistance becomes:
  options:
    A: |-
      twice as large
    B: |-
      half as large
    C: |-
      unchanged — resistivity is a property of the material
    D: |-
      a quarter as large
  answer: D
  explanation: |-
    $R = \rho L / A$, and doubling the diameter makes the cross-sectional area **four** times larger, since $A = \pi d^2/4$. Four times the area means a quarter of the resistance.
  misconceptions:
    A: |-
      Assumes more metal means more resistance. Extra length does add resistance, but extra *width* gives the charge more room, so it subtracts.
    B: |-
      Halves the resistance for a doubled diameter, forgetting that area depends on the **square** of the diameter, not on the diameter itself.
    C: |-
      Confuses resistivity with resistance. Resistivity $\rho$ really is fixed by the material and temperature; resistance also depends on the shape, which is exactly what has changed here.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A floodlit football ground at night with two lit pylons, an electronic scoreboard, a fourth official holding a glowing LED substitution board, and a pitch-side distribution box with cables running to the lights](scenes/football/current_electricity.svg "The main pylons are wired properly; the practice lamp at the far end is on the end of whatever lead was in the store room.")

The under-16s train at the far end, past the halfway line, where the pylons barely reach. So the coach, Sandhya, drags out a portable LED lamp on a tripod and runs a thin orange extension lead to it from the distribution box — the whole length of the touchline, a good hundred metres, most of it still coiled on its drum.

The lamp lights. It is also visibly weaker than it was last week in the car park, where it sat two metres from a socket.

Halfway through the session one of the players, Tanvi, comes off with a knock, sits on the drum, and stands straight back up. The coiled cable is warm.

Nothing is broken. The lamp is the same lamp, the socket is the same socket, and the electricity board is delivering exactly what it always does. So where has the missing brightness gone — and why is the *cable* warm, when the lamp is the thing that is supposed to be hot?

## The physics

Resistance is not only about *what* a conductor is made of; it is also about its shape. For a uniform conductor of length $L$ and cross-sectional area $A$,

$$R = \rho\,\frac{L}{A}$$

where $\rho$ is the **resistivity** of the material, in ohm metres ($\Omega\,\text{m}$). Resistivity is the property that belongs to the substance itself — copper's $\rho$ is about $1.7 \times 10^{-8}\,\Omega\,\text{m}$ at room temperature, whatever the shape of the piece. Resistance belongs to the particular object.

![Three bars of the same material: a reference bar, a longer bar with more resistance, and a thicker bar with less resistance](figures/resistivity/resistance-and-dimensions.svg "Twice the length doubles the resistance; twice the area halves it. Only the shape has changed, not the material.")

Both dependences make sense from the drifting electrons. A longer wire means more collisions on the way through, so more opposition. A wider wire gives the same current more cross-section to spread across, so each electron needs to drift more slowly — less opposition. And note the warning in the check question: it is the *area* that halves the resistance, and area goes as the square of the diameter.

**Temperature.** Resistivity is fixed for a material only at a fixed temperature. For a metal, over a modest range,

$$\rho = \rho_0\left[1 + \alpha\,(T - T_0)\right]$$

where $\alpha$ is the temperature coefficient of resistivity, positive for metals. Heat a metal and its ions vibrate harder, so the drifting electrons are scattered more often and $\rho$ rises. A **semiconductor** does the opposite, and dramatically: heating it frees far more charge carriers than it adds scattering, so its resistivity falls.

![Two graphs of relative resistivity against temperature: a rising straight line for a metal and a steeply falling curve for a semiconductor](figures/resistivity/resistivity-vs-temperature.svg "Heat a metal and it resists a little more; heat a semiconductor and it resists far less.")

So Sandhya's lead has resistance of its own, in series with the lamp. It takes a share of the mains voltage and turns it into heat in the cable — which is why the drum is warm, and, because it is warming, very slightly worse at its job than when it was cold.

## Worked example

**Given:** the lead is $100\,\text{m}$ long with a copper cross-section of $2.0\,\text{mm}^2$, and $\rho = 1.7 \times 10^{-8}\,\Omega\,\text{m}$.
**Find:** the resistance of the copper the current actually travels through.

First, the length. The current has to go *out* to the lamp along one conductor and come *back* along the other, so the copper in its path is twice the lead's length:

$$L = 2 \times 100 = 200\,\text{m}$$

That doubling is the step people forget, and it doubles the answer.

Now convert the area, $2.0\,\text{mm}^2 = 2.0 \times 10^{-6}\,\text{m}^2$, and substitute:

$$R = \rho\,\frac{L}{A} = \frac{(1.7 \times 10^{-8})(200)}{2.0 \times 10^{-6}} = 1.7\,\Omega$$

Not much on its own — but with a couple of amperes flowing, a resistance of $1.7\,\Omega$ quietly eats a few volts before they ever reach the lamp.

**Sanity check:** a short lead from a wall socket measures a fraction of an ohm, so a couple of ohms for two hundred metres of thin wire is the right size of answer.

## Where the picture breaks

The training ground is the setting, not an analogy — a long cable is not "like" a long run. What the calculation leaves out is real, though: only the copper is counted, while a plug, a socket and a drum's slip contacts add resistance of their own, sometimes more than the wire. The formula $R = \rho L/A$ also assumes a uniform cross-section and a steady current at one temperature, and the lead breaks that assumption as it warms. A coiled drum is worse still, because the heat cannot escape from the middle of the coil — which is why leads are meant to be unwound before use.

## Key takeaway

Resistivity $\rho$ is a property of the material; resistance also depends on shape, through $R = \rho L/A$ — longer means more, thicker means less, and thickness counts as area, so doubling a diameter quarters the resistance. Resistivity rises with temperature for a metal, $\rho = \rho_0[1 + \alpha(T - T_0)]$, and falls sharply for a semiconductor.
