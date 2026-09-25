---
concept_id: work_variable_force
interest: smartphones
format: explain
title: The energy in one key press
check:
  question: |-
    A robot vacuum nudges a floor cushion along in a straight line. Its push along the motion is a steady $6.0\,\text{N}$ for the first $2.0\,\text{m}$, then falls steadily to zero over the next $2.0\,\text{m}$ as the cushion slides off to one side. How much work does the vacuum do on the cushion over the whole $4.0\,\text{m}$?
  options:
    A: |-
      $18\,\text{J}$
    B: |-
      $24\,\text{J}$
    C: |-
      $12\,\text{J}$
    D: |-
      $6.0\,\text{J}$
  answer: A
  explanation: |-
    Work is the area under the force–displacement graph: a rectangle $6.0 \times 2.0 = 12\,\text{J}$ plus a triangle $\tfrac{1}{2} \times 2.0 \times 6.0 = 6.0\,\text{J}$, so $W = 18\,\text{J}$.
  misconceptions:
    B: |-
      Multiplies the largest force by the whole distance, $6.0 \times 4.0$, as if the force stayed at $6.0\,\text{N}$ all the way. When the force changes, you must add up force times width strip by strip — the area.
    C: |-
      Counts only the rectangle, as if a force that is dying away does no work. While it still points along the motion it does positive work: the triangle counts too.
    D: |-
      Counts only the triangle, the part where the force changes, and forgets the constant-force part before it. The work is the whole area from start to finish.
author: claude-code/opus-5
written: 2026-09-25
---
## The story

![A living room in the evening: a camera drone climbs straight up, a phone falls from a shelf towards a cushion, an earbuds case is whirled on a lanyard in a vertical circle, and a robot vacuum rolls towards a sofa leg](scenes/smartphones/work_energy_power.svg "Not every push in this room is steady. The robot vacuum's bumper, for one, pushes harder the more it is squashed.")

Tanvi has bought a mechanical keyboard to plug into her tablet, and she has become that person who reads datasheets. The box came with a graph for its switches: a line showing how hard you must press, plotted against how far down the key has travelled.

"Look — it's about a third of a newton when you start pressing, and more than double that at the bottom," she tells her friend Aman. "The spring gets stiffer as the key goes down."

Aman is unimpressed. "Great. So how much energy does one key press take? You can't just do force times distance if the force keeps changing."

Tanvi opens her typing app: ten thousand keystrokes this evening, it says. Is that a lot of energy, or next to none? And how do you even work out the work when the force won't stay still?

## The physics

For a constant force along the motion, $W = Fd$ — on a force–displacement graph, a rectangle of height $F$ and width $d$. When the force **varies** with position, split the motion into narrow strips of width $\Delta x$. Over each strip the force is nearly constant, so that strip's work is $F\,\Delta x$: a thin rectangle. Adding the strips and making them ever thinner gives

$$W = \int_{x_i}^{x_f} F(x)\,dx = \text{area under the } F\text{–}x \text{ graph}$$

(taking $F$ as the component along the displacement). Area above the axis is positive work; area below it is negative work.

![A force–displacement graph: the force rises from zero, runs flat across the middle, then falls back to zero; dashed strips of equal width approximate the area under the line](figures/work_variable_force/area-under-force-displacement.svg "The work is the area under the red line. The strips show the method: force times width, strip by strip, added up. This graph is a general example — for a key press the line is a straight slope instead.")

For straight-line graphs you don't need calculus at all: break the area into rectangles and triangles. A key switch's graph is a sloping straight line, so its area is a **trapezium**.

## Worked example

**Given:** the key needs $0.30\,\text{N}$ at the top of its travel, rising steadily to $0.70\,\text{N}$ at the bottom; the travel is $4.0\,\text{mm} = 0.0040\,\text{m}$ (illustrative, typical of such switches).
**Find:** the work done by your finger in one press, and in $10\,000$ presses.

1. *The shape:* a trapezium with parallel sides $0.30\,\text{N}$ and $0.70\,\text{N}$, width $0.0040\,\text{m}$.
2. *Its area:* $W = \tfrac{1}{2}(0.30 + 0.70) \times 0.0040 = 0.50 \times 0.0040 = 0.0020\,\text{J}$. That is the same as a steady $0.50\,\text{N}$ — the average force, because the line is straight — pushed through $4\,\text{mm}$.
3. *An evening's typing:* $10\,000 \times 0.0020 = 20\,\text{J}$.

Twenty joules is about the work of lifting a $2\,\text{kg}$ bag of rice from the floor onto a table one metre up — once. An evening of typing costs your fingers almost nothing.

**Sanity check:** pressing a key feels effortless, so a few thousandths of a joule per press is the right size.

## Where the picture breaks

The keyboard is a real device, not an analogy, but we simplified its graph. Many switches have a bump — the force rises, drops suddenly at the "click", then rises again — and the area still gives the work, just with a more awkward shape. The spring also pushes the key back up as you let go, so much of that $0.0020\,\text{J}$ is returned to your finger rather than lost; what you do lose goes into the sound and warmth of the click. And your muscles use far more than $20\,\text{J}$ of food energy to type, because muscles are not efficient machines.

## Key takeaway

When a force changes along the way, the work it does is the **area under its force–displacement graph**, $W = \int F\,dx$. For straight-line graphs, split the area into rectangles, triangles and trapeziums.
