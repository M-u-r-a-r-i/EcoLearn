---
concept_id: einstein_photoelectric_equation
interest: football
format: explain
title: The goal-line beam that could not be seen
check:
  question: |-
    Two emitters, metal X with $\varphi = 2.0\,\text{eV}$ and metal Y with $\varphi = 3.0\,\text{eV}$, are each tested over a range of frequencies and a graph of stopping potential against frequency is plotted for both. Which statement is correct?
  options:
    A: |-
      X's line is steeper, because its lower work function lets its electrons gain energy faster.
    B: |-
      Y's line is steeper, because more energy has to be supplied to free its electrons.
    C: |-
      The two lines are parallel, and Y's cuts the frequency axis at a lower frequency than X's.
    D: |-
      The two lines are parallel, and Y's cuts the frequency axis at a higher frequency than X's.
  answer: D
  explanation: |-
    Rearranging $eV_0 = h\nu - \varphi$ gives $V_0 = (h/e)\nu - \varphi/e$: the slope is $h/e$ for every metal, so the lines are parallel, and the intercept $\nu_0 = \varphi/h$ is larger for the larger work function.
  misconceptions:
    A: |-
      Treats the work function as setting how quickly $K_\text{max}$ grows with frequency. It doesn't — $\varphi$ is subtracted once, so it shifts the line sideways and never tilts it.
    B: |-
      The same confusion pointing the other way: a bigger $\varphi$ is read as a steeper climb. The slope belongs to Planck's constant alone, which is exactly why Millikan could measure $h$ from it.
    C: |-
      Gets the parallel lines right but inverts the threshold. Since $\nu_0 = \varphi/h$, the metal that holds its electrons more tightly needs a *higher* frequency before anything is emitted.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A floodlit football ground at night, with an inset panel drawing the same beam once as a wave and once as a stream of packets, a goal-line camera on a pole, a goalkeeper and a ball](scenes/football/dual_nature.svg "Somewhere inside every light sensor, a metal has to decide whether the arriving light is energetic enough.")

Ronit's school has a pitch, a goal, and the same argument every break time about whether the ball crossed the line. He has decided to end it with electronics: an invisible beam strung across the goalmouth, a detector on the far post, a buzzer when the beam is broken.

The source is sorted. He has a near-infrared LED, the same kind that sits in a television remote — invisible, cheap, already in his drawer.

The detector is the problem. The catalogue page for the vacuum photocell he can afford gives one useful number: **work function 2.0 eV**. That is all it says.

Vaishali reads it over his shoulder and is not convinced. "Your beam is infrared. Can that thing even *see* infrared?"

Ronit has one afternoon before the order closes, no photocell to test with, and exactly one number to reason from.

## The physics

In 1905 Einstein proposed that light is not merely emitted and absorbed in lumps but *travels* in them. A beam of frequency $\nu$ is a stream of **photons**, each carrying energy

$$E = h\nu$$

where $h = 6.63 \times 10^{-34}\,\text{J s}$ is Planck's constant. In the photoelectric effect **one photon is absorbed by one electron**, all of its energy at once. There is no saving up over time.

That electron must then pay the work function $\varphi$ to get out, and keeps whatever is left as kinetic energy. An electron starting deeper inside loses more on the way, so the best any electron can manage is

$$K_\text{max} = h\nu - \varphi$$

which is **Einstein's photoelectric equation**.

![Two energy bars: one photon's energy splitting into the work function plus leftover kinetic energy, and below it a smaller photon that cannot cover the work function at all](figures/einstein_photoelectric_equation/photon-energy-budget.svg "The work function is a fixed bill. Anything above it becomes speed; anything below it buys nothing at all.")

Three consequences fall straight out, and they are precisely the observations of the last lesson.

**Threshold.** $K_\text{max}$ cannot be negative, so emission needs $h\nu \ge \varphi$. The **threshold frequency** and wavelength are

$$\nu_0 = \frac{\varphi}{h} \qquad\text{and}\qquad \lambda_0 = \frac{hc}{\varphi}$$

**Stopping potential.** Since $K_\text{max} = eV_0$, we get $eV_0 = h\nu - \varphi$, so a graph of $V_0$ against $\nu$ is a straight line of slope $h/e$ — the *same* slope for every metal, with only the intercept moving. Millikan measured that slope carefully in 1916 and extracted Planck's constant from it.

![A graph of stopping potential against frequency: two parallel straight lines for two metals, cutting the frequency axis at different threshold frequencies](figures/einstein_photoelectric_equation/stopping-potential-vs-frequency.svg "Different metals, different starting points — but identical slope, because that slope is h/e.")

**Intensity.** Brighter light means more photons per second and so more electrons per second, but each photon is unchanged: the saturation current rises and $V_0$ does not.

One shortcut is worth memorising. Since $hc = 6.63\times10^{-34} \times 3.00\times10^{8} = 1.99\times10^{-25}\,\text{J m}$, dividing by $1.6\times10^{-19}$ gives $hc \approx 1240\,\text{eV nm}$, so

$$E\,(\text{in eV}) = \frac{1240}{\lambda\,(\text{in nm})}$$

## Worked example

**Given:** Ronit's photocell has $\varphi = 2.0\,\text{eV}$. Take his infrared LED's wavelength as $1240\,\text{nm}$ — a round value that keeps the arithmetic clean; real remote-control LEDs are a little shorter, near $900\,\text{nm}$.

**Find:** whether the infrared beam frees any electrons, and the longest wavelength that would.

One infrared photon carries

$$E = \frac{1240}{1240} = 1.0\,\text{eV}$$

which is half the toll. It does not matter how many arrive: one photon is absorbed by one electron, and $1.0\,\text{eV}$ cannot buy a $2.0\,\text{eV}$ escape. The beam could be blindingly intense and the meter would still read zero. (A real $900\,\text{nm}$ LED gives $1240/900 \approx 1.4\,\text{eV}$ — still short.)

The longest wavelength that just pays the bill is

$$\lambda_0 = \frac{1240}{2.0} = 620\,\text{nm}$$

That is orange-red. Anything longer than about $620\,\text{nm}$ — all of the infrared included — does nothing at all to this cell.

So Ronit's answer to Vaishali is no. His options are a visible or ultraviolet beam, or a different detector: the receiver in a television remote is a semiconductor photodiode, where the energy an electron must be given is far smaller than a metal's work function.

**Sanity check:** a photocell that ignores infrared is exactly what you would expect from a metal whose threshold sits in the orange — and it is why a vacuum photocell makes a poor night-vision sensor.

## Where the picture breaks

"One photon, one electron" is the heart of the equation, and it holds for ordinary sources — but a focused high-power laser can deliver two photons to one electron at once, and light below $\nu_0$ then does free electrons. Real physics, just beyond this syllabus.

$K_\text{max}$ is a *maximum*, not a typical value. Most photoelectrons emerge slower, having started deeper in the metal. The stopping potential measures only the best of them.

And a catalogue work function is for a clean surface in vacuum. A real cell ages; a film of oxide shifts $\varphi$, so Ronit's detector would need recalibrating, not just designing once.

Football sets the problem here — a real argument on a real pitch, and a device a student could actually build — but the physics is not an analogy for anything that happens to the ball.

## Key takeaway

Einstein's equation is one line of bookkeeping: $K_\text{max} = h\nu - \varphi$. The photon brings $h\nu$, the metal takes $\varphi$, and the electron keeps the difference, measurable as $eV_0$. Below the threshold $\nu_0 = \varphi/h$ there is no difference to keep, so nothing is emitted however bright the light.
