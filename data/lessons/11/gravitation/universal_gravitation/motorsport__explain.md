---
concept_id: universal_gravitation
interest: motorsport
format: explain
title: How hard do two parked cars pull on each other
check:
  question: |-
    Two cars of equal mass stand with their centres $2\,\text{m}$ apart, and the gravitational pull between them is $F$. They are rolled apart until their centres are $6\,\text{m}$ apart. The pull between them is now
  options:
    A: |-
      $F/3$
    B: |-
      $9F$
    C: |-
      $F/36$
    D: |-
      $F/9$
  answer: D
  explanation: |-
    $F \propto 1/r^2$, and the separation is multiplied by $6/2 = 3$, so the force is divided by $3^2 = 9$.
  misconceptions:
    A: |-
      Uses $F \propto 1/r$ instead of $1/r^2$, as if tripling the distance only divided the pull by three. The law has the distance squared.
    B: |-
      Gets the factor $9$ right but applies it the wrong way round. Gravity gets *weaker* with distance, so the force is divided by $9$, not multiplied.
    C: |-
      Puts $r = 6\,\text{m}$ into $1/r^2$ and compares the answer with $1$ instead of with $1/2^2$. A ratio needs both separations, not just the new one.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A pit lane at a hill-climb event: a car on a weighbridge, a team truck with a satellite dish on its roof, a GPS aerial on the car's engine cover and a drop-test rig beside the scrutineering bay](scenes/motorsport/gravitation.svg "Two cars in a pit lane pull on each other gravitationally. This lesson is about how much — and the answer is the point.")

It is two in the morning at a twelve-hour endurance race, and Sneha is watching the speed traces of two cars that have been nose to tail for six laps. Every time they reach the long back straight, the chasing car creeps closer without any extra throttle.

"It's getting pulled along," says a first-year who has come to watch. "Gravity. The car in front is heavy and it's right there."

Mahesh, the team's aerodynamicist, laughs so hard he spills his tea. "That's the tow. It's air, not gravity."

"Fine," says the first-year, a little stung, "but gravity is still there. Everything pulls on everything. You said so yourself."

Mahesh stops laughing, because that part is true. Two cars, a tonne each, two metres apart. There *is* a pull. So how big is it actually?

## The physics

**Newton's law of universal gravitation.** Every particle of matter attracts every other particle with a force along the line joining them:

$$F = G\,\frac{m_1 m_2}{r^2}$$

Here $m_1$ and $m_2$ are the two masses in $\text{kg}$, $r$ is the distance between their centres in $\text{m}$, and

$$G = 6.67 \times 10^{-11}\,\text{N}\,\text{m}^2/\text{kg}^2$$

is the **universal gravitational constant** — the same number for any two masses anywhere.

Three things to hold on to:

- The two forces are an **action–reaction pair**: the pull on the car in front is exactly as big as the pull on the car behind, and opposite in direction. Equal forces, not equal effects — the lighter body gets the larger acceleration.
- It is an **inverse-square** law. Double the separation and the force drops to a quarter; triple it and it drops to a ninth.
- Strictly, the law is for **point masses**. It also works exactly for a uniform sphere, which attracts outside bodies as though all its mass sat at its centre — which is why we can treat the whole Earth as a point at its centre.

![Two masses pulling on each other with equal and opposite forces along the line joining their centres, and a scale showing the force falling to a quarter at double the distance and a ninth at triple](figures/universal_gravitation/force-pair-inverse-square.svg "The pull is the same size on both bodies, whatever their masses. Moving them apart weakens it as 1/r².")

The reason nobody in the pit lane has ever noticed this force is the size of $G$. In SI units it is smaller than a ten-billionth. Gravity only becomes something you can feel when one of the masses is enormous — planet-sized enormous.

## Worked example

**Given:** two race cars, each of mass $m = 800\,\text{kg}$, with their centres $r = 2\,\text{m}$ apart.
**Find:** the gravitational pull between them, and how it compares with the Earth's pull on one of them.

**Step 1 — the masses.** $m_1 m_2 = 800 \times 800 = 6.4 \times 10^{5}\,\text{kg}^2$, and $r^2 = 4\,\text{m}^2$.

**Step 2 — the force.**

$$F = 6.67 \times 10^{-11} \times \frac{6.4 \times 10^{5}}{4} = 6.67 \times 10^{-11} \times 1.6 \times 10^{5} \approx 1.1 \times 10^{-5}\,\text{N}$$

**Step 3 — picture it.** A hundredth of a millinewton is roughly the weight of a single coarse grain of sand. Two cars, a tonne apiece, tug on each other about as hard as that grain presses on your palm.

**Step 4 — and the Earth?** Its pull on one car is $mg = 800 \times 9.8 = 7840\,\text{N}$ — roughly seven hundred million times larger. Same $G$, same inverse square; the Earth simply has about $6 \times 10^{24}\,\text{kg}$ on its side.

**Sanity check:** nobody has ever had to prise two parked cars apart, so an answer far below anything a hand could feel is the right size.

## Where the picture breaks

The tow really is air. A car punches a hole in the air and leaves a low-pressure wake; the car behind meets less drag there and gains. Gravity has nothing to do with it, and the first-year's instinct was wrong — but the question was a good one, because the pull genuinely exists and is simply tiny.

The number itself is only an estimate. $F = Gm_1m_2/r^2$ is exact for point masses and for uniform spheres, and two cars two metres apart are neither: their sizes are comparable with their separation, so different parts of each car sit at different distances. Treat $1.1 \times 10^{-5}\,\text{N}$ as an order of magnitude, not a measurement. And $G$ is the worst-known of the fundamental constants, because experiments to measure it must detect forces this small while the whole Earth pulls downwards.

## Key takeaway

Any two masses attract each other with $F = Gm_1m_2/r^2$, directed along the line between their centres, equal and opposite on the two bodies, with $G = 6.67 \times 10^{-11}\,\text{N}\,\text{m}^2/\text{kg}^2$. Because $G$ is so small, everyday objects pull on each other unmeasurably weakly; gravity only takes over when one mass is planet-sized.
