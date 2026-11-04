---
concept_id: dimensional_derivation
interest: cricket
format: explain
title: What sets the rhythm of the hanging ball
check:
  question: |-
    Dimensional analysis gives the period of a hanging ball as $T = k\sqrt{l/g}$. If the rope is lengthened from $0.50\,\text{m}$ to $2.0\,\text{m}$ (small swings), the period:
  options:
    A: |-
      becomes $4$ times as long
    B: |-
      becomes $16$ times as long
    C: |-
      doubles
    D: |-
      halves
  answer: C
  explanation: |-
    $T \propto \sqrt{l}$. The length is multiplied by $4$, so the period is multiplied by $\sqrt{4} = 2$. The unknown $k$ cancels in the ratio, so it isn't needed.
  misconceptions:
    A: |-
      Assumes the period is proportional to the length itself, ignoring the square root that the dimensions demand.
    B: |-
      Squares the length ratio instead of taking its square root.
    D: |-
      Inverts the relation, as if a longer rope swung faster. $l$ is in the numerator: longer rope, longer period.
author: claude-code/opus-5
written: 2026-09-21
---
## The story

![Groundstaff measure the pitch; a stopwatch nearby reads 3.50 seconds](scenes/cricket/units_measurement.svg "A tape for lengths, a stopwatch for times. Enough to crack the hanging ball.")

At the academy's indoor nets, Coach Iqbal hangs an old ball in a mesh bag from a rope tied to the top bar. It's a classic drill: the batter taps the hanging ball, and it swings away and back for the next shot, again and again.

Mehul notices something odd. Hit it hard or gently, the ball comes back after the same time, like a metronome. When the coach shortens the rope for the juniors, the rhythm speeds up.

"What if we hung a heavier ball?" Mehul asks. "Would it swing slower?" Nobody knows. The coach shrugs: "Try it."

But Mehul wonders whether he could work it out *without* trying it, knowing only what the rhythm could possibly depend on. Is there a way to find the formula for the swing time before doing a single experiment?

## The physics

**Dimensional analysis** can find the *form* of a relation. The method:

1. List the quantities the result might depend on.
2. Assume it is a product of their powers, times a dimensionless constant $k$.
3. Require both sides to have the same dimensions, and solve for the powers.

Model the hanging ball as a **simple pendulum**: a small bob on a light string, making small swings.

![A simple pendulum: a small bob of mass m on a string of length l, swinging under gravity g, with period T](figures/dimensional_derivation/pendulum-labelled.svg "The quantities that might set the period: the bob's mass m, the string's length l, and g.")

The period $T$ (time for one full swing, there and back) might depend on the mass $m$, the length $l$ and the acceleration due to gravity $g$. Assume

$$T = k\,m^a\,l^b\,g^c$$

Put in dimensions: $[\text{T}] = [\text{M}]^a\,[\text{L}]^b\,[\text{L}\,\text{T}^{-2}]^c = [\text{M}^a\,\text{L}^{b+c}\,\text{T}^{-2c}]$.

Match the powers of each base quantity on both sides:

- M: $a = 0$
- L: $b + c = 0$
- T: $-2c = 1$, so $c = -\tfrac{1}{2}$ and $b = \tfrac{1}{2}$

$$T = k\sqrt{\frac{l}{g}}$$

Mehul has his answer: **the mass doesn't appear** ($a = 0$). No other quantity in the list contains M, so nothing could cancel it. A heavier ball on the same rope swings with the same rhythm (for small swings, with a light rope). And the period grows as the square root of the rope's length.

What dimensional analysis can't give is $k$. Experiments (and the full theory) show $k = 2\pi$ for small swings:

$$T = 2\pi\sqrt{\frac{l}{g}}$$

![A graph of period against length: a red curve for T equals 2 pi root l over g, rising to 2.84 seconds at 2 metres, and a much lower dashed grey curve for root l over g](figures/dimensional_derivation/period-vs-length.svg "Both curves have the square-root shape dimensional analysis predicts. Only experiment shows that the true curve (red) is 2π times higher.")

## Worked example

**Given:** a hanging-ball rope of $l = 1.5\,\text{m}$; $g = 9.8\,\text{m/s}^2$; small swings.
**Find:** (a) the period; (b) the period if the rope is made four times as long.

(a) $$T = 2\pi\sqrt{\frac{1.5}{9.8}} = 2\pi \times 0.391 = 2.46\,\text{s} \approx 2.5\,\text{s}$$

(b) You don't need $k$ at all. Since $T \propto \sqrt{l}$,

$$\frac{T_2}{T_1} = \sqrt{\frac{4l}{l}} = 2 \quad\Rightarrow\quad T_2 \approx 4.9\,\text{s}$$

**Sanity check:** units of $\sqrt{l/g}$ are $\sqrt{\text{m}/(\text{m/s}^2)} = \sqrt{\text{s}^2} = \text{s}$. A period of a couple of seconds for a rope about as long as a person is tall matches everyday experience of swings.

## Where the picture breaks

The real drill isn't a perfect simple pendulum: the rope has mass, the ball and bag aren't tiny compared with the rope, and hard hits give large swings, where the period grows slightly. More generally, dimensional analysis has real limits:

- it **cannot find dimensionless constants** like the $2\pi$;
- it only works if you **list the right quantities** — it can't tell you that something is missing, and a dimensionless variable (like the swing angle) is invisible to it;
- in mechanics it can handle at most **three** unknown powers, since there are only three base quantities;
- it **fails for relations with sums of terms** ($s = ut + \tfrac{1}{2}at^2$) or with trigonometric, exponential or logarithmic functions.

## Key takeaway

Dimensional analysis finds the form of a relation by matching powers of M, L and T: for a pendulum, $T = k\sqrt{l/g}$, independent of mass. It can't supply the constant ($k = 2\pi$ comes from experiment or theory), and it fails for sums of terms or functions like sine and exponential.
