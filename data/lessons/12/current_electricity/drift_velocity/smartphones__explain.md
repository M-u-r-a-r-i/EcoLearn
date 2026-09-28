---
concept_id: drift_velocity
interest: smartphones
format: explain
title: The electrons that take an hour to cross a charging cable
check:
  question: |-
    A charging cable's copper conductor is replaced by one of the same copper with **twice** the cross-sectional area, and it carries the same current. What happens to the drift velocity of the electrons?
  options:
    A: |-
      it doubles
    B: |-
      it stays the same
    C: |-
      it falls to a quarter
    D: |-
      it halves
  answer: D
  explanation: |-
    From $I = neAv_d$, $v_d = \dfrac{I}{neA}$. With $I$, $n$ and $e$ unchanged, doubling $A$ halves $v_d$: the same flow of charge is spread over twice as many electrons in each slice of wire.
  misconceptions:
    A: |-
      Pictures a wider wire as a faster, freer path. A wider conductor does carry current more easily, but at the same current each electron needs to move only half as fast.
    B: |-
      Treats drift velocity as a fixed property of copper, like its density. It depends on the current and the area as well as on the material.
    C: |-
      Applies the square-of-the-diameter rule to the area. It is the *area* that has doubled, and $v_d$ is inversely proportional to the area itself, so it halves.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A charging corner: a phone on a wall charger, a power bank charging an earbuds case through a small USB meter, and a smartwatch on its charging puck, with current arrows on the cables](scenes/smartphones/current_electricity.svg "The phone lights up the moment the plug goes in — yet the electrons in that cable are barely moving.")

Kabir has read something in a physics forum that he refuses to believe. The electrons in a charging cable, the post said, crawl along more slowly than a snail — a fraction of a millimetre per second.

"Rubbish," he tells his cousin Riya. He holds up his phone, dead after a long day, and pushes the plug in. The charging icon appears instantly. "One metre of cable. If the electrons took forever, the phone would have to wait."

Riya has a counter-question. "And the charger says two amps. Two coulombs a second through a wire thinner than a pencil lead. If they were slow, how would so much charge get through?"

Both of them are pointing at something true. The phone does react at once. Charge does pour through. So how fast are the electrons in the cable really going — and how can a slow crawl carry so much?

## The physics

Every free electron in the copper already moves very fast — around $10^5\,\text{m/s}$ — but in random directions, bouncing off the vibrating ions. Averaged over all of them, that motion adds up to zero.

Connect the cable to a charger and an electric field $E$ is set up along the wire almost instantly. Between collisions each electron is accelerated slightly *against* the field, then loses that gained velocity in its next collision. The result is a slow, steady average creep superimposed on the random motion: the **drift velocity** $v_d$. If $\tau$ is the average time between collisions,

$$v_d = \frac{eE\tau}{m}$$

![An electron's zigzag path through a wire, with a small net drift opposite to the applied field](figures/drift_velocity/drift-velocity-zigzag.svg "The zigzag is fast and random; the slow net creep it adds up to is the drift velocity.")

How readily a carrier drifts in a given field is its **mobility**:

$$\mu = \frac{v_d}{E} = \frac{e\tau}{m}$$

measured in $\text{m}^2\,\text{V}^{-1}\,\text{s}^{-1}$.

**Linking drift to current.** Take a wire of cross-sectional area $A$ with $n$ free electrons per cubic metre. In time $t$ every electron moves forward $v_d t$, so all the electrons in a slab of length $v_d t$ cross the end. That slab holds $nAv_d t$ electrons, carrying charge $Q = neAv_d t$. Dividing by $t$:

$$I = neAv_d$$

![A wire with a marked cross-section and the slab of electrons that crosses it in a given time](figures/electric_current/current-as-charge-flow.svg "The charge in a slab of length v_d t crosses the end in time t — which is where I = neAv_d comes from.")

This resolves the argument. The phone responds at once because the *field* is set up along the cable at a large fraction of the speed of light, pushing every electron in the loop at the same moment. And a slow drift carries a large current because $n$ is enormous.

## Worked example

**Given:** each power conductor in Kabir's cable has area $A = 0.5\,\text{mm}^2 = 5 \times 10^{-7}\,\text{m}^2$ and carries $I = 2.0\,\text{A}$. Copper has about $n = 8.5 \times 10^{28}$ free electrons per cubic metre.
**Find:** the drift velocity, and how long an electron takes to drift the length of a $1\,\text{m}$ cable.

First, how much current one metre-per-second of drift would give, $neA$:

$$neA = 8.5 \times 10^{28} \times 1.6 \times 10^{-19} \times 5 \times 10^{-7} = 6800\,\text{C/m}$$

So the drift velocity is

$$v_d = \frac{I}{neA} = \frac{2.0}{6800} \approx 2.9 \times 10^{-4}\,\text{m/s}$$

About $0.3\,\text{mm}$ per second — the width of a pencil line each second.

To cross one metre: $t = \dfrac{1}{2.9 \times 10^{-4}} \approx 3400\,\text{s}$, just under an hour.

**Sanity check:** the forum post said "slower than a snail", and a snail manages about a millimetre a second — so a third of that is the right size.

## Where the picture breaks

The charging cable is real physics, not an analogy, but the model is simplified. Treating every electron as sharing one average collision time $\tau$ is a classical picture; the full explanation of conduction in metals needs quantum physics, well beyond this chapter.

Also, a phone charger's cable carries direct current, so the electrons do drift steadily one way. On a mains cable, which carries alternating current, they only jiggle back and forth by a tiny distance and never make the journey at all. And the "hour" is for one electron on average — none of them needs to arrive for the phone to charge, because energy is carried by the field, not by the electrons' travel.

## Key takeaway

Free electrons move fast but randomly; an applied field adds a slow average creep, the drift velocity $v_d = eE\tau/m$, and mobility is $\mu = v_d/E$. Counting the electrons that cross a cross-section gives $I = neAv_d$: a tiny drift carries a large current because copper holds an enormous number of free electrons.
