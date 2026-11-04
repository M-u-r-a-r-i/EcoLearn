---
concept_id: vertical_circle_motion
interest: gaming
format: explain
title: The slowest you can go round the loop
check:
  question: |-
    A ball on a light string is whirled in a vertical circle of radius $0.40\,\text{m}$. What is the minimum speed at the **top** for the string to stay taut? (Take $g = 9.8\,\text{m/s}^2$.)
  options:
    A: |-
      $2.0\,\text{m/s}$
    B: |-
      $0$
    C: |-
      $4.4\,\text{m/s}$
    D: |-
      $3.9\,\text{m/s}$
  answer: A
  explanation: |-
    At the top, with the string just going slack ($T = 0$), gravity alone supplies the centripetal force: $mg = mv^2/r$, so $v = \sqrt{gr} = \sqrt{9.8 \times 0.40} = \sqrt{3.92} \approx 2.0\,\text{m/s}$.
  misconceptions:
    B: |-
      Assumes the string can hold the ball up at any speed; a string can only pull inwards, so at the top it cannot slow the ball's fall — below $\sqrt{gr}$ the ball leaves the circular path.
    C: |-
      Uses $\sqrt{5gr} = 4.4\,\text{m/s}$, which is the minimum speed at the *bottom* of the circle, not at the top.
    D: |-
      Stops at $gr = 3.92$ and forgets the square root; $gr$ has units of $\text{m}^2/\text{s}^2$, so it is a speed squared, not a speed.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A gaming desk at night: a monitor shows a physics sandbox with a spring launcher, a kart at the top of a loop and a crate being dragged by a rope, beside a force-feedback racing wheel and a controller](scenes/gaming/work_energy_power.svg "The kart at the top of the loop is upside down, and both the track's push and its weight point towards the centre of the circle.")

Devansh's stunt track has one loop in it, and it is ruining his playtest. Half the testers sail round it; the other half peel off the ceiling at the top and land on their roof in a shower of sparks.

His fix so far has been to keep raising the boost pad before the loop. Now the karts go round — and overshoot the next corner every time.

Sneha, who is testing for him, asks the obvious question: "What speed should I actually hit the loop at?"

Devansh doesn't know. He has been guessing. But watching the replays, something stands out: the karts that fail all fail at the *same place*, right at the top, and they fail the same way — they stop following the track before they fall. It is not that they run out of speed; they still have some. So what exactly does a kart need at the top of a loop that a slow one does not have?

## The physics

At any point on a vertical circle, the **net force towards the centre** must equal $mv^2/r$. Both the track's normal force $N$ (or a string's tension $T$) and gravity contribute, and their directions change around the loop.

![A mass on a string at the top, side and bottom of a vertical circle, with the tension and the weight drawn at each point, and the conditions for the minimum speeds](figures/vertical_circle_motion/forces-top-bottom-side.svg "At the top, the pull and the weight both point to the centre. At the bottom they point opposite ways, so the force there is large.")

**At the top**, the centre is *below* the kart, so gravity and the track's push both point that way:

$$N + mg = \frac{mv_\text{top}^2}{r}$$

A track can only push, never pull, so $N \ge 0$. The critical case is $N = 0$, where gravity alone bends the path:

$$mg = \frac{mv_\text{top}^2}{r} \quad\Rightarrow\quad v_\text{top} \ge \sqrt{gr}$$

Below that speed the kart cannot turn tightly enough to stay on the track: it leaves the loop and becomes a projectile. That is exactly what Devansh saw — the failing karts do not stop, they stop *turning*.

**At the bottom**, gravity points away from the centre, so $N - mg = mv_\text{bottom}^2/r$ and the track has to push hard; this is the heavy, pressed-into-your-seat point of the loop.

**Linking the two** uses energy. If the loop is smooth, mechanical energy is conserved between the bottom and the top, a height $2r$ higher:

$$\tfrac{1}{2}v_\text{bottom}^2 = \tfrac{1}{2}v_\text{top}^2 + g(2r) \quad\Rightarrow\quad v_\text{bottom}^2 = v_\text{top}^2 + 4gr$$

Putting the minimum top speed into this gives the minimum entry speed, $v_\text{bottom} \ge \sqrt{5gr}$.

## Worked example

**Given** (illustrative level values): a smooth loop of radius $r = 5\,\text{m}$, with $g = 9.8\,\text{m/s}^2$.
**Find:** the slowest the kart can pass the top, and the slowest it can enter at the bottom.

**Step 1 — the top.** With the track just about to lose contact:

$$v_\text{top} = \sqrt{gr} = \sqrt{9.8 \times 5} = \sqrt{49} = 7\,\text{m/s}$$

Anything slower and the kart falls away from the track instead of following it.

**Step 2 — the bottom.** Climbing to the top costs the height $2r = 10\,\text{m}$:

$$v_\text{bottom}^2 = v_\text{top}^2 + 4gr = 49 + 4 \times 9.8 \times 5 = 49 + 196 = 245$$

$$v_\text{bottom} = \sqrt{245} \approx 15.7\,\text{m/s}$$

That is about $56\,\text{km/h}$ — city traffic speed — to creep round a loop the height of a three-storey building.

**Sanity check:** the entry speed has to be much larger than the top speed, because most of the entry energy is spent climbing $10\,\text{m}$; an entry speed *smaller* than the top speed would have been nonsense.

## Where the picture breaks

The figure shows a ball on a string, where tension replaces the track's normal force; the physics is identical except that a string can go slack and a loop's track simply stops pushing. Both were assumed smooth and drag-free, so a real kart needs a margin above $15.7\,\text{m/s}$, and game loops are usually clothoid-shaped rather than circular so that the radius is tighter at the top. A real kart is also not a point: its wheels and its own rotation carry energy, and downforce can hold a car on the track below the "minimum" speed. And $v_\text{top} = \sqrt{gr}$ is a knife edge — designing a level to sit exactly on it guarantees half your testers fall off.

## Key takeaway

Going round a vertical circle needs the net inward force to equal $mv^2/r$ everywhere. At the top, gravity and the track both push inwards, so the slowest safe speed is $v_\text{top} = \sqrt{gr}$, where the track's push has fallen to zero. Adding the energy needed to climb the height $2r$ gives the minimum speed at the bottom, $v_\text{bottom} = \sqrt{5gr}$.
