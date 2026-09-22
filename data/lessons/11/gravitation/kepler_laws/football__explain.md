---
concept_id: kepler_laws
interest: football
format: explain
title: The league whose two halves wouldn't come out equal
check:
  question: |-
    The Earth takes about $179$ days to go from the September equinox to the March equinox, but about $186$ days to go from the March equinox back to the September equinox. Which statement correctly explains the difference?
  options:
    A: |-
      The Earth is nearest the Sun in early January; the Sun's pull points at the Sun, so the Earth's angular momentum is conserved and it moves fastest when it is closest, covering that half sooner.
    B: |-
      The Earth is nearest the Sun in July, during the northern summer, so it moves fastest then and the March to September half is covered sooner.
    C: |-
      The Earth moves at a steady speed, but the Sun sits at the centre of the ellipse, so the winter half of the path is simply shorter.
    D: |-
      Winter days in the northern hemisphere have fewer hours of daylight, so fewer full days pass between the September and March equinoxes.
  answer: A
  explanation: |-
    Gravity on the Earth points at the Sun, so it exerts no torque about the Sun and $L = mvr$ is conserved. Near perihelion (early January) $r$ is smallest, so $v$ is largest, and the half of the orbit containing perihelion takes less time.
  misconceptions:
    B: |-
      Assumes summer happens when the Earth is closest to the Sun; seasons come from the tilt of the axis, and the Earth is actually farthest from the Sun in early July.
    C: |-
      Pictures a planet moving at constant speed with the Sun at the centre; the Sun is at a focus, and the speed changes all the way round the orbit.
    D: |-
      Confuses the length of daylight with the length of a day; every day is about $24$ hours long whatever the season, so daylight hours cannot change the count.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A night match: the goalkeeper's long kick at the top of its arc, the Moon and a satellite overhead, and a dish on the stand roof aimed at the satellite](scenes/football/gravitation.svg "Above the pitch, the Moon, the satellites and the planets all follow the same rules of motion.")

Aditi runs the fixtures for her district's inter-school football league, and she wants it to be fair. Her plan: the first half of the season from the March equinox to the September equinox, the second half from September back to March. "Two equal halves," she tells the committee, "just like a match."

Kabir, the league's statistician, counts the days on the calendar and frowns. "They're not equal. The first half is about $186$ days. The second is only about $179$."

"That can't be right. The equinoxes are exactly opposite each other. The Earth goes halfway round the Sun each time."

Kabir counts again and gets the same answer. A match has two halves of $45$ minutes each. Why doesn't the year?

## The physics

In the early 1600s **Johannes Kepler**, using years of careful planet positions recorded by Tycho Brahe, found three laws of planetary motion.

1. **Law of orbits:** every planet moves in an **ellipse** with the Sun at one **focus**, not at the centre. The nearest point is the **perihelion**, the farthest the **aphelion**.
2. **Law of areas:** the line joining the Sun to the planet sweeps out **equal areas in equal times**.
3. **Law of periods:** the square of the orbital period $T$ is proportional to the cube of the **semi-major axis** $a$ (half the longest diameter of the ellipse): $T^2 \propto a^3$, with the same constant for every planet of the Sun.

**Why the law of areas holds.** The Sun's pull on a planet always points along the line to the Sun. A force along the line through a point has no torque about that point, so the planet's **angular momentum** about the Sun, $\vec{L} = \vec{r} \times \vec{p}$, is conserved. In a short time $\Delta t$ the line sweeps a thin triangle of area $\Delta A = \tfrac{1}{2}|\vec{r} \times \vec{v}|\,\Delta t$, so

$$\frac{\Delta A}{\Delta t} = \frac{L}{2m} = \text{constant}$$

At perihelion and aphelion the velocity is perpendicular to $\vec{r}$, so $L = mvr$ and $v_\text{p} r_\text{p} = v_\text{a} r_\text{a}$: **closer means faster**.

**Aditi's puzzle.** The line joining the two equinox positions passes through the Sun, so it cuts the orbit into two parts of *different* area. The Earth is at perihelion in early January, so the September-to-March part is the smaller one, covered at higher speed. Equal areas in equal times means it takes less time: about $179$ days against $186$.

![An exaggerated ellipse cut by a dashed line through the Sun into a small orange part near perihelion and a large blue part near aphelion, with a long speed arrow at perihelion and a short one at aphelion](figures/kepler_laws/unequal-halves-of-year.svg "The equinox line runs through the Sun, not the centre, so the two halves have different areas. The half near perihelion is smaller and is covered faster.")

![An ellipse with the Sun at one focus; a short wide shaded sector at perihelion and a long thin one at aphelion have equal areas](figures/kepler_laws/equal-areas-ellipse.svg "Equal areas take equal times. Near the Sun the sector is short and wide, so the planet covers a longer arc in the same time.")

## Worked example

**Given:** Mercury's distance from the Sun is $4.60 \times 10^{10}\,\text{m}$ at perihelion and $6.98 \times 10^{10}\,\text{m}$ at aphelion. Jupiter's semi-major axis is $5.20\,\text{AU}$ (Earth: $1.00\,\text{AU}$, $T = 1.00$ year).
**Find:** (a) how much faster Mercury moves at perihelion than at aphelion; (b) Jupiter's period.

(a) Angular momentum is conserved and $\vec{v} \perp \vec{r}$ at both points:

$$\frac{v_\text{p}}{v_\text{a}} = \frac{r_\text{a}}{r_\text{p}} = \frac{6.98 \times 10^{10}}{4.60 \times 10^{10}} \approx 1.52$$

Mercury is about $52\%$ faster at perihelion.

(b) Same Sun, so $T^2/a^3$ is the same for Earth and Jupiter:

$$T_\text{J} = 1.00 \times (5.20)^{3/2}\ \text{years} = \sqrt{140.6}\ \text{years} \approx 11.9\ \text{years}$$

**Sanity check:** $11.9^2 = 141.6 \approx 5.20^3 = 140.6$. Jupiter is far out and slow, so a long period makes sense. And in (a) the nearer point has the higher speed, as the law of areas says.

## Where the picture breaks

A football season has nothing to do with orbits: the league only borrows the calendar. Kabir's day counts are real, but the difference also depends slightly on exactly where the equinox line sits relative to perihelion, which drifts over thousands of years. The figure exaggerates the ellipse enormously; Earth's real orbit is so nearly circular that you could not tell it from a circle by eye.

Kepler's laws also treat the Sun as fixed and ignore the small pulls the planets exert on each other. And the constant in $T^2 \propto a^3$ is shared only by bodies orbiting the **same** central body.

## Key takeaway

Planets move in ellipses with the Sun at a focus, sweep equal areas in equal times, and obey $T^2 \propto a^3$. The law of areas is conservation of angular momentum: the Sun's pull has no torque about the Sun, so $vr$ stays fixed and a planet speeds up near perihelion. That is why the Earth's September-to-March half of the year is about a week shorter.
