---
concept_id: drift_velocity
interest: cricket
format: explain
title: The electrons in the scoreboard cable crawl slower than a walked single
check:
  question: |-
    A copper cable feeding a scoreboard is replaced by one of the same material carrying the same current, but with **twice** the cross-sectional area. The drift velocity of the electrons in it becomes:
  options:
    A: |-
      twice as large
    B: |-
      unchanged — drift velocity depends only on the metal
    C: |-
      half as large
    D: |-
      a quarter as large
  answer: C
  explanation: |-
    From $I = neAv_d$, with $I$, $n$ and $e$ fixed, $v_d$ is inversely proportional to $A$. Doubling the area halves the drift velocity: the same charge per second is shared over a wider cross-section, so each electron needs to creep more slowly.
  misconceptions:
    A: |-
      Reads $I = neAv_d$ as if $v_d$ grew with $A$. They are on the same side of the equation, so with $I$ fixed one must fall when the other rises.
    B: |-
      Confuses drift velocity with the random thermal speed of the electrons, which does depend only on the metal and temperature. Drift velocity is set by the current and the wire's geometry.
    D: |-
      Treats the area as if it entered squared, perhaps by also changing the radius. $I = neAv_d$ contains the area itself, to the first power.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A cricket ground at dusk with floodlights, an electronic scoreboard, glowing stumps and an umpire holding a light meter](scenes/cricket/current_electricity.svg "The scoreboard is at one end of the ground and its power cable runs all the way from the pavilion.")

Ayesha keeps the scorebook for her school's first XI, in a little box at square leg with a switch panel wired to the electronic board across the ground. A boundary is hit; she presses the button; the total jumps from 84 to 88 before the ball has finished rolling.

In physics class the next morning, her teacher says something that sounds like a joke: the electrons carrying that signal move through the cable slower than a fielder strolling in. Slower, in fact, than a batter walking a single. A tenth of a millimetre a second, roughly.

Ayesha does the arithmetic in the margin of her book. At that speed an electron would need nearly two full days to travel the length of the pitch. The scoreboard changed in an instant.

Both things can't be true — and yet both are. So what exactly is crawling, and what is arriving instantly?

## The physics

Inside a metal, free electrons are already flying about at enormous random speeds, of order $10^5\,\text{m/s}$, bouncing off the vibrating metal ions. That motion is random: as much one way as the other, so it carries no net charge anywhere.

Switch on a cell and an electric field $\vec{E}$ appears inside the wire, along its whole length, almost at once (at nearly the speed of light). Between one collision and the next, each electron is accelerated slightly backwards along the field — it is negative — and every collision wipes that gain out. The result is a tiny steady average velocity superposed on the random motion. This average is the **drift velocity** $v_d$.

![An electron's fast zigzag path between collisions inside a wire, with a small steady net drift opposite to the electric field](figures/drift_velocity/drift-velocity-zigzag.svg "The zigzag is fast and random; the slow sideways creep it adds up to is the drift velocity.")

**Mobility** $\mu$ measures how much drift you get per unit field:

$$\mu = \frac{v_d}{E}$$

with units $\text{m}^2\,\text{V}^{-1}\text{s}^{-1}$.

Now the relation that ties drift to current. Let the wire have cross-sectional area $A$ and $n$ free electrons per unit volume, each of charge magnitude $e$. In a time $t$, every electron within a distance $v_d t$ of a chosen cross-section gets through it. That slab has volume $A v_d t$, so it contains $n A v_d t$ electrons, carrying a charge

$$Q = n e A v_d t$$

Divide by $t$, using $I = Q/t$:

$$\boxed{I = n e A v_d}$$

This holds for a metallic conductor with a uniform cross-section and a steady current. And it answers Ayesha: what travels near light speed is the *field*, which starts every electron all along the cable moving together. The electrons themselves only creep.

## Worked example

**Given:** a scoreboard cable of cross-section $A = 1.0\,\text{mm}^2$ carrying $I = 2.0\,\text{A}$, in a metal with about $n = 1.0 \times 10^{29}$ free electrons per cubic metre (illustrative, but the right size for copper). Take $e = 1.6 \times 10^{-19}\,\text{C}$.
**Find:** the drift velocity.

Convert the area first: $1.0\,\text{mm}^2 = 1.0 \times 10^{-6}\,\text{m}^2$.

Rearrange $I = neAv_d$:

$$v_d = \frac{I}{neA} = \frac{2.0}{(1.0 \times 10^{29})(1.6 \times 10^{-19})(1.0 \times 10^{-6})}$$

The denominator is $1.6 \times 10^{4}$ — that is the charge, in coulombs, contained in a one-metre length of this cable. So the drift velocity is

$$v_d = 1.25 \times 10^{-4}\,\text{m/s} \approx 0.13\,\text{mm/s}$$

About a millimetre every eight seconds: an electron would take some **40 hours** to cover the 22 yards of a pitch.

**Sanity check:** a wire holds a huge amount of free charge, so a modest current needs only a crawl — a tiny speed is exactly what we should expect.

## Where the picture breaks

The word "velocity" oversells it: $v_d$ is an average over a wildly random motion, not the speed of any particular electron. Nothing here is a cricketing analogy, and it shouldn't be — fielders run one at a time along a path you can see, while the current is set by a whole population creeping together. Also, $n$ is not a free choice: for a given metal it is fixed by its atoms. And in a semiconductor both electrons and positive holes carry the current, so $I = neAv_d$ needs a second term — that comes later.

## Key takeaway

An electric field inside a wire gives the randomly moving free electrons a tiny average velocity, the drift velocity $v_d$, with mobility $\mu = v_d/E$. Counting the charge that crosses a cross-section gives $I = neAv_d$. The drift is slower than a walking pace; the light comes on instantly because the field, not the electrons, travels the length of the wire.
