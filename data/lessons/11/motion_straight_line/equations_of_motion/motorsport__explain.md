---
concept_id: equations_of_motion
interest: motorsport
format: explain
title: Where should she actually hit the brakes
check:
  question: |-
    A kart moving at $12\,\text{m/s}$ brakes uniformly and comes to rest in $8.0\,\text{m}$. Taking its direction of motion as positive, what is its acceleration?
  options:
    A: |-
      $-9.0\,\text{m/s}^2$
    B: |-
      $-18\,\text{m/s}^2$
    C: |-
      $-1.5\,\text{m/s}^2$
    D: |-
      $+9.0\,\text{m/s}^2$
  answer: A
  explanation: |-
    No time is given, so use $v^2 = u^2 + 2as$: $0 = 12^2 + 2a(8.0)$, giving $a = -144/16 = -9.0\,\text{m/s}^2$, negative because it points against the motion.
  misconceptions:
    B: |-
      Leaves out the factor of $2$ in $v^2 = u^2 + 2as$ and computes $144/8.0$.
    C: |-
      Divides the speed by the stopping distance, $12/8.0$, as if $a = \Delta v/\Delta t$ worked with a distance in place of a time. The units come out as $\text{s}^{-1}$, not $\text{m/s}^2$.
    D: |-
      Gets the size right but ignores the sign convention. Slowing down while moving in the positive direction requires a negative acceleration.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A long straight at a race circuit with a car accelerating away from the timing beam at the start line, distance boards reading 0, 100 and 200 along the verge, and an arrow marking the positive direction](scenes/motorsport/motion_straight_line.svg "The boards down the straight are not decoration. They are there so a driver can decide, once, where to brake.")

Ayesha has booked her first track day and is losing two seconds a lap in the same place every time.

"You're braking at the two-hundred board," says Prakash, her instructor, replaying the onboard footage in the paddock. "Then coasting. You could have driven halfway to the corner before you needed to touch the pedal."

"If I brake later I'll go straight on," says Ayesha. "The corner's *right there*."

"Maybe. How much room do you actually need?"

She has no idea. She knows roughly how fast she arrives, she knows roughly how slow she needs to be for the corner, and she knows her tyres will only shed speed so quickly. Everything else has been guesswork and nerve.

The braking force is steady once the pedal is down and the tyres are working. Surely that is enough to work out the answer instead of guessing it?

## The physics

When an object moves along a straight line with **constant acceleration** $a$, three equations tie together the initial velocity $u$, the final velocity $v$, the displacement $s$ and the time $t$:

$$v = u + at$$

$$s = ut + \tfrac{1}{2}at^2$$

$$v^2 = u^2 + 2as$$

Each one leaves out a different quantity: the first has no $s$, the second no $v$, the third no $t$. Choose the one containing the three things you know and the thing you want.

Where they come from:

- **$v = u + at$** is the definition of acceleration, $a = (v - u)/t$, rearranged — valid only while $a$ stays constant.
- **$s = ut + \tfrac{1}{2}at^2$** is the area under the straight $v$–$t$ line: a rectangle $ut$ plus a triangle $\tfrac{1}{2}t(at)$.
- **$v^2 = u^2 + 2as$** comes from eliminating $t$ between the other two.

![A velocity–time graph rising in a straight line, with the area below it split into a rectangle of height u and a triangle of height at](figures/equations_of_motion/vt-area-derivation.svg "The displacement is the area under the line: the rectangle ut plus the triangle ½at². That is where the second equation comes from.")

**Signs matter more than anything else here.** Pick a positive direction and then give every vector — $u$, $v$, $a$ and $s$ — its sign. For a car braking while travelling forwards, $u$ and $v$ are positive and $a$ is negative, all the way through the braking zone.

## Worked example

**Given:** Ayesha arrives at $u = 40\,\text{m/s}$ ($144\,\text{km/h}$) and needs to be down to $v = 20\,\text{m/s}$ ($72\,\text{km/h}$) at the corner. Under firm braking the car loses speed at a steady $10\,\text{m/s}^2$, so $a = -10\,\text{m/s}^2$ (illustrative, about $1g$). Positive is her direction of travel.
**Find:** how much track the braking takes, and how long it lasts.

**The distance.** No time is involved, so use $v^2 = u^2 + 2as$:

$$20^2 = 40^2 + 2(-10)s \;\Rightarrow\; 400 = 1600 - 20s \;\Rightarrow\; s = \frac{1200}{20} = 60\,\text{m}$$

So she needs $60\,\text{m}$ — not the $200\,\text{m}$ she has been giving herself.

**The time.** Now use $v = u + at$:

$$20 = 40 - 10t \;\Rightarrow\; t = \frac{20}{10} = 2.0\,\text{s}$$

Two seconds of braking, over a stretch of track a little longer than an Olympic swimming pool.

**Sanity check:** with constant acceleration the average velocity is simply $(u + v)/2 = 30\,\text{m/s}$, and $30 \times 2.0 = 60\,\text{m}$ — the same distance, found a different way.

## Where the picture breaks

The equations demand a **constant** acceleration, and real braking is not quite that. Grip changes as fuel burns off and tyres heat up; a car with downforce can brake hardest at high speed, where the wings press it down, and less hard as it slows; and the first tenths of a second go into the pedal moving and the weight shifting forward. Cold or overheated brakes change the number again. So $60\,\text{m}$ is the physics answer for an idealised, steady $10\,\text{m/s}^2$, and it is a floor, not a target: drivers leave a margin because tyres do not warn you before they let go. Reaction time is left out entirely — the equations start counting from the instant the deceleration begins.

## Key takeaway

For constant acceleration in a straight line: $v = u + at$, $s = ut + \tfrac{1}{2}at^2$ and $v^2 = u^2 + 2as$. Fix a positive direction, sign every vector, and pick the equation that holds what you know and what you want. Shedding $40\,\text{m/s}$ to $20\,\text{m/s}$ at $10\,\text{m/s}^2$ takes $60\,\text{m}$ and $2.0$ seconds — which is why braking markers exist, and why guessing costs seconds.
