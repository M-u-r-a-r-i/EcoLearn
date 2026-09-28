---
concept_id: einstein_photoelectric_equation
interest: smartphones
format: explain
title: Building a UV sensor that ignores the room lights
check:
  question: |-
    Light falls on an emitter whose work function is $2.5\,\text{eV}$. The stopping potential is measured as $1.5\,\text{V}$. What energy does each photon of this light carry?
  options:
    A: |-
      $1.5\,\text{eV}$
    B: |-
      $1.0\,\text{eV}$
    C: |-
      $4.0\,\text{eV}$
    D: |-
      $2.5\,\text{eV}$
  answer: C
  explanation: |-
    From $h\nu = \varphi_0 + eV_0$, each photon pays the $2.5\,\text{eV}$ work function and still leaves the fastest electron with $1.5\,\text{eV}$, so $h\nu = 2.5 + 1.5 = 4.0\,\text{eV}$.
  misconceptions:
    A: |-
      Forgets the work function and sets $h\nu = eV_0$. The stopping potential measures only what the electron keeps after escaping, not the whole photon.
    B: |-
      Subtracts instead of adds, as if $h\nu = \varphi_0 - eV_0$. A photon with only $1.0\,\text{eV}$ could not even pay the $2.5\,\text{eV}$ work function, so no electrons would come out.
    D: |-
      Assumes the photon energy always equals the work function. That is true only at the threshold frequency, where the electrons leave with no kinetic energy and the stopping potential would be zero.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A phone beside a sunny window, its screen showing a UV-index meter, its flashlight beam drawn half as a wave and half as a stream of packets, and a magnified camera pixel where light frees electrons](scenes/smartphones/dual_nature.svg "The UV number on the phone is a forecast. To measure it, you need a sensor that knows ultraviolet from ordinary light.")

Siddharth's weather app in Jaipur shows a big orange "UV 9" every afternoon in May. One day he reads the small print: the app estimates the number from a forecast. Nothing in his phone is actually measuring ultraviolet.

So he decides to build a clip-on UV sensor for his science project: a small photocell that plugs into the phone and should react to sunlight's ultraviolet, but *not* to the tube lights in his classroom or the glow of the phone's own screen.

A parts catalogue lists photocells that differ in only one thing: the emitter metal, with its work function printed next to it — $2.0\,\text{eV}$, $3.0\,\text{eV}$, $4.5\,\text{eV}$.

His friend Zoya shrugs. "Just buy the most sensitive one."

But the most sensitive one might be the worst choice. Which number should he pick — and what would it do in real sunlight?

## The physics

In 1905 Einstein proposed that light is not only emitted and absorbed in packets but *travels* as them. Light of frequency $\nu$ is a stream of **photons**, each carrying energy

$$E = h\nu$$

where $h = 6.63\times10^{-34}\,\text{J s}$ is Planck's constant. When light meets a metal, **one photon gives all its energy to one electron**, at once.

The electron spends at least the work function $\varphi_0$ getting out, and keeps the rest as kinetic energy. The luckiest electrons, from right at the surface, spend exactly $\varphi_0$, so

$$K_\text{max} = h\nu - \varphi_0$$

This is **Einstein's photoelectric equation**.

![Two energy bars: one photon's energy splitting into the work function plus leftover kinetic energy, and below it a smaller photon that cannot cover the work function at all](figures/einstein_photoelectric_equation/photon-energy-budget.svg "The work function is a fixed bill. Anything above it becomes speed; anything below it buys nothing at all.")

Everything in the last lesson falls out of it.

- **Threshold.** $K_\text{max}$ cannot be negative, so emission needs $h\nu \ge \varphi_0$. The **threshold frequency** is $\nu_0 = \varphi_0 / h$, and the matching **threshold wavelength** is $\lambda_0 = c/\nu_0 = hc/\varphi_0$.
- **Stopping potential.** Since $K_\text{max} = eV_0$,
$$eV_0 = h\nu - \varphi_0$$
  so $V_0$ rises in a straight line with $\nu$, with slope $h/e$ — the same slope for every metal.
- **Intensity.** Brighter light means more photons per second, so more electrons, but each photon is the same. So intensity changes the current and not $V_0$.
- **No delay.** One photon does the whole job, so there is nothing to wait for.

![A graph of stopping potential against frequency: two parallel straight lines for two metals, cutting the frequency axis at different threshold frequencies](figures/einstein_photoelectric_equation/stopping-potential-vs-frequency.svg "Different metals, different starting points — but identical slope, because that slope is h/e.")

A shortcut saves a lot of arithmetic. Since $hc = 1.99\times10^{-25}\,\text{J m}$, which is about $1240\,\text{eV nm}$,

$$E\,(\text{in eV}) = \frac{1240}{\lambda\,(\text{in nm})}$$

Visible light runs from about $400\,\text{nm}$ (violet, $3.1\,\text{eV}$) to about $700\,\text{nm}$ (red, $1.8\,\text{eV}$).

## Worked example

**Given:** Siddharth picks the cell with $\varphi_0 = 3.0\,\text{eV}$ and tests it with ultraviolet of wavelength $310\,\text{nm}$.
**Find:** $K_\text{max}$, the stopping potential, and the threshold frequency.

First, each photon:

$$E = \frac{1240}{310} = 4.0\,\text{eV}$$

Every UV packet brings $4.0\,\text{eV}$ — more than the $3.0\,\text{eV}$ toll.

What is left for the electron:

$$K_\text{max} = 4.0 - 3.0 = 1.0\,\text{eV}$$

So the stopping potential is $V_0 = 1.0\,\text{V}$.

Now the threshold, in SI units:

$$\nu_0 = \frac{\varphi_0}{h} = \frac{3.0 \times 1.6\times10^{-19}}{6.63\times10^{-34}} \approx 7.2\times10^{14}\,\text{Hz}$$

That frequency is a wavelength of $c/\nu_0 \approx 410\,\text{nm}$ — the violet edge of the visible range. Almost all the light from classroom lamps and the phone screen has longer wavelengths than this, so those photons cannot free a single electron.

**Sanity check:** the $2.0\,\text{eV}$ cell Zoya liked would have a threshold near $620\,\text{nm}$, orange-red, so it would react to almost every lamp in the room — sensitive, and useless for this job.

## Where the picture breaks

The $3.0\,\text{eV}$ cell's threshold sits right at the violet edge, so a little deep-violet light still gets through. A real design would pick a slightly higher work function or add a filter that blocks visible light.

"One photon, one electron" holds for ordinary light. With a very intense focused laser, an electron can absorb two photons at once — real physics, but outside this syllabus.

$K_\text{max}$ is the *best* case. Most electrons start deeper in the metal and leave slower, and a dirty or oxidised surface changes $\varphi_0$, so a real sensor needs calibrating.

## Key takeaway

Einstein's equation is energy bookkeeping for one photon and one electron: $K_\text{max} = h\nu - \varphi_0 = eV_0$. The photon brings $h\nu$, the metal takes $\varphi_0$, and the electron keeps the difference. Below the threshold frequency $\nu_0 = \varphi_0/h$ there is nothing left over, so no electrons come out, however bright the light.
