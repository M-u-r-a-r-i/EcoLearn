---
concept_id: einstein_photoelectric_equation
interest: gaming
format: explain
title: Picking the sensor tube for a light-gun cabinet
check:
  question: |-
    The sensor tube in a restored cabinet has a photocathode of work function $1.5\,\text{eV}$. Ultraviolet light of wavelength $310\,\text{nm}$, whose photons carry $4.0\,\text{eV}$ each, falls on it. What is the stopping potential?
  options:
    A: |-
      $4.0\,\text{V}$
    B: |-
      $5.5\,\text{V}$
    C: |-
      $1.5\,\text{V}$
    D: |-
      $2.5\,\text{V}$
  answer: D
  explanation: |-
    $eV_0 = K_\text{max} = h\nu - \varphi = 4.0 - 1.5 = 2.5\,\text{eV}$, and with $K_\text{max}$ in electron volts the stopping potential is numerically the same: $V_0 = 2.5\,\text{V}$.
  misconceptions:
    A: |-
      Sets $K_\text{max} = h\nu$ and forgets the work function. Part of every photon's energy is always spent getting the electron out of the metal.
    B: |-
      Adds the work function instead of subtracting it. $\varphi$ is a cost paid out of the photon's energy, not an extra supply added to it.
    C: |-
      Quotes the work function itself as the stopping potential. $\varphi$ is what the electron spends; $eV_0$ is what it has left afterwards.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A gaming room shown in three stages: a cut-away retro CRT cabinet with a glowing filament and an electron beam, a flat monitor whose light leaves as a wave and then as packets, and a camera sensor feeding a current to a meter](scenes/gaming/dual_nature.svg "Somewhere in every light sensor, a metal is deciding whether the arriving light is energetic enough.")

The retro corner of the club now has a light-gun cabinet in pieces on a table. Rhea has the gun itself open. Behind the muzzle sits a small evacuated tube — the sensor that decides, when you pull the trigger, whether you hit anything on the screen. It is cracked.

The replacement catalogue describes each tube in one line: a photocathode material, then a number. **Work function 2.0 eV.** That is all it says.

Tushar is holding the only light source in the room they can test with tonight: a deep red indicator LED, $620\,\text{nm}$ printed on its bag.

"If the tube sees red, we can check the whole gun before we order anything."

Rhea is not convinced it will see red. She has one number from the catalogue, one number from the bag, and a shop that is shut until Monday. Can she settle it from that alone?

## The physics

In 1905 Einstein proposed that light is not merely emitted and absorbed in lumps — it *travels* in them. A beam of frequency $\nu$ is a stream of packets, **photons**, each carrying

$$E = h\nu$$

with $h = 6.63 \times 10^{-34}\,\text{J s}$, Planck's constant. In the photoelectric effect **one photon is absorbed by one electron**, all of its energy at once. There is no pooling and no saving up.

That electron then has to pay the work function $\varphi$ to get out. Whatever is left over it keeps as kinetic energy. An electron starting deeper in the metal loses more on the way to the surface, so the best any electron can manage is

$$K_\text{max} = h\nu - \varphi$$

which is **Einstein's photoelectric equation**.

![Two energy bars: one photon's energy splitting into the work function plus leftover kinetic energy, and below it a smaller photon that cannot cover the work function at all](figures/einstein_photoelectric_equation/photon-energy-budget.svg "The work function is a fixed bill. Anything above it becomes speed; anything below it buys nothing at all.")

Three consequences follow at once, and they are exactly the observations from the last lesson.

**Threshold.** $K_\text{max}$ cannot be negative, so emission needs $h\nu \ge \varphi$. The **threshold frequency** and **threshold wavelength** are

$$\nu_0 = \frac{\varphi}{h} \qquad \text{and} \qquad \lambda_0 = \frac{hc}{\varphi}$$

**Stopping potential.** Since $K_\text{max} = eV_0$,

$$eV_0 = h\nu - \varphi$$

so a graph of $V_0$ against $\nu$ is a straight line of slope $h/e$ — the *same* slope for every metal, with only the intercept moving. Millikan measured that slope carefully in 1916 and extracted Planck's constant from it, which is a large part of why Einstein's 1921 Nobel Prize was awarded for this work rather than for relativity.

![A graph of stopping potential against frequency: two parallel straight lines for two metals, cutting the frequency axis at different threshold frequencies](figures/einstein_photoelectric_equation/stopping-potential-vs-frequency.svg "Different metals, different starting points — but identical slope, because that slope is h/e.")

**Intensity.** More intensity means more photons each second, so more electrons each second, but every photon is unchanged — the saturation current rises and $V_0$ does not.

One shortcut is worth memorising. Since $hc = 6.63\times10^{-34} \times 3.00\times10^{8} = 1.99\times10^{-25}\,\text{J m}$, dividing by $1.6\times10^{-19}$ gives $hc \approx 1240\,\text{eV nm}$, so

$$E\,(\text{in eV}) = \frac{1240}{\lambda\,(\text{in nm})}$$

## Worked example

**Given:** the catalogue tube has $\varphi = 2.0\,\text{eV}$. Rhea first works out what violet light of $400\,\text{nm}$ would do to it.
**Find:** the maximum kinetic energy and the stopping potential — and then the longest wavelength the tube responds to at all.

Each violet photon first:

$$E = \frac{1240}{400} = 3.1\,\text{eV}$$

Comfortably more than the $2.0\,\text{eV}$ toll, so electrons will come out.

Now the change left over after paying it:

$$K_\text{max} = 3.1 - 2.0 = 1.1\,\text{eV}$$

About two-thirds of the photon's energy went on the escape; the remaining third became speed. And since $K_\text{max} = eV_0$, with $K_\text{max}$ in electron volts,

$$V_0 = 1.1\,\text{V}$$

Finally, Tushar's LED. The longest wavelength that still just covers the bill is

$$\lambda_0 = \frac{1240}{2.0} = 620\,\text{nm}$$

which is exactly where his deep red LED sits. Photons of $620\,\text{nm}$ carry precisely $2.0\,\text{eV}$ — enough to free an electron with nothing whatever left over, so the tube would give no useful current, and anything redder than that would do nothing at all. Their test tonight would have proved nothing about the gun.

**Sanity check:** a single torch cell would stop these photoelectrons, and a tube that is blind to red is exactly what a metal with a red threshold should be.

## Where the picture breaks

"One photon, one electron" is the heart of the equation and holds for ordinary light sources — but with a focused high-power laser an electron can absorb two photons at once, and light below $\nu_0$ then does free electrons. Real physics, just beyond this syllabus.

$K_\text{max}$ is a *maximum*, not a typical value. Most photoelectrons emerge slower, having started deeper in the metal; the stopping potential only ever measures the best of them.

And a catalogue work function is for a clean surface. Real tubes age — a film of oxide or a fingerprint shifts $\varphi$ — so a restored cabinet would need testing, not just calculating.

Gaming sets the problem here: a real device, a real decision, a real number on a real data sheet. It is not an analogy for anything happening inside the game.

## Key takeaway

Einstein's equation is one line of bookkeeping: $K_\text{max} = h\nu - \varphi$. The photon brings $h\nu$, the surface takes $\varphi$, and the electron keeps the difference as kinetic energy, measurable as $eV_0$. Below the threshold $\nu_0 = \varphi/h$ there is no difference left to keep, so nothing comes out at all.
