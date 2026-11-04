---
concept_id: momentum
interest: football
format: explain
title: The shot that bounced off the post at full speed
check:
  question: |-
    A $0.45\,\text{kg}$ football hits the post at $20\,\text{m/s}$ and bounces straight back at $20\,\text{m/s}$. What is the size of the change in the ball's momentum?
  options:
    A: |-
      $0\,\text{kg m/s}$
    B: |-
      $9.0\,\text{kg m/s}$
    C: |-
      $180\,\text{kg m/s}$
    D: |-
      $18\,\text{kg m/s}$
  answer: D
  explanation: |-
    Taking "away from the post" as positive, $p$ goes from $-9.0$ to $+9.0\,\text{kg m/s}$, so $\Delta p = 9.0 - (-9.0) = 18\,\text{kg m/s}$. Momentum is a vector, so reversing the direction is a change.
  misconceptions:
    A: |-
      Treats momentum as a scalar: same speed before and after, so "no change". Momentum has a direction, and reversing it is the largest change possible at that speed.
    B: |-
      Counts only stopping the ball ($9.0\,\text{kg m/s}$) and forgets that the post must also send it back the other way.
    C: |-
      Squares the speed ($0.45 \times 20^2$), mixing momentum up with kinetic energy. Momentum is $mv$, proportional to speed, not speed squared.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![Under floodlights, a striker follows through after a shot while the ball flies towards the goalkeeper](scenes/football/laws_of_motion.svg "The ball is fast but light. The players are slow but heavy. Which is harder to stop?")

It's the second half of the inter-college final and Kiran, the centre-back, has one job: get in the way. The opposing striker hits a drive from the edge of the box, and Kiran throws himself in front of it. The ball smacks off his chest and flies straight back out, almost as fast as it came in.

On the bench, the substitutes argue about the replay on a phone.

"Nothing happened to the ball," says Pallavi. "Same speed in, same speed out. Kiran just stood there."

"Then why is he still rubbing his chest?" says Sameer. "And another thing: the ball was going far faster than Kiran ever runs. So when he charged at the striker a minute earlier, was he easier to stop than the ball, or harder?"

Speed alone doesn't seem to settle either argument. What does?

## The physics

How hard a moving body is to stop depends on its mass as well as its velocity. Newton combined the two into one quantity, the **linear momentum**:

$$\vec{p} = m\vec{v}$$

- $m$ is the mass in kilograms and $\vec{v}$ the velocity in metres per second.
- The SI unit is the kilogram metre per second, $\text{kg m/s}$ (the same as $\text{N s}$).
- Momentum is proportional to both. Double the mass or double the velocity and the momentum doubles.

**Momentum is a vector.** Mass is a positive scalar, so $m\vec{v}$ points the same way as $\vec{v}$. In a straight line, handle the direction with signs: choose a positive direction, and anything moving the other way has negative momentum.

That settles Pallavi's claim. The ball arriving at Kiran and the ball leaving him have the same speed but **opposite** momenta. The change is not zero; at that speed, it is the biggest change there can be. Kiran's chest had to stop the ball *and* send it back, which is why it hurt.

![A ball arriving leftwards at 25 m/s has momentum −4.0 kg m/s; driven back at 25 m/s it has +4.0 kg m/s; the change is +8.0 kg m/s](figures/momentum/momentum-is-a-vector.svg "Drawn for a lighter ball, but the idea is the same for a football: same speed, opposite arrows, so the change in momentum is twice the momentum, not zero.")

And Sameer's question: a body's momentum can be large because it is fast *or* because it is heavy. A charging defender is slow, but his mass is more than a hundred times the ball's. In the next lessons you'll see that the force needed to stop something in a given time is set by its momentum.

## Worked example

**Given:** football $m = 0.43\,\text{kg}$ at $25\,\text{m/s}$; a $70\,\text{kg}$ player running at $3.0\,\text{m/s}$ (illustrative values).
**Find:** (a) the momentum of each; (b) the change in the ball's momentum if it arrives at $15\,\text{m/s}$ and rebounds straight back at $15\,\text{m/s}$.

(a) Magnitudes:

$$p_\text{ball} = 0.43 \times 25 \approx 10.8\,\text{kg m/s}$$

$$p_\text{player} = 70 \times 3.0 = 210\,\text{kg m/s}$$

The jogging player has about 20 times the momentum of the flying ball.

(b) Take "away from Kiran" as positive. Arriving: $p_1 = 0.43 \times (-15) = -6.45\,\text{kg m/s}$. Leaving: $p_2 = +6.45\,\text{kg m/s}$.

$$\Delta p = p_2 - p_1 = 6.45 - (-6.45) \approx +12.9\,\text{kg m/s}$$

**Sanity check:** in (a), the mass ratio is $70/0.43 \approx 163$ and the speed ratio $3.0/25 = 0.12$; the product is about $19.5$, matching $210/10.8$. In (b), $\Delta p = m\,\Delta v = 0.43 \times 30 = 12.9\,\text{kg m/s}$.

## Where the picture breaks

"Harder to stop" is only part of what momentum measures. How much a block *hurts* also depends on how quickly the ball is stopped and over what area of the body, ideas you'll meet with impulse. A real rebound off a chest is never at exactly the same speed: some energy goes into squashing the ball and the body, so it usually comes back slower. We also treated the ball as a point moving in a straight line and ignored its spin. In two dimensions, such as a ball glancing off a player at an angle, momentum is a full vector with components, and plus and minus signs are no longer enough.

## Key takeaway

Linear momentum is mass times velocity, $\vec{p} = m\vec{v}$, in $\text{kg m/s}$. It is a vector along the velocity, so a ball that rebounds at the same speed has a large change in momentum, twice its original size. A slow, heavy player can carry far more momentum than a fast, light ball.
