---
concept_id: capacitor_energy
interest: cricket
format: explain
title: Where a camera flash keeps its energy between sixes
check:
  question: |-
    A $100\,\mu\text{F}$ capacitor is charged to $200\,\text{V}$. How much energy does it store?
  options:
    A: |-
      $4.0\,\text{J}$
    B: |-
      $0.010\,\text{J}$
    C: |-
      $2.0 \times 10^6\,\text{J}$
    D: |-
      $2.0\,\text{J}$
  answer: D
  explanation: |-
    $U = \tfrac{1}{2}CV^2 = \tfrac{1}{2} \times 100 \times 10^{-6} \times 200^2 = \tfrac{1}{2} \times 10^{-4} \times 4.0 \times 10^4 = 2.0\,\text{J}$.
  misconceptions:
    A: |-
      Uses $CV^2$ without the $\tfrac{1}{2}$, as if all the charge had been moved at the full final voltage. The voltage rises from zero during charging, so on average it is only half the final value.
    B: |-
      Uses $\tfrac{1}{2}CV$, forgetting to square the voltage. Energy grows as $V^2$ because both the charge and the voltage grow together.
    C: |-
      Substitutes $100$ for the capacitance without converting microfarads to farads, so the answer is a million times too large.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A cricket ground under a storm cloud with lightning in the distance, a floodlight tower, a curator on the pitch, a car by the boundary and a photographer's flash](scenes/cricket/potential_capacitance.svg "The photographer at the boundary: a flash that fires in a blink, then needs a few seconds to get ready again.")

Diya is doing a photography course and has talked her way onto the boundary at an evening club match. The light is going, so she's using a clip-on flash. It runs on two ordinary AA cells.

Every time she switches it on there is a thin, rising whine, and a few seconds later a small green light says READY. The batter swings, the ball sails over long-on, she presses the shutter, and the flash lights the whole scene for a moment. Then the whine starts again.

Her friend Parth, holding her camera bag, is unimpressed. "Why all the waiting? Why can't the batteries just power the flash directly?"

Diya knows two AA cells give about three volts, and the flash tube needs hundreds of volts to fire. It also needs its energy in about a thousandth of a second, far faster than small batteries can deliver it. Somewhere in that flash, energy is being collected during the whine and held ready. Where is it kept, and how much is there?

## The physics

The flash stores its energy in a **capacitor**. Charging one means moving charge from one plate to the other against the growing voltage between them. That takes work, and the work is stored.

**Deriving the energy.** Suppose the capacitor already holds charge $q$, so the voltage across it is $v = q/C$. Moving a further small charge $dq$ across takes work

$$dW = v\,dq = \frac{q}{C}\,dq$$

Adding this up from $q = 0$ to $q = Q$:

$$U = \int_0^Q \frac{q}{C}\,dq = \frac{Q^2}{2C}$$

Using $Q = CV$, the same energy can be written three ways:

$$U = \frac{Q^2}{2C} = \frac{1}{2}CV^2 = \frac{1}{2}QV$$

**Why the half?** The voltage rises steadily from $0$ to $V$ as the charge builds up, so on average each bit of charge was moved through only $V/2$. On a $V$–$q$ graph, the stored energy is the **area of the triangle** under the line.

![A straight line from the origin to 45 mC at 300 V, with a dashed line at the average voltage of 150 V](figures/capacitor_energy/v-q-line.svg "The energy stored is the triangle's area under the line, ½QV. The charge went in at an average of half the final voltage.")

**Energy density.** Where is the energy? For a parallel-plate capacitor, $C = \varepsilon_0 A/d$ and $V = Ed$, so

$$U = \frac{1}{2}\,\frac{\varepsilon_0 A}{d}\,(Ed)^2 = \left(\frac{1}{2}\varepsilon_0 E^2\right) \times (Ad)$$

$Ad$ is the volume between the plates, where the field is. So the energy can be described as stored **in the electric field**, with energy per unit volume

$$u = \frac{1}{2}\varepsilon_0 E^2$$

This holds for any electric field in vacuum, not just inside capacitors.

## Worked example

**Given** (illustrative values for a small flash): $C = 150\,\mu\text{F} = 1.5 \times 10^{-4}\,\text{F}$, charged to $V = 300\,\text{V}$, and discharged in about $1.0\,\text{ms}$.
**Find:** the charge, the stored energy and the average power during the flash.

$$Q = CV = 1.5 \times 10^{-4} \times 300 = 0.045\,\text{C} = 45\,\text{mC}$$

$$U = \tfrac{1}{2}CV^2 = \tfrac{1}{2} \times 1.5 \times 10^{-4} \times (300)^2 = \tfrac{1}{2} \times 1.5 \times 10^{-4} \times 9.0 \times 10^4 = 6.75\,\text{J}$$

$$P_\text{avg} = \frac{U}{t} = \frac{6.75}{1.0 \times 10^{-3}} \approx 6.8 \times 10^3\,\text{W}$$

That's nearly seven kilowatts for a thousandth of a second. The batteries refill the capacitor over about two seconds, an average of only about $3.4\,\text{W}$. The capacitor lets energy trickle in slowly and rush out fast.

**Sanity check:** $\tfrac{1}{2}QV = \tfrac{1}{2} \times 0.045 \times 300 = 6.75\,\text{J}$, the same answer.

**Why not simply use air between large plates?** Air breaks down (sparks) at a field of about $3 \times 10^6\,\text{V/m}$. At that field, $u = \tfrac{1}{2} \times 8.85 \times 10^{-12} \times (3 \times 10^6)^2 \approx 40\,\text{J/m}^3$. Holding $6.75\,\text{J}$ would need about $6.75/40 \approx 0.17\,\text{m}^3$ of charged air, bigger than the photographer. Real flash capacitors use thin insulating films instead. You'll see why that helps in the next lesson.

## Where the picture breaks

The whine is a small circuit that steps the battery's three volts up to a few hundred. It works by electromagnetic induction, which is beyond this chapter. Not all of the $6.75\,\text{J}$ becomes light: much of it ends up as heat in the tube and circuit. The discharge isn't a steady power either; it surges and then falls away, so $6.8\,\text{kW}$ is only an average. One more subtlety you may meet later: when a battery charges a capacitor through a resistance, the battery supplies $QV$ but only $\tfrac{1}{2}QV$ ends up stored. The other half is lost as heat in the wires.

## Key takeaway

A charged capacitor stores energy $U = \tfrac{1}{2}CV^2 = Q^2/2C = \tfrac{1}{2}QV$. The half appears because charge is moved at an average of half the final voltage. The energy can be thought of as stored in the field, with energy density $u = \tfrac{1}{2}\varepsilon_0 E^2$. Capacitors let energy be collected slowly and released very fast.
