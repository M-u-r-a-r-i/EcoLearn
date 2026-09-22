---
concept_id: dimensional_consistency
interest: gaming
format: explain
title: The enemy who ran faster on a faster monitor
check:
  question: |-
    In a game's update code, $x$ is a position, $v$ a velocity, $a$ an acceleration, $\Delta t$ the time step and $f$ the update rate in hertz. Which line is dimensionally inconsistent?
  options:
    A: |-
      $x_\text{new} = x + v$
    B: |-
      $v_\text{new} = v + a\,\Delta t$
    C: |-
      $x_\text{new} = x + v\,\Delta t + \tfrac{1}{2}a\,(\Delta t)^2$
    D: |-
      $\Delta t = 1/f$
  answer: A
  explanation: |-
    $x$ is $[\text{L}]$ but $v$ is $[\text{L}\,\text{T}^{-1}]$. A length can't be added to a velocity, so line A must be wrong; it is missing a factor of $\Delta t$.
  misconceptions:
    B: |-
      Judges by the look of the symbols ("you can't add an acceleration to a velocity"). But the term is $a\,\Delta t$: $[\text{L}\,\text{T}^{-2}][\text{T}] = [\text{L}\,\text{T}^{-1}]$, a velocity.
    C: |-
      Thinks the squared time step or the $\tfrac{1}{2}$ spoils the balance. $\tfrac{1}{2}a(\Delta t)^2$ is $[\text{L}\,\text{T}^{-2}][\text{T}^2] = [\text{L}]$, the same as $x$ and $v\,\Delta t$.
    D: |-
      Thinks a frequency can't give a time. Hertz means "per second", $[\text{T}^{-1}]$, so $1/f$ has dimensions $[\text{T}]$, exactly a time.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A gaming desk: a monitor showing a racing game with a 144 FPS counter in the corner](scenes/gaming/units_measurement.svg "Look at the frame counter. Should a game run differently at 60 frames per second than at 144?")

Ishita's first multiplayer game has one enemy: a robot that chases you at a steady speed. She tests it on her laptop, which runs the game at $60$ frames per second, and it feels fair.

Then her cousin Rahul tries it on his gaming monitor at $144$ frames per second. "Your robot is a rocket," he messages. "I can't escape it."

Ishita records both screens. Rahul's robot really is faster — about $2.4$ times faster. She opens her code and finds the line that moves it, run once every frame:

`x = x + v`

Here `v` is the robot's speed, which she tuned by eye on her laptop until it looked right: $0.08$. It looks innocent. It *reads* like "new position equals old position plus speed". But something about it makes the game depend on the monitor. Without running a single test, can the line itself tell her what's wrong?

## The physics

You can only add, subtract or equate quantities of the **same kind**. A length can be added to a length, never to a speed. This is the **principle of homogeneity of dimensions**:

> In a correct equation, every term that is added, subtracted or set equal must have the same dimensions.

An equation that obeys it is **dimensionally consistent**. One that breaks it is certainly wrong.

To test an equation, work out the dimensions of each term **separately**, then compare. For Ishita's line:

$$[x] = [\text{L}], \qquad [v] = [\text{L}\,\text{T}^{-1}]$$

The two terms don't match, so `x = x + v` is inconsistent. A speed must be multiplied by a time to become a distance. The fix is to multiply by the time step $\Delta t$, the time between updates:

$$x_\text{new} = x + v\,\Delta t, \qquad [v\,\Delta t] = [\text{L}\,\text{T}^{-1}][\text{T}] = [\text{L}] \checkmark$$

The broken line moved the robot $0.08$ metres *every frame*: $0.08 \times 60 = 4.8\,\text{m}$ each second on the laptop, but $0.08 \times 144 = 11.5\,\text{m}$ each second on Rahul's monitor. The ratio is $144/60 = 2.4$, exactly Rahul's rocket.

With the fix, Ishita sets a real speed, $v = 4.8\,\text{m/s}$, and the frame rate cancels out. At $60$ updates per second, $\Delta t = 1/60\,\text{s}$ and the robot moves $4.8/60 = 0.08\,\text{m}$ per update: $4.8\,\text{m}$ each second. At $144$ updates per second it moves $4.8/144 \approx 0.033\,\text{m}$ per update: still $4.8\,\text{m}$ each second.

![Two equations checked term by term. In v squared equals u squared plus 2as, every term is L squared T to the minus 2. In s equals ut plus half at, the last term is L T to the minus 1, so the equation is inconsistent](figures/dimensional_consistency/homogeneity-check.svg "Check every term, not just the two sides. One mismatched term is enough to prove an equation wrong.")

The same principle means that the argument of a function like $\sin\theta$ or an exponential must be dimensionless: you can't take the sine of a length.

## Worked example

**Check** whether each update line is dimensionally consistent: (a) $v_\text{new} = v + a\,\Delta t$; (b) $x_\text{new} = x + v\,\Delta t + a\,\Delta t$.

(a) $[v] = [\text{L}\,\text{T}^{-1}]$ and $[a\,\Delta t] = [\text{L}\,\text{T}^{-2}][\text{T}] = [\text{L}\,\text{T}^{-1}]$. Every term matches: **consistent**.

(b) $[x] = [v\,\Delta t] = [\text{L}]$, but $[a\,\Delta t] = [\text{L}\,\text{T}^{-1}]$, a velocity. One term doesn't match: **inconsistent**. The acceleration term needs $(\Delta t)^2$ to become a length.

**Sanity check:** try (b) in SI units: $\text{m} + (\text{m/s})(\text{s}) + (\text{m/s}^2)(\text{s}) = \text{m} + \text{m} + \text{m/s}$. The last term can't be added to the others.

## Where the picture breaks

Two honest limits. First, a consistent equation isn't necessarily right: dimensions ignore pure numbers, so the check can't tell whether a factor like $\tfrac{1}{2}$ belongs in a formula. A mismatch proves an equation wrong; a match only says it *might* be right. Second, some game code stores velocity as "distance per frame". Then `x = x + v` is consistent — the frame is built into $v$ — but the motion still depends on the frame rate, which is exactly the bug. Writing speeds per second and multiplying by $\Delta t$ is what makes the code both consistent and fair. And stepping a position forward in small jumps is itself an approximation of smooth motion; you'll see why when you study motion.

## Key takeaway

Principle of homogeneity: every term that is added, subtracted or equated must have the same dimensions. Check each term separately; one mismatch proves the equation wrong, as in `x = x + v`. Passing the check is necessary, but not enough to prove an equation right.
