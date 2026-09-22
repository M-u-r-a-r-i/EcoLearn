---
concept_id: kinetic_energy
interest: football
format: explain
title: The heavy wet ball or the faster shot
check:
  question: |-
    A goal kick sends a $0.45\,\text{kg}$ ball off at $90\,\text{km/h}$. What is its kinetic energy as it leaves the boot?
  options:
    A: |-
      $1823\,\text{J}$
    B: |-
      $141\,\text{J}$
    C: |-
      $5.6\,\text{J}$
    D: |-
      $281\,\text{J}$
  answer: B
  explanation: |-
    Convert first: $90\,\text{km/h} = 90/3.6 = 25\,\text{m/s}$. Then $K = \tfrac{1}{2}mv^2 = \tfrac{1}{2} \times 0.45 \times 25^2 = 0.225 \times 625 \approx 141\,\text{J}$.
  misconceptions:
    A: |-
      Puts the speed in km/h straight into $\tfrac{1}{2}mv^2$ ($0.225 \times 90^2$); the joule is built on metres per second, so the speed must be converted first.
    C: |-
      Forgets to square the speed ($0.225 \times 25$); kinetic energy grows with the square of the speed, not in proportion to it.
    D: |-
      Leaves out the factor of one half ($0.45 \times 25^2$); the $\tfrac{1}{2}$ comes from the work needed to build up the speed from rest.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A football training ground by day: a player drags a weighted sled on a strap, a striker lofts the ball in a high arc, and the goalkeeper dives to catch it](scenes/football/work_energy_power.svg "Every ball in flight here carries energy. How much depends on its mass and, even more, on its speed.")

Rohit's grandfather played for his village team decades ago, and whenever it rains he tells the same story. "Our balls were leather, and they soaked up water. By the second half, heading one was like heading a coconut. You young ones have it easy."

Rohit is sceptical. That evening, he watches a keeper at his club parry a shot that was simply hit very, very hard. The keeper shakes out his wrists for a full minute afterwards.

"So which hurts more, Dadaji?" Rohit asks at dinner. "A ball that's heavier, or a shot that's faster?"

His grandfather shrugs. "Heavier, obviously."

Rohit isn't sure. Suppose the wet ball is ten percent heavier, and the shot is ten percent faster. Which one arrives carrying more energy, and by how much? And what exactly is this "energy of motion" in the first place?

## The physics

A moving body can do work: a moving ball can push a keeper's gloves back, stretch a net or rattle a crossbar. The energy a body has **because of its motion** is its **kinetic energy**:

$$K = \tfrac{1}{2}mv^2$$

where $m$ is the mass and $v$ the speed. It is a scalar, measured in joules, never negative, and independent of the direction of motion.

**Where the formula comes from.** Push a body of mass $m$, starting from rest, with a constant net force $F$ along a straight line for a distance $d$. Its acceleration is $a = F/m$, and from the equations of motion $v^2 = 0 + 2ad$. The work done is

$$W = Fd = (ma)d = m \cdot \frac{v^2}{2} = \tfrac{1}{2}mv^2$$

So $\tfrac{1}{2}mv^2$ is exactly the work needed to bring the body from rest to speed $v$, and the same work must be taken away to stop it.

That answers Rohit's question. Mass appears once in the formula, but speed appears twice. A faster ball needs a bigger force for the same distance, *and* it covers more distance while you're bringing it up to speed.

![Kinetic energy against speed for a 0.43 kilogram ball and a 10 percent heavier 0.473 kilogram ball: both curves bend upwards, and the lighter ball has 86 joules at 20 metres per second and 344 joules at 40 metres per second](figures/kinetic_energy/ke-vs-speed-mass-compare.svg "Ten percent more mass lifts the curve only a little. Doubling the speed multiplies the energy by four.")

## Worked example

**Given:** a dry ball of mass $m = 0.43\,\text{kg}$ (within the Laws' $410$–$450\,\text{g}$) struck at $v = 20\,\text{m/s}$; a wet ball $10\%$ heavier, $0.473\,\text{kg}$ (illustrative); a shot $10\%$ faster, $22\,\text{m/s}$.
**Find:** the kinetic energy in each case, and the average force a boot needs to give the dry ball $20\,\text{m/s}$ over a push of about $0.10\,\text{m}$ (illustrative).

$$K_\text{dry} = \tfrac{1}{2} \times 0.43 \times 20^2 = 0.215 \times 400 = 86\,\text{J}$$

$$K_\text{wet} = \tfrac{1}{2} \times 0.473 \times 20^2 = 0.2365 \times 400 \approx 94.6\,\text{J} \quad (10\%\text{ more})$$

$$K_\text{fast} = \tfrac{1}{2} \times 0.43 \times 22^2 = 0.215 \times 484 \approx 104\,\text{J} \quad (21\%\text{ more})$$

Ten percent more speed beats ten percent more mass, because $1.1^2 = 1.21$. Double the speed, to $40\,\text{m/s}$, and the energy becomes $0.215 \times 1600 = 344\,\text{J}$, four times as much.

The ball starts at rest, so the boot must do $86\,\text{J}$ of work on it:

$$F_\text{avg} = \frac{W}{d} = \frac{86}{0.10} = 860\,\text{N}$$

**Sanity check:** the ball's weight is $0.43 \times 9.8 \approx 4.2\,\text{N}$, so the boot pushes with about 200 times the ball's weight, but only for a tiny moment. Units: $\text{kg} \times (\text{m/s})^2 = \text{kg m}^2/\text{s}^2 = \text{J}$.

## Where the picture breaks

A real kick isn't a constant force along a straight line. The force rises and falls during contact, so $860\,\text{N}$ is only an average. A ball struck off-centre also spins, which stores some extra energy of rotation that $\tfrac{1}{2}mv^2$ leaves out; you'll meet that later. And kinetic energy isn't the same as "how much it hurts". That depends on how quickly, and over how small an area, the energy is taken away, which is why keepers wear padded gloves and give with their hands.

## Key takeaway

Kinetic energy is the energy of motion, $K = \tfrac{1}{2}mv^2$. It equals the work needed to bring a body from rest to speed $v$, and the work needed to stop it again. Energy grows in proportion to mass but with the square of speed, so doubling the speed quadruples the energy.
