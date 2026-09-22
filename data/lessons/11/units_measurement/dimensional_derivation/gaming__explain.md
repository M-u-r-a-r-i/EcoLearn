---
concept_id: dimensional_derivation
interest: gaming
format: explain
title: Timing the swinging trap before building it
check:
  question: |-
    A game's swinging trap behaves as a simple pendulum with small swings, so dimensional analysis gives $T = k\sqrt{l/g}$. To make its period half as long, the designer should make the chain length:
  options:
    A: |-
      half as long
    B: |-
      one-quarter as long
    C: |-
      about $0.71$ times as long
    D: |-
      the same, but halve the ball's mass
  answer: B
  explanation: |-
    $T \propto \sqrt{l}$, so $l \propto T^2$. Halving $T$ multiplies $l$ by $(\tfrac{1}{2})^2 = \tfrac{1}{4}$. The unknown $k$ cancels in the ratio.
  misconceptions:
    A: |-
      Assumes the period is proportional to the length itself, ignoring the square root that the dimensions demand.
    C: |-
      Takes the square root of the period ratio ($\sqrt{1/2} \approx 0.71$) instead of squaring it — the relation used backwards.
    D: |-
      Thinks a lighter bob swings faster. The mass has power zero in the result: no other quantity contains M to balance it, so mass can't affect the period.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A gaming desk: a monitor showing a game, a tape measure, a controller on a scale, a phone showing a time in seconds](scenes/gaming/units_measurement.svg "A tape for lengths, a scale for masses, a phone for times. Is that enough to predict a swing?")

Aman and Lakshmi are designing the castle level of their platform game. The star obstacle is a spiked iron ball on a long chain, swinging across a corridor. The player has to dash underneath it at exactly the right moment.

The first playtest goes badly. "It swings too slowly," says one tester. "I just wait, then walk under it. No challenge."

"Make the ball heavier," Lakshmi suggests. "Heavy things swing faster."

"Or make the chain shorter," says Aman. "But how much shorter? I don't want to guess and rebuild it ten times."

Their engine simulates real gravity, so the trap will swing like a real one. Lakshmi pulls out her physics notebook. They know what the swing might depend on: the ball's mass, the chain's length, and gravity. Could they find the formula for the swing time before building a single version of the trap?

## The physics

**Dimensional analysis** can find the *form* of a relation:

1. List the quantities the result might depend on.
2. Assume it is a product of their powers, times a dimensionless constant $k$.
3. Require both sides to have the same dimensions, and solve for the powers.

Model the trap as a **simple pendulum**: a small, heavy bob on a light chain, making small swings.

![A simple pendulum: a small bob of mass m on a string of length l, swinging under gravity g, with period T](figures/dimensional_derivation/pendulum-labelled.svg "The quantities that might set the period: the bob's mass m, the length l, and g.")

The period $T$ (one full swing, there and back) might depend on the mass $m$, the length $l$ and the acceleration due to gravity $g$. Assume

$$T = k\,m^a\,l^b\,g^c$$

In dimensions: $[\text{T}] = [\text{M}]^a\,[\text{L}]^b\,[\text{L}\,\text{T}^{-2}]^c = [\text{M}^a\,\text{L}^{b+c}\,\text{T}^{-2c}]$.

Match the powers on both sides:

- M: $a = 0$
- L: $b + c = 0$
- T: $-2c = 1$, so $c = -\tfrac{1}{2}$ and $b = \tfrac{1}{2}$

$$T = k\sqrt{\frac{l}{g}}$$

Lakshmi's idea fails: **mass drops out** ($a = 0$). Nothing else in the list contains M, so nothing could balance it. A heavier ball on the same chain swings with the same period (for small swings and a light chain). Aman's idea works, but through a square root: to halve the period, the chain must be **four** times shorter.

Dimensional analysis can't find $k$. Experiment and the full theory give $k = 2\pi$ for small swings:

$$T = 2\pi\sqrt{\frac{l}{g}}$$

![A graph of period against length: a red curve for T equals 2 pi root l over g, rising to 2.84 seconds at 2 metres, and a much lower dashed grey curve for root l over g](figures/dimensional_derivation/period-vs-length.svg "Both curves have the square-root shape dimensional analysis predicts; only experiment shows the true curve is 2π times higher. A quarter of the length gives half the period.")

## Worked example

**Given:** chain length $l = 8.0\,\text{m}$ (illustrative); the engine's gravity $g = 9.8\,\text{m/s}^2$; small swings.
**Find:** (a) the period; (b) the chain length that halves it.

(a) $$T = 2\pi\sqrt{\frac{8.0}{9.8}} = 2\pi \times 0.904 = 5.68\,\text{s} \approx 5.7\,\text{s}$$

At $60$ frames per second, that is about $340$ frames per swing — plenty of time to stroll under it.

(b) $T \propto \sqrt{l}$, so $l \propto T^2$:

$$\frac{l_2}{l_1} = \left(\frac{T_2}{T_1}\right)^2 = \left(\frac{1}{2}\right)^2 = \frac{1}{4} \quad\Rightarrow\quad l_2 = 2.0\,\text{m}$$

**Sanity check:** directly, $2\pi\sqrt{2.0/9.8} = 2\pi \times 0.452 = 2.84\,\text{s}$, half of $5.68\,\text{s}$ — and the same value the graph shows at $2.0\,\text{m}$. Units: $\sqrt{\text{m}/(\text{m/s}^2)} = \text{s}$.

## Where the picture breaks

A spiked ball on a chain is only roughly a simple pendulum: a real chain has mass, the ball isn't tiny, and a wide swing has a slightly longer period than the formula gives. A game designer can also break the model on purpose — for example, by setting a stronger gravity in the engine, which shortens the period as $1/\sqrt{g}$. The method itself has firm limits:

- it **cannot find dimensionless constants** like $2\pi$;
- it only works if you **list every relevant quantity**, and a dimensionless one (like the swing angle) is invisible to it;
- in mechanics it can find at most **three** unknown powers, one per base quantity;
- it **fails for sums of terms** and for trigonometric, exponential or logarithmic relations.

## Key takeaway

Dimensional analysis finds the form of a relation by matching the powers of M, L and T: for a pendulum, $T = k\sqrt{l/g}$, independent of mass. It can't supply the constant ($k = 2\pi$ comes from theory or experiment), and it fails for sums of terms or functions like sine and exponential.
