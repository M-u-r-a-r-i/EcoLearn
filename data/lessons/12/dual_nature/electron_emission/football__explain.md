---
concept_id: electron_emission
interest: football
format: explain
title: Why the X-ray machine has to glow before it works
check:
  question: |-
    The filament inside an X-ray tube is heated until it glows before any electrons come off it. Which statement best describes why heating frees electrons from the metal?
  options:
    A: |-
      Heat expands the metal, widening the gaps between the atoms so that electrons can slip out through them.
    B: |-
      Heating adds extra electrons to the metal, and those extra ones have nowhere to go but out of the surface.
    C: |-
      Heating raises the energy of the free electrons already there, and the few that end up with more than the work function escape.
    D: |-
      Heating lowers the work function to zero, after which every free electron in the metal leaves the surface.
  answer: C
  explanation: |-
    Thermionic emission does not change the barrier; it changes the spread of electron energies. Only the small fraction of electrons that happen to have more than $\varphi$ can climb out.
  misconceptions:
    A: |-
      Treats escaping as squeezing through a physical gap. The thing holding an electron in is the electrical pull of the positive ions, not a lack of room, so what matters is energy and not spacing.
    B: |-
      Assumes heating creates charge. Heating supplies energy, not electrons; the metal already has all the free electrons it will ever emit, and it becomes positively charged as they leave.
    D: |-
      Thinks the barrier itself disappears when the metal is hot. The work function is almost unchanged by temperature — if it did fall to zero, every electron would pour out at once and the current would not depend on temperature the way it does.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A floodlit football ground at night, with an inset panel drawing the same beam once as a wave and once as a stream of packets, a goal-line camera on a pole, a goalkeeper and a ball](scenes/football/dual_nature.svg "Every sensor at this ground begins the same way: light arrives, and electrons are knocked out of a metal.")

Keshav went over on his ankle in the eighty-ninth minute, studs caught in a soft patch near the corner flag. By the time his father drove him to the hospital it had swollen to twice its size.

The radiographer positions the ankle, steps behind a screen and flicks a switch. Nothing happens.

"Give it a second," she says.

Keshav looks up at the head of the machine. Through a small slot he can see a wire inside going dull red, then orange. Only then does the machine click and take its picture.

He is a Class 12 student and this bothers him the whole way home. X-rays come from electrons slamming into a metal target. So why does a machine that makes X-rays have to start by making something *hot*?

## The physics

A metal is full of **free electrons** — they drift between the atoms, which is exactly why metals conduct. But drifting *inside* is not the same as getting *out*. At the surface, the positive ions left behind pull an escaping electron back.

The **work function** $\varphi$ of a metal is the minimum energy that must be supplied to a free electron to just free it from the surface.

![An energy diagram: filled electron levels inside a metal, a dashed vacuum level above, and a green arrow marking the work function gap between them](figures/electron_emission/work-function-barrier.svg "The work function is the gap from the highest filled level up to the outside world — the toll every escaping electron must pay.")

It is quoted in **electron volts**, where

$$1\,\text{eV} = 1.6 \times 10^{-19}\,\text{J}$$

For most metals $\varphi$ is between about $2\,\text{eV}$ and $5\,\text{eV}$. It depends on the metal *and* on the state of its surface, which is why cathodes are specially coated to keep $\varphi$ low and sealed in vacuum to keep them clean.

Until that energy is supplied, nothing leaves. There are four standard ways to supply it:

![Four panels showing thermionic, photoelectric, field and secondary emission, each freeing electrons from a metal surface](figures/electron_emission/emission-methods.svg "Four different energy sources, one identical bill to pay: the work function.")

- **Thermionic emission** — heat the metal. Electron energies are spread over a range, and raising the temperature stretches that range until a useful number of electrons sit above $\varphi$ and boil off. This is Keshav's glowing filament.
- **Photoelectric emission** — shine light on it. A packet of light hands its energy to a single electron. This is the rest of the chapter.
- **Field emission** — apply a very strong electric field, of order $10^8\,\text{V/m}$, usually at a sharp tip; electrons are pulled straight out.
- **Secondary emission** — hit the surface with fast particles, which knock further electrons loose.

The goal-line camera on the pole uses the second one. The X-ray tube uses the first, and then the third and fourth idea downstream: the freed electrons are accelerated by a huge voltage and smashed into a metal target, where the sudden stop makes X-rays.

## Worked example

**Given:** a cathode coating with work function $\varphi = 2.0\,\text{eV}$. An electron in it is supplied with $5.0\,\text{eV}$ of energy.

**Find:** how fast that electron is moving once it is outside.

First, what is left after the toll:

$$K = 5.0 - 2.0 = 3.0\,\text{eV}$$

So more than half of what was supplied became speed, and the rest was spent simply getting out.

Now in SI units, so the kilograms and metres agree:

$$K = 3.0 \times 1.6 \times 10^{-19} = 4.8 \times 10^{-19}\,\text{J}$$

And from $K = \tfrac{1}{2}mv^2$ with the electron mass $m = 9.1 \times 10^{-31}\,\text{kg}$:

$$v = \sqrt{\frac{2K}{m}} = \sqrt{\frac{9.6 \times 10^{-19}}{9.1 \times 10^{-31}}} \approx 1.0 \times 10^{6}\,\text{m/s}$$

A million metres every second — that electron would cross a full-length pitch in about a ten-thousandth of a second.

**Sanity check:** a few electronvolts is a minute energy, but an electron is fantastically light, so an enormous speed is the right kind of answer — and it is still only about $0.3\%$ of the speed of light, which is why the ordinary formula $K = \tfrac{1}{2}mv^2$ was safe to use.

## Where the picture breaks

The energy-shelf diagram is a simplification. Electrons in a metal do not sit on a few neat shelves; they fill a continuous band, and the "highest filled level" is a statistical edge. The barrier is not a sharp wall either — it softens over a few atomic diameters outside the surface.

Two honest caveats. Thermionic emission never actually switches off: even at room temperature a few electrons escape, just far too few to be useful. And $\varphi$ is not a number you can look up once and trust — a fingerprint or a thin film of oxide changes it.

Football is only the setting here. An ankle X-ray and a goal-line camera are real devices that really work this way, but there is no analogy between a footballer and an electron, and you should not look for one.

## Key takeaway

Free electrons are trapped inside a metal by a surface barrier, and the minimum energy needed to escape it is the **work function** $\varphi$, typically $2$–$5\,\text{eV}$. Heat, light, a strong electric field or a particle impact can each pay that bill, giving thermionic, photoelectric, field and secondary emission. Whatever the source, nothing leaves until at least $\varphi$ has been supplied, and only the excess above $\varphi$ becomes kinetic energy.
