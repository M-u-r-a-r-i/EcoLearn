---
concept_id: moving_coil_galvanometer
interest: cricket
format: explain
title: One needle, two instruments
check:
  question: |-
    A galvanometer of resistance $G$ is converted into an ammeter by connecting a small shunt resistance in parallel with it. What is true of the finished instrument?
  options:
    A: |-
      Its resistance is larger than $G$, and it is connected across the component being measured.
    B: |-
      Its resistance is larger than $G$, and it is connected in series with the circuit.
    C: |-
      Its resistance is smaller than $G$, and it is connected across the component being measured.
    D: |-
      Its resistance is smaller than $G$, and it is connected in series with the circuit.
  answer: D
  explanation: |-
    Two resistances in parallel always give less than either one, so the shunt makes the instrument's resistance very small — which is what lets an ammeter sit in series without changing the current it is measuring.
  misconceptions:
    A: |-
      Describes a voltmeter: large resistance, connected across a component. That is the other conversion, made with a large resistance in **series** with the galvanometer.
    B: |-
      Connects it correctly but gets the resistance backwards. Adding any resistor in parallel lowers the combined resistance below both of them.
    C: |-
      Gets the low resistance right but connects it like a voltmeter. An ammeter placed across a component would short it out and could destroy the meter.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A cricket ground with an electric roller, a compass lying on a thick power cable, a bowling machine and a loudspeaker on a pole](scenes/cricket/moving_charges_magnetism.svg "Every meter on this ground's panel is, underneath, a coil twisting in a magnetic field.")

The borehole pump that waters the square is controlled from a rusting steel panel behind the pavilion, and on that panel is a round dial with a needle that has been telling the groundsman how hard the pump is working since long before Aparna was born.

The contractor rewiring the panel wants to throw it out. Aparna asks to keep it, and opens the back to see what is inside.

There is no electronics at all. A small coil, hanging between two curved magnet poles, with a hair-thin spiral spring above and below it and a light pointer fixed to the top. The whole thing is the size of a matchbox.

And here is what puzzles her. The pump draws several amperes. The identical-looking meter in the school physics lab flicks off the scale at a *thousandth* of an ampere. Same magnet, same coil, same spring. How can the same instrument read two things that differ by a factor of a thousand?

## The physics

Start with the meter itself. A **moving coil galvanometer** is a coil of $N$ turns and area $A$ suspended in a magnetic field, with springs that resist its rotation.

![The inside of a moving coil galvanometer: a coil on a soft iron core between curved pole pieces, with a spiral spring and a pointer](figures/moving_coil_galvanometer/galvanometer-construction.svg "The curved poles and iron core make the field radial, so the coil's plane always contains B and the torque stays NIAB at every angle.")

Pass a current $I$ and the field exerts a couple on the coil, $\tau = NIAB\sin\theta$. That $\sin\theta$ would be a disaster for a measuring instrument — the same current would give different deflections at different angles. So the poles are curved and a soft iron cylinder is placed inside the coil, making the field **radial**: $\vec{B}$ always lies in the plane of the coil, $\theta$ stays at $90°$, and the torque is simply $NIAB$ wherever the pointer happens to be.

The coil turns until the springs' restoring torque $k\phi$ balances it:

$$NIAB = k\phi \qquad\Longrightarrow\qquad \phi = \left(\frac{NAB}{k}\right) I$$

**The deflection is directly proportional to the current** — which is what makes the scale evenly spaced and readable. The bracket is the **current sensitivity**, $\phi/I = NAB/k$; the **voltage sensitivity** is $\phi/V = NAB/(kG)$, where $G$ is the coil's own resistance.

A galvanometer on its own is useless in a real circuit: it takes only a tiny current, and $G$ is large enough to disturb what it is measuring. So it is converted.

![On the left, a galvanometer with a small shunt in parallel making an ammeter in series with the circuit; on the right, a galvanometer with a large resistance in series making a voltmeter across a component](figures/moving_coil_galvanometer/ammeter-and-voltmeter.svg "Ammeter: small shunt, in series, nearly zero resistance. Voltmeter: large series resistance, across the component, nearly infinite resistance.")

- **Ammeter:** a small resistance $S$ in **parallel** (a *shunt*) carries almost all the current, leaving the galvanometer its safe share. The combination has a very low resistance and goes in **series** with the circuit.
- **Voltmeter:** a large resistance $R$ in **series** limits the current so that the full-scale deflection corresponds to the full-scale voltage, $R = V/I_g - G$. The combination has a very high resistance and goes **across** the component.

So the panel meter and the lab meter really can be the same movement. Only what is wired around it differs.

## Worked example

**Given:** a galvanometer of resistance $100\,\Omega$ that reads full scale at $1.0\,\text{mA}$.
**Find:** the shunt needed to turn it into an ammeter reading up to $1.0\,\text{A}$.

**Step 1 — how much current must bypass the coil?** Of the $1.0\,\text{A}$ arriving, only $0.001\,\text{A}$ may go through the galvanometer, so $0.999\,\text{A}$ — very nearly all of it — must go through the shunt.

**Step 2 — the shunt resistance.** The two branches are in parallel, so they have the same potential difference across them:

$$S \times 0.999 = 100 \times 0.001 \qquad\Longrightarrow\qquad S = \frac{0.1}{0.999} \approx 0.10\,\Omega$$

A tenth of an ohm: a short, thick strip of metal, barely more than a piece of wire. That is exactly what you want — an ammeter should be almost invisible to the circuit it sits in.

**Sanity check:** the meter's range went up a thousandfold, and the shunt came out about a thousand times smaller than $G$, which is the pattern to expect.

## Where the picture breaks

The radial field is very good but not perfect, so a real meter's scale is slightly uneven at the extreme ends, and the needle is damped so it settles instead of swinging for ever.

Sensitivity cannot simply be cranked up, either. Adding turns raises $NAB/k$, but more wire also raises $G$ — so a more sensitive galvanometer is not automatically a better voltmeter, since voltage sensitivity carries $G$ in its denominator.

And this movement responds to the *direction* of the current, so it reads direct current only; on alternating current the needle would try to follow both directions and simply sit near zero. Aparna's panel meter and the lab galvanometer share a mechanism, but neither is the digital meter the contractor is holding, which measures a voltage electronically and displays a number.

## Key takeaway

A moving coil galvanometer balances the magnetic torque $NIAB$ on a coil against a spring's $k\phi$, in a **radial** field that keeps the torque the same at all angles — so the deflection $\phi = (NAB/k)I$ is proportional to the current. Add a small **shunt in parallel** to make an ammeter (low resistance, in series); add a large resistance **in series** to make a voltmeter (high resistance, across the component).
