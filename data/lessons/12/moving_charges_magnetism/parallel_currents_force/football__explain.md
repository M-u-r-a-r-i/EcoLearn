---
concept_id: parallel_currents_force
interest: football
format: explain
title: What bent the copper bars in the switch room
check:
  question: |-
    Two long parallel bars carry equal currents in the same direction, and so attract each other. If **both** currents are doubled **and** the gap between the bars is also doubled, the force per unit length becomes
  options:
    A: |-
      unchanged.
    B: |-
      twice as big.
    C: |-
      four times as big.
    D: |-
      half as big.
  answer: B
  explanation: |-
    $\dfrac{F}{L} = \dfrac{\mu_0 I_1 I_2}{2\pi d}$. Doubling both currents multiplies the top by four; doubling $d$ divides by two. The result is twice the original force per metre.
  misconceptions:
    A: |-
      Treats the force as proportional to the current rather than to the *product* of the two currents, so the doubled gap appears to cancel the doubled current exactly.
    C: |-
      Gets the factor of four from the currents but forgets the separation in the denominator.
    D: |-
      Remembers the $1/d$ and applies it alone, ignoring what the currents did. The currents matter twice over, once for each bar.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A football ground with a coil traced around the goal frame, a pop-up sprinkler on a solenoid valve, an electric line-marking machine and a horn speaker on a pole with a compass lying on its supply cable](scenes/football/moving_charges_magnetism.svg "Every machine on this ground is fed from one switch room, through bars of solid copper.")

Rehan has three days of work experience at a stadium and has spent most of the first one carrying things. The best part comes at the end, when the duty electrician unlocks the switch room behind the north stand.

Inside, behind a mesh screen, are the busbars: flat bars of copper as thick as a finger, running in parallel pairs along the wall, bolted down every half metre.

One pair is not straight. Between two bolts the two bars bow towards each other, almost touching in the middle, the way a ruler bends when you press its ends. The electrician says it happened during a fault the previous winter — a short circuit that lasted a fraction of a second.

Nothing touched them. No one was in the room. In that fraction of a second, something bent solid copper sideways. What pulls two bars of metal together when all they are doing is carrying current?

## The physics

Each bar is doing both halves of this chapter at once: **making** a magnetic field, and **sitting in** the other bar's field.

Take two long straight parallel conductors a distance $d$ apart, carrying $I_1$ and $I_2$. The first makes a field at the second, by Ampère's law:

$$B_1 = \frac{\mu_0 I_1}{2\pi d}$$

The second conductor sits in that field, at right angles to it, so a length $L$ of it feels $F = B_1 I_2 L$. Put the two together and divide by $L$:

$$\frac{F}{L} = \frac{\mu_0 I_1 I_2}{2\pi d}$$

![Two parallel wires with currents in the same direction pulled towards each other, and the same two wires with opposite currents pushed apart](figures/parallel_currents_force/parallel-wires-attract-repel.svg "Same direction: attraction. Opposite directions: repulsion — the opposite of what you would guess from magnetic poles.")

Now the direction, and it catches almost everybody out:

> **Currents in the same direction attract. Currents in opposite directions repel.**

Work it through with the right hand once and it stops being surprising. Above bar 2, bar 1's field points one way; apply $\vec{F} = I\vec{L} \times \vec{B}$ to bar 2 and the force comes out pointing back towards bar 1. Reverse either current and the force reverses with it. Note also that the force on each bar is the same size and opposite in direction, as Newton's third law requires.

This equation is why the ampere was, for a long time, *defined* by it: one ampere is the steady current which, in two infinitely long thin parallel conductors one metre apart in vacuum, produces a force of $2 \times 10^{-7}\,\text{N}$ on each metre of length. Put $I_1 = I_2 = 1\,\text{A}$ and $d = 1\,\text{m}$ into the formula and that is exactly what comes out.

![Engraved portrait of a man in early nineteenth-century dress](famous/andre-marie-ampere-1825.jpg "André-Marie Ampère (1775–1836), engraved in 1825. Weeks after hearing of Ørsted's discovery he had measured the force between two currents — the effect the unit of current was later named for. Public domain, via Wikimedia Commons.")

## Worked example

**Given:** two busbars $d = 5.0\,\text{cm}$ apart, carrying equal currents in the same direction. Take $\dfrac{\mu_0}{2\pi} = 2 \times 10^{-7}\,\text{T}\,\text{m}\,\text{A}^{-1}$.
**Find:** the force on each metre at the normal running current of $200\,\text{A}$, and during a fault of $5000\,\text{A}$.

**Step 1 — running normally.**

$$\frac{F}{L} = \frac{(2 \times 10^{-7})(200)(200)}{0.050} = 0.16\,\text{N per metre}$$

That is the weight of a small handful of sugar, spread along every metre of bar. The bolts never notice it.

**Step 2 — during the fault.** The current is 25 times bigger, and the force depends on the **product** of the two currents, so it grows by $25 \times 25 = 625$:

$$\frac{F}{L} = 625 \times 0.16 = 100\,\text{N per metre}$$

A hundred newtons on every metre is like hanging a $10\,\text{kg}$ bag from the middle of each span — and it arrives in an instant. Copper bends.

**Sanity check:** the same equation gives a force too small to feel and a force that bends metal, purely because the current went up 25 times. That squaring is the whole story of a short circuit.

## Where the picture breaks

The busbars are not infinitely long, thin or straight, and they are bolted down, so the real force varies along them and is concentrated between the supports. The formula gives the size of the effect, not a stress analysis.

The fault current is also alternating. Both bars reverse together, so the *product* $I_1 I_2$ stays positive and the force stays an attraction — but it pulses at twice the mains frequency rather than pushing steadily.

One historical footnote: since 2019 the ampere is no longer defined by this force. It is defined by fixing the value of the elementary charge, and the constant $\mu_0$ is now something measured rather than exact. The force law is unchanged; only the status of the definition has moved.

## Key takeaway

Two parallel currents exert a force per unit length $\dfrac{F}{L} = \dfrac{\mu_0 I_1 I_2}{2\pi d}$ on each other — attracting when the currents run the same way, repelling when they run opposite ways. Because it depends on the product of the currents, a fault current a few tens of times too big produces a force hundreds of times too big.
