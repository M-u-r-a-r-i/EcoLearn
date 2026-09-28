---
concept_id: reversible_irreversible
interest: smartphones
format: explain
title: Why a reversed phone drop test looks fake
check:
  question: |-
    Which of these is closest to a reversible process?
  options:
    A: |-
      A phone battery warming up as it is charged, since it can be discharged again afterwards.
    B: |-
      A hot phone cooling down on a desk after a long game, since it can be warmed up again later.
    C: |-
      Gas rushing out of a can of compressed air, since the can could be refilled from a pump.
    D: |-
      Gas in a cylinder compressed extremely slowly by a frictionless, perfectly fitting piston.
  answer: D
  explanation: |-
    A frictionless, extremely slow (quasi-static) compression passes through equilibrium states with no dissipation, so it could be run backwards step by step, restoring both the gas and its surroundings. The other three each involve dissipation, heat flow across a finite temperature difference, or a sudden change.
  misconceptions:
    A: |-
      Thinks that because charging can be followed by discharging, the process is reversible. Current through the battery's resistance wastes energy as heat on the way in and on the way out, and that heat is never recovered.
    B: |-
      Thinks a process is reversible if the system can be brought back to its start by any means. Reheating the phone uses energy from elsewhere and leaves a change in the surroundings; heat flowing across a finite temperature difference is irreversible.
    C: |-
      Thinks being able to refill the can makes the escape reversible. The sudden rush of gas is far from equilibrium, and pumping it back takes extra work that leaves the surroundings changed.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A sunny room: a phone sealed in a puffed-up waterproof pouch on a windowsill, a phone charging on a desk seen through a clip-on thermal camera, an icy can of compressed air, and a wall air conditioner controlled from a phone app](scenes/smartphones/thermodynamics.svg "Nothing in this room runs backwards: the can won't refill itself, and the warm cable won't cool to recharge the phone.")

Siddharth runs a small channel that tests phone cases. His most popular videos are drop tests: he holds a phone in a case at shoulder height, lets it fall onto a sofa cushion, then onto a rug, then onto tiles, filmed in slow motion.

This week, for fun, his sister Aanya edits one clip to play backwards. The phone lies on the cushion, the cushion's dent smooths out, and the phone leaps up into Siddharth's waiting hand.

The comments pour in within minutes. *Obviously reversed.* *Fake.* *Physics doesn't work like that.*

"But why is it obvious?" Aanya asks. "Nothing in it breaks a law I know. The phone had energy at the top and the cushion had it at the bottom. Played backwards, the cushion just gives the energy back. Energy is still conserved."

Siddharth has no answer. Everyone can *see* the reversed clip is wrong. What exactly is it that never happens?

## The physics

A process is **reversible** if it can be run backwards so that both the **system and its surroundings** return exactly to their original states, with no change left anywhere else in the universe. If that is impossible, the process is **irreversible**.

A process can be reversible only if two conditions hold:

1. **It is quasi-static.** The system passes through a series of equilibrium states, changing so slowly that its pressure and temperature are well defined at every instant, and it differs from its surroundings only by an infinitesimal amount.
2. **There is no dissipation.** No friction, no viscosity, no electrical resistance, nothing that turns ordered energy into random molecular motion.

![Left: a piston loaded with sand, grains removed one at a time so the gas stays in equilibrium; right: a pinned piston released suddenly so the gas swirls unevenly](figures/reversible_irreversible/quasi-static-vs-sudden.svg "Removing one grain at a time can be undone grain by grain. A sudden release cannot be undone by any small nudge.")

Real processes break one or both conditions. The main culprits, all found on a gadget desk:

- **Friction and other dissipation:** the cushion's fibres rubbing as it squashes; current flowing through a battery's internal resistance.
- **Heat flowing across a finite temperature difference:** a hot phone cooling in room air.
- **Sudden, non-equilibrium changes:** gas rushing out of a can of compressed air.
- **Mixing:** that gas spreading out into the room.

Every real process has at least one of these, so **every real process is irreversible**. A reversible process is an ideal limit, approached by doing things infinitely slowly with no friction, and it is useful because it sets the best any real machine could do.

That is why the reversed clip looks fake. When the phone lands, its ordered downward motion, every atom moving together, is scattered into random jiggling of countless atoms in the cushion and the case. The first law would allow all that jiggling to gather itself back into one upward push, but it is never seen.

## Worked example

**Given (illustrative):** a $0.2\,\text{kg}$ phone is dropped from $1\,\text{m}$ onto a sofa cushion and comes to rest. Take $g = 9.8\,\text{m/s}^2$ and ignore air drag.
**Find:** how much energy ends up as internal energy, and what reversing the process would require.

**Step 1: the phone's energy at the top.**

$$mgh = 0.2 \times 9.8 \times 1 \approx 2\,\text{J}$$

**Step 2: where it goes.** Just before landing, that $2\,\text{J}$ is kinetic energy. The cushion squashes, its fibres rub and flex, and the phone stops. Almost all $2\,\text{J}$ ends up as internal energy of the cushion and the phone, a warming far too small to feel, plus a little sound.

**Step 3: the reverse.** To undo the drop, that $2\,\text{J}$ would have to flow back out of randomly jiggling atoms, all at once, into one upward push that lifts the phone exactly $1\,\text{m}$, with nothing else changing. The first law allows it; it simply never happens.

**Sanity check:** you have seen thousands of objects fall and stop, and never one that sprang up from rest on its own, so a one-way process is exactly what we should expect.

## Where the picture breaks

A bouncy surface would give some of the energy back as a rebound, so a drop is not a clean "all lost" case; only the part that becomes random motion is gone for good. The small warming of the cushion is real but far too tiny to measure without sensitive instruments. Nor does "irreversible" mean the phone can never get back to his hand: Siddharth can pick it up. But doing so uses energy from his muscles, which leaves a change elsewhere, and that is exactly what the definition of reversible rules out.

## Key takeaway

A reversible process can be run backwards, returning both system and surroundings to their original states. It must be quasi-static and free of dissipation. Friction, resistance, heat flowing across a finite temperature difference, sudden changes and mixing make every real process irreversible; reversible processes are an ideal limit.
