---
concept_id: spring_potential_energy
interest: football
format: explain
title: How far the rebounder net stretches
check:
  question: |-
    Treat a rebounder net as an ideal spring with $k = 2000\,\text{N/m}$. A ball pushes the centre of the net back by $0.20\,\text{m}$ before it stops for an instant. How much energy is stored in the net at that moment?
  options:
    A: |-
      $200\,\text{J}$
    B: |-
      $80\,\text{J}$
    C: |-
      $400\,\text{J}$
    D: |-
      $40\,\text{J}$
  answer: D
  explanation: |-
    The stored elastic potential energy is $U = \tfrac{1}{2}kx^2 = \tfrac{1}{2} \times 2000 \times 0.20^2 = 1000 \times 0.04 = 40\,\text{J}$.
  misconceptions:
    A: |-
      Uses $\tfrac{1}{2}kx$ without squaring the stretch; the stored energy is the area of a triangle whose height is $kx$ and whose base is $x$, so $x$ appears twice.
    B: |-
      Leaves out the factor of one half ($kx^2$); the force grows from zero to $kx$, so the average force during the stretch is only half of $kx$.
    C: |-
      Calculates the force $kx = 400\,\text{N}$ and treats it as the energy; force and energy are different quantities, and energy needs force times distance.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A football training ground by day: a player drags a weighted sled on a strap, a striker lofts the ball in a high arc, and the goalkeeper dives to catch it](scenes/football/work_energy_power.svg "Every ball that is caught, blocked or kicked into a net briefly squashes or stretches something.")

Aarav's parents gave him a rebounder for his birthday: a steel frame with a tight net held on by springs all round its edge. Kick the ball into it and the net sinks back, then fires the ball straight back at your feet.

On the first day, he passes gently. On the second, he wants to blast it. His sister Diya, who has been watching the net closely, stops him. "Look behind the net. There's a steel bar about $30\,\text{cm}$ back. Kick too hard and the ball will smash into it."

Aarav scoffs. "It's a net with springs. It'll just stretch a bit more."

For an instant, at the deepest point, the ball has stopped. Its kinetic energy has gone into the stretched net and its springs, and then it comes back out. How far does the net stretch for a given kick, and what happens to that stretch if Aarav kicks twice as hard?

## The physics

Many things behave like a **spring** when stretched or squashed a little. For an ideal spring, the restoring force obeys **Hooke's law**:

$$F = -kx$$

$x$ is the extension (positive) or compression (negative) from the natural length, and $k$ is the **spring constant** in N/m, a measure of stiffness. The minus sign means the force always points back towards the natural length.

**Stored energy from the graph.** To stretch the spring slowly by $x$, you must pull with a force that grows from $0$ to $kx$. The work you do is the area under the force-displacement graph, a triangle:

$$W = \tfrac{1}{2} \times x \times kx = \tfrac{1}{2}kx^2$$

The spring force is conservative, so this work is stored as **elastic potential energy**:

$$U = \tfrac{1}{2}kx^2$$

with $U = 0$ at the natural length. Because of the $x^2$, a compression and an extension of the same size store the same energy, and doubling $x$ stores four times as much.

![Left: spring force rising in a straight line with stretch, with the triangle under it equal to one half k x squared. Right: stored energy rising as a parabola, four times larger when the stretch doubles](figures/spring_potential_energy/spring-force-and-energy.svg "For any ideal spring (this one has k = 200 N/m), force grows in step with x, so the stored energy grows with x squared.")

**Using it in energy problems.** When a moving body stretches a spring and no other force does work, its kinetic energy becomes spring energy. At the deepest point the body is momentarily at rest:

$$\tfrac{1}{2}mv^2 = \tfrac{1}{2}kx_\text{max}^2 \quad\Rightarrow\quad x_\text{max} = v\sqrt{\frac{m}{k}}$$

So the stretch is proportional to the speed.

## Worked example

**Given** (illustrative): ball mass $m = 0.43\,\text{kg}$ arriving head-on at $v = 15\,\text{m/s}$; treat the net and its springs as one ideal spring with $k = 3000\,\text{N/m}$; the bar is $0.30\,\text{m}$ behind the net.
**Find:** the maximum stretch and the largest force on the ball; then the speed at which the ball would just reach the bar.

$$K = \tfrac{1}{2} \times 0.43 \times 15^2 = 0.215 \times 225 \approx 48.4\,\text{J}$$

$$x_\text{max} = \sqrt{\frac{2K}{k}} = \sqrt{\frac{2 \times 48.4}{3000}} = \sqrt{0.0323} \approx 0.18\,\text{m}$$

$$F_\text{max} = kx_\text{max} = 3000 \times 0.18 \approx 540\,\text{N}$$

The ball reaches the bar when $x_\text{max} = 0.30\,\text{m}$:

$$v = x_\text{max}\sqrt{\frac{k}{m}} = 0.30 \times \sqrt{\frac{3000}{0.43}} = 0.30 \times 83.5 \approx 25\,\text{m/s}$$

So Diya is right to worry. A $15\,\text{m/s}$ pass stretches the net $18\,\text{cm}$; a kick of about $25\,\text{m/s}$ ($90\,\text{km/h}$) reaches the bar. Doubling the speed to $30\,\text{m/s}$ would double the stretch to about $36\,\text{cm}$.

**Sanity check:** $\tfrac{1}{2} \times 3000 \times 0.18^2 = 1500 \times 0.0324 \approx 48.6\,\text{J}$, matching $48.4\,\text{J}$ within rounding.

## Where the picture breaks

A real rebounder isn't one ideal spring. The net sags and stretches as well as the springs, and the force grows faster than in proportion to the stretch as the net tightens, so a single $k$ is only an average. The ball itself also squashes, acting as a second, very stiff spring. Some energy becomes heat and sound in the net and the ball, so the rebound is always slower than the kick. And gravity pulls the ball down slightly during the brief contact. The model gives the size of the stretch, not every detail.

## Key takeaway

A spring stretched or compressed by $x$ stores elastic potential energy $U = \tfrac{1}{2}kx^2$, the area under its $F = kx$ line. In energy problems, set the kinetic energy lost equal to the spring energy gained, $\tfrac{1}{2}mv^2 = \tfrac{1}{2}kx^2$, so the maximum stretch grows in proportion to the speed.
