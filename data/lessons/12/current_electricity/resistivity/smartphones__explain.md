---
concept_id: resistivity
interest: smartphones
format: explain
title: Why the long thin cable charges slowly and runs warm
check:
  question: |-
    A charging cable is swapped for one made of the same copper but **twice as long**, with conductors of **half the cross-sectional area**. At the same temperature, the resistance of each conductor becomes:
  options:
    A: |-
      the same as before
    B: |-
      twice as large
    C: |-
      four times as large
    D: |-
      eight times as large
  answer: C
  explanation: |-
    $R = \rho L/A$ with $\rho$ unchanged. Doubling $L$ doubles $R$, and halving $A$ doubles it again, so $R$ becomes $2 \times 2 = 4$ times as large.
  misconceptions:
    A: |-
      Assumes the two changes cancel, as if resistance grew with area. A smaller cross-section gives the charge a narrower path, so it *raises* the resistance; both changes push the same way.
    B: |-
      Counts only the extra length and forgets the thinner conductor. Resistance depends on both the length and the cross-sectional area.
    D: |-
      Treats "half the area" as "half the diameter", which would cut the area to a quarter. The area itself has halved, so it contributes a factor of two, not four.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A charging corner: a phone on a wall charger, a power bank charging an earbuds case through a small USB meter, and a smartwatch on its charging puck, with current arrows on the cables](scenes/smartphones/current_electricity.svg "The cables look alike from outside; what matters is the copper hidden inside them.")

Rohan bought a two-metre charging cable from a roadside stall so he could use his phone in bed. It works — just slowly. The phone that charged in about an hour and a half on the short cable that came with it now takes most of the evening, and the cheap cable feels faintly warm along its length.

His sister Sneha, who studies electronics, cuts open an old stall cable from the drawer. The copper strands inside are hair-thin; the original cable, cut beside it, has a visibly thicker bundle.

"Same copper," she says. "Same charger. Different cable."

Rohan also remembers something from the phone's settings: when the battery gets hot, charging slows down on its own. So something inside the phone is keeping track of temperature — electrically.

What makes one piece of copper resist more than another, and how could a resistance tell a phone how hot it is?

## The physics

Experiments show that a uniform conductor's resistance is proportional to its length $L$ and inversely proportional to its cross-sectional area $A$:

$$R = \rho\,\frac{L}{A}$$

The constant $\rho$ is the **resistivity**, in $\Omega\,\text{m}$. It belongs to the *material* (and its temperature), not to the particular piece: copper is about $1.7 \times 10^{-8}\,\Omega\,\text{m}$ at room temperature whatever shape it is drawn into. Resistance belongs to the *object*.

![Two conductors of the same material: a longer one with more resistance and a thicker one with less](figures/resistivity/resistance-and-dimensions.svg "Longer means more resistance; fatter means less — and it is the area, not the diameter, that enters the formula.")

Why these dependences? A longer wire means more collisions along the way, and a wider one offers more parallel paths for the charge.

**Temperature.** In a metal, heating makes the ions vibrate more, so electrons collide more often and the resistivity *rises*, roughly in a straight line over ordinary temperatures:

$$\rho_T = \rho_0\,[1 + \alpha\,(T - T_0)]$$

where $\alpha$ is the **temperature coefficient of resistivity**, positive for metals.

In a **semiconductor** such as silicon, heating frees many more charge carriers, and that effect wins, so the resistivity *falls* steeply. A **thermistor** made of semiconducting material uses this: a small rise in temperature gives a large fall in resistance. Phone battery packs typically include one, so the charging circuit can sense the battery's temperature and slow down when it gets hot.

![A graph of resistivity against temperature: rising for a metal, falling steeply for a semiconductor](figures/resistivity/resistivity-vs-temperature.svg "Metal resistivity climbs gently with temperature; a semiconductor's plunges as heating frees more carriers.")

## Worked example

**Given:** one conductor of the stall cable is copper, $\rho = 1.7 \times 10^{-8}\,\Omega\,\text{m}$, with area $A = 0.1\,\text{mm}^2 = 1 \times 10^{-7}\,\text{m}^2$.
**Find:** the resistance of $1\,\text{m}$ of it, and then of the full $2\,\text{m}$.

For one metre,

$$R = \rho\,\frac{L}{A} = 1.7 \times 10^{-8} \times \frac{1}{1 \times 10^{-7}} = 0.17\,\Omega$$

Small — but a charging cable carries amperes, so even a fraction of an ohm matters.

For two metres, the length doubles and so does the resistance:

$$R = 2 \times 0.17 = 0.34\,\Omega$$

That is one conductor. The current has to go out along one and back along another, so the charging loop sees about twice this again.

**Sanity check:** a conductor with ten times the copper area would have a tenth of the resistance for the same length, and a short one less again — that is why the original cable barely warms.

## Where the picture breaks

Cutting the cable open is honest physics, but real cables are more than a straight copper rod. The conductors are bundles of fine strands, so $A$ means the total copper area of the bundle; the connectors at each end add resistance of their own; and a slow charge also depends on the negotiation between phone and charger, not only on the cable.

The straight-line temperature rule for metals holds only over a moderate range. A thermistor does not follow it at all — its resistance falls in a steep curve — and the phone's circuit is built to read that curve, not a straight line.

## Key takeaway

Resistance depends on the material and the shape: $R = \rho L/A$, so a longer or thinner conductor resists more. Resistivity $\rho$ is a property of the material: in metals it rises with temperature, roughly as $\rho_0[1 + \alpha(T - T_0)]$, while in semiconductors it falls, which is what makes a thermistor a thermometer.
