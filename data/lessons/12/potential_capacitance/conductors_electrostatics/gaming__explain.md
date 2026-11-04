---
concept_id: conductors_electrostatics
interest: gaming
format: explain
title: Why the metal case takes the zap and the card does not
check:
  question: |-
    A hollow metal shell carries a charge $+Q$ spread over it, and there is nothing inside the cavity. What is true at a point inside the empty cavity?
  options:
    A: |-
      Both the field and the potential are zero, since there is no charge in the cavity.
    B: |-
      The field is zero at the exact centre by symmetry, but grows as you move towards the inner wall.
    C: |-
      The field is zero everywhere in the cavity, and the potential equals its value on the shell.
    D: |-
      The field is zero, but the potential is smaller than on the shell, because $V = kq/r$ falls off as you go inwards.
  answer: C
  explanation: |-
    Charge on a conductor arranges itself so that $E = 0$ throughout the metal and the cavity. With $E = 0$, $V$ cannot change from point to point, so the whole conductor and its hollow sit at one potential — the surface value.
  misconceptions:
    A: |-
      Assumes zero field implies zero potential. $V$ is fixed only up to where you put the zero; here the shell is at $kQ/R$ relative to infinity, and the cavity is at that same value. A constant potential means no field, not no potential.
    B: |-
      Thinks the cancellation inside a shell is a symmetry accident that works only at the centre. It is exact at every point — that is the result Gauss's law gives for any closed conductor, whatever its shape.
    D: |-
      Applies the point-charge formula $V = kq/r$ inside the shell. That formula holds only outside the charge distribution; inside, $V$ stops falling and stays flat at the surface value.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A gaming desk with a monitor showing rings of equal potential around a charge, a phone with a fingertip on its screen, an old picture tube on the bench and an opened power supply with two big capacitors](scenes/gaming/potential_capacitance.svg "The bare metal chassis of that power supply is doing more work than it looks. This lesson is about what a piece of metal does to a field.")

It is a dry January evening and Tanvi is installing more memory in her PC. She shuffles across the carpet in socks, reaches for the open case, and *crack* — a blue spark jumps from her knuckle to the metal frame, loud enough to make Rohan look up from the sofa.

Tanvi freezes. "Did I just kill the graphics card?"

Rohan tells her to boot it. Everything comes up fine. The card, the memory, the board — all of it untouched, sitting a few centimetres from where thousands of volts had just arrived.

"That's the whole reason the case is metal," he says, with more confidence than evidence.

Tanvi isn't satisfied. If a huge amount of charge lands on the frame, the field from that charge should reach everywhere nearby — including inside. Why should the delicate silicon a few centimetres away feel nothing at all?

## The physics

Start from one fact: in a conductor, some charges are free to move. Now apply the condition for **electrostatics** — nothing is moving. Everything else follows.

**1. The field inside the conductor is zero.** If $\vec{E}$ were not zero anywhere in the metal, it would push the free charges and they would move — which contradicts "electrostatic". So the free charges rearrange themselves until their own field exactly cancels whatever is applied, everywhere inside. That rearrangement takes a fraction of a nanosecond in a good conductor.

![A metal sphere with a cavity in a field pointing right: field lines bend to meet the surface at right angles, minus charges on the left, plus charges on the right, and E = 0 in the metal and in the cavity](figures/conductors_electrostatics/conductor-in-field.svg "The induced charges arrange themselves so that their field cancels the outside field everywhere inside, including in the hollow.")

**2. All excess charge sits on the outer surface.** Draw a Gaussian surface just inside the metal. Since $E = 0$ on it, the flux is zero, so by Gauss's law the charge enclosed is zero. Shrink the surface anywhere you like inside the metal and the answer is the same — so no net charge can live in the bulk. It has nowhere to go but the outer surface.

**3. The whole conductor is one equipotential.** Between any two points in the metal, $V_B - V_A = -\int \vec{E}\cdot \vec{d\ell} = 0$ because $E = 0$ along the way. So the surface and the interior sit at a single potential, and field lines must meet the surface at right angles.

**4. Just outside the surface**, the field is perpendicular to it with magnitude $E = \sigma/\varepsilon_0$, where $\sigma$ is the local surface charge density.

**5. Electrostatic shielding.** A cavity inside a conductor, with no charge in it, has $E = 0$ throughout, whatever is going on outside. That is Rohan's answer, and it is exact: the induced charges on the outer surface always arrange themselves to cancel the outside field within the metal *and* the hollow. It is why sensitive electronics live in metal boxes, and why a car is a safe place in a lightning storm.

## Worked example

Take the chassis as a simple stand-in: a solid metal sphere of radius $R = 10\,\text{cm}$ that picks up a charge $q = +6.0\,\text{nC}$ from a static discharge (illustrative values).

**Find:** the potential of the sphere, and the potential $30\,\text{cm}$ from its centre.

**Step 1 — the potential at the surface.** Outside a uniformly charged sphere, the charge acts as if it were all at the centre:

$$V_R = \frac{kq}{R} = \frac{9.0\times10^{9} \times 6.0\times10^{-9}}{0.10} = \frac{54}{0.10} = 540\,\text{V}$$

Every point inside the metal is at this same $540\,\text{V}$, and the field there is zero. The sphere is charged through and through in potential, but dead quiet in field.

**Step 2 — the potential at $30\,\text{cm}$.**

$$V = \frac{kq}{r} = \frac{54}{0.30} = 180\,\text{V}$$

Three times as far out, one third of the potential — the $1/r$ fall has restarted now that we are outside.

**Sanity check:** the potential is highest on the conductor and drops off outside, never the other way round — which is what you would expect if it takes work to push another positive charge towards the sphere.

## Where the picture breaks

The static shock is genuinely electrostatics, but a PC case is not a sealed metal sphere. It has vents, a glass panel and a hole for every cable, and a gap lets a field leak in — shielding is as good as the box is closed. Nor does a metal case make a build immune: a discharge *through* a component, say from your finger straight onto a memory module you are holding, is exactly what wrist straps are for. The clean results here also assume electrostatics — charges at rest. Radio waves from a wireless controller pass through the same case because they are time-varying fields, and a slot the size of a wavelength is a door rather than a wall. Finally, "$E = 0$ inside the cavity" needs the cavity to be **empty**; put a charge in it and the inner wall picks up an induced charge and the cavity has a field again.

## Key takeaway

Because free charges move until nothing pushes them, a conductor in electrostatic equilibrium has $E = 0$ inside, all its excess charge on the outer surface, and a single potential throughout. A hollow in it is shielded — the field there is zero no matter what happens outside. That is the physics of the metal case, and of a car in a thunderstorm.
