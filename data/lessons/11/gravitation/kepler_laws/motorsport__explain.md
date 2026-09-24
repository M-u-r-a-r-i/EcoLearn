---
concept_id: kepler_laws
interest: motorsport
format: explain
title: The timetable printed four days early
check:
  question: |-
    Two satellites circle the Earth in circular orbits. The second one's orbit radius is **nine times** the first one's. How many times longer does the second satellite take to go round once?
  options:
    A: |-
      $9$ times as long
    B: |-
      $27$ times as long
    C: |-
      $3$ times as long
    D: |-
      $81$ times as long
  answer: B
  explanation: |-
    Kepler's third law gives $T^2 \propto r^3$, so $T \propto r^{3/2}$. With $r$ multiplied by $9$, the period is multiplied by $9^{3/2} = 27$.
  misconceptions:
    A: |-
      Assumes the period is simply proportional to the radius, as if the satellite kept the same speed in every orbit. A wider orbit is also a slower one, so the period grows faster than the radius.
    C: |-
      Takes a square root instead of the $3/2$ power, as if $T^2 \propto r$. The law has the *cube* of the radius, not the first power.
    D: |-
      Squares the radius ratio, swapping the roles of the two sides: it is $T$ that is squared and $r$ that is cubed, not the other way round.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A pit lane at a hill-climb event: a car on a weighbridge, a team truck with a satellite dish on its roof, a GPS aerial on the car's engine cover and a drop-test rig beside the scrutineering bay](scenes/motorsport/gravitation.svg "The dish on the truck roof and the small aerial on the car both listen to satellites. Everything in this chapter is really about what those satellites are doing.")

Ishaan's college car club has taken its hill-climb car to a course in the Ghats: a narrow road up through eleven hairpins, with no mobile signal anywhere on it. To get timing data back to their workshop they have borrowed a portable satellite terminal.

The handbook offers two services. One says *aim the dish once and leave it*. The other says *windows of about nine minutes, roughly every hour and a half*.

Pooja, who runs the timing laptop, prints the second service's window times for the whole weekend — four days ahead, to the minute.

"You can't possibly know that," Ishaan says. "That's four days away."

"Somebody worked out the rule four hundred years ago," Pooja says.

So what makes an orbit predictable to the minute — and why does one satellite need chasing while the other never moves at all?

## The physics

**Johannes Kepler** found three rules in years of patient naked-eye positions of the planets, collected by Tycho Brahe.

1. **Law of orbits.** Every planet moves in an **ellipse**, with the Sun at one **focus** — not at the centre.
2. **Law of areas.** The line from the Sun to the planet sweeps out **equal areas in equal times**.
3. **Law of periods.** $T^2 \propto a^3$, where $a$ is the **semi-major axis**, half the longest diameter of the ellipse.

Newton later showed all three follow from his law of gravitation, and that they hold for *any* light body orbiting a much heavier one. Word for word, they describe Pooja's satellites, with the Earth's centre at the focus.

![An ellipse with the Sun at one focus; a short wide shaded sector near the focus and a long thin one far away have equal areas](figures/kepler_laws/equal-areas-ellipse.svg "The two shaded areas are equal, so they take equal times. The arc near the focus is far longer, so the body must be moving much faster there.")

**Why the law of areas is true.** Gravity on the orbiting body always points at the central body. A force aimed straight at a chosen point has no turning effect about that point, so the **torque** about it is zero and the **angular momentum** $\vec{L} = \vec{r} \times \vec{p}$ cannot change. In a short time $\Delta t$ the line sweeps a thin triangle of area $\Delta A = \tfrac{1}{2}\,|\vec{r} \times \vec{v}|\,\Delta t$, so

$$\frac{\Delta A}{\Delta t} = \frac{L}{2m}$$

With $L$ and $m$ both fixed, area is swept at a steady rate. Kepler's second law *is* conservation of angular momentum, drawn as geometry. At the closest and farthest points the velocity is perpendicular to $\vec{r}$, so $L = mvr$ and

$$v_1 r_1 = v_2 r_2$$

A satellite three times farther out at its high point therefore crawls along at one third of its low-point speed — which is why a stretched orbit spends most of its time far away.

For a circular orbit, Newton's gravitation turns the third law into $T^2 = \dfrac{4\pi^2}{GM}\,r^3$. One constant, fixed by the Earth's mass, covers every satellite. That is the rule behind Pooja's four-day timetable.

## Worked example

**Given:** a satellite in a low circular orbit goes round once in about $1.5\,\text{hours}$. A second satellite has an orbit radius **four times** as large, also circular.
**Find:** how long the second satellite takes for one lap.

**Step 1 — same Earth, same constant.** So $T^2/r^3$ is the same for both, and

$$\frac{T_2^{\,2}}{T_1^{\,2}} = \left(\frac{r_2}{r_1}\right)^3 = 4^3 = 64$$

**Step 2 — undo the square.** $T_2/T_1 = \sqrt{64} = 8$. Four times farther out means eight times longer per lap.

**Step 3 — put the number in.** $T_2 = 8 \times 1.5\,\text{hours} = 12\,\text{hours}$.

**Sanity check:** the low satellite comes round about sixteen times a day and is gone over the horizon in minutes; the far one comes round twice a day and drifts slowly across the sky. That is exactly the difference between Pooja's two services.

## Where the picture breaks

The motorsport here is the setting, not the analogy. Nothing about the hill-climb car obeys Kepler's laws: gravity on it points straight down rather than at one fixed centre, the road pushes back, and its angular momentum about any point you choose is not conserved. Kepler's laws describe the satellites overhead, not the car.

The laws are idealisations even there. They treat the central body as fixed and ignore every other pull. Real satellites are nudged by the Earth's equatorial bulge, by the Moon and Sun, and in low orbit by the last traces of atmosphere, so pass predictions are refreshed from fresh tracking rather than trusted forever. And the constant in $T^2 = 4\pi^2 r^3/GM$ belongs to the central mass: you cannot compare an Earth satellite with a planet using the same one.

## Key takeaway

Kepler's laws: orbits are ellipses with the central body at a focus; the radius line sweeps equal areas in equal times; and $T^2 \propto a^3$. The law of areas is conservation of angular momentum in disguise — gravity points at the centre, so it exerts no torque about it, $vr$ stays fixed, and a body speeds up as it comes closer.
