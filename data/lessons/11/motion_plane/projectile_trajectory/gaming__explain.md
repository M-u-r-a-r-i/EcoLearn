---
concept_id: projectile_trajectory
interest: gaming
format: explain
title: Aiming the cannon when the power is fixed
check:
  question: |-
    In an artillery game with no wind, every shell leaves the cannon at the same speed, and a shell fired at $25^\circ$ lands exactly on a target on level ground. At which other launch angle would a shell hit the same target?
  options:
    A: |-
      $50^\circ$
    B: |-
      $45^\circ$
    C: |-
      $65^\circ$
    D: |-
      No other angle; each angle has its own range
  answer: C
  explanation: |-
    The range is $R = \dfrac{u^2 \sin 2\theta}{g}$, and $\sin 2\theta$ is the same for $\theta$ and $90^\circ - \theta$. So $65^\circ$ gives $\sin 130^\circ = \sin 50^\circ$, the same range as $25^\circ$, after a higher, longer flight.
  misconceptions:
    A: |-
      Thinks doubling the angle keeps the range, confusing $\sin 2\theta$ with the angle itself. $50^\circ$ gives $\sin 100^\circ \approx 0.98$, a longer range than $\sin 50^\circ \approx 0.77$.
    B: |-
      Knows $45^\circ$ is special but misremembers why: it gives the maximum range, which here overshoots the target, not the same range.
    D: |-
      Assumes range always grows with angle, so each range has only one angle. Range rises up to $45^\circ$ and then falls again, so complementary angles share a range.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A gaming desk at night: the monitor shows an artillery game where a cannon fires a shell along a curved arc at 45 degrees and 20 m/s towards a flag](scenes/gaming/motion_plane.svg "In this artillery game the launch speed is fixed. The only thing the player chooses is the angle.")

Zoya and Yash are playing a turn-based artillery game with wind switched off. There's a twist in this mode: every shell leaves the cannon at the same speed, $20\,\text{m/s}$. You can only choose the angle.

The enemy tank sits $35\,\text{m}$ away on level ground. Zoya aims at $30^\circ$ and scores a direct hit.

Yash's turn, same distance. "Higher is further," he says, confidently cranking his barrel up to $75^\circ$. His shell climbs almost straight up, hangs in the sky, and lands nowhere near, far short of the target. Zoya's second shot, at $60^\circ$, soars much higher than her first, and hits the same spot.

Yash is baffled. "So a steep shot sometimes lands short, and sometimes lands in exactly the same place as a low shot?"

What decides how far a shell goes, and which angle sends it furthest?

## The physics

Launch a projectile from level ground at speed $u$ and angle $\theta$, ignoring air resistance. From the previous lesson, $x = (u\cos\theta)\,t$ and $y = (u\sin\theta)\,t - \tfrac{1}{2}gt^2$.

**Path.** Eliminate $t = x/(u\cos\theta)$:
$$y = x\tan\theta - \frac{g x^2}{2u^2\cos^2\theta}$$
This has the form $y = ax - bx^2$, a **parabola**.

**Time of flight.** It lands when $y = 0$ again: $t\,(u\sin\theta - \tfrac{1}{2}gt) = 0$. The non-zero root is
$$T = \frac{2u\sin\theta}{g}$$

**Maximum height.** At the top $v_y = 0$, so $0 = (u\sin\theta)^2 - 2gH$:
$$H = \frac{u^2\sin^2\theta}{2g}$$

**Horizontal range.** Horizontal velocity times the time of flight, using $2\sin\theta\cos\theta = \sin 2\theta$:
$$R = (u\cos\theta)\,T = \frac{u^2\sin 2\theta}{g}$$

Since $\sin 2\theta$ is largest (equal to $1$) when $2\theta = 90^\circ$, the **maximum range** is at $\theta = 45^\circ$: $R_{\max} = u^2/g$. And because $\sin 2\theta = \sin(180^\circ - 2\theta)$, the angles $\theta$ and $90^\circ - \theta$ give the **same range**. The steeper one flies higher and for longer.

![Five parabolas for a launch speed of 28 m/s at 15, 30, 45, 60 and 75 degrees. The 45-degree path goes furthest, to 80 m; the 30 and 60 degree paths both land at 69 m](figures/projectile_trajectory/trajectories-by-angle.svg "Same speed, different angles (drawn here for a faster 28 m/s launch). 45 degrees goes furthest, and angles adding up to 90 degrees land in the same place.")

That explains the whole game. Zoya's $30^\circ$ and $60^\circ$ are complementary, so they share a range. Yash's $75^\circ$ is too steep: it spends its speed going up.

## Worked example

**Given:** $u = 20\,\text{m/s}$, $g = 9.8\,\text{m/s}^2$, level ground, no air resistance.
**Find:** $T$, $H$ and $R$ for $\theta = 30^\circ$ and $60^\circ$, the maximum range, and Yash's range at $75^\circ$.

At $30^\circ$ ($\sin 30^\circ = 0.5$, $\sin 60^\circ = 0.866$):
$$T = \frac{2(20)(0.5)}{9.8} \approx 2.0\,\text{s}, \quad H = \frac{(20)^2(0.5)^2}{2(9.8)} \approx 5.1\,\text{m}, \quad R = \frac{(20)^2(0.866)}{9.8} \approx 35\,\text{m}$$

At $60^\circ$ ($\sin 120^\circ = 0.866$):
$$T = \frac{2(20)(0.866)}{9.8} \approx 3.5\,\text{s}, \quad H = \frac{(20)^2(0.866)^2}{2(9.8)} \approx 15\,\text{m}, \quad R \approx 35\,\text{m}$$

Maximum range, at $45^\circ$: $R_{\max} = 400/9.8 \approx 41\,\text{m}$. At $75^\circ$: $R = 400 \times \sin 150^\circ / 9.8 = 400 \times 0.5/9.8 \approx 20\,\text{m}$, far short.

**Sanity check:** both hits land at $35\,\text{m}$, but the $60^\circ$ shell climbs three times as high ($\sin^2 60^\circ / \sin^2 30^\circ = 3$) and flies $\sqrt{3} \approx 1.7$ times as long.

## Where the picture breaks

With wind switched on, or in the real world with air resistance, the path is no longer a perfect parabola: it comes down more steeply than it went up, and the best angle for range is usually a little below $45^\circ$. The formulas also assume the landing point is at the same height as the launch; firing from a hill or at a target on a ledge changes $T$ and $R$. And many games scale gravity to suit their world, so "$20\,\text{m/s}$" on a game's screen only follows these numbers if the game uses $g = 9.8\,\text{m/s}^2$.

## Key takeaway

For a launch from level ground with no air resistance, $T = \dfrac{2u\sin\theta}{g}$, $H = \dfrac{u^2\sin^2\theta}{2g}$ and $R = \dfrac{u^2\sin 2\theta}{g}$. The range is greatest at $45^\circ$, and complementary angles such as $30^\circ$ and $60^\circ$ give the same range, the steeper one flying higher and longer.
