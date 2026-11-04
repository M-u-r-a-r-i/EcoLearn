---
concept_id: reversible_irreversible
interest: football
format: explain
title: The air that will never go back into the ball
check:
  question: |-
    A ball is punctured inside a closed store room. Its air hisses out and spreads through the room; not one molecule has left the building, and no energy has been destroyed. Which statement is correct?
  options:
    A: |-
      The process is irreversible because energy was destroyed when the air escaped.
    B: |-
      The process is reversible, because the air can simply be pumped back into the ball.
    C: |-
      The process is irreversible: the air can only be put back by doing work, which leaves a permanent change in the surroundings.
    D: |-
      The process is reversible in principle, because every molecule obeys Newton's laws and energy is conserved throughout.
  answer: C
  explanation: |-
    A process is reversible only if the system *and* its surroundings can both be returned to their original states. Refilling the ball needs a pump doing work, and that work leaves changes outside the ball that cannot be undone, so the escape is irreversible.
  misconceptions:
    A: |-
      Thinks irreversibility means energy has been lost. Energy is conserved exactly; what has changed is that it is now spread out and disordered instead of concentrated.
    B: |-
      Thinks restoring the system alone is enough. Reversible means the surroundings come back unchanged too, and a pump leaves behind heat, wear and the energy its user spent.
    D: |-
      Thinks that because every microscopic step is allowed, the whole process can run backwards. No single collision is forbidden; what never happens is billions of them lining up together to refill the ball.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A training ground on a hot day: a board reading 36 degrees Celsius, an ice box of drinks, a player inflating a ball with a hand pump, and a mower with a hot exhaust](scenes/football/thermodynamics.svg "Everything here runs one way in time: the drinks warm, the exhaust spreads, the pumped-up balls slowly soften.")

The store room behind the changing block has no window and one door, and the door is shut. Nikhil is in there counting cones when a ball he has just set down on a shelf gives a long, quiet hiss. By the time he picks it up it is half soft. Somewhere in the casing there is a thorn hole.

Asha, the kit manager, is unimpressed. "Third one this month."

Nikhil, who has just finished the first-law chapter, thinks it through and finds himself stuck. The air is still here. Every molecule of it is in this sealed room; nothing has escaped the building and nothing has been destroyed. Energy is conserved — the air that left the ball carried its energy with it into the room.

"So if I wait," he says, "some of it should wander back in through the hole. Nothing in physics says it can't."

Asha laughs and hands him the pump.

She is right, and Nikhil knows she is right. But *why* is she right? Which law, exactly, says the air will never go home by itself?

## The physics

A process is **reversible** if it can be run backwards so that **both the system and its surroundings** end up exactly as they started, with no trace left anywhere. Anything else is **irreversible**.

Two conditions must hold for a process to be reversible:

1. It is **quasi-static**: carried out so slowly that the system passes through an unbroken chain of equilibrium states, with uniform pressure and temperature throughout, differing from its surroundings only infinitesimally at every moment.
2. It has **no dissipative effects**: no friction, no viscosity, no turbulence, no electrical resistance — nothing that turns ordered energy into random molecular motion.

![Left: a piston loaded with sand, grains removed one at a time so the gas stays in equilibrium; right: a pinned piston released suddenly so the gas swirls unevenly](figures/reversible_irreversible/quasi-static-vs-sudden.svg "Removing one grain at a time can be undone grain by grain. A sudden release cannot be undone by any small nudge.")

Every real process breaks at least one condition, so **every real process is irreversible**. There are two usual culprits:

- **Finite differences and finite speed.** Nikhil's ball had air at roughly twice room pressure rushing out through a pinhole into air at room pressure. During that rush the gas is nowhere near equilibrium — it is uneven, swirling and noisy. A system that has passed through non-equilibrium states cannot be nudged back along the same path. The same is true of heat flowing across a real temperature difference.
- **Dissipation.** Friction and drag take ordered energy, where every molecule moves together, and scatter it into disordered thermal motion. Energy conservation would happily allow the reverse; it is simply never observed.

That is Asha's answer. Nothing in the escape broke energy conservation, and no single collision in it was forbidden. What it broke is the one-way character of real change, which the second law of thermodynamics — next — states precisely. You *can* get the air back, but only by doing work with a pump, and that leaves permanent changes outside the ball. The system returns; the surroundings do not.

Reversible processes are an idealisation, the limit that careful, slow, frictionless processes approach without reaching. They matter because they set the best performance any engine can ever have.

## Worked example

**Given (illustrative):** a ball of about $0.4\,\text{kg}$ is rolled across the pitch at $5\,\text{m/s}$ and comes to rest on the grass.
**Find:** how much mechanical energy is dissipated, and what running the process backwards would demand.

All of its kinetic energy goes, since it ends at rest:

$$E = \tfrac{1}{2}mv^2 = \tfrac{1}{2}(0.4)(5)^2 = 5\,\text{J}$$

Those $5\,\text{J}$ are now spread through the grass, the ball's casing and the air as extra random jiggling — a temperature rise far too small to feel.

To run the process backwards, that $5\,\text{J}$ of random jiggling would have to gather itself up and push the ball off in one direction at $5\,\text{m/s}$. Energy conservation permits it. Nobody has ever seen it.

**Sanity check:** $5\,\text{J}$ is about what it takes to lift that ball to chest height, which is a believable amount of energy for a gentle roll to carry.

## Where the picture breaks

The escaping air is a leaky system, not a closed one, so it is an example of irreversibility rather than a case you can apply the closed-system first law to directly. The rolling ball is a mechanical example, while thermodynamics textbooks usually argue with gases and heat; the lesson transfers, but the formal statement of the law does not come until the second law. And "irreversible" is a statement about what is overwhelmingly probable, not about what is logically impossible — a point you will meet again when entropy is defined properly.

## Key takeaway

A process is reversible only if system *and* surroundings can both be restored, which requires quasi-static change and no dissipation. Real processes involve friction, turbulence and finite differences of pressure and temperature, so every real process is irreversible. Energy conservation alone never tells you which way a process will run.
