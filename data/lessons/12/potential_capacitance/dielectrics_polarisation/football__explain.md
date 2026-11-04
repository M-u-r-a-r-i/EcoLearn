---
concept_id: dielectrics_polarisation
interest: football
format: explain
title: The grass clippings that jumped onto the blower tube
check:
  question: |-
    A slab is placed in a uniform field of $2.4 \times 10^{4}\,\text{V/m}$ with its faces perpendicular to the field, and the field inside it settles at $6.0 \times 10^{3}\,\text{V/m}$. What is its dielectric constant, and what caused the drop?
  options:
    A: |-
      $K = 0.25$; the slab's bound charges add their field to the applied one.
    B: |-
      $K = 4.0$; free electrons in the slab flow to its faces and cancel part of the field.
    C: |-
      $K = 4.0$; bound charges left uncancelled on the faces set up a field opposing the applied one.
    D: |-
      $K = 1.8 \times 10^{4}$; the drop in the field is the dielectric constant.
  answer: C
  explanation: |-
    Inside a slab $E = E_0/K$, so $K = E_0/E = 2.4 \times 10^{4} / 6.0 \times 10^{3} = 4.0$. The drop comes from the bound surface charges of the polarised material, whose field points against the applied field.
  misconceptions:
    A: |-
      Inverts the ratio, using $E/E_0$ instead of $E_0/E$, and has the bound charges' field the wrong way round. If it added to the applied field, the field inside would go up, not down.
    B: |-
      Gets $K$ right but treats a dielectric like a conductor. Its charges are **bound** inside molecules; they shift a little but cannot flow to the faces the way free electrons do.
    D: |-
      Subtracts the two fields instead of dividing them. $K$ is a ratio of two fields, so it is a pure number with no units.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A training ground at dusk with a floodlight pylon, an electric fence and its energiser box along the far side, a coach holding a touchscreen tablet, a water bowser and an AED cabinet](scenes/football/potential_capacitance.svg "Mowing day: dry clippings, a plastic blower tube, and a pitch that has not seen rain all week.")

It has not rained for a fortnight, and Ranjit has spent the morning cutting stripes into the pitch. Now he is walking the touchline with the blower, pushing the dry clippings off the white lines. The blower's tube is a length of ribbed orange plastic, and clippings have been rushing along inside it for two hours.

Aparna, who plays for the women's side and has come early for a session, watches him switch it off and rest the tube on the grass. Clippings hop off the ground and stick along it in a fuzzy green fur.

"That'll be static," she says. "The grass rubbed the plastic all the way up."

"So the plastic's charged," Ranjit agrees. "Fine. But look —" he brushes the tube clean and lowers it towards a fresh pile. The clippings jump up to meet it.

Aparna cut that grass herself an hour ago. Nobody rubbed it, nobody charged it. Each scrap is as neutral as it gets, and it is dry, dead plant matter — no free electrons sloshing about in it the way they do in a metal.

So what exactly is the tube pulling on?

## The physics

Plastic, paper, glass, dry grass and water are **dielectrics**: insulators whose charges are **bound** inside molecules and cannot flow. But they can shift a little, and a little is enough.

**Two kinds of molecule.**

- **Non-polar** molecules (such as $\text{O}_2$ or $\text{H}_2$) have their positive and negative centres in the same place. An applied field pulls them slightly apart, making an **induced dipole** pointing along the field.
- **Polar** molecules (such as $\text{H}_2\text{O}$) already carry a permanent dipole, but thermal jiggling leaves them pointing every which way, so they cancel on average. A field produces a partial **alignment**.

Either way the material becomes **polarised** — it picks up a net dipole moment. The dipole moment per unit volume is the **polarisation** $\vec{P}$, and for most materials it is proportional to the field inside.

**What that does to the field.** Inside a polarised slab, the positive end of each little dipole sits right beside the negative end of its neighbour, so they cancel in pairs. At the two faces there is nothing to cancel against. The face the field enters is left with a layer of negative **bound charge** $-\sigma_p$, and the face it leaves with $+\sigma_p$. Those two layers make a field of their own, pointing *against* the applied field $E_0$, so the field inside is weaker:

$$E = E_0 - \frac{\sigma_p}{\varepsilon_0} = \frac{E_0}{K}$$

The **dielectric constant** $K$ is always greater than 1 and measures how strongly the material polarises. Vacuum has $K = 1$, air is barely above it, and water is about 80 at room temperature.

![A dielectric slab in a field pointing right: the molecular dipoles line up, leaving negative bound charge on the left face and positive on the right, and the field inside the slab is drawn weaker](figures/dielectrics_polarisation/dielectric-slab-polarised.svg "Inside, neighbouring dipole ends cancel in pairs. Only the two face layers survive — and their field opposes the applied field.")

**Back to the clippings.** Near the charged tube, each scrap of grass polarises. The side facing the tube takes the opposite sign of bound charge and the far side the same sign. The tube's field is stronger nearer to it, so the near side is pulled in harder than the far side is pushed away, and the neutral scrap lifts off the ground.

## Worked example

Put a flat slab with $K = 4.0$ (illustrative; many plastics sit between about 2 and 5) into a uniform field $E_0 = 2.0 \times 10^{4}\,\text{V/m}$, faces perpendicular to the field.

**Find:** (a) the field inside it; (b) the bound surface charge density; (c) how much potential difference $1.0\,\text{mm}$ of slab accounts for, against $1.0\,\text{mm}$ of air.

**(a)** The field inside is cut by the factor $K$:

$$E = \frac{E_0}{K} = \frac{2.0 \times 10^{4}}{4.0} = 5.0 \times 10^{3}\,\text{V/m}$$

**(b)** The whole of that reduction is the bound layers' doing, so from $E_0 - E = \sigma_p/\varepsilon_0$:

$$\sigma_p = \varepsilon_0(E_0 - E) = 8.85 \times 10^{-12} \times 1.5 \times 10^{4} \approx 1.3 \times 10^{-7}\,\text{C/m}^2$$

**(c)** Over the same millimetre, the slab carries $Ed = 5.0 \times 10^{3} \times 1.0 \times 10^{-3} = 5.0\,\text{V}$, while the air carries $2.0 \times 10^{4} \times 1.0 \times 10^{-3} = 20\,\text{V}$. A millimetre of this plastic "uses up" only a quarter as much voltage as a millimetre of air.

**Sanity check:** the same bound charge comes out of $\sigma_p = \varepsilon_0 E_0(1 - 1/K) = 8.85 \times 10^{-12} \times 2.0 \times 10^{4} \times 0.75$. And the limiting cases behave: $K = 1$ gives $\sigma_p = 0$ and nothing changes, while a huge $K$ drives the field inside towards zero, the conductor-like extreme.

## Where the picture breaks

The tube and the clippings are real, but they are not the tidy slab the formula describes. $E = E_0/K$ holds for a slab with flat faces square-on to a **uniform** field — whereas the clippings are curled, tangled and sitting in a field that is anything but uniform. That non-uniformity is not a detail: it is the very reason they are attracted at all. In a perfectly uniform field a neutral scrap would polarise and feel no net force, only a turning effect. The little ellipses in the figure are cartoons too — real alignment is partial and constantly knocked about by thermal motion. And once a scrap touches the tube it can pick up charge by contact and fly off again, which is a different effect altogether.

## Key takeaway

A dielectric has bound charges, not free ones. In a field its molecules align or acquire induced dipoles, and the material becomes polarised. The uncancelled bound charge on its faces makes a field opposing the applied one, so inside a slab $E = E_0/K$ with $K > 1$. The same polarisation is why a charged object attracts neutral scraps of grass or paper.
