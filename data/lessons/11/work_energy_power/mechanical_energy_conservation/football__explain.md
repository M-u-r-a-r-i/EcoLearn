---
concept_id: mechanical_energy_conservation
interest: football
format: explain
title: How high the chip goes and how fast it drops in
check:
  question: |-
    A goalkeeper's clearance leaves the ground at $18\,\text{m/s}$ and climbs past a height of $9.0\,\text{m}$. Ignoring air resistance and taking $g = 9.8\,\text{m/s}^2$, what is the ball's speed at that height?
  options:
    A: |-
      $22.4\,\text{m/s}$
    B: |-
      $12.1\,\text{m/s}$
    C: |-
      It can't be found without knowing the angle of the kick.
    D: |-
      $15.4\,\text{m/s}$
  answer: B
  explanation: |-
    Only gravity does work, so $\tfrac{1}{2}mv^2 + mgh$ is constant. The mass cancels: $v = \sqrt{u^2 - 2gh} = \sqrt{324 - 176.4} = \sqrt{147.6} \approx 12.1\,\text{m/s}$.
  misconceptions:
    A: |-
      Adds the potential-energy term instead of subtracting it; climbing turns kinetic energy into potential energy, so the ball must be slower higher up.
    C: |-
      Thinks the speed at a given height depends on the direction of launch; energy is a scalar, so every ball launched at $18\,\text{m/s}$ has the same speed at $9.0\,\text{m}$, whatever its angle, as long as it gets there.
    D: |-
      Drops the factor of 2, using $v^2 = u^2 - gh$; equating $\tfrac{1}{2}mv^2$ changes with $mgh$ gives $v^2 = u^2 - 2gh$.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A football training ground by day: a player drags a weighted sled on a strap, a striker lofts the ball in a high arc, and the goalkeeper dives to catch it](scenes/football/work_energy_power.svg "A lofted ball trades speed for height on the way up, and gets it back on the way down.")

Zoya sees the keeper, Harsh, standing far off his line and doesn't think twice. From nearly $40\,\text{m}$ out, she scoops her foot under the ball and chips it. It rises in a high, slow arc, and Harsh starts backpedalling.

On the touchline, two substitutes argue as it climbs.

"At the top, it stops for a moment," says Manav. "Then it drops."

"No way it stops," says Rhea. "And it's going to come down into that net faster than she kicked it, gravity's been pulling on it the whole time."

Harsh stretches, but the ball drops just under the crossbar.

Afterwards Zoya wants to know. The chip left her boot at about $72\,\text{km/h}$, angled well upwards. How high did it go? Did it stop at the top? And how fast was it moving as it passed crossbar height on the way down?

## The physics

Kinetic energy and potential energy together make up **mechanical energy**:

$$E = K + U$$

**The principle of conservation of mechanical energy:** if only conservative forces do work on a body, its total mechanical energy stays constant:

$$K_i + U_i = K_f + U_f$$

**Why.** The work-energy theorem says the work done by all forces equals $\Delta K$. If only conservative forces act, that work also equals $-\Delta U$. So $\Delta K = -\Delta U$, and $K + U$ doesn't change. Kinetic energy lost reappears as potential energy, and vice versa.

For Zoya's chip, ignoring air, gravity is the only force doing work. As the ball climbs, $K$ turns into $U = mgh$. But the ball was kicked at an angle, so it keeps its horizontal velocity all the way; gravity changes only the vertical part. At the top it is still moving sideways, so $K$ is **not** zero there. Manav is wrong: only a ball kicked straight up stops at its highest point. Coming down, $U$ turns back into $K$, and at its starting height the ball has exactly its starting speed. Rhea is wrong too: it never lands faster than it was kicked, from the same height.

If **non-conservative** forces such as air drag do work $W_\text{nc}$, then $E_f = E_i + W_\text{nc}$. Drag's work is negative, so mechanical energy drains away.

![Energy against height for a 0.43 kilogram ball launched at 20 metres per second, 45 degrees above the horizontal: kinetic energy falls from 86 joules to 43 joules at the top, potential energy rises from 0 to 43 joules, and the total stays at 86 joules](figures/mechanical_energy_conservation/ke-pe-vs-height-angled.svg "The dashed total never changes. K stops falling at 43 J, not zero, because the ball is still moving sideways at the top.")

## Worked example

**Given** (illustrative): ball mass $m = 0.43\,\text{kg}$, kicked from the ground at $v_0 = 20\,\text{m/s}$ ($72\,\text{km/h}$), $45^\circ$ above the horizontal; crossbar height $2.44\,\text{m}$; $g = 9.8\,\text{m/s}^2$; no air resistance.
**Find:** the greatest height, and the speed as the ball drops past crossbar height.

Take $U = 0$ at the ground. Total energy:

$$E = \tfrac{1}{2}mv_0^2 = \tfrac{1}{2} \times 0.43 \times 20^2 = 86\,\text{J}$$

*At the top,* the ball moves horizontally at $v_x = 20\cos 45^\circ \approx 14.1\,\text{m/s}$, so $K_\text{top} = \tfrac{1}{2} \times 0.43 \times 200 = 43\,\text{J}$ and

$$mgh_\text{max} = 86 - 43 = 43\,\text{J} \quad\Rightarrow\quad h_\text{max} = \frac{43}{0.43 \times 9.8} \approx 10.2\,\text{m}$$

*At crossbar height:* $\tfrac{1}{2}mv^2 = E - mgh$, and the mass cancels:

$$v = \sqrt{v_0^2 - 2gh} = \sqrt{400 - 2 \times 9.8 \times 2.44} = \sqrt{352.2} \approx 18.8\,\text{m/s}$$

That speed is the same on the way up and on the way down. The ball reaches the ground again at $20\,\text{m/s}$, never faster.

**Sanity check:** kinematics agrees. The vertical launch speed is $20\sin 45^\circ \approx 14.1\,\text{m/s}$, and $h_\text{max} = v_y^2/2g = 200/19.6 \approx 10.2\,\text{m}$.

## Where the picture breaks

A real chip is struck with backspin, and a ball this light is noticeably slowed by air drag. Drag does negative work on the way up and on the way down, so the real ball doesn't reach $10.2\,\text{m}$ and arrives slower than $18.8\,\text{m/s}$, which makes Rhea's claim even more wrong. Spin can also make the ball dip or float, which the simple energy picture ignores. Mechanical energy is conserved only when non-conservative forces do no work; the *total* energy, including heat stirred into the air, is always conserved.

## Key takeaway

When only conservative forces such as gravity do work, $K + U$ is constant: $\tfrac{1}{2}mv^2 + mgh$ is the same at every point. Use it to find speeds and heights without knowing the path or the time. A ball has the same speed at a given height on the way up and on the way down, and comes back to its starting height no faster than it left.
