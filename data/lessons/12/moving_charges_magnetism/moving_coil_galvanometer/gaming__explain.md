---
concept_id: moving_coil_galvanometer
interest: gaming
format: explain
title: The strip of copper that tamed a needle
check:
  question: |-
    Harsh also wants a second round meter on the cabinet, this one showing the supply **voltage**. He has an identical galvanometer of resistance $G$ that gives full-scale deflection at a current $I_g$. To turn it into a voltmeter reading up to $V$, what must he add?
  options:
    A: |-
      A resistance $V/I_g$ in parallel with it.
    B: |-
      A resistance $V/I_g - G$ in parallel with it.
    C: |-
      A resistance $I_g G/(V - I_g)$ in series with it.
    D: |-
      A resistance $V/I_g - G$ in series with it.
  answer: D
  explanation: |-
    At full scale the whole chain carries $I_g$, so the total resistance must be $V/I_g$. The galvanometer already supplies $G$ of it, leaving $R = V/I_g - G$ — and it goes in **series**, making the instrument's resistance high so it barely disturbs the circuit it is placed across.
  misconceptions:
    A: |-
      Borrows "in parallel" from the ammeter case and forgets that the galvanometer's own $G$ is already part of the chain. A voltmeter needs a large resistance in series, not a parallel one.
    B: |-
      Has the right value but the wrong connection. Wired in parallel, the combination's resistance falls *below* $G$ — the exact opposite of what a voltmeter needs.
    C: |-
      Mixes the ammeter's shunt formula into the voltmeter question, and ends up subtracting a current from a voltage. The expression is not even dimensionally sound, which is a useful warning sign.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A gaming workbench with a bartop arcade cabinet carrying a round analogue needle meter on its front panel, a cutaway of a pinball flipper coil, a controller with its shell off, a PC case fan, and a phone on a power cable](scenes/gaming/moving_charges_magnetism.svg "The round dial on the front of the arcade cabinet holds a coil, a magnet and a hairspring — and nothing electronic at all.")

Harsh wants one thing on the front of the club's arcade cabinet that nobody else's has: a real analogue meter, round glass and a swinging needle, showing how hard the machine is working. He finds one in the physics lab store, dusty, in a wooden box.

He wires it into the cabinet's supply, switches on, and the needle slams across to the end stop and stays there quivering. He switches off fast.

The lab technician is unimpressed but not surprised. That meter, he says, goes full scale at five milliamperes. The cabinet draws about two amperes.

Harsh does the division and is ready to give up. He is out by a factor of four hundred. The technician opens a drawer, takes out a short strip of copper no thicker than a paperclip, and says the meter will read two amperes perfectly with that soldered across the back of it.

A strip of metal — and a meter reads four hundred times more?

## The physics

Start with the instrument itself. A **moving coil galvanometer** is a coil of $N$ turns and area $A$ suspended in a magnetic field, with hairsprings that resist its rotation and a pointer fixed to it.

![The inside of a moving coil galvanometer: a coil on a soft iron core between curved pole pieces, with a spiral spring and a pointer, and the scale seen from outside](figures/moving_coil_galvanometer/galvanometer-construction.svg "The curved poles and the iron core make the field radial, so the coil's plane always contains B and the torque stays NIAB at every angle.")

Pass a current $I$ and the field twists the coil with the torque from the last lesson, $\tau = NIAB\sin\theta$. That $\sin\theta$ would ruin a measuring instrument: the same current would give different deflections depending on where the pointer already was. So the pole pieces are curved and a soft iron cylinder is placed inside the coil, which makes the field **radial** — $\vec{B}$ always lies in the plane of the coil, $\theta$ stays at $90°$, and the torque is simply $NIAB$ at every position.

The coil turns until the springs' restoring torque $k\phi$ balances it:

$$NIAB = k\phi \qquad\Longrightarrow\qquad \phi = \left(\frac{NAB}{k}\right)I$$

**The deflection is directly proportional to the current**, which is what makes the scale evenly spaced and readable. The bracket is the **current sensitivity** $\phi/I = NAB/k$; the **voltage sensitivity** is $\phi/V = NAB/(kG)$, where $G$ is the coil's own resistance.

On its own such a meter is useless in a real circuit: it takes a tiny current and its $G$ is large enough to disturb what it is measuring. So it gets converted.

![On the left, a galvanometer with a small shunt in parallel making an ammeter in series with the circuit; on the right, a galvanometer with a large resistance in series making a voltmeter across a component](figures/moving_coil_galvanometer/ammeter-and-voltmeter.svg "Ammeter: small shunt, joined in series, nearly zero resistance. Voltmeter: large series resistance, joined across the component, nearly infinite resistance.")

- **Ammeter:** a small resistance $S$ in **parallel** — a *shunt* — carries almost all the current and leaves the galvanometer its safe share. The pair has a very low resistance and goes in **series** with the circuit.
- **Voltmeter:** a large resistance $R$ in **series** limits the current so full-scale deflection matches full-scale voltage, $R = V/I_g - G$. The pair has a very high resistance and goes **across** the component.

The technician's strip of copper is a shunt. Same meter, new range.

## Worked example

**Given:** Harsh's galvanometer has resistance $G = 20\,\Omega$ and reads full scale at $I_g = 5.0\,\text{mA} = 0.0050\,\text{A}$.
**Find:** the shunt that makes it read up to $2.0\,\text{A}$.

**Step 1 — how much current must bypass the coil?** Of the $2.0\,\text{A}$ arriving, only $0.0050\,\text{A}$ may go through the galvanometer, so $1.995\,\text{A}$ — very nearly all of it — has to go round through the shunt.

**Step 2 — the shunt resistance.** The two branches are in parallel, so the same potential difference sits across both:

$$S \times 1.995 = 20 \times 0.0050 \qquad\Longrightarrow\qquad S = \frac{0.10}{1.995} \approx 0.050\,\Omega$$

**Step 3 — picture it.** Fifty milliohms is a short, thick strip of copper: barely more resistance than a piece of wire, which is exactly what the technician handed over. And that is precisely what an ammeter should be — almost invisible to the circuit it sits in.

**Sanity check:** the range went up four hundredfold, and the shunt came out about four hundred times smaller than $G$. The two factors matching is the pattern to expect.

## Where the picture breaks

The radial field is very good and not perfect, so a real meter's scale is slightly uneven at the extreme ends, and the movement is damped so the needle settles instead of swinging for ever.

Sensitivity cannot simply be cranked up either. Adding turns raises $NAB/k$, but more wire also raises $G$ — and $G$ sits in the denominator of the voltage sensitivity. A more sensitive galvanometer is not automatically a better voltmeter.

The shunt has a practical catch the formula hides: it carries nearly the whole current, so it has to be thick enough not to heat up and change its resistance. A hot shunt is a wrong reading.

And this movement responds to the **direction** of the current, so it reads direct current only. On alternating current the needle would be tugged both ways fifty times a second and simply sit near zero. Harsh has to wire his meter on the DC side of the cabinet's power supply, past the point where the mains has been turned into a steady voltage — the same side of the same supply that started the first lesson of this chapter.

## Key takeaway

A moving coil galvanometer balances the magnetic torque $NIAB$ on a coil against a spring's $k\phi$, in a **radial** field that keeps the torque the same at every angle — so the deflection $\phi = (NAB/k)I$ is proportional to the current and the scale is even. Add a small **shunt in parallel** to make an ammeter (low resistance, wired in series); add a large resistance **in series** to make a voltmeter (high resistance, wired across).
