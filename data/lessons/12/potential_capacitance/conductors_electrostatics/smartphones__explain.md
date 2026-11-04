---
concept_id: conductors_electrostatics
interest: smartphones
format: explain
title: The phone that lost its signal inside a biscuit tin
check:
  question: |-
    A closed, hollow metal box is given a charge of $+5\,\text{nC}$. Nothing is charged inside the hollow. Treating everything as electrostatic, what is the electric field inside the empty hollow?
  options:
    A: |-
      Strongest close to the walls, weakening towards the centre.
    B: |-
      Uniform, and equal to the field just outside the box's surface.
    C: |-
      Zero at the exact centre only, where the pulls of all the walls balance.
    D: |-
      Zero everywhere in the hollow.
  answer: D
  explanation: |-
    The charge sits on the outer surface and arranges itself so the field inside the conductor, and in any empty cavity within it, is zero everywhere. That is electrostatic shielding.
  misconceptions:
    A: |-
      Pictures the walls' charges acting like nearby point charges on whatever is close to them. The surface charges arrange themselves so that all their contributions cancel at every point inside, not just some.
    B: |-
      Carries the outside field through the metal. The field just outside a charged conductor is $\sigma/\varepsilon_0$, but inside the conductor and its empty cavity it is zero.
    C: |-
      Thinks the cancellation happens only at a point of symmetry. For a closed conductor with no charge in its cavity, the field is zero at every point in the cavity, whatever the box's shape.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A desk by a rainy window: a phone with raindrops on its screen being tapped by a finger, a metal biscuit tin with its lid off, a breadboard with two supercapacitor cells wired in a chain, a stylus and a fitness band with a small display](scenes/smartphones/potential_capacitance.svg "An ordinary steel biscuit tin, lid off. With the lid on, it becomes a surprisingly good hiding place.")

Exams are a week away, and Tanya has made herself a rule: phone goes into Nani's old steel biscuit tin, lid on, until nine o'clock. Her brother Dev thinks this is funny, so he calls her from the next room to prove the rule is pointless.

He gets a recorded message: the number is not reachable.

He frowns and tries again. Same message. Tanya opens the tin; her phone shows barely any signal. She shuts it; he calls; unreachable. They try three times.

"It's a thin tin," Dev says. "The signal comes through the brick walls of this house. How does a sheet of metal half a millimetre thick stop it dead?"

Tanya has no answer — but she has noticed something else. The tin works with the lid on, and fails with the lid off. It isn't how thick the metal is. It's that the metal goes all the way round.

## The physics

A conductor contains **free electrons** that move whenever a field pushes on them. Put a conductor in a field and they drift until the charges they leave behind create a field that exactly cancels the outside one. Then nothing moves any more, and that is **electrostatic equilibrium**. From that one idea come four results:

1. **$E = 0$ everywhere inside the material of a conductor.** Otherwise the free electrons would still be moving.
2. **Any extra charge sits on the surface.** A Gaussian surface drawn just inside the metal has $E = 0$ at every point, so by Gauss's law it encloses no net charge.
3. **Just outside, the field is perpendicular to the surface**, with size $E = \sigma/\varepsilon_0$, where $\sigma$ is the local surface charge density. A sideways component would push charges along the surface.
4. **The whole conductor is at one potential.** With $E = 0$ inside, no work is done moving a charge anywhere through it, so its surface is an equipotential.

![A metal sphere with a cavity in a field pointing right: field lines bend to meet the surface at right angles, minus charges on the left, plus charges on the right, and E = 0 in the metal and in the cavity](figures/conductors_electrostatics/conductor-in-field.svg "The induced charges arrange themselves so that their field cancels the outside field everywhere inside, including in the hollow.")

**Shielding.** Hollow the conductor out. If there is no charge in the cavity, the field inside the cavity is **zero** too, whatever happens outside and whatever charge the conductor carries. A closed metal box shields its inside from external electrostatic fields — **electrostatic shielding**. That is why the lid matters: the effect needs the metal to enclose the space.

## Worked example

Treat the tin, lid on, as a metal sphere of radius $R = 10\,\text{cm}$ carrying $Q = +2.0\,\text{nC}$ (illustrative). Use $\dfrac{1}{4\pi\varepsilon_0} = 9.0\times10^9\,\text{N m}^2\text{C}^{-2}$.

**Step 1 — the field inside.** The charge sits on the outer surface; the hollow is empty. So $E = 0$ at every point inside, near the wall or at the centre.

**Step 2 — the potential of the tin.** Outside, a charged sphere acts like a point charge at its centre, so at its surface

$$V = \frac{9.0\times10^9 \times 2.0\times10^{-9}}{0.10} = 180\,\text{V}$$

With $E = 0$ inside, the potential never changes as you go in: the whole hollow is at $180\,\text{V}$.

**Step 3 — the field just outside.**

$$E = \frac{9.0\times10^9 \times 2.0\times10^{-9}}{(0.10)^2} = 1800\,\text{V/m}$$

pointing straight out from the surface.

**Sanity check:** a phone inside the tin sits at $180\,\text{V}$ along with everything around it, so there is no potential *difference* across it and no push on its charges — being at a high potential is harmless; differences are what matter.

## Where the picture breaks

A phone signal is not an electrostatic field. It is a radio wave, a field that reverses billions of times a second, and this chapter's argument is strictly about fields that do not change. The shielding idea does carry over — a metal enclosure also blocks radio waves, provided the gaps in it are much smaller than the wavelength (roughly $10$ to $30\,\text{cm}$ at mobile frequencies) — but proving it needs the electromagnetic waves chapter. A real biscuit tin also has a loose lid with gaps, so it often lets a weak signal through; Tanya's result will vary from tin to tin.

## Key takeaway

In electrostatics the field inside a conductor is zero, any extra charge lives on its surface, the field just outside is perpendicular to the surface with $E = \sigma/\varepsilon_0$, and the whole conductor is one equipotential. An empty cavity inside a conductor also has zero field — electrostatic shielding — as long as the metal encloses it completely.
