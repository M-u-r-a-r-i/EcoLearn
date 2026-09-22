---
concept_id: impulse
interest: cricket
format: explain
title: Why coaches shout soft hands at every catch
check:
  question: |-
    A fielder catches a ball once with stiff hands, stopping it in $0.03\,\text{s}$, and once by drawing her hands back so the catch lasts $0.12\,\text{s}$. The ball arrives at the same speed both times. Compared with the stiff catch, in the soft catch the impulse on the ball is ____ and the average force is ____.
  options:
    A: |-
      smaller; smaller
    B: |-
      the same; one quarter as large
    C: |-
      the same; the same
    D: |-
      four times as large; the same
  answer: B
  explanation: |-
    The impulse equals the change in momentum, which is the same because the ball goes from the same speed to rest. Since $F_\text{avg} = \Delta p / \Delta t$, making $\Delta t$ four times longer makes the average force four times smaller.
  misconceptions:
    A: |-
      Thinks soft hands reduce the impulse. The impulse is fixed by the ball's change in momentum; soft hands only spread it over more time.
    C: |-
      Thinks the force depends only on the ball's speed and mass, ignoring how long the stopping takes.
    D: |-
      Multiplies by the time as if the force stayed fixed. The change in momentum is what is fixed, so a longer time means a smaller force, not a bigger impulse.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A batter drives the ball back past the bowler in a floodlit stadium](scenes/cricket/laws_of_motion.svg "A hard hit like this one is exactly what a close fielder has to stop with bare hands.")

The batter rocks back and pulls hard. At short midwicket, Kavya has half a second to react. The ball hits her palms with a *smack*, bursts out and drops on the grass. Her hands are stinging.

At drinks, the coach, Mr Bhatia, makes her try again with throw-downs. "Soft hands," he says. "Let your hands travel back with the ball."

She catches the next ten without a drop, and they barely sting. But Kavya is annoyed rather than pleased. "It makes no sense," she says. "The ball arrives at the same speed and ends up stopped either way. It's the same ball, the same stop. How can moving my hands backwards change how hard it hits me?"

Mr Bhatia just smiles. The same trick is inside every batting helmet and every pair of pads. What is it?

## The physics

From Newton's second law, $\vec{F}_\text{net} = \dfrac{\Delta \vec{p}}{\Delta t}$ for the average force over a time $\Delta t$. Multiply both sides by $\Delta t$:

$$\vec{J} = \vec{F}_\text{avg}\,\Delta t = \Delta \vec{p}$$

The product of force and the time it acts is called the **impulse**, $\vec{J}$. It is a vector in the direction of the force, and its SI unit is the newton second, $\text{N s}$, the same as $\text{kg m/s}$. The equation says:

**impulse = change in momentum.**

Now look at Kavya's catch. The ball arrives with some momentum and ends at rest, so the change in momentum is **fixed** by the ball, whatever she does. The impulse her hands must deliver is therefore fixed too. But the impulse is a *product*, force × time. If she makes the time longer, the force must be smaller:

$$F_\text{avg} = \frac{\Delta p}{\Delta t}$$

Stiff hands stop the ball in a very short time, so the force is large. Soft hands, drawn back, stretch the stop over a longer time, so the average force falls in the same proportion. That is all "soft hands" is.

For a force that changes during the contact, the impulse is the **area under the force–time graph**. Two catches of the same ball have the same area, but a long, low curve is far kinder to your palms than a tall, narrow spike.

![Force–time graph: a tall narrow triangle lasting 20 ms with a peak of 480 N, and a low wide triangle lasting 100 ms with a peak of 96 N; both have an area of 4.8 N s](figures/impulse/force-time-stiff-vs-soft.svg "Both catches deliver the same impulse, 4.8 N s, because the areas are equal. Spreading it over five times the time cuts the force five times.")

Helmet foam, thigh pads and the padding in batting gloves use the same idea: they lengthen the time of an impact so that the same change in momentum needs less force.

## Worked example

**Given:** ball mass $m = 0.16\,\text{kg}$, arriving at $30\,\text{m/s}$ (about $108\,\text{km/h}$), caught and brought to rest. Stiff hands stop it in $0.020\,\text{s}$; soft hands in $0.10\,\text{s}$ (illustrative times).
**Find:** the impulse on the ball and the average force in each catch.

Take the ball's direction of travel as positive: $u = +30\,\text{m/s}$, $v = 0$.

$$J = \Delta p = m(v - u) = 0.16 \times (0 - 30) = -4.8\,\text{N s}$$

The minus sign says the impulse on the ball points backwards, against its motion. Its size is $4.8\,\text{N s}$ in both catches.

$$F_\text{stiff} = \frac{4.8}{0.020} = 240\,\text{N} \qquad F_\text{soft} = \frac{4.8}{0.10} = 48\,\text{N}$$

By Newton's third law (coming next), the ball pushes on the hands with equal-sized forces. Soft hands take $48\,\text{N}$ instead of $240\,\text{N}$ — five times less.

**Sanity check:** the time went up by a factor $0.10/0.020 = 5$, so the force should fall by 5: $240/5 = 48$. And $48\,\text{N} \times 0.10\,\text{s} = 4.8\,\text{N s}$, the same impulse.

## Where the picture breaks

The force in a real catch is not constant, and its peak is higher than the average; $\Delta p / \Delta t$ gives only the average. How much a catch hurts also depends on the area of palm the force is spread over and on how your hands absorb energy, not on force alone. And drawing the hands back only works up to a point: pull them back too fast and the ball never settles. The physics says a longer stop means a smaller force; the skill is making that stop controlled.

## Key takeaway

Impulse is force multiplied by the time it acts, $\vec{J} = \vec{F}_\text{avg}\,\Delta t$, and it equals the change in momentum, $\Delta\vec{p}$. When the change in momentum is fixed, as in stopping a ball, stretching the collision time reduces the average force in the same proportion. That is why soft hands, pads and helmets work.
