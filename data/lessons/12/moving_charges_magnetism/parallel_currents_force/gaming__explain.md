---
concept_id: parallel_currents_force
interest: gaming
format: explain
title: The arcade box with two strips of foil in it
check:
  question: |-
    Two long parallel wires each carry a current $I$ in the same direction and attract each other with a force $F$ per unit length. The current in **one** of the wires is now doubled, and at the same time the separation between them is doubled. What is the new force per unit length?
  options:
    A: |-
      $2F$
    B: |-
      $4F$
    C: |-
      $F$ — unchanged
    D: |-
      $F/2$
  answer: C
  explanation: |-
    $\dfrac{F}{L} = \dfrac{\mu_0 I_1 I_2}{2\pi d}$. Doubling one current doubles the force; doubling the separation halves it. The two changes cancel exactly, and the wires still attract.
  misconceptions:
    A: |-
      Counts the doubled current and forgets the doubled gap. The separation is in the denominator and undoes it.
    B: |-
      Applies $F \propto I^{2}$ as a reflex. The force depends on the *product* $I_1 I_2$, and here only one of the two currents changed — so it gains a single factor of two, not four.
    D: |-
      Counts the doubled separation and forgets the doubled current. Both factors have to be tracked.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A gaming workbench with a bartop arcade cabinet, a cutaway of a pinball flipper coil, a controller with its shell off, a PC case fan, and a phone on a power cable showing a swung compass needle](scenes/gaming/moving_charges_magnetism.svg "Every current on this bench sits near another current — and currents that run near each other push and pull on one another.")

Devansh has built the least computerised thing at the college game fest. A wooden box with a big red button on top. Behind a glass front, two strips of kitchen foil hang side by side, about a centimetre apart. In the base, borrowed from the physics lab, is a current-limited bench supply set to twenty amperes.

Press the button and the strips fly apart with a slap. There is a second switch that reverses which way the current runs down the right-hand strip, and with that thrown, the same press makes them snap *together* instead. Two outcomes, one button; players queue up to guess which they will get.

A physics teacher watches four rounds and asks Devansh what the strips are pushing against. Each other, he says.

She asks the obvious next question. Neither strip is a magnet. Neither is charged up. They never touch. So what is reaching across that centimetre of air?

## The physics

Two results from earlier in this chapter, bolted together.

**First**, a current makes a field. The left strip, carrying $I_1$, makes a field at the right strip's position, a distance $d$ away:

$$B_1 = \frac{\mu_0 I_1}{2\pi d}$$

and by the grip rule that field is perpendicular to the plane the two strips lie in — so it is at right angles to the right-hand strip.

**Second**, a current in a field feels a force. The right strip, carrying $I_2$ over a length $L$ at right angles to $B_1$, feels $F = B_1 I_2 L$. Put the two together and divide by the length:

$$\frac{F}{L} = \frac{\mu_0 I_1 I_2}{2\pi d}$$

![On the left, two parallel wires carrying current the same way are pulled towards each other; on the right, currents in opposite directions push the wires apart](figures/parallel_currents_force/parallel-wires-attract-repel.svg "Same direction: attraction. Opposite directions: repulsion. This is the reverse of what two charges do.")

Work the directions through with the grip rule and the right-hand rule and you get a result worth remembering, because it is the opposite of the electrostatic one you already know:

> **Currents in the same direction attract. Currents in opposite directions repel.**

Like charges repel; like currents attract. The two strips in Devansh's box fly apart on the default setting because the current runs *down* one and *back up* the other — which is exactly what a circuit has to do.

The force is mutual and equal, as Newton's third law demands: whatever the left strip does to the right, the right does back.

This is also the relation that fixed the size of the ampere for most of a century. Set $I_1 = I_2 = 1\,\text{A}$ and $d = 1\,\text{m}$ and the formula gives $2\times10^{-7}\,\text{N}$ on each metre of wire — and that number, in the definition NCERT states, is what *made* a current of one ampere one ampere.

The expression assumes long, thin, straight, parallel conductors carrying steady currents.

## Worked example

**Given:** two foil strips $1.0\,\text{cm} = 0.010\,\text{m}$ apart, each carrying $20\,\text{A}$ in the **same** direction.
**Find:** the force on each metre of strip, and which way it acts.

**Step 1 — the size.**

$$\frac{F}{L} = \frac{\mu_0 I_1 I_2}{2\pi d} = \frac{(2\times10^{-7})(20)(20)}{0.010} = \frac{8\times10^{-5}}{0.010} = 8\times10^{-3}\,\text{N/m}$$

**Step 2 — picture it.** Eight millinewtons per metre is about the weight of one gram of material per metre of strip — and a metre of kitchen foil cut a centimetre wide weighs roughly that much. The push is comparable to the strips' own weight, which is precisely why they visibly jump.

**Step 3 — which way.** Same direction, so they **attract**: this is the setting where they snap together. Flip the switch and one current reverses, so the force reverses and they fly apart.

**Sanity check:** twenty amperes is a serious current and it still only produces a gram's worth of push across a centimetre. Magnetic forces between ordinary wires are genuinely feeble — you need either huge currents or something very light to see anything at all.

## Where the picture breaks

Kitchen foil is not a long straight rigid wire. The strips bend, so the gap $d$ changes the instant they start to move, and the force changes with it — which is why the box gives a snap rather than a steady squeeze. Strips a few tens of centimetres long, a centimetre apart, are a fair approximation to "long", but their ends are close enough to the middle to matter.

The reversal of intuition is worth dwelling on. Everything you learned about like charges repelling has to be set aside here: like *currents* attract. Two charges push apart; two wires carrying the same way pull together. Nothing has gone wrong — a current is not a charge sitting still, and the force is magnetic, not electrostatic.

One honest footnote on the ampere. Since 2019 the SI defines the ampere by fixing the value of the elementary charge, not by this force between wires. The two-wire statement is now a consequence rather than the definition — but it is the definition your syllabus states, and it is still the best picture of what an ampere physically *is*.

## Key takeaway

Two parallel currents interact because each sits in the other's magnetic field: $\dfrac{F}{L} = \dfrac{\mu_0 I_1 I_2}{2\pi d}$, equal and opposite on the two wires. Currents in the **same** direction attract; currents in **opposite** directions repel. One ampere in each of two wires a metre apart gives $2\times10^{-7}\,\text{N}$ per metre — the force that classically defined the unit.
