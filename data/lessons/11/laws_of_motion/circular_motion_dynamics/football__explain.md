---
concept_id: circular_motion_dynamics
interest: football
format: explain
title: What turns a winger on a curved run
check:
  question: |-
    A $60\,\text{kg}$ player runs round a curve of radius $4.0\,\text{m}$ at a steady $5.0\,\text{m/s}$ on level grass. What horizontal force keeps her on the curve, and what supplies it?
  options:
    A: |-
      $375\,\text{N}$, from static friction of the grass on her boots, directed towards the centre
    B: |-
      $375\,\text{N}$, from an outward centrifugal force that balances her running
    C: |-
      $1500\,\text{N}$, from static friction of the grass on her boots, directed towards the centre
    D: |-
      $75\,\text{N}$, from static friction of the grass on her boots, directed towards the centre
  answer: A
  explanation: |-
    The centripetal force needed is $mv^2/r = 60 \times 5.0^2 / 4.0 = 375\,\text{N}$ towards the centre. On level grass the only horizontal force from outside is friction on her boots, and since they don't slip, it is static friction.
  misconceptions:
    B: |-
      Adds an outward "centrifugal force" to the forces on the runner as seen from the ground. In that frame there is no outward force: her body tends to go straight on, and friction pulls her inward.
    C: |-
      Forgets to divide by the radius, using $mv^2$. The centripetal force is $mv^2/r$; a wider curve needs less force.
    D: |-
      Uses $mv/r$, forgetting to square the speed. Doubling the speed needs four times the force, because the force goes as $v^2$.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![Under floodlights, a striker follows through after a shot while the ball flies towards the goalkeeper](scenes/football/laws_of_motion.svg "Players rarely run in straight lines. Every bent run needs a force towards the inside of the curve.")

Late in a wet evening match, Vikram, the club's fastest winger, tries his favourite move: a tight curved run around the full-back to get onto a through ball. On dry grass it always works. This time his boots go from under him halfway round the bend, and he slides off almost in a straight line, straight out of play.

Driving home, his cousin Salma takes the ring-road flyover. The curve is long and tight, and Vikram notices the road isn't flat: its outer edge is clearly higher than its inner edge. Salma keeps to a steady speed and the car sweeps round without drama.

"Why do I fall over on a bend and your car doesn't?" Vikram asks, still annoyed. "And why build a road on a slope? Wouldn't flat be safer?"

Salma shrugs. "Something must be turning both of us. What is it?"

## The physics

A body moving in a circle of radius $r$ at speed $v$ has a **centripetal acceleration** $v^2/r$ towards the centre. By Newton's second law, that needs a net force towards the centre:

$$F_\text{c} = \frac{mv^2}{r}$$

The **centripetal force** is not a new kind of force. It is the name for whichever real forces add up to point towards the centre. The job in every problem is to **identify what supplies it**.

**A runner, or a car, on level ground.** Weight and the normal force are vertical and cancel. The only horizontal force is **friction** from the ground. The boots or tyres do not slip sideways, so it is **static** friction, pointing towards the centre. It cannot exceed $\mu_s N = \mu_s mg$, so the curve can be taken only if

$$\frac{mv^2}{r} \le \mu_s mg \quad\Rightarrow\quad v_\text{max} = \sqrt{\mu_s r g}$$

On the wet grass, $\mu_s$ dropped. At his usual speed on his usual curve, Vikram needed more inward force than the grass could give, so his boots slid and his body carried on almost straight, by inertia.

**A banked road.** Tilting the road at an angle $\theta$ tilts the normal force towards the centre, so part of $N$ supplies the centripetal force too. With no friction at all, there is one speed at which the normal force does the whole job:

$$\tan\theta = \frac{v_0^2}{rg} \quad\Rightarrow\quad v_0 = \sqrt{rg\tan\theta}$$

Above that speed, friction acts down the slope as well, up to its limit. Resolving the forces horizontally and vertically gives the maximum safe speed:

$$v_\text{max} = \sqrt{rg\,\frac{\mu_s + \tan\theta}{1 - \mu_s\tan\theta}}$$

![Left: cross-section of a road banked at angle theta, higher on the outside, with a vehicle on it. Right: free-body diagram at maximum speed with the normal force perpendicular to the road tilted towards the centre, weight straight down, and friction down the slope, plus a horizontal acceleration arrow towards the centre](figures/circular_motion_dynamics/banked-road-forces.svg "On the banked flyover, both the normal force and friction have parts pointing towards the centre, so together they supply more centripetal force than friction alone.")

## Worked example

**Given:** (a) Vikram's curve, radius $r = 5.0\,\text{m}$, dry grass with $\mu_s = 0.70$; (b) the flyover, radius $r = 80\,\text{m}$, $\mu_s = 0.40$ between tyres and road, banked at $12^\circ$ (illustrative values); $g = 9.8\,\text{m/s}^2$.
**Find:** (a) Vikram's top speed on the curve; (b) the car's maximum safe speed if the road were level, and as banked; (c) the banked road's no-friction speed.

(a) $v_\text{max} = \sqrt{0.70 \times 5.0 \times 9.8} = \sqrt{34.3} \approx 5.9\,\text{m/s}$.

(b) Level: $v_\text{max} = \sqrt{0.40 \times 80 \times 9.8} = \sqrt{313.6} \approx 17.7\,\text{m/s} \approx 64\,\text{km/h}$.

Banked, with $\tan 12^\circ = 0.213$ and $rg = 784\,\text{m}^2/\text{s}^2$:

$$v_\text{max} = \sqrt{784 \times \frac{0.40 + 0.213}{1 - 0.40 \times 0.213}} = \sqrt{784 \times \frac{0.613}{0.915}} = \sqrt{525} \approx 22.9\,\text{m/s} \approx 82\,\text{km/h}$$

(c) $v_0 = \sqrt{784 \times 0.213} = \sqrt{167} \approx 12.9\,\text{m/s} \approx 46\,\text{km/h}$.

Banking lifts the safe speed from about $64$ to about $82\,\text{km/h}$ on the same surface.

**Sanity check:** units: $\sqrt{\text{m} \times \text{m/s}^2} = \text{m/s}$ ✓. With $\theta = 0$ the banked formula reduces to $\sqrt{\mu_s r g}$ ✓; with $\mu_s = 0$ it reduces to $\sqrt{rg\tan\theta}$ ✓. And if wet grass halved Vikram's $\mu_s$ to $0.35$, his top speed would fall by a factor $\sqrt{2}$, to about $4.1\,\text{m/s}$.

## Where the picture breaks

A runner is not a car: Vikram also leans into the bend and pushes sideways with his studs, which dig into the turf, so "surface friction" is only part of his grip, and his lean involves rotation, which you'll meet later. We treated the car as a point; a real vehicle can also topple on a tight curve. The formulas give the speed with friction at its absolute limit and no safety margin, so real speed limits are set well below them. And the outward lurch passengers feel is not an outward force on them, seen from the road; it is their inertia, with the seat pushing them round.

## Key takeaway

Circular motion needs a net force $mv^2/r$ towards the centre, supplied by real forces. On level ground it comes from static friction, so $v_\text{max} = \sqrt{\mu_s r g}$. Banking a road tilts the normal force inwards so it helps: with no friction the ideal speed is $v_0 = \sqrt{rg\tan\theta}$, and with friction the safe speed rises to $\sqrt{rg(\mu_s + \tan\theta)/(1 - \mu_s\tan\theta)}$.
