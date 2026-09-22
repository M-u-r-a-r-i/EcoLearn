---
concept_id: momentum
interest: cricket
format: explain
title: The slower ball that is harder to stop
check:
  question: |-
    A $0.16\,\text{kg}$ ball reaches the batter at $20\,\text{m/s}$ and is driven straight back at $20\,\text{m/s}$. What is the size of the change in the ball's momentum?
  options:
    A: |-
      $0\,\text{kg m/s}$
    B: |-
      $3.2\,\text{kg m/s}$
    C: |-
      $64\,\text{kg m/s}$
    D: |-
      $6.4\,\text{kg m/s}$
  answer: D
  explanation: |-
    Taking "back towards the bowler" as positive, $p$ goes from $-3.2$ to $+3.2\,\text{kg m/s}$, so $\Delta p = 3.2 - (-3.2) = 6.4\,\text{kg m/s}$. Momentum is a vector, so reversing direction counts.
  misconceptions:
    A: |-
      Treats momentum as a scalar: same speed before and after, so "no change". Momentum has direction, and reversing it is a large change.
    B: |-
      Counts only stopping the ball ($3.2\,\text{kg m/s}$) and forgets that the bat must also send it back the other way.
    C: |-
      Squares the speed ($0.16 \times 20^2$), mixing momentum up with kinetic energy. Momentum is $mv$, proportional to speed, not speed squared.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A batter drives the ball back past the bowler in a floodlit stadium](scenes/cricket/laws_of_motion.svg "How hard a ball is to stop depends on two things, not one.")

At the academy nets, Ishita's coach has two bowling machines side by side. The first fires tennis balls, set to a scary-sounding $120\,\text{km/h}$. The second fires a real cricket ball at only $90\,\text{km/h}$.

"Catch one from each," he says. "Then tell me which was harder to stop."

Ishita goes for the tennis balls first, sure they'll be the problem — they're a third faster. They whizz in, sting a little, and settle in her hands. Then the cricket ball arrives, slower on the speed readout, and it thumps into her palms and pushes her hands back towards her chest.

"The slower ball felt heavier to stop," she says, shaking out her fingers. "How can the slower one win?"

Her friend Kabir, waiting with his pads on, asks the sharper question: "And if you hit it straight back at the same speed, has anything about the ball's motion changed at all?"

## The physics

Speed alone doesn't tell you how hard a moving body is to stop. Mass matters too. Newton combined them into one quantity, the **linear momentum**:

$$\vec{p} = m\vec{v}$$

- $m$ is the mass in kilograms, $\vec{v}$ is the velocity in metres per second.
- The SI unit is the kilogram metre per second, $\text{kg m/s}$ (equivalently $\text{N s}$).
- Momentum is proportional to mass and to velocity. Double either one and the momentum doubles.

**Momentum is a vector.** Mass is a positive scalar, so multiplying the velocity vector by $m$ gives a vector pointing the same way as the velocity. In a straight line you handle this with signs: choose a positive direction, and anything moving the other way has negative momentum.

That answers Kabir. A ball arriving at $25\,\text{m/s}$ and a ball leaving at $25\,\text{m/s}$ have the same speed but **opposite** momenta. The change is not zero; it is the biggest change you can make at that speed.

![A ball arriving leftwards at 25 m/s has momentum −4.0 kg m/s; driven back at 25 m/s it has +4.0 kg m/s; the change is +8.0 kg m/s](figures/momentum/momentum-is-a-vector.svg "Same speed, opposite arrows: the change in momentum is 8.0 kg m/s, not zero. Direction is part of momentum.")

Why does momentum match "hard to stop"? You'll see in the next lessons that the force needed to stop something in a given time is set by how much momentum it has. More momentum, more force for the same stopping time.

## Worked example

**Given:** the cricket ball, mass $0.16\,\text{kg}$, at $90\,\text{km/h}$; a tennis ball of about $0.06\,\text{kg}$ at $120\,\text{km/h}$ (illustrative values).
**Find:** each ball's momentum; then the change in momentum when the cricket ball is driven straight back at the same speed.

*Convert speeds* (divide km/h by 3.6):
$90\,\text{km/h} = 25\,\text{m/s}$ and $120\,\text{km/h} \approx 33.3\,\text{m/s}$.

*Momenta* (magnitudes):

$$p_\text{cricket} = 0.16 \times 25 = 4.0\,\text{kg m/s}$$

$$p_\text{tennis} = 0.06 \times 33.3 \approx 2.0\,\text{kg m/s}$$

The slower cricket ball has **twice** the momentum. That is why it pushed Ishita's hands back.

*Driven back.* Take the direction towards the bowler as positive. Arriving: $p_1 = -4.0\,\text{kg m/s}$. Leaving: $p_2 = +4.0\,\text{kg m/s}$.

$$\Delta p = p_2 - p_1 = 4.0 - (-4.0) = +8.0\,\text{kg m/s}$$

**Sanity check:** the speed ratio is $25/33.3 = 0.75$ and the mass ratio is $0.16/0.06 \approx 2.7$; their product is $2.0$, matching $4.0/2.0$. And $\Delta p = m\,\Delta v = 0.16 \times 50 = 8.0\,\text{kg m/s}$.

## Where the picture breaks

"Harder to stop" mixes two ideas. Momentum decides how big a push is needed to stop the ball in a given time, but how much a catch *hurts* also depends on how quickly your hands stop it and on how the ball's energy is absorbed; you'll meet impulse and kinetic energy separately. We've also treated each ball as a point moving in a straight line and ignored its spin. In two or three dimensions, momentum is a full vector with components, and signs alone are not enough.

## Key takeaway

Linear momentum is mass times velocity, $\vec{p} = m\vec{v}$, measured in $\text{kg m/s}$. It is a vector pointing along the velocity, so a ball whose direction reverses has a large change in momentum even if its speed is unchanged. A slower but heavier ball can carry more momentum than a faster, lighter one.
