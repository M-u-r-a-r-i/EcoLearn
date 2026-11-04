---
concept_id: reversible_irreversible
interest: motorsport
format: explain
title: Why a hot brake disc never pushes the car forward again
check:
  question: |-
    Which of these is closest to a reversible process?
  options:
    A: |-
      A car braking to a stop, since all of its kinetic energy is conserved as heat in the discs.
    B: |-
      Air compressed extremely slowly by a frictionless piston, in contact with surroundings at the same temperature.
    C: |-
      A hot brake disc cooling in the garage, since it can always be heated back to its starting temperature.
    D: |-
      Air rushing out of the wheel gun's bottle in a burst, since it is too fast for any heat to be exchanged.
  answer: B
  explanation: |-
    A reversible process must be quasi-static (always in equilibrium) and free of dissipation such as friction. Very slow, frictionless compression with no temperature difference is the only option that approaches both conditions.
  misconceptions:
    A: |-
      Thinks energy conservation makes a process reversible. The energy is all still there, but it has spread into the random jiggling of the disc's atoms, and it never gathers back to push the car.
    C: |-
      Thinks restoring the system alone is enough. Reheating the disc needs a heater or more braking, which leaves a change somewhere else; reversible means system and surroundings both return.
    D: |-
      Confuses adiabatic with reversible. A sudden burst is far from equilibrium, with uneven pressure and swirling air, so it is irreversible even with no heat flow.
author: claude-code/opus-5
written: 2026-09-25
---
## The story

![A pit lane in the afternoon sun: a stack of tyres in electric tyre blankets with a probe thermometer, a race car with a glowing front brake disc and a hot exhaust, and a compressed-air bottle feeding a wheel gun](scenes/motorsport/thermodynamics.svg "The glowing disc holds the energy the car had a moment ago. It will never give it back as speed.")

In the team's data room, Meera, a performance engineer, is showing her nephew Aditya onboard footage from a practice run. The car screams down the main straight at over $250\,\text{km/h}$, the driver stamps on the brakes, and in slow motion the front discs flare from grey to cherry red as the car slows for the hairpin.

"Where did all that speed go?" Aditya asks.

"Into the discs, mostly," says Meera. "That glow is the car's motion, turned into heat."

Aditya frowns. "Then it's not lost, is it? Energy is conserved. So all that energy is sitting in the brakes, and the car could just use it to speed up again."

Meera rewinds the clip and plays it backwards. The glowing discs fade to grey as the car accelerates away from the corner, faster and faster, with no engine sound. It looks completely absurd.

The first law has no objection to it. So why does the world only ever run one way?

## The physics

A process is **reversible** if it can be run backwards so that both the **system and its surroundings** return exactly to their original states, with no change left anywhere else in the universe. If that is impossible, the process is **irreversible**.

A process can be reversible only if two conditions hold:

1. **It is quasi-static.** The system passes through a series of equilibrium states, changing so slowly that its pressure and temperature are well defined at every instant, and it differs from its surroundings only by an infinitesimal amount (in pressure, temperature and so on).
2. **There is no dissipation.** No friction, no viscosity, no electrical resistance, nothing that turns ordered energy into random molecular motion.

![Left: a piston loaded with sand, grains removed one at a time so the gas stays in equilibrium; right: a pinned piston released suddenly so the gas swirls unevenly](figures/reversible_irreversible/quasi-static-vs-sudden.svg "Removing one grain at a time can be undone grain by grain. A sudden release cannot be undone by any small nudge.")

Real processes break one or both conditions. The main culprits:

- **Friction and other dissipation:** the brake pads rubbing on the disc turn the car's ordered motion into disordered jiggling of atoms.
- **Heat flowing across a finite temperature difference:** the red-hot disc cooling in the air.
- **Sudden, non-equilibrium changes:** air bursting out of a wheel gun, a tyre blow-out, fuel burning in a cylinder.
- **Mixing:** exhaust gases spreading into the air.

Every real process has at least one of these, so **every real process is irreversible**. A reversible process is an ideal limit, approached by doing things infinitely slowly with no friction, and it is useful because it sets the best any real machine could do.

That is why the reversed clip looks absurd. In braking, the energy is conserved, but it is scattered among countless atoms moving at random. Gathering it all back into the car's forward motion, with nothing else changing, is never seen.

## Worked example

**Given (illustrative):** an $800\,\text{kg}$ car travelling at $20\,\text{m/s}$ (that is, $72\,\text{km/h}$) brakes to a stop. Ignore air drag.
**Find:** how much energy ends up as heat, and what reversing the process would require.

**Step 1: the car's kinetic energy.**

$$K = \tfrac{1}{2}mv^2 = \tfrac{1}{2} \times 800 \times 20^2 = 160\,000\,\text{J} = 160\,\text{kJ}$$

**Step 2: where it goes.** The friction between pads and discs turns all $160\,\text{kJ}$ into internal energy of the brakes. That is enough energy to warm a $2\,\text{L}$ bottle of water by about $19\,^\circ\text{C}$.

**Step 3: the reverse.** To undo the stop, the discs would have to cool by themselves and pass exactly $160\,\text{kJ}$ back to the car as forward motion, with nothing else changing. The first law allows it; it simply never happens.

**Sanity check:** in everyday life you have seen many things brake to a stop and warm up, and never one that cooled down and started moving on its own, so a one-way process is exactly what we should expect.

## Where the picture breaks

Electric and hybrid cars can recover some braking energy: the motor runs as a generator and charges the battery (regenerative braking). That does not make braking reversible. The recovery is only partial, the electrical parts dissipate some energy as heat, and the discs still do part of the work. What regeneration does is avoid *some* of the irreversibility, which is exactly why engineers bother. The $160\,\text{kJ}$ also really spreads further than the discs: into the pads, the tyres and the air. And the "backwards clip" is just a picture; the real test is that system and surroundings must both be restored.

## Key takeaway

A reversible process can be undone with both the system and the surroundings restored exactly; it needs a quasi-static change and no dissipation. Friction, heat flow across a temperature difference, sudden expansion and mixing all make processes irreversible, so every real process is irreversible. Energy conservation alone does not make a process reversible.
