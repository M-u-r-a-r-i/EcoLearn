---
concept_id: relative_velocity_2d
interest: gaming
format: explain
title: The enemy ship that drifted backwards on radar
check:
  question: |-
    In an open-world game, a drone flies due north at $12\,\text{m/s}$ while the player's car drives due east at $5\,\text{m/s}$. What is the drone's velocity relative to the car?
  options:
    A: |-
      $17\,\text{m/s}$, towards the north-east
    B: |-
      $13\,\text{m/s}$, north of west
    C: |-
      $7\,\text{m/s}$, due north
    D: |-
      $13\,\text{m/s}$, north of east
  answer: B
  explanation: |-
    $\vec{v}_{DC} = \vec{v}_D - \vec{v}_C = 12\hat{j} - 5\hat{i}$, taking $\hat{i}$ east and $\hat{j}$ north. Its size is $\sqrt{5^2 + 12^2} = 13\,\text{m/s}$, and the $-5\hat{i}$ part points west, so it is north of west (about $67^\circ$ from west).
  misconceptions:
    A: |-
      Adds the speeds as if they were numbers in a line. Relative velocity subtracts vectors, and perpendicular velocities never combine to their plain sum.
    C: |-
      Subtracts the speeds as if both motions were along one line. The motions are perpendicular, so they must be combined by the triangle law.
    D: |-
      Adds the velocity vectors instead of subtracting. $\vec{v}_D + \vec{v}_C$ has the right size but the wrong direction; seen from the eastbound car, the drone drifts west.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A gaming desk at night: the monitor shows an artillery game with a shell flying along a curved arc; a tablet shows a top-down minimap of a circular kart track](scenes/gaming/motion_plane.svg "A minimap or radar is usually centred on you, so everything on it is drawn relative to your own motion.")

Ishita is playing a naval strategy game, steering her ship due east. On the open sea she spots an enemy ship heading due north, straight across her course. She knows it is going north: she clicked on it, and its info panel says so.

Then she glances at her radar, which is always centred on her own ship. The enemy blip isn't moving north at all. It slides diagonally, up *and* backwards, towards the left edge of the screen, and faster than the enemy's listed speed.

"The radar's broken," says her brother Aman. "It's supposed to be going straight up."

Ishita isn't convinced. The radar has never lied to her before. And if it isn't broken, the enemy must look different from her deck than from the sky above.

Why does a ship sailing north appear to drift backwards on a radar that moves with her?

## The physics

The **velocity of A relative to B** is the velocity A appears to have to an observer moving with B:

$$\vec{v}_{AB} = \vec{v}_A - \vec{v}_B$$

Both velocities on the right are measured in the same frame, here the sea. In one dimension this is simple subtraction of signed numbers. In a plane the velocities point in different directions, so the subtraction is **vector** subtraction: add $-\vec{v}_B$ to $\vec{v}_A$ by the triangle law, or subtract the components separately.

$$\vec{v}_{AB} = (v_{Ax} - v_{Bx})\hat{i} + (v_{Ay} - v_{By})\hat{j}$$

Note that $\vec{v}_{BA} = -\vec{v}_{AB}$: each sees the other moving at the same speed, in opposite directions.

![Left: A moves straight down and observer B moves right. Right: v_A drawn down, then minus v_B drawn to the left, giving v_AB slanting down and backwards](figures/relative_velocity_2d/subtracting-velocities.svg "To find how A looks to B, add minus v_B to v_A. The result slants back towards B and is faster than either motion alone.")

Ishita's radar is a picture of **relative** motion, because it moves with her ship. Her own eastward velocity, reversed, gets added to everything she sees. So the northbound enemy picks up a westward part: up and backwards on the screen, exactly as she saw.

## Worked example

**Given (illustrative):** Ishita's ship moves east at $8.0\,\text{m/s}$; the enemy moves north at $6.0\,\text{m/s}$. Take $\hat{i}$ east and $\hat{j}$ north.
**Find:** the enemy's velocity relative to Ishita, and how far its blip moves across the radar in $20\,\text{s}$.

Write both velocities in unit-vector form, relative to the sea:
$$\vec{v}_E = 6.0\hat{j}\ \text{m/s}, \qquad \vec{v}_I = 8.0\hat{i}\ \text{m/s}$$

Subtract:
$$\vec{v}_{EI} = \vec{v}_E - \vec{v}_I = -8.0\hat{i} + 6.0\hat{j}\ \text{m/s}$$

Size and direction:
$$v_{EI} = \sqrt{8.0^2 + 6.0^2} = 10\,\text{m/s}, \qquad \tan\alpha = \frac{6.0}{8.0} \Rightarrow \alpha \approx 37^\circ \text{ north of west}$$

In $20\,\text{s}$ the blip moves $20\,\vec{v}_{EI} = -160\hat{i} + 120\hat{j}\ \text{m}$, a distance of $200\,\text{m}$ on the radar.

**Sanity check:** the relative speed, $10\,\text{m/s}$, is bigger than either ship's own speed, as expected for motions at right angles. From the enemy's deck, Ishita would appear to move at $10\,\text{m/s}$ in the opposite direction, $37^\circ$ south of east.

## Where the picture breaks

Real ships also ride currents and wind, so "velocity relative to the sea" and "relative to the sea floor" can differ; the game usually ignores that. Some game radars rotate so that your heading is always "up", which turns every blip's direction on screen as well. Here the radar keeps north up and only moves with the ship. And we assumed both ships hold steady velocities. The moment either one turns, the relative velocity changes too, and the blip's path on radar curves.

## Key takeaway

The velocity of A relative to B is $\vec{v}_{AB} = \vec{v}_A - \vec{v}_B$, a vector subtraction: reverse B's velocity and add it to A's, or subtract the components. That is why a ship sailing north drifts up and backwards on the radar of a ship sailing east.
