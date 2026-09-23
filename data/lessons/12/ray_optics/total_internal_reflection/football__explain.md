---
concept_id: total_internal_reflection
interest: football
format: explain
title: The camera feed that goes round corners in a glass thread
check:
  question: |-
    A ray travelling inside a glass block ($n = 1.5$) meets the glass–air face at $30^\circ$ to the normal. The critical angle for glass and air is about $42^\circ$. What happens to the ray?
  options:
    A: |-
      It is totally internally reflected, because light inside glass can never get out
    B: |-
      It grazes along the surface, leaving at $90^\circ$ to the normal
    C: |-
      It is totally internally reflected, because $30^\circ$ is less than $42^\circ$
    D: |-
      Most of it refracts out into the air, bending away from the normal
  answer: D
  explanation: |-
    Total internal reflection needs the angle of incidence to be **greater** than the critical angle. At $30^\circ$, which is less than $42^\circ$, Snell's law still has a solution — $\sin r = 1.5 \times 0.5 = 0.75$, so $r \approx 49^\circ$ — and the ray leaves the glass, bending away from the normal.
  misconceptions:
    A: |-
      Treats a denser medium as a trap at every angle. Light leaves glass easily at small angles; that is why you can see through a window at all.
    B: |-
      Applies the special case $i = C$, where the refracted ray just grazes along the surface. That happens at one particular angle, $42^\circ$ here, not at $30^\circ$.
    C: |-
      Inverts the condition. Below the critical angle the ray escapes; only beyond it does refraction become impossible and all the light reflect back.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A football ground in afternoon sun with a convex dome mirror on a post at the tunnel mouth, a broadcast camera with a long lens, an optical-fibre cable, and a rainbow in the sprinkler spray](scenes/football/ray_optics.svg "Follow the yellow cable from the camera to the pitch-side box. Everything the camera sees travels down it as light — round every bend in the touchline.")

Half-time, and the pitch-side camera has gone dead. Farhan, who runs the broadcast cables, is on his knees by the touchline box with a drum of spare cable, and Kiran — a substitute who has been warming up next to him for ten minutes and is bored — crouches down to watch.

Farhan strips back the yellow jacket. Inside there is no copper at all: just a glass thread thinner than a hair. He clips a small light source onto one end, and the far end of the drum lights up like a tiny green eye — through two hundred metres of glass wound into coils.

Kiran picks up a loop and bends it round his finger. The eye stays lit. He pinches it into a tight kink, and it dims.

Glass is transparent. Every window proves it. So how does light get carried two hundred metres and round every corner of a stadium without spilling out through the sides of a transparent thread?

## The physics

Start where the last lesson finished. When light goes from a denser medium into a rarer one — glass to air, water to air — it bends **away** from the normal, so $r > i$. Increase $i$ and $r$ climbs faster, until at one particular angle of incidence $r$ reaches $90^\circ$ and the refracted ray skims along the surface. That angle is the **critical angle** $C$.

Put $i = C$ and $r = 90^\circ$ into Snell's law, $n_1 \sin i = n_2 \sin r$, with the light starting in the denser medium $n_1$:

$$\sin C = \frac{n_2}{n_1}$$

Push past $C$ and Snell's law asks for $\sin r > 1$, which no angle satisfies. There is no refracted ray at all. Every bit of the light turns back into the denser medium: **total internal reflection**.

![Three rays leaving one point inside water: the first refracts out, the second at the critical angle grazes along the surface, the third beyond it is totally reflected back into the water](figures/total_internal_reflection/critical-angle.svg "Below C the ray escapes; at C it grazes; beyond C it is thrown back — with no loss, because there is nowhere else for the light to go.")

Two conditions, both needed: the light must be travelling from the **denser** medium towards the rarer one, and the angle of incidence must be **greater** than $C$.

This is the only kind of reflection that is total. A silvered mirror always absorbs a few per cent of the light at each bounce; total internal reflection loses nothing at the boundary, which is why it is used wherever light must bounce many times.

![A ray inside the core of an optical fibre striking the core–cladding boundary above the critical angle and being reflected again and again along the length of the fibre](figures/total_internal_reflection/optical-fibre.svg "A ray launched nearly along the fibre hits the wall at a very large angle — close to 90 degrees — so it is far beyond the critical angle and never escapes.")

In an **optical fibre**, a core of higher index is wrapped in cladding of slightly lower index. Light entering nearly along the axis strikes the boundary at a huge angle of incidence, so it is reflected again and again down the whole length. Bends are fine, because a gentle bend barely changes that angle — but a tight kink does, and there the ray finally hits below $C$ and leaks out. That is Kiran's dimming.

The same trick makes a **totally reflecting prism**: send light into a right-angled glass prism so that it meets the long face at $45^\circ$. Since $45^\circ$ is more than the $42^\circ$ critical angle of glass and air, all of it turns through $90^\circ$. Binoculars use a pair of these to flip the image upright.

## Worked example

**Given:** a fibre whose core has $n_1 = 1.5$ and whose cladding has $n_2 = 1.2$ (illustrative values).
**Find:** the critical angle at the core–cladding boundary.

**Step 1 — put the two indices into the critical-angle relation.**

$$\sin C = \frac{n_2}{n_1} = \frac{1.2}{1.5} = 0.80$$

**Step 2 — read off the angle.** $\sin C = 0.80$ gives $C = 53^\circ$.

So any ray meeting the wall of the core at more than $53^\circ$ to the normal stays inside. A ray running nearly parallel to the fibre meets that wall at close to $90^\circ$ — comfortably past $53^\circ$ — which is why almost all the light Farhan clips in at one end arrives at the other.

**Sanity check:** the two indices are fairly close together, so the light is only weakly held in and the critical angle comes out large; if the cladding were replaced by air, $\sin C$ would drop to $1/1.5$ and $C$ to about $42^\circ$, trapping a much wider spread of rays.

## Where the picture breaks

"Nothing is lost" is true at the boundary and false along the fibre. Over two hundred metres the glass itself absorbs and scatters a little light, which is why long links need repeaters — nothing to do with the reflections.

The ray picture is also a simplification. A real fibre's core is only a few wavelengths across, and there light behaves as a guided wave rather than a bouncing ray; the ray model predicts the critical angle correctly but not how the pulse spreads out as it travels.

And the football here is scenery. A ball rebounding inside the goal net is not an analogy for total internal reflection: the ball loses energy at every bounce and can leave at any angle, while this reflection is complete and only happens past a sharp threshold.

## Key takeaway

When light meets a boundary from the denser side, there is a critical angle $C$ with $\sin C = n_2/n_1$. Beyond it Snell's law has no solution and the light is thrown entirely back — total internal reflection, the one reflection that loses nothing. Optical fibres trap light this way along their whole length, and a $45^\circ$ glass prism uses it to turn a beam through a right angle.
