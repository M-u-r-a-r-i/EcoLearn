---
concept_id: friction
interest: cricket
format: explain
title: Why the pitch roller moves more easily than the kit trunk
check:
  question: |-
    A groundsman pushes horizontally with $200\,\text{N}$ on a $50\,\text{kg}$ trunk resting on a level floor. For trunk and floor, $\mu_s = 0.45$ and $\mu_k = 0.35$; take $g = 9.8\,\text{m/s}^2$. What happens?
  options:
    A: |-
      It slides, and the friction on it is $171.5\,\text{N}$
    B: |-
      It stays at rest, and the friction on it is $220.5\,\text{N}$
    C: |-
      It stays at rest, and the friction on it is $200\,\text{N}$
    D: |-
      It stays at rest, and there is no friction because nothing is moving
  answer: C
  explanation: |-
    The limiting static friction is $\mu_s N = 0.45 \times 490 = 220.5\,\text{N}$. The push of $200\,\text{N}$ is below this, so the trunk stays put, and static friction adjusts to exactly balance the push: $200\,\text{N}$.
  misconceptions:
    A: |-
      Compares the push with kinetic friction ($\mu_k N = 171.5\,\text{N}$) to decide whether sliding starts. To start sliding you must beat the larger, static limit $\mu_s N$.
    B: |-
      Thinks static friction always equals $\mu_s N$. That is only its maximum; below the limit it matches the applied force.
    D: |-
      Thinks friction appears only once things move. Static friction acts on a body at rest whenever something tries to slide it.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A batter drives the ball back past the bowler in a floodlit stadium](scenes/cricket/laws_of_motion.svg "Before the lights go on, the groundstaff have spent all day fighting friction, and using it.")

It's the morning before a club final, and Riya has volunteered to help Mahesh bhai, the head groundsman. Her first job is to move the old kit trunk out of the store. She leans into it with everything she has. Nothing. She pushes harder, and suddenly it lurches forward — and then, strangely, it's easier to keep it sliding than it was to get it going.

Her second job is the hand roller for the pitch, a steel drum several times heavier than the trunk. She expects it to be impossible. Instead, after a firm push, it trundles along almost happily.

"Why is the heaviest thing here the easiest to move?" she asks.

Mahesh bhai squeezes a blob of grease into the roller's axle and grins. "And why do you think I do this every week?"

## The physics

**Friction** is the force that opposes relative sliding (or attempted sliding) between two surfaces in contact. It acts along the surfaces. It arises because even smooth-looking surfaces touch only at tiny bumps, where the materials cling to each other.

There are three kinds you need:

**Static friction** acts when the surfaces are *not* sliding but something is trying to make them. It is self-adjusting: it grows to match the push, up to a maximum, the **limiting friction**:

$$f_s \le \mu_s N$$

where $N$ is the normal force and $\mu_s$ the **coefficient of static friction**. When Riya's push was small, static friction matched it exactly and the trunk stayed still.

**Kinetic friction** acts once the surfaces slide. It is roughly constant, independent of speed over ordinary ranges:

$$f_k = \mu_k N$$

For most pairs of surfaces, $\mu_k < \mu_s$, which is why the trunk was easier to keep moving than to start.

**The rule for "does it slide?":** compare the applied force with the limiting friction $\mu_s N$. Below it, no sliding and $f_s$ equals the applied force. Above it, sliding starts and friction drops to $\mu_k N$.

![Graph of friction against horizontal push for a 40 kg trunk: friction rises in a straight line equal to the push up to 196 N, then drops to a constant 157 N once the trunk slides](figures/friction/friction-vs-push.svg "Static friction matches the push until it hits its limit, 196 N here. Then the trunk slides and friction falls to the smaller kinetic value.")

**Rolling friction** acts when a body rolls rather than slides — a wheel, a roller, a ball rolling across the outfield. The contact point doesn't slide, and the resistance comes mainly from the slight squashing of the surfaces. For the same load, rolling friction is much smaller than sliding friction. That is why the roller moves more easily than the trunk despite its greater weight.

**Lubrication.** The roller turns on an axle, and at the axle, metal *slides* on metal. Grease or oil puts a thin fluid layer between the surfaces so the bumps don't touch directly, and the friction there drops sharply. Ball bearings go further, replacing sliding at the axle with rolling.

## Worked example

**Given:** trunk $m = 40\,\text{kg}$ on a level floor; $\mu_s = 0.50$, $\mu_k = 0.40$ (illustrative values); $g = 9.8\,\text{m/s}^2$.
**Find:** what happens with a horizontal push of (a) $150\,\text{N}$ and (b) $200\,\text{N}$.

The floor is level and nothing moves vertically, so $N = mg = 40 \times 9.8 = 392\,\text{N}$.

Limiting static friction: $\mu_s N = 0.50 \times 392 = 196\,\text{N}$.

(a) $150\,\text{N} < 196\,\text{N}$: no sliding. Static friction is $150\,\text{N}$, opposite to the push; net force zero.

(b) $200\,\text{N} > 196\,\text{N}$: the trunk slides. Now friction is kinetic: $f_k = 0.40 \times 392 = 156.8\,\text{N}$.

$$a = \frac{F - f_k}{m} = \frac{200 - 156.8}{40} = \frac{43.2}{40} \approx 1.1\,\text{m/s}^2$$

**Sanity check:** in (b), friction ($157\,\text{N}$) is less than the push, so the trunk speeds up, as it should; if Riya eased off to exactly $157\,\text{N}$ once it was sliding, it would keep going at constant velocity.

## Where the picture breaks

The laws $f_s \le \mu_s N$ and $f_k = \mu_k N$ are **empirical** approximations, not exact laws of nature. Real values of $\mu$ vary with dust, moisture and wear; a dewy outfield or a damp store floor changes them. Kinetic friction isn't perfectly constant with speed either. And the "sudden drop" on the graph is idealised; in reality the change from sticking to sliding can be jerky. The roller's ease also depends on its size and on how firm the ground is — rolling on soft turf is harder than on concrete.

## Key takeaway

Static friction matches any push up to its limit $\mu_s N$; a body slides only when the applied force exceeds that limit, and then kinetic friction $\mu_k N$ (usually smaller) takes over. Rolling friction is far smaller than sliding friction, and lubrication reduces friction by separating the sliding surfaces with a fluid layer.
