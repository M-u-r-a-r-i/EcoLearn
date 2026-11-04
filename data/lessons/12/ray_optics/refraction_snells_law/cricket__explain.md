---
concept_id: refraction_snells_law
interest: cricket
format: explain
title: The ball at the bottom of the water drum is deeper than it looks
check:
  question: |-
    A ball rests on the floor of a tank of water $60\,\text{cm}$ deep. Water has a refractive index of $\tfrac{4}{3}$. Looking from almost straight above, how far below the surface does the ball appear to be?
  options:
    A: |-
      $45\,\text{cm}$
    B: |-
      $80\,\text{cm}$
    C: |-
      $60\,\text{cm}$
    D: |-
      $15\,\text{cm}$
  answer: A
  explanation: |-
    For a near-vertical view, apparent depth $=$ real depth $/\,n = 60 \div \tfrac{4}{3} = 45\,\text{cm}$. Water always makes the bottom look nearer than it is.
  misconceptions:
    B: |-
      Multiplies by $n$ instead of dividing, which would make the ball look deeper than it is. Refraction on leaving the water bends rays away from the normal, so the bottom always looks raised.
    C: |-
      Assumes that looking straight down means no refraction, so nothing changes. The eye collects a narrow cone of rays, not one ray, and those slightly slanted rays are bent — which is what shifts the image.
    D: |-
      Calculates the amount by which the ball appears raised ($60 - 45 = 15\,\text{cm}$) and reports that as the apparent depth. It is the shift, not the depth.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A sunlit cricket ground with the sun's rays, a broadcast camera with a long lens, a stump camera, a fielder in curved sunglasses, and a small rainbow in the sprinkler spray](scenes/cricket/ray_optics.svg "Sunlight arrives in straight lines — until it meets water or glass. Then it changes direction.")

The drinks break is over and Faizan is the one who has to fish the spare ball out of the water drum beside the nets. It is sitting on the bottom, clearly visible, maybe a hand's depth down.

He reaches in confidently and closes his hand on nothing. He looks again — the ball hasn't moved. He reaches further, and this time his fingers find it, a good bit deeper than where he saw it.

Aisha, waiting with the drinks tray, laughs and dips a spare bat into the drum to prove a point. The handle looks **snapped** at the water line, bent sharply towards her. She lifts it out: perfectly straight. Back in: bent again, at exactly the surface.

Nothing about the ball or the bat has changed. So the water is not moving them — it is changing the light that comes from them. What exactly does it do to that light, and can you predict how far out it will be?

## The physics

Light travels slower in water than in air. The **refractive index** of a medium is

$$n = \frac{c}{v}$$

the speed of light in vacuum divided by its speed in that medium, so $n \ge 1$ and has no units. For water $n \approx \tfrac{4}{3}$, for ordinary glass $n \approx 1.5$, for air $n \approx 1.00$.

Because of that change in speed, a ray crossing a boundary changes direction — it **refracts**. The two laws of refraction are: the incident ray, the refracted ray and the normal at the point of incidence all lie in one plane; and the angles obey **Snell's law**,

$$n_1 \sin i = n_2 \sin r$$

where $i$ is measured from the normal in medium 1 and $r$ from the normal in medium 2. Going into a denser medium ($n_2 > n_1$), $\sin r$ must be smaller than $\sin i$, so the ray bends **towards** the normal; coming out into a rarer medium it bends **away** from the normal. A ray arriving exactly along the normal ($i = 0$) is not bent at all.

![A ray in air striking a water surface, with the normal, the angle of incidence, the smaller angle of refraction, and a weak reflected ray](figures/refraction_snells_law/refraction-at-a-boundary.svg "Entering the denser medium, the ray bends towards the normal — the angle of refraction is the smaller one.")

Now the ball. Light leaving it travels up through the water and bends *away* from the normal as it escapes into the air. Your eye cannot feel that kink; it simply traces the rays it receives back in straight lines, and those lines meet higher up than the ball really is. Looking from nearly straight above,

$$\text{apparent depth} = \frac{\text{real depth}}{n}$$

![An object on the floor of a water tank, with rays bending at the surface and their dashed back-projections meeting at a shallower point](figures/refraction_snells_law/apparent-depth.svg "The eye traces the bent rays back in straight lines, so the object seems raised. The deeper it really is, the bigger the mistake.")

The same bending, happening at the water line all along the bat, is why the handle looks snapped.

## Worked example

**Given:** sunlight strikes the flat water surface in the drum at $53^\circ$ to the normal. The ball lies $40\,\text{cm}$ below the surface. Take $n_\text{water} = \tfrac{4}{3}$ and $n_\text{air} = 1$.
**Find:** the angle of refraction in the water, and the ball's apparent depth.

**Step 1 — the bend.** Snell's law, with $\sin 53^\circ \approx 0.80$:

$$\sin r = \frac{n_1 \sin i}{n_2} = \frac{0.80}{4/3} = 0.60$$

so $r \approx 37^\circ$. The ray has swung about $16^\circ$ closer to the vertical on entering the water — a clear bend, but nothing dramatic.

**Step 2 — the apparent depth.**

$$\text{apparent depth} = \frac{40\,\text{cm}}{4/3} = 30\,\text{cm}$$

So the ball looks $30\,\text{cm}$ down when it is really $40\,\text{cm}$ down: raised by $10\,\text{cm}$, about the length of your palm. That is exactly the gap Faizan's hand closed on.

**Sanity check:** the refracted angle came out smaller than the angle of incidence, and the apparent depth smaller than the real depth — both are what a denser medium must do.

## Where the picture breaks

The apparent-depth formula is for looking from nearly straight above; from a low angle the ball appears shifted sideways as well, and the shift is larger. The drum's water must also be still — ripples tilt the surface, and the "normal" swings about, which is why a ball under choppy water seems to wobble even though it is lying still. And $n$ is not quite a single number: it depends slightly on the colour of the light (that is dispersion, coming later) and on temperature. The cricket here is the setting only; there is no analogy between light bending and a ball deviating off the pitch, which happens because of the seam gripping the surface, not because light changes speed.

## Key takeaway

Light changes speed when it changes medium, and so changes direction: $n_1 \sin i = n_2 \sin r$, with $n = c/v$. Into a denser medium a ray bends towards the normal, out of it away from the normal. Because your eye traces rays back in straight lines, anything under water looks raised: apparent depth $=$ real depth $/\,n$ for a near-vertical view.
