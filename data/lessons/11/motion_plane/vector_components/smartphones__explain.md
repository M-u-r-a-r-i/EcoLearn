---
concept_id: vector_components
interest: smartphones
format: explain
title: How your phone knows which way is up
check:
  question: |-
    A phone is held with its screen facing you and tilted so that its long edge makes $60^\circ$ with the vertical. What are the components of $g = 9.8\,\text{m/s}^2$ along the long edge and along the short edge? ($\cos 60^\circ = 0.50$, $\sin 60^\circ \approx 0.866$)
  options:
    A: |-
      $8.5\,\text{m/s}^2$ along the long edge and $4.9\,\text{m/s}^2$ along the short edge
    B: |-
      $4.9\,\text{m/s}^2$ along the long edge and $8.5\,\text{m/s}^2$ along the short edge
    C: |-
      $4.9\,\text{m/s}^2$ along the long edge and $4.9\,\text{m/s}^2$ along the short edge
    D: |-
      $8.5\,\text{m/s}^2$ along the long edge and $1.3\,\text{m/s}^2$ along the short edge
  answer: B
  explanation: |-
    The angle is measured from the long edge, so that component uses cosine: $9.8 \times 0.50 = 4.9\,\text{m/s}^2$. The short edge gets $9.8 \times 0.866 \approx 8.5\,\text{m/s}^2$. Check: $\sqrt{4.9^2 + 8.5^2} \approx 9.8$.
  misconceptions:
    A: |-
      Swaps sine and cosine. The component along the direction the angle is measured from (here the long edge) uses $\cos\theta$.
    C: |-
      Shares the vector equally between the two directions, as if each component were simply half of it.
    D: |-
      Thinks the two components must add up, as ordinary numbers, to $9.8$. Perpendicular components combine by Pythagoras, not by plain addition.
author: claude-code/opus-5
written: 2026-09-25
---
## The story

![An evening terrace: a phone in the foreground, a drone flying at a slant and an earbud case skidding off a table](scenes/smartphones/motion_plane.svg "Every arrow in this scene can be split into a sideways part and an up-down part. Your phone does this for gravity many times a second.")

Kavya is lying on the sofa watching a cooking video, phone upright in her hand. She slowly tips the phone sideways. Nothing happens, nothing happens, and then, somewhere past halfway, the video snaps to landscape.

"How does it know?" she asks her uncle Suresh, who repairs phones in a small shop near the station. "There's no spirit level in here."

"There's something better," he says. "A tiny sensor chip that feels gravity along two directions: along the phone's long edge and along its short edge. Upright, gravity is all along the long edge. Tip it and it slowly moves over to the short edge."

Kavya frowns. Gravity is one arrow, pointing straight down. How can one arrow be *partly* along one edge and *partly* along another, and how much goes each way?

## The physics

Any vector in a plane can be replaced by two perpendicular vectors that add up to it. These are its **components**, and choosing the axes is up to you. The phone chooses its own: $x$ along the short edge and $y$ along the long edge.

If a vector $\vec{A}$ has magnitude $A$ and makes an angle $\theta$ with the $x$-axis, then its **rectangular components** are

$$A_x = A\cos\theta, \qquad A_y = A\sin\theta$$

This is right-angled triangle trigonometry: $\vec{A}$ is the hypotenuse and the components are the two sides. The side next to the angle gets $\cos\theta$; the side opposite gets $\sin\theta$.

![A vector A at angle theta to the x-axis, with its x-component A cos theta and y-component A sin theta drawn along the axes](figures/vector_components/resolving-a-vector.svg "Drop perpendiculars from the vector's head to each axis. The two components added head to tail rebuild the original vector exactly.")

You can always **reconstruct** the vector from its components:

$$A = \sqrt{A_x^2 + A_y^2}, \qquad \tan\theta = \frac{A_y}{A_x}$$

Components carry signs: a component pointing the negative way along an axis is negative.

In Kavya's phone, the vector is $\vec{g}$, $9.8\,\text{m/s}^2$ straight down. Tilt the phone by an angle $\theta$ from upright (screen still facing her), and the angle between $\vec{g}$ and the long edge is $\theta$. So the long edge gets $g\cos\theta$ and the short edge gets $g\sin\theta$. Past $45^\circ$ the short-edge part becomes the bigger one, and that is the cue to rotate the screen.

## Worked example

**Given:** Kavya's phone tilted $30^\circ$ from upright ($\cos 30^\circ \approx 0.866$, $\sin 30^\circ = 0.50$); $g = 9.8\,\text{m/s}^2$.
**Find:** the components of $\vec{g}$ along each edge, then rebuild $\vec{g}$ from them.

1. Along the long edge: $g\cos 30^\circ = 9.8 \times 0.866 \approx 8.5\,\text{m/s}^2$. Most of gravity still runs along the long edge.
2. Along the short edge: $g\sin 30^\circ = 9.8 \times 0.50 = 4.9\,\text{m/s}^2$. Exactly half of $g$ has moved over to the short edge.
3. Rebuild: $\sqrt{8.5^2 + 4.9^2} = \sqrt{72.3 + 24.0} = \sqrt{96.3} \approx 9.8\,\text{m/s}^2$, the full $g$, as it must be.

The long-edge part is bigger, so the screen stays in portrait. Tip to $60^\circ$ and the two numbers swap places, and the screen flips.

**Sanity check:** each component is smaller than $9.8$, and at $45^\circ$ both would be equal, about $6.9\,\text{m/s}^2$ each, which is the changeover point.

## Where the picture breaks

The chip doesn't sense gravity itself. Strictly, it senses the push that stops the phone falling, which is equal in size and opposite in direction; in free fall it would read zero. It also has a third axis, straight out of the screen, because a phone lying flat on a table needs one. Real phones don't flip at exactly $45^\circ$: they wait until you're well past it, so the screen doesn't flicker when you hold it near the middle. The trigonometry of components is exact; the switching rule is a design choice.

## Key takeaway

A vector at angle $\theta$ to the $x$-axis splits into perpendicular components $A_x = A\cos\theta$ and $A_y = A\sin\theta$, and rebuilds as $A = \sqrt{A_x^2 + A_y^2}$ with $\tan\theta = A_y/A_x$. The side next to the angle gets cosine. A phone's orientation sensor is a component-resolver for gravity.
