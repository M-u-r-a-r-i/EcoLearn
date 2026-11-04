---
concept_id: collisions
interest: cricket
format: explain
title: When two fielders go for the same catch
check:
  question: |-
    On a smooth indoor-nets floor, a ball sliding at $20\,\text{m/s}$ hits an identical ball at rest, head-on. Treat the collision as perfectly elastic and ignore any rolling. What happens just after the collision?
  options:
    A: |-
      The first ball stops, and the second moves off at $20\,\text{m/s}$.
    B: |-
      Both balls move forwards together at $10\,\text{m/s}$.
    C: |-
      The first ball bounces straight back at $20\,\text{m/s}$, and the second stays at rest.
    D: |-
      Both balls move forwards at about $14.1\,\text{m/s}$.
  answer: A
  explanation: |-
    For an elastic collision with the second body at rest, $v_1 = \dfrac{(m_1 - m_2)u_1}{m_1 + m_2} = 0$ and $v_2 = \dfrac{2m_1u_1}{m_1 + m_2} = u_1$ when $m_1 = m_2$. Equal masses simply swap velocities, conserving both momentum and kinetic energy.
  misconceptions:
    B: |-
      Conserves momentum but not kinetic energy: moving off together at $10\,\text{m/s}$ is a perfectly inelastic collision, which loses half the kinetic energy.
    C: |-
      Treats the second ball like a fixed wall; that would reverse the total momentum, which is impossible without an outside force.
    D: |-
      Shares the kinetic energy equally between the balls; that total momentum, $2 \times 14.1m \approx 28m$, is more than the $20m$ at the start, so momentum would not be conserved.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A cricket ground by day: a batter watches a ball climb high, a fielder waits under it, a player runs up the stadium steps and a groundsman pushes a roller](scenes/cricket/work_energy_power.svg "A high catch, two fielders, one ball. Nobody is calling for it.")

The ball goes up off a leading edge, high towards the gap between cover and mid-off. Ananya sprints in from the cover boundary. Sameer races across from mid-off. Both have their eyes on the ball, and nobody calls.

They arrive at the same spot at the same moment, running at right angles to each other. They collide, grab each other, and tumble together across the grass. The ball lands softly between them.

They get up laughing, grass-stained. That evening the coach replays the clip in slow motion. "Look at the direction you two slid off in. Neither of you was going that way."

Ananya is curious. Could they have predicted the direction and speed of that tangled slide? And they were both sprinting hard before they hit, yet they barely slid at all afterwards. Where did all that energy go?

## The physics

In a **collision**, two bodies exert large forces on each other for a short time. Any outside forces, like gravity or friction from the ground, are small by comparison and act only briefly. So the colliding pair is effectively an isolated system, and **total momentum is conserved in every collision**:

$$m_1\vec{u}_1 + m_2\vec{u}_2 = m_1\vec{v}_1 + m_2\vec{v}_2$$

Kinetic energy is another matter. Collisions are classified by what happens to it:

- **Elastic:** total kinetic energy is the same before and after.
- **Inelastic:** some kinetic energy becomes heat, sound or deformation, so the total decreases.
- **Perfectly inelastic:** the bodies stick together and move with one common velocity. This loses the most kinetic energy that momentum conservation allows.

**Elastic collisions in one dimension.** If $m_2$ is initially at rest, conserving both momentum and kinetic energy gives

$$v_1 = \frac{(m_1 - m_2)\,u_1}{m_1 + m_2} \qquad v_2 = \frac{2m_1\,u_1}{m_1 + m_2}$$

For equal masses, $v_1 = 0$ and $v_2 = u_1$: the bodies **swap velocities**. If a light body hits a much heavier one ($m_1 \ll m_2$), it bounces back with nearly its original speed. If a heavy body hits a light one, the light one shoots off at nearly $2u_1$.

**Collisions in two dimensions.** Momentum is a vector, so it is conserved separately in each direction: total $p_x$ before equals total $p_x$ after, and the same for $p_y$. Ananya and Sameer's collision is perfectly inelastic and two-dimensional.

![Top: two equal balls in an elastic head-on collision swap velocities. Bottom: two bodies moving at right angles stick together, and the combined momentum is the vector sum of the two momenta](figures/collisions/one-d-and-two-d.svg "In one dimension, equal masses swap velocities in an elastic collision. In two dimensions, add the momenta as vectors to find where a stuck-together pair goes.")

## Worked example

**Given** (illustrative): Ananya, $m_1 = 60\,\text{kg}$, running east at $6.0\,\text{m/s}$; Sameer, $m_2 = 70\,\text{kg}$, running north at $5.0\,\text{m/s}$. They move off together.
**Find:** their common velocity, and the kinetic energy lost.

Take east as $+x$ and north as $+y$.

$$p_x = 60 \times 6.0 = 360\,\text{kg m/s} \qquad p_y = 70 \times 5.0 = 350\,\text{kg m/s}$$

Total mass $130\,\text{kg}$, so

$$V = \frac{\sqrt{360^2 + 350^2}}{130} = \frac{\sqrt{252\,100}}{130} = \frac{502}{130} \approx 3.9\,\text{m/s}$$

$$\tan\theta = \frac{350}{360} = 0.972 \quad\Rightarrow\quad \theta \approx 44^\circ \text{ north of east}$$

Kinetic energy before: $\tfrac{1}{2}(60)(6.0)^2 + \tfrac{1}{2}(70)(5.0)^2 = 1080 + 875 = 1955\,\text{J}$.

Kinetic energy after: $\tfrac{1}{2}(130)(3.86)^2 \approx 65 \times 14.9 \approx 970\,\text{J}$.

About $985\,\text{J}$ — half the energy — went into squashing, heat and sound in that tangle. That's why they barely slid.

**Sanity check:** the direction lies between east and north, and is tilted slightly towards east because Ananya's momentum was a little larger. A common speed smaller than either runner's speed makes sense, because the momenta partly point different ways.

## Where the picture breaks

People aren't rigid balls. They twist, brace and grab, so "sticking together" is only a rough description of the first instant. Friction from the grass is an outside force: it is small during the brief impact, which is why momentum conservation works there, but it stops them within a metre or two afterwards. And real fielding collisions can cause injuries, which is exactly why fielders are coached to call loudly for every catch.

## Key takeaway

Momentum is conserved in every collision; kinetic energy is conserved only in elastic ones. In one dimension, an elastic collision between equal masses swaps their velocities. In two dimensions, conserve $p_x$ and $p_y$ separately. When bodies stick together, their common velocity is the total momentum divided by the total mass.
