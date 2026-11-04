---
concept_id: circular_motion_dynamics
interest: motorsport
format: explain
title: The banked corner you can take hands off the wheel
check:
  question: |-
    A car takes a level, unbanked corner of radius $50\,\text{m}$. The coefficient of static friction between tyres and road is $0.50$; take $g = 9.8\,\text{m/s}^2$. What is the greatest speed at which it can hold the corner?
  options:
    A: |-
      $15.7\,\text{m/s}$
    B: |-
      $22.1\,\text{m/s}$
    C: |-
      $245\,\text{m/s}$
    D: |-
      It cannot be found without knowing the car's mass.
  answer: A
  explanation: |-
    Friction must supply $mv^2/r$ and can give at most $\mu_s mg$, so $v_\text{max} = \sqrt{\mu_s r g} = \sqrt{0.50 \times 50 \times 9.8} = \sqrt{245} \approx 15.7\,\text{m/s}$.
  misconceptions:
    B: |-
      Leaves $\mu_s$ out and computes $\sqrt{rg}$. The grip available is what sets the limit, so the coefficient must appear in the formula.
    C: |-
      Stops at $v^2 = \mu_s r g = 245$ without taking the square root. Check the units: $245$ is in $\text{m}^2/\text{s}^2$, not $\text{m/s}$.
    D: |-
      Thinks a heavier car can corner faster or slower. The mass appears on both sides of $mv^2/r \le \mu_s mg$ and cancels, so the limit is the same for every car on that surface.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A race car in a braking zone with glowing brake discs, a skid mark and tyre smoke, a tyre barrier along the wall and a marshal with a yellow flag](scenes/motorsport/laws_of_motion.svg "Straight-line braking is the easy part. The corner after it is where cars run out of grip.")

There is an old high-speed test bowl on the edge of the city, built decades ago for tyre testing and used a few days a year now by the car club. Its corners are not flat: the outer edge of the track is lifted so steeply that walking up it is hard work.

One of the older members has told Gurpreet that there is exactly one speed at which you can go round the bank with your hands off the wheel — no steering, no leaning on the tyres — and the car will simply track round on its own.

Padma doesn't believe a word of it. "It's a road," she says. "What holds a car on a curve is grip. Tilt it or don't tilt it, you still need the tyres."

She has evidence. On a level roundabout in the rain last month, she turned the wheel and the car ploughed straight on towards the kerb anyway.

So what actually turns a car — and why would anyone build a road on a slant?

## The physics

A body going round a circle of radius $r$ at speed $v$ has a **centripetal acceleration** of $v^2/r$ pointing at the centre. By Newton's second law, something must supply a net force

$$F_\text{c} = \frac{mv^2}{r}$$

towards the centre. **Centripetal force is not a new kind of force.** It is the name for whatever real forces happen to add up to point inwards, and the whole job in any problem is to say which ones.

**Level road.** Weight and the normal force are both vertical and cancel. The only horizontal force available is **friction** from the road on the tyres, and since a rolling tyre is not sliding sideways, it is **static** friction, with a ceiling of $\mu_s N = \mu_s mg$:

$$\frac{mv^2}{r} \le \mu_s mg \quad\Rightarrow\quad v_\text{max} = \sqrt{\mu_s r g}$$

The mass cancels. That is Padma's wet roundabout: the water cut $\mu_s$, friction could no longer supply $mv^2/r$, and the car carried on nearly straight by inertia, exactly as the first law says it must.

**Banked road.** Tilt the surface through an angle $\theta$ and the normal force, always perpendicular to the road, tilts inwards with it — so part of $N$ now points towards the centre. With **no friction at all** there is exactly one speed at which the normal force does the whole job:

$$\tan\theta = \frac{v_0^2}{rg} \quad\Rightarrow\quad v_0 = \sqrt{rg\tan\theta}$$

That is Gurpreet's hands-off speed, and it is real. Above it, friction acts down the slope as well, and at its limit the greatest safe speed becomes

$$v_\text{max} = \sqrt{rg\,\frac{\mu_s + \tan\theta}{1 - \mu_s\tan\theta}}$$

![Left: cross-section of a road banked at an angle, outer edge higher, with a vehicle on it. Right: the free-body diagram at maximum speed — the normal force perpendicular to the tilted surface, the weight straight down, friction down the slope, and the resulting horizontal acceleration towards the centre](figures/circular_motion_dynamics/banked-road-forces.svg "On a bank, the normal force and friction both have parts pointing at the centre, so together they can supply far more centripetal force than friction could alone.")

## Worked example

**Given:** a corner of radius $r = 100\,\text{m}$; $\mu_s = 0.80$ for racing tyres on dry tarmac (illustrative); the bank is $\theta = 20^\circ$, so $\tan 20^\circ = 0.364$; $g = 9.8\,\text{m/s}^2$.
**Find:** the maximum speed on a *level* corner of the same radius and surface; the hands-off speed on the bank; and the maximum speed on the bank.

*Level corner:*

$$v_\text{max} = \sqrt{0.80 \times 100 \times 9.8} = \sqrt{784} = 28\,\text{m/s} \approx 101\,\text{km/h}$$

*Hands-off speed on the bank,* where friction is not needed at all:

$$v_0 = \sqrt{100 \times 9.8 \times 0.364} = \sqrt{357} \approx 18.9\,\text{m/s} \approx 68\,\text{km/h}$$

Gurpreet's older member was right — but it is a fairly gentle speed, not a fast one.

*Maximum on the bank,* with friction helping as well:

$$v_\text{max} = \sqrt{980 \times \frac{0.80 + 0.364}{1 - 0.291}} = \sqrt{1609} \approx 40\,\text{m/s} \approx 144\,\text{km/h}$$

Banking the same corner, with the same tyres, raises the limit from about $101$ to about $144\,\text{km/h}$.

**Sanity check:** the units work out, since $\sqrt{\text{m} \times \text{m/s}^2}$ is $\text{m/s}$; and setting $\theta = 0$ in the banked formula gives back $\sqrt{\mu_s r g}$, while setting $\mu_s = 0$ gives back the hands-off speed.

## Where the picture breaks

We treated the car as a point. A tall vehicle can **topple** outwards before it ever skids, which depends on its height and track width and needs torques, later. The maximum-speed formula also assumes friction sitting exactly at its limit with no margin at all, so real limits are set well below it, and $\mu_s$ falls sharply in rain. Race cars break the formula in a useful way: aerodynamic **downforce** adds to $N$ without adding to $m$, so $v_\text{max}$ climbs above $\sqrt{\mu_s r g}$ and, unlike weight, it grows with speed. And the outward lean you feel in a corner is not an outward force on you from the road's point of view — it is your own inertia, with the seat supplying the inward push.

## Key takeaway

Circular motion needs a net force $mv^2/r$ towards the centre, and your job is to name the real force supplying it. On a level road it is static friction, giving $v_\text{max} = \sqrt{\mu_s r g}$, independent of mass. Banking tilts the normal force inwards so that it helps: with no friction the ideal speed is $v_0 = \sqrt{rg\tan\theta}$, and with friction the limit rises to $\sqrt{rg(\mu_s + \tan\theta)/(1 - \mu_s\tan\theta)}$.
