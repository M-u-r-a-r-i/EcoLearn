---
concept_id: vector_components
interest: cricket
format: explain
title: Splitting a lofted drive into forward and upward
check:
  question: |-
    A fielder's throw leaves the hand at $30\,\text{m/s}$, at $30^\circ$ above the horizontal. What are the horizontal and vertical components of its velocity? ($\sin 30^\circ = 0.50$, $\cos 30^\circ \approx 0.866$)
  options:
    A: |-
      $15\,\text{m/s}$ horizontal and $26\,\text{m/s}$ vertical
    B: |-
      $15\,\text{m/s}$ horizontal and $15\,\text{m/s}$ vertical
    C: |-
      $26\,\text{m/s}$ horizontal and $4\,\text{m/s}$ vertical
    D: |-
      $26\,\text{m/s}$ horizontal and $15\,\text{m/s}$ vertical
  answer: D
  explanation: |-
    $v_x = v\cos\theta = 30 \times 0.866 \approx 26\,\text{m/s}$ and $v_y = v\sin\theta = 30 \times 0.50 = 15\,\text{m/s}$. Check: $\sqrt{26^2 + 15^2} \approx 30\,\text{m/s}$.
  misconceptions:
    A: |-
      Swaps sine and cosine. The component next to the angle (here the horizontal one) uses $\cos\theta$.
    B: |-
      Shares the vector out equally between the two directions, as if each component were simply half of it.
    C: |-
      Thinks the two components must add up, as numbers, to the original $30\,\text{m/s}$. Perpendicular components combine by Pythagoras, not by ordinary addition.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A day match: a batter lofts the ball towards the boundary as a fielder races along the rope](scenes/cricket/motion_plane.svg "A lofted shot goes forward and upward at once. The fielder and the batter care about different parts of it.")

Ishita has been working on her lofted drive all month. At the academy, her coach, Mr Bhatt, films her with a video-analysis app. After a clean hit, the screen shows two numbers: launch speed $25\,\text{m/s}$, launch angle $40^\circ$ above the ground (her numbers, illustrative).

"Twenty-five metres per second!" she says. "That's fast."

"It is," says Mr Bhatt. "But the fielder at long-off doesn't care about twenty-five. He cares how fast the ball is coming *towards the rope*. And how long it stays up depends on something else: how fast it's going *upwards*. Those are two different numbers hiding inside your one."

Ishita looks at the screen again. There is only one arrow, one speed and one angle. How can a single velocity contain a "forward" part and an "upward" part, and how big is each?

## The physics

Any vector in a plane can be replaced by two perpendicular vectors that add up to it. These are its **components**. Choose axes: $x$ horizontal (along the ground towards long-off) and $y$ vertically up.

If a vector $\vec{A}$ has magnitude $A$ and makes an angle $\theta$ with the $x$-axis, then its **rectangular components** are

$$A_x = A\cos\theta, \qquad A_y = A\sin\theta$$

This is plain right-angled triangle trigonometry: $\vec{A}$ is the hypotenuse, and the two components are the sides. The side next to $\theta$ gets $\cos\theta$; the side opposite gets $\sin\theta$.

![A vector A at angle theta to the x-axis, with dashed lines dropping to each axis. The x-component A cos theta and the y-component A sin theta are drawn along the axes](figures/vector_components/resolving-a-vector.svg "Resolving: drop perpendiculars from the vector's head to each axis. The two components added head to tail rebuild the original vector exactly.")

Going the other way, you can **reconstruct** the vector from its components:

$$A = \sqrt{A_x^2 + A_y^2}, \qquad \tan\theta = \frac{A_y}{A_x}$$

Components can be negative. A ball hit downwards has a negative $A_y$; one heading back past the bowler would have a negative $A_x$ if $x$ points towards long-off. The sign carries the direction.

Why bother? Because perpendicular directions can be handled separately. Once a velocity is split into $v_x$ and $v_y$, each part can be treated like one-dimensional motion, which you already know how to do. For Ishita's drive, $v_x$ decides how quickly the ball reaches the rope, and $v_y$ decides how high it climbs and how long it hangs in the air.

## Worked example

**Given:** launch speed $v = 25\,\text{m/s}$ at $\theta = 40^\circ$ above the horizontal ($\cos 40^\circ \approx 0.766$, $\sin 40^\circ \approx 0.643$).
**Find:** the horizontal and vertical components, then rebuild the velocity from them.

$$v_x = v\cos\theta = 25 \times 0.766 \approx 19.2\,\text{m/s}$$
$$v_y = v\sin\theta = 25 \times 0.643 \approx 16.1\,\text{m/s}$$

So the ball leaves travelling at about $19.2\,\text{m/s}$ towards long-off and $16.1\,\text{m/s}$ upwards, both at the same time.

Rebuild:
$$v = \sqrt{19.2^2 + 16.1^2} = \sqrt{368.6 + 259.2} = \sqrt{627.8} \approx 25.1\,\text{m/s}$$
$$\tan\theta = \frac{16.1}{19.2} \approx 0.839 \quad\Rightarrow\quad \theta \approx 40^\circ$$

**Sanity check:** the rebuilt speed is $25\,\text{m/s}$ to within rounding. Each component is smaller than $25$, as it must be. The forward part is bigger than the upward part because $40^\circ$ is less than $45^\circ$.

## Where the picture breaks

The app's two numbers describe only the instant the ball leaves the bat. Straight afterwards, gravity starts reducing $v_y$ and air resistance starts reducing both parts, so the components change during the flight. A real drive also rarely goes exactly straight: it usually has a sideways part too, which needs a third axis. Resolving into two components is exact; the assumption that the motion stays in one vertical plane is the idealisation.

## Key takeaway

A vector at angle $\theta$ to the $x$-axis splits into perpendicular components $A_x = A\cos\theta$ and $A_y = A\sin\theta$. Put them back together with $A = \sqrt{A_x^2 + A_y^2}$ and $\tan\theta = A_y/A_x$. Components let you treat each direction on its own, which is how one "fast" hit becomes a forward speed and an upward speed.
