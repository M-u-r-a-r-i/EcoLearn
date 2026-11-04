---
concept_id: orbital_velocity
interest: cricket
format: explain
title: The boundary throw that never lands
check:
  question: |-
    Satellite P orbits the Earth in a circle of radius $r$. Satellite Q orbits in a circle of radius $4r$. How does Q's orbital speed compare with P's?
  options:
    A: |-
      Half of P's speed
    B: |-
      One quarter of P's speed
    C: |-
      The same as P's speed
    D: |-
      Twice P's speed
  answer: A
  explanation: |-
    $v_o = \sqrt{GM/r}$, so $v_o \propto 1/\sqrt{r}$. Four times the radius gives $1/\sqrt{4} = 1/2$ the speed.
  misconceptions:
    B: |-
      Uses the inverse-square law directly on the speed; it is the force that goes as $1/r^2$, while the speed goes as $1/\sqrt{r}$.
    C: |-
      Thinks all satellites circle at the same speed; the speed needed depends on how strong gravity is at that radius.
    D: |-
      Thinks a bigger orbit needs a faster satellite; in fact gravity is weaker farther out, so less speed is needed to stay in a circle.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A night match: a ball skied above a fielder, the Moon and a satellite overhead, and a broadcast van's dish aimed at the sky](scenes/cricket/gravitation.svg "The satellite high above the ground is falling towards the Earth, just like the ball. So why doesn't it land?")

Meera fields at deep midwicket, and her flat, fizzing throws are the pride of the team. In fielding practice she hurls one from the boundary. It barely rises, and it arrives at the keeper's gloves still travelling fast.

"If you threw it any harder," Coach Dinesh jokes, "it would go right round the world and hit you in the back."

The team laughs, but Meera thinks about it on the bus home. A faster throw does land farther away. And the Earth's surface curves away beneath a ball in flight. So if the throw were fast enough, would the ground keep curving away just as fast as the ball dropped? Would the ball keep falling and never land?

Looking out of the window, she sees a satellite dish on a rooftop. Something up there is doing exactly this. How fast would she have to throw?

## The physics

Newton himself imagined this: a cannon on a very high mountain firing horizontally, faster and faster. Each shot lands farther round the Earth, until one falls all the way round. That shot is in **orbit**.

![Left: shots fired level from a tower land farther round the Earth as speed increases, and the fastest circles it. Right: a satellite in a circular orbit with gravity pointing to the centre and velocity along the orbit](figures/orbital_velocity/throw-to-orbit.svg "An orbit is a fall that never reaches the ground. In a circular orbit, gravity is exactly the centripetal force needed.")

For a satellite of mass $m$ in a circular orbit of radius $r$ about a planet of mass $M$ ($r$ measured from the planet's **centre**), gravity is the only force, and it points to the centre. It must supply the whole **centripetal force**:

$$\frac{GMm}{r^2} = \frac{mv_o^2}{r} \quad\Rightarrow\quad v_o = \sqrt{\frac{GM}{r}}$$

This is the **orbital speed**. The satellite's mass cancels, so a tiny satellite and a huge space station in the same orbit move at the same speed. A larger orbit needs a *smaller* speed, because gravity is weaker there.

The **period** is the time for one lap, the circumference divided by the speed:

$$T = \frac{2\pi r}{v_o} = 2\pi\sqrt{\frac{r^3}{GM}}$$

So $T^2 \propto r^3$: Kepler's third law, now derived from Newton's law of gravitation.

For an orbit just above the surface ($r \approx R$, ignoring air), $GM = gR^2$ gives $v_o = \sqrt{gR} = \sqrt{9.8 \times 6.4 \times 10^{6}} \approx 7.9\,\text{km/s}$. That answers Meera's question: about $7.9\,\text{km/s}$, roughly $260$ times a fast throw of $30\,\text{m/s}$.

## Worked example

**Given:** a satellite at height $h = 400\,\text{km}$; $R = 6.4 \times 10^{6}\,\text{m}$; $GM = 4.0 \times 10^{14}\,\text{m}^3/\text{s}^2$ (from $G = 6.67 \times 10^{-11}$ and $M = 6.0 \times 10^{24}\,\text{kg}$).
**Find:** its orbital speed and period.

The radius is measured from the centre: $r = R + h = 6.4 \times 10^{6} + 0.4 \times 10^{6} = 6.8 \times 10^{6}\,\text{m}$.

$$v_o = \sqrt{\frac{4.0 \times 10^{14}}{6.8 \times 10^{6}}} = \sqrt{5.88 \times 10^{7}} \approx 7.67 \times 10^{3}\,\text{m/s}$$

$$T = \frac{2\pi r}{v_o} = \frac{2\pi \times 6.8 \times 10^{6}}{7.67 \times 10^{3}} \approx 5.57 \times 10^{3}\,\text{s} \approx 93\,\text{min}$$

**Sanity check:** the orbit is a little bigger than $R$, so $v_o$ should be a little less than $7.9\,\text{km/s}$, and it is. Second way: $2\pi\sqrt{r^3/GM} = 2\pi\sqrt{3.14 \times 10^{20}/4.0 \times 10^{14}} = 2\pi \times 886 \approx 5.57 \times 10^{3}\,\text{s}$, the same answer.

## Where the picture breaks

Meera's throw can never become an orbit at ground level. Air drag at $7.9\,\text{km/s}$ would stop the ball almost at once, and hills and buildings are in the way. Real satellites are first lifted above almost all of the atmosphere, and even then, low orbits slowly lose height to the thin air that remains. The formula also assumes a perfectly circular orbit around a uniform spherical Earth. Many real orbits are elliptical, and their speed changes around the orbit, as Kepler's second law says.

## Key takeaway

A satellite in a circular orbit is in free fall, with gravity supplying the centripetal force: $GMm/r^2 = mv_o^2/r$, so $v_o = \sqrt{GM/r}$ and $T = 2\pi\sqrt{r^3/GM}$. Always measure $r$ from the planet's centre. Higher orbits are slower and take longer; the satellite's own mass doesn't matter.
