---
concept_id: dimensional_derivation
interest: motorsport
format: explain
title: Why double the speed needs far more than double the braking zone
check:
  question: |-
    Dimensional analysis gives a car's braking distance as $d = k\,v^2/a$, for a constant deceleration $a$. If a driver arrives at a corner at twice the speed, with the same deceleration, the braking distance:
  options:
    A: |-
      doubles
    B: |-
      becomes $16$ times as long
    C: |-
      becomes $4$ times as long
    D: |-
      becomes $\sqrt{2}$ times as long
  answer: C
  explanation: |-
    $d \propto v^2$ when $a$ is fixed. Doubling $v$ multiplies $d$ by $2^2 = 4$. The unknown $k$ cancels in the ratio, so it isn't needed.
  misconceptions:
    A: |-
      Assumes distance is simply proportional to speed, ignoring the square that the dimensions demand.
    B: |-
      Squares twice — squares the speed ratio to get $4$, then squares that again.
    D: |-
      Takes a square root, as in the pendulum's $T \propto \sqrt{l}$, instead of squaring. Here the speed is squared.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A race track with a braking marker reading 100 by the track and a race car approaching the start-finish line](scenes/motorsport/units_measurement.svg "Braking markers count down the metres to a corner. How many metres does a car really need?")

At a track-day briefing, the instructor, Ms. Kulkarni, points to the braking markers before the hairpin. "Your braking point depends on your entry speed," she says. "Come in twice as fast and you'll need much more than twice the distance."

Aryan, driving his family's hatchback, isn't convinced. "Surely double speed means double distance?" His cousin Zainab, in a heavier SUV, has a different worry: "Won't my car need a longer distance just because it's heavier?"

Ms. Kulkarni smiles. "Go out and find out — carefully."

But Zainab wonders whether they could settle it before anyone drives a metre. Braking distance can only depend on a few things: the car's mass, its speed, how hard it decelerates. Is there a way to find the formula from those ingredients alone?

## The physics

**Dimensional analysis** can find the *form* of a relation:

1. List the quantities the result might depend on.
2. Assume the result is a product of their powers, times a dimensionless constant $k$.
3. Make both sides' dimensions match, and solve for the powers.

Suppose the braking distance $d$ depends on the mass $m$, the speed $v$ when braking starts, and a constant deceleration $a$:

$$d = k\,m^x\,v^y\,a^z$$

In dimensions: $[\text{L}] = [\text{M}]^x\,[\text{L}\,\text{T}^{-1}]^y\,[\text{L}\,\text{T}^{-2}]^z = [\text{M}^x\,\text{L}^{y+z}\,\text{T}^{-y-2z}]$.

Match the powers:

- M: $x = 0$
- T: $-y - 2z = 0$, so $y = -2z$
- L: $y + z = 1$, so $-2z + z = 1$, giving $z = -1$ and $y = 2$

$$d = k\,\frac{v^2}{a}$$

Both cousins have an answer. **Mass doesn't appear**: nothing else in the list contains M, so it can't be balanced. For the *same deceleration*, a heavy SUV and a light hatchback need the same distance. And **distance grows as the square of the speed**: double the speed, four times the distance.

Dimensional analysis can't give $k$. The equations of motion (next chapter) show $k = \tfrac{1}{2}$ for constant deceleration:

$$d = \frac{v^2}{2a}$$

![A graph of braking distance against speed at a deceleration of 8 metres per second squared: a red curve for v squared over 2a reaching 100 metres at 40 metres per second, and a dashed grey curve for v squared over a, twice as high](figures/dimensional_derivation/stopping-distance-vs-speed.svg "Both curves have the shape dimensional analysis predicts: double the speed, four times the distance. Only the full theory says the true curve (red) has k = ½.")

## Worked example

**Given:** a car braking at a constant $a = 8.0\,\text{m/s}^2$ (illustrative, a road car on a dry road).
**Find:** (a) the braking distance from $v = 20\,\text{m/s}$ ($72\,\text{km/h}$); (b) the distance from $40\,\text{m/s}$.

(a) $$d = \frac{v^2}{2a} = \frac{(20\,\text{m/s})^2}{2 \times 8.0\,\text{m/s}^2} = \frac{400}{16}\,\text{m} = 25\,\text{m}$$

(b) You don't need $k$. Since $d \propto v^2$ at fixed $a$:

$$\frac{d_2}{d_1} = \left(\frac{40}{20}\right)^2 = 4 \quad\Rightarrow\quad d_2 = 100\,\text{m}$$

**Sanity check:** units of $v^2/a$ are $(\text{m}^2/\text{s}^2)/(\text{m}/\text{s}^2) = \text{m}$. Directly, $40^2/16 = 1600/16 = 100\,\text{m}$ — the same.

## Where the picture breaks

The mass result holds only *for a given deceleration*. In a real car, mass can change the deceleration the brakes and tyres achieve (a heavier car loads its tyres and brakes more), so the two cars may not decelerate equally. Race cars also decelerate harder at high speed, when their aerodynamic downforce presses them onto the track, so $a$ isn't constant. And the method itself has limits:

- it **cannot find dimensionless constants** like the $\tfrac{1}{2}$;
- it works only if you **list the right quantities**; a dimensionless one, like a tyre's friction coefficient, is invisible to it;
- in mechanics it can find at most **three** unknown powers;
- it **fails for sums of terms**, such as the full stopping distance $v\,t_r + \dfrac{v^2}{2a}$, and for sine, exponential or logarithmic relations.

## Key takeaway

Dimensional analysis finds a relation's form by matching powers of M, L and T: braking distance $d = k\,v^2/a$, independent of mass for a given deceleration, so double the speed means four times the distance. It can't supply the constant ($k = \tfrac{1}{2}$ comes from theory), and it fails for sums of terms and functions like sine or exponential.
