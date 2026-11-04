---
concept_id: speed
interest: gaming
format: explain
title: Who really won the pier challenge
check:
  question: |-
    In an open-world game, a delivery drone flies $300\,\text{m}$ in a straight line to a drop point, hovers there for $10\,\text{s}$, and flies $300\,\text{m}$ straight back. The whole trip takes $50\,\text{s}$, including the hover. What is its average speed for the trip?
  options:
    A: |-
      $0\,\text{m/s}$
    B: |-
      $15\,\text{m/s}$
    C: |-
      $12\,\text{m/s}$
    D: |-
      $6.0\,\text{m/s}$
  answer: C
  explanation: |-
    Average speed is total distance over total time, and the hover counts as time: $(300 + 300)\,\text{m} / 50\,\text{s} = 12\,\text{m/s}$.
  misconceptions:
    A: |-
      Uses displacement (zero, because the drone came back to where it started) instead of distance. That gives the average velocity, not the average speed.
    B: |-
      Leaves out the $10\,\text{s}$ spent hovering and divides by $40\,\text{s}$. Average speed uses the total time, including time at rest.
    D: |-
      Counts only one $300\,\text{m}$ leg — the straight-line gap between base and drop point — instead of the whole $600\,\text{m}$ path.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A gaming desk at night: a monitor shows a side-scrolling game whose runner moves along a straight track marked like a number line, with a position and velocity readout; a tablet replays a velocity-time graph](scenes/gaming/motion_straight_line.svg "Racing and running games constantly time how fast you cover ground. But which ground counts?")

Ananya and Kunal have a running bet in their favourite open-world racing game: whoever wins more weekend challenges picks the next game they both buy.

This weekend's challenges are on the harbour map. Kunal does the *Harbour Sprint*: floor it along the seafront road, $500\,\text{m}$ from the fish market to the lighthouse, in $25$ seconds. Ananya does the *Pier Run*: drive to the end of the $400\,\text{m}$ pier, spin round, and drive back to the start line, in $36$ seconds.

"I win," Kunal declares. "You took longer. And anyway, you ended up exactly where you started. Your average speed is zero. You can't be fast if you went nowhere."

Ananya points at her replay, where her car is clearly screaming down the pier and back. "Does that look like zero to you?"

Who was actually faster? And is Kunal right that finishing where you started makes your average speed zero?

## The physics

**Average speed** is the total distance travelled divided by the total time taken:

$$\text{average speed} = \frac{\text{total distance}}{\text{total time}}$$

Its SI unit is the metre per second, $\text{m/s}$; racing games usually show $\text{km/h}$ ($1\,\text{m/s} = 3.6\,\text{km/h}$). Speed is a **scalar** — it tells you how fast, not which way.

Speed can **never be negative**. Distance adds up the lengths of every part of the path, so it is never negative, and time taken is always positive. A non-negative number divided by a positive number can't be negative. The lowest average speed possible is zero, which means not moving at all.

That settles Kunal's second claim. Ananya's path had two legs of $400\,\text{m}$: the distance is $800\,\text{m}$, even though she ended where she began. Kunal is thinking of **displacement**, which is zero for a round trip. Speed uses distance.

![A graph of metres against time for a trip 18 m out, a 2 s rest, and 18 m back: the distance line only ever rises to 36 m, while the dashed position line returns to zero](figures/speed/distance-never-falls.svg "Distance can stay level (at rest) but never falls. Average speed here is 36 m ÷ 10 s = 3.6 m/s — the time at rest counts too.")

The graph makes a second point: **every second counts**, including time spent standing still. The mover in it went at $4.5\,\text{m/s}$ on each leg but averaged only $3.6\,\text{m/s}$ over the ten seconds, because of the $2\,\text{s}$ pause. Ananya's slow spin at the end of the pier counts against her in exactly the same way.

## Worked example

**Given:** Kunal: $500\,\text{m}$ in $25\,\text{s}$. Ananya: $400\,\text{m}$ out and $400\,\text{m}$ back in $36\,\text{s}$ (illustrative numbers).
**Find:** each driver's average speed in m/s and km/h.

Kunal's distance is $500\,\text{m}$:

$$\text{Kunal: } \frac{500\,\text{m}}{25\,\text{s}} = 20.0\,\text{m/s} = 20.0 \times 3.6 = 72\,\text{km/h}$$

Ananya's distance is $400 + 400 = 800\,\text{m}$:

$$\text{Ananya: } \frac{800\,\text{m}}{36\,\text{s}} \approx 22.2\,\text{m/s} = 22.2 \times 3.6 \approx 80\,\text{km/h}$$

Ananya was faster on average, by about $8\,\text{km/h}$ — despite taking longer and despite the turn.

**Sanity check:** at $22.2\,\text{m/s}$ Ananya would cover Kunal's $500\,\text{m}$ in $500/22.2 \approx 22.5\,\text{s}$, less than his $25\,\text{s}$. Consistent. And both averages are well below the top speeds a racing car reaches, which makes sense for runs that include a standing start (and, for Ananya, a U-turn).

## Where the picture breaks

An average hides everything inside the interval. Both cars launch from rest, reach far more than their average speed mid-run, and Ananya's drops almost to zero at the turn. The number on the in-game speedometer is a different idea — the speed at one instant, which you'll meet as **instantaneous speed**. Also, a real U-turn isn't on a straight line: the car swings round in an arc, adding a little extra distance we've ignored. Games also sometimes round or smooth what they display; we've assumed the challenge timer and track lengths are exact.

## Key takeaway

Average speed $=$ total distance $\div$ total time, with every second counted, including stops. It is a scalar and can never be negative, because distance and time never are. A round trip has a real, positive average speed: Ananya's pier run averaged about $22\,\text{m/s}$ even though she finished on the start line.
