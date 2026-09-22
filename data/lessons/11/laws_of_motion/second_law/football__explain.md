---
concept_id: second_law
interest: football
format: explain
title: How hard a penalty kick really pushes the ball
check:
  question: |-
    A $0.45\,\text{kg}$ football rolling across the grass slows steadily from $6.0\,\text{m/s}$ to $3.0\,\text{m/s}$ in $2.0\,\text{s}$. What is the net force on it?
  options:
    A: |-
      $0.68\,\text{N}$, opposite to the ball's motion
    B: |-
      $0.68\,\text{N}$, in the direction of the ball's motion
    C: |-
      $1.35\,\text{N}$, opposite to the ball's motion
    D: |-
      Zero, because nothing is kicking the ball any more
  answer: A
  explanation: |-
    $a = \dfrac{v - u}{t} = \dfrac{3.0 - 6.0}{2.0} = -1.5\,\text{m/s}^2$, so $F_\text{net} = ma = 0.45 \times (-1.5) \approx -0.68\,\text{N}$. The minus sign means the force points against the motion, which is why the ball slows.
  misconceptions:
    B: |-
      Thinks the force on a body must point the way it is moving. Force points along the acceleration; a slowing ball has a backward acceleration, so the net force is backward.
    C: |-
      Uses the change in momentum ($0.45 \times 3.0 = 1.35\,\text{kg m/s}$) as if it were the force. Force is the rate of change of momentum, so divide by the $2.0\,\text{s}$.
    D: |-
      Thinks a force is only present while something is being pushed. The ball's velocity is changing, so by the second law a net force must be acting: friction from the grass.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![Under floodlights, a striker follows through after a shot while the ball flies towards the goalkeeper](scenes/football/laws_of_motion.svg "The boot touches the ball for a few thousandths of a second. That is all the time it has to launch it.")

The school's penalty shoot-out is at 4–4, and Aisha places the ball on the spot, eleven metres from the goal line. One step, two, and a clean strike with her instep. The ball is past the keeper's dive before he has left the ground.

Her little brother Farhan has been filming in slow motion. Frame by frame, they watch her boot meet the ball. The ball squashes, springs back and leaves. The boot is in contact for only about eight thousandths of a second, and in that time the ball goes from standing still to about as fast as a car on the highway.

"So how hard did I kick it?" Aisha asks. "In actual numbers."

Farhan has a follow-up. At practice last week she struck a light plastic ball with the same swing, and it flew off far faster. Same kick, very different result. Why?

## The physics

Newton's second law links force to the change it produces in motion. In its general form:

$$\vec{F}_\text{net} = \frac{d\vec{p}}{dt}$$

The **net force** on a body equals the rate of change of its **momentum** $\vec{p} = m\vec{v}$. When the mass stays constant, as it does for a football, this becomes

$$\vec{F}_\text{net} = m\vec{a}$$

Three points:

- It is the **net** force, the vector sum of every force on the body, that counts. During the kick the boot's push is so large that the ball's weight hardly matters.
- The acceleration points the **same way** as the net force. A ball slowing down on grass has a backward acceleration, so the net force on it (friction) is backward, even though the ball moves forward.
- For a given force, a bigger mass means a smaller acceleration, $a = F_\text{net}/m$. That is Farhan's plastic ball: similar push, much smaller mass, much larger acceleration.

![Two graphs: at fixed mass, acceleration rises in a straight line with force; at fixed force, acceleration falls along a curve as mass increases](figures/second_law/force-mass-acceleration.svg "Left: for one ball, twice the net force gives twice the acceleration. Right: for one force, a heavier ball gets a smaller acceleration.")

The unit of force, the **newton**, comes from this law: $1\,\text{N} = 1\,\text{kg}\,\text{m/s}^2$.

Once the ball leaves the boot, the boot's force is gone. The only force left (ignoring air) is the ball's weight, which bends its path downwards. There is no "force of the kick" travelling with the ball.

![A ball in flight with its velocity arrow along the path and a single weight arrow straight down, labelled the only force, and a crossed-out force of the hit](figures/second_law/forces-on-ball-in-flight.svg "After contact, the ball's velocity points along its path, but the only force on it is its weight. Velocity is not a force.")

## Worked example

**Given:** ball $m = 0.43\,\text{kg}$, at rest on the penalty spot; it leaves the boot at $25\,\text{m/s}$; contact time $\Delta t = 8.0 \times 10^{-3}\,\text{s}$ (illustrative values).
**Find:** the average force of the boot on the ball.

Take the direction of the kick as positive: $u = 0$, $v = +25\,\text{m/s}$.

$$\Delta p = m(v - u) = 0.43 \times (25 - 0) \approx 10.8\,\text{kg m/s}$$

$$F_\text{avg} = \frac{\Delta p}{\Delta t} = \frac{10.75}{8.0 \times 10^{-3}} \approx 1.3 \times 10^{3}\,\text{N}$$

That is about $1300\,\text{N}$ towards the goal, roughly the weight of two adult players, acting for eight thousandths of a second.

**Sanity check:** the average acceleration is $25 / 0.008 \approx 3.1 \times 10^{3}\,\text{m/s}^2$; times $0.43\,\text{kg}$ gives $1.3 \times 10^{3}\,\text{N}$ again. The same average force on a $0.10\,\text{kg}$ plastic ball would give $0.43/0.10 = 4.3$ times the acceleration, which is Farhan's puzzle in one line.

## Where the picture breaks

The boot's force is not constant: it rises from zero, peaks and falls back within those milliseconds, so $\Delta p/\Delta t$ gives only the *average*; the peak is higher. The ball squashes and may spin, and the foot slows down during contact, details a single "push" ignores. The plastic-ball comparison assumes the same force; a real boot meets a light ball differently (the contact time and the force both change), so the real speeds won't differ by exactly that factor. And $\vec{F} = m\vec{a}$ holds only for constant mass; for a body whose mass changes, such as a rocket, you need $\vec{F} = d\vec{p}/dt$.

## Key takeaway

The net force on a body equals its rate of change of momentum, $\vec{F}_\text{net} = d\vec{p}/dt$, which for constant mass is $\vec{F}_\text{net} = m\vec{a}$. Force and acceleration always point the same way, and the same force gives a lighter ball a larger acceleration.
