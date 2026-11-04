---
concept_id: total_internal_reflection
interest: cricket
format: explain
title: How the stump camera sends its picture down a glass thread
check:
  question: |-
    Light inside still water ($n = \tfrac{4}{3}$) meets the water–air surface. What is the critical angle, measured from the normal inside the water?
  options:
    A: |-
      about $41^\circ$
    B: |-
      $90^\circ$
    C: |-
      about $37^\circ$
    D: |-
      about $49^\circ$
  answer: D
  explanation: |-
    $\sin C = n_2/n_1 = 1 \div \tfrac{4}{3} = 0.75$, so $C = \sin^{-1}(0.75) \approx 49^\circ$. Beyond that angle no light escapes into the air.
  misconceptions:
    A: |-
      Recalls the familiar "about $42^\circ$" value, which is the critical angle for ordinary glass ($n = 1.5$), and applies it to water. The critical angle depends on the pair of media, not on light.
    B: |-
      Confuses the critical angle with the angle of the refracted ray at that moment. At $i = C$ the refracted ray grazes along the surface at $90^\circ$, but the critical angle itself is measured inside the denser medium and is always less than $90^\circ$.
    C: |-
      Uses $\tan C = 0.75$ instead of $\sin C = 0.75$ — the tangent formula belongs to Brewster's angle for polarisation, not to total internal reflection.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A sunlit cricket ground with the sun's rays, a broadcast camera with a long lens, a stump camera, a fielder in curved sunglasses, and a small rainbow in the sprinkler spray](scenes/cricket/ray_optics.svg "The stump camera in the middle of the picture has no cable to the truck that you could call a wire — what runs to it is glass.")

The match is over and Zoya has stayed back to help the broadcast crew coil cables. She picks up the thin one that runs from the stumps to the outside-broadcast van and is surprised by how light it is.

"That's the camera feed," the engineer says. "It's glass inside. Hair-thin."

Zoya does not believe him, so he shines a torch into one end. She walks the whole loop of the cable, around the back of the sightscreen, past the van — and at the far end, fifty metres away, the light is coming out. She bends a loose section into a gentle U. The light still comes out. She holds the middle of the bend up to her eye, looking at the side of the fibre: nothing. The glass looks dark.

Light went in one end and came out the other, round two corners, and not a bit of it leaked out of the sides on the way. A mirror-lined tube would lose some at every bounce. So what is stopping it?

## The physics

When light travels from a denser medium into a rarer one — glass to air, water to air — it bends **away** from the normal, so the angle of refraction $r$ is larger than the angle of incidence $i$. Push $i$ up and $r$ grows faster, until at one particular angle $r$ reaches $90^\circ$ and the refracted ray grazes along the boundary. That angle of incidence is the **critical angle** $C$. Putting $r = 90^\circ$ into Snell's law, $n_1 \sin C = n_2 \sin 90^\circ$, gives

$$\sin C = \frac{n_2}{n_1} \qquad (n_1 > n_2)$$

Beyond $C$ there is no angle $r$ that Snell's law could satisfy, and the refracted ray simply does not exist. Every bit of the light is reflected back into the denser medium, obeying the ordinary law of reflection. This is **total internal reflection**.

![Three rays leaving a lamp under water at increasing angles: one escapes, one grazes along the surface at ninety degrees, and one is reflected back into the water](figures/total_internal_reflection/critical-angle.svg "Only rays inside the cone of the critical angle can get out. Past C, the surface behaves like a perfect mirror — seen from below.")

Two conditions must both hold: the light must start in the **denser** medium, and it must strike the boundary at an angle **greater than** the critical angle. Both, or nothing happens.

"Total" is meant literally. An ordinary silvered mirror absorbs a few per cent of the light at every bounce; total internal reflection absorbs none, because no light crosses the boundary at all. That is why the glass fibre beats a mirror-lined tube, and why the sides looked dark to Zoya — there was nothing leaking out for her eye to catch.

![A length of optical fibre in cross-section, with a ray zig-zagging along the core and reflecting completely at each wall](figures/total_internal_reflection/optical-fibre.svg "The cladding has a lower refractive index than the core, so every bounce is beyond the critical angle. The ray zig-zags the whole length without losing light to the sides.")

The same effect puts the sparkle in a cut diamond ($C \approx 24^\circ$, so light rattles around inside before it finds a way out), makes the shimmering "water" of a road mirage, and turns the light in $45^\circ$ prisms inside binoculars without a mirror coating.

## Worked example

**Given:** an optical fibre has a core of refractive index $1.5$ and a cladding of refractive index $1.2$. A ray inside the core meets the core–cladding wall at $60^\circ$ to the normal.
**Find:** the critical angle for that wall, and whether this ray escapes.

**Step 1 — the critical angle.**

$$\sin C = \frac{n_2}{n_1} = \frac{1.2}{1.5} = 0.80$$

so $C \approx 53^\circ$. Any ray hitting the wall more steeply slanted than this — that is, at more than $53^\circ$ from the normal — is trapped.

**Step 2 — compare.** The ray arrives at $60^\circ$, and $60^\circ > 53^\circ$, so it is totally internally reflected and stays in the core. It will meet the next wall at the same $60^\circ$, and the next, all the way to the van.

**Sanity check:** the closer the two refractive indices are, the closer $n_2/n_1$ is to $1$ and the larger $C$ becomes — meaning fewer rays are trapped. That is why a fibre's core and cladding are made with a clear difference between them.

## Where the picture breaks

A real fibre is not perfect: over kilometres the glass absorbs and scatters some light, so long links need repeaters — total internal reflection loses nothing at the wall, but the material itself is not perfectly transparent. Bending matters too: Zoya's gentle U was fine, but a sharp kink changes the angle at which rays meet the wall, and any ray that drops below the critical angle refracts straight out and is lost. Finally, the cricket is only the setting. There is no analogy between a ball trapped in the field and light trapped in glass — the ball is stopped by fielders, while the light is not stopped by anything; it is simply never allowed to leave.

## Key takeaway

Going from a denser medium to a rarer one, light escapes only if it meets the boundary within the critical angle $C$, where $\sin C = n_2/n_1$. Beyond $C$, no refracted ray is possible and all the light is reflected back — total internal reflection, with no loss at all. It is what makes optical fibres, binocular prisms and a diamond's sparkle work.
