---
concept_id: prism_refraction
interest: gaming
format: explain
title: The streamer's prism that refuses to move past one spot
check:
  question: |-
    A glass prism has a refracting angle of $60^\circ$. A ray enters one face at $55^\circ$ to the normal and leaves the other face at $45^\circ$ to the normal. What is the angle of deviation?
  options:
    A: |-
      $100^\circ$
    B: |-
      $10^\circ$
    C: |-
      $160^\circ$
    D: |-
      $40^\circ$
  answer: D
  explanation: |-
    The geometry of a prism gives $\delta = i + e - A$, so $\delta = 55^\circ + 45^\circ - 60^\circ = 40^\circ$.
  misconceptions:
    A: |-
      Adds the two bends and stops there. The two refractions do add, but the refracting angle $A$ has to come off: part of the turning is built into the wedge itself, not into the ray's change of direction.
    B: |-
      Subtracts the angle of emergence from the angle of incidence. Both faces bend the ray the *same* way, towards the base, so their effects add — subtracting would mean the second face undid the first.
    C: |-
      Adds $A$ instead of subtracting it. A quick check kills this one: a $60^\circ$ prism cannot turn light by $160^\circ$, which would be sending it almost straight back the way it came.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A gaming desk at night with a monitor, a coolant reservoir, a cut-away VR headset, a glass prism, a glowing optical cable, a hand lens over a controller board and a wall-mounted dome mirror](scenes/gaming/ray_optics.svg "The glass wedge on the desk sends the beam off at an angle. Turn the wedge and that angle changes — but not without limit.")

Sana streams three evenings a week, and she has been chasing a look she saw on another channel: a soft band of colour lying across one corner of the frame. The trick, she reads, is a solid glass prism held in the beam of the key light.

The prism arrives — a triangular block the length of her hand — and she starts experimenting before the light is even set. Held in the lamp's beam, it throws a bright patch onto the wall behind her chair.

She turns the prism slowly, watching the patch. At first it slides along the wall towards the door, exactly as you would expect. She keeps turning the same way. The patch slows. Then it **stops**, sits still for a moment while the prism is plainly still rotating — and starts travelling *back* the way it came.

She rolls it back and forth a few times. The turning point is always at the same place on the wall, and the patch cannot be pushed past it from either direction.

The glass has not changed and the lamp has not moved. So why should a smooth, steady turn produce a patch that goes one way, stops, and reverses?

## The physics

A **prism** is a wedge of transparent material with two flat refracting faces meeting at the **refracting angle** $A$. Light entering the first face bends towards the normal; leaving the second face, it bends away from the normal. Crucially both bends turn the ray the *same* way — towards the base — so they add rather than cancel. Every angle here is measured from the normal to the face.

![A ray passing through a triangular prism, marked with the refracting angle A, the angles of incidence and emergence, the two internal angles, and the angle of deviation between the extended incoming ray and the emergent ray](figures/prism_refraction/prism-deviation.svg "The deviation δ is the angle between the direction the ray came in on and the direction it finally leaves on.")

Two relations follow from the geometry alone, with no optics in them at all:

$$r_1 + r_2 = A \qquad\text{and}\qquad \delta = i + e - A$$

where $i$ is the angle of incidence, $e$ the angle of emergence, $r_1$ and $r_2$ the two angles inside the glass, and $\delta$ the **angle of deviation**. Snell's law then ties each pair together: $\sin i = n \sin r_1$ at the first face, and $n \sin r_2 = \sin e$ at the second.

Now turn the prism, which changes $i$. Both $i$ and $e$ shift, and $\delta$ traces out this curve:

![A graph of the angle of deviation against the angle of incidence for an equilateral prism, falling to a minimum near 49 degrees and rising again](figures/prism_refraction/deviation-vs-incidence.svg "The deviation never falls below one particular value. At that dip the light passes symmetrically, entering and leaving at the same angle.")

The curve has a **minimum**, and that is Sana's turning point: the patch reverses because $\delta$ stops falling and starts rising. For every deviation above the minimum there are *two* angles of incidence that produce it — the ray entering steeply, and the same path run backwards — but at the bottom of the dip those two merge into one. There the path through the prism is symmetric:

$$i = e, \qquad r_1 = r_2 = \frac{A}{2}, \qquad \delta = \delta_\text{min}$$

and the ray inside runs parallel to the base. Putting $i = (A + \delta_\text{min})/2$ into Snell's law at the first face gives the standard result

$$n = \frac{\sin\left(\dfrac{A + \delta_\text{min}}{2}\right)}{\sin\left(\dfrac{A}{2}\right)}$$

This is the classic laboratory method for measuring a refractive index: two angles off a protractor, and no measurement of distance at all. It assumes a single wavelength, flat polished faces, and light that escapes the second face instead of being totally internally reflected.

## Worked example

**Given:** Sana's prism is equilateral, so $A = 60^\circ$. Turned to the position where the patch stops moving, the deviation measures $\delta_\text{min} = 60^\circ$.
**Find:** the refractive index of the glass.

**Step 1 — use the symmetry.** At minimum deviation the ray splits the prism evenly, so each internal angle is

$$r_1 = r_2 = \frac{A}{2} = 30^\circ$$

**Step 2 — find the angle of incidence.** From $\delta = i + e - A$ with $i = e$,

$$i = \frac{A + \delta_\text{min}}{2} = \frac{60^\circ + 60^\circ}{2} = 60^\circ$$

**Step 3 — Snell's law at the first face.**

$$n = \frac{\sin i}{\sin r_1} = \frac{\sin 60^\circ}{\sin 30^\circ} = \frac{0.866}{0.500} = 1.73$$

**Sanity check:** $1.73$ is well above $1$, as any real medium must be, and it sits at the heavy end of the range for optical glasses — ordinary window glass is nearer $1.5$ and would have given a smaller minimum deviation. A dense glass bends light more, which is exactly what you would buy a prism for.

## Where the picture breaks

A real lamp beam is white, and every colour has its own refractive index, so strictly there is a minimum deviation for red and a slightly different one for violet. Sana's patch is not a sharp spot but a short smear with coloured edges, and her "turning point" is really several turning points a fraction of a degree apart. Treating $n$ as one number is an approximation the next lesson takes apart.

The formula also assumes the light gets through. Turn the prism far enough and the ray inside meets the second face beyond the critical angle; it is then totally internally reflected, and the patch vanishes altogether instead of reversing.

And the prism is doing nothing gaming-specific: it is ordinary glass in an ordinary beam, and a paperweight would behave the same. The stream is only why anyone was watching the wall.

## Key takeaway

A prism bends light twice, both times towards its base, and the total turn is the deviation $\delta = i + e - A$, with $r_1 + r_2 = A$. As the prism is rotated, $\delta$ passes through a minimum where the path is symmetric and $r_1 = r_2 = A/2$. Measuring $A$ and $\delta_\text{min}$ then gives the refractive index directly from $n = \sin\!\left(\frac{A + \delta_\text{min}}{2}\right)\big/\sin\!\left(\frac{A}{2}\right)$.
