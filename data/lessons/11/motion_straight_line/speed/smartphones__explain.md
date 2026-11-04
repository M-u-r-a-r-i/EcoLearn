---
concept_id: speed
interest: smartphones
format: explain
title: Why the walking app shows two different speeds
check:
  question: |-
    Arnav's phone tracks his cycle ride to tuition, $2.4\,\text{km}$ along a straight road, which takes $10\,\text{min}$. He rides home the same way in $6\,\text{min}$. What is his average speed for the round trip?
  options:
    A: |-
      $0\,\text{km/h}$
    B: |-
      $18\,\text{km/h}$
    C: |-
      $9.0\,\text{km/h}$
    D: |-
      $19.2\,\text{km/h}$
  answer: B
  explanation: |-
    Average speed is total distance over total time: $4.8\,\text{km}$ in $16\,\text{min} = \tfrac{16}{60}\,\text{h}$, so $4.8 \div \tfrac{16}{60} = 18\,\text{km/h}$ (that is $5.0\,\text{m/s}$).
  misconceptions:
    A: |-
      Uses displacement (zero, since he ends at home) instead of distance. That gives the average velocity, not the average speed; the ride home still covers real kilometres.
    C: |-
      Counts only one way, $2.4\,\text{km}$, but divides by the whole $16\,\text{min}$. Distance must include every leg of the path.
    D: |-
      Averages the two leg speeds, $(14.4 + 24)/2$. He spends longer on the slow leg, so the true average is weighted towards the slower speed; always divide total distance by total time.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![An evening street: a phone shows a live-tracking map of a straight road, while a delivery scooter rides past kilometre markers](scenes/smartphones/motion_straight_line.svg "Every trip a phone tracks gets summed up as a distance, a time, and a speed.")

Every morning Sameer walks with his nani to the temple at the end of their road and back. This week he has installed a walking app on her phone to keep her doctor happy.

On the first day, the summary screen pops up:

*Distance 3.0 km · Time 50 min · Average speed 3.6 km/h · Moving speed 4.5 km/h*

Nani peers at it through her glasses. "Two speeds? We only went at one speed. Slowly."

His cousin Ishaan, on holiday with them, has a different complaint. "Half of that walk was *coming back*. You were going the opposite way, so that half should count as a negative speed. It should cancel out and give nearly zero."

Sameer isn't sure how to answer either of them. The app was made by people who know what they're doing.

Why are there two speeds on the screen — and is Ishaan right that walking back should cancel walking there?

## The physics

**Average speed** is the total distance travelled divided by the total time taken:

$$\text{average speed} = \frac{\text{total distance}}{\text{total time}}$$

Its SI unit is the metre per second, $\text{m/s}$; apps usually show $\text{km/h}$, and $1\,\text{m/s} = 3.6\,\text{km/h}$. Speed is a **scalar**: it says how fast, not which way.

**Speed can never be negative.** Distance adds up the length of every part of the path, so it is never negative, and the time taken is always positive. A non-negative number divided by a positive one can't be negative. That answers Ishaan: walking back adds $1.5\,\text{km}$ to the distance; it doesn't subtract anything. The lowest possible speed is zero — standing still.

The two numbers on the screen differ in *which time* they divide by. "Average speed" uses the total time, including the ten minutes Nani spent chatting at the temple gate. "Moving speed" leaves out the time spent stopped. Both are honest; they answer different questions.

![A graph of metres against time for a trip 18 m out, a 2 s rest, and 18 m back: the distance line only ever rises to 36 m, while the dashed position line returns to zero](figures/speed/distance-never-falls.svg "Distance can stay level during a rest but never falls. Average speed here is 36 m ÷ 10 s = 3.6 m/s — the rest time counts too.")

The graph shows the same pattern on a small scale: the distance line climbs, stays flat during the rest, and climbs again. It never turns down, even when the position comes back to where it began.

## Worked example

**Given:** the app's summary: $3.0\,\text{km}$ in $50\,\text{min}$, with $10\,\text{min}$ spent stopped at the temple (illustrative).
**Find:** the average speed and the moving speed, in m/s and km/h.

Convert to SI first: $3.0\,\text{km} = 3000\,\text{m}$; $50\,\text{min} = 3000\,\text{s}$; moving time $= 40\,\text{min} = 2400\,\text{s}$.

$$\text{average speed} = \frac{3000\,\text{m}}{3000\,\text{s}} = 1.0\,\text{m/s} = 1.0 \times 3.6 = 3.6\,\text{km/h}$$

$$\text{moving speed} = \frac{3000\,\text{m}}{2400\,\text{s}} = 1.25\,\text{m/s} = 1.25 \times 3.6 = 4.5\,\text{km/h}$$

Both match the app.

**Sanity check:** the average speed is lower than the moving speed, as it must be when stops are included. And $4.5\,\text{km/h}$ is a normal, steady walking pace — believable for a grandmother and a grandson who is being patient.

## Where the picture breaks

The app doesn't measure distance perfectly. It builds the path from a series of location fixes, each a few metres off, and joins them up; on a slow walk those small errors can add a little false distance, even while you stand still. It also has to guess when you are "stopped" to compute moving speed. And "average" hides everything inside the walk: Nani slows at a crossing and speeds up downhill, so at any given moment her speed was rarely exactly $4.5\,\text{km/h}$. The speed at a single moment is **instantaneous speed**, which comes later in this chapter.

## Key takeaway

Average speed $=$ total distance $\div$ total time, and every second counts, including stops. It is a scalar and can never be negative, because distance and time never are — so walking home adds to the distance instead of cancelling it. Nani's walk averaged $3.6\,\text{km/h}$.
