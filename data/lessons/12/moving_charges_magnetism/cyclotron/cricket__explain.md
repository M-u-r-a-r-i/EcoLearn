---
concept_id: cyclotron
interest: cricket
format: explain
title: The machine in the hospital basement
check:
  question: |-
    A cyclotron is tuned to accelerate protons. A deuteron has the same charge as a proton but twice the mass. To accelerate deuterons in the same magnetic field, the frequency of the alternating voltage across the gap must be
  options:
    A: |-
      doubled.
    B: |-
      left unchanged.
    C: |-
      made four times smaller.
    D: |-
      halved.
  answer: D
  explanation: |-
    The cyclotron frequency is $f = qB/(2\pi m)$. The charge and the field are the same, the mass is doubled, so $f$ is halved — the heavier particle takes twice as long to go round.
  misconceptions:
    A: |-
      Inverts the dependence, thinking a heavier particle must be pushed faster. Mass is in the denominator: more mass means a *slower* circulation.
    B: |-
      Remembers that the frequency does not depend on the speed or the radius, and over-generalises that to "it depends only on $B$". It also depends on the charge-to-mass ratio $q/m$.
    C: |-
      Applies the mass factor twice, as if $f \propto 1/m^{2}$. The period is directly proportional to $m$, not to $m^{2}$.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A cricket ground with an electric roller, a compass lying on a thick power cable, a bowling machine and a loudspeaker on a pole](scenes/cricket/moving_charges_magnetism.svg "The physics on this ground also runs the scanner that checks a bowler's stress fracture.")

Farhan has bowled through a dull ache in his lower back for half a season, and the club doctor has finally sent him for a scan. Before it, a nurse injects a small dose of something and tells him to sit still for an hour.

His mother asks what is in the syringe. A radioactive tracer, the nurse says — and it was made this morning, in the basement of this building, in a machine the size of a kitchen table. It has to be used today, because it fades away in a couple of hours.

Farhan cannot let that go. Radioactive material that has to be *made on the spot*, in a basement, because it will not survive the journey? What is down there?

A **cyclotron** — and it works by spinning charged particles up to enormous speed with nothing but a magnetic field and a voltage that keeps changing its mind.

## The physics

The hard part of accelerating a particle is that a single voltage can only push it once. A cyclotron gets around this by making the particle come back for another push, over and over, using the one fact from the last lesson:

$$T = \frac{2\pi m}{qB}$$

**The time for one turn does not depend on the speed.** A slow particle takes a small circle, a fast one a big circle, and both arrive back in the same time.

![Two hollow D-shaped chambers with a gap between them, a source at the centre, the field pointing out of the page, and a spiral path growing outwards to a fast beam](figures/cyclotron/cyclotron-dees.svg "Inside a dee the particle only turns. It gains energy each time it crosses the gap — which is why the spiral gets wider.")

Two hollow metal **dees** sit in a strong magnetic field, in a vacuum, with a narrow gap between them. Inside a dee there is no electric field, so the particle simply curves round a half-circle. Across the gap there *is* an electric field, and that is where the work is done.

The trick is timing. An alternating voltage flips the polarity of the gap at exactly the rate the particle circulates, so the gap is always pulling the particle forward as it arrives, never pushing it back. That matching condition — the **resonance condition** — is

$$f = \frac{qB}{2\pi m}$$

called the **cyclotron frequency**.

Each crossing of the gap adds energy, so $v$ grows, so $r = mv/(qB)$ grows — and the path becomes an outward spiral of ever wider half-circles taking equal times. When the spiral reaches the edge of the dees, at radius $R$, the beam is deflected out at its top speed:

$$v_\text{max} = \frac{qBR}{m}$$

Fired at a target, that beam converts stable atoms into short-lived radioactive ones — which is why the tracer in Farhan's arm was made a few hundred metres from where it was injected.

## Worked example

**Given:** a cyclotron accelerating protons ($m = 1.7 \times 10^{-27}\,\text{kg}$, $q = 1.6 \times 10^{-19}\,\text{C}$) in a field of $1.0\,\text{T}$, with dees of radius $0.50\,\text{m}$.
**Find:** the frequency the supply must run at, and the speed of the beam that comes out.

**Step 1 — the frequency.**

$$f = \frac{qB}{2\pi m} = \frac{(1.6 \times 10^{-19})(1.0)}{2\pi (1.7 \times 10^{-27})} \approx 1.5 \times 10^{7}\,\text{Hz}$$

About $15\,\text{MHz}$ — the supply has to change direction fifteen million times a second, which is an ordinary radio frequency.

**Step 2 — the exit speed.**

$$v_\text{max} = \frac{qBR}{m} = \frac{(1.6 \times 10^{-19})(1.0)(0.50)}{1.7 \times 10^{-27}} \approx 4.7 \times 10^{7}\,\text{m/s}$$

That is roughly a sixth of the speed of light: the proton crosses a cricket pitch about two million times in the second it takes you to blink.

**Sanity check:** a radio-frequency supply and a beam a good fraction of light speed are both what you would expect of a machine that fits in a basement yet makes new isotopes — neither number is absurd.

## Where the picture breaks

The cyclotron's whole design rests on the period staying constant, and at the speeds in Step 2 that is starting to be a lie. As a particle approaches light speed its effective mass grows, the turns take longer, and it drifts out of step with the supply. That sets a ceiling on a plain cyclotron; machines that push further have to change the frequency or the field as the beam speeds up.

Two more limits. The particle must be **charged** — a cyclotron cannot accelerate a neutron. And electrons are hopeless in one, because they are so light that they reach relativistic speeds almost immediately.

Finally, the spiral in the diagram is drawn with only a few loops for clarity. A real beam may go round many hundreds of times, each half-circle taking exactly as long as the first.

## Key takeaway

A cyclotron accelerates a charged particle by letting a magnetic field bend it back to the same gap again and again, while an alternating voltage flips in time with it. It works because the period $T = 2\pi m/(qB)$ is independent of speed, so one fixed **cyclotron frequency** $f = qB/(2\pi m)$ stays in step from the first turn to the last.
