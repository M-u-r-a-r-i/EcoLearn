---
concept_id: refraction_snells_law
interest: gaming
format: explain
title: Why the coolant in a PC reservoir is never where it looks
check:
  question: |-
    A clear reservoir is filled to a depth of $12\,\text{cm}$ with coolant of refractive index $1.5$. Looking almost straight down into it, how far below the surface does the floor of the reservoir appear to be?
  options:
    A: |-
      $8.0\,\text{cm}$
    B: |-
      $18\,\text{cm}$
    C: |-
      $12\,\text{cm}$
    D: |-
      $4.0\,\text{cm}$
  answer: A
  explanation: |-
    For a near-vertical view, apparent depth $=$ real depth $/\,n = 12 \div 1.5 = 8.0\,\text{cm}$. A denser liquid always makes its floor look nearer than it is.
  misconceptions:
    B: |-
      Multiplies by $n$ instead of dividing, which would make the floor look *deeper* than it really is. Rays leaving the liquid bend away from the normal, so your eye traces them back to a point that is raised, never lowered.
    C: |-
      Assumes that looking straight down means the light is not bent, so nothing changes. Your eye collects a narrow cone of rays, not a single one, and those slightly slanted rays are refracted — that is what shifts the image.
    D: |-
      Works out how much the floor is raised ($12 - 8 = 4\,\text{cm}$) and gives that as the apparent depth. It is the shift, not the depth.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A gaming desk at night with a monitor, a coolant reservoir, a cut-away VR headset, a glass prism, a glowing optical cable, a hand lens over a controller board and a wall-mounted dome mirror](scenes/gaming/ray_optics.svg "The clear reservoir on the desk: notice how the tube running through it does not line up above and below the liquid.")

Kabir has spent two months' savings on a custom water-cooling loop, and tonight is the night he fills it. The reservoir is a clear cylinder, the coolant is a pale blue, and the instructions say to fill it to a depth of about fifteen centimetres.

He pours, looking down into the cylinder, until the layer of coolant looks about right. Then he checks properly, sliding a steel ruler down the inside wall, and the ruler comes out wet to twenty centimetres. He has poured a third more than he meant to.

While he is fishing the ruler out, he notices something else. A tubing run passes behind the reservoir, and where it crosses the coolant line it looks **snapped** — the lower half sitting a clear centimetre to one side of the upper half. He taps the tube. It is one solid piece.

Nothing inside the loop has moved. So the coolant is not bending the tube; it is bending the light that comes from it. What exactly does it do to that light, and can you work out in advance how wrong your eyes will be?

## The physics

Light travels more slowly in a liquid than in air. The **refractive index** of a medium is

$$n = \frac{c}{v}$$

the speed of light in vacuum divided by its speed in that medium, so $n \ge 1$ and it has no units. Water — and a water-based coolant is very nearly water — has $n \approx \tfrac{4}{3}$; ordinary glass and clear acrylic are about $1.5$; air is about $1.00$.

Because the speed changes, a ray crossing a boundary changes direction: it **refracts**. Two laws describe it. The incident ray, the refracted ray and the normal at the point of incidence all lie in one plane; and the angles obey **Snell's law**,

$$n_1 \sin i = n_2 \sin r$$

with $i$ measured from the normal in medium 1 and $r$ from the normal in medium 2. Every angle in this lesson is measured from the normal, never from the surface. Going into a denser medium the ray bends **towards** the normal; coming out into a rarer one it bends **away** from the normal. A ray arriving exactly along the normal ($i = 0$) is not bent at all.

![A ray in air striking a water surface, with the normal, the angle of incidence, the smaller angle of refraction, and a weak reflected ray](figures/refraction_snells_law/refraction-at-a-boundary.svg "Entering the denser medium, the ray bends towards the normal — the angle of refraction is the smaller one.")

Now the reservoir floor. Light leaving it travels up through the coolant and bends *away* from the normal as it escapes into the air. Your eye cannot detect that kink; it simply traces the rays it receives back in straight lines, and those lines meet **higher up** than the floor really is. For a view from nearly straight above,

$$\text{apparent depth} = \frac{\text{real depth}}{n}$$

![An object on the floor of a water tank, with rays bending at the surface and their dashed back-projections meeting at a shallower point](figures/refraction_snells_law/apparent-depth.svg "The eye traces the bent rays back in straight lines, so the object looks raised. The deeper it really is, the bigger the error.")

That is Kabir's mistake. Looking down, the floor appeared raised, so the layer of coolant looked thinner than it was — and he kept pouring until it *looked* deep enough. The same bending, happening all along the coolant line, is why the tube behind it looks snapped.

## Worked example

**Given:** the reservoir holds coolant $20\,\text{cm}$ deep, with $n_\text{coolant} = \tfrac{4}{3}$; above it is air, $n_\text{air} = 1$. A small LED on the floor of the reservoir sends a ray up at $30^\circ$ to the normal.
**Find:** the angle at which that ray leaves the surface, and the apparent depth of the floor.

**Step 1 — the bend on the way out.** Here medium 1 is the coolant, so

$$\sin r = \frac{n_1 \sin i}{n_2} = \frac{\tfrac{4}{3} \times 0.50}{1} = 0.67$$

giving $r \approx 42^\circ$. The ray has swung about $12^\circ$ further from the vertical on leaving — bent away from the normal, as it must be on the way out of a denser medium.

**Step 2 — the apparent depth.**

$$\text{apparent depth} = \frac{20\,\text{cm}}{\tfrac{4}{3}} = 15\,\text{cm}$$

So the floor looks $15\,\text{cm}$ down when it is really $20\,\text{cm}$ down: raised by $5\,\text{cm}$, about the width of a controller's grip. Kabir stopped pouring when the coolant *looked* fifteen deep — and that is why the ruler said twenty.

**Sanity check:** leaving a denser medium the ray bent away from the normal, and the floor came out looking shallower than it is. Both are exactly what a denser medium must do.

## Where the picture breaks

The apparent-depth formula is for looking from nearly straight above. From a low angle across the desk, the floor looks shifted sideways as well, and by more — which is why the tube behind the reservoir appears offset rather than simply raised.

The reservoir wall is doing something too. It is acrylic, a third medium with its own index, so the light actually crosses coolant to acrylic to air. For a thin wall the two bends nearly cancel, but a thick one adds a shift of its own that this simple treatment ignores.

And the cylinder is round. A curved wall acts as a weak lens, stretching the reflection sideways — the formula above assumes a flat surface, and a flat-sided reservoir really does behave better.

Finally, $n$ is not exactly one number: it depends slightly on the colour of the light and on temperature, and coolant warms up once the loop is running.

## Key takeaway

Light changes speed when it changes medium, and so changes direction: $n_1 \sin i = n_2 \sin r$ with $n = c/v$. Into a denser medium a ray bends towards the normal, out of it away from the normal. Because your eye traces rays back in straight lines, anything under a liquid looks raised — apparent depth $=$ real depth $/\,n$ for a near-vertical view — so a reservoir is always fuller-looking than it is.
