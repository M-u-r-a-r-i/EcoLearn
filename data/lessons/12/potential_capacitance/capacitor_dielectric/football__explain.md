---
concept_id: capacitor_dielectric
interest: football
format: explain
title: The water gauge with no float in it
check:
  question: |-
    A parallel-plate capacitor is left **connected to its battery** while a dielectric slab with $K = 3$ is slid in to fill the gap completely. What happens?
  options:
    A: |-
      The charge stays the same and the voltage falls to a third.
    B: |-
      The voltage stays the same and the charge triples.
    C: |-
      The voltage stays the same and the charge falls to a third.
    D: |-
      Only the capacitance changes; the charge and the voltage both stay as they were.
  answer: B
  explanation: |-
    A connected battery holds $V$ fixed. The capacitance becomes $3C_0$, so $Q = CV$ triples — the extra charge flows onto the plates from the battery.
  misconceptions:
    A: |-
      Applies the disconnected case. Only once the battery is removed is the charge trapped; with it connected, $V$ is what is held fixed.
    C: |-
      Pictures the dielectric as something in the way of the charge. It raises the capacitance, so at the same voltage the plates hold *more* charge, not less.
    D: |-
      Forgets that $C$, $Q$ and $V$ are tied together by $C = Q/V$. If $C$ changes while $V$ is held fixed, $Q$ has to change.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A training ground at dusk with a floodlight pylon, an electric fence and its energiser box along the far side, a coach holding a touchscreen tablet, a water bowser and an AED cabinet](scenes/football/potential_capacitance.svg "The bowser is towed out before every dry-weather session. Its gauge says how much water is left — without a single moving part.")

The bowser is the tank on wheels the club tows behind the mower to water the pitch in dry weather. On its side is a small display that counts down as the water goes out, and Sunita trusts it completely.

Omkar, on his second week of a summer job at the ground, does not. He climbs the ladder and shines a torch into the filler while the tank is half empty, looking for the float he is sure must be bobbing about in there.

There is no float. No bobbing arm, no window, nothing that moves. Just two long flat metal strips running down the inside wall, sealed under a coating, with a single cable going off to the display.

"It's a capacitor," Sunita says, without looking up from the hose.

Omkar has just done capacitors in school and that makes it worse, not better. Capacitance is about the area of the plates and the gap between them. The strips are bolted to the wall. They don't move a millimetre when water goes in or out.

So what has water got to do with capacitance?

## The physics

**Filling the gap.** Start with a parallel-plate capacitor in air, $C_0 = \varepsilon_0 A/d$, holding charge $\pm Q$. Now fill the gap with a dielectric of dielectric constant $K$. The material polarises, and its bound surface charges cut the field between the plates from $E_0$ to $E_0/K$. With the same charge on the plates, $V = Ed$ falls by the same factor $K$, so $C = Q/V$ goes **up** by $K$:

$$C = K C_0 = \frac{K\varepsilon_0 A}{d}$$

Omkar's objection was right as far as it went: $A$ and $d$ really do not change. What he had missed is the third thing in the formula — the material in between is part of what sets the capacitance. Air has $K \approx 1$. Water has $K \approx 80$ at room temperature. Swapping air for water in that gap changes $C$ by a factor of eighty, and the display is watching for exactly that.

**A slab that only partly fills the gap.** Slide in a slab of thickness $t$, less than $d$. The field is $E_0$ in the air and $E_0/K$ inside the slab, so

$$V = E_0(d - t) + \frac{E_0}{K}\,t \quad\Rightarrow\quad C = \frac{\varepsilon_0 A}{d - t + t/K}$$

As far as capacitance goes, a slab of thickness $t$ counts as a layer of air only $t/K$ thick.

![A capacitor with its plates 4.0 mm apart and a 2.0 mm slab of K = 4 in the middle, the field drawn full strength in the air gaps and weaker inside the slab](figures/capacitor_dielectric/slab-partial.svg "A different case from the one worked below, but the same idea: the slab weakens the field inside itself, so it counts as only t/K of air.")

**Battery connected, or not?** What changes depends on what is being held fixed.

| Dielectric fills the gap | $C$ | $Q$ | $V$ | $E$ | $U$ |
|---|---|---|---|---|---|
| Battery still connected ($V$ fixed) | $\times K$ | $\times K$ | same | same | $\times K$ |
| Battery disconnected ($Q$ fixed) | $\times K$ | same | $\div K$ | $\div K$ | $\div K$ |

## Worked example

Take an air-filled capacitor with $C_0 = 20\,\text{pF}$ and a gap $d = 4.0\,\text{mm}$ (illustrative values).

**Find** its capacitance (a) with a $3.0\,\text{mm}$ slab of $K = 3.0$ pushed in, (b) with the gap completely full of water, and (c) after it is charged to $12\,\text{V}$ on air, disconnected, and then filled with the $K = 3.0$ material.

**(a)** First the effective gap, in millimetres:

$$d - t + \frac{t}{K} = 4.0 - 3.0 + \frac{3.0}{3.0} = 2.0\,\text{mm}$$

The gap has effectively halved, and since $C \propto 1/d$, the capacitance doubles: $C = 40\,\text{pF}$.

**(b)** Water fills it completely, so $C = KC_0 \approx 80 \times 20 = 1600\,\text{pF}$. Eighty times the empty value — an enormous, easy-to-measure jump, and the whole basis of the gauge.

**(c)** Disconnected means the charge is trapped at $Q = C_0V_0 = 20\,\text{pF} \times 12\,\text{V} = 240\,\text{pC}$. Filling the gap makes $C = KC_0 = 60\,\text{pF}$, so

$$V = \frac{Q}{C} = \frac{240\,\text{pC}}{60\,\text{pF}} = 4.0\,\text{V}$$

The voltage falls to a third, exactly as the table's second row promises, while the charge sits where it was.

**Sanity check:** in (a), putting $K = 1$ gives an effective gap of $4.0\,\text{mm}$ and $C = C_0$ — a slab of "air" changes nothing, as it must. And $40\,\text{pF}$ sits between the empty $20\,\text{pF}$ and the completely full $60\,\text{pF}$.

## Where the picture breaks

The gauge is real, but the strips in the tank are not the neat sandwich worked above. Water rises *along* the strips rather than filling the gap from one face to the other, so a level probe behaves like two capacitors side by side — a wet one and a dry one **in parallel**, with the split moving as the level changes. That gives a capacitance rising steadily with depth, which is what a gauge needs; the slab formula above is the other arrangement, where the dielectric sits across the gap. Three more cautions: water's $K \approx 80$ drops as the temperature rises; dissolved salts and dirt let a little current leak between the strips and distort the reading; and any real gauge is **calibrated** against known levels rather than trusted to a formula. The physics it leans on is still the simple bit — more water between the plates, more capacitance.

## Key takeaway

Filling a capacitor's gap with a dielectric multiplies its capacitance by $K$: $C = K\varepsilon_0 A/d$. A slab of thickness $t$ gives $C = \varepsilon_0 A/(d - t + t/K)$, as though it were a layer of air only $t/K$ thick. With the battery connected, $V$ is held fixed and $Q$ rises by $K$; with the battery disconnected, $Q$ is fixed and $V$, $E$ and $U$ all fall by $K$.
