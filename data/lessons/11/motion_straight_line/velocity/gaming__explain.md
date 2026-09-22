---
concept_id: velocity
interest: gaming
format: explain
title: The guard who sprinted at zero velocity
check:
  question: |-
    In a stealth game, take the positive direction as pointing away from the drone's base. A scouting drone flies $30\,\text{m}$ straight back towards its base in $6.0\,\text{s}$. What is its average velocity during this flight?
  options:
    A: |-
      $+5.0\,\text{m/s}$
    B: |-
      $-0.20\,\text{m/s}$
    C: |-
      $0\,\text{m/s}$
    D: |-
      $-5.0\,\text{m/s}$
  answer: D
  explanation: |-
    Average velocity is displacement over time. Flying towards the base is the negative direction, so $\Delta x = -30\,\text{m}$ and $\bar{v} = -30/6.0 = -5.0\,\text{m/s}$.
  misconceptions:
    A: |-
      Gives the drone's speed, $5.0\,\text{m/s}$, and forgets that velocity carries a direction. Flying towards the base is the negative direction here.
    B: |-
      Divides the time by the displacement ($6.0/30$) instead of the displacement by the time — an inverted ratio, with units of s/m rather than m/s.
    C: |-
      Assumes a drone returning to base must have zero velocity, as for a full out-and-back trip. This flight is one leg only, and the drone's position clearly changes.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A gaming desk at night: a monitor shows a side-scrolling game whose runner moves along a straight track marked like a number line, with a position and velocity readout; a tablet replays a velocity-time graph](scenes/gaming/motion_straight_line.svg "Games track every character's position frame by frame — and can report more than one kind of 'how fast'.")

Meera is building a mod for a stealth game, and tonight she's studying one guard. His route is simple: he stands at the vault door, then walks slowly away down a long straight corridor to check a window. When Meera's character trips the alarm, he turns and sprints straight back to the door.

Her mod prints two numbers for that one patrol cycle:

*Average speed: 1.9 m/s.*
*Average velocity: 0.0 m/s.*

Her cousin Dev, watching over her shoulder, snorts. "Zero? He came back like a rocket. Your mod's broken."

"It also says his speed was one point nine," Meera says. "It obviously doesn't think he stood still."

"Then speed and velocity are the same thing, and your mod is contradicting itself."

Meera took the formulas from a physics textbook, so she trusts them. But she can't yet say why one of them comes out as zero.

What does velocity measure that speed doesn't?

## The physics

**Average velocity** is the displacement divided by the time taken:

$$\bar{v} = \frac{\Delta x}{\Delta t} = \frac{x_f - x_i}{t_f - t_i}$$

It is the **rate of change of position** (of displacement). Like displacement, velocity is a **vector**: in one dimension its sign gives its direction. Its SI unit is $\text{m/s}$.

**Average speed** is the total distance divided by the time taken. It is a scalar and never negative.

The two differ whenever the path doubles back, because distance keeps adding while displacement can cancel. Put the origin at the vault door, with the corridor running off in the negative direction. Take the window to be $18\,\text{m}$ down the corridor (illustrative numbers).

![A position–time graph: position falls from 0 to −18 m over 15 s, then rises back to 0 at 19 s](figures/velocity/out-slow-back-fast-xt.svg "The slope of a position–time line is the velocity: gentle and negative on the slow walk away, steep and positive on the sprint back.")

- Walking away: $\Delta x = -18\,\text{m}$ in $15\,\text{s}$, so $\bar{v} = -1.2\,\text{m/s}$. His speed is $1.2\,\text{m/s}$.
- Sprinting back: $\Delta x = +18\,\text{m}$ in $4.0\,\text{s}$, so $\bar{v} = +4.5\,\text{m/s}$. His speed is $4.5\,\text{m/s}$.
- Whole cycle: he ends exactly where he started, so $\Delta x = 0$ and $\bar{v} = 0$.

The mod is right on both lines. Over the whole cycle the guard went $36\,\text{m}$ but got nowhere: a real speed, zero velocity.

On a position–time graph, velocity is the **slope**: a rising line means positive velocity, a falling line negative velocity, and a steeper line a greater speed.

## Worked example

**Given:** walk away $18\,\text{m}$ in $15\,\text{s}$; sprint back $18\,\text{m}$ in $4.0\,\text{s}$.
**Find:** the guard's average speed and average velocity over the whole cycle.

Total distance $= 18 + 18 = 36\,\text{m}$; total time $= 15 + 4.0 = 19\,\text{s}$.

$$\text{average speed} = \frac{36\,\text{m}}{19\,\text{s}} \approx 1.9\,\text{m/s}$$

Displacement $= x_f - x_i = 0 - 0 = 0$:

$$\bar{v} = \frac{0\,\text{m}}{19\,\text{s}} = 0\,\text{m/s}$$

Exactly the mod's two numbers.

**Sanity check:** the average speed ($1.9\,\text{m/s}$) lies between the two leg speeds ($1.2$ and $4.5\,\text{m/s}$), nearer the slow one because he spent far longer walking. And the size of the average velocity ($0$) is no bigger than the average speed — which must always be true.

## Where the picture breaks

In the game, the guard's animation speeds up and slows down — he doesn't switch instantly from $-1.2$ to $+4.5\,\text{m/s}$ — so these are average velocities over each leg, not his velocity at a particular moment. That needs **instantaneous velocity**, coming next. The sharp corner in the graph at $15\,\text{s}$ is an idealisation for the same reason. Game AI often does move characters at exactly constant speeds along straight paths, which makes games a surprisingly good match for these graphs; real people never quite manage it.

## Key takeaway

Velocity is the rate of change of position: average velocity $\bar{v} = \Delta x / \Delta t$, a vector whose sign shows direction. Speed uses distance and ignores direction. When the path turns back they differ — the guard's full patrol cycle has a real average speed but zero average velocity.
