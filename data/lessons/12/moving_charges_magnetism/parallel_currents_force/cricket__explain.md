---
concept_id: parallel_currents_force
interest: cricket
format: explain
title: Why the busbars are bolted down
check:
  question: |-
    Two long parallel wires carry currents in **opposite** directions. Each current is then doubled and the separation between the wires is also doubled. The force per unit length between them becomes
  options:
    A: |-
      twice as large, and attractive.
    B: |-
      twice as large, and repulsive.
    C: |-
      unchanged, and repulsive.
    D: |-
      four times as large, and repulsive.
  answer: B
  explanation: |-
    $F/L = \mu_0 I_1 I_2/(2\pi d)$. The product $I_1I_2$ becomes four times larger and $d$ doubles, so the force per unit length doubles. Antiparallel currents repel, whatever their size.
  misconceptions:
    A: |-
      Gets the size right but reverses the direction — usually by borrowing "opposites attract" from magnetic poles or charges. For currents it is the other way round: **parallel currents attract, antiparallel currents repel.**
    C: |-
      Cancels one doubling of current against the doubling of distance, as if the current appeared only once. Both currents appear, so the numerator grows four times while the denominator only doubles.
    D: |-
      Doubles each current correctly but forgets that the wires also moved further apart, which divides the result by two.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A cricket ground with an electric roller, a compass lying on a thick power cable, a bowling machine and a loudspeaker on a pole](scenes/cricket/moving_charges_magnetism.svg "Everything on this ground draws its power through a cabinet of heavy copper bars.")

The new floodlights need a new supply cabinet, and Meher, doing a summer apprenticeship with the contractor, is handed the boring job: bolting the copper busbars to their insulators. Three flat bars, running side by side down the panel, a hand's width apart. A clamp every twenty centimetres or so, and every single bolt has to be torqued.

She points out that the bars are rigid copper, screwed at both ends, in a cabinet nobody will ever touch. Nothing is going to move them.

The foreman doesn't argue. He just says that he has seen a panel after a short circuit, and the bars had bent away from each other like a bow. The clamps had held; the bar between two clamps had not.

Meher looks again at three motionless bars in a sealed steel box. What, in a cabinet with no moving parts at all, could bend solid copper sideways?

## The physics

Each bar carries a current, so each one sits in the *other's* magnetic field — and a current in a magnetic field feels a force. Put the two results of this chapter together and the whole answer falls out.

Take two long parallel wires a distance $d$ apart, carrying $I_1$ and $I_2$. At the second wire, the field of the first is

$$B_1 = \frac{\mu_0 I_1}{2\pi d}$$

and it points perpendicular to the second wire. So a length $L$ of the second wire feels

$$F = B_1 I_2 L = \frac{\mu_0 I_1 I_2 L}{2\pi d} \qquad\Longrightarrow\qquad \frac{F}{L} = \frac{\mu_0 I_1 I_2}{2\pi d}$$

![Two parallel wires with currents in the same direction pulled towards each other, and the same two wires with opposite currents pushed apart](figures/parallel_currents_force/parallel-wires-attract-repel.svg "Same direction: attraction. Opposite directions: repulsion. The opposite of what you would guess from magnetic poles.")

Work the directions through with the grip rule and then $I\vec{L} \times \vec{B}$, and you get a result that catches most people out:

> **Currents in the same direction attract. Currents in opposite directions repel.**

The forces on the two wires are equal and opposite, as Newton's third law demands. Note also that the force depends on the **product** $I_1I_2$ — so if both currents reverse together, as they do on alternating supply, the product stays positive and the force does not change direction. It is a steady push, not a vibration at the supply frequency.

This force used to define the **ampere**: one ampere was the steady current which, in two infinitely long parallel wires one metre apart in vacuum, gives a force of exactly $2 \times 10^{-7}\,\text{N}$ per metre of length. (Since 2019 the SI defines the ampere by fixing the value of the elementary charge instead, and this statement is a consequence rather than the definition — but it is still the clearest picture of what one ampere means.)

All of this assumes long, straight, parallel conductors with steady currents, thin compared with their separation.

## Worked example

**Given:** two of Meher's busbars run parallel, $10\,\text{cm}$ apart, each carrying $100\,\text{A}$ in the same direction.
**Find:** the force per metre between them — in normal use, and in a fault that briefly drives a hundred times the current.

**Step 1 — normal running.**

$$\frac{F}{L} = \frac{\mu_0 I_1 I_2}{2\pi d} = \frac{(2 \times 10^{-7})(100)(100)}{0.10} = 0.02\,\text{N/m}$$

That is the weight of about two grams on every metre of bar: completely negligible, and attractive.

**Step 2 — the fault.** The force depends on the product of the currents, so multiplying **both** by $100$ multiplies the force by $100 \times 100 = 10\,000$:

$$\frac{F}{L} \approx 200\,\text{N/m}$$

Now every metre of bar is being pulled sideways with the weight of a $20\,\text{kg}$ sack of cement — for the fraction of a second before the breaker trips. That is what bends copper, and that is what the clamps are for.

**Sanity check:** the current went up a hundredfold and the force ten-thousandfold, which is the signature of a square law — exactly what $I_1I_2$ predicts.

## Where the picture breaks

The formula is for infinitely long, thin, straight wires. Real busbars are flat, finite, and clamped at intervals, so the force is not evenly shared and the bending happens between supports — which is precisely the failure the foreman described.

The bars in a cabinet also carry currents in different directions at different moments across the three phases, so some pairs attract while others repel. The design has to survive the worst case, not the average.

And do not carry "opposites attract" over from magnets or charges. Here it is reversed, and the reversal is not a special rule to memorise: it drops out of the grip rule and $\vec{F} = I\vec{L}\times\vec{B}$ every time you work it through.

## Key takeaway

Two parallel currents exert equal and opposite forces on each other, with $\dfrac{F}{L} = \dfrac{\mu_0 I_1 I_2}{2\pi d}$ — **attracting** when the currents run the same way and **repelling** when they run opposite ways. At one ampere in wires one metre apart, that force is $2 \times 10^{-7}\,\text{N}$ per metre, the value that long defined the ampere.
