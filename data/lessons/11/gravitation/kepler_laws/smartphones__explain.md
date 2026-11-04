---
concept_id: kepler_laws
interest: smartphones
format: explain
title: The sky app that steps faster in January
check:
  question: |-
    A sky-map app shows a distant planet whose orbit has a semi-major axis of $9\,\text{AU}$. Earth's orbit has a semi-major axis of $1\,\text{AU}$ and a period of $1$ year. What is the planet's period?
  options:
    A: |-
      $9$ years
    B: |-
      $27$ years
    C: |-
      $81$ years
    D: |-
      $729$ years
  answer: B
  explanation: |-
    By Kepler's third law $T^2 \propto a^3$, so $T = 1 \times 9^{3/2}$ years $= (\sqrt{9})^3 = 3^3 = 27$ years.
  misconceptions:
    A: |-
      Assumes the period grows in simple proportion to the orbit's size ($T \propto a$); the law is $T^2 \propto a^3$, so the period grows faster than the distance.
    C: |-
      Uses $T \propto a^2$, squaring the distance instead of raising it to the power three-halves.
    D: |-
      Writes $T \propto a^3$, forgetting that it is $T^2$, not $T$, that is proportional to $a^3$; the square root was never taken.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A city rooftop at night: a fixed satellite dish, moving navigation satellites, a weather balloon rising with a phone, and a phone and tablet on a table showing a sky plot and a weather image](scenes/smartphones/gravitation.svg "Everything in this sky, from the Moon to the satellites your phone listens to, follows the same few rules of motion.")

Tanvi's new sky-map app has a time slider. Drag it, and the stars, planets and Sun wheel across the screen in fast-forward. For a school project she sets it to jump exactly one day per tap and records where the Sun sits against the background stars.

Tap, tap, tap through July. She marks the Sun's position after each step.

Then, out of curiosity, she tries January. The same one-day tap, and the Sun seems to hop slightly farther along the stars each time.

"Your app's buggy," says her cousin Aarav, reading over her shoulder. "A day is a day. The Earth goes round at the same speed all year."

Tanvi checks the settings. No bug, no setting to change. The app is simply calculating where the Earth really is on each date. So is the Earth moving faster in January? And if so, what makes it speed up?

## The physics

The app is running the rules first found by **Johannes Kepler**, from years of careful observations of Mars. His three laws describe how every planet moves.

1. **Law of orbits:** each planet moves in an **ellipse**, with the Sun at one **focus**, not at the centre. The closest point is the **perihelion**; the farthest is the **aphelion**.
2. **Law of areas:** the line from the Sun to the planet sweeps out **equal areas in equal times**.
3. **Law of periods:** the square of the orbital period $T$ is proportional to the cube of the **semi-major axis** $a$ (half the longest diameter of the ellipse):

$$T^2 \propto a^3$$

![An ellipse with the Sun at one focus; a short wide shaded sector at perihelion and a long thin one at aphelion have equal areas](figures/kepler_laws/equal-areas-ellipse.svg "Both shaded areas are swept in the same time. Near the Sun the line is short, so the planet must cover a longer arc: it moves faster.")

**Why the law of areas holds.** The Sun's pull always points along the line to the Sun, so it has no turning effect about the Sun: the **torque** about the Sun is zero. With no torque, the planet's **angular momentum** $\vec{L} = \vec{r} \times \vec{p}$ stays constant. In a short time $\Delta t$ the Sun–planet line sweeps a thin triangle, and

$$\frac{\Delta A}{\Delta t} = \frac{L}{2m}$$

which is constant because $L$ and $m$ are. At perihelion and aphelion the velocity is perpendicular to the line, so $L = mvr$ and

$$v_\text{p}\,r_\text{p} = v_\text{a}\,r_\text{a}$$

The Earth reaches perihelion in early January. It is a little closer to the Sun then, so it moves a little faster, and each day's tap in Tanvi's app carries it farther round. That is the "bug" she saw.

## Worked example

**Given:** Earth's orbit has $a = 1\,\text{AU}$ (the astronomical unit, the average Earth–Sun distance) and $T = 1$ year. A planet in the app has $a = 4\,\text{AU}$.
**Find:** its period.

**Step 1 — compare with Earth.** Both orbit the same Sun, so $T^2/a^3$ is the same for both:

$$T^2 = 1^2 \times \left(\frac{4}{1}\right)^3 = 64$$

**Step 2 — take the square root.** $T = \sqrt{64} = 8$ years.

So a planet four times as far out takes eight years for one lap: by the time it goes round once, a Class 11 student would be out of college.

**Law of areas, in one line:** a comet whose farthest distance is five times its closest distance moves five times as fast at its closest point, because $vr$ is the same at both.

**Sanity check:** a farther planet has a bigger orbit and a weaker pull, so it should take longer than a year, and $8$ years is longer.

## Where the picture breaks

The phone is only the window here. The physics is the Earth's orbit; the app just computes it from Kepler's and Newton's laws, so it cannot be "evidence" for them on its own. Real astronomers checked these laws against the sky itself.

The Sun's day-to-day hop in the app also mixes in some geometry beyond the speed change, and Earth's orbit is so nearly circular that the effect is small: only a few per cent between January and July. Kepler's laws are idealisations too. They treat the Sun as fixed and ignore the planets' pulls on one another. And the constant in $T^2 \propto a^3$ is shared only by bodies orbiting the **same** central body: you cannot compare a satellite of the Earth with Mars this way.

## Key takeaway

Planets move in ellipses with the Sun at a focus, sweep equal areas in equal times, and obey $T^2 \propto a^3$. The law of areas is conservation of angular momentum: gravity points at the Sun and exerts no torque about it, so $vr$ stays fixed and a planet speeds up as it comes closer.
