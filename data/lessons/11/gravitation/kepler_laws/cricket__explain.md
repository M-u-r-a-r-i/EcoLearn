---
concept_id: kepler_laws
interest: cricket
format: explain
title: The ball tracker who tracked the planets
check:
  question: |-
    A comet's closest distance from the Sun is one quarter of its farthest distance. At both of these points its velocity is perpendicular to the line joining it to the Sun. How does its speed at the closest point compare with its speed at the farthest point?
  options:
    A: |-
      About $4$ times as fast
    B: |-
      About $16$ times as fast
    C: |-
      The same speed, since the orbit is a closed loop
    D: |-
      About one quarter as fast
  answer: A
  explanation: |-
    Gravity points at the Sun, so the comet's angular momentum $mvr$ is conserved: $v_\text{near} r_\text{near} = v_\text{far} r_\text{far}$. A quarter of the distance means four times the speed.
  misconceptions:
    B: |-
      Applies the inverse-square law to the speed; speed at these points scales as $1/r$, from conserving angular momentum, not as $1/r^2$.
    C: |-
      Pictures every orbit as a circle travelled at steady speed; on an ellipse the speed changes all the way round.
    D: |-
      Inverts the relation, as if a body closer to the Sun moves more slowly; it is the other way round, because $vr$ stays fixed.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A night match: a ball skied above a fielder, the Moon and a satellite overhead, and a broadcast van's dish aimed at the sky](scenes/cricket/gravitation.svg "A cricket ground at night has the whole sky above it. The same laws steer the skied ball, the Moon and the satellite.")

Rain has stopped play, and Zoya is stuck in the broadcast truck with her little brother Arjun. She is an intern on the ball-tracking team, and she has a replay up on her screen: the path of a delivery drawn as a string of dots, one dot for every equal slice of time.

"Why are the dots bunched up here and spread out there?" Arjun asks.

"Spread-out dots mean the ball was moving fast. Same time between dots, more distance covered."

Arjun looks up through the truck window at the clearing sky. "Could you track a planet like this?"

"Someone did, about four hundred years ago," Zoya says. "No cameras. Just years of careful naked-eye positions of Mars. And when he joined the dots, he found that the planets don't move in circles at a steady speed at all."

So what shape do they trace, and what decides when a planet speeds up or slows down?

## The physics

The astronomer was **Johannes Kepler**, working from observations collected by Tycho Brahe. He summed up the motion of the planets in three laws.

1. **Law of orbits:** every planet moves in an **ellipse**, with the Sun at one **focus** (not at the centre). The closest point is the **perihelion**, the farthest the **aphelion**.
2. **Law of areas:** the line from the Sun to the planet sweeps out **equal areas in equal times**. Near the Sun the line is short, so the planet must cover a longer arc to sweep the same area: it moves faster.
3. **Law of periods:** the square of the period $T$ is proportional to the cube of the **semi-major axis** $a$ (half the longest diameter of the ellipse):

$$T^2 \propto a^3$$

![An ellipse with the Sun at one focus; a short wide shaded sector at perihelion and a long thin one at aphelion have equal areas](figures/kepler_laws/equal-areas-ellipse.svg "The two shaded areas are equal, so they take equal times. The arc near the Sun is much longer, so the planet must be moving much faster there.")

**Why the law of areas is true.** The Sun's pull on a planet always points along the line to the Sun. A force along the line from the pivot point has no turning effect about that point, so the **torque** about the Sun is zero, and the planet's **angular momentum** $\vec{L} = \vec{r} \times \vec{p}$ stays constant. In a short time $\Delta t$ the line sweeps a thin triangle of area

$$\Delta A = \tfrac{1}{2}\,|\vec{r} \times \vec{v}\,\Delta t| \quad\Rightarrow\quad \frac{\Delta A}{\Delta t} = \frac{L}{2m}$$

Since $L$ and $m$ are constant, the rate of sweeping area is constant. Kepler's second law is conservation of angular momentum, seen as geometry. At perihelion and aphelion the velocity is perpendicular to $\vec{r}$, so $L = mvr$ and

$$v_\text{p}\,r_\text{p} = v_\text{a}\,r_\text{a}$$

That is exactly what Zoya's dots show: equal time between dots, but longer gaps where the planet moves fast.

## Worked example

**Given:** the semi-major axis of Earth's orbit is $1.00\,\text{AU}$ (the astronomical unit, the Earth–Sun distance) with $T = 1.00$ year; for Mars, $a = 1.52\,\text{AU}$.
**Find:** the period of Mars.

Both planets orbit the same Sun, so $T^2/a^3$ is the same for both:

$$\frac{T_\text{M}^2}{T_\text{E}^2} = \frac{a_\text{M}^3}{a_\text{E}^3} \quad\Rightarrow\quad T_\text{M} = 1.00 \times (1.52)^{3/2}\ \text{years}$$

$(1.52)^3 = 3.51$, and $\sqrt{3.51} = 1.87$, so $T_\text{M} \approx 1.87$ years.

**Sanity check:** Mars is farther out, so it should take longer than a year, and it does. Reversing: $1.87^2 = 3.50 \approx 1.52^3$.

**Law of areas, in numbers:** Earth is about $1.47 \times 10^{11}\,\text{m}$ from the Sun at perihelion (early January) and $1.52 \times 10^{11}\,\text{m}$ at aphelion. So $v_\text{p}/v_\text{a} = 1.52/1.47 \approx 1.03$: Earth moves about $3\%$ faster in January than in July.

## Where the picture breaks

Zoya's replay borrows only the *method*: equal-time dots, spaced out where the motion is fast. A bowled ball is not an orbit. The gravity on it points straight down, not towards a single centre, so its angular momentum about any fixed point is not conserved and there is no law of areas for it.

Kepler's laws are also idealisations. They treat the Sun as fixed, because it is far heavier than any planet. In reality the planets tug on each other, so orbits are very slightly disturbed. And the constant in $T^2 \propto a^3$ is the same only for bodies orbiting the **same** central body: you can't compare a moon of Jupiter with Mars this way.

## Key takeaway

Planets move in ellipses with the Sun at a focus; the Sun–planet line sweeps equal areas in equal times; and $T^2 \propto a^3$. The law of areas is conservation of angular momentum: gravity points at the Sun, so it exerts no torque about it, $vr$ stays the same at perihelion and aphelion, and a planet speeds up as it comes closer.
