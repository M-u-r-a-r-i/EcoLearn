---
concept_id: reversible_irreversible
interest: cricket
format: explain
title: Why a replay run backwards looks impossible
check:
  question: |-
    Which of these is closest to a reversible process?
  options:
    A: |-
      Air in a pump compressed extremely slowly by a frictionless piston, in contact with surroundings at the same temperature.
    B: |-
      A ball rolling across the outfield until friction brings it to rest, since the total energy is conserved.
    C: |-
      Hot tea cooling on the dressing-room table, since it can always be reheated to its starting temperature.
    D: |-
      Air compressed very quickly in a well-insulated pump, since no heat escapes to the surroundings.
  answer: A
  explanation: |-
    A reversible process must be quasi-static (always in equilibrium) and free of dissipation such as friction. Very slow, frictionless compression with no temperature difference is the only option that approaches both conditions.
  misconceptions:
    B: |-
      Thinks energy conservation makes a process reversible. The energy is conserved, but it has spread into random thermal motion of the ball and grass, and it never gathers back to roll the ball.
    C: |-
      Thinks restoring the system alone is enough. Reheating the tea needs a stove or heater, which leaves a change in the surroundings; reversible means system and surroundings both return.
    D: |-
      Confuses adiabatic with reversible. A fast compression is far from equilibrium, with uneven pressure and swirling air, so it is irreversible even with no heat flow.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A hot afternoon at a cricket ground: blazing sun, a board showing 38 degrees, a bowler polishing the ball, a generator with hot exhaust and an ice box of drinks](scenes/cricket/thermodynamics.svg "Everything in this scene runs one way in time: the ice melts, the exhaust spreads, the ball warms.")

In the broadcast van, Lakshmi, a video operator, is training a new colleague, Rahul, on the replay system. To show off the controls, she takes a clip of a fielder's throw landing short. The ball thuds onto the pitch, bounces a few times, each bounce lower, and rolls to a stop on the grass.

Then she plays it backwards.

The ball lies still. Suddenly it starts rolling on its own, faster and faster, then leaps off the pitch in bigger and bigger bounces and flies into a fielder's hand. Rahul laughs. "Nobody would believe that."

"Why not?" says Lakshmi. "Every frame obeys the laws of motion. And energy is conserved both ways: going forwards, the ball's energy went into the grass and the ball as heat. Going backwards, the heat just comes back."

Rahul stops laughing. She's right that energy is conserved either way. So what, exactly, is forbidden about the backwards version?

## The physics

A process is **reversible** if it can be run backwards so that **both the system and its surroundings** return exactly to their original states, with no change left anywhere. Otherwise it is **irreversible**.

A process can be reversible only if two conditions hold:

1. It is **quasi-static**: carried out so slowly that the system passes through a continuous chain of equilibrium states, with uniform pressure and temperature at every moment, and differing from its surroundings only infinitesimally.
2. It has **no dissipative effects**: no friction, viscosity, electrical resistance or other effect that turns ordered energy into random thermal motion.

![Left: a piston loaded with sand, grains removed one at a time so the gas stays in equilibrium; right: a pinned piston released suddenly so the gas swirls unevenly](figures/reversible_irreversible/quasi-static-vs-sudden.svg "Removing one grain at a time can be undone grain by grain. A sudden release cannot be undone by any small nudge.")

Every real process breaks at least one condition, so **every real process is irreversible**. There are two main culprits:

- **Finite speed and differences.** Heat flowing across a real temperature difference, or a gas expanding suddenly with uneven pressure and eddies, passes through non-equilibrium states. The system cannot be nudged back along the same path.
- **Dissipation.** Friction and drag turn the ball's ordered kinetic energy, every molecule moving together, into disordered thermal motion, molecules jiggling at random. Energy conservation would allow the reverse, but the random jiggling of billions of molecules never lines up by itself to push the ball in one direction.

That is Rahul's answer. Nothing in the backwards replay breaks energy conservation. What it breaks is the one-way character of real processes, which the second law of thermodynamics makes precise. Reversible processes are an idealisation, the limit that real processes approach, and they set the best performance any engine can achieve.

## Worked example

**Given (illustrative):** a ball of mass $0.16\,\text{kg}$ is dropped from $2.0\,\text{m}$ onto the pitch and rebounds to only $0.50\,\text{m}$. Take $g = 9.8\,\text{m/s}^2$ and ignore air resistance.
**Find:** the mechanical energy dissipated in one bounce, and what a reversed bounce would require.

Energy at the top before: $mgh_1 = 0.16 \times 9.8 \times 2.0 = 3.14\,\text{J}$.
Energy at the top after: $mgh_2 = 0.16 \times 9.8 \times 0.50 = 0.784\,\text{J}$.
Dissipated: $3.14 - 0.784 \approx 2.4\,\text{J}$, into thermal energy of the ball and pitch, and a little sound.

To run the bounce backwards, $2.4\,\text{J}$ of random molecular motion in the ball and pitch would have to concentrate itself into one upward push. Energy conservation allows it; it is never observed.

**Sanity check:** directly, $mg(h_1 - h_2) = 0.16 \times 9.8 \times 1.5 = 2.35\,\text{J}$, the same.

## Where the picture breaks

A bouncing ball is a mechanical example; thermodynamics textbooks usually talk about gases and heat. The principle is the same, but the replay story shows the effect of irreversibility, not the full law behind it; that comes with the second law. And a video can always be reversed: the point is that the reversed events would not happen in nature, not that they break any single law of motion.

## Key takeaway

A reversible process can be undone with system and surroundings both restored. That requires quasi-static change and no dissipation. Real processes involve friction, finite temperature and pressure differences, and fast changes, so every real process is irreversible. Energy conservation alone does not decide which way things run.
