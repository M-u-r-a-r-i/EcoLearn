---
concept_id: cyclotron
interest: smartphones
format: explain
title: The radio transmitter that makes protons fast
check:
  question: |-
    A cyclotron's oscillator runs at about $15\,\text{MHz}$ to accelerate protons. The operators now want to accelerate **deuterons** — same charge as a proton, about **twice** the mass — using the **same** magnetic field. What should the oscillator frequency be set to?
  options:
    A: |-
      About $15\,\text{MHz}$, the same as before
    B: |-
      About $30\,\text{MHz}$
    C: |-
      About $7.5\,\text{MHz}$
    D: |-
      About $7.5\,\text{MHz}$ at first, raised steadily as the deuterons speed up
  answer: C
  explanation: |-
    The cyclotron frequency is $f_c = \dfrac{qB}{2\pi m}$. With the same $q$ and $B$ and twice the mass, $f_c$ halves: $15\,\text{MHz}/2 = 7.5\,\text{MHz}$. It does not depend on the speed, so it stays fixed during the whole acceleration.
  misconceptions:
    A: |-
      Thinks the frequency is set by the magnetic field alone. $f_c = qB/(2\pi m)$ also depends on the particle's charge-to-mass ratio, so a heavier particle needs a lower frequency.
    B: |-
      Inverts the dependence on mass. A heavier particle turns *more slowly* in the same field, so each half-circle takes longer and the voltage must flip less often.
    D: |-
      Thinks faster particles need a faster oscillator. The time for each half-circle, $\pi m/(qB)$, does not depend on speed: a faster particle simply runs round a bigger semicircle in the same time.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A desk with a phone lying on a charging cable showing a swung compass arrow, a wireless charging pad with its coil exposed, a flip-cover case with a small magnet in its flap, and a speaker and a small cylinder-shaped vibration motor taken apart](scenes/smartphones/moving_charges_magnetism.svg "Every gadget here combines a magnetic field with a current or an oscillating signal. The cyclotron does the same, on a far bigger scale.")

Ishita's aunt is a medical physicist at a big hospital, and on a holiday visit she takes Ishita down to the basement to see "the machine". It is a squat metal drum the size of a car, behind thick concrete walls. Each morning it makes a short-lived tracer that is injected into patients before a scan.

"It's basically a huge magnet with a radio transmitter bolted on," her aunt says. "The transmitter is the part that speeds up the protons."

Ishita, who listens to FM radio on her phone every day, is not convinced. A radio signal is just a voltage wiggling back and forth millions of times a second. Push a proton one way, then the other way, then back again — surely it ends up going nowhere.

So how can a wiggling signal make protons go faster and faster, until they are racing at a good fraction of the speed of light?

## The physics

A **cyclotron** makes a small voltage do a huge job by using it again and again. It combines two things from this chapter.

**The magnetic field turns the particle.** Two hollow D-shaped metal chambers (the **dees**) sit between the poles of a big magnet, with a narrow gap between them. Inside a dee there is no electric field, so a proton simply moves in a semicircle under the magnetic force.

**The gap speeds it up.** An oscillator applies an alternating voltage across the gap. Each time the proton crosses, the voltage is timed to push it forwards, and it gains a little energy.

![Two hollow D-shaped chambers with a gap between them, a source at the centre, the field pointing out of the page, and a spiral path growing outwards to a fast beam](figures/cyclotron/cyclotron-dees.svg "Inside a dee the particle only turns. It gains energy only in the gap — and each half-turn, the voltage there has flipped to push it forwards again.")

The trick that makes the timing possible comes from the last lesson: the time for a circle, $T = 2\pi m/(qB)$, **does not depend on speed**. As the proton speeds up it swings out on bigger semicircles, but each semicircle takes exactly the same time. So a voltage that flips at one fixed frequency stays in step for the whole ride. That frequency is the **cyclotron frequency**:

$$f_c = \frac{qB}{2\pi m}$$

and the oscillator must be tuned to match it — the **resonance condition**, $f_a = f_c$.

The particle leaves when its path reaches the edge, radius $R$. Setting $r = mv/(qB) = R$ gives its final speed $v = qBR/m$, and its kinetic energy

$$K = \frac{1}{2}mv^{2} = \frac{q^{2}B^{2}R^{2}}{2m}$$

Notice that $K$ does not depend on the gap voltage: a small voltage just means more laps.

## Worked example

**Given:** protons ($m = 1.67\times10^{-27}\,\text{kg}$, $q = 1.6\times10^{-19}\,\text{C}$) in a field $B = 1.0\,\text{T}$; the dees have radius $R = 0.50\,\text{m}$ (illustrative values).
**Find:** the oscillator frequency, the final speed, and the final energy.

**Step 1 — the frequency.**

$$f_c = \frac{qB}{2\pi m} = \frac{1.6\times10^{-19}\times1.0}{2\pi\times1.67\times10^{-27}} \approx 1.5\times10^{7}\,\text{Hz} = 15\,\text{MHz}$$

That is a genuine radio frequency — in the shortwave band, well below the FM stations (around $100\,\text{MHz}$) that Ishita's phone tunes to.

**Step 2 — the final speed.**

$$v = \frac{qBR}{m} = \frac{1.6\times10^{-19}\times1.0\times0.50}{1.67\times10^{-27}} \approx 4.8\times10^{7}\,\text{m/s}$$

About one-sixth of the speed of light. At that pace, the proton could go once around the Earth in under a second.

**Step 3 — the final energy.**

$$K = \frac{1}{2}mv^{2} = \frac{1}{2}(1.67\times10^{-27})(4.8\times10^{7})^{2} \approx 1.9\times10^{-12}\,\text{J} \approx 12\,\text{MeV}$$

**Sanity check:** a gap voltage of tens of kilovolts, crossed twice per lap, reaches $12\,\text{MeV}$ in a few hundred laps — which is why the path is a spiral with many turns.

## Where the picture breaks

The link to Ishita's phone is only the frequency. A phone's radio *receives* weak signals; the cyclotron's oscillator drives a powerful voltage across the gap. They share the idea of an oscillating signal and nothing else.

The formula $T = 2\pi m/(qB)$ holds only while the particle is well below light speed. At one-sixth of it, the error is about one per cent; much faster, and the particle's effective mass grows, its turns take longer, and it falls out of step with a fixed-frequency oscillator. That sets a cyclotron's upper limit.

A cyclotron also cannot accelerate electrons usefully: they are so light that they approach light speed almost at once.

## Key takeaway

A cyclotron accelerates charged particles by making them circle in a magnetic field and giving them a push each time they cross a gap. It works because the time for a turn does not depend on speed, so an oscillator at the fixed **cyclotron frequency** $f_c = \dfrac{qB}{2\pi m}$ stays in step for the whole spiral. The final energy, $\dfrac{q^{2}B^{2}R^{2}}{2m}$, is set by the field and the size of the dees.
