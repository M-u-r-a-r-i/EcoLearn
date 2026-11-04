---
concept_id: electric_potential
interest: football
format: explain
title: What the fence energiser means by eight thousand volts
check:
  question: |-
    A fence wire is held at $4000\,\text{V}$ above the earth. One pulse drives a charge of $20\,\mu\text{C}$ from the wire to the ground. How much energy does that pulse deliver?
  options:
    A: |-
      $0.080\,\text{J}$
    B: |-
      $0.040\,\text{J}$
    C: |-
      $4000\,\text{J}$
    D: |-
      $2.0 \times 10^{8}\,\text{J}$
  answer: A
  explanation: |-
    Potential difference is energy per unit charge, so the energy is $W = qV = (20 \times 10^{-6}\,\text{C}) \times 4000\,\text{V} = 0.080\,\text{J}$.
  misconceptions:
    B: |-
      Uses $\tfrac{1}{2}qV$, the formula for charging a capacitor from zero. Here the charge crosses the full $4000\,\text{V}$, so the energy is $qV$.
    C: |-
      Reads volts as though they were joules. A volt is a joule **per coulomb**; the energy also depends on how much charge moves.
    D: |-
      Divides the potential difference by the charge instead of multiplying. $V = W/q$ rearranges to $W = qV$.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A training ground at dusk with a floodlight pylon, an electric fence and its energiser box along the far side, a coach holding a touchscreen tablet, a water bowser and an AED cabinet](scenes/football/potential_capacitance.svg "One training ground, four devices that only make sense once you know what a volt counts.")

The club's pitch backs onto open grazing land, and cattle kept wandering across it at night and churning up the goalmouth. So last month Bhaskar, the groundsman, ran a single wire along the far side and bolted a small grey box to the corner post.

Suhani is helping him coil the hose after training when Mohit reads the label on the box out loud. **8000 V.** Below it, a fat cable runs to an ordinary 12 V battery.

"That's a lie," Mohit says. "Twelve volts in, eight thousand out? It can't give out more than it's got."

The box clicks, once a second. Bhaskar hangs a tester lamp on the wire and it flashes with every click. "Feels like a hard flick on the arm," he says. "Nothing worse. Cattle learn in one go."

Suhani has just been told that the socket in the clubhouse wall, at 230 V, could kill her. This wire carries thirty times that number and only stings.

So what is a volt actually counting?

## The physics

Push a small positive **test charge** $q$ towards other charges and the electric field pushes back, so you must do work. The **electrostatic potential** $V$ at a point is the work an external force does bringing one unit of positive charge slowly — without letting it speed up — from infinity to that point:

$$V = \frac{W}{q}$$

Potential is a **scalar**, and its SI unit is the **volt**: $1\,\text{V} = 1\,\text{J/C}$.

In practice what you measure is the **potential difference** between two points. Carrying a charge $q$ slowly from $B$ to $A$ takes work

$$W_{BA} = q\,(V_A - V_B)$$

Because the electrostatic force is conservative, that work is the same along every path, which is exactly why one number can be pinned to each point.

Now read the label again. Between the wire and the earth, each coulomb of charge carries $8000$ joules. That is a big number **per coulomb**. Whether it hurts depends on the *other* factor in $W = qV$: how much charge actually moves. The energiser lets go of a tiny sliver of charge in each pulse, so the energy per pulse is small. The clubhouse socket, by contrast, will push charge through you for as long as you are connected.

**Potential and field.** The field tells you how fast potential falls with distance:

$$E = -\frac{dV}{dr}$$

The minus sign says the field points the way the potential *drops*. Where the field is uniform this becomes $E = \Delta V/d$, with $d$ measured along the field — which also gives the field a second unit, $1\,\text{V/m} = 1\,\text{N/C}$.

![A uniform field between two plates at 300 V and 0 V, with lines drawn at 200 V and 100 V one centimetre apart and a positive charge being pushed from the 100 V line up to the 200 V line](figures/electric_potential/uniform-field-potential.svg "Between parallel plates the potential falls at a steady rate. Moving a positive charge the other way, from 100 V to 200 V, costs q × 100 V of work.")

## Worked example

Take the wire as sitting $0.50\,\text{m}$ above damp earth and held at $4000\,\text{V}$ (illustrative values — energisers are labelled in kilovolts, and the height is whatever the posts give). One pulse moves about $50\,\mu\text{C}$.

**Find:** (a) the energy in one pulse; (b) the field in the gap, treating it as uniform.

**(a)** Energy is charge times potential difference:

$$W = qV = (50 \times 10^{-6}\,\text{C}) \times 4000\,\text{V} = 0.20\,\text{J}$$

That is the whole of the sting — about the work you do lifting a match ball five centimetres off the grass.

**(b)** Now the field. Over a short vertical gap, treat the potential as falling steadily:

$$E = \frac{\Delta V}{d} = \frac{4000\,\text{V}}{0.50\,\text{m}} = 8000\,\text{V/m}$$

**Sanity check:** dry air only breaks down and sparks at about $3 \times 10^{6}\,\text{V/m}$. At $8000\,\text{V/m}$ the air holds, which is why the fence does nothing at all until something touches the wire and bridges the gap.

## Where the picture breaks

The fence is a real device, but it is not a tidy electrostatics problem.

- A battery on its own cannot produce $8000\,\text{V}$. The box uses a rapidly changing magnetic field to do it — electromagnetic induction, which you meet in a later chapter.
- Each pulse is a brief **current**, not a static arrangement of charge. Electrostatics describes the situation between pulses.
- $E = \Delta V/d$ needs a uniform field. Round a thin wire the field is nothing like uniform: it is fiercest right at the wire's surface and weakens quickly away from it, so $8000\,\text{V/m}$ is only a rough average across the gap.
- The number on the label is the peak voltage with nothing touching the wire. Touch it and the voltage collapses as charge flows.
- And the obvious one: never test a fence by hand. Bhaskar uses a lamp.

## Key takeaway

Electrostatic potential is work per unit charge, $V = W/q$, measured in volts, where $1\,\text{V} = 1\,\text{J/C}$. Moving a charge $q$ between two points takes $q(V_A - V_B)$ of work, along any path. A high voltage on its own is not a lot of energy — the energy is $qV$, and $q$ can be tiny. The field points where the potential falls: $E = -dV/dr$, or $E = \Delta V/d$ in a uniform field.
