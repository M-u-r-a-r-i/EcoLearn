---
concept_id: second_law
interest: cricket
format: explain
title: What a cover drive does to the ball in one millisecond
check:
  question: |-
    In the nets, a cricket ball ($0.16\,\text{kg}$) and a tennis ball ($0.06\,\text{kg}$) are each given the same net force for the same short time. Which statement is correct?
  options:
    A: |-
      Both balls get the same acceleration, because the force is the same.
    B: |-
      The cricket ball gets the larger acceleration, because a heavier ball takes more of the force.
    C: |-
      The tennis ball gets the larger acceleration — about $2.7$ times that of the cricket ball.
    D: |-
      Both balls end with the same speed, because they received the same push.
  answer: C
  explanation: |-
    With the same net force, $a = F/m$, so the lighter ball accelerates more: $0.16/0.06 \approx 2.7$ times as much.
  misconceptions:
    A: |-
      Thinks acceleration depends only on the force applied, ignoring the mass being pushed.
    B: |-
      Thinks a heavier object "absorbs" or holds more force and so moves more — mass resists acceleration, it doesn't collect force.
    D: |-
      Thinks an equal push gives an equal change in speed, forgetting that the change in velocity depends on mass.
author: claude-code/opus-5
written: 2026-09-21
---
## The story

![A batter drives the ball back past the bowler in a floodlit stadium](scenes/cricket/laws_of_motion.svg "One swing, one millisecond — and the ball's journey is reversed.")

Under the floodlights, Aarav faces the last ball of the over. The bowler charges in and sends it down at about $30\,\text{m/s}$ — faster than a car on the highway. Aarav leans forward, the bat comes down, and there's a sharp *crack*. Before anyone can blink, the ball is racing back past the bowler at around $40\,\text{m/s}$.

In the stands, his younger sister Anya frowns. "The ball was coming *at* him," she says. "How did it turn around and go even faster?" Her father explains that the bat touched the ball for only about a thousandth of a second. That makes it stranger, not simpler. What kind of push can reverse a speeding ball in a thousandth of a second? And why would the very same swing send a tennis ball flying away much faster than a cricket ball?

Newton's second law answers both questions.

## The physics

Newton's second law connects force to the change it produces in motion. In its general form:

$$\vec{F}_\text{net} = \frac{d\vec{p}}{dt}$$

The **net force** on a body equals the rate of change of its **momentum** $\vec{p} = m\vec{v}$. For a body whose mass stays constant — like a cricket ball — this becomes the familiar

$$\vec{F}_\text{net} = m\vec{a}$$

Three things to notice:

- It is the **net** force — the vector sum of all forces — that counts. During the drive the bat's push is so large that gravity and air drag hardly matter.
- Force and acceleration point the **same way**. The bat pushes the ball back towards the bowler, so the ball accelerates towards the bowler, even though it was arriving the other way.
- For a given force, a larger mass means a smaller acceleration: $a = F_\text{net}/m$. Mass measures how strongly a body resists changes to its motion.

![Two graphs: at fixed mass, acceleration rises in a straight line with force; at fixed force, acceleration falls along a curve as mass increases](figures/second_law/force-mass-acceleration.svg "Left: same mass, so acceleration is proportional to force. Right: same force, so doubling the mass halves the acceleration.")

The SI unit of force, the **newton**, is defined by this law: $1\,\text{N} = 1\,\text{kg}\,\text{m/s}^2$ — named after Isaac Newton, who set the law down in 1687 in his book *Principia*. He wrote that the change of motion is proportional to the force impressed, and takes place in the direction of that force. By "motion" he meant what we now call momentum.

![The Latin title page of Newton's Principia Mathematica, printed in London in 1687](famous/newton-principia-title-page.jpg "Newton stated his three laws of motion in the Principia (1687). Public domain, via Wikimedia Commons.")

## Worked example

**Given:** ball mass $m = 0.16\,\text{kg}$; arriving at $30\,\text{m/s}$ towards the batter; leaving at $40\,\text{m/s}$ towards the bowler; contact time $\Delta t = 1.0 \times 10^{-3}\,\text{s}$.
**Find:** the average force of the bat on the ball.

Take the direction towards the bowler as positive. Then $u = -30\,\text{m/s}$ and $v = +40\,\text{m/s}$.

$$\Delta p = m(v - u) = 0.16 \times (40 - (-30)) = 0.16 \times 70 = 11.2\,\text{kg m/s}$$

$$F_\text{avg} = \frac{\Delta p}{\Delta t} = \frac{11.2}{1.0 \times 10^{-3}} \approx 1.1 \times 10^{4}\,\text{N}$$

That is about $11\,000\,\text{N}$, towards the bowler — roughly the weight of a one-tonne car, acting for a thousandth of a second.

**Sanity check:** the ball's velocity changes by $70\,\text{m/s}$ in $0.001\,\text{s}$, an average acceleration of $7 \times 10^{4}\,\text{m/s}^2$; multiplying by $0.16\,\text{kg}$ gives the same $1.1 \times 10^{4}\,\text{N}$.

## Where the picture breaks

The force during the drive is not constant: it rises from zero, peaks and falls back to zero within that millisecond. The second law gives the *average* force over the contact, not the peak, which is higher. The ball also squashes and spins during contact, and the bat flexes — real details our "one push" picture ignores. And $F = ma$ holds only for constant mass; for something that loses mass as it moves, such as a rocket, you must use the momentum form.

## Key takeaway

Force changes motion: the net force on a body equals its rate of change of momentum, $\vec{F}_\text{net} = d\vec{p}/dt$, which for constant mass is $\vec{F}_\text{net} = m\vec{a}$. The same force gives a lighter object a larger acceleration — which is why the same swing sends a tennis ball away much faster than a cricket ball.
