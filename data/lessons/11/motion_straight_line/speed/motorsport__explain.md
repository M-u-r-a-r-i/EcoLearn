---
concept_id: speed
interest: motorsport
format: explain
title: Who was quicker on the shuttle run
check:
  question: |-
    In a tyre-warming run, a test car covers $400\,\text{m}$ down a straight and $400\,\text{m}$ back, taking $80\,\text{s}$ in total, and finishes beside the cone it started from. What was its average speed?
  options:
    A: |-
      $0\,\text{m/s}$
    B: |-
      $5\,\text{m/s}$
    C: |-
      $-10\,\text{m/s}$
    D: |-
      $10\,\text{m/s}$
  answer: D
  explanation: |-
    Average speed is total distance over total time: $(400 + 400)\,\text{m} \div 80\,\text{s} = 10\,\text{m/s}$. Finishing where it started makes no difference, because distance counts every leg.
  misconceptions:
    A: |-
      Uses the displacement, which is zero because the car ended where it began. That gives the average velocity, not the average speed.
    B: |-
      Counts only one $400\,\text{m}$ leg against the whole $80\,\text{s}$, leaving half the path out of the total distance.
    C: |-
      Makes the speed negative because the second leg pointed the other way. Distance and time are both positive, so their ratio never is.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A long straight at a race circuit with a car accelerating away from the timing beam at the start line, distance boards reading 0, 100 and 200 along the verge, and an arrow marking the positive direction](scenes/motorsport/motion_straight_line.svg "No circuit today — just a 200-metre strip, two cones and a stopwatch.")

The karting circuit is closed for resurfacing, so the club's practice session has been squeezed onto a $200\,\text{m}$ strip of the access road with a cone at each end. Coach Salim runs the drill everyone secretly enjoys: out, turn, back, against the stopwatch.

Jaya goes first. Three lengths of the strip, finishing at the far cone: $60$ seconds.

Ayaan goes next. Two lengths, out and back, finishing at the cone he started from: $50$ seconds.

"Easy," says Ayaan's friend Nitin, from the shade. "Jaya did three lengths, Ayaan did two. Jaya wins."

"She also took longer," says the coach.

Nitin tries again. "Fine — but Ayaan finished exactly where he started. So his average speed is zero. You can't be quick if you went nowhere."

Ayaan, still catching his breath in the kart, looks ready to argue.

Who was actually quicker on the strip — and is Nitin right that ending where you started makes your speed zero?

## The physics

**Average speed** is the total distance travelled divided by the total time taken:

$$\text{average speed} = \frac{\text{total distance}}{\text{total time}}$$

Its SI unit is the metre per second, $\text{m/s}$. Motorsport talks in $\text{km/h}$, and the conversion is worth memorising: $1\,\text{m/s} = 3.6\,\text{km/h}$, so to go from km/h to m/s you divide by $3.6$. Speed is a **scalar** — it says how fast, never which way.

Speed can **never be negative**. Distance adds the lengths of every part of the path, so it is never negative, and a time taken is always positive. A non-negative number divided by a positive number cannot come out negative. The smallest possible speed is zero, which means not moving at all.

That settles Nitin. Ayaan's path was two legs of $200\,\text{m}$, so his distance is $400\,\text{m}$ even though he finished at his starting cone. What Nitin is thinking of is **displacement**, which really is zero for a round trip. Speed uses distance instead.

![A graph of metres against time for a trip 18 m out, a 2 s rest, and 18 m back: the distance line only ever rises to 36 m, while the dashed position line returns to zero](figures/speed/distance-never-falls.svg "Distance can stay level while the object is stopped, but it never falls. The dashed position line comes back to zero; the solid distance line does not.")

The figure makes a second point worth having. **Every second counts**, including the seconds spent stopped — in the flat stretch the distance line stops climbing but the clock keeps running. That is why an average speed is usually lower than the speed reached while actually moving: the turns at the cones, where a kart is almost stationary, drag the average down.

## Worked example

**Given:** the strip is $200\,\text{m}$ between cones. Jaya: $3$ lengths in $60\,\text{s}$. Ayaan: $2$ lengths in $50\,\text{s}$.
**Find:** each driver's average speed, in m/s and km/h.

Jaya's total distance is $3 \times 200 = 600\,\text{m}$:

$$\text{Jaya: } \frac{600\,\text{m}}{60\,\text{s}} = 10\,\text{m/s} = 10 \times 3.6 = 36\,\text{km/h}$$

Ayaan's total distance is $2 \times 200 = 400\,\text{m}$:

$$\text{Ayaan: } \frac{400\,\text{m}}{50\,\text{s}} = 8\,\text{m/s} = 8 \times 3.6 = 28.8\,\text{km/h}$$

Jaya was quicker on the strip, by $2\,\text{m/s}$ — and Ayaan's average speed is very obviously not zero.

**Sanity check:** had Ayaan kept up his $8\,\text{m/s}$ over Jaya's $600\,\text{m}$, he would have needed $600/8 = 75\,\text{s}$, well outside her $60\,\text{s}$. Consistent. And $36\,\text{km/h}$ is a believable average for a kart that has to stop and turn every $200\,\text{m}$.

## Where the picture breaks

An average speed hides everything that happened inside the interval. Both drivers accelerated hard, ran fast down the middle, braked, turned almost to a standstill and set off again, so their speed at any instant ranged from nearly zero to well above the average. The number a speed trap shows is a different idea altogether — the speed at very nearly one instant, which you will meet as **instantaneous speed**. The $200\,\text{m}$ is also approximate: a kart swings wide at each turn rather than pivoting on the cone, so each "length" is a little longer than the gap between the cones.

## Key takeaway

Average speed $=$ total distance $\div$ total time. It is a scalar and can never be negative, because neither distance nor time ever is. A round trip still has a real, positive average speed: Ayaan's two lengths averaged $8\,\text{m/s}$, or about $29\,\text{km/h}$, even though he finished at the cone he started from.
