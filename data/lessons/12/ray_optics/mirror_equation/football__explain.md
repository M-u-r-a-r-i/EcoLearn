---
concept_id: mirror_equation
interest: football
format: explain
title: Why the kit van looks so far behind the team bus
check:
  question: |-
    A concave mirror has a focal length of $20\,\text{cm}$ in size. A water bottle stands $30\,\text{cm}$ in front of it, on the axis. Where is the image, and what is it like?
  options:
    A: |-
      $60\,\text{cm}$ behind the mirror, virtual and erect, twice the size
    B: |-
      $60\,\text{cm}$ in front of the mirror, real and inverted, twice the size
    C: |-
      $12\,\text{cm}$ in front of the mirror, real and inverted, $0.4$ times the size
    D: |-
      $60\,\text{cm}$ in front of the mirror, real and erect, twice the size
  answer: B
  explanation: |-
    With $f = -20\,\text{cm}$ and $u = -30\,\text{cm}$, $\dfrac{1}{v} = \dfrac{1}{f} - \dfrac{1}{u} = -\dfrac{1}{20} + \dfrac{1}{30} = -\dfrac{1}{60}$, so $v = -60\,\text{cm}$ — in front of the mirror, so real — and $m = -v/u = -2$, so inverted and twice as tall.
  misconceptions:
    A: |-
      Reads a negative $v$ as "behind the mirror". In the Cartesian convention negative means on the same side as the object, in front of the mirror — which is exactly where light really crosses, so the image is real.
    C: |-
      Rearranges the mirror equation as $\dfrac{1}{v} = \dfrac{1}{f} + \dfrac{1}{u}$. The $\dfrac{1}{u}$ has to be subtracted, because the equation reads $\dfrac{1}{v} + \dfrac{1}{u} = \dfrac{1}{f}$.
    D: |-
      Gets the position right but assumes an enlarged image must be upright. The sign of $m$ decides that, and a negative $m$ means inverted; a single mirror's real image is always inverted.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A football ground in afternoon sun with a convex dome mirror on a post at the tunnel mouth, a broadcast camera with a long lens, an optical-fibre cable, and a rainbow in the sprinkler spray](scenes/football/ray_optics.svg "The dome mirror at the tunnel mouth does the same job as the bus's wing mirror: a wide view, paid for in size.")

The team bus is crawling out of the ground after an away game, and Harsh has the seat behind the driver. In the wing mirror he can see the kit van that is supposed to be following them. It looks tiny — a toy van, a long way back down the road.

Then the bus stops at the gate, and the kit van pulls up so close that Harsh can read the writing on its bonnet through the side window. It had been about four metres behind the whole time.

He looks again at the mirror. Etched into the bottom corner of the glass is a line he has read a hundred times and never thought about: *objects in mirror are closer than they appear*.

The van did not move. The mirror is not lying — it is showing something real. So where exactly has the mirror put that little van, and how small is it really?

## The physics

For a mirror, the object distance $u$, the image distance $v$ and the focal length $f$ are locked together by the **mirror equation**:

$$\frac{1}{v} + \frac{1}{u} = \frac{1}{f}, \qquad f = \frac{R}{2}$$

and the **magnification** — how tall the image is compared with the object — is

$$m = \frac{h'}{h} = -\frac{v}{u}$$

Every distance is measured from the pole in the Cartesian convention, light travelling left to right, so a real object in front of the mirror always has $u < 0$.

![A diagram of the Cartesian sign convention: distances measured from the pole, negative to the left of it and positive to the right, heights above the axis positive](figures/spherical_mirrors/cartesian-sign-convention.svg "Get u, f and R signed correctly before substituting and the equation does the rest by itself.")

Three signs carry all the meaning in the answer:

- $v$ **negative** — the image is in front of the mirror, where light actually crosses, so it is **real** and could be caught on a screen. $v$ **positive** — the image is behind the glass, where no light ever goes, so it is **virtual**.
- $m$ **negative** — inverted; $m$ **positive** — erect.
- $|m| > 1$ — magnified; $|m| < 1$ — diminished.

![Two ray diagrams: a concave mirror forming a real inverted smaller image of a distant object, and a convex mirror forming a virtual erect smaller image behind the glass](figures/mirror_equation/ray-diagrams-concave-convex.svg "The two standard rays: one parallel to the axis reflects through the focus, one aimed at the focus reflects parallel. Where they cross is the image — behind the glass for a convex mirror, always.")

A convex mirror is used on vehicles and in corridors for exactly one reason: whatever you put in front of it, the image comes out virtual, erect and *smaller*, so a very wide scene squeezes into a small piece of glass. The price is written on the mirror: smaller looks farther away.

The equation assumes paraxial rays and a thin, truly spherical mirror.

## Worked example

**Given:** the bus's wing mirror is convex with a focal length of $1.0\,\text{m}$, and the kit van is $4.0\,\text{m}$ behind it.
**Find:** where the image of the van is, and how big it is.

**Step 1 — the signs.** The mirror is convex, so $f = +1.0\,\text{m}$. The van is in front of the mirror, so $u = -4.0\,\text{m}$.

**Step 2 — the image distance.**

$$\frac{1}{v} = \frac{1}{f} - \frac{1}{u} = \frac{1}{1.0} + \frac{1}{4.0} = 1.25\,\text{m}^{-1} \quad\Rightarrow\quad v = +0.80\,\text{m}$$

$v$ is positive, so the image sits $0.80\,\text{m}$ *behind* the glass — less than an arm's length in, even though the van is four metres out.

**Step 3 — the size.**

$$m = -\frac{v}{u} = -\frac{0.80}{-4.0} = +0.20$$

Positive, so the image is the right way up; $0.20$, so it is one-fifth as tall. A van about $2\,\text{m}$ high appears about $40\,\text{cm}$ high — roughly the height of a football boot held up at arm's length.

**Sanity check:** a fifth-size, upright van that seems to sit just inside the door panel is exactly what Harsh saw, and it is why his brain read it as distant. The warning etched on the glass is the honest translation of $m = 0.2$.

## Where the picture breaks

The formula gives position and size, and nothing else. It says nothing about the blur at the edge of a wide mirror, where rays are no longer paraxial, and nothing about how your brain converts a small image into a guess at distance — which is the part that actually makes drivers misjudge a gap.

The wing mirror is also curved more strongly at its outer end than a sphere would be, so the single number $f$ only describes the middle of the glass. And treat the bus as scenery, not physics: the rules here are the rules of light, and they would be identical if the van were a bicycle.

## Key takeaway

For any spherical mirror, $\dfrac{1}{v} + \dfrac{1}{u} = \dfrac{1}{f}$ with $f = R/2$, and $m = -\dfrac{v}{u}$. Sign the inputs by the Cartesian convention and the outputs read themselves: $v$ negative means a real image in front, $v$ positive a virtual image behind, and a negative $m$ means inverted. A convex mirror always gives a virtual, erect, diminished image — a wide view bought at the cost of apparent size.
