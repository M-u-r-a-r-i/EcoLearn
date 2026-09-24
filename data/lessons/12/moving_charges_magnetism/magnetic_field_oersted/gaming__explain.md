---
concept_id: magnetic_field_oersted
interest: gaming
format: explain
title: The arcade cabinet that moved a compass
check:
  question: |-
    Inside a cabinet a wire runs horizontally along the bench from south to north, and a steady current flows through it towards the **north**. A phone lies flat directly **underneath** the wire, with its compass app open. In which direction does the wire's own magnetic field point at the phone?
  options:
    A: |-
      Towards the east
    B: |-
      Towards the west
    C: |-
      Towards the north, the same way as the current
    D: |-
      Straight up, from the phone towards the wire
  answer: B
  explanation: |-
    Grip the wire with the right hand, thumb pointing north along $I$. The fingers sweep round the wire; underneath it they are heading west, so $\vec{B}$ points west at the phone. (Directly above the wire it would point east.)
  misconceptions:
    A: |-
      Right rule, wrong side. East is the answer for a point *above* the wire; below it the circle carries the field the opposite way. Using the left hand gives the same mistake.
    C: |-
      Thinks the magnetic field points along the current. It never does — $\vec{B}$ is always at right angles to the wire, wrapping around it in closed circles.
    D: |-
      Treats the magnetic field like the electric field of a charge, pointing along the line joining the wire to the point. Magnetic field lines around a wire are closed circles, not radial spokes.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A gaming workbench with a bartop arcade cabinet, a cutaway of a pinball flipper coil, a controller with its shell off, a PC case fan, and a phone lying on a power cable showing a swung compass needle](scenes/gaming/moving_charges_magnetism.svg "Everything on this bench runs on current — and every one of those currents is making a magnetic field. Start with the phone on the cable.")

The college game-dev club has a bartop arcade cabinet in pieces on a bench, and Nikhil has the back panel off. There is no mains anywhere near the screen: a supply in the base turns everything into 12 volts of direct current, and two heavy wires carry it up to the monitor board — one up the left side of the cabinet, the return coming back down the right.

He sets his phone on the shelf inside while he hunts for a screwdriver. The compass app is still open from earlier. Someone flips the switch to test the marquee light, and the arrow jumps to a new heading and holds it — tilted well off, but rock steady. Switch off, and it swings back.

He tries it three more times. Same jump, same wrong heading, every time. Nothing has moved, and there is not a magnet in the whole cabinet.

So what is a wire full of current doing to his compass?

## The physics

In 1820 the Danish scientist **Hans Christian Oersted** noticed exactly this in a lecture room: a compass needle beside a wire twitched the moment the circuit was closed, and settled back when it was opened. That twitch is the whole discovery.

> **A steady electric current produces a magnetic field in the space around it.**

Before Oersted, electricity and magnetism were two separate subjects. After him they were one.

![On the left, a compass under a wire pointing north with the switch open and swinging sideways when current flows. On the right, the right-hand grip rule: the thumb along the current, the fingers curling round it](figures/magnetic_field_oersted/oersted-compass-and-grip-rule.svg "Switch open, the needle points north. Switch closed, it swings across the wire — the field of the current is at right angles to it.")

The field of a long straight wire is not a push outwards from the wire. The field lines are **closed circles**, drawn in the plane at right angles to the wire and centred on it. Their direction comes from the **right-hand grip rule**:

> Hold the wire in your right hand with the thumb pointing along the conventional current $I$. Your curled fingers then point the way $\vec{B}$ goes around the wire.

Two things worth fixing in your head:

- At any point, $\vec{B}$ is perpendicular both to the wire and to the line from the wire to that point. It never points along the current, and never straight at the wire.
- Because the field wraps round, two points on opposite sides of the same wire get fields pointing **opposite** ways. Move the phone from above the wire to below it and the needle swings the other way.

A compass — needle or phone chip — lines up with the **total** field where it sits: the Earth's field plus whatever the wiring adds. That is why Nikhil's arrow only misbehaves on one shelf, and only while the cabinet is on.

![Portrait photograph of a man in a dark coat with a high collar](famous/hans-christian-oersted.jpg "Hans Christian Ørsted (1777–1851). In 1820 he saw a compass needle twitch when he switched a current on — the first link found between electricity and magnetism. Public domain, via Wikimedia Commons.")

## Worked example

**Given:** the two heavy supply wires run vertically inside the cabinet, about $20\,\text{cm}$ apart — the left one carrying the current **upwards**, the right one carrying the same current back **downwards**. The phone lies on the shelf midway between them. Stand facing the open back of the cabinet, so "right" is your right and "away" means into the cabinet.
**Find:** which way the wiring's field points at the phone, and whether it is stronger or weaker than one wire alone would give.

**Step 1 — the left wire.** Thumb up along its current. The phone is to the *right* of this wire, and there the curled fingers are sweeping **away from you**, into the cabinet.

**Step 2 — the right wire.** Thumb now points *down*. The phone is to the *left* of this wire — and turning the thumb round and changing sides reverses the answer twice, so the fingers there are sweeping **away from you** as well.

Both wires push the field the same way, so at the midpoint they **add**: about twice what one wire on its own would give.

**Sanity check:** the go and return currents are opposite, yet between them their circles happen to sweep the same way — which is exactly why the strongest swing was on the shelf right in the middle, and not somewhere else.

## Where the picture breaks

A phone's "compass" is not a pivoted needle. It is a magnetometer chip, and the app draws an arrow from its reading — often after trying to correct for stray magnetism. That is why the arrow jumps to a new heading and sits there, rather than swinging and wobbling the way a real needle does.

The reading is also a **sum**, never the cable's field on its own. Turn the whole cabinet through a right angle and the same current gives a different deflection, because the cable's field is now added to the Earth's at a different angle.

And this trick needs **direct** current. The lead from the wall is alternating: it reverses fifty times a second, and neither a needle nor your eye can follow that, so the average effect on a compass is nothing. Inside the cabinet, past the power supply, the current is steady — which is why the arrow holds still at the wrong heading.

## Key takeaway

A current makes a magnetic field: that is Oersted's discovery. Around a long straight wire the field lines are closed circles at right angles to the wire, and the **right-hand grip rule** gives their direction — thumb along $I$, fingers curl the way $\vec{B}$ goes. The field never points along the wire, and never straight at it, and it reverses as you cross from one side of the wire to the other.
