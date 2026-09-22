---
concept_id: circular_motion_dynamics
interest: gaming
format: explain
title: Why the racing sim lets you corner faster on the banked oval
check:
  question: |-
    A car in a realistic racing game takes a level, unbanked curve of radius $50\,\text{m}$. The coefficient of static friction between tyres and track is $0.80$; take $g = 9.8\,\text{m/s}^2$. What is the maximum speed at which it can take the curve without skidding?
  options:
    A: |-
      $392\,\text{m/s}$
    B: |-
      $19.8\,\text{m/s}$
    C: |-
      $24.7\,\text{m/s}$
    D: |-
      $6.3\,\text{m/s}$
  answer: B
  explanation: |-
    Static friction supplies the centripetal force, up to $\mu_s mg$. Setting $\dfrac{mv^2}{r} = \mu_s mg$ gives $v_\text{max} = \sqrt{\mu_s r g} = \sqrt{0.80 \times 50 \times 9.8} = \sqrt{392} \approx 19.8\,\text{m/s}$.
  misconceptions:
    A: |-
      Forgets the square root: $\mu_s r g$ is $v^2$ (in m²/s²), not $v$. A car at $392\,\text{m/s}$ would be faster than sound.
    C: |-
      Divides by $\mu_s$ instead of multiplying, computing $\sqrt{rg/\mu_s}$. More grip must allow more speed, so $\mu_s$ belongs in the numerator.
    D: |-
      Leaves out $g$. The maximum friction force is $\mu_s N = \mu_s mg$, so $g$ enters the result; the answer also has the wrong units without it.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A gaming desk at night: a racing game on the monitor and a zero-gravity game on a tablet](scenes/gaming/laws_of_motion.svg "The dashed line is where the kart would go with no grip. Friction, pointing towards the centre, is what bends its path.")

Leela and Tushar are practising time trials in a racing sim that prides itself on real physics. On the city circuit there's a flat hairpin, and Tushar keeps losing it there. At about 90 km/h, his car simply refuses to turn: the tyres squeal, the nose runs wide, and he slides straight into the barrier.

Then they switch to the oval track. Its curves are about the same size as the hairpin, but the track surface is tilted steeply, the outside edge far higher than the inside. Here Leela sweeps round at 105 km/h without a twitch.

"The game's rigged," says Tushar. "Same car, same tyres, same size of corner. Why does the oval let you go faster?"

Leela doesn't know either. She only knows the tilt matters. But what is actually turning the car in each corner, and how does tilting the track help?

## The physics

A car moving in a circle of radius $r$ at speed $v$ has a **centripetal acceleration** $v^2/r$, directed towards the centre. By Newton's second law, that requires a net force towards the centre:

$$F_\text{c} = \frac{mv^2}{r}$$

The **centripetal force** is not a new kind of force. It is the name for whatever real forces add up to point towards the centre. In every problem, the job is to **identify what supplies it**.

**Level track.** Weight and the normal force are vertical and cancel. The only horizontal force is **friction** from the track on the tyres. The tyres grip without slipping sideways, so this is **static** friction, and it points towards the centre. It can be at most $\mu_s N = \mu_s mg$, so the corner can be taken only if

$$\frac{mv^2}{r} \le \mu_s mg \quad\Rightarrow\quad v_\text{max} = \sqrt{\mu_s r g}$$

Above this speed, friction can't supply enough inward force. The car's inertia carries it off along a straighter line, which is what Tushar saw.

**Banked track.** Tilting the track at angle $\theta$ tilts the normal force towards the centre, so part of $N$ now helps. With no friction at all, there is exactly one speed at which the normal force does the whole job:

$$v_0 = \sqrt{rg\tan\theta}$$

Above $v_0$, friction also acts, down the slope, until it reaches its limit. Resolving the forces horizontally and vertically then gives the maximum safe speed:

$$v_\text{max} = \sqrt{rg\,\frac{\mu_s + \tan\theta}{1 - \mu_s\tan\theta}}$$

![Left: cross-section of a road banked at angle theta, higher on the outside, with a vehicle on it. Right: free-body diagram at maximum speed with the normal force perpendicular to the road tilted towards the centre, weight straight down, and friction down the slope, plus a horizontal acceleration arrow towards the centre](figures/circular_motion_dynamics/banked-road-forces.svg "On the banked oval, both the normal force and friction have parts pointing towards the centre, so together they supply more centripetal force than friction alone.")

## Worked example

**Given (illustrative values):** both corners have radius $r = 80\,\text{m}$; $\mu_s = 0.60$ between tyres and track; the oval is banked at $20^\circ$ ($\tan 20^\circ = 0.364$); $g = 9.8\,\text{m/s}^2$.
**Find:** the maximum speed on (a) the level hairpin and (b) the banked oval; (c) the speed at which the oval needs no friction.

(a) Level:

$$v_\text{max} = \sqrt{0.60 \times 80 \times 9.8} = \sqrt{470.4} \approx 21.7\,\text{m/s} \approx 78\,\text{km/h}$$

Tushar at $90\,\text{km/h}$ was over the limit.

(b) Banked, with $rg = 784\,\text{m}^2/\text{s}^2$:

$$v_\text{max} = \sqrt{784 \times \frac{0.60 + 0.364}{1 - 0.60 \times 0.364}} = \sqrt{784 \times \frac{0.964}{0.782}} \approx \sqrt{967} \approx 31.1\,\text{m/s} \approx 112\,\text{km/h}$$

Leela at $105\,\text{km/h}$ was safely inside it.

(c) $v_0 = \sqrt{784 \times 0.364} = \sqrt{285} \approx 16.9\,\text{m/s} \approx 61\,\text{km/h}$.

**Sanity check:** units: $\sqrt{\text{m} \times \text{m/s}^2} = \text{m/s}$ ✓. With $\theta = 0$ the banked formula reduces to $\sqrt{\mu_s r g}$, the level result ✓; with $\mu_s = 0$ it reduces to $\sqrt{rg\tan\theta}$ ✓.

## Where the picture breaks

We treated the car as a point. Real racing cars also use aerodynamic downforce, which presses them onto the track and raises $N$, and so the friction available; a sim may model that too, which our formulas leave out. Real tyres don't have one fixed $\mu_s$: grip changes with temperature, wear and load. And the formulas give the speed at which friction is exactly at its limit, with no safety margin at all. The drivers in the sim feel pushed "outwards" in the corners, but from the track's frame there is no outward force: it is their inertia, with the seat pushing them inwards.

## Key takeaway

Circular motion needs a net force $mv^2/r$ towards the centre, supplied by real forces. On a level track it comes from static friction, so $v_\text{max} = \sqrt{\mu_s r g}$. Banking tilts the normal force inwards so it helps: with no friction the ideal speed is $v_0 = \sqrt{rg\tan\theta}$, and with friction the safe speed rises to $\sqrt{rg(\mu_s + \tan\theta)/(1 - \mu_s\tan\theta)}$.
