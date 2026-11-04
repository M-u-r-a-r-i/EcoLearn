---
concept_id: collisions
interest: football
format: explain
title: Why a hard shot doesn't knock the diving keeper back
check:
  question: |-
    In a gym drill, a $0.45\,\text{kg}$ football moving at $20\,\text{m/s}$ hits a $4.5\,\text{kg}$ medicine ball at rest, head-on, on a smooth floor. Treat the collision as perfectly elastic and ignore rolling. What is the football's velocity just after the collision?
  options:
    A: |-
      $0\,\text{m/s}$: it stops dead and the medicine ball moves off at $20\,\text{m/s}$.
    B: |-
      About $16.4\,\text{m/s}$, bouncing straight back.
    C: |-
      $20\,\text{m/s}$, bouncing straight back, with the medicine ball staying at rest.
    D: |-
      About $1.8\,\text{m/s}$ forwards, moving together with the medicine ball.
  answer: B
  explanation: |-
    For an elastic collision with $m_2$ at rest, $v_1 = \dfrac{(m_1 - m_2)u_1}{m_1 + m_2} = \dfrac{(0.45 - 4.5) \times 20}{4.95} \approx -16.4\,\text{m/s}$. The minus sign means it bounces back; the medicine ball moves off at $\dfrac{2m_1u_1}{m_1 + m_2} \approx 3.6\,\text{m/s}$.
  misconceptions:
    A: |-
      Applies the equal-mass result (the bodies swap velocities) to unequal masses; that only happens when $m_1 = m_2$.
    C: |-
      Treats the medicine ball like an immovable wall; any free body that is hit must move off, or the total momentum would change with no outside force.
    D: |-
      Uses the perfectly inelastic (stick-together) result; that conserves momentum but loses most of the kinetic energy, which an elastic collision does not.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A football training ground by day: a player drags a weighted sled on a strap, a striker lofts the ball in a high arc, and the goalkeeper dives to catch it](scenes/football/work_energy_power.svg "On the right, the keeper is in mid-air, flying sideways, just as the ball arrives.")

Shooting practice, last drill of the evening. Salman, the academy's hardest striker, hits one low and fierce towards the far corner. Gurpreet, in goal, launches himself sideways, fully airborne, and the ball smacks into his gloves. He clutches it to his chest and lands, still flying along the line in almost the same direction he dived.

Salman can't believe it. "That shot was around $90\,\text{km/h}$! It should have knocked you straight into the net."

Gurpreet grins from the grass. "It barely moved me."

The goalkeeping coach, Mrs D'Souza, replays the clip in slow motion. The ball was going towards the goal; Gurpreet was flying across it. After the catch they moved as one, in a direction almost exactly along his dive.

Why did such a fast shot hardly change his path? And the ball's energy clearly didn't survive the catch. Where did it go?

## The physics

In a **collision**, two bodies push on each other with large forces for a short time. Outside forces, like gravity or friction, are small by comparison and act only briefly, so the pair is effectively an isolated system. **Total momentum is conserved in every collision**:

$$m_1\vec{u}_1 + m_2\vec{u}_2 = m_1\vec{v}_1 + m_2\vec{v}_2$$

Kinetic energy is another matter. Collisions are classified by what happens to it:

- **Elastic:** total kinetic energy is the same before and after.
- **Inelastic:** some kinetic energy becomes heat, sound or deformation.
- **Perfectly inelastic:** the bodies stick together and share one velocity. This loses the most kinetic energy that momentum conservation allows.

**Elastic collisions in one dimension.** If $m_2$ is initially at rest, conserving both momentum and kinetic energy gives

$$v_1 = \frac{(m_1 - m_2)\,u_1}{m_1 + m_2} \qquad v_2 = \frac{2m_1\,u_1}{m_1 + m_2}$$

Equal masses **swap velocities**. A light body hitting a much heavier one bounces back with nearly its original speed, like a ball off a goalpost.

**Collisions in two dimensions.** Momentum is a vector, so it is conserved separately in each direction: total $p_x$ before equals total $p_x$ after, and the same for $p_y$. Gurpreet's catch is perfectly inelastic and two-dimensional. Because he is in mid-air, no friction from the ground acts on him during the catch.

![Top: two equal balls in an elastic head-on collision swap velocities. Bottom: two bodies moving at right angles stick together, and the combined momentum is the vector sum of the two momenta](figures/collisions/one-d-and-two-d.svg "In two dimensions, add the momenta as vectors. The pair moves off along the total, tilted towards the bigger momentum.")

## Worked example

**Given** (illustrative): ball $m_1 = 0.43\,\text{kg}$ moving towards the goal at $25\,\text{m/s}$ ($90\,\text{km/h}$); Gurpreet $m_2 = 75\,\text{kg}$ flying along the goal line at $3.0\,\text{m/s}$. Take $+x$ towards the goal and $+y$ along his dive. They move off together.
**Find:** the common velocity, and the kinetic energy lost.

$$p_x = 0.43 \times 25 = 10.75\,\text{kg m/s} \qquad p_y = 75 \times 3.0 = 225\,\text{kg m/s}$$

Total mass $75.43\,\text{kg}$:

$$V = \frac{\sqrt{10.75^2 + 225^2}}{75.43} = \frac{225.3}{75.43} \approx 2.99\,\text{m/s}$$

$$\tan\phi = \frac{10.75}{225} \approx 0.048 \quad\Rightarrow\quad \phi \approx 2.7^\circ \text{ from his dive, towards the goal}$$

Gurpreet's momentum was about 20 times the ball's, so the ball tilted his path by less than $3^\circ$.

Kinetic energy before: $\tfrac{1}{2}(0.43)(25)^2 + \tfrac{1}{2}(75)(3.0)^2 = 134.4 + 337.5 \approx 472\,\text{J}$.
After: $\tfrac{1}{2}(75.43)(2.99)^2 \approx 336\,\text{J}$.

About $136\,\text{J}$, roughly all the energy the ball brought in, went into squashing the ball and gloves, bending Gurpreet's wrists, heat and the smack of the catch.

**Sanity check:** the common velocity lies between the two original directions and very close to the keeper's, as it should for such unequal momenta. And $2.99\,\text{m/s}$ is just below his $3.0\,\text{m/s}$, since he now carries the extra mass of the ball.

## Where the picture breaks

A keeper isn't a rigid block. His arms give as he catches, which spreads the impact over a longer time, gentler on the wrists but with the same total momentum change. Gravity acts throughout his dive; it doesn't change the horizontal momentum, but it does bring him down. The ball also spins, and a real shot may dip or swerve before arriving. None of that changes the key result: momentum is shared, while kinetic energy is not conserved in a catch.

## Key takeaway

Momentum is conserved in every collision; kinetic energy is conserved only in elastic ones. In one dimension, an elastic collision between equal masses swaps their velocities. In two dimensions, conserve $p_x$ and $p_y$ separately. When bodies stick together, their common velocity is the total momentum divided by the total mass.
