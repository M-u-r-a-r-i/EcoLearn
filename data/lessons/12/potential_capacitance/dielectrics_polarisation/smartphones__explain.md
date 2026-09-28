---
concept_id: dielectrics_polarisation
interest: smartphones
format: explain
title: The tap water that bent towards a rubbed phone
check:
  question: |-
    A slab of material with dielectric constant $K = 4$ is placed in a uniform field of $8000\,\text{V/m}$, with its faces perpendicular to the field. What is the field inside the slab?
  options:
    A: |-
      $32\,000\,\text{V/m}$
    B: |-
      $8000\,\text{V/m}$
    C: |-
      $2000\,\text{V/m}$
    D: |-
      $0\,\text{V/m}$
  answer: C
  explanation: |-
    The slab polarises, and the bound charges on its faces set up a field opposing the applied one, reducing it by the factor $K$: $E = E_0/K = 8000/4 = 2000\,\text{V/m}$.
  misconceptions:
    A: |-
      Thinks the dielectric strengthens the field because the capacitance goes up by $K$. The bound charges oppose the applied field, so the field inside is divided by $K$, not multiplied.
    B: |-
      Thinks a neutral material cannot affect the field because it has no net charge. Its molecules polarise, and the separated bound charges on its faces have a field of their own.
    D: |-
      Treats the dielectric like a conductor. Its charges are bound to their molecules and can only shift slightly, so they weaken the field but cannot cancel it completely.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A desk by a rainy window: a phone with raindrops on its screen being tapped by a finger, a metal biscuit tin with its lid off, a breadboard with two supercapacitor cells wired in a chain, a stylus and a fitness band with a small display](scenes/smartphones/potential_capacitance.svg "Glass, plastic, water on the screen: most of what is on this desk does not conduct. It still responds to a field.")

Farah is cooking dinner with a recipe video on her phone, and the screen is covered in fingerprints. She wipes it hard on the woollen scarf hanging by the kitchen door, then reaches past the sink to prop it up again.

As the phone passes the thin stream running from the tap, the stream **bends** — a clear kink, curving towards the glass. She pulls the phone away; the stream falls straight. Brings it back; it bends again.

Her younger brother Yusuf is fascinated. "Is the water charged?"

"It's tap water. It can't be."

"Then why does it care?"

They try the other end of the phone, which she hadn't rubbed. Nothing. So the rubbed glass is charged, and the water is being pulled. But water is neutral: as many plus charges as minus. A neutral thing has nothing to be attracted with — or does it?

## The physics

An insulator — a **dielectric** — has no free charges that can wander. But its molecules still respond to a field, in one of two ways:

- **Non-polar molecules** (no built-in dipole) have their electron clouds pulled one way and nuclei the other, so each becomes a small **induced dipole**.
- **Polar molecules**, like water, already have a dipole moment. Normally they point every which way; a field **turns** them partly into line with it.

Either way, the material becomes **polarised**: it gains a net dipole moment per unit volume, the **polarisation** $\vec{P}$. For most materials it is proportional to the field, $\vec{P} = \chi_e \vec{E}$, where $\chi_e$ is the **electric susceptibility**.

**Why the field inside is weaker.** Inside the slab, the $+$ end of each dipole sits beside the $-$ end of the next, and they cancel. Only the two faces are left over: a layer of **bound charge**, negative on the face where the field enters and positive on the face where it leaves. Those face charges make their own field, pointing **against** the applied field. So the field inside is reduced:

$$E = \frac{E_0}{K}$$

where $K = 1 + \chi_e$ is the **dielectric constant** (relative permittivity) of the material. $K = 1$ for vacuum, about $1$ for air, and about $80$ for water at room temperature.

![A dielectric slab in a field pointing right: molecular dipoles line up, leaving negative bound charge on the left face and positive on the right, and the field inside is weaker](figures/dielectrics_polarisation/dielectric-slab-polarised.svg "Inside, neighbouring dipole ends cancel. Only the two face layers are left over, and their field opposes the applied field.")

**Farah's water stream.** The water's molecules turn so their ends facing the charged glass carry the opposite sign. Those ends are slightly closer to the glass than the far ends, and the field near a small charged patch is stronger closer in. So the attraction wins over the repulsion, and the stream bends **towards** the glass — whichever sign the glass has.

## Worked example

A glass slab $2.0\,\text{mm}$ thick with $K = 5$ (illustrative) sits with its faces across a uniform field of $E_0 = 1000\,\text{V/m}$.

**Step 1 — the field inside.**

$$E = \frac{E_0}{K} = \frac{1000}{5} = 200\,\text{V/m}$$

**Step 2 — what the bound charges contribute.** Their field must be $1000 - 200 = 800\,\text{V/m}$, pointing against $E_0$. The glass has cancelled four-fifths of the field, while carrying no net charge at all.

**Step 3 — the voltage across the slab.** $V = Ed = 200 \times 2.0\times10^{-3} = 0.4\,\text{V}$. The same thickness of air would have $2.0\,\text{V}$ across it, five times as much.

**Sanity check:** with $K = 1$ the formula gives $E = E_0$ and no bound charge, which is exactly what empty space should do.

## Where the picture breaks

$E = E_0/K$ is for a slab with its faces across a **uniform** field. Farah's stream sits in the strongly non-uniform field of a small charged patch, and that non-uniformity is what makes a net pull possible — in a perfectly uniform field a polarised object feels no net force, only a twist. Tap water also contains dissolved ions that move a little, so conduction adds to the effect. And the rubbed glass loses its charge within seconds in a humid kitchen.

## Key takeaway

A dielectric has no free charge, but its molecules polarise in a field — induced dipoles, or polar molecules turning into line. The bound charges left on its faces oppose the applied field, so the field inside a slab across a uniform field falls to $E = E_0/K$, where $K$ is the dielectric constant. Neutral objects are attracted to charged ones because the polarisation puts the opposite charge nearer.
