---
concept_id: magnetic_field_oersted
interest: smartphones
format: explain
title: The compass app that flinched at a wire
check:
  question: |-
    A long straight wire is taped along the underside of a shelf, running from west to east, and a steady current flows through it towards the **east**. A phone lies flat on the desk directly **below** the wire, with its compass app open. In which direction does the wire's own magnetic field point at the phone?
  options:
    A: |-
      Towards the south
    B: |-
      Towards the north
    C: |-
      Towards the east, the same way as the current
    D: |-
      Straight up, from the phone towards the wire
  answer: B
  explanation: |-
    Grip the wire with the right hand, thumb pointing east along $I$. The fingers curl round the wire; underneath it they are heading north, so $\vec{B}$ points north at the phone. (Directly above the wire it would point south.)
  misconceptions:
    A: |-
      Right rule, wrong side. South is the answer for a point *above* the wire; below it the circle of field runs the opposite way. Using the left hand gives the same mistake.
    C: |-
      Thinks the magnetic field points along the current. It never does — around a straight wire $\vec{B}$ is always at right angles to the wire, wrapping round it in closed circles.
    D: |-
      Treats the field like the electric field of a charge, pointing along the line from the wire to the point. Magnetic field lines around a wire are closed circles, not spokes pointing at the wire.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A desk with a phone lying on a charging cable showing a swung compass arrow, a wireless charging pad with its coil exposed, a flip-cover case with a small magnet in its flap, and a speaker and a small cylinder-shaped vibration motor taken apart](scenes/smartphones/moving_charges_magnetism.svg "Every gadget on this desk has a current in it, and every one of those currents makes a magnetic field. This lesson starts with the phone and the wire.")

Riya is packing for a school trek and does not trust her phone's compass app. Her friend Kabir bets her fifty rupees that he can make it point the wrong way without going near it with a magnet.

He clips a long piece of plain copper wire to a holder of torch cells, stretches it straight across the lab bench, and runs the return wire the long way round, along the far edge of the table. There is a push switch in the middle. Riya's phone lies flat on the bench, right on top of the straight stretch, arrow pointing north.

Kabir presses the switch. The arrow jumps round by a large angle and stays there, steady. He lets go, and it swings back to north. Press, jump. Release, back.

There is no magnet anywhere on the bench — only a wire, a few cells and a switch. Riya hands over the fifty rupees and asks the obvious question: what did the wire do to her compass?

## The physics

In 1820 the Danish scientist **Hans Christian Oersted** saw exactly this during a lecture: a compass needle beside a wire twitched when he closed the circuit, and settled back when he opened it. His conclusion changed physics:

> **A steady electric current produces a magnetic field in the space around it.**

![On the left, a compass under a wire pointing north with the switch open and swinging sideways when current flows. On the right, the right-hand grip rule: the thumb along the current, the fingers curling round it](figures/magnetic_field_oersted/oersted-compass-and-grip-rule.svg "Switch open, the needle points north. Switch closed, it swings across the wire — the field of the current is at right angles to the wire.")

For a long straight wire, the field lines are **closed circles** in planes perpendicular to the wire, centred on it. Their direction follows the **right-hand grip rule**:

> Hold the wire in your right hand with the thumb along the conventional current $I$. Your curled fingers show the direction of $\vec{B}$ around the wire.

Two consequences matter most:

- At any point, $\vec{B}$ is perpendicular to the wire *and* to the line joining the wire to that point. It never points along the current, and never straight at or away from the wire.
- Points on **opposite sides** of the wire get fields in **opposite** directions. Above the wire and below it, the circle is running opposite ways.

Riya's phone does not contain a needle. It has a tiny **magnetometer** chip that measures the magnetic field where it sits, and the app turns that reading into an arrow. It measures the **total** field — the Earth's plus the wire's — so the arrow swings to wherever that sum points.

![Portrait photograph of a man in a dark coat with a high collar](famous/hans-christian-oersted.jpg "Hans Christian Ørsted (1777–1851). In 1820 he saw a compass needle twitch when he switched a current on — the first link found between electricity and magnetism. Public domain, via Wikimedia Commons.")

## Worked example

**Given:** Kabir's straight wire runs **south to north** across the bench, with the current flowing **north**. The phone lies flat **on top** of the wire.
**Find:** which way the wire's field points at the phone, and what happens if the wire is turned so the current flows **west** instead.

**Step 1 — current flowing north.** Thumb pointing north along the wire. Above the wire, your curled fingers are sweeping towards the **east**. So the wire's field at the phone points east, at right angles to the Earth's northward pull. The sum of the two points north-east-ish, and the arrow swings towards the east. That is Riya's jump.

**Step 2 — current flowing west.** Now the thumb points west. Above the wire, the fingers sweep towards the **north**. The wire's field now points the *same* way as the Earth's horizontal field. The two simply add: the chip measures a bigger field, but its direction is still north — so the arrow **does not move at all**.

**Sanity check:** the same current, the same distance, and in one case a big swing and in the other none — the swing depends on the *direction* of the wire's field compared with the Earth's, which is exactly what Oersted's rule predicts.

## Where the picture breaks

Kabir ran the return wire the long way round for a reason. A normal charging cable has its go and return wires side by side, carrying equal currents in opposite directions. Their circles of field point opposite ways and almost cancel a short distance away, which is why a phone lying near its own charging cable usually keeps a sensible heading.

A magnetometer chip is not a needle, either. It reports a reading, and the app draws an arrow from it — often after trying to correct for stray fields. That is why the arrow jumps to a new heading and sits still, instead of swinging and wobbling like a real compass.

And this needs **direct** current, as from cells. The mains supply reverses fifty times a second; the field it makes reverses with it, and a compass averages that to nothing.

## Key takeaway

A current makes a magnetic field — Oersted's discovery. Around a long straight wire the field lines are closed circles at right angles to the wire, and the **right-hand grip rule** gives their direction: thumb along $I$, fingers curl the way $\vec{B}$ goes. The field never points along the wire or straight at it, and it reverses from one side of the wire to the other.
