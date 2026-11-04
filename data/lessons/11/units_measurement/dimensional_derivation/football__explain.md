---
concept_id: dimensional_derivation
interest: football
format: explain
title: What sets the rhythm of the heading ball
check:
  question: |-
    Dimensional analysis gives the period of a hanging heading ball as $T = k\sqrt{l/g}$. If the rope is shortened from $2.0\,\text{m}$ to $0.50\,\text{m}$ (small swings), the period:
  options:
    A: |-
      halves
    B: |-
      becomes a quarter as long
    C: |-
      becomes one-sixteenth as long
    D: |-
      doubles
  answer: A
  explanation: |-
    $T \propto \sqrt{l}$. The length is divided by $4$, so the period is divided by $\sqrt{4} = 2$. The unknown $k$ cancels in the ratio, so it isn't needed.
  misconceptions:
    B: |-
      Assumes the period is proportional to the length itself, ignoring the square root that the dimensions demand.
    C: |-
      Squares the length ratio instead of taking its square root.
    D: |-
      Inverts the relation, as if a shorter rope swung more slowly. $l$ is in the numerator: shorter rope, shorter period.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A groundsman measures a goal with a tape while a match clock runs](scenes/football/units_measurement.svg "A tape for lengths, a clock for times. Enough to crack the swinging ball.")

At the academy, Coach Faizal has rigged up a heading trainer: a ball in a mesh net, hanging on a rope from a tall metal frame. Mira heads it, it swings away, and it comes back for the next header, again and again.

After a few minutes she notices something odd. Whether she heads it firmly or gently, the ball comes back after the same time, like a metronome. When the coach shortens the rope for the under-12s, the rhythm speeds up.

"What if we used a heavier ball?" Mira asks. "Would it swing back slower?"

"No idea," says the coach. "Try it after practice."

But Mira wonders whether she could work it out *without* trying it — just by thinking about what the rhythm could possibly depend on. Is there a way to find the formula for the swing time before doing a single experiment?

## The physics

**Dimensional analysis** can find the *form* of a relation. The method:

1. List the quantities the result might depend on.
2. Assume it is a product of their powers, times a dimensionless constant $k$.
3. Require both sides to have the same dimensions, and solve for the powers.

Model the heading ball as a **simple pendulum**: a small bob on a light string, making small swings.

![A simple pendulum: a small bob of mass m on a string of length l, swinging under gravity g, with period T](figures/dimensional_derivation/pendulum-labelled.svg "The quantities that might set the period: the bob's mass m, the string's length l, and g.")

The period $T$ (the time for one full swing, there and back) might depend on the mass $m$, the length $l$ and the acceleration due to gravity $g$. Assume

$$T = k\,m^a\,l^b\,g^c$$

Put in dimensions: $[\text{T}] = [\text{M}]^a\,[\text{L}]^b\,[\text{L}\,\text{T}^{-2}]^c = [\text{M}^a\,\text{L}^{b+c}\,\text{T}^{-2c}]$.

Match the powers of each base quantity on both sides:

- M: $a = 0$
- T: $-2c = 1$, so $c = -\tfrac{1}{2}$
- L: $b + c = 0$, so $b = \tfrac{1}{2}$

$$T = k\sqrt{\frac{l}{g}}$$

Mira has her answer: **the mass doesn't appear** ($a = 0$). Nothing else in the list contains M, so nothing could balance it. A heavier ball on the same rope swings with the same rhythm (for small swings and a light rope). And the period grows as the square root of the rope's length.

What dimensional analysis can't give is $k$. Experiment (and the full theory, later in Class 11) gives $k = 2\pi$ for small swings:

$$T = 2\pi\sqrt{\frac{l}{g}}$$

![A graph of period against length: a red curve for T equals 2 pi root l over g, rising to 2.84 seconds at 2 metres, and a much lower dashed grey curve for root l over g](figures/dimensional_derivation/period-vs-length.svg "Both curves have the square-root shape dimensional analysis predicts. Only experiment shows the true curve (red) is 2π times higher.")

## Worked example

**Given:** a heading-trainer rope of $l = 1.2\,\text{m}$; $g = 9.8\,\text{m/s}^2$; small swings.
**Find:** (a) the period; (b) the period if the rope is shortened to a quarter of its length for the juniors.

(a) $$T = 2\pi\sqrt{\frac{1.2}{9.8}} = 2\pi \times 0.350 = 2.20\,\text{s} \approx 2.2\,\text{s}$$

(b) You don't need $k$ at all. Since $T \propto \sqrt{l}$,

$$\frac{T_2}{T_1} = \sqrt{\frac{l/4}{l}} = \frac{1}{2} \quad\Rightarrow\quad T_2 \approx 1.1\,\text{s}$$

**Sanity check:** the units of $\sqrt{l/g}$ are $\sqrt{\text{m}/(\text{m/s}^2)} = \sqrt{\text{s}^2} = \text{s}$. A couple of seconds for a rope about a metre long matches what you see on any playground swing.

## Where the picture breaks

The heading trainer isn't a perfect simple pendulum: the net and rope have mass, the ball isn't tiny compared with the rope, and a firm header gives a large swing, whose period is slightly longer. More generally, dimensional analysis has real limits:

- it **cannot find dimensionless constants** like the $2\pi$;
- it only works if you **list the right quantities** — it can't tell you something is missing, and a dimensionless variable (like the swing angle) is invisible to it;
- in mechanics it can find at most **three** unknown powers, one per base quantity;
- it **fails for relations with sums of terms** ($s = ut + \tfrac{1}{2}at^2$) or with trigonometric, exponential or logarithmic functions.

## Key takeaway

Dimensional analysis finds the form of a relation by matching powers of M, L and T: for a pendulum, $T = k\sqrt{l/g}$, independent of mass. It can't supply the constant ($k = 2\pi$ comes from experiment or theory), and it fails for sums of terms or functions like sine and exponential. For ratios, where $k$ cancels, it's all you need.
