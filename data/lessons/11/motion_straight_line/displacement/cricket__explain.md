---
concept_id: displacement
interest: cricket
format: explain
title: Nineteen metres of running, out by one
check:
  question: |-
    Take the origin at the striker's crease and the positive direction towards the bowler. For the spinner's over the wicketkeeper stands up close at $x = -1.0\,\text{m}$. For the fast bowler's next over she moves back to $x = -16.0\,\text{m}$. What is her displacement?
  options:
    A: |-
      $-15.0\,\text{m}$
    B: |-
      $+15.0\,\text{m}$
    C: |-
      $-17.0\,\text{m}$
    D: |-
      $-16.0\,\text{m}$
  answer: A
  explanation: |-
    Displacement is final position minus initial position: $\Delta x = (-16.0) - (-1.0) = -15.0\,\text{m}$. She moved $15\,\text{m}$ in the negative direction, away from the bowler.
  misconceptions:
    B: |-
      Subtracts the wrong way round (initial minus final), or drops the sign because "displacement is how far she moved". The sign carries the direction and must come from final minus initial.
    C: |-
      Adds the two positions instead of subtracting them, treating displacement like a total of the numbers on the scale.
    D: |-
      Gives her final position as the displacement. Position says where she is measured from the origin; displacement says how her position changed.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A cricket ground in sunshine: a batter runs between the wickets on a 22-yard pitch while a fielder chases the ball towards the boundary rope](scenes/cricket/motion_straight_line.svg "Along the pitch, every movement is either towards the bowler or away from him.")

Tanvi pushes the ball to cover and bolts. Ten metres down the pitch she hears "NO!" — the fielder has swooped. She plants her foot, turns, and sprints back, bat stretched out in front of her. The throw hits the stumps. The bails fly.

The third umpire's replay is agonising: Tanvi's bat is about one metre short of the crease when the bails come off. Out.

Afterwards, her friend Aditya tries to cheer her up. "You ran nineteen metres in about four seconds. That's a lot of effort."

"Effort doesn't matter," Tanvi says. "The only number anyone will remember is that one metre."

She has a point. Nineteen metres of running, but the question the umpire asked had nothing to do with how far she'd run. It was about where she ended up compared with where she needed to be.

Which quantity captures that — and why does it need a direction, not just a size?

## The physics

**Displacement** is the change in position. In one dimension, if an object starts at position $x_i$ and ends at $x_f$:

$$\Delta x = x_f - x_i$$

It is a **vector**: it has a size and a direction. Along a line, the direction is carried by the **sign**: $+$ means the object ended up further along the positive direction, $-$ means it ended up further along the negative direction.

Three properties follow from the definition:

- It depends only on the **start and the end**, not on the path in between.
- Its size is never larger than the distance travelled — equal if the path never turns back, smaller if it does.
- A round trip gives $\Delta x = 0$, however far you ran.

![Three trips on a line: from 1 m to 5 m gives Δx = +4 m; from 5 m to 2 m gives Δx = −3 m; out 3 m and back gives Δx = 0 m although the distance is 6 m](figures/displacement/sign-in-one-dimension.svg "Displacement is final minus initial. The arrow's direction gives the sign; a round trip gives zero whatever the distance.")

For Tanvi, put the origin at her starting crease with positive towards the bowler. She started at $x_i = 0$ and was caught at $x_f = +1\,\text{m}$ (one metre short, on the pitch side). So $\Delta x = +1\,\text{m}$, while the distance she covered was $10 + 9 = 19\,\text{m}$. The umpire's question — is the bat behind the crease? — is a question about position and displacement, not distance.

## Worked example

**Given:** origin at the striker's crease, positive towards the bowler. For a spinner the keeper stands close, at $x = -0.5\,\text{m}$; for a fast bowler she stands back at $x = -15.0\,\text{m}$ (illustrative).
**Find:** her displacement (a) when she moves back for the fast bowler, and (b) when she comes up again for the spinner.

(a) $x_i = -0.5\,\text{m}$, $x_f = -15.0\,\text{m}$:

$$\Delta x = (-15.0) - (-0.5) = -14.5\,\text{m}$$

The minus sign says she moved away from the bowler.

(b) $x_i = -15.0\,\text{m}$, $x_f = -0.5\,\text{m}$:

$$\Delta x = (-0.5) - (-15.0) = +14.5\,\text{m}$$

Over both moves together, $\Delta x = -14.5 + 14.5 = 0$, while the distance is $29.0\,\text{m}$.

**Sanity check:** both answers have size $14.5\,\text{m}$, the gap between the two spots, and opposite signs for opposite directions. Reversing a trip should flip the sign of the displacement and nothing else — and it does.

## Where the picture breaks

We have squashed everything onto the line of the pitch. Tanvi's bat also moved sideways and down to the ground, so her full displacement is a vector in three dimensions; only its component along the pitch decided the run-out. In real run-outs the question is also *when* — the bat must be grounded behind the crease at the instant the wicket is broken — which makes it a question about position at a moment in time. And the sign convention is a choice: had we taken positive towards the striker, every sign here would flip, but the physical movement would be the same.

## Key takeaway

Displacement is the change in position, $\Delta x = x_f - x_i$: a vector that points from where you started to where you finished, with its direction shown by the sign in one dimension. It ignores the path, so a round trip gives zero — and nineteen metres of running can end in a displacement of just one metre.
