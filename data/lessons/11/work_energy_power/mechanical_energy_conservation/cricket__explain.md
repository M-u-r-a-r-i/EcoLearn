---
concept_id: mechanical_energy_conservation
interest: cricket
format: explain
title: How fast a skier comes down into your hands
check:
  question: |-
    Two skiers are hit from the same height at $20\,\text{m/s}$: one straight up, the other at $60^\circ$ above the horizontal. Ignoring air resistance, how do their speeds compare when each falls back to the height it was hit from?
  options:
    A: |-
      The one hit straight up is faster, because it climbed higher and had further to fall.
    B: |-
      The one hit at $60^\circ$ is faster, because its horizontal motion adds to its falling speed.
    C: |-
      Both are moving at $20\,\text{m/s}$.
    D: |-
      Both are moving faster than $20\,\text{m/s}$, because gravity speeds them up on the way down.
  answer: C
  explanation: |-
    Only gravity does work, so $K + U$ stays constant. Each ball returns to its starting height with the same $U$, so it has the same $K$ as at the start — $20\,\text{m/s}$ — whatever its angle.
  misconceptions:
    A: |-
      Counts only the energy gained while falling and forgets the energy lost while climbing; the extra height gives back exactly the speed it cost, no more.
    B: |-
      Adds the horizontal speed on top of the returning speed; the horizontal part was there from the start and is already part of the $20\,\text{m/s}$.
    D: |-
      Thinks gravity gives net energy over a round trip; it takes energy away going up and returns the same amount coming down, so the net work is zero.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A cricket ground by day: a batter watches a ball climb high, a fielder waits under it, a player runs up the stadium steps and a groundsman pushes a roller](scenes/cricket/work_energy_power.svg "A skier: the ball climbs, stops for a moment near the top, and falls back towards the waiting fielder.")

The batter gets a top edge, and the ball climbs almost straight up above the pitch — a towering skier. Sneha, at mid-wicket, calls "Mine!" and settles underneath it, eyes up, hands ready.

The ball keeps rising. And rising.

From square leg, Varun shouts helpfully, "Careful! It's going to come down way faster than it went up!"

Sneha isn't so sure. The batter's edge sent it up at maybe $85\,\text{km/h}$. Gravity slowed it all the way up, and now gravity will speed it up all the way down. Does the ball gain more than it lost? What speed will it actually have when it lands in her hands, and how high did it go?

## The physics

Kinetic energy and potential energy together make up **mechanical energy**:

$$E = K + U$$

**The principle of conservation of mechanical energy:** if only conservative forces do work on a body, its total mechanical energy stays constant.

$$K_i + U_i = K_f + U_f$$

**Why it follows.** The work-energy theorem says the work done by all forces equals $\Delta K$. If only conservative forces act, that work also equals $-\Delta U$ (the definition of potential energy). So $\Delta K = -\Delta U$, which means $\Delta K + \Delta U = 0$, and $K + U$ doesn't change. Whatever kinetic energy is lost reappears as potential energy, and vice versa.

For Sneha's skier, gravity is the only force that matters if we ignore air. Going up, $K$ turns into $U = mgh$. At the top, the ball hit straight up is momentarily at rest, with all its energy as $U$. Coming down, $U$ turns back into $K$. At the height it started from, it has exactly its starting $K$ back. So Varun is wrong: it arrives no faster than it left.

If **non-conservative** forces such as air drag do work $W_\text{nc}$, then $E_f = E_i + W_\text{nc}$. Drag's work is negative, so mechanical energy drains away.

![Graph of energy against height for a ball hit straight up at 24 metres per second: kinetic energy falls in a straight line, potential energy rises in a straight line, and their total stays at 46 joules](figures/mechanical_energy_conservation/ke-pe-vs-height.svg "Every metre climbed moves the same amount of energy from K to U. The dashed total never changes.")

## Worked example

**Given** (illustrative): ball mass $m = 0.16\,\text{kg}$; it leaves the bat at $v_0 = 24\,\text{m/s}$ straight up, $1.0\,\text{m}$ above the ground; Sneha catches it $1.5\,\text{m}$ above the ground; $g = 9.8\,\text{m/s}^2$; no air resistance.
**Find:** the greatest height, the speed $20\,\text{m}$ above the bat, and the speed at the catch.

Measure heights from the bat, so $U = 0$ there. Total energy:

$$E = \tfrac{1}{2}mv_0^2 = \tfrac{1}{2} \times 0.16 \times 24^2 = 46.08\,\text{J}$$

*Greatest height* (where $K = 0$): $mgh_\text{max} = E$, so

$$h_\text{max} = \frac{v_0^2}{2g} = \frac{576}{19.6} \approx 29.4\,\text{m}$$

That is about $30\,\text{m}$ above the ground — as tall as a ten-storey building.

*At $20\,\text{m}$ above the bat:* $\tfrac{1}{2}mv^2 = E - mgh$, and the mass cancels:

$$v = \sqrt{v_0^2 - 2gh} = \sqrt{576 - 392} = \sqrt{184} \approx 13.6\,\text{m/s}$$

*At the catch*, $0.5\,\text{m}$ above the bat:

$$v = \sqrt{576 - 2 \times 9.8 \times 0.5} = \sqrt{566.2} \approx 23.8\,\text{m/s}$$

Slightly **slower** than it left the bat, because Sneha catches it a little higher than it started.

**Sanity check:** kinematics agrees. The time to the top is $24/9.8 \approx 2.45\,\text{s}$, and the average speed on the way up is $12\,\text{m/s}$, so the climb is $12 \times 2.45 \approx 29.4\,\text{m}$. Also, $24\,\text{m/s} = 86\,\text{km/h}$, matching the story's estimate.

## Where the picture breaks

For a skier this high, air drag is not negligible. It does negative work on the way up *and* on the way down, so the real ball doesn't reach $29\,\text{m}$ and comes back noticeably slower than $24\,\text{m/s}$. Varun's worry is even more wrong than the ideal calculation suggests. Mechanical energy is conserved only when non-conservative forces do no work. The *total* energy, including the heat stirred into the air, is always conserved.

## Key takeaway

When only conservative forces such as gravity do work, $K + U$ is constant: $\tfrac{1}{2}mv^2 + mgh$ is the same at every point. Use it to find speeds and heights without knowing the path or the time. A ball returns to its starting height with the speed it started with — never faster.
