---
concept_id: prism_refraction
interest: cricket
format: explain
title: The trophy that turns the sunbeam back on itself
check:
  question: |-
    An equilateral glass prism is set at minimum deviation and the deviation is measured as $30^\circ$. What is the refractive index of the glass?
  options:
    A: |-
      $1.15$
    B: |-
      $1.50$
    C: |-
      $0.52$
    D: |-
      $1.41$
  answer: D
  explanation: |-
    For an equilateral prism $A = 60^\circ$, so $n = \dfrac{\sin\left(\frac{A + \delta_\text{min}}{2}\right)}{\sin\left(\frac{A}{2}\right)} = \dfrac{\sin 45^\circ}{\sin 30^\circ} = \dfrac{0.707}{0.5} = 1.41$.
  misconceptions:
    A: |-
      Uses $\sin(A + \delta_\text{min})/\sin A$ and drops both halves. The halves are not decoration — they come from $r_1 = r_2 = A/2$ at minimum deviation, which is the whole reason the formula works.
    B: |-
      Applies the thin-prism result $\delta = (n-1)A$, giving $n = 30/60 + 1 = 1.5$. That shortcut is only valid for a prism of very small angle, where all the sines can be replaced by the angles themselves. A $60^\circ$ prism is nowhere near that.
    C: |-
      Uses $\sin(\delta_\text{min}/2)/\sin(A/2)$ and forgets to add $A$ to the deviation. The result is less than $1$, which should be the alarm bell: no ordinary medium has a refractive index below that of vacuum.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A sunlit cricket ground with the sun's rays, a broadcast camera with a long lens, a stump camera, a fielder in curved sunglasses, and a small rainbow in the sprinkler spray](scenes/cricket/ray_optics.svg "Sunlight comes in straight and leaves bent every time it passes through a wedge of glass.")

The under-17 trophy in the clubhouse window is a solid glass wedge — a long triangular block on a wooden base, engraved down one face. On sunny afternoons it throws a bright patch onto the wall opposite, above the honours board.

Devansh, waiting for his turn in the nets, starts turning it slowly on its base and watching the patch. At first the patch slides along the wall towards the door, the way you would expect. He keeps turning the same way. The patch slows down. Then it stops, sits still for a moment while the trophy keeps rotating — and then starts coming *back*, towards where it began.

He turns it back and forth a few times. The turning point is always at the same place on the wall, and the patch never gets past it, no matter which way he goes.

The glass has not changed. The Sun has not moved. So why should a smooth, steady turn of the prism produce a patch that goes one way, stops, and reverses?

## The physics

A **prism** is a wedge of glass with two flat refracting faces meeting at the **refracting angle** $A$. Light entering one face bends towards the normal; leaving the other face, it bends away. Crucially, both bends turn the ray the *same* way — towards the base — so the deviations add rather than cancel.

![A ray passing through a triangular prism, marked with the refracting angle A, the angles of incidence and emergence, the two internal angles, and the angle of deviation between the extended incoming ray and the emergent ray](figures/prism_refraction/prism-deviation.svg "The deviation δ is the angle between the direction the ray came in on and the direction it finally leaves on.")

Two relations follow from the geometry alone, with no optics in them at all:

$$r_1 + r_2 = A \qquad\text{and}\qquad \delta = i + e - A$$

where $i$ is the angle of incidence, $e$ the angle of emergence, $r_1$ and $r_2$ the two angles inside the glass, and $\delta$ the **angle of deviation**. Snell's law then ties each pair together: $\sin i = n \sin r_1$ at the first face, and $n \sin r_2 = \sin e$ at the second.

Now turn the prism, which changes $i$. Both $i$ and $e$ shift, and $\delta$ traces out this curve:

![A graph of the angle of deviation against the angle of incidence for an equilateral prism, falling to a minimum near 49 degrees and rising again](figures/prism_refraction/deviation-vs-incidence.svg "The deviation never falls below one particular value. At that dip the light passes symmetrically, entering and leaving at the same angle.")

The curve has a **minimum**. That is Devansh's turning point: the patch on the wall reverses because $\delta$ stops falling and starts rising. For every value of $\delta$ above the minimum there are two angles of incidence that give it — the ray entering steeply and the same path run backwards — but at the bottom of the dip those two merge into one. At that single position the path through the prism is symmetric:

$$i = e, \qquad r_1 = r_2 = \frac{A}{2}, \qquad \delta = \delta_\text{min}$$

and the ray inside runs parallel to the base. Putting $i = (A + \delta_\text{min})/2$ into Snell's law at the first face gives the standard result

$$n = \frac{\sin\left(\dfrac{A + \delta_\text{min}}{2}\right)}{\sin\left(\dfrac{A}{2}\right)}$$

This is the classic laboratory method for measuring a refractive index: you need only two angles, both read off a protractor, and no absolute measurement of distance at all. It assumes a single wavelength, a prism with flat polished faces, and light that actually gets out of the second face rather than being totally internally reflected.

## Worked example

**Given:** an equilateral glass prism, so $A = 60^\circ$. Turned to minimum deviation, $\delta_\text{min}$ measures $30^\circ$.
**Find:** the refractive index of the glass.

**Step 1 — use the symmetry.** At minimum deviation the ray splits the prism evenly, so each internal angle is

$$r_1 = r_2 = \frac{A}{2} = 30^\circ$$

**Step 2 — find the angle of incidence.** From $\delta = i + e - A$ with $i = e$:

$$i = \frac{A + \delta_\text{min}}{2} = \frac{60^\circ + 30^\circ}{2} = 45^\circ$$

**Step 3 — Snell's law at the first face.**

$$n = \frac{\sin i}{\sin r_1} = \frac{\sin 45^\circ}{\sin 30^\circ} = \frac{0.707}{0.500} = 1.41$$

**Sanity check:** ordinary glass sits between about $1.5$ and $1.6$, and light crown glass a little below that, so $1.41$ is the right size for a transparent solid — and comfortably above $1$, as any real medium must be.

## Where the picture breaks

A real sunbeam is white, and every colour has its own refractive index, so strictly there is a minimum deviation for red and a slightly different one for violet. Devansh's patch is not a single sharp spot but a short smear with coloured edges, and the "turning point" he sees is really several turning points a fraction of a degree apart. Treating $n$ as one number is an approximation that the next lesson takes apart.

The formula also assumes the light gets through. Turn the prism far enough and the ray inside meets the second face beyond the critical angle; it is then totally internally reflected and the patch on the wall vanishes altogether rather than reversing.

And the trophy is just glass in a window. Nothing about cricket explains this — it is an ordinary prism, and the ground would do exactly the same with a paperweight.

## Key takeaway

A prism bends light twice, both times towards its base, and the total turn is the deviation $\delta = i + e - A$, with $r_1 + r_2 = A$. As you rotate the prism, $\delta$ passes through a minimum, where the path is symmetric and $r_1 = r_2 = A/2$. Measuring $A$ and $\delta_\text{min}$ gives the refractive index directly from $n = \sin\left(\frac{A+\delta_\text{min}}{2}\right)\big/\sin\left(\frac{A}{2}\right)$.
