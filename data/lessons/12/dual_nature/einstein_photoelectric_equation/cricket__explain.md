---
concept_id: einstein_photoelectric_equation
interest: cricket
format: explain
title: Choosing the metal for a bad-light alarm
check:
  question: |-
    An emitter has a work function of $2.0\,\text{eV}$. Light whose photons carry $5.0\,\text{eV}$ falls on it. The light is then changed so that each photon carries $10.0\,\text{eV}$. What happens to the maximum kinetic energy of the photoelectrons?
  options:
    A: |-
      It rises from $3.0\,\text{eV}$ to $8.0\,\text{eV}$ — a factor of about $2.7$.
    B: |-
      It doubles, from $3.0\,\text{eV}$ to $6.0\,\text{eV}$.
    C: |-
      It doubles, from $5.0\,\text{eV}$ to $10.0\,\text{eV}$.
    D: |-
      It stays at $3.0\,\text{eV}$; only the number of electrons emitted changes.
  answer: A
  explanation: |-
    $K_\text{max} = h\nu - \varphi$, so the work function is subtracted each time: $5.0 - 2.0 = 3.0\,\text{eV}$ becomes $10.0 - 2.0 = 8.0\,\text{eV}$, a factor of $8/3 \approx 2.7$.
  misconceptions:
    B: |-
      Treats $K_\text{max}$ as proportional to $h\nu$, so doubling the photon energy is assumed to double $K_\text{max}$. The work function is a fixed subtraction, not a fixed fraction, so doubling $h\nu$ more than doubles what is left.
    C: |-
      Forgets the work function altogether and sets $K_\text{max} = h\nu$. Some of every photon's energy is always spent getting the electron out of the metal.
    D: |-
      Swaps the roles of frequency and intensity, treating frequency as the thing that sets how many electrons come out. Frequency sets their energy; intensity sets their number.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A floodlit cricket ground at night, with a light beam drawn half as a wave and half as a stream of packets, an umpire holding a light meter and a tracking camera on a tripod](scenes/cricket/dual_nature.svg "Somewhere in every light sensor, a metal has to decide whether the arriving light is energetic enough.")

Ananya wants to fix an argument that starts at her club every single evening: whether the light is still good enough to bat. Her science-fair plan is a small box on the boundary rope with a photocell inside — light falls off below a set level, a buzzer sounds, everyone goes home without shouting.

The catalogue page for the photocell is one line long. Emitter material, then a number: **work function 2.1 eV**. That is all.

Her partner Vikram is doubtful. "At six o'clock the light out there is orange. Will your cell even notice orange light?"

Ananya has one afternoon before the order closes, no photocell to test, and exactly one number to work with. Can she answer him from that alone?

## The physics

In 1905 Einstein proposed that light is not only emitted and absorbed in lumps, but *travels* in them. A beam of frequency $\nu$ is a stream of packets — **photons** — each carrying energy

$$E = h\nu$$

where $h = 6.63 \times 10^{-34}\,\text{J s}$ is Planck's constant. In the photoelectric effect **one photon is absorbed by one electron**, all of its energy at once. There is no saving up.

That electron must pay the work function $\varphi$ to get out. Whatever is left over it keeps as kinetic energy. An electron from deeper in the metal loses more on the way out, so the best any electron can do is

$$K_\text{max} = h\nu - \varphi$$

which is **Einstein's photoelectric equation**.

![Two energy bars: one photon's energy splitting into the work function plus leftover kinetic energy, and below it a smaller photon that cannot cover the work function at all](figures/einstein_photoelectric_equation/photon-energy-budget.svg "The work function is a fixed bill. Anything above it becomes speed; anything below it buys nothing at all.")

Three results follow immediately, and they are exactly the four observations from the previous lesson.

**Threshold.** $K_\text{max}$ cannot be negative, so emission needs $h\nu \ge \varphi$. The **threshold frequency** is

$$\nu_0 = \frac{\varphi}{h} \qquad \text{and the threshold wavelength} \qquad \lambda_0 = \frac{hc}{\varphi}$$

**Stopping potential.** Since $K_\text{max} = eV_0$,

$$eV_0 = h\nu - \varphi$$

so a graph of $V_0$ against $\nu$ is a straight line of slope $h/e$ — the *same* slope for every metal, with only the intercept moving. Millikan measured that slope carefully in 1916 and got Planck's constant out of it, which is a large part of why Einstein received the 1921 Nobel Prize for this work rather than for relativity.

![A graph of stopping potential against frequency: two parallel straight lines for two metals, cutting the frequency axis at different threshold frequencies](figures/einstein_photoelectric_equation/stopping-potential-vs-frequency.svg "Different metals, different starting points — but identical slope, because that slope is h/e.")

**Intensity.** More intensity means more photons per second, hence more electrons per second, but each photon is unchanged — so the saturation current rises and $V_0$ does not.

One shortcut is worth memorising. Since $hc = 6.63\times10^{-34} \times 3.00\times10^{8} = 1.99\times10^{-25}\,\text{J m}$, dividing by $1.6\times10^{-19}$ gives $hc \approx 1240\,\text{eV nm}$, so

$$E\,(\text{in eV}) = \frac{1240}{\lambda\,(\text{in nm})}$$

## Worked example

**Given:** Ananya's photocell has $\varphi = 2.1\,\text{eV}$. She tests it with violet light of wavelength $400\,\text{nm}$.
**Find:** the maximum kinetic energy of the photoelectrons and the stopping potential — and then, the longest wavelength the cell responds to at all.

Each photon first:

$$E = \frac{1240}{400} = 3.1\,\text{eV}$$

So every violet packet arrives carrying $3.1\,\text{eV}$ — comfortably more than the $2.1\,\text{eV}$ toll.

Now the change left over:

$$K_\text{max} = 3.1 - 2.1 = 1.0\,\text{eV}$$

Two-thirds of the photon's energy went on the escape; one-third became speed.

And the stopping potential, since $K_\text{max} = eV_0$ with $K_\text{max}$ in electron volts:

$$V_0 = 1.0\,\text{V}$$

Finally, Vikram's question. The longest wavelength that still just pays the bill is

$$\lambda_0 = \frac{1240}{2.1} \approx 590\,\text{nm}$$

which is yellow. Orange and red light — anything longer than about $590\,\text{nm}$ — will do nothing at all. Ananya needs a lower-work-function cell, or a different sensor.

**Sanity check:** a single torch cell would stop these electrons, and a photocell that ignores red light is exactly the kind of thing you would expect from a metal with a yellow threshold.

## Where the picture breaks

The "one photon, one electron" rule is the heart of the equation, and it holds for ordinary light sources — but with a focused high-power laser an electron can absorb two photons at once, and light below $\nu_0$ then does free electrons. That is real physics, just beyond this syllabus.

$K_\text{max}$ is a *maximum*, not a typical value. Most photoelectrons come out slower, because they started deeper in the metal and lost energy reaching the surface. The stopping potential measures only the best of them.

And the work function quoted in a catalogue is for a clean surface. A real cell ages: a film of oxide or grease shifts $\varphi$, so Ananya's alarm would need recalibrating, not just designing once.

Cricket sets the problem here — a real club argument, a real device — but the physics is not an analogy for anything on the field.

## Key takeaway

Einstein's equation is one line of bookkeeping: $K_\text{max} = h\nu - \varphi$. The photon brings $h\nu$, the metal takes $\varphi$, and the electron keeps the difference as kinetic energy, measurable as $eV_0$. Below the threshold $\nu_0 = \varphi/h$ there is no difference to keep, so nothing comes out at all.
