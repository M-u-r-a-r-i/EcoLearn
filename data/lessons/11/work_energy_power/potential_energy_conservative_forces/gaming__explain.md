---
concept_id: potential_energy_conservative_forces
interest: gaming
format: explain
title: Gravity charges for height, not for distance
check:
  question: |-
    In a climbing game a $60\,\text{kg}$ character goes from the valley floor to a ledge $15\,\text{m}$ higher. She takes a winding route $100\,\text{m}$ long instead of the $20\,\text{m}$ direct scramble. How much work does gravity do on her along the winding route? (Take $g = 9.8\,\text{m/s}^2$.)
  options:
    A: |-
      $-58\,800\,\text{J}$
    B: |-
      $-8820\,\text{J}$
    C: |-
      $+8820\,\text{J}$
    D: |-
      $0$
  answer: B
  explanation: |-
    Gravity is conservative, so only the height change counts: $W_\text{gravity} = -mgh = -(60)(9.8)(15) = -8820\,\text{J}$, the same on either route.
  misconceptions:
    A: |-
      Puts the $100\,\text{m}$ of path travelled into $mgh$ in place of the height; gravity acts straight down, so only the $15\,\text{m}$ of vertical rise enters the calculation.
    C: |-
      Gets the size right but the sign wrong; gravity points down while the character moves up, so its work is negative — it takes energy out of her motion and stores it as potential energy.
    D: |-
      Assumes that because the winding path is mostly sideways, gravity is perpendicular to the motion and does no work; it is perpendicular only on the level stretches, and every metre of rise still costs $mg$ per metre.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A gaming desk at night: a monitor shows a physics sandbox with a spring launcher, a kart at the top of a loop and a crate being dragged by a rope, beside a force-feedback racing wheel and a controller](scenes/gaming/work_energy_power.svg "Anything lifted in this sandbox — a crate, a kart, a character — is being given energy that can be taken back later.")

Ananya and her younger brother Vihaan have a race: first to the shrine on the cliff ledge in their open-world game. They start together at the river.

Ananya goes straight up the rock face, hauling herself up in a few brutal minutes with her stamina bar flashing red the whole way. Vihaan takes the goat track that loops lazily around the hill — five times the distance, but gentle, and his stamina never drops below half.

They arrive on the same ledge, at the same height, with very different bars.

"The long way is cheaper," Vihaan says. "Gravity's easier when you go sideways."

Ananya isn't sure that's what happened. Something about the climb clearly *was* the same for both of them — they are standing on the same rock, and if either jumped off they would land just as hard. But something else was clearly different. Which part of a climb does gravity actually charge you for?

## The physics

A force is **conservative** if the work it does between two points is the same along every path — and therefore zero around any closed loop. Gravity, the spring force and the electrostatic force are conservative. Friction and air drag are **non-conservative**: their work depends on the route, and it is always negative, so a round trip never gives your energy back.

![Two paths from A up to B, one short and straight, one long and winding: gravity does minus m g h on both, while friction does more negative work on the longer path](figures/potential_energy_conservative_forces/path-independence.svg "Gravity only counts the height gained. Friction charges for every metre of the route.")

Only a conservative force lets you define a **potential energy** — energy stored by position, which the force can hand back in full. Near the Earth's surface, lifting a mass $m$ through a height $h$ at constant speed takes work $mgh$ against gravity, and that is what gets stored:

$$U = mgh$$

with $g = 9.8\,\text{m/s}^2$, valid only close to the surface, where $g$ is effectively constant. Going up, gravity does $W = -mgh$; coming down it does $+mgh$ and gives every joule back.

Two conditions are worth keeping straight. First, **$h$ is measured from a level you choose** — the river, the ledge, sea level. Only *changes* in $U$ have physical meaning, so any zero will do as long as you keep it. Second, friction stores nothing: there is no "friction potential energy" to reclaim, because the work it does depends on the route and comes back as heat.

## Worked example

**Given** (illustrative game values): a character of mass $m = 50\,\text{kg}$ climbs from the river to a ledge $h = 20\,\text{m}$ above it. The rock rubs against her with a steady $20\,\text{N}$ along whichever route she takes.
**Find:** the potential energy she gains, and what the two routes cost her on top of it.

**Step 1 — the store gravity builds.** Taking the river as $h = 0$:

$$U = mgh = 50 \times 9.8 \times 20 = 9800\,\text{J}$$

Gravity does $-9800\,\text{J}$ on her going up, and would do $+9800\,\text{J}$ on the way down. This number is the same on both routes, because it depends only on the $20\,\text{m}$.

**Step 2 — the short route's rubbing cost.** Ananya climbs about $25\,\text{m}$ of rock:

$$W_\text{friction} = -20 \times 25 = -500\,\text{J}$$

**Step 3 — the long route's rubbing cost.** Vihaan covers about $120\,\text{m}$:

$$W_\text{friction} = -20 \times 120 = -2400\,\text{J}$$

So Vihaan actually spent nearly $2000\,\text{J}$ *more* in total — roughly the energy of a brisk two-minute jog — even though his climb felt easy. Gravity charged them both the same $9800\,\text{J}$; friction charged by the metre.

**Sanity check:** the gravity term used only the height, and the friction term only the length, which is exactly the difference between a conservative and a non-conservative force.

## Where the picture breaks

A stamina bar measures how hard something feels, not joules — a gentle slope is easier on a body than a vertical haul even when both store the same $9800\,\text{J}$, and your muscles waste energy as heat whichever way you go. The rubbing force in this example was made constant to keep the numbers clean; in reality it depends on the slope and the grip. And $U = mgh$ only works while $g$ is effectively constant: climb far enough above the surface and $g$ itself starts to fall, which is a later chapter.

## Key takeaway

A conservative force does the same work along every path, so the energy it takes can be stored as potential energy and given back in full; gravity near the Earth stores $U = mgh$, measured from whatever level you choose. A non-conservative force like friction charges for the route you took, and never gives anything back.
