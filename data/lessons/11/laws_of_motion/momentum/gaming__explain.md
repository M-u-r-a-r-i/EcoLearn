---
concept_id: momentum
interest: gaming
format: explain
title: The drone, the tank robot and the stat that made no sense
check:
  question: |-
    In a robot-arena game with realistic physics, a $3.0\,\text{kg}$ drone flies east at $20\,\text{m/s}$, hits a wall and flies back west at $20\,\text{m/s}$. What is the size of the change in its momentum?
  options:
    A: |-
      $0\,\text{kg m/s}$
    B: |-
      $60\,\text{kg m/s}$
    C: |-
      $120\,\text{kg m/s}$
    D: |-
      $40\,\text{kg m/s}$
  answer: C
  explanation: |-
    Taking east as positive, $p_i = 3.0 \times 20 = +60\,\text{kg m/s}$ and $p_f = 3.0 \times (-20) = -60\,\text{kg m/s}$, so $\Delta p = -60 - 60 = -120\,\text{kg m/s}$: a change of $120\,\text{kg m/s}$ towards the west.
  misconceptions:
    A: |-
      Treats momentum as a scalar: the speed is unchanged, so it assumes the momentum is unchanged. Momentum is a vector, and reversing its direction is a large change.
    B: |-
      Finds the size of the momentum before (or after) but not the change. Going from $+60$ to $-60$ is a change of $120$, not $60$.
    D: |-
      Adds the velocities to get $40\,\text{m/s}$ and forgets to multiply by the mass. Momentum is mass times velocity, so its unit is kg m/s, not m/s.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A gaming desk at night: a racing game on the monitor and a zero-gravity game on a tablet](scenes/gaming/laws_of_motion.svg "In every game with real physics, the engine keeps track of how much motion each object carries, and in which direction.")

Siddharth has found a robot-arena game with a physics engine his cousin Tanvi says is "scarily realistic". In the practice arena, two machines come at his force-field gate at once: a tiny scout drone zipping in fast, and a huge tank robot crawling along at walking pace.

"Stop the drone first," Tanvi says. "It's way faster. It'll hit way harder."

Siddharth isn't sure. The tank is slow, but it looks like a small building.

Later he watches a replay. The scout drone bounces off an arena wall and flies straight back out at exactly the speed it came in. The stats panel beside it reads *momentum change: 160 kg m/s*.

"That's a bug," says Tanvi. "Same speed before and after. Nothing changed."

Two puzzles, then. Which machine is really harder to stop? And how can a bounce at the same speed change anything at all?

## The physics

How hard something is to stop depends on **both** its mass and its velocity. The quantity that combines them is **linear momentum**:

$$\vec{p} = m\vec{v}$$

- $m$ is the mass in kg, $\vec{v}$ the velocity in m/s.
- The SI unit of momentum is $\text{kg m/s}$.
- A fast, light body and a slow, heavy body can have the same momentum. That answers the first puzzle: the game should compare $m v$, not speed alone.

**Momentum is a vector.** Because velocity is a vector and mass is a positive scalar, $\vec{p}$ points in the same direction as $\vec{v}$. In one dimension, choose a positive direction and give each momentum a sign.

That answers the second puzzle. When the drone bounces back, its speed is unchanged but its direction reverses, so its momentum goes from $+p$ to $-p$. The change is

$$\Delta\vec{p} = \vec{p}_f - \vec{p}_i = (-p) - (+p) = -2p$$

The size of the change is **twice** the momentum, not zero. The stats panel was right. You'll soon see that it takes a force to produce any change in momentum, which is why the wall had to push the drone hard.

![A ball arriving leftwards at 25 m/s has momentum −4.0 kg m/s; driven back at 25 m/s it has +4.0 kg m/s; the change is +8.0 kg m/s](figures/momentum/momentum-is-a-vector.svg "Drawn for a light ball, but it is exactly the drone at the wall: same speed, opposite arrows, so the change in momentum is twice the momentum, not zero.")

## Worked example

**Given (illustrative values):** the scout drone has $m = 2.0\,\text{kg}$ and $v = 40\,\text{m/s}$. The tank robot has $m = 250\,\text{kg}$ and moves at $1.8\,\text{km/h}$. Later, the drone hits a wall at $40\,\text{m/s}$ and rebounds at $40\,\text{m/s}$.
**Find:** (a) the momentum of each machine; (b) the change in the drone's momentum at the wall.

(a) Convert the tank's speed first: $1.8\,\text{km/h} = \dfrac{1.8 \times 1000\,\text{m}}{3600\,\text{s}} = 0.50\,\text{m/s}$.

$$p_\text{drone} = 2.0 \times 40 = 80\,\text{kg m/s} \qquad p_\text{tank} = 250 \times 0.50 = 125\,\text{kg m/s}$$

The slow tank carries more momentum than the fast drone. Tanvi's "faster means harder to stop" misses the mass.

(b) Take the direction *away from* the wall as positive. Arriving, $p_i = 2.0 \times (-40) = -80\,\text{kg m/s}$. Leaving, $p_f = 2.0 \times (+40) = +80\,\text{kg m/s}$.

$$\Delta p = p_f - p_i = 80 - (-80) = +160\,\text{kg m/s}$$

That matches the stats panel: $160\,\text{kg m/s}$, directed away from the wall.

**Sanity check:** the tank has $125 \times$ the drone's mass but $\dfrac{1}{80}$ of its speed, and $125/80 \approx 1.6$, so its momentum should be about $1.6$ times the drone's: $1.6 \times 80 = 125$ ✓. For the bounce, a drone that simply stopped at the wall would change by only $80\,\text{kg m/s}$; bouncing back doubles it, as it should.

## Where the picture breaks

"Harder to stop" is about momentum only if you stop things in the same way over the same time; how much damage a hit does also depends on energy and on how quickly it happens, which you'll meet later. Real bounces are rarely perfect: most objects come back a little slower than they arrived, so the change is a bit less than $2p$. And a game might not use real physics for every object; some give robots scripted motion that ignores momentum entirely. Here we treated each machine as a single point moving in a straight line.

## Key takeaway

Linear momentum is mass times velocity, $\vec{p} = m\vec{v}$, measured in kg m/s. It depends on both mass and speed, so a slow heavy body can carry more than a fast light one. Momentum is a vector: reversing direction at the same speed changes it by twice its size.
