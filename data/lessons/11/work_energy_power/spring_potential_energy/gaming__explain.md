---
concept_id: spring_potential_energy
interest: gaming
format: explain
title: Pull the plunger twice as far, get four times the punch
check:
  question: |-
    A spring launcher in an arcade machine has spring constant $k = 400\,\text{N/m}$ and is compressed by $0.05\,\text{m}$. How much potential energy is stored in it?
  options:
    A: |-
      $20\,\text{J}$
    B: |-
      $10\,\text{J}$
    C: |-
      $0.5\,\text{J}$
    D: |-
      $1.0\,\text{J}$
  answer: C
  explanation: |-
    $U = \tfrac{1}{2}kx^2 = \tfrac{1}{2} \times 400 \times (0.05)^2 = 200 \times 0.0025 = 0.5\,\text{J}$.
  misconceptions:
    A: |-
      Computes $kx = 20$, which is the restoring *force* in newtons, not an energy; force and stored energy are different quantities with different units.
    B: |-
      Uses $\tfrac{1}{2}kx$ — the compression is squared, because the force grows as the spring is squeezed and the energy is the area under that rising line.
    D: |-
      Leaves out the factor $\tfrac{1}{2}$ ($kx^2$); the half is the area of the triangle under the straight line $F = kx$, not of the rectangle around it.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A gaming desk at night: a monitor shows a physics sandbox with a spring launcher, a kart at the top of a loop and a crate being dragged by a rope, beside a force-feedback racing wheel and a controller](scenes/gaming/work_energy_power.svg "On the left of the screen, a compressed spring is about to hand everything it holds to a ball.")

The college fest has an old pinball table in the corner, and Kabir has been feeding it coins for an hour. The plunger is the only control he has before the ball enters the table: pull it back, let go, and the ball shoots up the side lane.

He has worked out that a half pull just barely reaches the top lane, so he tries a full pull — twice as far back — expecting a ball that arrives twice as fast. Instead the ball rockets round the loop, slams the top bumper and drops back down so quickly he loses it.

His friend Aditi, waiting for her turn, is delighted. "You doubled the pull and the ball went ballistic."

Kabir pulls the plunger back slowly, feeling it. Near the start it barely resists; near the end he has to lean on it. That is the clue: the spring does not push back with one fixed force. So how much energy does a pulled-back spring actually hold — and why does pulling twice as far do so much more than twice as much?

## The physics

For an ideal spring, the restoring force grows in step with how far it is stretched or compressed — **Hooke's law**:

$$F = -kx$$

$x$ is the displacement from the spring's natural length, $k$ is the **spring constant** in newtons per metre (a stiff plunger has a large $k$), and the minus sign says the force always points back towards the natural length, opposing whatever you are doing to it.

Because $F$ changes with $x$, the work you do is the area under the $F$–$x$ line — a triangle of base $x$ and height $kx$:

$$U = \tfrac{1}{2}kx^2$$

That is the **elastic potential energy**: the energy stored in the spring, in joules, measured from the natural length where $U = 0$. The spring force is conservative, so a spring hands back every joule when it returns to its natural length.

![Left: the spring force rising in a straight line with stretch, with the triangle under it equal to one half k x squared. Right: the stored energy rising as a parabola, four times larger when the stretch doubles](figures/spring_potential_energy/spring-force-and-energy.svg "For an ideal spring (this one has k = 200 N/m), the force grows in step with x, so the stored energy grows with x squared.")

The $x^2$ is Kabir's answer. Pull twice as far and you fight twice the force through twice the distance: $2 \times 2 = 4$ times the energy. Hooke's law holds only up to the spring's **elastic limit** — stretch it beyond that and it stays bent, and none of this applies.

## Worked example

**Given** (illustrative arcade values): a plunger spring with $k = 200\,\text{N/m}$, pulled back $x = 0.10\,\text{m}$, launching a steel ball of mass $0.08\,\text{kg}$ along a level lane.
**Find:** the energy stored, the ball's launch speed, and what changes at a full $0.20\,\text{m}$ pull.

**Step 1 — the energy in the spring.**

$$U = \tfrac{1}{2}kx^2 = \tfrac{1}{2} \times 200 \times (0.10)^2 = 100 \times 0.01 = 1.0\,\text{J}$$

**Step 2 — hand it to the ball.** The spring returns to its natural length, so all $1.0\,\text{J}$ becomes kinetic energy (ignoring friction in the lane):

$$\tfrac{1}{2}mv^2 = 1.0 \quad\Rightarrow\quad v^2 = \frac{2 \times 1.0}{0.08} = 25 \quad\Rightarrow\quad v = 5\,\text{m/s}$$

That is about the speed of a jog — fast for something the size of a marble.

**Step 3 — the full pull.** Doubling $x$ to $0.20\,\text{m}$ gives $U = \tfrac{1}{2} \times 200 \times 0.04 = 4.0\,\text{J}$: four times the energy. Since $v \propto \sqrt{U}$, the ball leaves at $10\,\text{m/s}$ — twice as fast, carrying four times the punch into the bumpers.

**Sanity check:** four times the energy but only twice the speed is exactly what $\tfrac{1}{2}mv^2$ demands, so the two halves of the calculation agree.

## Where the picture breaks

A real plunger has a rubber tip and a shaft that rubs in its guide, so a little of the stored energy turns into heat and sound rather than motion — the ball leaves slightly slower than $5\,\text{m/s}$. Hooke's law is itself an approximation: coils that begin to touch stiffen up, and past the elastic limit the spring is simply ruined. The ideal spring here is also massless; a heavy spring keeps some of the energy as motion of its own coils. And nothing in $U = \tfrac{1}{2}kx^2$ cares whether you stretched or compressed the spring — the sign of $x$ disappears in the square.

## Key takeaway

An ideal spring obeys $F = -kx$ and stores $U = \tfrac{1}{2}kx^2$ — the triangular area under the force line, measured from its natural length. Because the stored energy goes as $x^2$, doubling the stretch stores four times the energy, which a spring returns in full when it relaxes.
