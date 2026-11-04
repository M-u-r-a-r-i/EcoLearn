---
concept_id: impulse
interest: football
format: explain
title: Why a good first touch gives with the ball
check:
  question: |-
    A goalkeeper catches a $0.40\,\text{kg}$ ball travelling at $20\,\text{m/s}$ and brings it to rest in $0.050\,\text{s}$. What is the size of the average force between the ball and her gloves?
  options:
    A: |-
      $8.0\,\text{N}$
    B: |-
      $0.40\,\text{N}$
    C: |-
      $160\,\text{N}$
    D: |-
      $320\,\text{N}$
  answer: C
  explanation: |-
    The impulse equals the change in momentum: $0.40 \times 20 = 8.0\,\text{N s}$. The average force is $F = \Delta p / \Delta t = 8.0 / 0.050 = 160\,\text{N}$.
  misconceptions:
    A: |-
      Gives the impulse ($8.0\,\text{N s}$) as if it were the force. Impulse is force multiplied by time; to get the force, divide the change in momentum by the time.
    B: |-
      Multiplies the change in momentum by the time instead of dividing, as if a longer stop meant more force. $F = \Delta p/\Delta t$.
    D: |-
      Counts the change in momentum as $2mv$, as if the ball bounced back out at the same speed. A caught ball only goes from $mv$ to zero.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![Under floodlights, a striker follows through after a shot while the ball flies towards the goalkeeper](scenes/football/laws_of_motion.svg "Every ball that arrives, at a keeper's gloves or a player's chest, has to be stopped somehow.")

The goalkeeper launches a long kick upfield, and Sneha, playing up front for her club's under-17 side, sets herself to take it on her chest. She stands tall and braced, and the ball smacks off her and bounces five metres away, straight to a defender.

At half-time, Coach Rebello doesn't shout. He just tosses her a ball, hard, from ten metres. "Again. But this time, when it arrives, lean back and let your chest go with it."

She tries it. The ball hits her, she sinks back as it lands, and it drops dead at her feet, as if it has lost interest. Ten throws, ten perfect controls, and her chest doesn't ache any more either.

Sneha frowns. The ball arrives at the same speed each time and ends up still each time. Same ball, same stop. So what did leaning back change?

## The physics

From Newton's second law, the average net force over a time $\Delta t$ is $\vec{F} = \dfrac{\Delta\vec{p}}{\Delta t}$. Multiply both sides by $\Delta t$:

$$\vec{J} = \vec{F}_\text{avg}\,\Delta t = \Delta\vec{p}$$

The product of a force and the time it acts is the **impulse** $\vec{J}$. It is a vector in the direction of the force, measured in newton seconds, $\text{N s}$ (the same as $\text{kg m/s}$). The equation says:

**impulse = change in momentum.**

To control the ball, Sneha has to take away all its momentum. That change in momentum is **fixed** by the ball's mass and arrival speed, whatever she does. So the impulse her chest must give is fixed too. But impulse is force × time. If the time goes up, the force must come down:

$$F_\text{avg} = \frac{\Delta p}{\Delta t}$$

Braced, her chest stops the ball in a very short time, so the force is big: big enough that the ball squashes hard and springs away. Leaning back stretches the stop over a longer time, so the average force falls in the same proportion. The ball is taken gently, with nothing to bounce it away.

When the force changes during contact, the impulse is the **area under the force–time graph**. Two stops of the same ball have the same area; a long, low curve is much kinder than a tall, narrow spike.

![Force–time graph: a tall narrow triangle lasting 20 ms with a peak of 480 N, and a low wide triangle lasting 100 ms with a peak of 96 N; both have an area of 4.8 N s](figures/impulse/force-time-stiff-vs-soft.svg "Two ways to stop the same ball. The areas, and so the impulses, are equal; stretching the time five times cuts the force five times.")

A keeper's gloves, a player's shin pads and the soft landing when you bend your knees after a header all use the same idea: lengthen the time of an impact so that the same change in momentum needs less force.

## Worked example

**Given:** ball $m = 0.45\,\text{kg}$, arriving at $12\,\text{m/s}$, brought to rest. Braced chest: stopped in $0.012\,\text{s}$. Cushioned chest: stopped in $0.060\,\text{s}$ (illustrative times).
**Find:** the impulse on the ball and the average force in each case.

Take the ball's direction of travel as positive: $u = +12\,\text{m/s}$, $v = 0$.

$$J = \Delta p = m(v - u) = 0.45 \times (0 - 12) = -5.4\,\text{N s}$$

The minus sign says the impulse on the ball points backwards, against its motion. Its size is $5.4\,\text{N s}$ either way.

$$F_\text{braced} = \frac{5.4}{0.012} = 450\,\text{N} \qquad F_\text{cushioned} = \frac{5.4}{0.060} = 90\,\text{N}$$

By Newton's third law (next lesson), the ball pushes on Sneha's chest with forces of the same size: $90\,\text{N}$ instead of $450\,\text{N}$.

**Sanity check:** the time went up by $0.060/0.012 = 5$, so the force should drop by 5: $450/5 = 90$ ✓. And $90\,\text{N} \times 0.060\,\text{s} = 5.4\,\text{N s}$, the same impulse ✓.

## Where the picture breaks

We assumed both chest controls stop the ball completely. A braced chest usually doesn't: the ball rebounds, and a rebound means an even *bigger* change in momentum (it is stopped and then sent back), so the real braced force is larger still. Real contact forces rise and fall, and $\Delta p/\Delta t$ gives only the average; the peak is higher. How much an impact hurts also depends on the area it is spread over. And cushioning has limits: give too much and the ball runs away from you. The physics says a longer stop means a smaller force; the skill is timing it.

## Key takeaway

Impulse is force times the time it acts, $\vec{J} = \vec{F}_\text{avg}\,\Delta t$, and it equals the change in momentum, $\Delta\vec{p}$. When the change in momentum is fixed, as in stopping a ball, making the contact last longer reduces the average force in the same proportion. That is the physics of a soft first touch, a keeper's catch and every pad and glove.
