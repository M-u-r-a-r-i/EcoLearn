---
concept_id: moving_coil_galvanometer
interest: football
format: explain
title: Two meters that look the same and are not
check:
  question: |-
    A galvanometer of resistance $50\,\Omega$ shows a full-scale deflection for a current of $2.0\,\text{mA}$. To convert it into a voltmeter reading up to $10\,\text{V}$, you must connect
  options:
    A: |-
      a small resistance of about $0.10\,\Omega$ in parallel with it.
    B: |-
      a large resistance of about $5000\,\Omega$ in parallel with it.
    C: |-
      a small resistance of about $0.10\,\Omega$ in series with it.
    D: |-
      a large resistance of about $4950\,\Omega$ in series with it.
  answer: D
  explanation: |-
    The coil may carry only $2.0\,\text{mA}$, so the rest of the $10\,\text{V}$ must fall across a resistance in series: $R = \dfrac{V}{I_g} - G = \dfrac{10}{0.0020} - 50 = 4950\,\Omega$. The series resistor also makes the voltmeter's resistance high, so it barely disturbs the circuit it measures.
  misconceptions:
    A: |-
      Builds an ammeter by mistake: a small resistance in parallel is the shunt that carries the extra current past the coil.
    B: |-
      Gets the size roughly right but connects it the wrong way. A *voltmeter* is connected in parallel with the component being measured; the big resistor inside it is in series with the coil.
    C: |-
      Mixes both halves up — the right connection with the shunt's value. A $0.10\,\Omega$ resistor in series would let the coil burn out long before $10\,\text{V}$.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A football ground with a coil traced around the goal frame, a pop-up sprinkler on a solenoid valve, an electric line-marking machine and a horn speaker on a pole with a compass lying on its supply cable](scenes/football/moving_charges_magnetism.svg "The supply box by the pole has two old panel meters on it — and underneath, they are the same instrument.")

The battery trolley that feeds the line marker has been left on charge all week, and Ishani has volunteered to check it before the tournament.

On the wall of the supply box hang two meters, salvaged from something older than she is. Same square case, same white face, same thin black needle, same little screw at the bottom. One is lettered **A**, the other **V**.

She clips the **A** meter straight across the battery terminals — it is a meter, after all, and she wants a reading. There is a crack, a smell of hot varnish, and the trolley's fuse is gone. The needle is bent against its stop.

The groundsman replaces the fuse and clips the **V** meter across the same terminals. It settles calmly at twelve volts.

Two instruments that look identical, wired the same way to the same battery. One reads; one destroys itself. What is different inside?

## The physics

Almost nothing. Both are the same **moving coil galvanometer**, with different resistors added.

A galvanometer is a coil of $N$ turns, wound on a light frame around a soft iron cylinder, hanging between the curved poles of a permanent magnet, with a hairspring at each end and a pointer on the shaft.

![The inside of a moving coil galvanometer: a coil on a soft iron core between curved pole pieces, with a spiral spring and a pointer](figures/moving_coil_galvanometer/galvanometer-construction.svg "The curved poles and iron core make the field radial, so the coil's plane always contains B and the torque stays NIAB at every angle.")

Send a current $I$ through it and, from the last lesson, the coil feels a torque $NIAB\sin\theta$. The springs twist back with a torque $k\phi$ proportional to the angle turned. The needle stops where the two balance.

The $\sin\theta$ would make the scale hopelessly uneven — so the designers get rid of it. The concave pole pieces and the iron core make the field **radial**: wherever the coil turns to, $\vec{B}$ still lies in its plane, so $\sin\theta = 1$ always. Then

$$NIAB = k\phi \qquad \Longrightarrow \qquad \phi = \left(\frac{NAB}{k}\right) I$$

The deflection is **directly proportional to the current**, which is why the scale is evenly spaced. The bracket is the **current sensitivity**: more turns, bigger area, stronger magnet or a weaker spring all make a twitchier meter.

The coil is fine wire, so a galvanometer takes only a milliamp or two and has a resistance $G$ of tens of ohms. Everything else is arithmetic:

![On the left, a galvanometer with a small shunt in parallel making an ammeter in series with the circuit; on the right, a galvanometer with a large resistance in series making a voltmeter across a component](figures/moving_coil_galvanometer/ammeter-and-voltmeter.svg "Ammeter: small shunt, connected in series with the circuit, nearly zero resistance. Voltmeter: large series resistance, connected across the component, nearly infinite resistance.")

- **Ammeter:** put a *small* resistance $S$ (a **shunt**) in **parallel** with the coil, so nearly all the current goes past it: $S = \dfrac{I_g G}{I - I_g}$. The whole thing has a tiny resistance and goes **in series** with the circuit.
- **Voltmeter:** put a *large* resistance $R$ in **series** with the coil, so only a trickle flows: $R = \dfrac{V}{I_g} - G$. The whole thing has a huge resistance and goes **across** the component.

Ishani's **A** meter had a fraction of an ohm across the battery. That is a short circuit, and the fuse did its job.

## Worked example

**Given:** a galvanometer with $G = 50\,\Omega$ and a full-scale current $I_g = 2.0\,\text{mA} = 0.0020\,\text{A}$.
**Find:** what to add to make it read $1.0\,\text{A}$, and what to add instead to make it read $10\,\text{V}$.

**Step 1 — the ammeter shunt.** The shunt must carry everything the coil cannot, at the same voltage:

$$S = \frac{I_g G}{I - I_g} = \frac{(0.0020)(50)}{1.0 - 0.0020} \approx 0.10\,\Omega$$

A tenth of an ohm — in practice a short stub of thick wire, which is exactly what you see bolted inside an ammeter.

**Step 2 — the voltmeter's series resistor.**

$$R = \frac{V}{I_g} - G = \frac{10}{0.0020} - 50 = 5000 - 50 = 4950\,\Omega$$

Nearly five thousand ohms. Set the two side by side — $0.1\,\Omega$ against $4950\,\Omega$ — and the two identical-looking meters are about fifty thousand times apart.

**Sanity check:** an ammeter should let current through as freely as a piece of wire, and a voltmeter should let through almost none. The two answers sit at exactly those extremes.

## Where the picture breaks

No meter is free. An ammeter adds a small resistance to the circuit it is measuring and a voltmeter draws a small current out of it, so both change the thing they read, slightly. The design aim is to make that change too small to matter, never to abolish it.

The radial field is also only radial in the working region between the poles. Push the needle far past full scale — as Ishani did — and neither the linear scale nor the springs can be trusted again.

And a moving coil meter reads **direct current only**. On a.c. the coil is twisted one way and then the other fifty times a second; it cannot follow, and reads zero. Meters for a.c. rectify the current first.

## Key takeaway

A moving coil galvanometer balances the magnetic torque $NIAB$ on a coil against a spring's $k\phi$, in a radial field that keeps the torque the same at every angle — so the deflection is proportional to the current. Add a small **shunt in parallel** and it becomes an ammeter; add a large resistance **in series** and it becomes a voltmeter.
