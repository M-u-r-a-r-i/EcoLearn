---
concept_id: uniform_circular_motion
interest: cricket
format: explain
title: Why letting go too early sends the ball sailing high
check:
  question: |-
    A fielder jogs round a circular track at a steady $5\,\text{m/s}$ during warm-ups. Which statement about the fielder is correct?
  options:
    A: |-
      The velocity keeps changing because its direction keeps changing, so the fielder is accelerating.
    B: |-
      The velocity is constant because the speed stays at $5\,\text{m/s}$.
    C: |-
      The velocity at each moment points towards the centre of the track.
    D: |-
      If the fielder suddenly stopped steering, they would carry on curving round for a while before going straight.
  answer: A
  explanation: |-
    Velocity is a vector, so a change of direction is a change of velocity even when the speed is constant. A changing velocity means an acceleration.
  misconceptions:
    B: |-
      Treats speed and velocity as the same thing. Speed is only the size of the velocity; the direction is changing all the time.
    C: |-
      Confuses the direction of the velocity with the radius. The velocity is along the tangent, at right angles to the radius.
    D: |-
      Believes a body "remembers" curved motion and keeps curving on its own. Without something to turn it, a moving body goes straight, along the tangent.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A day match: a batter lofts the ball towards the boundary as a fielder races along the rope](scenes/cricket/motion_plane.svg "Cricket is full of curved motion: the path of a lofted ball, a fielder chasing round the rope, a bowler's arm swinging over.")

Pooja is sixteen and quick, but lately something has gone wrong with her bowling. Every few overs, a ball slips out and sails high over the batter's head.

Her coach, Mr Venkat, films her from side-on and plays it back frame by frame. Her bowling arm swings round in a big arc, up behind her head, over the top and down in front. On the bad balls, the ball leaves her fingers early, while her hand is still behind her head.

"But my arm is swinging *forwards* when I let go," Pooja says. "How does the ball end up going *up*?"

"The ball doesn't know your arm was going round," says Mr Venkat. "The moment you let go, it simply carries on the way it was moving at that instant."

So which way *is* something moving, at each instant, when it goes round in a circle?

## The physics

**Uniform circular motion** is motion along a circle at **constant speed**. Examples include a point on a spinning wheel, a satellite in a circular orbit, or, in an idealised model, a bowler's hand in the last part of the arm swing.

At every instant, the velocity points along the **tangent** to the circle, at right angles to the radius. If whatever keeps the object on the circle lets go, it moves off along that tangent in a straight line.

![Left: a circle with six equal velocity arrows, each tangent to the circle, and a dashed tangent line at the top labelled 'let go here: it leaves along the tangent'. Right: the same six arrows drawn from one point, forming a star](figures/uniform_circular_motion/velocity-around-circle.svg "Every velocity arrow has the same length, because the speed is constant, but each points a different way. Redrawn from one point, they fan out in all directions: the velocity is always changing.")

That explains Pooja's problem. Just before the top of the swing, the tangent points forward *and upward*, so a ball released there flies up. Released exactly at the top, it leaves horizontally. Released late, past the top, the tangent points forward and down, and the ball goes into the ground short.

The key point: **velocity is a vector**. In uniform circular motion the speed (its size) is constant, but the direction changes continuously. So the velocity changes continuously, and a changing velocity means the body is **accelerating**, even though it never speeds up or slows down. You'll find the size and direction of this acceleration in the next lesson.

Some terms for describing the motion, for a circle of radius $r$:

- **Period** $T$: time for one full revolution, $T = \dfrac{2\pi r}{v}$.
- **Frequency** $\nu = 1/T$: revolutions per second.
- **Angular speed** $\omega = \dfrac{2\pi}{T}$ (in rad/s): the angle swept per second. The speed is $v = \omega r$.

## Worked example

**Given (illustrative):** treat the last part of Pooja's arm swing as uniform circular motion: the ball moves on a circle of radius $r = 0.80\,\text{m}$ about her shoulder at a steady $v = 20\,\text{m/s}$.
**Find:** the angular speed, the period, and the change in velocity over a quarter-turn, from pointing straight up to pointing straight forward.

$$\omega = \frac{v}{r} = \frac{20}{0.80} = 25\,\text{rad/s}, \qquad T = \frac{2\pi}{\omega} = \frac{6.28}{25} \approx 0.25\,\text{s}$$

Over a quarter-turn (taking about $0.063\,\text{s}$), the velocity goes from $20\,\text{m/s}$ up to $20\,\text{m/s}$ forward. These are at right angles, so the change is

$$|\Delta\vec{v}| = \sqrt{20^2 + 20^2} \approx 28\,\text{m/s}$$

The speed changed by **zero**, but the velocity changed by about $28\,\text{m/s}$.

**Sanity check:** $T = 2\pi r/v = 2\pi(0.80)/20 \approx 0.25\,\text{s}$ agrees. Over a half-turn the velocity reverses, so $|\Delta\vec{v}| = 2v = 40\,\text{m/s}$, the largest possible change.

## Where the picture breaks

A real bowling arm is **not** in uniform circular motion. The hand speeds up through the swing, the shoulder moves forward with the run-up and body, and the wrist flicks at the end. So the ball's real release velocity is the hand's full velocity relative to the ground, including the body's forward motion. What does carry over exactly is the tangent rule: at release, the ball leaves with the velocity it had that instant, and from then on only gravity and air act on it.

## Key takeaway

In uniform circular motion the speed is constant but the velocity is not: it always points along the tangent, and its direction keeps turning. A changing velocity means acceleration, so a body going round a circle at steady speed is accelerating. Let go at any instant, and it leaves along the tangent at that point.
