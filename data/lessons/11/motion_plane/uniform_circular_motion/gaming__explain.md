---
concept_id: uniform_circular_motion
interest: gaming
format: explain
title: The orbiting fireball that flew off the wrong way
check:
  question: |-
    In a racing game, a kart drives around a circular track at a steady $20\,\text{m/s}$ on its speedometer. Which statement about its motion is correct?
  options:
    A: |-
      Its velocity is constant, because its speed is constant.
    B: |-
      Its acceleration is zero, because the speedometer never changes.
    C: |-
      Its velocity always points towards the centre of the track.
    D: |-
      Its velocity keeps changing, because its direction keeps changing.
  answer: D
  explanation: |-
    Velocity is a vector: it has a size and a direction. The speed (the size) stays $20\,\text{m/s}$, but the direction, along the tangent, turns continuously, so the velocity changes and the kart is accelerating.
  misconceptions:
    A: |-
      Treats speed and velocity as the same thing. Constant speed means only the size of the velocity is constant; its direction can still change.
    B: |-
      Thinks acceleration means only speeding up or slowing down. Any change in velocity, including a change of direction, is an acceleration.
    C: |-
      Confuses the direction of the velocity with the direction of the acceleration. The velocity is along the tangent; it is the acceleration that points towards the centre.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A gaming desk at night: the monitor shows an artillery game; a tablet shows a top-down minimap of a circular kart track, with a blue velocity arrow along the track and a green acceleration arrow towards the centre](scenes/gaming/motion_plane.svg "Look at the minimap: the kart's velocity arrow points along the track, not towards the centre.")

Siddharth is coding a spell for his fantasy game: a fireball that orbits the wizard in a perfect circle, and flies off at an enemy when you press a button.

The orbit looks beautiful. The fireball whirls round at a steady speed; the debug panel shows it holding exactly the same number every frame. So Siddharth writes the release code the obvious way: when the button is pressed, launch the fireball straight **outwards**, away from the wizard, keeping its speed.

His friend Pranav tries it and frowns. "It jumps sideways when I let go. Like it forgets which way it was moving."

Pranav has a point. A moment before release, the fireball was moving one way; a frame later it is racing off in a completely different direction, as if kicked. And there's a second puzzle in the debug panel: the physics engine reports that the orbiting fireball is **accelerating**, even though its speed never changes.

Which way was the fireball really moving? And how can something with a constant speed be accelerating?

## The physics

An object moving in a circle at **constant speed** is in **uniform circular motion**. A kart going steadily round a circular track, a point on a spinning fan blade and Siddharth's fireball are all examples.

At every instant the velocity points along the **tangent** to the circle, at right angles to the radius. That is the direction the object is moving at that moment. If the circular path is suddenly removed, the object carries on in a straight line along that tangent.

![Left: a circle with six equal velocity arrows, each tangent to the circle, and a dashed tangent line at the top labelled 'let go here: it leaves along the tangent'. Right: the same six arrows drawn from one point, forming a star](figures/uniform_circular_motion/velocity-around-circle.svg "Every velocity arrow has the same length, because the speed is constant, but each points a different way. Redrawn from one point, they fan out in all directions: the velocity is always changing.")

Now the key idea. Velocity is a **vector**. In uniform circular motion its size, the speed $v$, stays the same, but its direction turns continuously. A change of direction is a change of velocity, and any change of velocity is an **acceleration**. So an object in uniform circular motion is always accelerating, even at constant speed.

For a circle of radius $r$ taken in time $T$ (the **period**),

$$v = \frac{2\pi r}{T}, \qquad \omega = \frac{2\pi}{T}, \qquad v = \omega r$$

where $\omega$ is the **angular speed** in $\text{rad/s}$.

Siddharth's bug is now clear. The fireball was moving along the tangent, not outwards. Launching it outwards meant turning its velocity by $90^\circ$ in one frame. To let it fly naturally, he should release it along the tangent.

## Worked example

**Given (illustrative):** the fireball orbits at radius $r = 2.0\,\text{m}$, once every $T = 0.80\,\text{s}$, anticlockwise. Take the centre as origin, $\hat{i}$ right and $\hat{j}$ up.
**Find:** its speed and angular speed, and its velocity at the rightmost point and a quarter turn later. How big is the change in velocity?

$$v = \frac{2\pi r}{T} = \frac{2\pi (2.0)}{0.80} \approx 15.7\,\text{m/s}, \qquad \omega = \frac{2\pi}{0.80} \approx 7.85\,\text{rad/s}$$

At the rightmost point the tangent is vertical and the motion is anticlockwise, so $\vec{v}_1 = 15.7\hat{j}\ \text{m/s}$. A quarter turn later, $0.20\,\text{s}$ on, it is at the top moving left: $\vec{v}_2 = -15.7\hat{i}\ \text{m/s}$.

$$\Delta\vec{v} = \vec{v}_2 - \vec{v}_1 = -15.7\hat{i} - 15.7\hat{j}\ \text{m/s}, \qquad |\Delta\vec{v}| = 15.7\sqrt{2} \approx 22\,\text{m/s}$$

The speed is the same at both points, yet the velocity changed by about $22\,\text{m/s}$ in $0.20\,\text{s}$. That change points down and to the left, from the middle of that quarter-arc towards the centre.

**Sanity check:** $v = \omega r = 7.85 \times 2.0 = 15.7\,\text{m/s}$, matching. If the fireball stopped turning, $\Delta\vec{v}$ would be zero, and so would the acceleration.

## Where the picture breaks

In a game, the fireball can be locked to a circle by code; nothing needs to pull it inwards. A real object only goes round a circle if a real force (string tension, friction, gravity) keeps pulling it towards the centre. You'll meet that force in the laws of motion. Real circular motion is also rarely perfectly uniform: a kart slows for traffic, a fan speeds up after being switched on. Here we assume the speed is exactly constant. The size of the acceleration, and the exact direction at each instant, is the next lesson.

## Key takeaway

In uniform circular motion the speed is constant but the velocity is not: it always points along the tangent, and its direction turns continuously. Because velocity changes, the object is accelerating, even though its speed never changes. The speed is $v = 2\pi r/T = \omega r$.
