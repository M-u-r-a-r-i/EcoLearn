---
concept_id: second_law
interest: cricket
format: challenge
title: How much harder does a fast bowler push than a spinner
check:
  question: |-
    A bowler's arm push takes the ball from rest to $30\,\text{m/s}$ in $0.10\,\text{s}$. To take it from rest to $45\,\text{m/s}$ with a push of the same duration, the average net force on the ball must be:
  options:
    A: |-
      $1.5$ times as large
    B: |-
      The same — the extra speed comes from swinging for longer, not from more force
    C: |-
      $2.25$ times as large
    D: |-
      It depends on the bowler's own body mass, so it cannot be worked out
  answer: A
  explanation: |-
    From rest, $F = m\,\Delta v/\Delta t$. With the same ball mass and the same push time, force is proportional to the speed gained: $45/30 = 1.5$.
  misconceptions:
    B: |-
      Believes speed comes from how long a force acts rather than how large it is — but the push time is fixed here, so a bigger change in velocity needs a bigger force.
    C: |-
      Squares the speed ratio, mixing up force with kinetic energy ($\tfrac{1}{2}mv^2$). Force is linked to the change in velocity, not its square.
    D: |-
      Uses the wrong mass: the second law for the ball involves the ball's mass, not the bowler's.
author: claude-code/opus-5
written: 2026-09-21
---
## The story

![A batter and a bowler in a floodlit stadium](scenes/cricket/laws_of_motion.svg "Two bowlers, one ball, one argument.")

It's the last net session before the school tournament. Meera bowls fast — her deliveries thud into the keeper's gloves. Kabir bowls spin, loopy and slow. After practice, the coach's speed gun settles a long-running argument: Meera releases the ball at about $40\,\text{m/s}$, Kabir at about $22\,\text{m/s}$.

"So you're nearly twice as fast," Kabir says. "Which means your arm must push the ball *four* times harder than mine. Speed always costs more than you think."

Meera isn't sure. They both use the same ball, and their final arm-whip takes about the same time. Is Kabir right? Before you read the physics, try to settle it yourself.

## The challenge

Two bowlers use the same cricket ball ($0.16\,\text{kg}$). Both start the ball from rest in the hand, and in both actions the final whip of the arm pushes the ball for about the same time, say $0.10\,\text{s}$.

- The fast bowler releases it at $40\,\text{m/s}$ (about $144\,\text{km/h}$).
- The spinner releases it at $22\,\text{m/s}$ (about $79\,\text{km/h}$).

On average, how many times harder does the fast bowler push the ball than the spinner?

## Think first

Make a guess before reading on. Roughly twice as hard, since the speed is roughly doubled? Or more like three or four times, because "fast is so much faster"? Or does it depend on how strong the bowlers are? Write down a number.

## The reveal

The ball starts from rest and speeds up during the push, so use Newton's second law in the form "force equals rate of change of momentum":

$$F_\text{avg} = \frac{\Delta p}{\Delta t} = \frac{m\,\Delta v}{\Delta t}$$

The mass $m$ is the same ball, and the push time $\Delta t$ is the same. So the only thing that differs is the speed gained, $\Delta v$, and the force is simply proportional to it:

$$\frac{F_\text{fast}}{F_\text{spin}} = \frac{\Delta v_\text{fast}}{\Delta v_\text{spin}} = \frac{40}{22} \approx 1.8$$

The fast bowler pushes only about $1.8$ times as hard — not four times. In numbers:

$$F_\text{fast} = \frac{0.16 \times 40}{0.10} = 64\,\text{N}, \qquad F_\text{spin} = \frac{0.16 \times 22}{0.10} \approx 35\,\text{N}$$

If you guessed "about three and a third" ($40^2/22^2 \approx 3.3$), you were thinking of kinetic energy, which depends on $v^2$. That ratio *would* matter if both pushes acted over the same *distance* rather than the same *time* — a link you'll meet in the chapter on work and energy. With the time fixed, force follows the change in velocity, not its square.

And the bowlers' own strength or body mass doesn't enter the calculation: the second law for the ball involves only the ball's mass and the net force on the ball.

## The physics

Newton's second law states that the net force on a body equals the rate of change of its momentum:

$$\vec{F}_\text{net} = \frac{d\vec{p}}{dt}$$

For constant mass this is $\vec{F}_\text{net} = m\vec{a}$, and over a finite interval the average force is $F_\text{avg} = m\,\Delta v / \Delta t$. The force and the change in velocity point in the same direction, and for a fixed mass and time the force needed is directly proportional to the change in velocity.

![Two graphs: at fixed mass, acceleration rises in a straight line with force; at fixed force, acceleration falls along a curve as mass increases](figures/second_law/force-mass-acceleration.svg "The left graph is the bowlers' case: same ball, so acceleration — and the speed gained in a fixed time — is proportional to force.")

## Key takeaway

For the same mass and the same push time, the force needed is proportional to the change in velocity: $F_\text{avg} = m\,\Delta v/\Delta t$. Doubling the speed gained doubles the force — it does not quadruple it.
