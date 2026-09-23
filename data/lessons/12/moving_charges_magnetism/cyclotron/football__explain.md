---
concept_id: cyclotron
interest: football
format: explain
title: The appointment that cannot be moved
check:
  question: |-
    A cyclotron is running with a fixed magnetic field and a supply of fixed frequency. As a proton gains energy on each crossing of the gap, which statement describes its motion correctly?
  options:
    A: |-
      The supply frequency has to be raised steadily to keep up with the faster proton.
    B: |-
      The radius of each half-circle stays the same, because the magnetic field is unchanged.
    C: |-
      Each half-circle takes less time than the one before, because the proton is faster.
    D: |-
      Each half-circle is wider than the one before, but takes exactly the same time.
  answer: D
  explanation: |-
    The radius $r = mv/(qB)$ grows with the speed, but the period $T = 2\pi m/(qB)$ does not contain $v$ at all — so the proton sweeps a wider arc in the same time, and one fixed frequency stays in step from the first turn to the last.
  misconceptions:
    A: |-
      Assumes a faster particle must be pushed more often. It travels further each turn in exactly the same time, which is the reason a *fixed* frequency works.
    B: |-
      Treats the field as fixing the radius by itself. The field fixes the *period*; the radius depends on the momentum, and grows every time the proton is accelerated.
    C: |-
      Uses "faster means quicker" without noticing that the path lengthens by the same factor. Speed and circumference grow together, so the lap time is unchanged.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A football ground with a coil traced around the goal frame, a pop-up sprinkler on a solenoid valve, an electric line-marking machine and a horn speaker on a pole with a compass lying on its supply cable](scenes/football/moving_charges_magnetism.svg "The academy's machines run on currents and magnets — and so does the scanner that will look inside a defender's knee.")

Ritu is three weeks into a physiotherapy placement at a football academy, and she has been given one simple job: get a centre-back with a stubborn knee to the hospital for a scan.

The appointment is 11:40. Not 11:30, not noon. When the team bus is delayed and she phones to ask for a later slot, the answer is no — not "the doctor is busy", but *that scan cannot happen this afternoon at all*. The next one is in four days.

The substance the player is injected with, the radiographer explains, was made this morning in the building next door. It weakens by the hour. Nobody can store it, nobody can post it, and there is no point making extra.

A medicine that has to be manufactured a few hundred metres from the patient, on the morning it is used. What kind of machine makes something like that — and why does it have to be so close?

## The physics

A **cyclotron**: a machine the size of a kitchen table that accelerates protons to a few per cent of the speed of light and fires them at a target, turning ordinary atoms into short-lived radioactive ones.

The hard part of accelerating a charge is that one voltage can push it only once. A cyclotron solves that by bringing the particle back for another push, over and over, using the one fact from the last lesson:

$$T = \frac{2\pi m}{qB}$$

**The time for one turn does not depend on the speed.** A slow particle takes a tight circle, a fast one a wide circle, and both come back in the same time.

![Two hollow D-shaped chambers with a gap between them, a source at the centre, the field pointing out of the page, and a spiral path growing outwards to a fast beam](figures/cyclotron/cyclotron-dees.svg "Inside a dee the particle only turns. It gains energy each time it crosses the gap — which is why the spiral gets wider.")

Two hollow metal **dees** sit in a strong magnetic field, in a vacuum, with a narrow gap between them. Inside a dee there is no electric field, so the proton merely curves round a half-circle. Across the gap there *is* an electric field, and that is where every bit of the work is done.

The trick is timing. An alternating voltage reverses the gap's polarity at exactly the rate the particle circulates, so the gap is always pulling the proton forward as it arrives and never pushing it back. That matching condition is the **resonance condition**:

$$f = \frac{qB}{2\pi m}$$

called the **cyclotron frequency**. Notice what is *not* in it: the speed and the radius. That is the whole design.

Each crossing adds energy, so $v$ grows, so $r = mv/(qB)$ grows, and the path opens into a spiral of ever wider half-circles that each take the same time. At the rim of the dees, at radius $R$, the beam leaves at

$$v_\text{max} = \frac{qBR}{m}$$

## Worked example

**Given:** a cyclotron accelerating protons ($m = 1.7 \times 10^{-27}\,\text{kg}$, $q = 1.6 \times 10^{-19}\,\text{C}$) in a field of $0.50\,\text{T}$, with dees of radius $0.40\,\text{m}$.
**Find:** the frequency the supply must run at, and the speed of the beam that comes out.

**Step 1 — the frequency.**

$$f = \frac{qB}{2\pi m} = \frac{(1.6 \times 10^{-19})(0.50)}{2\pi\,(1.7 \times 10^{-27})} \approx 7.5 \times 10^{6}\,\text{Hz}$$

About $7.5\,\text{MHz}$: the supply reverses seven and a half million times a second, an ordinary radio frequency.

**Step 2 — the exit speed.**

$$v_\text{max} = \frac{qBR}{m} = \frac{(1.6 \times 10^{-19})(0.50)(0.40)}{1.7 \times 10^{-27}} \approx 1.9 \times 10^{7}\,\text{m/s}$$

That is about six per cent of the speed of light — fast enough to cross a full-length pitch something like two hundred thousand times in a second.

**Sanity check:** a radio-frequency supply and a beam at a few per cent of light speed are both what you would expect of a machine that fits in a basement and still makes new isotopes. Neither number is absurd.

## Where the picture breaks

The design rests on the period staying constant, and near the exit speed that is beginning to be a lie. As a particle approaches light speed its effective mass grows, its turns take longer, and it drifts out of step with the supply. That sets a ceiling on a plain cyclotron; machines that go further have to change the frequency or the field as the beam speeds up.

Two other limits. The particle must be **charged** — a cyclotron cannot accelerate a neutron. And electrons are hopeless in one: they are so light that they turn relativistic almost immediately.

Finally, the spiral in the diagram has a handful of loops for clarity. A real beam may go round hundreds of times, every half-circle taking as long as the first.

## Key takeaway

A cyclotron accelerates a charged particle by letting a magnetic field bend it back to the same gap again and again while an alternating voltage flips in time with it. It works only because $T = 2\pi m/(qB)$ is independent of speed, so one fixed **cyclotron frequency** $f = qB/(2\pi m)$ stays in step throughout.
