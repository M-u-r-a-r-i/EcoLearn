---
concept_id: universal_gravitation
interest: gaming
format: explain
title: The mod that made every crate pull every other crate
check:
  question: |-
    Two identical crates, each of mass $1000\,\text{kg}$, stand with their centres $2\,\text{m}$ apart. Taking $G = 6.67 \times 10^{-11}\,\text{N m}^2/\text{kg}^2$, what is the gravitational force between them?
  options:
    A: |-
      $3.3 \times 10^{-5}\,\text{N}$
    B: |-
      $3.3 \times 10^{-8}\,\text{N}$
    C: |-
      $1.7 \times 10^{-5}\,\text{N}$
    D: |-
      $1.7 \times 10^{-11}\,\text{N}$
  answer: C
  explanation: |-
    $F = Gm_1m_2/r^2 = 6.67 \times 10^{-11} \times 1000 \times 1000 / (2)^2 = 6.67 \times 10^{-5}/4 \approx 1.7 \times 10^{-5}\,\text{N}$.
  misconceptions:
    A: |-
      Divides by $r$ instead of $r^2$, missing the inverse-square dependence on distance.
    B: |-
      Adds the two masses instead of multiplying them; the force is proportional to the product $m_1 m_2$, not to the total mass.
    D: |-
      Puts the masses in tonnes instead of kilograms, a unit slip that makes the answer a million times too small.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A gaming desk at night: a monitor runs an orbit simulator with a planet and a ship, and a tablet shows a satellite above a planet](scenes/gaming/gravitation.svg "The same one-line rule pulls the ship towards the planet and the player towards the floor.")

Ritika is building a physics mod for a sandbox game. Her ambition is stated in the readme: *every object attracts every other object*. Not a downward push, not a special case for the ground — one universal rule, applied to every pair in the level.

She writes it, compiles it, and loads a test map: a flat floor, frictionless, with two steel crates standing a couple of metres apart. Her flatmate Joydeep is watching over her shoulder.

Nothing happens. The crates sit there.

"So it doesn't work," says Joydeep.

Ritika drops a barrel from the ceiling. It falls, exactly as it should, and lands on the floor with a thud. "It works fine. The planet is pulling the barrel."

"Then why won't the crates budge? They're a tonne each."

Ritika opens the console and prints the force her own code computed between the two crates. She goes quiet when she sees the number. How small is the pull between two crates, and why does a whole planet win so completely?

## The physics

**Newton's law of universal gravitation:** every particle in the universe attracts every other particle with a force proportional to the product of their masses and inversely proportional to the square of the distance between them:

$$F = \frac{G\,m_1 m_2}{r^2}$$

- $m_1$ and $m_2$ are the masses in $\text{kg}$, and $r$ is the distance between them in $\text{m}$. For uniform spheres, $r$ is measured **centre to centre**, and each sphere pulls as though all its mass sat at its centre.
- $G = 6.67 \times 10^{-11}\,\text{N m}^2/\text{kg}^2$ is the **universal gravitational constant** — the same value for every pair of masses anywhere.
- The force is always **attractive** and acts **along the line joining the two centres**.
- The two forces are a **Newton's third law pair**: the crate pulls the planet exactly as hard as the planet pulls the crate. The planet simply has far too much mass to be moved noticeably.

![Two spheres pulling each other with equal and opposite red arrows; below, bars show the pull falling to a quarter at twice the distance and a ninth at three times](figures/universal_gravitation/force-pair-inverse-square.svg "The two pulls are equal and opposite. Double the separation and the force drops to a quarter; triple it and it drops to a ninth.")

The reason Ritika's mod *feels* like it only does gravity-down is the size of $G$. It is a very small number, so the product $m_1m_2$ has to be enormous before the force is worth noticing — and only a planet-sized mass can do that.

Newton published this law in 1687 in the *Principia*, and used the one rule to explain both a falling body and the Moon's orbit.

![The Latin title page of Newton's Principia Mathematica, printed in London in 1687](famous/newton-principia-title-page.jpg "Newton set out universal gravitation in the Principia (1687). Public domain, via Wikimedia Commons.")

## Worked example

**Given:** two crates, each $m = 1000\,\text{kg}$, centres $r = 10\,\text{m}$ apart; $G = 6.67 \times 10^{-11}\,\text{N m}^2/\text{kg}^2$; take $g = 9.8\,\text{m/s}^2$ at the planet's surface.
**Find:** (a) the pull between the crates; (b) the planet's pull on one crate, and the ratio of the two.

(a) Substituting into the law:

$$F = \frac{6.67 \times 10^{-11} \times 1000 \times 1000}{(10)^2} = \frac{6.67 \times 10^{-5}}{100} \approx 6.7 \times 10^{-7}\,\text{N}$$

That is the weight of about a tenth of a milligram — a speck too small to see. Any friction at all, and the crates never move.

(b) The planet's pull on the same crate is its weight:

$$F = mg = 1000 \times 9.8 = 9800\,\text{N}$$

which is about $10^{10}$ times larger.

**Sanity check:** the weight also comes out of the same law, $GMm/R^2$, using the planet's mass and radius — one rule, two very different answers, because one of the masses is a planet.

## Where the picture breaks

A game crate is a hollow box, not a uniform sphere, so the centre-to-centre shortcut is only approximate for it; the shortcut is exact only for spherically symmetric bodies. Ritika's mod also has a practical problem her readme didn't foresee: applying the law to every pair means the work grows as the square of the number of objects, so a level with thousands of items would stall. Real engines cheat, and apply a single constant downward $g$ instead — which is a good approximation near the surface, and completely wrong once you leave it.

Nothing here says the crates *don't* attract. They do, exactly as computed. Measuring a force that small in the real world needs a torsion balance in a sealed room.

## Key takeaway

Every pair of masses attracts along the line joining their centres with $F = Gm_1m_2/r^2$, equal and opposite on the two bodies. Because $G$ is tiny, the pull only matters when one of the masses is astronomically large. Two one-tonne crates ten metres apart pull each other with under a millionth of a newton; the planet pulls each of them with about $9800\,\text{N}$.
