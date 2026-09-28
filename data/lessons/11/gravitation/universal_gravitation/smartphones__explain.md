---
concept_id: universal_gravitation
interest: smartphones
format: explain
title: Why two phones on a desk never drift together
check:
  question: |-
    Two phones lying on a table attract each other with a gravitational force $F$. One phone is swapped for a tablet with **twice** its mass, and the two are moved to **twice** the distance apart (centre to centre). What is the new force between them?
  options:
    A: |-
      $F$
    B: |-
      $2F$
    C: |-
      $F/2$
    D: |-
      $F/4$
  answer: C
  explanation: |-
    $F \propto m_1 m_2 / r^2$. Doubling one mass doubles the force; doubling the distance divides it by $2^2 = 4$. Together: $2/4 = 1/2$, so the new force is $F/2$.
  misconceptions:
    A: |-
      Treats the force as falling in simple proportion to distance, so doubling the mass and doubling the distance seem to cancel; the force falls as $1/r^2$, not $1/r$.
    B: |-
      Accounts for the heavier tablet but ignores the change in distance, as if the gravitational pull did not weaken as the objects move apart.
    D: |-
      Applies the inverse-square law but forgets that the force also depends on the tablet's mass; the pull depends on both masses, not only on the distance.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A city rooftop at night: a fixed satellite dish, moving navigation satellites, a weather balloon rising with a phone, and a phone and tablet on a table showing a sky plot and a weather image](scenes/smartphones/gravitation.svg "The phone and tablet on the table pull on each other. So does the Earth pull on both, and the Moon on all three.")

It's the last period, the physics teacher is late, and Nisha has just read the line in her textbook: *every particle in the universe attracts every other particle*.

She puts her phone down on the desk, then slides Kabir's phone next to it, a hand's width away.

"So these two are pulling on each other. Right now."

"Obviously not," says Kabir. "Leave them there all day and they won't move a millimetre. If they attracted each other, they'd slide together like two magnets."

"The book says *every* particle."

"Then the book is talking about planets, not phones."

Nisha nudges the phones even closer. Nothing happens. Either the textbook is wrong, or the pull is there and something is hiding it. Which is it, and how big is this pull?

## The physics

**Newton's law of universal gravitation:** any two point masses $m_1$ and $m_2$, a distance $r$ apart, attract each other with a force along the line joining them, of size

$$F = \frac{G\,m_1 m_2}{r^2}$$

where $G = 6.67 \times 10^{-11}\,\text{N m}^2/\text{kg}^2$ is the **universal gravitational constant**. The word *universal* matters: the same $G$ works for two phones, the Earth and a phone, and the Sun and a planet.

- The force is always **attractive**.
- It obeys Newton's third law: the pull of phone 1 on phone 2 is **equal and opposite** to the pull of phone 2 on phone 1, even if one is far heavier.
- It is an **inverse-square law**: double the distance and the force drops to a quarter.
- For uniform spheres, $r$ is measured between the **centres**. For phones, which are not spheres, treating each as a point mass is only an estimate.

![Two spheres pulling each other with equal and opposite red arrows; below, bars show the pull falling to a quarter at twice the distance and a ninth at three times](figures/universal_gravitation/force-pair-inverse-square.svg "The pulls on the two masses are equal and opposite. Double the distance and the pull drops to a quarter; triple it and it drops to a ninth.")

So Nisha is right: her phone and Kabir's are attracting each other. The question is only whether the pull is big enough to notice. The tiny size of $G$ is the clue.

## Worked example

**Given:** two phones of mass $m = 0.2\,\text{kg}$ each (illustrative), with centres $r = 0.2\,\text{m}$ apart; $G = 6.67 \times 10^{-11}\,\text{N m}^2/\text{kg}^2$. Treat them as point masses.
**Find:** the gravitational pull between them.

**Step 1 — the masses multiplied.** $m_1 m_2 = 0.2 \times 0.2 = 0.04\,\text{kg}^2$.

**Step 2 — the distance squared.** $r^2 = 0.2^2 = 0.04\,\text{m}^2$. The two numbers happen to cancel.

**Step 3 — the force.**

$$F = 6.67 \times 10^{-11} \times \frac{0.04}{0.04} = 6.7 \times 10^{-11}\,\text{N}$$

Compare this with each phone's weight, about $0.2 \times 9.8 \approx 2\,\text{N}$. The phones' pull on each other is roughly **thirty billion times** smaller than the Earth's pull on either one. Friction from the desk easily holds them still; that is what hides the attraction.

**Sanity check:** the same law with the Earth's mass ($6.0 \times 10^{24}\,\text{kg}$) and radius ($6.4 \times 10^{6}\,\text{m}$) gives the phone's weight: $6.67 \times 10^{-11} \times 6.0 \times 10^{24} \times 0.2 / (6.4 \times 10^{6})^2 \approx 2\,\text{N}$. One law, both answers.

## Where the picture breaks

The phones are a fair real example, not an analogy: they genuinely attract each other. But the numbers are rough. A phone is a flat slab, not a sphere, so using centre-to-centre distance is only an estimate; the true force differs a little, though it stays around $10^{-10}\,\text{N}$.

Kabir's magnet comparison also breaks down. Magnets can repel as well as attract, and their pull is huge compared with gravity between small objects. Gravity only ever attracts, and it becomes important only when at least one of the masses is enormous, like the Earth. Measuring the pull between everyday objects is possible, but it needs a delicate torsion balance in a still room, not a school desk.

## Key takeaway

Every two masses attract each other with $F = G m_1 m_2 / r^2$, equal and opposite on the two bodies. Because $G$ is so small, the pull between phones is about $10^{-10}\,\text{N}$ and completely hidden by friction; the same law with the Earth's huge mass gives an everyday weight.
