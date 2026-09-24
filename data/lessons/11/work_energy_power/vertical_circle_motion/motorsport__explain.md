---
concept_id: vertical_circle_motion
interest: motorsport
format: explain
title: The slowest you can go round a loop upside down
check:
  question: |-
    A car runs on the inside of a smooth vertical loop of radius $5\,\text{m}$. Take $g = 9.8\,\text{m/s}^2$. What is the minimum speed it must have **at the very top** to stay in contact with the track?
  options:
    A: |-
      $0\,\text{m/s}$ — it only has to reach the top.
    B: |-
      $9.9\,\text{m/s}$
    C: |-
      $7\,\text{m/s}$
    D: |-
      $15.7\,\text{m/s}$
  answer: C
  explanation: |-
    At the minimum the track pushes with $N = 0$, so weight alone supplies the centripetal force: $mg = mv^2/r$, giving $v_\text{top} = \sqrt{gr} = \sqrt{9.8 \times 5} = \sqrt{49} = 7\,\text{m/s}$.
  misconceptions:
    A: |-
      Treats the loop like a hill, where arriving with almost no speed is fine. On the *inside* of a loop the car must still be turning at the top, and that needs a centripetal force of at least $mg$.
    B: |-
      Uses $\sqrt{2gr}$, the speed gained by falling through the loop's radius. That number answers a different question; the condition at the top comes from the centripetal requirement, not from a drop.
    D: |-
      Quotes $\sqrt{5gr}$, which is the right formula for the minimum speed at the **bottom** of the loop, not at the top.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A race track scene: a car coasts down a hill road onto the circuit, a second car speeds along the straight with a velocity arrow, a third brakes with glowing red discs, and two people push a kart in the foreground](scenes/motorsport/work_energy_power.svg "Everything on this track is turning in a horizontal plane. A loop asks the same question in a vertical one.")

A stunt display is coming to the club's open day, and part of the deal is that the engineering students check the rig. The centrepiece is a steel loop, ten metres across, that a car is supposed to drive round — right over the top, upside down, and out the other side.

Chandni has the drawings in front of her and one number missing: how fast the car has to be going when it enters.

Rizwan, who has spent the week rebuilding the entry ramp, has a confident answer. "Fast enough to get to the top. Work out the height, work out the speed you need to climb it, add a bit for safety."

Chandni isn't convinced, and it is bothering her all afternoon. Something about the top of the loop is different from the top of a hill. On a hill, a car that only just crawls over is perfectly safe. Upside down, at walking pace, at the top of a ten-metre circle — what exactly is holding it against the track?

## The physics

A body going round a vertical circle needs a net **centripetal force** $mv^2/r$ pointing at the centre at every instant. What changes as it goes round is *which* forces are available to supply it, because gravity always points down while "towards the centre" keeps rotating.

![A mass on a string at the top, side and bottom of a vertical circle, with tension and weight drawn at each point, and the conditions for the minimum speeds at the top and bottom](figures/vertical_circle_motion/forces-top-bottom-side.svg "At the top, the contact force and the weight both point to the centre. At the bottom they point opposite ways, so the contact force there must be large.")

For a car on the **inside** of a loop, the track can only *push* inwards with a normal force $N \ge 0$ — it cannot pull, exactly like a string that can only pull and never push. (In the figure the string's tension plays the same role.)

**At the top**, "towards the centre" is straight down, so the weight and the normal force both point that way:

$$N + mg = \frac{mv_\text{top}^2}{r}$$

The car is on the point of falling away when $N = 0$, which leaves gravity alone to do the turning:

$$mg = \frac{mv_\text{top}^2}{r} \quad\Rightarrow\quad v_\text{top,min} = \sqrt{gr}$$

There is Chandni's answer. **There is a minimum speed at the top, and it is not zero.** Go slower and the required centripetal force is less than $mg$; gravity supplies more turning than the circle needs, and the car leaves the track before the top.

**At the bottom**, "towards the centre" is straight up, so $N$ and $mg$ oppose each other and $N - mg = mv_\text{bottom}^2/r$ — meaning $N$ is much larger than the car's weight down there, which is why the loop has to be built strongly and why the driver is pressed hard into the seat.

To connect the two, use conservation of mechanical energy on a smooth track. The top is a height $2r$ above the bottom:

$$\tfrac{1}{2}mv_\text{bottom}^2 = \tfrac{1}{2}mv_\text{top}^2 + mg(2r) \quad\Rightarrow\quad v_\text{bottom}^2 = v_\text{top}^2 + 4gr$$

Put in the minimum $v_\text{top}^2 = gr$:

$$v_\text{bottom,min}^2 = gr + 4gr = 5gr \quad\Rightarrow\quad v_\text{bottom,min} = \sqrt{5gr}$$

Both results are **independent of mass**, and both assume a smooth track — no friction or drag doing work.

## Worked example

**Given:** a vertical loop of radius $r = 5\,\text{m}$; the track is treated as smooth; $g = 9.8\,\text{m/s}^2$.
**Find:** the minimum speed at the top, and the entry speed at the bottom that goes with it.

*At the top:*

$$v_\text{top,min} = \sqrt{gr} = \sqrt{9.8 \times 5} = \sqrt{49} = 7\,\text{m/s}$$

Seven metres per second is about $25\,\text{km/h}$ — the car is upside down, ten metres up, at little more than a cyclist's pace.

*At the bottom:*

$$v_\text{bottom,min} = \sqrt{5gr} = \sqrt{245} \approx 15.7\,\text{m/s}$$

Roughly $56\,\text{km/h}$ on entry. So Rizwan's instinct was right that entry speed matters and wrong about why: the car does not need merely to *reach* the top, it needs to still be doing $7\,\text{m/s}$ when it gets there.

**Sanity check:** the entry speed comes out a bit more than twice the speed at the top, which makes sense — the car has traded a ten-metre climb for speed, and speed goes as the square root of energy, so a big climb makes a modest difference.

## Where the picture breaks

These are absolute minimums, and no stunt team would ever use them. At exactly $\sqrt{gr}$ the wheels are carrying zero load at the top, so there is no grip, no steering and no margin at all; a real loop is entered far faster, which presses the car onto the track the whole way round. The smooth-track assumption is also generous: friction and drag remove energy through the loop, so the true entry speed must be higher still than $\sqrt{5gr}$. A car is not a point either — it has length, so its nose and tail are at different angles round the loop at once, and a real loop is usually shaped as a teardrop rather than a circle to keep the forces on the driver tolerable at the bottom. And nothing here accounts for the wheels' own spin, or for what happens to the fuel and the oil when the car inverts.

## Key takeaway

On the inside of a vertical circle the track or string can only push or pull inwards, never outwards, so there is a **minimum speed at the top**: $v_\text{top,min} = \sqrt{gr}$, where gravity alone supplies the centripetal force. Conservation of mechanical energy over the height $2r$ then gives the matching minimum at the bottom, $v_\text{bottom,min} = \sqrt{5gr}$. Both are independent of mass and both assume no friction.
