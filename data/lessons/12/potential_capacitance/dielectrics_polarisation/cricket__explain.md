---
concept_id: dielectrics_polarisation
interest: cricket
format: explain
title: The confetti that jumped onto a rubbed clapper
check:
  question: |-
    A slab of dielectric with dielectric constant $K = 5$ is placed in a uniform field of $1.0 \times 10^5\,\text{V/m}$, with its faces perpendicular to the field. What is the field inside the slab?
  options:
    A: |-
      $5.0 \times 10^5\,\text{V/m}$
    B: |-
      Zero
    C: |-
      $1.0 \times 10^5\,\text{V/m}$, unchanged
    D: |-
      $2.0 \times 10^4\,\text{V/m}$
  answer: D
  explanation: |-
    The polarised slab develops bound surface charges whose field opposes the applied field, reducing it by a factor $K$: $E = E_0/K = 1.0 \times 10^5/5 = 2.0 \times 10^4\,\text{V/m}$.
  misconceptions:
    A: |-
      Multiplies by $K$, as if the dielectric strengthened the field. The bound charges' field opposes the applied field, so the field inside is weaker.
    B: |-
      Treats the dielectric like a conductor. Its charges are bound and can only shift slightly, so they reduce the field but cannot cancel it.
    C: |-
      Thinks an insulator has no charges that can respond, so nothing changes. Its bound charges do shift, and that shifting is polarisation.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A cricket ground under a storm cloud with lightning in the distance, a floodlight tower, a curator on the pitch, a car by the boundary and a photographer's flash](scenes/cricket/potential_capacitance.svg "Before the storm breaks, the stands are dry, packed and noisy.")

It's the club final, and the stands are packed. Ananya and her little brother Vihaan each have a pair of long inflatable plastic clappers, the kind fans bang together every time the ball crosses the rope. For twenty overs they have been rubbing and banging them non-stop.

Between overs, Vihaan tears his ticket stub into confetti for the next six. He drops a few bits on the seat, and as Ananya's clapper swings past them, they leap up and cling to it.

"Magic," says Vihaan.

"Static," says Ananya. "Rubbing charged the plastic."

"Fine. But the *paper* isn't charged," Vihaan points out. "I just tore it. Why would something with no charge get pulled by a charge?"

Ananya opens her mouth, then closes it. A neutral scrap of paper, with no free electrons worth mentioning, is being pulled across a gap. What is happening inside it?

## The physics

Paper, plastic, glass and water are **dielectrics**: insulators whose charges are **bound** inside molecules. They cannot flow the way free electrons in a metal do. But they can shift slightly, and that is enough to matter.

**Two kinds of molecule.**

- **Non-polar molecules** (for example $\text{O}_2$, $\text{H}_2$): the centres of positive and negative charge coincide. An external field pulls them slightly apart, creating an **induced dipole** along the field.
- **Polar molecules** (for example $\text{H}_2\text{O}$, $\text{HCl}$): each already has a permanent dipole, but thermal jiggling points them every which way, so they cancel on average. A field produces a partial **alignment** along it.

Either way the material becomes **polarised**: it acquires a net dipole moment. The dipole moment per unit volume is the **polarisation** $\vec{P}$. For most materials it is proportional to the field inside.

**What polarisation does to the field.** Inside a polarised slab, the $+$ end of each tiny dipole sits next to the $-$ end of its neighbour, so they cancel. But at the faces nothing cancels. The face where the field enters gets a layer of negative **bound charge** $-\sigma_p$, and the face where it leaves gets $+\sigma_p$. These layers make their own field, pointing *against* the applied field $E_0$. So the field inside is reduced:

$$E = E_0 - \frac{\sigma_p}{\varepsilon_0} = \frac{E_0}{K}$$

The **dielectric constant** $K$ (always greater than 1) measures how strongly the material polarises. For vacuum $K = 1$, air is very close to 1, and water is about 80 at room temperature.

![A dielectric slab in a field pointing right: molecular dipoles line up, leaving negative bound charge on the left face and positive on the right, and the field inside is weaker](figures/dielectrics_polarisation/dielectric-slab-polarised.svg "Inside, neighbouring dipole ends cancel. Only the two face layers are left over, and their field opposes the applied field.")

**Back to the paper.** Near the charged clapper, the paper's molecules polarise. The side facing the clapper gets the opposite sign of bound charge, and the far side the same sign. The clapper's field is stronger closer to it, so the near side is attracted more strongly than the far side is repelled. The net force pulls the neutral paper in.

## Worked example

**Given:** a flat slab with $K = 5.0$ (illustrative; many glasses lie between about 5 and 10) in a uniform field $E_0 = 3.0 \times 10^4\,\text{V/m}$, faces perpendicular to the field.
**Find:** (a) the field inside; (b) the bound surface charge density; (c) the potential difference across $2.0\,\text{mm}$ of slab, compared with $2.0\,\text{mm}$ of air.

(a) $E = E_0/K = 3.0 \times 10^4/5.0 = 6.0 \times 10^3\,\text{V/m}$.

(b) From $E_0 - E = \sigma_p/\varepsilon_0$:

$$\sigma_p = \varepsilon_0 (E_0 - E) = 8.85 \times 10^{-12} \times 2.4 \times 10^4 \approx 2.1 \times 10^{-7}\,\text{C/m}^2$$

(c) Slab: $V = Ed = 6.0 \times 10^3 \times 0.0020 = 12\,\text{V}$. Air: $3.0 \times 10^4 \times 0.0020 = 60\,\text{V}$.

**Sanity check:** $\sigma_p = \varepsilon_0 E_0 (1 - 1/K) = 8.85 \times 10^{-12} \times 3.0 \times 10^4 \times 0.80 \approx 2.1 \times 10^{-7}\,\text{C/m}^2$, the same answer. Limiting cases: $K = 1$ gives $\sigma_p = 0$ and no change. Very large $K$ drives the field inside towards zero, the conductor-like limit.

## Where the picture breaks

The paper-and-clapper scene is real, but it is a **non-uniform** field acting on a crumpled scrap. $E = E_0/K$ holds only for a slab whose faces are perpendicular to a uniform field. The attraction happens precisely *because* the field is non-uniform. The ellipse "molecules" in the figure are cartoons: real alignment is partial and constantly jostled by thermal motion. And once the paper touches the plastic, it can pick up charge by contact and then fly off, which is a different effect altogether.

## Key takeaway

A dielectric has bound charges, not free ones. In a field its molecules become aligned or induced dipoles, and the material is polarised. The uncancelled bound charge on its faces opposes the applied field, so inside a slab $E = E_0/K$, with $K > 1$. Polarisation is also why a charged object attracts neutral bits of paper.
