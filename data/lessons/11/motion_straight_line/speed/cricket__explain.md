---
concept_id: speed
interest: cricket
format: explain
title: Who is quicker between the wickets
check:
  question: |-
    In a running drill, a batter completes two runs — about $18\,\text{m}$ each — in $9.0\,\text{s}$, finishing in the same crease she started from. What was her average speed?
  options:
    A: |-
      $0\,\text{m/s}$
    B: |-
      $-4.0\,\text{m/s}$
    C: |-
      $4.0\,\text{m/s}$
    D: |-
      $2.0\,\text{m/s}$
  answer: C
  explanation: |-
    Average speed is total distance over total time: $(18 + 18)\,\text{m} / 9.0\,\text{s} = 4.0\,\text{m/s}$. Finishing where she started doesn't matter, because distance counts every leg.
  misconceptions:
    A: |-
      Uses displacement (zero, since she ended where she began) instead of distance. That gives average velocity, not average speed.
    B: |-
      Thinks speed can be negative because the second run was in the opposite direction. Distance and time are both positive, so speed never is negative.
    D: |-
      Counts only one run's $18\,\text{m}$ — the straight-line gap she covered on the final leg — instead of the whole path of $36\,\text{m}$.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A cricket ground in sunshine: a batter runs between the wickets on a 22-yard pitch while a fielder chases the ball towards the boundary rope](scenes/cricket/motion_straight_line.svg "Running between the wickets is a sprint, a turn, and another sprint.")

At the academy nets, Coach Pillai runs the drill everyone dreads: running between the wickets against the stopwatch.

Dev goes first and completes three runs in $12.0$ seconds, sliding his bat in at the far end. Farhan goes next and completes two runs in $7.5$ seconds, finishing back in the crease he started from.

"Farhan loses," announces Kunal from the side. "He ran two, Dev ran three."

"He also took less time," the coach points out.

Kunal has another idea. "Anyway, Farhan ended up exactly where he started. So his average speed is zero. You can't be quick if you went nowhere."

Farhan, still gasping, looks ready to argue with his whole body.

Who was actually quicker between the wickets? And is Kunal right that ending where you started makes your speed zero?

## The physics

**Average speed** is the total distance travelled divided by the total time taken:

$$\text{average speed} = \frac{\text{total distance}}{\text{total time}}$$

Its SI unit is the metre per second, $\text{m/s}$; in cricket you'll often see $\text{km/h}$ ($1\,\text{m/s} = 3.6\,\text{km/h}$). Speed is a **scalar** — it tells you how fast, not which way.

Speed can **never be negative**. Distance adds up the lengths of every part of the path, so it is never negative; time taken is always positive. A ratio of a non-negative number to a positive number cannot be negative. The lowest speed possible is zero, which means not moving at all.

That also answers Kunal. Farhan's path had two legs of about $18\,\text{m}$ each (illustrative — the gap between the creases). The distance is $36\,\text{m}$ even though he ended where he began. Kunal is thinking of **displacement**, which is zero for a round trip; speed uses distance.

![A graph of metres against time for a trip 18 m out, a 2 s rest, and 18 m back: the distance line only ever rises to 36 m, while the dashed position line returns to zero](figures/speed/distance-never-falls.svg "Distance can stay level (at rest) but never falls. Average speed here is 36 m ÷ 10 s = 3.6 m/s — the rest time counts too.")

Notice from the graph that **every second of the trip counts**, including time spent standing still. That is why average speed is often lower than how fast the object moved while it was moving: here the mover travelled at $4.5\,\text{m/s}$ on each leg, but averaged only $3.6\,\text{m/s}$ over the ten seconds.

## Worked example

**Given:** about $18\,\text{m}$ per run (illustrative). Dev: $3$ runs in $12.0\,\text{s}$. Farhan: $2$ runs in $7.5\,\text{s}$.
**Find:** each batter's average speed, in m/s and km/h.

Dev's total distance is $3 \times 18 = 54\,\text{m}$:

$$\text{Dev: } \frac{54\,\text{m}}{12.0\,\text{s}} = 4.5\,\text{m/s} = 4.5 \times 3.6 = 16.2\,\text{km/h}$$

Farhan's total distance is $2 \times 18 = 36\,\text{m}$:

$$\text{Farhan: } \frac{36\,\text{m}}{7.5\,\text{s}} = 4.8\,\text{m/s} = 4.8 \times 3.6 \approx 17.3\,\text{km/h}$$

Farhan was quicker between the wickets, by $0.3\,\text{m/s}$.

**Sanity check:** if Farhan had kept up his $4.8\,\text{m/s}$ for Dev's $54\,\text{m}$, he'd have needed $54/4.8 = 11.25\,\text{s}$ — less than Dev's $12.0\,\text{s}$. Consistent. Both speeds are a brisk jog-to-sprint pace, which is realistic once you include the turns.

## Where the picture breaks

"Average speed" hides everything inside the interval. Each batter sprints, brakes hard, turns and accelerates again, so their speed at any given instant ranges from nearly zero at the turn to well above the average mid-pitch. The speed a speed gun shows for a delivery is a different idea — the speed at (nearly) one instant, which you'll meet as **instantaneous speed**. Also, $18\,\text{m}$ per run is approximate: batters stretch their bats over the crease rather than running every centimetre, so a coach comparing two batters is really comparing times over roughly equal distances.

## Key takeaway

Average speed $=$ total distance $\div$ total time. It is a scalar and can never be negative, because distance and time never are. A round trip still has a real, positive average speed — Farhan's two runs averaged $4.8\,\text{m/s}$, even though he finished where he started.
