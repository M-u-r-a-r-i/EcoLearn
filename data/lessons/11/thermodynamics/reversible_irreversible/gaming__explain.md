---
concept_id: reversible_irreversible
interest: gaming
format: explain
title: The rewind button that reality does not have
check:
  question: |-
    Which of these is closest to a reversible process?
  options:
    A: |-
      The gas in a chair's lift cylinder compressed a hair at a time by a frictionless piston, always at the temperature of the room around it.
    B: |-
      A racing game's rewind, since the crash is undone exactly, frame by frame, and nothing is left behind.
    C: |-
      A case fan coasting to a stop after you cut its power, since you can always switch it on again.
    D: |-
      The gas in a well-insulated duster can expanding fast during a blast, since no heat escapes to the surroundings.
  answer: A
  explanation: |-
    A reversible process must be quasi-static — always in equilibrium, never more than infinitesimally different from its surroundings — and free of dissipation such as friction. Only the slow, frictionless, same-temperature compression comes close to both conditions.
  misconceptions:
    B: |-
      Confuses a simulation being rewound with a physical process being reversed. Reversibility is a claim about what can happen in the world, not about what a program can redraw.
    C: |-
      Thinks restoring the system is enough. Switching the fan on again takes fresh electrical work and warms the room further, so the surroundings do not return to their original state.
    D: |-
      Confuses adiabatic with reversible. A fast expansion has uneven pressure and swirling gas, so it is nowhere near equilibrium and is irreversible even with no heat flow at all.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A gaming desk at night: a monitor showing GPU and CPU temperatures, a tower PC with a heat sink and fans, hot air leaving the top and cool air drawn in, a can of compressed-air duster, a mini fridge under the desk and a backup generator outside the window](scenes/gaming/thermodynamics.svg "Everything in this room runs one way in time: the hot air spreads, the cold drinks warm, the fans wear out.")

Aditi is showing her cousin Farhan the rally game she has been playing all week. She takes the last corner too fast, clips the barrier and puts the car into a spin, and the screen fills with dust and sparks.

Then she taps a button on the controller, and the crash runs backwards.

The dust gathers itself off the air and packs back into the verge. The sparks fly back into the barrier. The dented panel un-dents. The car straightens, unspins, and rolls smoothly back up the road, and Aditi picks up the corner again three seconds before her mistake.

Farhan laughs. "If only."

"Why not?" says Aditi. "Every frame there obeys Newton's laws. And nothing was destroyed in the crash — the car's energy went into heating the barrier, the tyres and the air. Running it backwards, the heat just comes back out."

Farhan stops laughing, because she is right about the energy. Both directions balance the books exactly. So what, precisely, is forbidden about the backwards version?

## The physics

A process is **reversible** if it can be run backwards in such a way that **both the system and its surroundings** end up exactly as they started, with no trace left anywhere. Anything else is **irreversible**.

A process can be reversible only if two conditions hold:

1. It is **quasi-static**: carried out so slowly that the system passes through a continuous chain of equilibrium states, with a single well-defined pressure and temperature at every instant, differing from its surroundings only infinitesimally.
2. It has **no dissipative effects**: no friction, no viscosity, no electrical resistance — nothing that turns ordered energy into random molecular motion.

![Left: a piston loaded with sand, with grains removed one at a time so the gas stays in equilibrium; right: a pinned piston released suddenly so the gas swirls unevenly](figures/reversible_irreversible/quasi-static-vs-sudden.svg "Removing one grain at a time can be undone one grain at a time. A sudden release cannot be undone by any small nudge.")

Every real process breaks at least one of these, so **every real process is irreversible**. There are two usual culprits:

- **Finite speed and finite differences.** Heat crossing a real temperature gap, or a gas expanding suddenly with uneven pressure and eddies, passes through states that are not equilibrium states at all. There is no path to retrace, because the system was never on a well-defined path.
- **Dissipation.** Friction and drag take ordered kinetic energy — every molecule of the car moving the same way — and scatter it into disordered thermal motion of the barrier, the tyres and the air. Energy conservation would permit the reverse; it simply never happens, because the random jiggling of billions of molecules does not spontaneously line up and push in one direction.

That is Farhan's answer. Nothing in the reversed clip breaks energy conservation. What it breaks is the one-way character of real change, and the second law of thermodynamics is what makes that precise. Reversible processes are an idealisation — the limit that real processes approach as you make them slower and smoother — and they set the ceiling on what any engine can achieve.

## Worked example

**Given (illustrative):** the remote-controlled car Aditi had as a child, of mass $0.50\,\text{kg}$, is rolling at $2.0\,\text{m/s}$ across a tiled floor when its battery dies. It coasts $4.0\,\text{m}$ and stops.
**Find:** the mechanical energy dissipated, and what a reversed version would require.

All the kinetic energy it had is gone by the end, so the energy dissipated is the kinetic energy it started with:

$$E = \tfrac{1}{2}mv^2 = \tfrac{1}{2}(0.50)(2.0)^2 = 1.0\,\text{J}$$

One joule, spread as extra thermal motion through the wheels, the bearings and a four-metre strip of floor. To run the coast backwards, that same joule of random jiggling would have to gather itself out of the tiles and the axles and push, all at once, in one direction. Energy conservation permits it. Nobody has ever seen it.

**Sanity check:** a joule is about what it takes to lift a small apple one metre — a believable amount for a toy car rolling to a stop, and small enough that the floor's temperature rise is far too tiny to feel.

## Where the picture breaks

A rolling car is a mechanical example, while thermodynamics usually argues about gases and heat; the story shows you irreversibility in action but not the law behind it, which arrives with the second law. A game's rewind is not a physical process at all — it is a program restoring saved numbers, and doing so costs the machine electricity and warms the room a little more. And a video can always be played backwards: the claim is not that the reversed frames break any single law of motion, but that the events they show do not occur in nature.

## Key takeaway

A reversible process can be undone with both the system and its surroundings fully restored, which demands quasi-static change and no dissipation. Real processes have friction, finite temperature and pressure differences, and finite speed, so every real process is irreversible. Energy conservation alone never tells you which way things will run.
