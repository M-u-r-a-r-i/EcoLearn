---
concept_id: electric_potential
interest: smartphones
format: explain
title: What the numbers on a charger brick are counting
check:
  question: |-
    A small charge of $+2.0\,\mu\text{C}$ is moved slowly a distance of $5.0\,\text{mm}$ straight against a uniform field of $2000\,\text{V/m}$. How much work does the external force do?
  options:
    A: |-
      $10\,\text{J}$
    B: |-
      $2.0 \times 10^{-5}\,\text{J}$
    C: |-
      $2.0 \times 10^{-2}\,\text{J}$
    D: |-
      $-2.0 \times 10^{-5}\,\text{J}$
  answer: B
  explanation: |-
    The potential rises by $\Delta V = Ed = 2000 \times 0.0050 = 10\,\text{V}$, so the work is $W = q\,\Delta V = 2.0\times10^{-6} \times 10 = 2.0\times10^{-5}\,\text{J}$.
  misconceptions:
    A: |-
      Confuses potential difference with work. $10\,\text{V}$ is the work *per coulomb*; the charge is only two millionths of a coulomb, so you must multiply by $q$.
    C: |-
      Leaves the distance in millimetres. $5.0\,\text{mm} = 5.0\times10^{-3}\,\text{m}$; using $5$ makes the answer a thousand times too big.
    D: |-
      Gets the sign backwards. Moving a positive charge *against* the field, the external force pushes the same way the charge moves, so it does positive work and the charge gains energy.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A desk by a rainy window: a phone with raindrops on its screen being tapped by a finger, a metal biscuit tin with its lid off, a breadboard with two supercapacitor cells wired in a chain, a stylus and a fitness band with a small display](scenes/smartphones/potential_capacitance.svg "A desk full of gadgets, and every one of them has a voltage printed somewhere on it. This chapter is about what that number means.")

Kavya's new fast charger arrives, and her little brother Aditya grabs the brick before she can. He reads the tiny grey print on its side out loud like a secret code.

"Output: 5 V. Or 9 V. Why does it get to choose?"

"The phone asks for more when it wants to charge faster," Kavya says.

"So 9 V is more electricity."

She hesitates. The phone's own battery label, when she once saw it at a repair shop, said 3.7 V — less than either. Yet the battery is where all the energy ends up. And the old charger in the drawer says 5 V too, but it takes all evening to fill the phone.

"Not more electricity," she says slowly. "More... something."

Aditya waits. Kavya realises she can't finish the sentence. If a volt isn't an amount of electricity, what exactly is it counting?

## The physics

Take a small positive **test charge** $q$ and move it slowly (without speeding it up) through a region where other charges create a field. The field pushes on it, so an external force has to do work. The **electrostatic potential** $V$ at a point is the work done by an external force in bringing a unit positive charge from infinity to that point:

$$V = \frac{W}{q}$$

Potential is a **scalar**. Its SI unit is the **volt**: $1\,\text{V} = 1\,\text{J/C}$. So a volt is **energy per unit charge** — it tells you how many joules each coulomb gains or gives up, not how many coulombs there are.

What devices care about is the **potential difference** between two points. Moving charge $q$ slowly from $B$ to $A$ takes

$$W_{BA} = q\,(V_A - V_B)$$

The electrostatic force is conservative, so this work does not depend on the path — that is why each point can be given a single number.

Back to Kavya's brick. At $5\,\text{V}$, every coulomb that passes through the charger is handed $5\,\text{J}$. At $9\,\text{V}$ each coulomb is handed $9\,\text{J}$. Same charge, more energy per coulomb — "more something" is **energy per charge**.

**Potential and field.** The field tells you how fast the potential changes with distance:

$$E = -\frac{dV}{dr}$$

The minus sign means the field points the way the potential **falls**. In a uniform field, $E = \Delta V/d$ with $d$ measured along the field, which is why $1\,\text{V/m} = 1\,\text{N/C}$.

![A uniform field between plates at 300 V and 0 V, with lines at 200 V and 100 V one centimetre apart, and a positive charge being pushed from 100 V up to 200 V](figures/electric_potential/uniform-field-potential.svg "Potential falls steadily along the field. Pushing a positive charge against the field, from 100 V to 200 V, costs q × 100 V of work.")

## Worked example

A USB port holds its two power contacts at a potential difference of $5\,\text{V}$. Suppose (illustratively) that $100\,\text{C}$ of charge passes through it, and that two metal contacts at $5\,\text{V}$ and $0\,\text{V}$ sit $1.0\,\text{mm}$ apart with a roughly uniform field between them.

**Step 1 — energy per coulomb.** By definition, $5\,\text{V}$ means $5\,\text{J}$ for every coulomb that crosses.

**Step 2 — energy for 100 coulombs.**

$$W = qV = 100\,\text{C} \times 5\,\text{V} = 500\,\text{J}$$

That is about the work of lifting a $50\,\text{kg}$ sack of rice one metre off the floor.

**Step 3 — the field between the contacts.**

$$E = \frac{\Delta V}{d} = \frac{5\,\text{V}}{1.0\times10^{-3}\,\text{m}} = 5000\,\text{V/m}$$

**Sanity check:** dry air sparks at about $3\times10^{6}\,\text{V/m}$, hundreds of times more — which is why a USB plug never sparks at $5\,\text{V}$.

## Where the picture breaks

This chapter is **electrostatics**: charges held at rest. A charger drives a steady **current** through wires, and that is the next chapter's story — the "100 coulombs passing through" above borrows the idea early, only to show that energy = charge × volts. Real contacts are not flat parallel plates, so $5000\,\text{V/m}$ is an order-of-magnitude estimate. And the phone's 3.7 V battery is not "weaker" than a 5 V charger in any simple sense: how much energy a battery *holds* depends on how much charge it can move, not only on its voltage.

## Key takeaway

Electrostatic potential is work per unit charge, $V = W/q$, measured in volts, with $1\,\text{V} = 1\,\text{J/C}$. Moving charge $q$ between two points takes $q(V_A - V_B)$ of work, whatever the path. The field points the way potential falls, $E = -dV/dr$, or $E = \Delta V/d$ in a uniform field.
