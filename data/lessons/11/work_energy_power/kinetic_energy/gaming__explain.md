---
concept_id: kinetic_energy
interest: gaming
format: explain
title: Double the speed, four times the wreck
check:
  question: |-
    A crate in a game engine has mass $2\,\text{kg}$ and is moving at $54\,\text{km/h}$. What kinetic energy does the engine store for it?
  options:
    A: |-
      $2916\,\text{J}$
    B: |-
      $15\,\text{J}$
    C: |-
      $450\,\text{J}$
    D: |-
      $225\,\text{J}$
  answer: D
  explanation: |-
    Convert first: $54\,\text{km/h} = 54/3.6 = 15\,\text{m/s}$. Then $K = \tfrac{1}{2}mv^2 = \tfrac{1}{2} \times 2 \times 15^2 = 225\,\text{J}$.
  misconceptions:
    A: |-
      Substitutes the speed in km/h ($\tfrac{1}{2} \times 2 \times 54^2$); the joule is built from metres and seconds, so the speed must be converted to m/s before squaring.
    B: |-
      Forgets to square the speed ($\tfrac{1}{2} \times 2 \times 15$); kinetic energy grows with the *square* of the speed, not in proportion to it.
    C: |-
      Leaves out the factor $\tfrac{1}{2}$ ($2 \times 15^2$); the half comes from the work needed to build the speed up from rest, where the force acts on a body that is slower than $v$ for most of the push.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A gaming desk at night: a monitor shows a physics sandbox with a spring launcher, a kart at the top of a loop and a crate being dragged by a rope, beside a force-feedback racing wheel and a controller](scenes/gaming/work_energy_power.svg "Everything moving on this screen carries energy, and the engine tracks it frame by frame.")

Priya has the worst job on her team's racing game: the crash code. Hit the barrier and something has to break, and it has to feel fair.

Her first rule was simple — damage in proportion to speed. Twice as fast, twice the damage. The testers hated it. "You can slam the wall at full speed and drive away," one wrote. So she watched real crash-test videos, and a pattern jumped out: a small increase in speed made a shockingly larger mess.

Her teammate Zubin shrugs. "So multiply by three instead of two."

Priya doesn't want a magic number that feels right; she wants the number the physics gives. Her engine already stores every object's mass and speed. What quantity should a crash actually scale with — and why does going from $10\,\text{m/s}$ to $20\,\text{m/s}$ break so much more than twice as much?

## The physics

The energy a body has **because of its motion** is its **kinetic energy**:

$$K = \tfrac{1}{2}mv^2$$

with $m$ in kilograms and $v$ in metres per second, giving joules. It is a scalar, never negative, and it does not depend on the direction of travel — only on how fast.

**Where the formula comes from.** Push a body of mass $m$ from rest with a constant net force $F$ along a straight line for a distance $d$. Its acceleration is $a = F/m$, and $v^2 = 0 + 2ad$, so $d = v^2/2a$. The work done is

$$W = Fd = (ma)\frac{v^2}{2a} = \tfrac{1}{2}mv^2$$

So $\tfrac{1}{2}mv^2$ is exactly the work needed to bring a body from rest up to speed $v$ — and exactly the work that must be taken away to stop it again. In a crash, the barrier is what takes it away.

![A curve of kinetic energy against speed, rising steeply: at twice the speed the energy is four times as large](figures/kinetic_energy/ke-vs-speed.svg "Plotted for a 0.16 kg object, but the shape is the point: because K depends on v squared, doubling the speed multiplies the energy by four, whatever the mass.")

That $v^2$ is Priya's answer. Speed counts twice over: a faster body needs a bigger force to stop in a given distance, *and* it travels further while that force acts.

## Worked example

**Given** (illustrative game values): a kart of mass $m = 200\,\text{kg}$, first at $v = 10\,\text{m/s}$, then at $20\,\text{m/s}$.
**Find:** the kinetic energy at each speed, and the ratio between them.

**Step 1 — the slower kart.**

$$K_1 = \tfrac{1}{2} \times 200 \times 10^2 = 100 \times 100 = 10\,000\,\text{J} = 10\,\text{kJ}$$

**Step 2 — the faster kart.** Only the speed changes:

$$K_2 = \tfrac{1}{2} \times 200 \times 20^2 = 100 \times 400 = 40\,000\,\text{J} = 40\,\text{kJ}$$

**Step 3 — compare.** $K_2/K_1 = 40/10 = 4$. Twice the speed, four times the energy the barrier has to absorb.

To picture $40\,\text{kJ}$: lifting this $200\,\text{kg}$ kart onto a roof $20\,\text{m}$ up takes $mgh = 200 \times 9.8 \times 20 \approx 39\,\text{kJ}$ — about the same. The faster crash is a six-storey drop.

**Sanity check:** the mass never changed and the speed doubled, so the $v^2$ in the formula must give a factor of $2^2 = 4$ — which is what the arithmetic shows.

## Where the picture breaks

Kinetic energy is not damage. How much a crash breaks depends on how quickly and over how small an area that energy is removed — a crumple zone that stretches the stop over half a metre lowers the force enormously without changing the energy at all. $\tfrac{1}{2}mv^2$ also counts only motion of the body as a whole; a spinning kart stores extra rotational energy you will meet later. And speed depends on who measures it: to a stationary barrier the kart carries $40\,\text{kJ}$, while to a kart driving alongside at the same speed it carries none — which is why side-by-side contact at high speed is survivable and a wall is not.

## Key takeaway

Kinetic energy is the energy of motion, $K = \tfrac{1}{2}mv^2$. It equals the work needed to bring a body from rest to speed $v$, and the work that must be removed to stop it. Because it depends on $v^2$, doubling the speed quadruples the energy.
