---
concept_id: parallel_currents_force
interest: smartphones
format: explain
title: Do the two wires in a charging cable pull or push
check:
  question: |-
    Inside a charging cable, two long parallel wires carry equal steady currents in **opposite** directions — one to the phone, one back. The cable as a whole carries no net charge. What magnetic force do the two wires exert on each other?
  options:
    A: |-
      They push each other apart.
    B: |-
      They pull each other together.
    C: |-
      No force, because each wire is electrically neutral.
    D: |-
      A force only while the current is switching on or off, none while it is steady.
  answer: A
  explanation: |-
    Each wire sits in the magnetic field of the other and feels $\vec{F} = I\vec{L}\times\vec{B}$. For currents in opposite directions, that force points away from the other wire, so they repel, with $F/L = \dfrac{\mu_0 I_1 I_2}{2\pi d}$.
  misconceptions:
    B: |-
      Carries over "opposites attract" from electric charges. For parallel currents the rule is the other way round: currents in the **same** direction attract, currents in **opposite** directions repel.
    C: |-
      Thinks only net charge can produce a force between wires. The magnetic force comes from the *moving* charges — the current — even when each wire is neutral overall.
    D: |-
      Confuses this with electromagnetic induction, which does need a change. A steady current makes a steady field, and the other wire's steady current feels a steady force in it.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A desk with a phone lying on a charging cable showing a swung compass arrow, a wireless charging pad with its coil exposed, a flip-cover case with a small magnet in its flap, and a speaker and a small cylinder-shaped vibration motor taken apart](scenes/smartphones/moving_charges_magnetism.svg "Look at the charging cable under the phone. Inside it are two wires side by side, one carrying current to the phone and one carrying it back.")

Pooja helps out at her uncle Salim's phone repair stall on Saturdays. A customer brings in a fast-charging cable with a split in its sleeve, and through the gap Pooja can see two thin copper wires running side by side, a couple of millimetres apart.

"When it's charging, both of these carry current," she says. "So both make a magnetic field. So they must be pulling on each other."

"Pushing," says Salim, without looking up.

"Pulling. One goes to the phone and one comes back. Opposite directions. Opposites attract."

Salim bets her a cup of chai that she's wrong. Pooja plugs the cable in and watches the wires through the split. Nothing moves at all — no squeeze, no bulge.

So is there a force between them? If there is, which way does it point, and how big is it that nobody can see it?

## The physics

Put two long, straight, parallel wires a distance $d$ apart, carrying currents $I_1$ and $I_2$. Each wire sits in the magnetic field of the other.

**Step 1 — the field of wire 1 at wire 2.** From Ampere's law, $B_1 = \dfrac{\mu_0 I_1}{2\pi d}$, and it points at right angles to wire 2.

**Step 2 — the force on wire 2.** A length $L$ of wire 2 carrying $I_2$ in field $B_1$ feels $F = B_1 I_2 L$, so the **force per unit length** is

$$\frac{F}{L} = \frac{\mu_0 I_1 I_2}{2\pi d}$$

By Newton's third law, wire 1 feels an equal and opposite force.

**Direction.** Use the grip rule for $B_1$ and the right-hand rule for $I\vec{L}\times\vec{B}$, and you find:

> **Currents in the same direction attract. Currents in opposite directions repel.**

This is the opposite of the rule for electric charges, which is exactly why it catches people out.

![On the left, two parallel wires carrying current the same way are pulled towards each other; on the right, currents in opposite directions push the wires apart](figures/parallel_currents_force/parallel-wires-attract-repel.svg "Same direction: attract. Opposite directions: repel. It is the reverse of the rule for charges.")

**The ampere.** This force was used to define the unit of current. Two long parallel wires $1\,\text{m}$ apart in vacuum, each carrying $1\,\text{A}$, push or pull on each other with

$$\frac{F}{L} = \frac{(4\pi\times10^{-7})(1)(1)}{2\pi(1)} = 2\times10^{-7}\,\text{N/m}$$

NCERT's definition says exactly this: one ampere is the steady current which, in two such wires, produces a force of $2\times10^{-7}\,\text{N}$ per metre of length. (Since 2019 the SI defines the ampere by fixing the charge of the electron instead, but the force between the wires is still exactly what this formula predicts.)

## Worked example

**Given:** the two wires in Pooja's cable are $d = 2.0\,\text{mm} = 2.0\times10^{-3}\,\text{m}$ apart, each carrying $I = 3.0\,\text{A}$, in opposite directions (illustrative values).
**Find:** the force per metre, which way it points, and whether Pooja could see it.

**Step 1 — the size.**

$$\frac{F}{L} = \frac{\mu_0 I^{2}}{2\pi d} = \frac{(4\pi\times10^{-7})(3.0)(3.0)}{2\pi(2.0\times10^{-3})} = 9.0\times10^{-4}\,\text{N/m}$$

**Step 2 — the direction.** The currents are opposite, so the wires **repel**. Salim wins the chai.

**Step 3 — can anyone see it?** A metre of cable feels about $9\times10^{-4}\,\text{N}$ in total — the weight of less than a tenth of a gram, a few grains of rice spread along a whole metre. The plastic insulation holding the wires in place easily resists that.

**Sanity check:** the force grows with the product of the currents, so a far bigger current — a short circuit in a power station, say — can make heavy conductors jump. At phone-charging currents it is real but invisible.

## Where the picture breaks

The formula is for **long, straight, thin** wires. Real cable wires are thick bundles of strands, and only $2\,\text{mm}$ apart, so treating each as a thin line is an approximation — a reasonable one here.

The wires are not free to move, either. The formula gives the force on each wire, but the insulation and the sleeve hold them in place and take up the push, so "no visible movement" never meant "no force".

And the "opposites attract" instinct is not silly — it is right for charges. It just belongs to electric forces, not to the magnetic forces between currents.

## Key takeaway

Two long parallel wires carrying currents $I_1$ and $I_2$ a distance $d$ apart exert a force per unit length $\dfrac{F}{L} = \dfrac{\mu_0 I_1 I_2}{2\pi d}$ on each other. Currents in the **same** direction **attract**; currents in **opposite** directions **repel**. This force gave the classic definition of the ampere: $2\times10^{-7}\,\text{N/m}$ for $1\,\text{A}$ in each wire, $1\,\text{m}$ apart.
