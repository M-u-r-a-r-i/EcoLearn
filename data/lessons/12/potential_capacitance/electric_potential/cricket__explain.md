---
concept_id: electric_potential
interest: cricket
format: explain
title: What the danger sign behind the pavilion is really measuring
check:
  question: |-
    In fair weather the air near the ground has a downward electric field of about $100\,\text{V/m}$. In the open air beside the pitch, what is the potential difference between a point level with the top of the stumps ($71.1\,\text{cm}$ high) and the ground?
  options:
    A: |-
      $7110\,\text{V}$
    B: |-
      $141\,\text{V}$
    C: |-
      $71\,\text{V}$
    D: |-
      $0\,\text{V}$, because no current flows through the air
  answer: C
  explanation: |-
    In a uniform field the potential difference is $\Delta V = Ed = 100\,\text{V/m} \times 0.711\,\text{m} \approx 71\,\text{V}$, with the higher point at the higher potential because the field points down.
  misconceptions:
    A: |-
      Multiplies by $71.1$ without converting centimetres to metres, so the answer is 100 times too large.
    B: |-
      Divides the field by the distance instead of multiplying; potential difference is field times distance, $\Delta V = Ed$.
    D: |-
      Thinks a potential difference exists only when a current flows. Potential is work per unit charge in a field; it exists whether or not anything moves.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A cricket ground under a storm cloud with lightning in the distance, a floodlight tower, a curator on the pitch, a car by the boundary and a photographer's flash](scenes/cricket/potential_capacitance.svg "A storm rolls in over the ground. Clouds, floodlights, cameras and the pitch itself all involve electric potential.")

Rain has stopped play at a district ground, and the covers are on. Rohan, sixteen and bored, wanders behind the pavilion with his friend Farhan. They stop at a fenced enclosure humming quietly — the substation that feeds the floodlights. A red sign on the gate reads **DANGER — 11000 V**.

In Rohan's pocket is the small battery for the scoreboard remote, marked **9 V**.

"Same unit," Farhan says. "So the substation is just a much bigger battery. It's got eleven thousand volts of current in it."

"Volts aren't current," Rohan says, then realises he can't say what they *are*. Overhead, a dark cloud rumbles. The commentator on someone's radio says the cloud base may be millions of volts above the ground.

Millions of volts between a cloud and the grass. Eleven thousand behind a fence. Nine in his pocket. Volts of *what*? What is one volt actually counting?

## The physics

Bring a small positive **test charge** $q$ towards other charges and the electric field pushes back. To move it you must do work against that force. The **electrostatic potential** $V$ at a point is the work done by an external force in bringing a unit positive charge, slowly (without accelerating it), from infinity to that point:

$$V = \frac{W}{q}$$

Potential is a **scalar**. Its SI unit is the **volt**: $1\,\text{V} = 1\,\text{J/C}$.

What matters in practice is the **potential difference** between two points. The work needed to carry a charge $q$ slowly from $B$ to $A$ is

$$W_{BA} = q\,(V_A - V_B)$$

Because the electrostatic force is conservative, this work is the same whichever path you take. That is why a single number can be attached to each point.

So the sign on the gate means: between the live conductor and the earth, each coulomb carries a difference of $11\,000$ joules of energy. The battery says $9$ joules per coulomb between its terminals. Volts count **energy per unit charge** — not current, and not charge.

**Potential and field.** The field tells you how fast the potential changes with distance:

$$E = -\frac{dV}{dr}$$

The minus sign means the field points in the direction in which the potential *falls*. In a uniform field this becomes $E = \Delta V / d$, where $d$ is measured along the field. That gives a second unit for the field: $1\,\text{V/m} = 1\,\text{N/C}$.

![A uniform field between plates at 300 V and 0 V, with lines at 200 V and 100 V one centimetre apart, and a positive charge being pushed from 100 V up to 200 V](figures/electric_potential/uniform-field-potential.svg "Potential falls steadily along the field. Pushing a positive charge against the field, from 100 V to 200 V, costs q × 100 V of work.")

In the figure, the field points from the $300\,\text{V}$ plate towards the $0\,\text{V}$ plate. Carrying $+q$ from $B$ ($100\,\text{V}$) to $A$ ($200\,\text{V}$) costs $W = q \times 100\,\text{V}$. The lines are $1.0\,\text{cm}$ apart, so $E = 100\,\text{V} / 0.010\,\text{m} = 1.0 \times 10^4\,\text{V/m}$.

## Worked example

Even on a clear day there is a natural electric field in the air near the ground. It points downward and is roughly $100\,\text{V/m}$ in size (take that value as illustrative; it varies with place and weather).

**Given:** $E = 100\,\text{V/m}$, downward; stump height $h = 71.1\,\text{cm} = 0.711\,\text{m}$.
**Find:** (a) the potential difference between a point level with the stump tops and the ground, in the open air; (b) the work needed to lift a charge of $+2.0\,\text{nC}$ through that height.

(a) The field is uniform over this small height, so

$$\Delta V = E\,h = 100 \times 0.711 = 71.1\,\text{V} \approx 71\,\text{V}$$

The field points down and potential falls along the field, so the higher point is at the **higher** potential.

(b) $W = q\,\Delta V = (2.0 \times 10^{-9}\,\text{C}) \times 71.1\,\text{V} \approx 1.4 \times 10^{-7}\,\text{J}$.

**Sanity check:** (V/m) × m gives V, and C × V gives J. A tiny charge gives a tiny amount of work, as it should.

## Where the picture breaks

Cricket gives the setting here, not an analogy: we are looking at real potentials around a ground. Three cautions:

- Seventy volts between head height and your feet sounds alarming, but air conducts so poorly that almost no charge can flow. Your body is a conductor, so it also distorts the field around it. The $71\,\text{V}$ is for open air, not for a person or a wet stump.
- The substation supplies alternating voltage, which changes many times a second. Electrostatics deals with charges at rest, so the sign illustrates the *unit*, not a static situation.
- Under a storm cloud the field near the ground can be far larger than $100\,\text{V/m}$ and is anything but uniform. $E = \Delta V/d$ holds only where the field is uniform.

## Key takeaway

Electrostatic potential is work per unit charge: $V = W/q$, measured in volts ($1\,\text{V} = 1\,\text{J/C}$). The work to move a charge between two points is $q(V_A - V_B)$, whatever the path. The field points the way potential falls: $E = -dV/dr$, or $E = \Delta V/d$ in a uniform field.
