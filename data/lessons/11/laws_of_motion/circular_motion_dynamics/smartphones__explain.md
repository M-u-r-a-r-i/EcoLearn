---
concept_id: circular_motion_dynamics
interest: smartphones
format: explain
title: The speed the maps app warned about
check:
  question: |-
    A car takes an unbanked, level curve of radius $40\,\text{m}$. The coefficient of static friction between tyres and road is $0.40$. Taking $g = 10\,\text{m/s}^2$, what is the maximum speed at which it can take the curve without skidding?
  options:
    A: |-
      $160\,\text{m/s}$
    B: |-
      $12.6\,\text{m/s}$
    C: |-
      $4.0\,\text{m/s}$
    D: |-
      $20\,\text{m/s}$
  answer: B
  explanation: |-
    Static friction supplies the centripetal force, so $mv^2/r \le \mu_s mg$, giving $v_\text{max} = \sqrt{\mu_s r g} = \sqrt{0.40 \times 40 \times 10} = \sqrt{160} \approx 12.6\,\text{m/s}$.
  misconceptions:
    A: |-
      Sets up the right condition but forgets the square root at the end. $\mu_s r g = 160$ is $v^2$ in $\text{m}^2/\text{s}^2$, not a speed; a car at $160\,\text{m/s}$ would be going faster than most aircraft take off.
    C: |-
      Leaves $g$ out, using $v = \sqrt{\mu_s r}$. The grip available comes from the normal force $mg$, so $g$ must appear, and without it the units don't even come out as a speed.
    D: |-
      Leaves out the coefficient of friction, as though the tyres could supply a sideways force equal to the car's whole weight. Here they can supply only $0.40$ of it.
author: claude-code/opus-5
written: 2026-09-25
---
## The story

![A study room at night: a camera drone hovers pushing air down, a phone tumbles off a shelf towards the tiles, and a power bank dangles off a desk by its cable](scenes/smartphones/laws_of_motion.svg "Nothing moves in a curve unless a net force points towards the centre. On a road, that force has to come from somewhere real.")

Leela has just got her licence and is driving the family to a hill station, with her brother Harsh navigating on the phone clipped to the dashboard. It has been raining. As they climb the ghat road, the maps app chimes: *sharp curve ahead*. A yellow signboard at the bend shows a low speed limit and a bent arrow.

Leela slows right down. A big SUV behind them doesn't, swings past, and takes the curve noticeably faster.

"See, it's heavier," Leela says. "More weight, more grip. Heavy cars can take bends faster. The sign is for little cars like ours."

Harsh looks at the curve on the map, a tight hook of blue line. Somebody chose the number on that signboard for every car that would ever drive past it, small or big, on a dry day or a wet one.

So what actually decides how fast a car can go round a curve — and does the car's weight come into it at all?

## The physics

A body moving in a circle of radius $r$ at speed $v$ has a **centripetal acceleration** $v^2/r$ towards the centre. By the second law, something must supply a net force towards the centre:

$$F_c = \frac{mv^2}{r}$$

This **centripetal force** is not a new kind of force. It is whatever real force, or combination of forces, happens to point towards the centre: a string's tension, gravity, a normal force, or friction. The first step in every problem is to **identify which one**.

**Level road.** For a car on a flat curve, only **static friction** between tyres and road points sideways, towards the centre. (Static, because the tyres aren't sliding across the road.) Friction can be at most $\mu_s N = \mu_s mg$, so

$$\frac{mv^2}{r} \le \mu_s mg \quad\Rightarrow\quad v_\text{max} = \sqrt{\mu_s r g}$$

The mass **cancels**. A heavier car needs more centripetal force, but it also presses harder on the road and gets proportionally more grip.

**Banked road.** Tilting the road by an angle $\theta$, higher on the outside, lets part of the **normal force** point towards the centre too. With no friction at all, the ideal speed is $v_0 = \sqrt{r g \tan\theta}$. With friction helping, the maximum safe speed rises to

$$v_\text{max} = \sqrt{\frac{r g\,(\mu_s + \tan\theta)}{1 - \mu_s\tan\theta}}$$

![Left: cross-section of a road banked at angle theta, higher on the outside, with a vehicle on it. Right: free-body diagram at maximum speed with the normal force perpendicular to the road tilted towards the centre, weight straight down, friction down the slope, and a horizontal acceleration towards the centre](figures/circular_motion_dynamics/banked-road-forces.svg "On a banked curve, the tilted normal force and friction together point towards the centre. Set θ = 0 and this becomes the level road, with friction doing all the work.")

## Worked example

**Given:** a level, wet curve of radius $r = 100\,\text{m}$, with $\mu_s = 0.40$ (illustrative). Take $g = 10\,\text{m/s}^2$.
**Find:** the maximum safe speed, and whether the SUV's extra weight helps.

1. *Which force?* The road is level, so static friction is the only force towards the centre.

2. *Maximum speed.*
$$v_\text{max} = \sqrt{\mu_s r g} = \sqrt{0.40 \times 100 \times 10} = \sqrt{400} = 20\,\text{m/s}$$
That is $72\,\text{km/h}$ — the very edge of grip, which is why the sign shows a figure well below it.

3. *The SUV.* $m$ does not appear in $v_\text{max}$, so a car twice as heavy has exactly the same limit. The SUV simply had less margin left.

**Sanity check:** on a dry road $\mu_s$ might double, which only raises $v_\text{max}$ by a factor of $\sqrt{2}$ — about $28\,\text{m/s}$ — so rain costs speed, but not half of it.

## Where the picture breaks

Real curves are rarely flat or perfectly circular, and roads are often cambered slightly for drainage. $\mu_s$ is not a fixed number: it changes with rain, tyre wear, oil on the road and temperature, which is why signboards are set with a large safety margin. A heavy SUV is also taller, so it may *tip* before it skids — something our point-mass model can't show. And the maps app does not calculate any of this; it only reads the road's shape and passes on a warning. The physics is in the road, not in the phone.

## Key takeaway

Circular motion needs a net force $mv^2/r$ towards the centre, supplied by a real force you must identify — on a level road, static friction. That gives $v_\text{max} = \sqrt{\mu_s r g}$, independent of the car's mass. Banking the road lets the normal force help, raising the safe speed.
