---
concept_id: displacement
interest: motorsport
format: explain
title: Two metres too far in the pit box
check:
  question: |-
    Take the origin at the pit-box marker and the positive direction as the way the cars travel down the pit lane. A kart rolls to a stop at $x = +3.0\,\text{m}$. Its crew then pushes it back to $x = -1.0\,\text{m}$ to line it up with the fuel rig. What is the kart's displacement during the push?
  options:
    A: |-
      $+4.0\,\text{m}$
    B: |-
      $-4.0\,\text{m}$
    C: |-
      $-1.0\,\text{m}$
    D: |-
      $+2.0\,\text{m}$
  answer: B
  explanation: |-
    Displacement is final position minus initial position: $\Delta x = (-1.0) - (+3.0) = -4.0\,\text{m}$. The kart moved $4.0\,\text{m}$ against the direction of travel.
  misconceptions:
    A: |-
      Subtracts the wrong way round (initial minus final), or drops the sign because "it moved four metres". The sign carries the direction, and it must come from final minus initial.
    C: |-
      Reports the final position as the displacement. Position says where the kart is; displacement says how its position changed.
    D: |-
      Adds the two positions, $3.0 + (-1.0)$, instead of subtracting them — treating displacement as a total of the numbers on the scale.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A long straight at a race circuit with a car accelerating away from the timing beam at the start line, distance boards reading 0, 100 and 200 along the verge, and an arrow marking the positive direction](scenes/motorsport/motion_straight_line.svg "Along the pit lane, as along the straight, there are only two ways to move: forward or back.")

Ishita has the least glamorous job on her college endurance team and the one everyone shouts about: she stands at the pit box holding the board that tells the driver where to stop.

Karan comes in hot, locks a front wheel, and the car slides to a halt two metres past the marks. The jack will not reach. Four mechanics heave the car backwards to the marks, and the stop takes eleven seconds longer than it should have.

Afterwards Karan reads the data trace and grins. "Look. Displacement during the stop: zero. So I didn't overshoot at all."

Ishita is not impressed. The wheels rolled forward two metres and then backward two metres, and she has the sore arms to prove the second part.

Zero is clearly the honest answer to *something*. What question is it answering — and which question was the one that cost the team eleven seconds?

## The physics

**Displacement** is the change in position. In one dimension, if an object starts at $x_i$ and ends at $x_f$,

$$\Delta x = x_f - x_i$$

It is a **vector**: it has a size and a direction. Along a line the direction is carried entirely by the **sign**. A plus means the object ended further along the positive direction; a minus means it ended further the other way.

Three properties follow straight from the definition:

- It depends only on the **start and the end**, never on the path between them.
- Its size is never larger than the distance travelled — equal if the motion never reverses, smaller if it does.
- Any round trip gives $\Delta x = 0$, however far the wheels rolled.

![Three trips on a line: from 1 m to 5 m gives Δx = +4 m; from 5 m to 2 m gives Δx = −3 m; out 3 m and back gives Δx = 0 m although the distance is 6 m](figures/displacement/sign-in-one-dimension.svg "Displacement is final minus initial. The arrow's direction gives the sign; a round trip gives zero whatever the distance.")

So Karan is right and irrelevant. Over the whole stop the car finished where it was supposed to be, so $\Delta x = 0$ for the stop as a whole — while the distance the wheels covered was $2 + 2 = 4\,\text{m}$. The question that cost eleven seconds was about a single moment: at the instant the car first stopped, what was its position? Not $0$, but $+2\,\text{m}$ — and the jack does not care how the car got there.

## Worked example

**Given:** origin at the pit-box front marker, positive in the direction the cars travel down the pit lane. The car first stops at $x = +2.0\,\text{m}$. The crew pushes it back to the marker, $x = 0$. It later leaves and reaches the pit-exit line at $x = +80\,\text{m}$ (illustrative).
**Find:** the displacement in the push, the displacement in the drive out, and the displacement and distance from arrival to pit exit.

**The push.** $x_i = +2.0\,\text{m}$, $x_f = 0$:

$$\Delta x = 0 - 2.0 = -2.0\,\text{m}$$

The minus sign says the car moved back up the pit lane, against the direction of travel.

**The drive out.** $x_i = 0$, $x_f = +80\,\text{m}$:

$$\Delta x = 80 - 0 = +80\,\text{m}$$

**Arrival to pit exit.** Start $+2.0\,\text{m}$, finish $+80\,\text{m}$, so $\Delta x = 80 - 2.0 = +78\,\text{m}$, while the distance covered is $2.0 + 80 = 82\,\text{m}$.

**Sanity check:** the overshoot and the push are the same size with opposite signs, which is what "back to where it should have been" must mean. And the displacement ($78\,\text{m}$) comes out smaller than the distance ($82\,\text{m}$), exactly by the $4\,\text{m}$ the car wasted going forwards and back.

## Where the picture breaks

We have flattened the whole stop onto the line of the pit lane. The car also moved sideways as it slid, and the wheel that locked left a mark that is not on our axis at all. Real stop positions are judged against a box painted on the ground, so what matters is whether the car lies inside a region, not a single number — the position of one point (the front axle, say) stands in for the whole car. And the sign convention is a free choice: had we taken positive up the pit lane instead, every sign here would flip while nothing physical changed.

## Key takeaway

Displacement is the change in position, $\Delta x = x_f - x_i$: a vector from where you started to where you finished, its direction shown by a sign in one dimension. It ignores the path completely, so a round trip gives zero — which is why "my displacement was zero" is no defence for stopping two metres too far.
