---
concept_id: electron_emission
interest: cricket
format: explain
title: Why the old commentary radio had to warm up first
check:
  question: |-
    A metal used in a light meter has a work function of $2.5\,\text{eV}$. What does that number mean?
  options:
    A: |-
      Every free electron inside the metal already carries $2.5\,\text{eV}$ of energy.
    B: |-
      An electron at the top of the filled levels needs at least $2.5\,\text{eV}$ of extra energy to get out of the metal.
    C: |-
      An electron that escapes from the surface leaves with $2.5\,\text{eV}$ of kinetic energy.
    D: |-
      The surface emits electrons once the light falling on it has delivered $2.5\,\text{eV}$ in total, however slowly it arrives.
  answer: B
  explanation: |-
    The work function is the *minimum* extra energy an electron must be given to escape the surface. Anything more than $\varphi$ becomes kinetic energy once it is out.
  misconceptions:
    A: |-
      Confuses the height of the escape barrier with the energy the electrons already have. The work function is the gap still to be climbed, not a store the electrons are carrying.
    C: |-
      Confuses $\varphi$ with the kinetic energy of the escaped electron. An electron given exactly $\varphi$ just barely gets out, with no kinetic energy left; only the excess above $\varphi$ becomes kinetic energy.
    D: |-
      The idea that energy can be collected slowly and added up until it reaches $\varphi$. Energy arrives in whole packets, and one electron takes one packet, so a weak beam of the wrong colour never works no matter how long you wait.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A floodlit cricket ground at night, with a light beam drawn half as a wave and half as a stream of packets, an umpire holding a light meter and a tracking camera on a tripod](scenes/cricket/dual_nature.svg "Every light sensor at this ground — the meter, the camera — starts with electrons being knocked out of a metal.")

Aarav's grandfather refuses to watch the match on the television. He carries a wooden radio out to the veranda, sets it on the stool, and switches it on — and nothing happens. No commentary, no crowd. Just silence.

"Wait," the old man says.

Twenty seconds later an orange glow appears behind the grille, and a voice arrives mid-sentence: *"...and that's beaten the outside edge."*

Aarav looks through the vents. Inside are glass tubes, and inside each tube a thin wire glowing like a filament. The radio only works once those wires are hot.

His grandfather shrugs: "It has to warm up." But why? What is heat doing inside a sealed glass tube that electricity alone can't do?

## The physics

A metal is full of **free electrons** — they wander between the atoms, which is why metals conduct. But wandering *inside* is not the same as getting *out*. At the surface, the positive ions of the metal pull an escaping electron back. An electron trying to leave has to climb an energy barrier.

The **work function** $\varphi$ of a metal is the minimum energy that must be supplied to a free electron to just free it from the surface.

![An energy diagram: filled electron levels inside a metal, a dashed vacuum level above, and a green arrow marking the work function gap between them](figures/electron_emission/work-function-barrier.svg "The work function is the gap from the highest filled level up to the outside world — the toll every escaping electron must pay.")

It is measured in **electron volts**, where

$$1\,\text{eV} = 1.6 \times 10^{-19}\,\text{J}$$

and for most metals $\varphi$ lies between about $2\,\text{eV}$ and $5\,\text{eV}$. It depends on the metal *and* on the state of its surface — a clean surface and an oxidised one give different values, which is why the cathodes in vacuum tubes are specially coated to keep $\varphi$ low.

Nothing happens until that energy is supplied. There are four standard ways to supply it:

![Four panels showing thermionic, photoelectric, field and secondary emission, each freeing electrons from a metal surface](figures/electron_emission/emission-methods.svg "Four different energy sources, one identical bill to pay: the work function.")

- **Thermionic emission** — heat the metal. Raise the temperature enough and a few electrons in the thermal spread have more than $\varphi$ and boil off. This is the glowing filament in your grandfather's radio.
- **Photoelectric emission** — shine light on it. A packet of light hands its energy to a single electron.
- **Field emission** — apply a very strong electric field (of order $10^8\,\text{V/m}$), usually at a sharp tip, and electrons are dragged straight out.
- **Secondary emission** — hit the surface with fast particles, which knock further electrons loose.

The umpire's light meter uses the second one, and that is where this chapter is going.

## Worked example

**Given:** a cathode coating with work function $\varphi = 2.5\,\text{eV}$.
**Find:** that energy in joules, and whether room temperature could supply it.

$$\varphi = 2.5 \times 1.6 \times 10^{-19}\,\text{J} = 4.0 \times 10^{-19}\,\text{J}$$

So freeing one electron costs four ten-billion-billionths of a joule — tiny on our scale, but it is the whole budget of a single electron.

At room temperature the typical thermal energy available to a particle is only about $0.026\,\text{eV}$. Compare the two:

$$\frac{2.5}{0.026} \approx 100$$

The barrier is about a hundred times the energy on offer. That is why the radio must warm up: only at a glowing-hot filament does a useful number of electrons have enough.

**Sanity check:** metal spoons sitting in a hot cup of tea do not spray electrons into the room, so room temperature being far short of the barrier is exactly what we should expect.

## Where the picture breaks

The energy-shelf diagram is a simplification. Electrons in a metal do not sit on a few neat levels; they fill a continuous band, and the "highest filled level" is a statistical edge, not a shelf. The barrier itself is not a sharp wall either — it softens over a few atomic diameters outside the surface.

Two more honest caveats. Even at room temperature a handful of electrons *do* escape — thermionic emission never switches off, it just becomes negligibly small. And $\varphi$ is not a fixed property you can look up once: a fingerprint or a thin oxide layer changes it, which is why photocells are sealed in evacuated tubes.

The cricket here is only the setting. Radios and light meters live at a ground, but there is no analogy between a batter and an electron — this is a case for learning the physics directly.

## Key takeaway

Free electrons are trapped inside a metal by a surface barrier, and the minimum energy needed to escape it is the **work function** $\varphi$, typically $2$–$5\,\text{eV}$. Heat, light, a strong electric field or a particle impact can each pay that bill — giving thermionic, photoelectric, field and secondary emission. Whatever the source, no electron leaves until at least $\varphi$ has been supplied.
