---
concept_id: cyclotron
interest: gaming
format: explain
title: The machine whose note never rises
check:
  question: |-
    In a cyclotron, which field does the work on the particle, and what fixes the energy it finally leaves with?
  options:
    A: |-
      The magnetic field does the work each time the particle curves round inside a dee.
    B: |-
      The electric field across the gap does the work, and the final energy is fixed by the gap voltage — double the voltage and you double the energy of the beam.
    C: |-
      Both fields do work; the magnetic field's share is what makes the spiral widen turn by turn.
    D: |-
      The electric field across the gap does all the work, and the final energy is fixed by the magnetic field and the radius of the dees, not by the gap voltage.
  answer: D
  explanation: |-
    Inside a dee there is no electric field, and the magnetic force is perpendicular to $\vec{v}$, so it does no work at all. Every joule is gained crossing the gap — but the particle leaves when its radius reaches the rim, at $v_\text{max} = qBR/m$. A bigger gap voltage only means fewer crossings are needed to get there.
  misconceptions:
    A: |-
      Thinks the field that bends the path must also be the one that speeds it up. A magnetic force is always perpendicular to the velocity, so it can only steer, never do work.
    B: |-
      Confuses "what supplies the energy" with "what limits it". The gap voltage sets the energy gained *per crossing*; the exit energy is capped by the dees, at $q^{2}B^{2}R^{2}/2m$.
    C: |-
      Believes the widening spiral is caused by the magnetic field pushing outwards. The spiral widens because $v$ has grown and $r = mv/(qB)$ grows with it — the magnetic force still points inwards, to the centre.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A gaming workbench with a bartop arcade cabinet, a cutaway of a pinball flipper coil, a controller with its shell off, a PC case fan, and a phone on a power cable showing a swung compass needle](scenes/gaming/moving_charges_magnetism.svg "The same two ingredients as everything on this bench — a current and a magnetic field — scaled up until they can build new atoms.")

Rohit's game-jam team has four days and a level set in an abandoned accelerator lab. He has built the whole room around one prop: a flat circular chamber, waist high, split down the middle, with a beam pipe leading off its rim.

Anjali is doing the sound, and she objects to the machinery hum he has looped over it. "If the particle inside is speeding up all the way round, the hum should climb," she says. "Yours is flat. It sounds fake."

Rohit agrees and rebuilds it as a rising whine, faster and faster as the spiral widens. Their mentor walks past the screen, listens for ten seconds and tells him to put the flat hum back.

Both of them are certain. The particle really does speed up, turn after turn. So why should the machine's note stay on one pitch?

## The physics

Because of one surprising result from the last lesson. For a charge circling in a uniform field,

$$T = \frac{2\pi m}{qB}$$

**The time for one turn does not depend on the speed.** A slow particle takes a small circle, a fast one a wide circle, and both arrive back in the same time. That single fact is what makes a cyclotron possible.

The problem a cyclotron solves is that one voltage can only push a particle once. So it brings the particle back for another push, over and over.

![Two hollow D-shaped chambers with a gap between them, a source at the centre, the field pointing out of the page, and a spiral path growing outwards to a fast beam](figures/cyclotron/cyclotron-dees.svg "Inside a dee the particle only turns. It gains energy each time it crosses the gap — which is why the spiral gets wider.")

Two hollow metal **dees** sit in a strong magnetic field, in a vacuum, with a narrow gap between them. Inside a dee there is no electric field, so the particle just curves round a half-circle at constant speed. Across the gap there *is* an electric field, and that is the only place work is done.

The trick is timing. An alternating voltage flips the polarity of the gap at exactly the rate the particle circulates, so the gap is always pulling it forward as it arrives and never pushing it back. Matching those two rates is the **resonance condition**:

$$f = \frac{qB}{2\pi m}$$

the **cyclotron frequency**. It contains no $v$ and no $r$ — which is Anjali's answer. The supply runs at one fixed frequency from the first turn to the last, and the note does not climb.

Each gap crossing adds energy, so $v$ grows, so $r = mv/(qB)$ grows, and the path becomes an outward spiral of ever wider half-circles that all take the same time. When it reaches the rim of the dees, at radius $R$, the beam is kicked out at

$$v_\text{max} = \frac{qBR}{m}$$

Notice what is *not* in that expression: the gap voltage. A bigger voltage gets the particle to the rim in fewer turns, but not out of it any faster.

## Worked example

**Given:** a cyclotron accelerating protons ($m = 1.7\times10^{-27}\,\text{kg}$, $q = 1.6\times10^{-19}\,\text{C}$) in a field of $0.50\,\text{T}$, with dees of radius $0.40\,\text{m}$.
**Find:** the frequency the supply must run at, and the speed of the beam that leaves.

**Step 1 — the frequency.**

$$f = \frac{qB}{2\pi m} = \frac{(1.6\times10^{-19})(0.50)}{2\pi(1.7\times10^{-27})} = \frac{8.0\times10^{-20}}{1.07\times10^{-26}} \approx 7.5\times10^{6}\,\text{Hz}$$

About $7.5\,\text{MHz}$ — an ordinary radio frequency, and a fixed one.

**Step 2 — the exit speed.**

$$v_\text{max} = \frac{qBR}{m} = \frac{(1.6\times10^{-19})(0.50)(0.40)}{1.7\times10^{-27}} \approx 1.9\times10^{7}\,\text{m/s}$$

Roughly 6% of the speed of light.

**Step 3 — put the frequency in something you can picture.** One frame of a game at 60 frames per second lasts about $16.7\,\text{ms}$. In that single frame the cyclotron's supply changes its mind about $125{,}000$ times — all at the same steady pitch.

**Sanity check:** a radio-frequency supply and a beam a few per cent of light speed are both what you would expect of a machine that fits in a room and still makes new isotopes. Neither number is absurd.

## Where the picture breaks

The whole design rests on $T$ staying constant, and near light speed that quietly stops being true: the particle's effective mass grows, the turns take longer, and it drifts out of step with the supply. That puts a ceiling on a plain cyclotron. Machines that push past it have to sweep the frequency or ramp the field as the beam speeds up — and *those* really would give Rohit a rising note.

Two more limits. The particle must be **charged**: a cyclotron can do nothing with a neutron. And electrons are hopeless in one, because they are so light that a few crossings already take them close to light speed.

The spiral in the diagram is also drawn with a handful of loops for clarity. A real beam may go round many hundreds of times, every half-circle taking exactly as long as the first.

## Key takeaway

A cyclotron accelerates a charged particle by letting a magnetic field bend it back to the same gap again and again, while an alternating voltage flips in time with it. It works because the period $T = \dfrac{2\pi m}{qB}$ is independent of speed, so one fixed **cyclotron frequency** $f = \dfrac{qB}{2\pi m}$ stays in step throughout. All the work is done in the gap; the exit speed $qBR/m$ is set by the magnet and the dees.
