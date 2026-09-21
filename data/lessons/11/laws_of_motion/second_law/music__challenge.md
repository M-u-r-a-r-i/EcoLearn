---
concept_id: second_law
interest: music
format: challenge
title: The roadie's race between an amp and a flight case
check:
  question: |-
    A roadie gives a $20\,\text{kg}$ amplifier and a $10\,\text{kg}$ amplifier the same net force, starting both from rest on smooth wheels. After the same time, the $10\,\text{kg}$ amplifier's speed is:
  options:
    A: |-
      The same as the $20\,\text{kg}$ amplifier's, because the force is the same
    B: |-
      Half the $20\,\text{kg}$ amplifier's, because lighter things carry less momentum
    C: |-
      Four times the $20\,\text{kg}$ amplifier's
    D: |-
      Twice the $20\,\text{kg}$ amplifier's
  answer: D
  explanation: |-
    Same net force, half the mass, so twice the acceleration ($a = F/m$). Starting from rest for the same time, $v = at$, so the speed is also twice as large.
  misconceptions:
    A: |-
      Thinks equal forces produce equal speeds, ignoring mass.
    B: |-
      Reverses the effect of mass — a smaller mass accelerates more, not less, under the same force.
    C: |-
      Squares the mass ratio; acceleration and speed are simply inversely proportional to mass here.
author: claude-code/opus-5
written: 2026-09-21
---
## The story

![A concert stage with a roadie pushing a wheeled flight case towards the exit](scenes/music/laws_of_motion.svg "Pack-up time: the same push, two very different cases.")

It's 1 a.m., the concert is over, and Irfan the roadie has one job left: roll everything to the truck before the venue locks up. He's tired, so he's decided to push every case with exactly the same effort — no more, no less.

The first thing he pushes is the huge speaker cabinet. It creeps forward. Then he gives the empty flight case the very same push, and it shoots off across the stage so fast he has to jog after it.

"Same push," he mutters. "Why is one crawling and the other one running away from me?" His friend Nisha, the drummer, bets him a samosa that she can predict exactly how much faster the light case will be going. Can you?

## The challenge

After a concert, a roadie pushes two wheeled cases across a smooth stage floor towards the loading bay:

- a speaker cabinet of mass $60\,\text{kg}$;
- an empty flight case of mass $15\,\text{kg}$.

Each gets the same steady net force of $30\,\text{N}$, starting from rest, for $2.0\,\text{s}$. Assume the wheels roll so smoothly that friction can be ignored.

At the end of the two seconds, how fast is each case moving — and how many times faster is the flight case?

## Think first

The force is the same for both. Does that mean they end up equally fast? Or is the lighter case faster — twice as fast? Four times? Sixteen? Make a prediction before you read on.

## The reveal

Newton's second law gives each case's acceleration:

$$a = \frac{F_\text{net}}{m}$$

$$a_\text{cabinet} = \frac{30}{60} = 0.50\,\text{m/s}^2, \qquad a_\text{case} = \frac{30}{15} = 2.0\,\text{m/s}^2$$

Both start from rest and accelerate uniformly for $2.0\,\text{s}$, so $v = at$:

$$v_\text{cabinet} = 0.50 \times 2.0 = 1.0\,\text{m/s}, \qquad v_\text{case} = 2.0 \times 2.0 = 4.0\,\text{m/s}$$

The flight case is **four times** faster — because it has a quarter of the mass. Equal forces do not give equal speeds, and the effect of mass is a simple inverse proportion: four times less mass, four times more acceleration, four times the speed after the same time. Not sixteen times — nothing here is squared.

## The physics

Newton's second law says the net force on a body equals its rate of change of momentum, $\vec{F}_\text{net} = d\vec{p}/dt$. For constant mass:

$$\vec{F}_\text{net} = m\vec{a}$$

![Two graphs: at fixed mass, acceleration rises in a straight line with force; at fixed force, acceleration falls along a curve as mass increases](figures/second_law/force-mass-acceleration.svg "Irfan's cases sit on the right-hand curve: same force, and a quarter of the mass means four times the acceleration.")

Acceleration is in the direction of the net force, proportional to it, and inversely proportional to the mass. The word **net** matters: it's the vector sum of *all* the forces. We could ignore friction here only because the wheels were assumed very smooth.

## Worked example

On a real stage, the roadie actually pushes the cabinet with $40\,\text{N}$, and rolling friction opposes it with $10\,\text{N}$. Find the cabinet's acceleration.

Take the direction of the push as positive. The net force is the vector sum:

$$F_\text{net} = 40 - 10 = 30\,\text{N}$$

$$a = \frac{F_\text{net}}{m} = \frac{30}{60} = 0.50\,\text{m/s}^2$$

The roadie has to push harder than $30\,\text{N}$ to get the same acceleration as on a frictionless floor — the second law uses the net force, not the applied force alone.

## Key takeaway

For the same net force, acceleration is inversely proportional to mass: $a = F_\text{net}/m$. A quarter of the mass means four times the acceleration — and, starting from rest for the same time, four times the speed.
