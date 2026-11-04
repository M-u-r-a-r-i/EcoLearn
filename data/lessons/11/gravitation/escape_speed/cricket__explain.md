---
concept_id: escape_speed
interest: cricket
format: explain
title: How fast a bowler would need to bowl to leave Earth
check:
  question: |-
    The escape speed from the Earth is about $11.2\,\text{km/s}$. A planet has the same radius as the Earth but four times its mass. What is the escape speed from its surface?
  options:
    A: |-
      $44.8\,\text{km/s}$
    B: |-
      $11.2\,\text{km/s}$
    C: |-
      $22.4\,\text{km/s}$
    D: |-
      $5.6\,\text{km/s}$
  answer: C
  explanation: |-
    $v_e = \sqrt{2GM/R}$. With $R$ unchanged and $M$ four times as large, $v_e$ grows by $\sqrt{4} = 2$: $2 \times 11.2 = 22.4\,\text{km/s}$.
  misconceptions:
    A: |-
      Takes escape speed to be proportional to the planet's mass, forgetting the square root that comes from kinetic energy $\tfrac{1}{2}mv^2$.
    B: |-
      Thinks escape speed is a universal constant; it depends on the mass and radius of the body you are escaping from.
    D: |-
      Inverts the ratio, as if a more massive planet were easier to escape; a stronger pull needs a faster launch.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A night match: a ball skied above a fielder, the Moon and a satellite overhead, and a broadcast van's dish aimed at the sky](scenes/cricket/gravitation.svg "Every skier comes back down. How fast would it have to go to never come back?")

At the evening nets, Harpreet is in rhythm. The speed gun behind the bowler's arm flashes $144\,\text{km/h}$ (say), and the ball thuds into the sightscreen before the batter has moved.

Vikram, padding up for his turn, whistles. "At that speed you could bowl it into space."

"Don't be silly," says Harpreet. "Even if I bowled straight up, it would come back down."

"Everything comes back down," Vikram agrees. "The harder you throw, the higher it goes, and then it comes back. Unless..." He stops. "Is there a speed where it *doesn't* come back? Where it just keeps going, slowing down forever but never turning round?"

Harpreet laughs. "And how fast is that?"

Vikram doesn't know. Is there such a speed, and would it depend on how heavy the ball is?

## The physics

Launch a body of mass $m$ from the surface of a planet (mass $M$, radius $R$), and ignore air. Only gravity acts, and gravity is conservative, so **mechanical energy is conserved**:

$$\tfrac{1}{2}mv^2 - \frac{GMm}{r} = \text{constant}$$

As the body climbs, $r$ increases, the potential energy $-GMm/r$ rises towards zero, and the kinetic energy falls. There are two possibilities.

- If the **total energy is negative**, the kinetic energy runs out at some finite $r$. The body stops and falls back.
- If the **total energy is zero or more**, the body can reach "infinity" (in practice, very far away) with kinetic energy to spare, or just zero. It never comes back.

![A graph of energy against r over R: the red potential energy curve rises towards zero; a green dashed line at zero total energy never meets it, and an orange dashed line at minus a half meets it at r equals 2R](figures/escape_speed/energy-to-escape.svg "With total energy zero (green), the ball always has some kinetic energy left and never returns. With less (orange), it stops where the line meets the curve and falls back.")

The **escape speed** $v_e$ is the minimum launch speed from the surface that makes the total energy exactly zero:

$$\tfrac{1}{2}mv_e^2 - \frac{GMm}{R} = 0 \quad\Rightarrow\quad v_e = \sqrt{\frac{2GM}{R}} = \sqrt{2gR}$$

using $GM = gR^2$. Notice three things:

- **The mass $m$ cancels.** A cricket ball, a tennis ball and a spacecraft all need the same escape speed from the same place.
- **The direction doesn't matter**, provided the path doesn't run into the planet, because energy is a scalar.
- It depends on the planet: a larger $M$ or a smaller $R$ means a larger $v_e$.

## Worked example

**Given:** $g = 9.8\,\text{m/s}^2$ and $R = 6.4 \times 10^{6}\,\text{m}$ for the Earth; Harpreet's ball leaves the hand at $144\,\text{km/h}$.
**Find:** (a) the Earth's escape speed; (b) how many times faster than Harpreet's delivery that is.

(a) $$v_e = \sqrt{2 \times 9.8 \times 6.4 \times 10^{6}} = \sqrt{1.25 \times 10^{8}} \approx 1.12 \times 10^{4}\,\text{m/s} = 11.2\,\text{km/s}$$

(b) $144\,\text{km/h} = 144/3.6 = 40\,\text{m/s}$, so the ratio is $11\,200/40 = 280$.

**Sanity check:** the kinetic energy at escape speed is $\tfrac{1}{2} \times 0.16 \times (1.12 \times 10^{4})^2 \approx 1.0 \times 10^{7}\,\text{J}$. That exactly cancels the ball's surface potential energy, $-mgR = -0.16 \times 9.8 \times 6.4 \times 10^{6} \approx -1.0 \times 10^{7}\,\text{J}$, as it should.

**On the Moon** ($M = 7.4 \times 10^{22}\,\text{kg}$, $R = 1.74 \times 10^{6}\,\text{m}$):
$$v_e = \sqrt{\frac{2 \times 6.67 \times 10^{-11} \times 7.4 \times 10^{22}}{1.74 \times 10^{6}}} = \sqrt{5.67 \times 10^{6}} \approx 2.4\,\text{km/s}$$

That is about a fifth of the Earth's escape speed. It's one reason the Moon has kept almost no atmosphere: fast-moving gas molecules escape it far more easily.

## Where the picture breaks

A ball bowled at $11.2\,\text{km/s}$ at ground level would not escape: air drag at that speed is enormous, and the ball would be slowed and heated violently within moments. Escape speed assumes no air. Rockets also don't work like a bowled ball. They keep firing their engines as they climb, so they never need to reach $11.2\,\text{km/s}$ at the ground. And "escape" here means escaping the **Earth's** pull only: an object that leaves the Earth is still held by the Sun.

## Key takeaway

Escape speed is the smallest launch speed that makes the total mechanical energy zero, so the body never falls back: $v_e = \sqrt{2GM/R} = \sqrt{2gR} \approx 11.2\,\text{km/s}$ for the Earth. It doesn't depend on the mass being launched or on its direction, only on the planet it is leaving.
