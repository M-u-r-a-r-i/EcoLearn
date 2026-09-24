---
concept_id: total_internal_reflection
interest: gaming
format: explain
title: The red glow at the end of an optical audio cable
check:
  question: |-
    Light travelling inside a clear acrylic light pipe ($n = 1.5$) reaches the acrylic–air wall. What is the critical angle?
  options:
    A: |-
      about $34^\circ$
    B: |-
      $90^\circ$
    C: |-
      about $48^\circ$
    D: |-
      about $42^\circ$
  answer: D
  explanation: |-
    $\sin C = n_2/n_1 = 1 \div 1.5 = 0.67$, so $C = \sin^{-1}(0.67) \approx 42^\circ$, measured from the normal inside the acrylic. Any ray meeting the wall at more than that is totally internally reflected.
  misconceptions:
    A: |-
      Uses $\tan C = 0.67$ instead of $\sin C = 0.67$. The tangent formula belongs to Brewster's angle for polarisation, not to total internal reflection, which comes straight out of Snell's law with $r = 90^\circ$.
    B: |-
      Confuses the critical angle with the angle of the *refracted* ray at that moment. At $i = C$ the refracted ray does graze along the wall at $90^\circ$, but the critical angle itself is measured inside the denser medium and is always less than $90^\circ$.
    C: |-
      Measures the angle from the surface instead of from the normal, giving $90^\circ - 42^\circ = 48^\circ$. Every angle in refraction is measured from the normal.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A gaming desk at night with a monitor, a coolant reservoir, a cut-away VR headset, a glass prism, a glowing optical cable, a hand lens over a controller board and a wall-mounted dome mirror](scenes/gaming/ray_optics.svg "The cable lying across the desk glows red only at its tip. Along its whole length, nothing leaks out of the sides.")

Devika is rebuilding her setup before a weekend tournament, and there is one cable in the box she has never used: a stiff black lead with a square plug and a little hinged flap over the end. The label calls it an optical audio cable.

She lifts the flap and a **red dot** stares back at her. Not a warm glow along the cable — a single point of red light, right at the tip.

Her brother tells her it is glass inside. Devika does not believe him, so she runs the free end under her desk, behind the monitor, round the leg of the table, and back up. The red dot is still there at the far end, just as bright. She pinches the cable into a gentle U. Still there. Then she holds the middle of the bend up to her eye and looks at the *side* of it, hard, in a dark room. Nothing. The cable is black.

Light went in one end, round two corners and a bend, and came out the other — and not a bit of it escaped through the sides on the way. A mirror-lined pipe would leak a little at every bounce. So what is holding it in?

## The physics

When light goes from a denser medium into a rarer one — glass to air, acrylic to air — it bends **away** from the normal, so the angle of refraction $r$ is larger than the angle of incidence $i$. Push $i$ up and $r$ grows faster, until at one particular angle of incidence $r$ reaches $90^\circ$ and the refracted ray grazes along the boundary. That angle is the **critical angle** $C$. Put $r = 90^\circ$ into Snell's law, $n_1 \sin C = n_2 \sin 90^\circ$, and

$$\sin C = \frac{n_2}{n_1} \qquad (n_1 > n_2)$$

Beyond $C$ there is no angle $r$ that Snell's law could satisfy: the refracted ray simply does not exist. All of the light is reflected back into the denser medium, obeying the ordinary law of reflection. This is **total internal reflection**. All angles here are measured from the normal, inside the denser medium.

![Three rays leaving a lamp under water at increasing angles: one escapes, one grazes along the surface at ninety degrees, and one is reflected back into the water](figures/total_internal_reflection/critical-angle.svg "Only rays inside the cone of the critical angle can get out. Past C, the boundary behaves like a perfect mirror seen from below.")

Two conditions must hold together: the light must start in the **denser** medium, and it must strike the boundary at more than the **critical angle**. Both, or nothing special happens.

"Total" is meant literally. A silvered mirror absorbs a few per cent of the light at every bounce; total internal reflection absorbs nothing at the boundary, because no light crosses it at all. That is why Devika's cable beats a mirror-lined pipe, and why the sides looked black — there was nothing leaking out for her eye to catch.

![A length of optical fibre in cross-section, with a ray zig-zagging along the core and reflecting completely at each wall](figures/total_internal_reflection/optical-fibre.svg "The cladding has a lower refractive index than the core, so every bounce is beyond the critical angle. The ray zig-zags the whole length without losing light to the sides.")

The same effect turns light through $45^\circ$ prisms inside binoculars with no mirror coating at all, puts the fire in a cut diamond, and carries the broadband that decides your ping.

## Worked example

**Given:** a plastic optical cable with a core of refractive index $1.50$ and a cladding of refractive index $1.35$. A ray inside the core meets the core–cladding wall at $70^\circ$ to the normal.
**Find:** the critical angle for that wall, and whether this ray gets out.

**Step 1 — the critical angle.**

$$\sin C = \frac{n_2}{n_1} = \frac{1.35}{1.50} = 0.90$$

so $C \approx 64^\circ$. Any ray that meets the wall at more than $64^\circ$ from the normal — that is, sliding along the cable rather than heading across it — is trapped.

**Step 2 — compare.** The ray arrives at $70^\circ$, and $70^\circ > 64^\circ$, so it is totally internally reflected and stays in the core. It meets the next wall at the same $70^\circ$, and the next, all the way to the plug.

**Sanity check:** the closer the two indices are, the closer $n_2/n_1$ is to $1$ and the larger $C$ becomes — meaning fewer of the rays inside are steep enough to be trapped. That is why a fibre is made with a clear difference between core and cladding.

## Where the picture breaks

Total internal reflection loses nothing *at the wall*, but the material between the walls is not perfectly transparent. Plastic fibre absorbs and scatters enough that a run of a few tens of metres is about its limit; the glass fibre in a broadband line goes much further, and over kilometres even that needs repeaters.

Bending matters too. Devika's gentle U was fine, but a sharp kink changes the angle at which rays meet the wall, and any ray that drops below the critical angle refracts straight out and is gone. That is why these cables are stiff and why the instructions warn against tight bends.

And do not picture the light as something being *carried* down the cable the way a wire carries charge. Nothing is flowing along the glass. Each ray simply travels in a straight line until a wall turns it, and the wall turns it because of an angle, not because of any barrier.

## Key takeaway

Going from a denser medium to a rarer one, light escapes only if it meets the boundary within the critical angle $C$, where $\sin C = n_2/n_1$. Beyond $C$ no refracted ray is possible and every bit of the light is reflected back, with no loss at the boundary at all. That is total internal reflection, and it is what makes optical cables, binocular prisms and a diamond's sparkle work.
