---
concept_id: uniform_circular_motion
interest: football
format: explain
title: Why a steady jog round the centre circle still counts as accelerating
check:
  question: |-
    Seen from above, a player dribbles anticlockwise round the centre circle at a steady speed. At the moment she is at the northernmost point of the circle, she stops steering and just taps the ball straight on. Ignoring friction's slowing effect, which way does the ball roll?
  options:
    A: |-
      North, straight outwards, away from the centre
    B: |-
      West, along the tangent to the circle at that point
    C: |-
      South, towards the centre of the circle
    D: |-
      West at first, then curving round the circle for a while before straightening out
  answer: B
  explanation: |-
    In circular motion the velocity at each instant is along the tangent. Going anticlockwise, at the northernmost point that is due west, and with nothing turning it, the ball carries on in that straight line.
  misconceptions:
    A: |-
      Believes objects are flung outwards along the radius when released from a circle. They leave along the tangent, at right angles to the radius.
    C: |-
      Confuses the direction of the velocity with the direction towards the centre. The inward direction belongs to the acceleration, not to the velocity.
    D: |-
      Believes a body "remembers" curved motion and keeps curving on its own. Without something to turn it, a moving body goes straight.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A player lofts the ball in an arc over the goalkeeper while a teammate jogs round the centre circle](scenes/football/motion_plane.svg "Look at the player on the centre circle: however steadily they run, their velocity arrow must keep turning to follow the line.")

Aarav's academy has started using GPS vests in training. The warm-up drill is simple: dribble round the painted centre circle at an easy, steady pace, keeping the ball on the line.

Afterwards the sports scientist, Ms Rao, shows him the data. His speed trace is almost perfectly flat, about $4\,\text{m/s}$ the whole way round. But the vest's accelerometer trace is not zero. It shows a steady reading for the whole drill.

"Your vest's broken," says Aarav. "I never sped up and never slowed down. How can I be accelerating?"

"It's working fine," says Ms Rao. "Try this. Go round again, and halfway through, stop steering the ball and just tap it straight on. Watch where it goes."

Where does the ball go, and how can someone moving at a perfectly steady speed be accelerating?

## The physics

**Uniform circular motion** is motion along a circle at **constant speed**. Examples: a point on a spinning wheel, a satellite in a circular orbit, or Aarav jogging round the $9.15\,\text{m}$ radius of the centre circle at a steady pace.

At every instant, the velocity points along the **tangent** to the circle, at right angles to the radius. Nothing about the velocity points "round" the circle. If whatever keeps the body turning stops, it moves off along that tangent, in a straight line. That is Ms Rao's test: the moment Aarav stops steering, the ball rolls off along the tangent, not round the curve and not outwards.

![Left: a circle with six equal velocity arrows, each tangent to the circle, and a dashed tangent line at the top labelled 'let go here: it leaves along the tangent'. Right: the same six arrows drawn from one point, forming a star](figures/uniform_circular_motion/velocity-around-circle.svg "Every velocity arrow has the same length, because the speed is constant, but each points a different way. Redrawn from one point, they fan out in all directions: the velocity never stays the same.")

The key point: **velocity is a vector**. In uniform circular motion its size, the speed, is constant, but its direction changes continuously. So the velocity changes continuously, and a changing velocity *is* an acceleration, even though the body never speeds up or slows down. Aarav's vest is measuring exactly that. You'll find the size and direction of this acceleration in the next lesson.

Some terms, for a circle of radius $r$:

- **Period** $T$: the time for one full revolution, $T = \dfrac{2\pi r}{v}$.
- **Frequency** $\nu = 1/T$: revolutions per second.
- **Angular speed** $\omega = \dfrac{2\pi}{T}$, in rad/s: the angle swept per second. The speed is $v = \omega r$.

## Worked example

**Given:** the centre circle has radius $r = 9.15\,\text{m}$. Aarav jogs round it at a steady $v = 4.0\,\text{m/s}$ (illustrative).
**Find:** the period, the angular speed, and the change in his velocity over a quarter-lap.

$$T = \frac{2\pi r}{v} = \frac{2\pi \times 9.15}{4.0} = \frac{57.5}{4.0} \approx 14.4\,\text{s}, \qquad \omega = \frac{v}{r} = \frac{4.0}{9.15} \approx 0.44\,\text{rad/s}$$

Over a quarter-lap, about $3.6\,\text{s}$, his velocity turns through $90^\circ$: say from $4.0\,\text{m/s}$ north to $4.0\,\text{m/s}$ west. These are at right angles, and the change is final minus initial, so

$$|\Delta\vec{v}| = \sqrt{4.0^2 + 4.0^2} \approx 5.7\,\text{m/s}$$

His speed changed by **zero**, but his velocity changed by about $5.7\,\text{m/s}$, more than his speed itself.

**Sanity check:** $2\pi/\omega = 6.28/0.437 \approx 14.4\,\text{s}$, matching $T$. Over half a lap the velocity reverses, so $|\Delta\vec{v}| = 2v = 8.0\,\text{m/s}$, the biggest change possible.

## Where the picture breaks

Nobody jogs a perfect circle at a perfectly steady speed. Aarav's speed wobbles with each stride, and his path drifts slightly off the line, so his real motion is only close to uniform circular motion. A rolling ball also slows because of friction with the grass, so after he taps it, it goes straight but gradually loses speed. What carries over exactly is the tangent rule: the ball leaves with the velocity it had at that instant, and with nothing turning it, it doesn't curve.

## Key takeaway

In uniform circular motion the speed is constant but the velocity is not: it always points along the tangent, and its direction keeps turning. A changing velocity means an acceleration, so a body going round a circle at steady speed is accelerating. Stop turning it, and it leaves along the tangent at that point.
