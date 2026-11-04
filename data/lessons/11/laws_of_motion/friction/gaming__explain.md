---
concept_id: friction
interest: gaming
format: explain
title: Moving the gaming desk and the two friction numbers
check:
  question: |-
    A $25\,\text{kg}$ PC cabinet rests on a level floor, with $\mu_s = 0.50$ and $\mu_k = 0.40$ between them. You push it horizontally with $130\,\text{N}$. Taking $g = 9.8\,\text{m/s}^2$, what is its acceleration?
  options:
    A: |-
      $0.30\,\text{m/s}^2$
    B: |-
      $0\,\text{m/s}^2$
    C: |-
      $1.28\,\text{m/s}^2$
    D: |-
      $5.2\,\text{m/s}^2$
  answer: C
  explanation: |-
    $N = mg = 245\,\text{N}$, so the static limit is $\mu_s N = 122.5\,\text{N}$. The $130\,\text{N}$ push exceeds it, so the cabinet slides and kinetic friction $\mu_k N = 98\,\text{N}$ acts: $a = \dfrac{130 - 98}{25} = 1.28\,\text{m/s}^2$.
  misconceptions:
    A: |-
      Keeps using the static limit $\mu_s N$ once the cabinet is sliding. After sliding starts, friction drops to the kinetic value $\mu_k N$.
    B: |-
      Thinks the push must exceed the cabinet's weight ($245\,\text{N}$) to move it. A horizontal push only has to beat the limiting friction, $\mu_s N$, not the weight.
    D: |-
      Ignores friction and divides the push by the mass. The net force is the push minus kinetic friction.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A gaming desk at night: a racing game on the monitor and a zero-gravity game on a tablet](scenes/gaming/laws_of_motion.svg "The kart's grip on the track is friction too. Tonight, though, the friction problem is the furniture.")

Aarav's new monitor arm has arrived, and his whole setup has to move to the other wall. First, the heavy wooden desk, its drawers full of cables. He leans into it. Nothing. He pushes harder, and harder, and suddenly it jerks forward. Strangely, once it's moving, it takes much less effort to keep it going than it did to start.

His cousin Ritika rolls in a furniture dolly, a flat board on four castors. They lift the desk onto it, and now Aarav can push the desk across the room with one hand. One castor squeaks badly; Ritika puts a drop of oil on its axle and the squeak stops.

Later, back at his screen, Aarav opens the game engine he has been learning. Every surface material in it asks for two friction numbers, one labelled *static* and one *dynamic*.

"Why two?" he asks. "Friction is friction."

Is it?

## The physics

**Friction** is the force that opposes relative sliding, or attempted sliding, between two surfaces in contact. It acts along the surfaces. It arises because even smooth-looking surfaces touch only at tiny bumps, where the materials cling together.

**Static friction** acts when the surfaces are *not* sliding but something is trying to make them. It adjusts itself to match the push, up to a maximum called **limiting friction**:

$$f_s \le \mu_s N$$

where $N$ is the normal force and $\mu_s$ the **coefficient of static friction**. When Aarav's push was small, static friction matched it exactly, so the desk didn't move.

**Kinetic friction** acts once the surfaces slide. It is roughly constant over ordinary speeds:

$$f_k = \mu_k N$$

For most pairs of surfaces $\mu_k < \mu_s$, so it is easier to keep a body sliding than to start it. That is why the desk jerked forward: the moment it broke free, the friction dropped. It is also why the game engine asks for two numbers: *dynamic* is the engine's word for kinetic.

**Deciding whether a body slides:** compare the applied force with $\mu_s N$. Below it, no sliding, and static friction equals the applied force. Above it, the body slides and friction becomes $\mu_k N$.

![Graph of friction against horizontal push for a 40 kg trunk: friction rises in a straight line equal to the push up to 196 N, then drops to a constant 157 N once the trunk slides](figures/friction/friction-vs-push.svg "Drawn for a 40 kg load, but it is Aarav's desk exactly: friction matches the push up to the static limit, then falls to the smaller kinetic value the moment sliding starts.")

**Rolling friction** acts when a body rolls: a wheel, a castor, a ball. The contact point doesn't slide; the resistance comes mainly from the slight squashing of the surfaces. For the same load it is far smaller than sliding friction, which is why the dolly made the heavy desk easy.

**Lubrication.** At each castor's axle, metal *slides* on metal. Oil puts a thin fluid layer between the surfaces so their bumps don't touch directly, and friction there falls sharply. Ball bearings go further, replacing sliding with rolling.

## Worked example

**Given (illustrative values):** desk $m = 60\,\text{kg}$ on a level floor; $\mu_s = 0.40$, $\mu_k = 0.30$; $g = 9.8\,\text{m/s}^2$.
**Find:** what happens with a horizontal push of (a) $200\,\text{N}$ and (b) $250\,\text{N}$.

The floor is level and nothing moves vertically, so $N = mg = 60 \times 9.8 = 588\,\text{N}$.

Limiting static friction: $\mu_s N = 0.40 \times 588 \approx 235\,\text{N}$.

(a) $200\,\text{N} < 235\,\text{N}$: no sliding. Static friction is $200\,\text{N}$, opposite to the push; the net force is zero.

(b) $250\,\text{N} > 235\,\text{N}$: the desk slides, and friction is kinetic, $f_k = 0.30 \times 588 = 176.4\,\text{N}$.

$$a = \frac{F - f_k}{m} = \frac{250 - 176.4}{60} = \frac{73.6}{60} \approx 1.2\,\text{m/s}^2$$

**Sanity check:** in (b) friction is less than the push, so the desk speeds up, as it should. If Aarav eased off to $176\,\text{N}$ once it was sliding, it would move at constant velocity; that easing off is exactly the "easier to keep going" he felt.

## Where the picture breaks

$f_s \le \mu_s N$ and $f_k = \mu_k N$ are **empirical** rules, good approximations rather than exact laws. Real coefficients change with dust, moisture and wear, and kinetic friction varies a little with speed. The sharp drop on the graph is idealised; real starts can be jerky, which is partly why furniture judders. A game engine's two numbers are a simplified model of the same thing, and designers often pick them for feel rather than realism.

## Key takeaway

Static friction matches any push up to its limit $\mu_s N$; a body slides only when the applied force exceeds that limit, and then kinetic friction $\mu_k N$, usually smaller, takes over. Rolling friction is much smaller than sliding friction, and lubrication cuts friction by keeping the sliding surfaces apart with a fluid layer.
