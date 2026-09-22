---
concept_id: speed
interest: football
format: explain
title: Can you be quick and go nowhere
check:
  question: |-
    In a fitness drill, a midfielder sprints to a cone $25\,\text{m}$ away and straight back, finishing where she started, in $10.0\,\text{s}$. What was her average speed?
  options:
    A: |-
      $5.0\,\text{m/s}$
    B: |-
      $0\,\text{m/s}$
    C: |-
      $-5.0\,\text{m/s}$
    D: |-
      $2.5\,\text{m/s}$
  answer: A
  explanation: |-
    Average speed is total distance over total time: $(25 + 25)\,\text{m} / 10.0\,\text{s} = 5.0\,\text{m/s}$. Finishing where she started doesn't matter, because distance counts every leg.
  misconceptions:
    B: |-
      Uses displacement (zero, since she ended where she began) instead of distance. That gives average velocity, not average speed.
    C: |-
      Thinks speed can be negative because the second leg was in the opposite direction. Distance and time are both positive, so speed never is negative.
    D: |-
      Counts only one leg's $25\,\text{m}$ instead of the whole path of $50\,\text{m}$.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A winger dribbles along the touchline towards goal, chased by a defender, while the goalkeeper comes off the line; a number line with origin O and +x runs beneath](scenes/football/motion_straight_line.svg "Football fitness is sprint, stop, turn and sprint again — up and down one line.")

Pre-season at the academy, and Coach D'Souza has laid out cones $20\,\text{m}$ apart for the shuttle drill everyone hates.

Mehul goes first: cone to cone and back, twice — four legs — in $16.0$ seconds, finishing exactly where he started. Tenzin goes next: three legs, ending at the far cone, in $12.5$ seconds.

Aakash, sitting out with a sore ankle, has the stopwatch and strong opinions. "Tenzin wins. Mehul finished where he began. His average speed is zero — he literally went nowhere."

"He ran eighty metres!" Tenzin protests, oddly defending his rival.

"And you took less time," Aakash says. "So you're quicker anyway."

Coach D'Souza just raises an eyebrow and waits.

Who was actually quicker over the drill? And can you really have a speed of zero after sprinting for sixteen seconds?

## The physics

**Average speed** is the total distance travelled divided by the total time taken:

$$\text{average speed} = \frac{\text{total distance}}{\text{total time}}$$

Its SI unit is the metre per second, $\text{m/s}$; player-tracking systems often show $\text{km/h}$ ($1\,\text{m/s} = 3.6\,\text{km/h}$). Speed is a **scalar** — how fast, not which way.

Speed can **never be negative**. Distance adds up the lengths of every part of the path, so it is never negative; time taken is always positive. A ratio of a non-negative number to a positive number cannot be negative. The lowest speed possible is zero, which means not moving at all.

That settles Aakash's first claim. Mehul's path had four legs of $20\,\text{m}$: a distance of $80\,\text{m}$, even though he ended where he began. Aakash is thinking of **displacement**, which is zero for a round trip; speed uses distance.

![A graph of metres against time for a trip 18 m out, a 2 s rest, and 18 m back: the distance line only ever rises to 36 m, while the dashed position line returns to zero](figures/speed/distance-never-falls.svg "Distance can stay level (at rest) but never falls. Average speed here is 36 m ÷ 10 s = 3.6 m/s — the rest time counts too.")

Notice from the graph that **every second counts**, including time spent standing still. That is why average speed is often lower than how fast something moved while it was moving: here the mover travelled at $4.5\,\text{m/s}$ on each leg, but averaged only $3.6\,\text{m/s}$ over the ten seconds.

## Worked example

**Given:** cones $20\,\text{m}$ apart. Mehul: $4$ legs in $16.0\,\text{s}$. Tenzin: $3$ legs in $12.5\,\text{s}$.
**Find:** each player's average speed, in m/s and km/h.

Mehul's total distance is $4 \times 20 = 80\,\text{m}$:

$$\text{Mehul: } \frac{80\,\text{m}}{16.0\,\text{s}} = 5.0\,\text{m/s} = 5.0 \times 3.6 = 18.0\,\text{km/h}$$

Tenzin's total distance is $3 \times 20 = 60\,\text{m}$:

$$\text{Tenzin: } \frac{60\,\text{m}}{12.5\,\text{s}} = 4.8\,\text{m/s} = 4.8 \times 3.6 \approx 17.3\,\text{km/h}$$

Mehul was quicker, by $0.2\,\text{m/s}$ — Aakash was wrong twice.

**Sanity check:** at Mehul's $5.0\,\text{m/s}$, Tenzin's $60\,\text{m}$ would take $60/5.0 = 12.0\,\text{s}$ — less than Tenzin's $12.5\,\text{s}$. Consistent. Both are realistic averages once you include three or four sharp turns.

## Where the picture breaks

"Average speed" hides everything inside the interval. Each player sprints, brakes, plants a foot, turns and accelerates again, so their speed at any instant ranges from almost zero at the cone to well above the average in mid-leg. The top speed a tracking board flashes up is a different idea — the speed at (nearly) one instant, which you'll meet as **instantaneous speed**. And a real player doesn't run exactly $20\,\text{m}$ per leg: they turn a little before or beyond the cone, so the coach is comparing times over roughly equal distances.

## Key takeaway

Average speed $=$ total distance $\div$ total time. It is a scalar and can never be negative, because distance and time never are. A round trip still has a real, positive average speed — Mehul's four shuttles averaged $5.0\,\text{m/s}$, even though he finished where he started.
