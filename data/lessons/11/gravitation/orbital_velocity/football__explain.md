---
concept_id: orbital_velocity
interest: football
format: explain
title: The light that crossed the sky during training
check:
  question: |-
    A satellite in a circular orbit just above the Earth's surface (radius $R$) has period $T$. Another satellite moves in a circular orbit of radius $4R$. What is its period?
  options:
    A: |-
      $2T$
    B: |-
      $16T$
    C: |-
      $4T$
    D: |-
      $8T$
  answer: D
  explanation: |-
    $T = 2\pi\sqrt{r^3/GM}$, so $T \propto r^{3/2}$. Four times the radius gives $4^{3/2} = 8$ times the period.
  misconceptions:
    A: |-
      Uses $T \propto \sqrt{r}$, forgetting that a larger orbit is both longer and travelled more slowly.
    B: |-
      Takes $T \propto r^2$, applying the inverse-square law of the force to the period.
    C: |-
      Assumes the satellite moves at the same speed in every orbit, so the period just grows with the circumference; in fact higher orbits are also slower.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A night match: the goalkeeper's long kick at the top of its arc, the Moon and a satellite overhead, and a dish on the stand roof aimed at the satellite](scenes/football/gravitation.svg "The goalkeeper's kick and the satellite are both falling towards the Earth. Only one of them lands.")

It's the last drill of the evening, just after sunset. Mawia, the goalkeeper, launches a long kick towards the far half, and every head follows the ball up. Then Coach Joseph points past it.

"Look there. That steady light, moving across the sky. It's a satellite, catching the sunlight."

The players watch it glide from one side of the stadium to the other in a couple of minutes, with no sound.

"It goes right round the Earth in about an hour and a half," the coach says.

Mawia's kick has already thudded down near the halfway line. "My kick comes down in a few seconds. Why doesn't that thing fall?"

"It does," says the coach. "It's falling right now."

How can something be falling and never land? And how fast must it go to manage that?

## The physics

Newton imagined a cannon on a very high mountain firing horizontally. A faster shot lands farther away, but the Earth's surface curves away beneath it. Fire fast enough and the shot keeps falling but the ground keeps curving away just as fast: it falls all the way round. That shot is in **orbit**.

![Left: shots fired level from a tower land farther round the Earth as speed increases, and the fastest circles it. Right: a satellite in a circular orbit with gravity pointing to the centre and velocity along the orbit](figures/orbital_velocity/throw-to-orbit.svg "An orbit is a fall that never reaches the ground. In a circular orbit, gravity provides exactly the centripetal force needed.")

For a satellite of mass $m$ in a circular orbit of radius $r$ about a planet of mass $M$, with $r$ measured from the planet's **centre**, gravity is the only force and it points to the centre. It must provide the whole **centripetal force**:

$$\frac{GMm}{r^2} = \frac{mv_o^2}{r} \quad\Rightarrow\quad v_o = \sqrt{\frac{GM}{r}}$$

This is the **orbital speed**. The satellite's own mass cancels. A larger orbit needs a *smaller* speed, because gravity is weaker there.

The **period** is the circumference divided by the speed:

$$T = \frac{2\pi r}{v_o} = 2\pi\sqrt{\frac{r^3}{GM}}$$

So $T^2 \propto r^3$: Kepler's third law, now following from Newton's law of gravitation.

For an orbit skimming the surface ($r \approx R$, ignoring air), $GM = gR^2$ gives $v_o = \sqrt{gR} = \sqrt{9.8 \times 6.4 \times 10^{6}} \approx 7.9\,\text{km/s}$. That's more than $250$ times a $30\,\text{m/s}$ goal kick.

## Worked example

**Given:** a satellite at height $h = 600\,\text{km}$ (illustrative); $R = 6.4 \times 10^{6}\,\text{m}$; $GM = 4.0 \times 10^{14}\,\text{m}^3/\text{s}^2$ (from $G = 6.67 \times 10^{-11}\,\text{N m}^2/\text{kg}^2$ and $M = 6.0 \times 10^{24}\,\text{kg}$).
**Find:** its orbital speed and period.

The radius is measured from the centre: $r = R + h = 6.4 \times 10^{6} + 0.6 \times 10^{6} = 7.0 \times 10^{6}\,\text{m}$.

$$v_o = \sqrt{\frac{4.0 \times 10^{14}}{7.0 \times 10^{6}}} = \sqrt{5.71 \times 10^{7}} \approx 7.56 \times 10^{3}\,\text{m/s}$$

$$T = \frac{2\pi r}{v_o} = \frac{2\pi \times 7.0 \times 10^{6}}{7.56 \times 10^{3}} \approx 5.82 \times 10^{3}\,\text{s} \approx 97\,\text{min}$$

That matches the coach's "about an hour and a half".

**Sanity check:** the second formula gives $2\pi\sqrt{r^3/GM} = 2\pi\sqrt{3.43 \times 10^{20}/4.0 \times 10^{14}} = 2\pi \times 926 \approx 5.82 \times 10^{3}\,\text{s}$, the same. And since $r$ is a bit more than $R$, $v_o$ should be a bit less than $7.9\,\text{km/s}$. It is.

## Where the picture breaks

Mawia's kick can never become an orbit at ground level: air drag at $7.9\,\text{km/s}$ would stop the ball almost at once, and the stands are in the way. Real satellites are first carried above almost all of the atmosphere, and even there, low orbits slowly lose height to the thin air that remains.

The formula assumes a perfectly circular orbit round a uniform spherical Earth. Many real orbits are elliptical, and the speed changes around them, as Kepler's second law says. And the satellite only shines because it reflects sunlight: it is visible shortly after sunset because it is high enough to still be in sunshine while the pitch is in shadow.

## Key takeaway

A satellite in a circular orbit is in free fall, with gravity providing the centripetal force: $GMm/r^2 = mv_o^2/r$, so $v_o = \sqrt{GM/r}$ and $T = 2\pi\sqrt{r^3/GM}$. Measure $r$ from the planet's centre. Higher orbits are slower and take longer, and the satellite's own mass doesn't matter.
