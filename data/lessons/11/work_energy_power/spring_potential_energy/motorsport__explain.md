---
concept_id: spring_potential_energy
interest: motorsport
format: explain
title: What a suspension spring is really holding
check:
  question: |-
    A spring of stiffness $k = 200\,\text{N/m}$ stores $1.0\,\text{J}$ when it is compressed by $0.10\,\text{m}$. How much energy does it store when the compression is $0.20\,\text{m}$?
  options:
    A: |-
      $2.0\,\text{J}$
    B: |-
      $8.0\,\text{J}$
    C: |-
      $20\,\text{J}$
    D: |-
      $4.0\,\text{J}$
  answer: D
  explanation: |-
    $U = \tfrac{1}{2}kx^2 = \tfrac{1}{2}(200)(0.20)^2 = 100 \times 0.04 = 4.0\,\text{J}$. Doubling the compression multiplies the stored energy by four.
  misconceptions:
    A: |-
      Doubles the energy because the compression doubled. The *force* is proportional to $x$, but the stored energy is proportional to $x^2$.
    B: |-
      Uses $U = kx^2$ and forgets the factor $\tfrac{1}{2}$. That factor comes from the triangular area under the straight $F = kx$ line.
    C: |-
      Uses $U = \tfrac{1}{2}kx$ without squaring. Check the units: $\text{N/m} \times \text{m}$ gives newtons, a force, not joules.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A race track scene: a car coasts down a hill road onto the circuit, a second car speeds along the straight with a velocity arrow, a third brakes with glowing red discs, and two people push a kart in the foreground](scenes/motorsport/work_energy_power.svg "Every car here is sitting on four coil springs, each one holding a corner of the car off the road.")

At the chicane there is a kerb the drivers are supposed to ride, and all morning the club's single-seater has been coming off it with a bang you can hear from the paddock. Omkar, who is running the car, says the springs are too soft and it is bottoming out.

Vandana is not convinced, and she has a question nobody in the tent can answer.

They measure the spring on the bench first: a certain push squashes it a centimetre, twice that push squashes it two centimetres, exactly as you would expect. So Omkar's plan is simple — give it more travel, let the spring squash twice as far, and it will swallow the kerb.

"Twice the squash, twice the bang absorbed," he says.

Vandana keeps staring at the bench numbers. The *force* clearly doubles when the squash doubles. But the thing they actually need the spring to swallow is the kerb's energy, and she has a suspicion that energy does not follow the same simple rule.

## The physics

An **ideal spring** obeys **Hooke's law**: the restoring force is proportional to the displacement from its natural length and points back towards it,

$$F = -kx$$

where $x$ is the extension or compression and $k$ is the **spring constant** (or stiffness), in $\text{N/m}$. The minus sign says *restoring*: stretch it and it pulls back, squash it and it pushes back. The law holds only up to the spring's **elastic limit**; past that it deforms permanently and none of this applies.

To find the energy stored you cannot use $W = Fd$, because the force changes the whole way. You need the area under the force–displacement graph — and since $F = kx$ is a straight line through the origin, that area is a **triangle** of base $x$ and height $kx$:

$$U = \tfrac{1}{2} \times x \times kx = \frac{1}{2}kx^2$$

![Left: spring force rising in a straight line with compression, with the triangle under it equal to one half k x squared. Right: stored energy rising as a parabola, four times larger when the compression doubles](figures/spring_potential_energy/spring-force-and-energy.svg "The force grows in step with x, so the stored energy — the area under the force line — grows with x squared.")

That $x^2$ is Vandana's suspicion, confirmed. **Double the compression and the force doubles, but the stored energy quadruples**, because you are filling a triangle that has grown in both directions at once. The same formula covers stretching: $x^2$ is positive either way, so $U$ is never negative and the spring's natural length is the zero of the store.

The spring force is **conservative**, so all of it comes back: release the spring and every joule of $\tfrac{1}{2}kx^2$ is returned to whatever is holding it. In energy problems you simply carry the term along, exactly like $mgh$:

$$K_i + U_{\text{grav},i} + \tfrac{1}{2}kx_i^2 = K_f + U_{\text{grav},f} + \tfrac{1}{2}kx_f^2$$

when no non-conservative force does work.

## Worked example

**Given** (illustrative): a suspension spring of stiffness $k = 40\,000\,\text{N/m}$; the kerb pushes the wheel up so the spring compresses by $x = 0.10\,\text{m}$.
**Find:** the force at full compression, the energy stored, and what happens if the compression is doubled to $0.20\,\text{m}$.

*Force at full compression:*

$$F = kx = 40\,000 \times 0.10 = 4000\,\text{N}$$

That is the spring shoving back on the chassis with about the weight of four adults — at that one corner, for that instant.

*Energy stored:*

$$U = \tfrac{1}{2}kx^2 = \tfrac{1}{2}(40\,000)(0.10)^2 = 20\,000 \times 0.01 = 200\,\text{J}$$

*Double the compression:*

$$U = \tfrac{1}{2}(40\,000)(0.20)^2 = 20\,000 \times 0.04 = 800\,\text{J}$$

Four times the energy, from twice the travel. Omkar expected $400\,\text{J}$ and would have got $800\,\text{J}$ — his extra travel buys far more than he thought, which is good news for the kerb and bad news for whoever has to sit on the rebound.

**Sanity check:** $200\,\text{J}$ is roughly the work of lifting a $20\,\text{kg}$ wheel and tyre a metre off the ground. A spring that can absorb a wheel-drop of about that size sounds like the right order for a kerb hit.

## Where the picture breaks

A real suspension spring is not the whole story, and treating it as one would make a car undriveable. All the energy a conservative spring takes in, it gives straight back — so a car with springs alone would bounce off that kerb and keep bouncing. The damper beside the spring exists precisely to be **non-conservative**: it forces oil through small holes and turns the motion into heat, which is why the car settles. Real springs are also only linear over part of their travel; bump stops deliberately stiffen towards the end, so $U = \tfrac{1}{2}kx^2$ underestimates the last centimetre. And the tyre itself is a spring, a fairly stiff one, sitting in series with the coil — the bang Omkar can hear is the two of them running out of room together.

## Key takeaway

An ideal spring obeys $F = -kx$, and the energy stored in it is the triangular area under that line, $U = \tfrac{1}{2}kx^2$ — the same for a stretch or a squash. Because the displacement is squared, doubling the compression quadruples the energy. The spring force is conservative, so this term joins $mgh$ in any energy accounting.
