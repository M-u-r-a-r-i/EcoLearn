---
concept_id: lenzs_law
interest: smartphones
format: explain
title: Why the hand-crank charger gets stiff when you plug in a phone
check:
  question: |-
    The N pole of a small magnet is pushed straight towards a flat, closed coil lying on a phone's circuit board. Looking at the coil **from the magnet's side**, which way does the induced current flow, and why?
  options:
    A: |-
      Clockwise, so the near face of the coil becomes an S pole that pulls the magnet in.
    B: |-
      There is no current, because the magnet never touches the coil.
    C: |-
      Clockwise, so the near face of the coil becomes an N pole that pushes the magnet back.
    D: |-
      Anticlockwise, so the near face of the coil becomes an N pole that pushes the magnet back.
  answer: D
  explanation: |-
    The flux through the coil is rising, so the induced current must oppose the approach by making the near face an N pole. A current that looks anticlockwise from one side makes that side an N pole, so the current is anticlockwise as seen from the magnet.
  misconceptions:
    A: |-
      Thinks the induced current helps the change along; if it pulled the magnet in, the coil would make energy from nothing, which Lenz's law forbids.
    B: |-
      Thinks induction needs contact; a changing flux through the coil is enough, whether or not the magnet touches it.
    C: |-
      Has the right idea (the coil repels) but the wrong rule for the pole: a clockwise current seen from a side makes that side an S pole, not an N pole.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A desk at night with a phone on a wireless charging pad, a shake torch, a hand-crank charger, wired earbuds and a coin beside the pad](scenes/smartphones/electromagnetic_induction.svg "Every gadget on this desk works because a magnetic field is changing. This lesson is about the hand-crank charger: a coil turning between magnets.")

On the second night of the school trek, the camp has no electricity and Zoya's phone is at two per cent. Her teacher lends her a hand-crank emergency charger — a small box with a folding handle and a USB socket.

With nothing plugged in, Zoya flicks the handle and it spins round and round on its own, light as a toy.

Then she plugs in her phone. The next turn of the handle is suddenly heavy. She has to lean into it, and the moment she lets go, the handle stops dead.

"You've jammed it," says her friend Manav. Zoya unplugs the phone to check — and the handle spins freely again. Plug in: stiff. Unplug: free.

Nothing inside the box has touched anything new. How can a handle *feel* whether a phone is connected at the end of a cable?

## The physics

Inside the box, turning the handle spins a coil past magnets, so the flux through the coil keeps changing and an emf is induced. Faraday's law tells you the size of that emf. **Lenz's law** tells you its direction:

> The induced current flows in the direction that **opposes the change in flux** that produced it.

That is the meaning of the minus sign in $\varepsilon = -N\,\dfrac{d\Phi_B}{dt}$.

To use it, follow three steps:

1. Is the flux through the loop **rising or falling**, and in which direction does the field point?
2. The induced current makes its own field that **fights that change**: opposite to the field if the flux is rising, along it if the flux is falling. Equivalently, the coil's near face repels an approaching magnet and attracts a retreating one.
3. Turn that into a current direction. Seen from one side of a loop, an **anticlockwise** current makes that face an **N pole**; a **clockwise** current makes it an **S pole**.

![Two panels: a magnet's N pole approaching a coil, which forms an N face and pushes it back; the magnet moving away, and the coil forming an S face that holds it back](figures/lenzs_law/magnet-approaching-coil.svg "Whether the magnet comes or goes, the coil resists its motion. That resistance is why you must do work, and the work is where the electrical energy comes from.")

Why must it be this way? **Conservation of energy.** Suppose the induced current *helped* the change — attracting an approaching magnet. The magnet would speed up, the flux would change faster, the current would grow, and you would get ever more electrical energy and kinetic energy out of nothing. That cannot happen. So the induced current always opposes, and you must do work against it; that work is exactly where the electrical energy comes from.

Now Zoya's handle. With nothing plugged in the circuit is **open**: an emf appears, but no current flows, so there is nothing to push back. Plug in the phone and a current flows. That current, sitting in the magnets' field, feels a force that opposes the rotation. Her arm's work turns into the energy flowing into the battery.

## Worked example

**Given:** a magnet with its **S pole** facing a closed coil is pulled **away** from it.
**Find:** the direction of the induced current seen from the magnet's side.

**Step 1 — what changes?** Field lines point **into** an S pole, so at the coil they point towards the magnet. As the magnet leaves, this flux **falls**.

**Step 2 — what does the coil do?** It opposes the fall by trying to hold the magnet back — so its near face must attract an S pole. The near face becomes an **N pole**.

**Step 3 — which way round?** An N face means the current looks **anticlockwise** from the magnet's side.

**Now the energy.** Say the phone draws $2\,\text{W}$ from the charger and Zoya cranks for $60\,\text{s}$. Her arm must supply at least

$$W = Pt = 2 \times 60 = 120\,\text{J}$$

That is about the work of lifting a one-litre water bottle up a four-storey building — for one minute of charging.

**Sanity check:** the more power the phone draws, the more current flows and the harder the handle pushes back — exactly the stiffness Zoya felt.

## Where the picture breaks

The "it fights back" picture is about the **change**, not the magnet. The coil does not repel magnets in general: an approaching magnet is pushed away, a retreating one is held back, and a magnet at rest is left alone.

The energy step is also a lower limit. A real crank charger loses some of your work as heat in the wire, in friction in the gears and in the charging circuit, so your arm does rather more than $120\,\text{J}$.

And the charger's electrical load is not the only thing you feel. Even unplugged, you are turning gears and bearings. But that friction is small and doesn't depend on the phone — the sudden stiffness when you plug in is the Lenz's-law part.

## Key takeaway

The induced current always flows so as to **oppose the change in flux** that caused it — that is Lenz's law and the minus sign in Faraday's law. It is conservation of energy in disguise: you must do work against the opposition, and that work becomes the electrical energy. No current, no opposition — which is why the crank only gets stiff when a phone is drawing current.
