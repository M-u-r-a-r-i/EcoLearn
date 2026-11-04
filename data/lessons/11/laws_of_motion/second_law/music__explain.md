---
concept_id: second_law
interest: music
format: explain
title: Why tweeters are tiny and woofers are big
check:
  question: |-
    A drummer swings a light stick ($40\,\text{g}$) and a heavy stick ($80\,\text{g}$) with the same net force. Compared with the light stick, the heavy stick's acceleration is:
  options:
    A: |-
      Twice as large, because a heavier stick has more power behind it
    B: |-
      Half as large
    C: |-
      The same, because the force is the same
    D: |-
      A quarter as large
  answer: B
  explanation: |-
    With the same net force, $a = F/m$. Doubling the mass halves the acceleration.
  misconceptions:
    A: |-
      Thinks extra mass adds to the motion, when mass actually resists changes in motion.
    C: |-
      Thinks acceleration is set by the force alone, ignoring the mass being accelerated.
    D: |-
      Assumes acceleration depends on the square of the mass; the relation $a = F/m$ is a simple inverse proportion.
author: claude-code/opus-5
written: 2026-09-21
---
## The story

![A concert stage with a speaker cabinet showing a big woofer and a small tweeter, a drum kit, and a roadie](scenes/music/laws_of_motion.svg "Every speaker cabinet hides a physics decision: which cone plays which notes.")

Diya's band has its first real gig, and during the sound check she wanders over to the speaker stack. The sound engineer has taken the front grille off one cabinet, and inside are two very different circles: a big, heavy cone as wide as a dinner plate, and above it a tiny dome no bigger than a coin.

"The big one's the woofer — it does the bass," the engineer says. "The little one's the tweeter. It does the cymbals and the high notes."

Diya frowns. The same amplifier drives both. Surely the big, powerful cone should handle everything, and the tiny one looks almost like decoration. Why would anyone hand the hardest, fastest job — high notes, where the cone must flip back and forth thousands of times a second — to the smallest, weakest-looking part?

The answer is Newton's second law.

Here's how both drivers work: the music signal flows as a current through a coil sitting next to a magnet, the magnetic force pushes the coil and the cone attached to it back and forth, and the moving cone pushes the air to make sound.

## The physics

Newton's second law says the **net force** on a body equals the rate of change of its **momentum**:

$$\vec{F}_\text{net} = \frac{d\vec{p}}{dt}$$

For a body of constant mass — like a speaker cone — this becomes

$$\vec{F}_\text{net} = m\vec{a}, \qquad a = \frac{F_\text{net}}{m}$$

The acceleration is in the direction of the net force, and for a given force it is **inversely proportional to the mass**. Mass measures how strongly a body resists having its motion changed.

Making a high note means changing the cone's velocity — forwards, stop, backwards, stop — very rapidly, which needs large accelerations. For a given driving force, the lighter the cone, the larger the acceleration it can reach. So the lightest cone gets the fastest job. The heavy woofer can't be pushed back and forth fast enough to follow high notes well, but it moves a lot of air slowly — exactly what bass needs.

![Two graphs: at fixed mass, acceleration rises in a straight line with force; at fixed force, acceleration falls along a curve as mass increases](figures/second_law/force-mass-acceleration.svg "The right-hand graph is the speaker's story: for the same force, a lighter cone gets a larger acceleration.")

The SI unit of force follows from the law: $1\,\text{N} = 1\,\text{kg}\,\text{m/s}^2$, named after Isaac Newton, who published the law in 1687 in his *Principia*.

![The Latin title page of Newton's Principia Mathematica, printed in London in 1687](famous/newton-principia-title-page.jpg "Newton stated his three laws of motion in the Principia (1687). Public domain, via Wikimedia Commons.")

## Worked example

**Given:** a tweeter dome of mass about $0.5\,\text{g}$ and a woofer cone of about $25\,\text{g}$ (illustrative values), each driven by the same net force of $2.0\,\text{N}$.
**Find:** the acceleration of each.

Convert to kilograms first: $0.5\,\text{g} = 5.0 \times 10^{-4}\,\text{kg}$ and $25\,\text{g} = 2.5 \times 10^{-2}\,\text{kg}$.

$$a_\text{tweeter} = \frac{F}{m} = \frac{2.0}{5.0 \times 10^{-4}} = 4.0 \times 10^{3}\,\text{m/s}^2$$

$$a_\text{woofer} = \frac{F}{m} = \frac{2.0}{2.5 \times 10^{-2}} = 80\,\text{m/s}^2$$

The same force gives the tweeter $50$ times the acceleration — exactly the mass ratio, $25/0.5 = 50$.

**Sanity check:** $a \propto 1/m$, so a mass $50$ times smaller should give an acceleration $50$ times larger: $80 \times 50 = 4000$. ✓

## Where the picture breaks

A real speaker cone isn't a free object: it's held by a springy suspension, it has to push air (which pushes back), and the driving force changes all the time as the signal changes. So "same force, compare accelerations" is a simplified snapshot, not a full model of a speaker — you'll need oscillations to describe it properly. How good a speaker sounds also depends on its magnet, its shape and the cabinet, not just its mass. But the core reason tweeters are light is exactly $a = F/m$.

## Key takeaway

The net force on a body equals its rate of change of momentum; for constant mass, $\vec{F}_\text{net} = m\vec{a}$. The same force gives a lighter object a larger acceleration — which is why the smallest, lightest driver in a speaker plays the highest notes.
