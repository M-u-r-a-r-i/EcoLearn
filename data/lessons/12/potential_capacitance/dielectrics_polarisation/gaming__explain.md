---
concept_id: dielectrics_polarisation
interest: gaming
format: explain
title: How a touchscreen feels you through solid glass
check:
  question: |-
    A slab of dielectric with $K = 5$ is placed in a uniform external field of $1.0 \times 10^{5}\,\text{V/m}$. What is the field inside the slab, and what field do the bound charges alone produce?
  options:
    A: |-
      $2.0 \times 10^{4}\,\text{V/m}$ inside; the bound charges alone give $8.0 \times 10^{4}\,\text{V/m}$, opposing the applied field.
    B: |-
      $5.0 \times 10^{5}\,\text{V/m}$ inside; the dielectric strengthens the field by a factor $K$.
    C: |-
      $2.0 \times 10^{4}\,\text{V/m}$ inside; the bound charges alone give $2.0 \times 10^{4}\,\text{V/m}$.
    D: |-
      Zero inside, because the induced charges cancel the applied field completely.
  answer: A
  explanation: |-
    Inside a dielectric, $E = E_0/K = 1.0\times10^{5}/5 = 2.0\times10^{4}\,\text{V/m}$. The bound-charge field is the difference, $E_p = E_0 - E = 1.0\times10^{5} - 2.0\times10^{4} = 8.0\times10^{4}\,\text{V/m}$.
  misconceptions:
    B: |-
      Multiplies by $K$ instead of dividing. Polarisation opposes the applied field, so the field inside is always *weaker*; $K > 1$ goes in the denominator.
    C: |-
      Confuses the bound-charge field with the net field. $E_p$ is what must be subtracted from $E_0$ to leave $E$, so $E_p = E_0 - E$, not $E$.
    D: |-
      Treats a dielectric like a conductor. In a conductor free charges move until the cancellation is complete; in a dielectric the charges are bound to their molecules, can only shift slightly, and so reduce the field without ever wiping it out.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A gaming desk with a monitor showing rings of equal potential around a charge, a phone with a fingertip on its screen, an old picture tube on the bench and an opened power supply with two big capacitors](scenes/gaming/potential_capacitance.svg "A fingertip resting on a phone screen. Nothing conducts through that glass, and yet the phone knows the finger is there.")

Aarav has just put a thick tempered-glass protector on his phone, and he is annoyed about it. He plays a rhythm game that needs taps landing inside a few hundredths of a second, and he is convinced the extra glass will ruin it.

His sister Meera makes him test it before he peels it off. He plays a round. It works exactly as before.

"It shouldn't," Aarav says. "Glass is an insulator. Nothing gets through it. No charge moves from my finger to the screen — I checked, the sensor grid is *under* the glass."

Meera shrugs. "Try it with a glove on."

The glove kills it stone dead. So a layer of glass is transparent to whatever the screen is sensing, and a layer of cloth and rubber is not. Something is happening *inside* the glass that does not happen inside the glove. What does an electric field actually do to an insulator?

## The physics

A **dielectric** is an insulator: its electrons are bound to their molecules and cannot wander. Put it in an external field $\vec{E}_0$ and nothing flows — but something still happens.

**Two ways to polarise.** In a **non-polar** molecule the centres of positive and negative charge coincide until a field pulls them slightly apart, creating an induced dipole. In a **polar** molecule (water is the standard example) permanent dipoles already exist but point randomly; the field turns them, partially, against the jumbling of thermal motion. Either way the result is the same: a slab full of tiny dipoles all lined up with the field.

**Polarisation and bound charge.** Describe this by the **polarisation** $\vec{P}$, the dipole moment per unit volume. Inside the slab, the $+$ end of one molecule sits next to the $-$ end of its neighbour and they cancel. Only the two end faces are left over: a layer of negative **bound charge** where the field enters and positive where it leaves. These charges are not free to move — they cannot be drawn off with a wire.

![A dielectric slab in a field pointing right: molecular dipoles line up, leaving negative bound charge on the left face and positive on the right, and the field inside is weaker](figures/dielectrics_polarisation/dielectric-slab-polarised.svg "Inside, neighbouring dipole ends cancel. Only the two face layers are left over, and their field opposes the applied field.")

**The field is reduced.** Those two face layers make a field $\vec{E}_p$ of their own, pointing from the positive face back to the negative one — that is, **opposite** to $\vec{E}_0$. The net field inside is

$$E = E_0 - E_p = \frac{E_0}{K}$$

where $K$ is the **dielectric constant** of the material ($K > 1$, dimensionless; it is also written $\varepsilon_r$). The reduction is partial, never total: $K$ is finite because the bound charges can shift only a little. A conductor is the extreme case where the cancellation *is* complete, which is why you can think of it as $K \to \infty$.

This is Aarav's answer. His fingertip, a reasonably conducting bag of salty water, raises the potential at the surface; the field from it reaches straight through the glass to the sensor grid, weakened by $K$ but very much still there. The glove is thicker, has a smaller $K$, and holds his finger further away — so the signal falls below what the grid can pick out.

## Worked example

A slab of plastic with dielectric constant $K = 4$ is placed in a uniform field of $E_0 = 2.0 \times 10^{5}\,\text{V/m}$, with the slab faces perpendicular to the field.

**Find:** the field inside the slab, and the field produced by the bound charges alone.

**Step 1 — the field inside.**

$$E = \frac{E_0}{K} = \frac{2.0 \times 10^{5}}{4} = 5.0 \times 10^{4}\,\text{V/m}$$

A quarter of what was applied. The field has not been blocked — it has been damped.

**Step 2 — the bound-charge field.** It is whatever was subtracted:

$$E_p = E_0 - E = 2.0\times10^{5} - 5.0\times10^{4} = 1.5\times10^{5}\,\text{V/m}$$

pointing the opposite way to $E_0$, or three quarters of it. So the molecules of the slab are, between them, pushing back with three units of field for every four applied.

**Sanity check:** $E_p$ came out smaller than $E_0$. It had to — if the bound charges could produce as much field as was applied, the slab would be a conductor, not an insulator.

## Where the picture breaks

The touchscreen is a real place where a dielectric matters, but the phone is not doing electrostatics. The sensor grid drives the screen with a rapidly alternating voltage and watches how much charge a touch steals, so $K$ there is a response at some frequency, not the static value in a table. The tidy $E = E_0/K$ also assumes a **linear, isotropic** material in a field that is not too strong, with the slab faces square-on to the field — push a dielectric hard enough and it stops being linear, and eventually breaks down and conducts. And the picture of neat rows of aligned dipoles is a time-average: in a polar material the molecules are being knocked about constantly by heat, and only a small fraction are lined up at any instant.

## Key takeaway

An insulator in a field does not conduct, but its bound charges shift: induced or existing molecular dipoles line up, leaving a layer of bound charge on each face. Their field opposes the applied one, so the field inside drops to $E = E_0/K$, where the dielectric constant $K > 1$. The cancellation is partial — complete cancellation is what makes a conductor.
