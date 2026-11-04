---
concept_id: magnetic_field_oersted
interest: cricket
format: explain
title: The compass that refused to point north
check:
  question: |-
    A vertical cable at the edge of a ground carries a steady current straight upwards. A compass is placed on the ground due **north** of the cable. In which direction does the cable's magnetic field point at the compass?
  options:
    A: |-
      Towards the west
    B: |-
      Towards the east
    C: |-
      Vertically upwards, the same way as the current
    D: |-
      Towards the south, straight back at the cable
  answer: A
  explanation: |-
    Grip the cable with the right hand, thumb pointing up along the current. At a point north of the wire the curled fingers are sweeping towards the west, so $\vec{B}$ points west there.
  misconceptions:
    B: |-
      Curls the fingers the wrong way — usually by using the left hand. The grip rule is a right-hand rule; the left hand reverses every answer.
    C: |-
      Thinks the magnetic field points along the current. It doesn't: $\vec{B}$ is always at right angles to the wire, wrapping around it.
    D: |-
      Treats the magnetic field like the electric field of a charge, pointing along the line joining the wire to the point. Magnetic field lines around a wire are closed circles, not radial spokes.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A cricket ground with an electric roller, a compass lying on a thick power cable, a bowling machine and a loudspeaker on a pole](scenes/cricket/moving_charges_magnetism.svg "Every machine on this ground works because a current makes a magnetic field. Notice the compass sitting on the cable.")

Aarti has one job before the camp starts: mark the practice pitch so it runs north–south, the way the main square does. She borrows a compass from the school lab, kneels at the far end and lines up her string.

Then she walks twenty steps towards the pavilion, puts the compass down again to check — and the needle has swung a long way off. She moves it a metre sideways; it comes back. A metre back; it swings again.

Her friend Kabir laughs and points at the ground. Right where she keeps putting the compass, a thick black cable runs across the turf to the electric roller. The roller is switched on.

Nothing has moved. No magnet is anywhere near. So what is a cable, carrying nothing but current, doing to her compass?

## The physics

In 1820 the Danish scientist **Hans Christian Oersted** noticed exactly this in a lecture room: a compass needle near a wire twitched the moment the circuit was closed, and settled back when it was opened. That twitch is the whole discovery.

> **A steady electric current produces a magnetic field in the space around it.**

Before Oersted, electricity and magnetism were two separate subjects. After him they were one.

![On the left, a compass under a wire pointing north with the switch open and swinging sideways when current flows. On the right, the right-hand grip rule: the thumb along the current, the fingers curling round it](figures/magnetic_field_oersted/oersted-compass-and-grip-rule.svg "Switch open, the needle points north. Switch closed, it swings across the wire — the field of the current is at right angles to it.")

The field of a long straight wire is not a push outwards from the wire. The field lines are **closed circles**, drawn in the plane at right angles to the wire, centred on it. Their direction is given by the **right-hand grip rule**:

> Hold the wire in your right hand with the thumb pointing along the conventional current $I$. Your curled fingers then point the way $\vec{B}$ goes around the wire.

Two consequences worth fixing in your head:

- At any point, $\vec{B}$ is perpendicular both to the wire and to the line from the wire to that point. It never points along the current, and never straight at the wire.
- The circles get farther apart as you move away, so the field weakens with distance. Ampère's law, later in this chapter, gives the exact size.

A compass needle is just a small bar magnet free to turn. It lines up with the **total** field at its position — the Earth's field plus whatever the cable adds. That is why Aarti's needle behaves everywhere except on that one line across the outfield.

![Portrait photograph of a man in a dark coat with a high collar](famous/hans-christian-oersted.jpg "Hans Christian Ørsted (1777–1851). In 1820 he noticed a compass needle twitch when he switched a current on — the first link found between electricity and magnetism. Public domain, via Wikimedia Commons.")

## Worked example

**Given:** a cable lies along the ground running south to north, with the current flowing towards the north. A compass rests directly on top of it. At the compass, the cable's own field turns out to be exactly as strong as the Earth's horizontal field.
**Find:** which way the needle settles.

**Step 1 — the cable's field at that spot.** Right hand, thumb pointing north along $I$. The compass is *above* the wire, so look at where the fingers are sweeping as they pass over the top: towards the **east**.

**Step 2 — add the Earth's field.** The Earth's horizontal field points north. So the needle feels one pull north and an equal pull east, at right angles to each other.

Two equal pulls at right angles give a resultant exactly halfway between them, so the needle settles **45° east of north** — pointing north-east.

**Sanity check:** the cable can only ever turn the needle, never hold it still, and a field of equal strength should move it a good chunk of the way round — 45° is exactly the kind of "obviously wrong" reading Aarti was getting.

## Where the picture breaks

The compass is doing something a little different from what the diagram shows. It does not reveal the cable's field on its own; it reveals the **sum** of that field and the Earth's, so the deflection depends on how the cable is laid relative to north. Lay the same cable running east–west and the needle barely moves at all.

The roller's cable also carries two conductors, a live and a return, running side by side with opposite currents. Their fields largely cancel a short distance away — so the real cable is a much weaker source than a single wire, and Aarti had to put the compass almost on top of it.

## Key takeaway

A current makes a magnetic field: that is Oersted's discovery. Around a long straight wire the field lines are closed circles at right angles to the wire, and the **right-hand grip rule** gives their direction — thumb along $I$, fingers curl the way $\vec{B}$ goes. The field never points along the wire, and never straight at it.
