---
concept_id: magnetic_field_oersted
interest: football
format: explain
title: The keyring compass that lied behind the goal
check:
  question: |-
    A heavy lead lies flat on the grass running from south to north, carrying a steady current towards the **north**. A compass is placed on the grass resting directly on top of the lead. In which direction does the lead's own magnetic field point at the compass?
  options:
    A: |-
      Towards the west
    B: |-
      Towards the east
    C: |-
      Towards the north, the same way as the current
    D: |-
      Vertically upwards, straight away from the lead
  answer: B
  explanation: |-
    Grip the lead with the right hand, thumb pointing north along $I$. As the curled fingers pass over the top of the lead they are sweeping towards the east, so at a point above the lead $\vec{B}$ points east.
  misconceptions:
    A: |-
      Curls the fingers the wrong way — almost always by using the left hand. The grip rule is a right-hand rule, and the left hand reverses every answer.
    C: |-
      Thinks the magnetic field points along the current, like the current's own arrow. It never does: $\vec{B}$ is always at right angles to the wire, wrapping around it.
    D: |-
      Treats the magnetic field like the electric field of a charge, pointing straight out along the line from the wire to the point. Magnetic field lines around a wire are closed circles, not radial spokes.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A football ground with a coil traced around the goal frame, a pop-up sprinkler on a solenoid valve, an electric line-marking machine and a horn speaker on a pole with a compass lying on its supply cable](scenes/football/moving_charges_magnetism.svg "Every machine on this ground makes a magnetic field while it runs. Notice the compass sitting on the cable.")

Yuvraj keeps goal for his school team, and he has spent most of a long team talk doing nothing useful with the compass keyring clipped to his kitbag. He puts it down on the grass behind his goal to settle an argument: which end of the ground faces the afternoon sun?

The needle gives him an answer. He shuffles a metre sideways and asks again — and the needle has turned nearly a quarter of a circle. A metre back, and it behaves. He tries twice more, certain he is being clumsy with it.

Then the groundsman finishes the touchline, switches off the battery trolley feeding the line-marking machine and starts coiling in its thick lead. Yuvraj tries the bad spot once more. The needle points where it should.

There is no magnet anywhere on this ground. A lead is just a lead. So what was a switched-on machine doing to a compass from three metres away?

## The physics

In 1820 the Danish scientist **Hans Christian Oersted** saw exactly this in a lecture room: a compass needle beside a wire twitched the instant the circuit was closed, and settled back when it was opened. That twitch is the whole discovery.

> **A steady electric current produces a magnetic field in the space around it.**

Before Oersted, electricity and magnetism were two separate subjects. After him they were one.

![On the left, a compass under a wire pointing north with the switch open and swinging sideways when current flows. On the right, the right-hand grip rule: the thumb along the current, the fingers curling round it](figures/magnetic_field_oersted/oersted-compass-and-grip-rule.svg "Switch open, the needle points north. Switch closed, it swings across the wire — the field of a current is at right angles to it, not along it.")

The field of a long straight wire does not push outwards from the wire. Its field lines are **closed circles**, drawn in the plane at right angles to the wire and centred on it. Their direction comes from the **right-hand grip rule**:

> Hold the wire in your right hand with the thumb along the conventional current $I$. Your curled fingers then point the way $\vec{B}$ goes around the wire.

Two things worth fixing in your head:

- At every point, $\vec{B}$ is perpendicular both to the wire and to the line joining the wire to that point. It never points along the current, and never straight at the wire.
- The circles spread out as you move away, so the field weakens with distance. Ampère's law, later in this chapter, gives its exact size.

A compass needle is only a small bar magnet free to turn. It lines up with the **total** horizontal field where it sits — the Earth's field plus whatever the lead adds. That is why Yuvraj's needle misbehaved in one place and nowhere else.

![Portrait photograph of a man in a dark coat with a high collar](famous/hans-christian-oersted.jpg "Hans Christian Ørsted (1777–1851). In 1820 he noticed a compass needle twitch as he switched a current on — the first link found between electricity and magnetism. Public domain, via Wikimedia Commons.")

## Worked example

**Given:** the trolley's lead lies flat on the grass running east–west, with the conventional current flowing towards the **east**. Yuvraj's compass rests on top of the lead, a centimetre from the copper, where the lead's field is far stronger than the Earth's.
**Find:** which way the needle settles, and what happens when he slides it 30 cm to one side.

**Step 1 — the field on top of the lead.** Right hand, thumb pointing east along $I$. Where the fingers pass over the *top* of the lead they are sweeping towards the **south**. So the lead's field at the compass points south.

That is the opposite of the Earth's field, and much bigger than it, so the needle settles pointing **south** — backwards. A compass reading that is 180° wrong is not a broken compass; it is a compass obeying a bigger field.

**Step 2 — slide it 30 cm north.** Now the compass sits beside the lead rather than above it. The circles of field there pass *vertically* through that spot, and a needle pivoted to swing horizontally cannot follow a vertical field. So it swings back to north.

**Sanity check:** the effect switching on and off within a metre is exactly what Yuvraj saw — a field that wraps tightly around the lead and changes direction as you walk around it.

## Where the picture breaks

The compass never shows you the lead's field on its own. It shows the **sum** of that field and the Earth's, so how far it turns depends on which way the lead happens to be laid. Lay it east–west, as in the worked example, and the needle cannot settle at an angle at all: it either holds still or flips end for end.

This also only works because the trolley supplies a **steady, one-way current**. A mains cable carries a current that reverses fifty times a second, and the needle is far too heavy to follow it, so it hardly stirs. The same cable also runs its outward and return conductors side by side, with opposite currents whose fields largely cancel a short distance away.

## Key takeaway

A current makes a magnetic field — that is Oersted's discovery, and the start of this whole chapter. Around a long straight wire the field lines are closed circles at right angles to the wire, and the **right-hand grip rule** gives their direction: thumb along $I$, fingers curl the way $\vec{B}$ goes.
