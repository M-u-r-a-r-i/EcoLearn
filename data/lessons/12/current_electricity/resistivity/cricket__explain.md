---
concept_id: resistivity
interest: cricket
format: explain
title: Why the thin extension cable to the sightscreen gets warm
check:
  question: |-
    Two wires are made of the same metal and have the same length, but the second has **twice the diameter** of the first. Compared with the first wire, the resistance of the second is:
  options:
    A: |-
      one quarter
    B: |-
      one half
    C: |-
      twice
    D: |-
      four times
  answer: A
  explanation: |-
    $R = \rho L/A$, and area goes as the square of the diameter: doubling the diameter multiplies $A$ by $4$, so $R$ falls to a quarter.
  misconceptions:
    B: |-
      Uses the diameter directly instead of the area. Resistance depends on cross-sectional area, and $A = \pi d^2/4$ — so the diameter enters squared.
    C: |-
      Has the dependence upside down, treating a thicker wire as harder to push current through. More area means more parallel paths, so less resistance.
    D: |-
      Combines both errors: inverts the relationship *and* squares it, as if $R \propto d^2$.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A cricket ground at dusk with floodlights, an electronic scoreboard, glowing stumps and an umpire holding a light meter](scenes/cricket/current_electricity.svg "One floodlight, one long cable trailing back to the pavilion socket.")

The practice floodlight has to reach the far net, and the pavilion socket is the only one on the ground. Karthik, who looks after the square, brings out the club's cable drum and unrolls fifty metres of thin white extension cable across the outfield.

The lamp comes on — but dull, a tired orange instead of white. Tanvi, who has just finished her Class 12 electricity chapter, walks back along the cable and notices something else: it is *warm*, the whole way along, on a cold January evening.

Karthik swaps it for the short, thick orange cable the roller uses. Same lamp, same socket. This time it blazes white, and the cable stays cold.

Same copper in both. Same lamp. So what did the length and the thickness actually change?

## The physics

Resistance is not a property of a material — it is a property of a *piece* of material. For a conductor of uniform cross-section, length $L$ and cross-sectional area $A$,

$$R = \rho \frac{L}{A}$$

where $\rho$ is the **resistivity** of the material, measured in ohm metres ($\Omega\,\text{m}$). Resistivity is the material's own property: copper has $\rho \approx 1.7 \times 10^{-8}\,\Omega\,\text{m}$ at room temperature, whatever shape you cut it into.

![Three bars of the same material: a reference bar, a longer bar with more resistance, and a thicker bar with less resistance](figures/resistivity/resistance-and-dimensions.svg "Twice the length doubles the resistance; twice the area halves it.")

The two dependences make sense from the drift picture: a longer conductor makes the electrons run a longer gauntlet of collisions, while a wider one offers more paths side by side for the same current, so each carries less.

Resistivity also changes with **temperature**. Over a modest range,

$$\rho_T = \rho_0\left[1 + \alpha (T - T_0)\right]$$

where $\alpha$ is the temperature coefficient of resistivity. For metals $\alpha$ is positive and small (about $0.004\,\text{K}^{-1}$ for copper): heat a metal and its ions vibrate harder, collisions get more frequent, and resistivity rises. For **semiconductors** like silicon, $\alpha$ is negative and large: warming frees many more charge carriers, and that flood of new carriers beats the extra collisions, so resistivity *falls* sharply.

![Two graphs of relative resistivity against temperature: a rising straight line for a metal, a steeply falling curve for a semiconductor](figures/resistivity/resistivity-vs-temperature.svg "Heat a metal and it resists more; heat a semiconductor and it resists far less.")

## Worked example

**Given:** Karthik's thin cable, $50\,\text{m}$ long with a conductor of cross-section $1.0\,\text{mm}^2$, made of copper with $\rho = 1.7 \times 10^{-8}\,\Omega\,\text{m}$.
**Find:** the resistance of that length of wire.

Put the area in SI units first: $1.0\,\text{mm}^2 = 1.0 \times 10^{-6}\,\text{m}^2$.

$$R = \rho\frac{L}{A} = 1.7 \times 10^{-8} \times \frac{50}{1.0 \times 10^{-6}}$$

The ratio $L/A$ is $5.0 \times 10^{7}\,\text{m}^{-1}$ — this is the *shape* part of the answer, and it is huge because the wire is long and thin.

$$R = 0.85\,\Omega$$

Under an ohm sounds negligible, and for a small lamp it would be. But the roller's cable has a conductor of $2.5\,\text{mm}^2$ — two and a half times the area — so its resistance is $0.85/2.5 = 0.34\,\Omega$, less than half. With several amperes flowing, that difference is enough voltage lost in the cable to dull the lamp, and the lost energy is exactly what warms the thin one.

**Sanity check:** a cable you can carry over your shoulder has a resistance well under an ohm, while a heating element has tens of ohms — the numbers are in the right order.

## Where the picture breaks

The cable is a real circuit, not a cricketing analogy, so nothing about the game is being stretched here. What *is* idealised: the formula assumes a uniform cross-section and a steady temperature, and the cable breaks the second assumption as soon as it warms — its resistance creeps up as it heats, making things slightly worse than the cold calculation says. The linear $\rho_T$ formula is itself only good over a limited range, and fails badly near very low temperatures. And a real extension cable carries two conductors, out and back, so the current actually travels twice the drum's length.

## Key takeaway

Resistivity $\rho$ belongs to the material; resistance belongs to the piece: $R = \rho L/A$. Long and thin means high resistance, short and thick means low. Warming a metal raises its resistivity roughly linearly, $\rho_T = \rho_0[1 + \alpha(T - T_0)]$, while a semiconductor's resistivity falls steeply with temperature.
