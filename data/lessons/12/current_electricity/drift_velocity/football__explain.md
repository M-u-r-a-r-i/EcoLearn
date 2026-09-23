---
concept_id: drift_velocity
interest: football
format: explain
title: The floodlights come on before the electrons have gone anywhere
check:
  question: |-
    The current in a floodlight cable is doubled, while the cable itself is unchanged. The drift velocity of its free electrons:
  options:
    A: |-
      stays the same — drift velocity is fixed by the metal
    B: |-
      doubles
    C: |-
      halves
    D: |-
      becomes four times as large
  answer: B
  explanation: |-
    From $I = neAv_d$, the quantities $n$, $e$ and $A$ are all fixed by the cable, so $v_d$ is directly proportional to $I$. Twice the current means twice the drift velocity.
  misconceptions:
    A: |-
      Confuses drift velocity with the electrons' random thermal speed, which really is set by the metal and its temperature. Drift velocity is set by the current and the wire's geometry.
    C: |-
      Reads $I = neAv_d$ as though $I$ and $v_d$ were on the same side, so that one must fall when the other rises. They are on opposite sides: $v_d = I/(neA)$.
    D: |-
      Squares the current, probably borrowing the $I^2$ from the heating formula $P = I^2R$. Current enters $I = neAv_d$ to the first power only.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A floodlit football ground at night with two lit pylons, an electronic scoreboard, a fourth official holding a glowing LED substitution board, and a pitch-side distribution box with cables running to the lights](scenes/football/current_electricity.svg "The switch is at the tunnel; the far pylon is most of a pitch-length away, at the end of a long buried cable.")

Everyone has gone home. Kabir and Nandini have the keys and one job: kill the floodlights and lock the gate. The switch panel is just inside the tunnel mouth; the far pylon stands beyond the opposite corner flag, at the end of a cable buried the whole length of the touchline — about a hundred metres of copper.

Nandini flicks the switch back on, just to check something. "There has to be a gap," she says. "The push starts here. It has to travel all that way before the far lamp knows."

Kabir watches the far pylon. Near lamp, far lamp — they come on together, as far as any eye can tell.

The next morning their teacher listens to the argument and says something that satisfies neither of them. Nandini is right that something has to make the journey. Kabir is right that the lights came on together. And the electrons in that cable, she adds, are creeping along it more slowly than a snail — so slowly that one of them would need the better part of two weeks to reach the far pylon.

Both things are true at once. So what is crawling, and what is arriving instantly?

## The physics

Inside a metal, the free electrons are already flying about at enormous random speeds, of order $10^5\,\text{m/s}$, colliding constantly with the vibrating metal ions. That motion is random — as much one way as the other — so it carries no net charge anywhere.

Close the switch and an electric field $\vec{E}$ appears along the whole length of the wire almost at once, at close to the speed of light. Between one collision and the next, each electron is nudged slightly along the field direction (backwards along it, since the electron is negative), and every collision wipes that gain out again. What survives is a tiny, steady *average* velocity laid on top of the random dance. That average is the **drift velocity** $v_d$.

![An electron's fast zigzag path between collisions inside a wire, with a small steady net drift opposite to the electric field](figures/drift_velocity/drift-velocity-zigzag.svg "The zigzag is fast and random; the slow, steady creep it adds up to is the drift velocity.")

**Mobility** $\mu$ measures how much drift a given field buys you:

$$\mu = \frac{v_d}{E}$$

in units of $\text{m}^2\,\text{V}^{-1}\text{s}^{-1}$.

Now tie the drift to the current. Let the wire have cross-sectional area $A$ and $n$ free electrons per unit volume, each of charge magnitude $e$. In a time $t$, every free electron within a distance $v_d t$ of a chosen cross-section gets across it. That slab has volume $A v_d t$, so it holds $nAv_dt$ electrons, carrying a charge

$$Q = neAv_d\,t$$

Divide by $t$ and use $I = Q/t$:

$$I = neAv_d$$

This holds for a metallic conductor of uniform cross-section carrying a steady current. And it settles the argument: what races down the touchline is the **field**, which starts every electron all along the cable moving at practically the same moment. The electrons themselves only creep.

## Worked example

**Given:** the buried cable has a cross-section $A = 2.0\,\text{mm}^2$ and carries $I = 3.2\,\text{A}$. Copper holds about $n = 1.0 \times 10^{29}$ free electrons per cubic metre (illustrative, but the right size). Take $e = 1.6 \times 10^{-19}\,\text{C}$.
**Find:** the drift velocity.

Convert the area first: $2.0\,\text{mm}^2 = 2.0 \times 10^{-6}\,\text{m}^2$.

Work out the bottom of the fraction on its own, because it has a meaning worth seeing:

$$neA = (1.0 \times 10^{29})(1.6 \times 10^{-19})(2.0 \times 10^{-6}) = 3.2 \times 10^{4}\,\text{C/m}$$

That is the free charge carried by every metre of this cable — thirty-two thousand coulombs of electrons, standing there ready.

$$v_d = \frac{I}{neA} = \frac{3.2}{3.2 \times 10^{4}} = 1.0 \times 10^{-4}\,\text{m/s}$$

A tenth of a millimetre per second: one millimetre every ten seconds. Over the hundred metres to the far pylon, that is $10^6\,\text{s}$ — about twelve days.

**Sanity check:** a wire already holds a colossal amount of mobile charge, so a few amperes need only a crawl — a tiny drift speed is exactly the right size of answer.

## Where the picture breaks

The word "velocity" oversells it: $v_d$ is an average over a wildly random motion, not the speed of any one electron, and no electron travels in a straight line for even a micrometre. Nothing here is a football analogy, and it shouldn't be — a pass is one object moving along a path you can watch, while a current is a whole population of carriers creeping together, the same number leaving one end as entering the other. Also, $n$ is not something you choose: for a given metal it is fixed by its atoms. And in a semiconductor both electrons and positive holes carry the current, so $I = neAv_d$ needs a second term there — that comes later.

## Key takeaway

An electric field inside a wire gives the randomly moving free electrons a tiny average velocity, the drift velocity $v_d$, with mobility $\mu = v_d/E$. Counting the charge that crosses a cross-section gives $I = neAv_d$, so for a fixed cable the drift is proportional to the current. The drift is slower than a snail; the lamp lights instantly because the field, not the electron, makes the journey.
