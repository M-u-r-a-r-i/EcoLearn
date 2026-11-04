---
concept_id: vector_components
interest: football
format: explain
title: How much of a diagonal pass is going up the pitch
check:
  question: |-
    A goalkeeper kicks the ball at $25\,\text{m/s}$, at $37^\circ$ above the horizontal. What are the horizontal and vertical components of its velocity as it leaves the boot? ($\sin 37^\circ \approx 0.60$, $\cos 37^\circ \approx 0.80$)
  options:
    A: |-
      $20\,\text{m/s}$ horizontal and $15\,\text{m/s}$ vertical
    B: |-
      $15\,\text{m/s}$ horizontal and $20\,\text{m/s}$ vertical
    C: |-
      $12.5\,\text{m/s}$ horizontal and $12.5\,\text{m/s}$ vertical
    D: |-
      $20\,\text{m/s}$ horizontal and $5\,\text{m/s}$ vertical
  answer: A
  explanation: |-
    $v_x = v\cos\theta = 25 \times 0.80 = 20\,\text{m/s}$ and $v_y = v\sin\theta = 25 \times 0.60 = 15\,\text{m/s}$. Check: $\sqrt{20^2 + 15^2} = 25\,\text{m/s}$.
  misconceptions:
    B: |-
      Swaps sine and cosine. The component along the side next to the angle (here the horizontal) uses $\cos\theta$.
    C: |-
      Shares the vector out equally between the two directions, as if each component were half of it, whatever the angle.
    D: |-
      Thinks the two components must add up, as plain numbers, to $25\,\text{m/s}$. Perpendicular components combine by Pythagoras, not by ordinary addition.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A player lofts the ball in an arc over the goalkeeper while a teammate jogs round the centre circle](scenes/football/motion_plane.svg "A pass or a kick has one speed, but it moves in more than one direction at once.")

Imran is the midfielder who plays the long diagonal passes. In training he pings one along the ground from the left of midfield towards Meenakshi, who is sprinting up the right touchline. The analyst's tracking app shows one arrow for the pass: $22\,\text{m/s}$, at $25^\circ$ to the touchline (illustrative).

"Twenty-two metres per second," says Imran. "Meenakshi only runs about eight. She'll never keep up with that."

Coach Pillai laughs. "She doesn't have to keep up with twenty-two. She's running *up* the pitch. What she needs to know is how fast the ball is going up the pitch. And the defender trying to cut it out cares about something else: how fast it's crossing the pitch towards him."

Imran looks at the screen. There is only one arrow. How can one velocity have an "up the pitch" part and an "across the pitch" part, and how big is each?

## The physics

Any vector in a plane can be replaced by two perpendicular vectors that add up to it. These are its **components**. Choose axes: for Imran's pass, seen from above, take $x$ along the touchline (up the pitch) and $y$ across the pitch.

If a vector $\vec{A}$ has magnitude $A$ and makes an angle $\theta$ with the $x$-axis, its **rectangular components** are

$$A_x = A\cos\theta, \qquad A_y = A\sin\theta$$

This is right-angled triangle trigonometry: $\vec{A}$ is the hypotenuse, and the components are the other two sides. The side next to $\theta$ gets $\cos\theta$; the side opposite gets $\sin\theta$.

![A vector A at angle theta to the x-axis, with dashed lines dropping to each axis. The x-component A cos theta and the y-component A sin theta are drawn along the axes](figures/vector_components/resolving-a-vector.svg "Resolving: drop perpendiculars from the vector's head to each axis. The two components, added head to tail, rebuild the original vector exactly.")

Going the other way, you can **reconstruct** the vector from its components:

$$A = \sqrt{A_x^2 + A_y^2}, \qquad \tan\theta = \frac{A_y}{A_x}$$

Components can be negative: a pass played back towards your own goal has a negative $A_x$. The sign carries the direction.

Why split a vector at all? Because perpendicular directions can be handled separately. Once the pass is split into $v_x$ and $v_y$, each part behaves like one-dimensional motion. The $x$-part is the ball's race with Meenakshi up the line; the $y$-part is how quickly it crosses the pitch.

## Worked example

**Given:** $v = 22\,\text{m/s}$ at $\theta = 25^\circ$ to the touchline ($\cos 25^\circ \approx 0.906$, $\sin 25^\circ \approx 0.423$).
**Find:** the components along and across the pitch, then rebuild the velocity from them.

$$v_x = v\cos\theta = 22 \times 0.906 \approx 19.9\,\text{m/s} \quad (\text{up the pitch})$$
$$v_y = v\sin\theta = 22 \times 0.423 \approx 9.3\,\text{m/s} \quad (\text{across the pitch})$$

So the ball moves up the pitch at about $19.9\,\text{m/s}$ and across it at $9.3\,\text{m/s}$, both at once. Meenakshi, at $8\,\text{m/s}$, can't race it; she has to be ahead of it and let it arrive.

Rebuild:
$$v = \sqrt{19.9^2 + 9.3^2} = \sqrt{396.0 + 86.5} = \sqrt{482.5} \approx 22.0\,\text{m/s}$$
$$\tan\theta = \frac{9.3}{19.9} \approx 0.467 \quad\Rightarrow\quad \theta \approx 25^\circ$$

**Sanity check:** the rebuilt speed matches $22\,\text{m/s}$. Each component is smaller than $22$, as it must be, and the along-the-line part is the bigger one because $25^\circ$ is less than $45^\circ$.

## Where the picture breaks

The app's arrow describes the ball at one instant. A rolling ball slows down as the grass drags on it, so both components shrink during the pass, and a ball struck with spin may curve, which changes the angle too. A lofted pass would also need a third, vertical component. Resolving a vector into components is exact at every instant; what changes is the vector itself.

## Key takeaway

A vector at angle $\theta$ to the $x$-axis splits into perpendicular components $A_x = A\cos\theta$ and $A_y = A\sin\theta$. Rebuild it with $A = \sqrt{A_x^2 + A_y^2}$ and $\tan\theta = A_y/A_x$. Components let you treat each direction on its own, which is how one fast pass becomes an "up the pitch" speed and an "across the pitch" speed.
