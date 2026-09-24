---
concept_id: escape_speed
interest: motorsport
format: explain
title: The speed no wheel will ever reach
check:
  question: |-
    A planet has the same radius as the Earth but **four times** its mass. Earth's escape speed is $11.2\,\text{km/s}$. What is the escape speed from this planet?
  options:
    A: |-
      $11.2\,\text{km/s}$
    B: |-
      $22.4\,\text{km/s}$
    C: |-
      $44.8\,\text{km/s}$
    D: |-
      $5.6\,\text{km/s}$
  answer: B
  explanation: |-
    $v_e = \sqrt{2GM/R}$, so with $R$ fixed, $v_e \propto \sqrt{M}$. Four times the mass gives $\sqrt{4} = 2$ times the escape speed.
  misconceptions:
    A: |-
      Remembers that escape speed does not depend on mass — but that is the mass of the *escaping body*, which cancels. The **planet's** mass is what sets the number.
    C: |-
      Multiplies the escape speed by $4$ along with the mass. The mass sits under a square root, so four times the mass gives only twice the speed.
    D: |-
      Divides instead of multiplying, as if a heavier planet were easier to leave. More mass means a deeper well and a higher escape speed.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A pit lane at a hill-climb event: a car on a weighbridge, a team truck with a satellite dish on its roof, a GPS aerial on the car's engine cover and a drop-test rig beside the scrutineering bay](scenes/motorsport/gravitation.svg "Everything in this pit lane is firmly attached to the Earth. This lesson is about the speed at which it would stop being.")

Once a year the club takes cars out to a dry lake bed for a mile of flat-out running, and this year Bhaskar's uncle has brought a car that goes past $300\,\text{km/h}$ on the measured mile.

The driver climbs out afterwards looking slightly stunned. "It goes light at the top end," she says. "Like it's deciding whether to stay."

Bhaskar is delighted. "So there's a speed where it doesn't stay. Get fast enough and the Earth just lets go of you."

Aparna, who has been marshalling all morning and is not in the mood, says: "There is such a speed. You are nowhere near it, and I don't think you realise by how much."

"Twice this? Five times?"

Aparna shakes her head. The number exists, and it is the same for a car, a cricket ball or a spacecraft. So what is it, and what decides it?

## The physics

**Escape speed** is the smallest speed you must give a body at a planet's surface so that, with no further push, it never comes back.

Use conservation of mechanical energy, with potential energy $U = -GMm/r$ and its zero at infinity. "Just barely escapes" means arriving infinitely far away with nothing left over — speed zero there, so total energy zero. Since the total is the same at both ends,

$$\frac{1}{2}mv_e^2 - \frac{GMm}{R} = 0 \quad\Rightarrow\quad v_e = \sqrt{\frac{2GM}{R}} = \sqrt{2gR}$$

using $GM = gR^2$. Read off three things:

- **The escaping body's mass cancels**, so the escape speed is the same for a wheel nut and for a rocket. The energy needed is not the same — that scales with $m$ — but the speed is.
- Anything with total energy **below zero is bound**: it climbs, slows, stops and falls back. Zero or more, and it is gone.
- Escape speed depends only on the **planet**: its mass and its radius.

![A graph of energy against distance from Earth's centre: the potential energy curve, a zero-total-energy line for a body launched at escape speed, and a negative-total-energy line for a slower launch that turns back at twice the Earth's radius](figures/escape_speed/energy-to-escape.svg "A launch with total energy below zero runs out of kinetic energy at the height where the curve meets its line, and falls back. Only a total energy of zero or more escapes.")

NCERT calls it escape *speed* rather than escape velocity for a good reason: without air, the direction of launch makes no difference at all. Energy conservation knows nothing about direction.

## Worked example

**Given:** $g = 9.8\,\text{m/s}^2$ and $R = 6.4 \times 10^{6}\,\text{m}$ for the Earth.
**Find:** the escape speed, and how Bhaskar's $300\,\text{km/h}$ compares.

**Step 1 — the speed squared.**

$$v_e^2 = 2gR = 2 \times 9.8 \times 6.4 \times 10^{6} = 1.25 \times 10^{8}\,\text{m}^2/\text{s}^2$$

**Step 2 — the speed.** $v_e = \sqrt{1.25 \times 10^{8}} \approx 1.12 \times 10^{4}\,\text{m/s} = 11.2\,\text{km/s}$.

**Step 3 — in car units.** Multiplying by $3.6$ gives about $40\,000\,\text{km/h}$. The lake-bed car, at $300\,\text{km/h}$, is short by a factor of about $134$ — and since kinetic energy goes as $v^2$, it is short on **energy** by a factor of about $18\,000$.

**Sanity check:** $11.2\,\text{km/s}$ would cross a ten-kilometre city in under a second. Aparna was right: this is not a few times faster than a fast car, it is another world entirely.

## Where the picture breaks

Say it plainly: motorsport is the setting here, not the analogy. No car escapes anything. There is no racing story inside escape speed, and the honest use of the pit lane is as a ruler — a thing whose speed you know, held up against a number from a different scale.

The derivation is also idealised. It assumes **no air**: a real body leaving the surface at $11.2\,\text{km/s}$ would be destroyed by the atmosphere, which is why rockets accelerate gradually while climbing out of the thick air instead of being fired like a bullet. It ignores the Earth's rotation, which gives a small free head start to an eastward launch from near the equator. It ignores the Sun and the Moon: escaping the Earth still leaves you orbiting the Sun. And the "goes light at the top end" the driver felt is aerodynamic lift on the bodywork, not gravity weakening — the car's weight is unchanged at any speed.

## Key takeaway

Escape speed is the launch speed that makes the total mechanical energy exactly zero: $v_e = \sqrt{2GM/R} = \sqrt{2gR}$, about $11.2\,\text{km/s}$ for the Earth. It does not depend on the escaping body's mass or on the launch direction, only on the planet's mass and radius. Below it, the body is bound and must come back down.
