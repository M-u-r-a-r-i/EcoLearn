---
concept_id: refraction_snells_law
interest: football
format: explain
title: The ice bath is deeper than it looks
check:
  question: |-
    A recovery tub is filled to a depth of $60\,\text{cm}$ with water ($n = 4/3$). A whistle lies on the bottom. Looking almost straight down, how deep does the whistle appear to be?
  options:
    A: |-
      $80\,\text{cm}$
    B: |-
      $60\,\text{cm}$
    C: |-
      $45\,\text{cm}$
    D: |-
      $40\,\text{cm}$
  answer: C
  explanation: |-
    For near-normal viewing, apparent depth $=$ real depth $/\,n = 60 \times \dfrac{3}{4} = 45\,\text{cm}$. The rays bend away from the normal as they leave the water, so they seem to come from a point higher up.
  misconceptions:
    A: |-
      Multiplies by $n$ instead of dividing. Water makes things look *shallower*, never deeper, so the answer has to come out smaller than $60\,\text{cm}$.
    B: |-
      Assumes that looking straight down avoids refraction altogether. Only a ray exactly along the normal is undeviated; the rays that actually reach your eye leave at small angles either side of it, and they bend.
    D: |-
      Uses $n = 1.5$, the refractive index of glass, instead of $4/3$ for water. Each material has its own index, and the tub is full of water.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A football ground in afternoon sun with a convex dome mirror on a post at the tunnel mouth, a broadcast camera with a long lens, an optical-fibre cable, and a rainbow in the sprinkler spray](scenes/football/ray_optics.svg "The sunbeam slanting across the pitch will do something odd the instant it meets water — in the sprinkler spray, or in the recovery tub inside.")

Training has finished and the recovery tub in the corner of the physio room is full to the brim with iced water. Manas, the striker, lowers himself in up to his knees and yelps at the cold — and then stops yelping, because his own shins look wrong. At the water line each leg has a kink in it, as though someone had snapped it sideways and joined it up again.

Pooja, the physio, is not impressed. She holds a stopwatch over the tub. "Watch." She lets it drop, and it settles flat on the bottom. Manas reaches down to pick it up, closes his fingers exactly where he can see it — and grabs cold water. His hand stops well above the stopwatch.

He tries twice more and misses twice more. The water is perfectly clear and perfectly still, and it is telling him something untrue about where the bottom of the tub is. What is it doing to the light?

## The physics

Light travels at different speeds in different materials — fastest in vacuum, and slower in water or glass. The **refractive index** of a medium is

$$n = \frac{c}{v}$$

where $c$ is the speed of light in vacuum and $v$ its speed in the medium. Water has $n \approx 4/3$, ordinary glass $n \approx 1.5$; air is so close to $1$ that we take it as $1$.

Because the speed changes at a boundary, the direction changes too. That bending is **refraction**, and it obeys two laws: the incident ray, the refracted ray and the normal all lie in one plane, and

$$n_1 \sin i = n_2 \sin r$$

which is **Snell's law**. Here $i$ is measured between the incident ray and the normal, $r$ between the refracted ray and the normal.

![A ray in air striking a water surface: it bends towards the normal on entering the water, with a weak reflected ray going back into the air](figures/refraction_snells_law/refraction-at-a-boundary.svg "Going into the denser medium, the ray bends towards the normal. Coming out, it bends away from it by exactly the same rule.")

Read the law both ways round. Into a denser medium ($n_2 > n_1$): $\sin r < \sin i$, so the ray bends **towards** the normal. Out of a denser medium into a rarer one: it bends **away** from the normal. A ray arriving exactly along the normal, $i = 0$, is not bent at all — it only slows down.

Now Manas's problem. Rays leave the stopwatch, bend away from the normal as they escape into the air, and reach his eye. His eye simply runs those rays back in straight lines, and they meet at a point **higher** than the stopwatch. For rays close to the normal that point works out at

$$\text{apparent depth} = \frac{\text{real depth}}{n}$$

![An object on the bottom of a tank of water: rays bend away from the normal on leaving, and their backward extensions meet at a shallower point, so the object looks raised](figures/refraction_snells_law/apparent-depth.svg "Nothing has moved. Your eye assumes light travels in straight lines, and the bend at the surface is what raises the image.")

So a tub filled $40\,\text{cm}$ deep shows its floor at $40 \times \dfrac{3}{4} = 30\,\text{cm}$: the stopwatch looks a full $10\,\text{cm}$ higher than it is, which is about the width of Manas's palm — and about how far his grab missed by. This shortcut holds only for **near-normal viewing**; look in steeply from the side and the shift is larger and the image distorted, which is why his shins looked bent, not just short.

## Worked example

**Given:** low evening sunlight strikes the still surface of the tub at $53^\circ$ to the normal ($\sin 53^\circ = 0.80$). The water has $n = 4/3$.
**Find:** the angle of refraction inside the water.

**Step 1 — write Snell's law for this boundary.** Light goes from air into water, so $n_1 = 1$ and $n_2 = 4/3$:

$$\sin r = \frac{n_1 \sin i}{n_2} = \frac{0.80}{4/3} = 0.80 \times \frac{3}{4} = 0.60$$

**Step 2 — read off the angle.** $\sin r = 0.60$ gives $r = 37^\circ$.

So the beam that met the surface at $53^\circ$ carries on inside the water at $37^\circ$ — it has swung about $16^\circ$ closer to the vertical, a noticeable kink but nowhere near a right-angle turn.

**Sanity check:** the ray bent *towards* the normal on entering the denser water, which is what Snell's law must give whenever $n_2 > n_1$.

## Where the picture breaks

The tub is a clean case only while the water is still. The moment Manas moves, the surface is a shifting set of tilted mirrors and lenses, the normal changes from point to point, and no single value of $r$ describes anything.

Two more honest limits. The simple depth formula assumes you are looking almost straight down; his bent-looking shins are the steeply-viewed case, which the formula does not cover. And $n$ depends slightly on the colour of the light — a fact this lesson ignores and the dispersion lesson is built on.

Football is only the setting here. There is no footballing analogy for refraction, and a ball skidding on wet turf is a poor one to reach for: the ball slows because of friction, not because it enters a medium where waves travel more slowly.

## Key takeaway

Light changes speed at a boundary, and so changes direction: $n_1 \sin i = n_2 \sin r$, with $n = c/v$. Into a denser medium the ray bends towards the normal, out of one it bends away. Because your eye traces rays back in straight lines, an object under water looks raised: for near-normal viewing, apparent depth is the real depth divided by $n$.
