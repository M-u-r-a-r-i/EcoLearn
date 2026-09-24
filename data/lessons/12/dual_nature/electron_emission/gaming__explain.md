---
concept_id: electron_emission
interest: gaming
format: explain
title: The arcade cabinet that needs eight seconds to wake up
check:
  question: |-
    The heater wire inside an old cabinet's picture tube has to glow before the tube produces any picture at all. Which statement about that is correct?
  options:
    A: |-
      Heating gives the metal a net positive charge, and that charge pushes electrons off the surface.
    B: |-
      Heating softens the surface of the metal, letting the trapped electrons leak away through it.
    C: |-
      Heating shares energy among the free electrons until a few of them have more than the work function and can cross the surface barrier.
    D: |-
      The heat is not what frees the electrons; the tube's accelerating voltage pulls them straight out of the cold metal.
  answer: C
  explanation: |-
    Free electrons are held inside the metal by a surface barrier of height $\varphi$. Heating widens the spread of thermal energies until the fastest few exceed $\varphi$ and escape — thermionic emission.
  misconceptions:
    A: |-
      Confuses heating with charging. A hot filament stays electrically neutral overall; what heat changes is the energy of the electrons, not the charge of the metal.
    B: |-
      Imagines escape as a mechanical leak through a softened surface. The barrier is an energy barrier, not a physical skin, and the filament works far below its melting point.
    D: |-
      Confuses the accelerating voltage with emission. That voltage steers electrons that are already outside the cathode; pulling them out of cold metal directly would need a field of about $10^8\,\text{V/m}$, which a tube's few hundred volts nowhere near produces.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A gaming room shown in three stages: a cut-away retro CRT cabinet with a glowing filament and an electron beam, a flat monitor whose light leaves as a wave and then as packets, and a camera sensor feeding a current to a meter](scenes/gaming/dual_nature.svg "Every stage on this desk is the same trade: energy goes in, electrons come out.")

The college gaming club has been given a storeroom, and at the back of it, under a dust sheet, is an arcade cabinet older than anyone in the club. Nikhil finds the switch.

The machine hums. The screen stays black.

"It's dead," Priya says, already turning away.

Nikhil waits. Eight seconds later a blue glow floods the screen, a title slides in, and tinny music starts.

He gets round the back and looks in through the vents. The picture tube is heavy glass with a narrow neck, and deep inside that neck a tiny wire is glowing orange, like the filament of a bulb.

The club's flat monitor lights up the instant you press its button. This one refuses to start until that little wire is hot.

Why should a picture depend on a scrap of metal being heated? What is the heat doing that switching the power on cannot?

## The physics

A metal is full of **free electrons** — they drift between the atoms, which is why metals conduct and why a current flows the moment you close a circuit. But moving around *inside* the metal is not the same as getting *out* of it. At the surface, the positive ions left behind pull an escaping electron back. Leaving means climbing an energy barrier.

The **work function** $\varphi$ of a metal is the minimum energy that must be supplied to a free electron to just free it from the surface.

![An energy diagram: filled electron levels inside a metal, a dashed vacuum level above, and an arrow marking the work function gap between them](figures/electron_emission/work-function-barrier.svg "The work function is the gap from the highest filled level up to the outside world — the toll every escaping electron has to pay.")

It is quoted in **electron volts**:

$$1\,\text{eV} = 1.6 \times 10^{-19}\,\text{J}$$

For most metals $\varphi$ lies between about $2\,\text{eV}$ and $5\,\text{eV}$. It depends on the metal *and* on the state of its surface, which is why a picture tube's cathode is coated with a special oxide layer — the coating drops $\varphi$ far enough that a dull orange heat is already enough.

Until that energy is supplied, nothing leaves. There are four standard ways to supply it:

![Four panels showing thermionic, photoelectric, field and secondary emission, each freeing electrons from a metal surface](figures/electron_emission/emission-methods.svg "Four different energy sources, one identical bill to pay: the work function.")

- **Thermionic emission** — heat the metal. Temperature spreads the electrons' energies, and once the metal is hot enough a small fraction of them have more than $\varphi$ and boil off. This is Nikhil's glowing wire, and those eight seconds are simply the cathode reaching working temperature.
- **Photoelectric emission** — shine light on it. A single packet of light hands its energy to a single electron. This is what happens in the sensor of a webcam or a console's tracking camera, and it is where the rest of this chapter goes.
- **Field emission** — apply an enormous electric field, of order $10^8\,\text{V/m}$, usually at a sharp tip, and electrons are dragged straight out of cold metal.
- **Secondary emission** — hit the surface with fast particles, which knock further electrons loose.

The beam that draws the picture is made of thermionic electrons; the few hundred volts inside the tube only accelerate and steer them once they are already out.

## Worked example

**Given:** a cathode coating with work function $\varphi = 2.0\,\text{eV}$, and a USB port supplying $5\,\text{V}$ across a gap of $1\,\text{mm}$ between two contacts.
**Find:** the escape energy in joules, and whether that $5\,\text{V}$ could pull electrons out by itself.

First the toll, in SI units:

$$\varphi = 2.0 \times 1.6 \times 10^{-19} = 3.2 \times 10^{-19}\,\text{J}$$

That is the entire energy budget of one escaping electron — tiny on our scale, enormous on its own.

Now the field the USB port makes across $1\,\text{mm} = 1 \times 10^{-3}\,\text{m}$:

$$E = \frac{V}{d} = \frac{5}{1 \times 10^{-3}} = 5 \times 10^{3}\,\text{V/m}$$

Compare that with the $10^{8}\,\text{V/m}$ field emission needs:

$$\frac{10^{8}}{5 \times 10^{3}} = 2 \times 10^{4}$$

The USB field is about twenty thousand times too weak. Heat it is, then — which is exactly why the cabinet has a filament and takes eight seconds to think about it.

**Sanity check:** USB cables do not spray electrons into the room, so a field twenty thousand times short of the mark is the answer we should have expected.

## Where the picture breaks

The energy-shelf diagram is a simplification. Electrons in a metal do not sit on a few neat levels; they fill a continuous band, and the "highest filled level" is a statistical edge rather than a shelf. The barrier is not a sharp wall either — it softens over a few atomic diameters outside the surface.

Two honest caveats. Thermionic emission never actually switches off: even at room temperature a handful of electrons escape, just far too few to draw a picture. And $\varphi$ is not a number you look up once and trust forever — a fingerprint or a thin film of oxide shifts it, which is why these tubes are sealed and evacuated.

Gaming supplies the setting here, not an analogy. A picture tube and a camera sensor are real electron-emission devices sitting on a real desk; nothing about game mechanics maps onto an electron.

## Key takeaway

Free electrons are trapped inside a metal by a surface barrier, and the minimum energy needed to cross it is the **work function** $\varphi$, typically $2$–$5\,\text{eV}$. Heat, light, a very strong electric field or a particle impact can each pay that bill, giving thermionic, photoelectric, field and secondary emission. Whatever the source, no electron leaves until at least $\varphi$ has been handed over.
