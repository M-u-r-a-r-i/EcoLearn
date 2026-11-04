---
concept_id: escape_speed
interest: football
format: explain
title: How hard would you have to kick a ball off the planet
check:
  question: |-
    The escape speed from the Earth's surface is about $11.2\,\text{km/s}$. A planet has the same mass as the Earth but four times its radius. What is the escape speed from its surface?
  options:
    A: |-
      $2.8\,\text{km/s}$
    B: |-
      $22.4\,\text{km/s}$
    C: |-
      $5.6\,\text{km/s}$
    D: |-
      $11.2\,\text{km/s}$
  answer: C
  explanation: |-
    $v_e = \sqrt{2GM/R}$. With $M$ unchanged and $R$ four times larger, $v_e$ is divided by $\sqrt{4} = 2$: $11.2/2 = 5.6\,\text{km/s}$.
  misconceptions:
    A: |-
      Takes escape speed to be inversely proportional to $R$, forgetting the square root that comes from the kinetic energy $\tfrac{1}{2}mv^2$.
    B: |-
      Thinks a bigger planet is harder to escape whatever its mass; with the same mass spread over a larger radius, the surface is farther from the centre and escape is easier.
    D: |-
      Treats escape speed as a universal constant; it depends on the mass and radius of the body being escaped.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A night match: the goalkeeper's long kick at the top of its arc, the Moon and a satellite overhead, and a dish on the stand roof aimed at the satellite](scenes/football/gravitation.svg "However hard the goalkeeper kicks, the ball comes back down. Is there a kick that wouldn't?")

After the evening session, Rohit, the goalkeeper, is proud of his goal kicks. "Coach timed one on the app. The ball left my boot at about thirty metres a second."

Tenzin, who plays up front and watches every space documentary he can find, isn't impressed. "Still came back down, didn't it?"

"Everything comes back down."

"Not everything. Rockets leave. So there must be a speed where a ball just keeps going: slowing down forever but never turning round." Tenzin grins. "And I bet it's easier on Mars. Smaller planet."

"Would a heavier ball need a harder kick?" asks Rohit. "And does it matter if I kick it straight up or at an angle?"

Neither of them knows. Is there really such a speed? What does it depend on, and what doesn't it depend on?

## The physics

Launch a body of mass $m$ from the surface of a planet of mass $M$ and radius $R$, and ignore air. Only gravity acts, and gravity is a conservative force, so the **mechanical energy is conserved**:

$$\tfrac{1}{2}mv^2 - \frac{GMm}{r} = \text{constant}$$

As the body rises, $r$ grows, the potential energy $-GMm/r$ climbs towards zero, and the kinetic energy falls.

- If the **total energy is negative**, the kinetic energy runs out at some finite distance. The body stops and falls back.
- If the **total energy is zero or positive**, the kinetic energy never runs out. The body keeps moving away forever and never returns.

![A graph of energy against r over R: the red potential energy curve rises towards zero; a green dashed line at zero total energy never meets it, and an orange dashed line at minus a half meets it at r equals 2R](figures/escape_speed/energy-to-escape.svg "At zero total energy (green), there is always some kinetic energy left, so the body never returns. With less (orange), it stops where the line meets the curve and falls back.")

The **escape speed** $v_e$ is the smallest launch speed that makes the total energy exactly zero:

$$\tfrac{1}{2}mv_e^2 - \frac{GMm}{R} = 0 \quad\Rightarrow\quad v_e = \sqrt{\frac{2GM}{R}} = \sqrt{2gR}$$

using $GM = gR^2$. That answers Rohit's questions:

- **The mass $m$ cancels.** A light ball, a heavy medicine ball and a spacecraft all need the same escape speed.
- **The direction doesn't matter** (as long as the path doesn't hit the planet), because energy is a scalar.
- It depends only on the planet: a larger $M$ or a smaller $R$ gives a larger $v_e$.

## Worked example

**Given:** Earth: $g = 9.8\,\text{m/s}^2$, $R = 6.4 \times 10^{6}\,\text{m}$. Mars: $M = 6.4 \times 10^{23}\,\text{kg}$, $R = 3.4 \times 10^{6}\,\text{m}$. $G = 6.67 \times 10^{-11}\,\text{N m}^2/\text{kg}^2$. Rohit's kick: $30\,\text{m/s}$.
**Find:** (a) the Earth's escape speed and how many times Rohit's kick it is; (b) the escape speed from Mars.

(a)
$$v_e = \sqrt{2 \times 9.8 \times 6.4 \times 10^{6}} = \sqrt{1.25 \times 10^{8}} \approx 1.12 \times 10^{4}\,\text{m/s} = 11.2\,\text{km/s}$$

That is $11\,200/30 \approx 370$ times Rohit's kick.

(b)
$$v_e = \sqrt{\frac{2 \times 6.67 \times 10^{-11} \times 6.4 \times 10^{23}}{3.4 \times 10^{6}}} = \sqrt{2.5 \times 10^{7}} \approx 5.0 \times 10^{3}\,\text{m/s} = 5.0\,\text{km/s}$$

Tenzin is right: Mars is easier to escape, but a ball would still need about $5\,\text{km/s}$.

**Sanity check:** a $0.43\,\text{kg}$ ball at $11.2\,\text{km/s}$ has kinetic energy $\tfrac{1}{2} \times 0.43 \times (1.12 \times 10^{4})^2 \approx 2.7 \times 10^{7}\,\text{J}$. Its potential energy at the surface is $-mgR = -0.43 \times 9.8 \times 6.4 \times 10^{6} \approx -2.7 \times 10^{7}\,\text{J}$. The total is zero, as the definition requires.

## Where the picture breaks

A ball kicked at $11.2\,\text{km/s}$ from a football pitch would not escape. Air drag at that speed is enormous; the ball would be slowed and heated violently within moments. The escape speed assumes no air at all.

Rockets also don't escape like a kicked ball. A kick gives all the speed at once, at the start; a rocket keeps its engines firing as it climbs, so it never needs to reach $11.2\,\text{km/s}$ at ground level. And "escape" here means escaping the **Earth's** pull only. An object that leaves the Earth is still held by the Sun.

## Key takeaway

Escape speed is the smallest launch speed that makes the total mechanical energy zero, so the body never comes back: $v_e = \sqrt{2GM/R} = \sqrt{2gR} \approx 11.2\,\text{km/s}$ for the Earth. It doesn't depend on the mass launched or its direction, only on the mass and radius of the planet being left.
