---
concept_id: capacitor_energy
interest: football
format: explain
title: Why the green box on the post spends five seconds whirring
check:
  question: |-
    A capacitor charged to $2000\,\text{V}$ stores $200\,\text{J}$. If the same capacitor were charged to $1000\,\text{V}$ instead, how much energy would it store?
  options:
    A: |-
      $100\,\text{J}$
    B: |-
      $200\,\text{J}$
    C: |-
      $50\,\text{J}$
    D: |-
      $25\,\text{J}$
  answer: C
  explanation: |-
    $U = \tfrac{1}{2}CV^2$, and $C$ is unchanged, so the energy goes as $V^2$. Halving the voltage divides the energy by four: $200/4 = 50\,\text{J}$.
  misconceptions:
    A: |-
      Reads $U = \tfrac{1}{2}CV^2$ as if it were linear in $V$. Halving the voltage also halves the stored charge, so the energy drops by two factors of two, not one.
    B: |-
      Treats the stored energy as a fixed property of the capacitor. The geometry fixes $C$; the energy depends on how far you charge it.
    D: |-
      Applies the factor of $\tfrac{1}{2}$ a second time. The half is already inside the formula — halving $V$ contributes only the $V^2$ factor.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A training ground at dusk with a floodlight pylon, an electric fence and its energiser box along the far side, a coach holding a touchscreen tablet, a water bowser and an AED cabinet](scenes/football/potential_capacitance.svg "The green cabinet by the pitch holds the one device at the ground that has to deliver a lot of energy in a very short time.")

Saturday morning, and the club has booked Farida to run the annual first-aid course for coaches and senior players. The last session is the green cabinet on the post beside the pitch: the defibrillator, which everyone walks past every week and nobody has opened.

She takes out the training unit and lays it on the bench. Inside is a battery pack no bigger than the one in a head torch.

She presses the button. The unit begins to whirr — a thin rising note that goes on for about five seconds — and then a light says it is ready. The delivery itself, she explains, is over in a few thousandths of a second.

Rishabh, sixteen and impatient, asks the obvious question. "If those little cells can't do the job on their own, how does waiting five seconds help? They're the same cells either way."

Farida taps the case. "Something in here is filling up."

Between the whirr and the ready light, energy is being gathered and parked somewhere. Where — and how much of it fits?

## The physics

It is parked in a **capacitor**. Charging one means dragging charge from one plate to the other against the voltage that is already between them, and the work you do is stored.

**Deriving the energy.** Suppose the capacitor already holds charge $q$, so the voltage across it is $v = q/C$. Moving a further small charge $dq$ across takes work

$$dW = v\,dq = \frac{q}{C}\,dq$$

Add that up from $q = 0$ to $q = Q$:

$$U = \int_0^Q \frac{q}{C}\,dq = \frac{Q^2}{2C}$$

and with $Q = CV$ the same energy can be written three ways:

$$U = \frac{Q^2}{2C} = \frac{1}{2}CV^2 = \frac{1}{2}QV$$

**Why the half?** Because the voltage climbed steadily from $0$ to $V$ as the charge went on, so on average each scrap of charge crossed only $V/2$. Draw $v$ against $q$ and you get a straight line through the origin; the stored energy is the **area of the triangle** beneath it.

![A straight line from the origin rising to 45 mC at 300 V, with a dashed line marking the average voltage of 150 V](figures/capacitor_energy/v-q-line.svg "Whatever the capacitor, the picture is this shape: the stored energy is the triangle's area, ½QV, because the charge went on at an average of half the final voltage.")

**Energy density.** Where does the energy actually sit? For parallel plates, $C = \varepsilon_0 A/d$ and $V = Ed$, so

$$U = \frac{1}{2}\,\frac{\varepsilon_0 A}{d}\,(Ed)^2 = \left(\frac{1}{2}\varepsilon_0 E^2\right) \times (Ad)$$

and $Ad$ is just the volume between the plates — the volume the field occupies. So the energy can be thought of as stored **in the electric field**, with energy per unit volume

$$u = \frac{1}{2}\varepsilon_0 E^2$$

This holds for any electric field in vacuum, not only inside capacitors.

## Worked example

Take the unit's capacitor as $C = 100\,\mu\text{F} = 1.0 \times 10^{-4}\,\text{F}$, charged to $V = 2000\,\text{V}$, and delivering its energy in about $10\,\text{ms}$ (illustrative values).

**Find:** the stored energy, and the power during the delivery.

**Step 1 — the energy.** Use the form with the two quantities you have:

$$U = \tfrac{1}{2}CV^2 = \tfrac{1}{2} \times 1.0 \times 10^{-4} \times (2000)^2 = \tfrac{1}{2} \times 1.0 \times 10^{-4} \times 4.0 \times 10^{6} = 200\,\text{J}$$

Two hundred joules is about what it takes to lift a full $10\,\text{kg}$ kit bag two metres off the ground — a real amount of energy, but not an alarming one.

**Step 2 — the power.** Power is energy divided by the time it takes:

$$P = \frac{U}{t} = \frac{200\,\text{J}}{10 \times 10^{-3}\,\text{s}} = 2.0 \times 10^{4}\,\text{W}$$

Twenty kilowatts — more than a row of floodlights — for one hundredth of a second. Meanwhile the battery pack spent five seconds putting that same $200\,\text{J}$ in, an average of only $40\,\text{W}$. That gap is Rishabh's answer: the capacitor lets energy trickle in slowly and leave all at once.

**Sanity check:** the charge stored is $Q = CV = 0.20\,\text{C}$, and $\tfrac{1}{2}QV = \tfrac{1}{2} \times 0.20 \times 2000 = 200\,\text{J}$ — the same number by a different route.

## Where the picture breaks

The training unit is a real device, but this is a physics lesson about capacitors, not a lesson in using one — that part belongs to Farida's course and to the instructions on the lid. The numbers above are illustrative. Two physics caveats as well. The whirr is a small circuit stepping a few volts up to a few thousand, and it does that by electromagnetic induction, which is a later chapter. And the discharge is not at constant power: it surges and then tails away, so $20\,\text{kW}$ is an average over the pulse, not a steady figure. One more subtlety you will meet again: when a supply charges a capacitor through a resistance, it hands over $QV$ but only $\tfrac{1}{2}QV$ ends up stored — the other half is lost as heat on the way in.

## Key takeaway

A charged capacitor stores $U = \tfrac{1}{2}CV^2 = Q^2/2C = \tfrac{1}{2}QV$. The half is there because the charge was moved at an average of half the final voltage. The energy can be pictured as living in the field, with density $u = \tfrac{1}{2}\varepsilon_0 E^2$. Because energy goes as $V^2$, doubling the charging voltage stores four times as much — and a capacitor can release it far faster than the source that filled it.
