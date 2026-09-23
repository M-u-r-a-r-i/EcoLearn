---
concept_id: capacitance
interest: football
format: explain
title: The tablet on the touchline that will not take a gloved finger
check:
  question: |-
    A capacitor charged to $2.0\,\text{V}$ holds $40\,\text{pC}$. The same capacitor is then charged to $6.0\,\text{V}$. What are its charge and its capacitance now?
  options:
    A: |-
      $120\,\text{pC}$ and $60\,\text{pF}$
    B: |-
      $40\,\text{pC}$ and $6.7\,\text{pF}$
    C: |-
      $13\,\text{pC}$ and $20\,\text{pF}$
    D: |-
      $120\,\text{pC}$ and $20\,\text{pF}$
  answer: D
  explanation: |-
    $C = Q/V = 40/2.0 = 20\,\text{pF}$, and capacitance is fixed by the geometry, so it stays $20\,\text{pF}$. Tripling the voltage triples the charge to $120\,\text{pC}$.
  misconceptions:
    A: |-
      Reads $C = Q/V$ as though the capacitance itself grew with the voltage. $C$ is set by the plates' area, their separation and the material between them — not by how hard you charge them.
    B: |-
      Treats the stored charge as a fixed property of the capacitor. Raise the voltage and more charge flows on; it is the *ratio* $Q/V$ that stays the same.
    C: |-
      Uses $Q = C/V$ instead of $Q = CV$, so a higher voltage appears to strip charge off. Charge and voltage rise together.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A training ground at dusk with a floodlight pylon, an electric fence and its energiser box along the far side, a coach holding a touchscreen tablet, a water bowser and an AED cabinet](scenes/football/potential_capacitance.svg "The analyst's tablet on the touchline: a sheet of glass that somehow knows where your finger is.")

Tarun is the club's video analyst, and on match days he stands at the halfway line with a tablet, tagging every turnover as it happens.

Yashika comes off at half time still in her keeper's gloves, wanting to see a corner again. She swipes. Nothing. She jabs harder, then with two fingers. The tablet ignores her completely.

"Gloves off," says Tarun.

She peels one off and the screen obeys her at once. Then the drizzle starts, and within a minute the tablet is misbehaving on its own — the video scrubs back and forth under fat drops of water that nobody is touching.

Yashika turns it over. Sealed glass. No holes, no buttons, nothing that moves. The electronics are underneath, behind an insulating layer, and nothing about her finger ever reaches them.

So what is it detecting? And why does a wet drop count, while a dry glove does not?

## The physics

A **capacitor** is any two conductors separated by an insulator. Connect it to a battery and $+Q$ collects on one conductor, $-Q$ on the other. Nothing crosses the gap: charge flows *around* the circuit until the potential difference between the conductors matches the battery.

That potential difference $V$ is proportional to $Q$, and the ratio is the **capacitance**:

$$C = \frac{Q}{V}$$

Its SI unit is the **farad**, $1\,\text{F} = 1\,\text{C/V}$. A farad is enormous, so in practice you meet $\mu\text{F}$, $\text{nF}$ and $\text{pF}$. Capacitance depends only on the size and shape of the conductors and on what lies between them — never on $Q$ or $V$. Double the charge and the voltage doubles with it; $C$ does not budge.

**The parallel-plate capacitor.** Take two flat plates of area $A$, a distance $d$ apart, with $d$ much smaller than the plates themselves, vacuum or air between them, charged to $\pm Q$.

1. Surface charge density: $\sigma = Q/A$.
2. Each plate on its own makes a field $\sigma/2\varepsilon_0$. Between the plates the two fields point the same way and add; outside they cancel. So between the plates the field is uniform and
$$E = \frac{\sigma}{\varepsilon_0} = \frac{Q}{\varepsilon_0 A}$$
3. Potential difference: $V = Ed = \dfrac{Qd}{\varepsilon_0 A}$.
4. Capacitance:
$$C = \frac{Q}{V} = \frac{\varepsilon_0 A}{d}$$

with $\varepsilon_0 = 8.85 \times 10^{-12}\,\text{F/m}$. Larger plates hold more charge at the same voltage; a narrower gap needs less voltage for the same charge. Both push $C$ up.

![Two parallel plates of area A a distance d apart carrying +Q and −Q, with a uniform field between them and a little fringing at the edges](figures/capacitance/parallel-plate-capacitor.svg "The field is uniform between the plates and almost nothing outside. The derivation ignores the slight fringing at the edges.")

Under the glass, a touchscreen carries a grid of fine transparent electrodes. Each crossing is a tiny capacitor, and the controller measures its capacitance many times a second. A bare finger is a conductor that is part of a much larger conducting body — you — and bringing it close changes that capacitance measurably. Water does too, which is why the drizzle scrubbed the video. A dry glove is an insulator that simply holds your finger too far away to change anything.

## Worked example

Take one crossing of the grid as two small plates: area $A = 1.0\,\text{cm}^2 = 1.0 \times 10^{-4}\,\text{m}^2$, separation $d = 0.10\,\text{mm} = 1.0 \times 10^{-4}\,\text{m}$ (illustrative values).

**Find:** (a) its capacitance; (b) the charge it holds at $5.0\,\text{V}$; (c) what happens if the insulating layer is made half as thick.

**(a)** Substitute into $C = \varepsilon_0 A/d$. The numbers were chosen so that $A/d = 1.0\,\text{m}$ exactly, which leaves

$$C = \varepsilon_0 \times 1.0\,\text{m} = 8.9 \times 10^{-12}\,\text{F} \approx 8.9\,\text{pF}$$

So a square centimetre of plate, a tenth of a millimetre away, is worth about nine picofarads. Picture how far that is from one farad: you would need roughly a hundred thousand million such patches.

**(b)** Charge follows from the definition, $Q = CV$:

$$Q = 8.9 \times 10^{-12} \times 5.0 = 4.4 \times 10^{-11}\,\text{C} \approx 44\,\text{pC}$$

**(c)** Halve $d$ to $0.05\,\text{mm}$ and, since $C \propto 1/d$, the capacitance doubles to about $18\,\text{pF}$. Nothing about the charge or the voltage came into that — only the geometry.

**Sanity check:** the units run $(\text{F/m}) \times \text{m}^2/\text{m} = \text{F}$, as they must, and $\text{F} \times \text{V} = \text{C}$ in part (b).

## Where the picture breaks

The touchscreen is a real device, not an analogy, but the parallel-plate model is a sketch of it. The electrodes are long thin strips crossing at right angles, not neat facing squares, and much of the useful field is the part that **fringes** out through the glass — precisely the part the derivation throws away. Real screens also measure the *change* in capacitance rather than its value, and they reject slow drifts, which is how a good one ignores rain that a cheap one cannot. Finally, some screens are not capacitive at all: a resistive screen works by two layers physically touching, and that kind does take a gloved finger.

## Key takeaway

Capacitance is charge stored per volt, $C = Q/V$, measured in farads. It is fixed by the conductors' geometry and by the material between them, not by how much charge you put on. For parallel plates in air or vacuum, $C = \varepsilon_0 A/d$: bigger plates and a smaller gap give more capacitance.
