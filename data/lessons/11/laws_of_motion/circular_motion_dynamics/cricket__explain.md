---
concept_id: circular_motion_dynamics
interest: cricket
format: explain
title: How the team bus stays on the curve to the stadium
check:
  question: |-
    The team bus goes round a level, unbanked curve at a steady speed. Which force supplies the centripetal force that keeps it on the curve?
  options:
    A: |-
      The forward push from the engine, acting through the wheels
    B: |-
      An outward centrifugal force, which balances the bus's weight on the curve
    C: |-
      The weight of the bus, pulling it towards the centre of the curve
    D: |-
      Static friction from the road on the tyres, directed towards the centre of the curve
  answer: D
  explanation: |-
    On a level road the only horizontal force that can point towards the centre is friction between road and tyres. The tyres don't slide sideways, so it is static friction, and it must equal $mv^2/r$.
  misconceptions:
    A: |-
      Confuses the force that keeps the bus moving forward with the force that turns it. The engine's drive acts along the direction of motion; turning needs a sideways force towards the centre.
    B: |-
      Adds a "centrifugal force" to the forces on the bus as seen from the road. In that frame there is no outward force: the bus tends to go straight on (inertia) and friction pulls it inward.
    C: |-
      Weight acts straight down. On a level road it has no component towards the centre, and it is balanced by the normal force.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A batter drives the ball back past the bowler in a floodlit stadium](scenes/cricket/laws_of_motion.svg "The match is at the end of the journey. The physics starts on the road there.")

The team bus to the away final swings off the highway onto a long, curving flyover ramp. Aditi, the vice-captain, has a window seat, and she notices two things. The road surface isn't flat: it is visibly tilted, the outer edge higher than the inner. And everyone in the bus leans towards the outside of the curve, bags sliding across the seats.

Behind her, Harsh is still grumbling about yesterday's practice. Chasing a ball around the boundary on wet grass, he tried to curve his run towards it, his feet went from under him, and he slid off in almost a straight line.

"Same thing," says Aditi. "You needed something to turn you, and the grass didn't give it."

"Then what's turning this bus?" Harsh asks. "And why would anyone build a road on a slant?"

## The physics

A body moving in a circle of radius $r$ at speed $v$ has a **centripetal acceleration** $v^2/r$ towards the centre. By Newton's second law, that needs a net force towards the centre:

$$F_\text{c} = \frac{mv^2}{r}$$

The **centripetal force** is not a new kind of force. It is the name for whichever real forces add up to point towards the centre. The job in every problem is to **identify what supplies it**.

**Level road.** Weight and the normal force are vertical and cancel. The only horizontal force is **friction** from the road on the tyres. The tyres roll without slipping sideways, so this is **static** friction, and it points towards the centre. It has a maximum value $\mu_s N = \mu_s mg$, so the curve can be taken only if

$$\frac{mv^2}{r} \le \mu_s mg \quad\Rightarrow\quad v_\text{max} = \sqrt{\mu_s r g}$$

Harsh on wet grass is the same story: the grass's $\mu_s$ was too small to supply $mv^2/r$, so his feet slid and he carried on almost straight, by inertia. The passengers lean outwards for the same reason: their bodies tend to go straight on, and the seats have to push them round.

**Banked road.** Tilting the road at an angle $\theta$ tilts the normal force towards the centre, so part of $N$ helps supply the centripetal force. With no friction at all, there is exactly one speed at which the normal force does the whole job:

$$\tan\theta = \frac{v_0^2}{rg} \quad\Rightarrow\quad v_0 = \sqrt{rg\tan\theta}$$

At higher speeds friction also acts, down the slope, until it reaches its limit. Resolving the forces horizontally and vertically then gives the maximum safe speed:

$$v_\text{max} = \sqrt{rg\,\frac{\mu_s + \tan\theta}{1 - \mu_s\tan\theta}}$$

![Left: cross-section of a road banked at angle theta, higher on the outside, with a vehicle on it. Right: free-body diagram at maximum speed with the normal force perpendicular to the road tilted towards the centre, weight straight down, and friction down the slope, plus a horizontal acceleration arrow towards the centre](figures/circular_motion_dynamics/banked-road-forces.svg "On a banked road both the normal force and friction have parts pointing towards the centre, so together they can supply more centripetal force than friction alone.")

## Worked example

**Given:** a curve of radius $r = 100\,\text{m}$, with $\mu_s = 0.30$ between tyres and road (illustrative values); $g = 9.8\,\text{m/s}^2$.
**Find:** the maximum safe speed if the road is (a) level, (b) banked at $10^\circ$; and (c) the speed at which the banked road needs no friction.

(a) Level road:

$$v_\text{max} = \sqrt{0.30 \times 100 \times 9.8} = \sqrt{294} \approx 17.1\,\text{m/s} \approx 62\,\text{km/h}$$

(b) Banked at $10^\circ$, with $\tan 10^\circ = 0.176$:

$$v_\text{max} = \sqrt{980 \times \frac{0.30 + 0.176}{1 - 0.30 \times 0.176}} = \sqrt{980 \times \frac{0.476}{0.947}} = \sqrt{492.6} \approx 22.2\,\text{m/s} \approx 80\,\text{km/h}$$

(c) No friction needed:

$$v_0 = \sqrt{980 \times 0.176} = \sqrt{172.5} \approx 13.1\,\text{m/s} \approx 47\,\text{km/h}$$

Banking raised the safe speed from about $62$ to about $80\,\text{km/h}$ on the same road surface.

**Sanity check:** units: $\sqrt{\text{m} \times \text{m/s}^2} = \text{m/s}$ ✓. Limiting cases: with $\theta = 0$, the banked formula becomes $\sqrt{\mu_s r g}$, the level-road result ✓; with $\mu_s = 0$, it becomes $\sqrt{rg\tan\theta}$, the no-friction speed ✓.

## Where the picture breaks

We treated the bus as a point. A real bus is tall, so on a sharp curve it can **topple** outwards before it skids; that depends on its height and width, which needs rotational ideas you'll meet later. Real roads have $\mu_s$ that drops sharply in rain, and the maximum-speed formula assumes friction is at its absolute limit, with no margin, so real speed limits are set well below it. And the "outward lean" passengers feel is not an outward force on them from the road's point of view: it is their inertia, with the seat supplying the inward push.

## Key takeaway

Circular motion needs a net force $mv^2/r$ towards the centre, supplied by real forces. On a level road it comes from static friction, so $v_\text{max} = \sqrt{\mu_s r g}$. Banking the road tilts the normal force inwards so it helps: with no friction the ideal speed is $v_0 = \sqrt{rg\tan\theta}$, and with friction the safe speed rises to $\sqrt{rg(\mu_s + \tan\theta)/(1 - \mu_s\tan\theta)}$.
