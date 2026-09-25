---
concept_id: free_body_diagrams
interest: smartphones
format: explain
title: Which part of the phone stand takes the load
check:
  question: |-
    A $2.0\,\text{kg}$ ring light for video calls hangs at rest from two cords. Each cord makes an angle of $60^\circ$ with the vertical, one on each side. Taking $g = 9.8\,\text{m/s}^2$, what is the tension in each cord?
  options:
    A: |-
      $9.8\,\text{N}$
    B: |-
      $19.6\,\text{N}$
    C: |-
      $11.3\,\text{N}$
    D: |-
      $39.2\,\text{N}$
  answer: B
  explanation: |-
    Only the vertical components of the tensions hold up the weight: $2T\cos 60^\circ = mg$, so $T = \dfrac{19.6}{2 \times 0.5} = 19.6\,\text{N}$. The horizontal components cancel each other.
  misconceptions:
    A: |-
      Shares the weight equally between the cords and ignores the angle. A slanted cord supports only its vertical component, $T\cos 60^\circ$, so it must pull harder than half the weight.
    C: |-
      Resolves with the wrong trigonometric function, $2T\sin 60^\circ = mg$. The angle is measured from the vertical, so the vertical component is $T\cos 60^\circ$.
    D: |-
      Resolves correctly but lets one cord carry the whole weight, $T\cos 60^\circ = mg$. There are two cords, and their vertical components add.
author: claude-code/opus-5
written: 2026-09-25
---
## The story

![A study room at night: a camera drone hovers pushing air down, a phone tumbles off a shelf towards the tiles, and a power bank dangles off a desk by its cable](scenes/smartphones/laws_of_motion.svg "Even a gadget sitting perfectly still has several forces on it. Equilibrium means they add to zero.")

Pooja watches her online classes on a cheap plastic phone stand: a slanted back for the phone to lean on and a small lip along the bottom edge. On Monday, halfway through a chemistry lecture, the lip snaps off and the phone slithers down onto the desk.

She shows the broken stand to her friend Rahul. He isn't surprised.

"The back does all the work," he says. "The phone leans on it, so the back carries the phone. The lip's just a little ledge to stop it sliding — it hardly holds anything."

"Then why did the lip break and not the back?"

Rahul shrugs. "Cheap plastic."

Pooja isn't convinced. The back of the stand is steep, not far off vertical. She props the broken stand at the same angle and holds the phone on it with one fingertip at the bottom edge, where the lip used to be. It takes a surprisingly firm push. So how is the phone's weight actually shared between the back and the lip?

## The physics

A **free-body diagram** shows **one body**, drawn as a dot or simple outline, with **every force acting on it** as an arrow from that body, and nothing else — no forces the body exerts on other things, and no velocity arrows.

To draw one:

1. Isolate the body you care about.
2. Add its weight, $mg$, straight down.
3. Add one force for each thing that touches it: a **normal force** perpendicular to each surface, a **tension** along each string, friction along a surface.
4. Choose axes, often along and perpendicular to a slope, and resolve every force into components.

When the body is at rest (or moving at constant velocity), it is in **equilibrium**, so the forces must add to zero. For forces meeting at one point — **concurrent** forces — that means

$$\sum F_x = 0 \qquad \sum F_y = 0$$

![Left: a body resting on a smooth slope at angle theta, held by a small stop at the lower end. Right: its free-body diagram with the normal force perpendicular to the slope, the weight straight down, the stop's push up the slope, and the weight's two dashed components](figures/free_body_diagrams/body-on-incline-against-stop.svg "Pooja's stand exactly: the back gives the normal force N, the lip gives the push S up the slope. The weight splits into mg cos θ into the back and mg sin θ down the slope, and a steeper back means more for the lip.")

For the phone on the stand, the back pushes perpendicular to its surface, $N$, and the lip pushes up along the slope, $S$. Take axes along and perpendicular to the back:

$$\text{perpendicular: } N = mg\cos\theta \qquad \text{along: } S = mg\sin\theta$$

A steep back has a large $\theta$, so $\sin\theta$ is big and $\cos\theta$ small: the lip does most of the work.

## Worked example

**Given:** the phone weighs about $2.0\,\text{N}$ (a $0.20\,\text{kg}$ phone); the back of the stand is at $\theta = 60^\circ$ to the horizontal and is treated as smooth (illustrative).
**Find:** the force from the back, $N$, and from the lip, $S$.

1. *Perpendicular to the back.*
$$N = mg\cos 60^\circ = 2.0 \times 0.50 = 1.0\,\text{N}$$
The back carries only half the phone's weight.

2. *Along the back.*
$$S = mg\sin 60^\circ = 2.0 \times 0.87 \approx 1.7\,\text{N}$$
The little lip carries the bigger share — almost the whole weight.

**Sanity check:** the two forces are at right angles, so together they should rebuild the weight: $\sqrt{1.0^2 + 1.7^2} \approx 2.0\,\text{N}$, and it does.

## Where the picture breaks

A real stand is not smooth: friction between the phone and the back takes some of the load off the lip, which is why a rubber-coated stand can hold a phone with a worn lip. We also treated the phone as a single point where all forces meet. A real phone is an extended body, and whether it tips forward depends on *where* each force acts — that needs torques, which you'll meet in Rotational Motion. Finally, a finger tapping the screen adds a force of its own, which is often what finishes off a weak lip.

## Key takeaway

A free-body diagram isolates one body and shows every force on it, and nothing else. If the body is in equilibrium, resolve along two perpendicular axes and set each sum to zero. On a steep phone stand, $S = mg\sin\theta$ is larger than $N = mg\cos\theta$, so the small lip, not the back, carries most of the weight.
