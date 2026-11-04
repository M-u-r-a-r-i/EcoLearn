---
concept_id: dimensional_derivation
interest: smartphones
format: explain
title: Would a heavier phone swing slower
check:
  question: |-
    A phone hanging on a $0.80\,\text{m}$ string swings with a period of $1.8\,\text{s}$ (small swings). The phone is replaced by one twice as heavy, on the same string. Dimensional analysis, $T = k\sqrt{l/g}$, predicts the new period is:
  options:
    A: |-
      $3.6\,\text{s}$
    B: |-
      $0.9\,\text{s}$
    C: |-
      $1.8\,\text{s}$
    D: |-
      $2.5\,\text{s}$
  answer: C
  explanation: |-
    Mass doesn't appear in $T = k\sqrt{l/g}$: no other quantity contains M, so its power must be zero. Same length, same $g$, same period, $1.8\,\text{s}$.
  misconceptions:
    A: |-
      Assumes the period is proportional to the mass — "twice as heavy, twice as sluggish". Matching the powers of M forces the mass's power to be zero.
    B: |-
      Assumes a heavier object swings faster, the way many people expect heavier things to fall faster. Neither the fall nor the swing depends on mass here.
    D: |-
      Puts the mass under the square root, as if $T \propto \sqrt{m}$ ($1.8 \times \sqrt{2} \approx 2.5$). That would leave an unmatched $\text{M}^{1/2}$, since a time has no mass in it.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A phone hanging from a shelf on a string, swinging, its screen showing a wavy sensor graph, above a desk with a scale, a caliper and a charger](scenes/smartphones/units_measurement.svg "The swinging phone records its own motion. What sets the rhythm of its swing?")

Diya has found a use for her phone's sensor app that her physics teacher will love. She ties the phone's lanyard to a string, hangs it from the bookshelf, and gives it a small push. As it swings, the app draws a neat wave, and she can read off the time for each full swing.

Her friend Karthik watches the wave. "Now try mine," he says, holding out his phone in its chunky rugged case. "It's nearly twice as heavy. It'll swing way slower."

"Or faster," says Diya. "Heavy things fall faster, right?"

They don't agree, and Karthik won't risk tying his phone to a shelf until they do. Diya wonders whether they can settle it on paper first. If the swing time can only depend on a few things — the phone's mass, the string's length, gravity — could they work out the formula before a single experiment?

## The physics

**Dimensional analysis** can find the *form* of a relation. The method:

1. List the quantities the result might depend on.
2. Assume it is a product of their powers, times a dimensionless constant $k$.
3. Require both sides to have the same dimensions, and solve for the powers.

Model the hanging phone as a **simple pendulum**: a small bob on a light string, making small swings.

![A simple pendulum: a small bob of mass m on a string of length l, swinging under gravity g, with period T](figures/dimensional_derivation/pendulum-labelled.svg "The quantities that might set the period: the bob's mass m, the string's length l, and g.")

The period $T$ (time for one full swing, there and back) might depend on the mass $m$, the length $l$ and the acceleration due to gravity $g$. Assume

$$T = k\,m^a\,l^b\,g^c$$

In dimensions: $[\text{T}] = [\text{M}]^a\,[\text{L}]^b\,[\text{L}\,\text{T}^{-2}]^c = [\text{M}^a\,\text{L}^{b+c}\,\text{T}^{-2c}]$.

Match the powers of each base quantity on both sides:

- M: $a = 0$
- L: $b + c = 0$
- T: $-2c = 1$, so $c = -\tfrac{1}{2}$ and $b = \tfrac{1}{2}$

$$T = k\sqrt{\frac{l}{g}}$$

**The mass drops out** ($a = 0$). It's the only quantity in the list containing M, so nothing could cancel it — its power has to be zero. Karthik's heavier phone, on the same string, swings with the same rhythm (for small swings, with a light string). Neither friend was right.

What dimensional analysis can't give is $k$. Experiments and the full theory show $k = 2\pi$ for small swings:

$$T = 2\pi\sqrt{\frac{l}{g}}$$

![A graph of period against length: a red curve for T equals 2 pi root l over g, rising to 2.84 seconds at 2 metres, and a much lower dashed grey curve for root l over g](figures/dimensional_derivation/period-vs-length.svg "Both curves have the square-root shape dimensional analysis predicts. Only experiment shows that the true curve (red) is 2π times higher.")

## Worked example

**Given:** a string of length $l = 0.80\,\text{m}$ (illustrative); $g = 9.8\,\text{m/s}^2$; small swings.
**Find:** (a) the period; (b) the period if the string is shortened to $0.20\,\text{m}$.

(a) $$T = 2\pi\sqrt{\frac{0.80}{9.8}} = 2\pi \times 0.286 = 1.80\,\text{s} \approx 1.8\,\text{s}$$

(b) You don't need $k$ at all. Since $T \propto \sqrt{l}$:

$$\frac{T_2}{T_1} = \sqrt{\frac{0.20}{0.80}} = \sqrt{\tfrac{1}{4}} = \tfrac{1}{2} \quad\Rightarrow\quad T_2 \approx 0.90\,\text{s}$$

**Sanity check:** the unit of $\sqrt{l/g}$ is $\sqrt{\text{m}/(\text{m/s}^2)} = \sqrt{\text{s}^2} = \text{s}$. And the limiting case makes sense: as $l \to 0$ the period shrinks towards zero, and a longer string swings more slowly, as any playground swing shows.

## Where the picture breaks

A phone on a string isn't a perfect simple pendulum. The phone is a few centimetres long, not a point, so on a short string its size matters (that's a *physical* pendulum, which you'll meet later). A flat phone also meets noticeable air resistance, the lanyard can twist, and big pushes give large swings, where the period grows slightly.

Dimensional analysis also has real limits:

- it **cannot find dimensionless constants** like the $2\pi$;
- it only works if you **list the right quantities** — it can't warn you that something is missing, and a dimensionless variable such as the swing angle is invisible to it;
- in mechanics it can find at most **three** unknown powers, since there are only three base quantities;
- it **fails for relations with sums of terms**, or with trigonometric, exponential or logarithmic functions.

## Key takeaway

Dimensional analysis finds the form of a relation by matching the powers of M, L and T. For a pendulum it gives $T = k\sqrt{l/g}$, independent of mass. It can't supply the constant ($k = 2\pi$ comes from experiment or theory), and it fails for sums of terms or for functions like sine and exponential.
