---
concept_id: friction
interest: motorsport
format: explain
title: Why braking harder can make you stop later
check:
  question: |-
    A driver brakes so hard that the wheels lock and the car skids. Compared with braking just hard enough to stay on the point of locking, with the wheels still turning, the skidding car:
  options:
    A: |-
      stops in a shorter distance, because pressing the pedal harder always gives more braking force
    B: |-
      stops in a longer distance, because kinetic friction is smaller than the limiting static friction
    C: |-
      stops in the same distance, because friction depends only on the car's weight, which has not changed
    D: |-
      stops in a longer distance, because the brakes stop working altogether once the wheels lock
  answer: B
  explanation: |-
    A rolling tyre grips through static friction, with a limit $\mu_s N$. Once the wheels lock the rubber slides, so the smaller kinetic friction $\mu_k N$ applies, the deceleration drops and the car travels further.
  misconceptions:
    A: |-
      Thinks the stopping force is set by the pedal. Beyond the locking point the limit is the grip at the road, not how hard the brakes squeeze.
    C: |-
      Remembers $f = \mu N$ but treats $\mu$ as fixed. The normal force is unchanged, but the *coefficient* changes from $\mu_s$ to the smaller $\mu_k$ the moment sliding begins.
    D: |-
      Reaches the right answer for the wrong reason. The brakes go on working perfectly — they are holding the wheel still. What has run out is grip between tyre and road.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A race car in a braking zone with glowing brake discs, a skid mark and tyre smoke, a tyre barrier along the wall and a marshal with a yellow flag](scenes/motorsport/laws_of_motion.svg "The dark line on the track is a locked tyre sliding. It is not the fastest way to stop.")

The driving school's skid pan is a square of polished, wet concrete behind an industrial estate, and Meenakshi has been looking forward to it all week. Zubair sir has one exercise for her: come at the cone at a fixed speed and stop as short as you possibly can.

First attempt, she stands on the pedal with everything she has. The wheels lock, the car slides with a long squeal, the steering goes dead in her hands, and she finishes well past the cone.

Second attempt, he tells her to brake hard but ease off the instant she feels the wheels about to lock. It feels almost timid. The car stops noticeably shorter — and she can still steer it.

Rehan, waiting his turn on the fence, says what everyone is thinking. "Pressing harder has to stop you sooner. How can doing less work better?"

## The physics

**Friction** is the force that opposes sliding, or attempted sliding, between two surfaces in contact. It acts along the surfaces, and it exists because even polished surfaces touch only at tiny high points, where the materials cling.

**Static friction** acts when the surfaces are *not* sliding but something is trying to make them. It is self-adjusting: it grows to match whatever is applied, up to a maximum called the **limiting friction**:

$$f_s \le \mu_s N$$

where $N$ is the normal force and $\mu_s$ the **coefficient of static friction**.

**Kinetic friction** takes over once the surfaces slide, and is roughly constant over ordinary speeds:

$$f_k = \mu_k N$$

For almost every pair of surfaces, $\mu_k < \mu_s$.

![Graph of friction against the horizontal push on a resting body: friction rises along a straight line equal to the push until it reaches its limit, then drops abruptly to a smaller constant value once sliding starts](figures/friction/friction-vs-push.svg "Static friction matches the push exactly, right up to the limit. Past that, the body slides and friction falls to the smaller kinetic value — the step down is the whole story of a locked wheel. The numbers are for a small box; the shape is general.")

Here is the part that answers Meenakshi. A wheel that is **rolling** has a contact patch that is momentarily at rest against the road — it is not sliding — so the grip available is **static** friction, with the larger limit $\mu_s N$. That is also why **rolling friction**, the small resistance of a rolling wheel, is so much less than sliding friction: nothing is scraping. The moment the wheel locks, the rubber genuinely slides on the tarmac, and the car has to make do with the smaller $\mu_k N$. Braking harder past the locking point therefore *loses* you grip. It costs steering too, because a sliding tyre cannot push sideways either.

**Lubrication** reduces friction where sliding is unavoidable — in the engine, the gearbox and the wheel bearings — by putting a thin fluid layer between the surfaces so the high points never touch. Ball bearings go further still, replacing sliding with rolling.

## Worked example

**Given:** car plus driver $m = 1000\,\text{kg}$ on a level road; $\mu_s = 0.80$ and $\mu_k = 0.60$ for these tyres on dry tarmac (illustrative); braking from $v = 20\,\text{m/s}$; $g = 9.8\,\text{m/s}^2$.
**Find:** the deceleration and stopping distance, wheels rolling at the grip limit and wheels locked.

*Normal force.* The road is level and nothing accelerates vertically, so $N = mg = 1000 \times 9.8 = 9800\,\text{N}$.

*Wheels rolling, at the limit.* $f = \mu_s N = 0.80 \times 9800 = 7840\,\text{N}$, so

$$a = \frac{f}{m} = \frac{7840}{1000} = 7.84\,\text{m/s}^2$$

Notice $a = \mu_s g$: the mass cancels, so a loaded car and an empty one stop in the same distance.

*Wheels locked.* $f_k = \mu_k N = 0.60 \times 9800 = 5880\,\text{N}$, giving $a = 5.88\,\text{m/s}^2$.

*Distances,* from $v^2 = 2ad$:

$$d_\text{rolling} = \frac{20^2}{2 \times 7.84} \approx 26\,\text{m} \qquad d_\text{locked} = \frac{20^2}{2 \times 5.88} \approx 34\,\text{m}$$

**Sanity check:** locking the wheels costs about eight metres, roughly two car lengths — which is exactly the gap between stopping at the cone and sliding past it.

## Where the picture breaks

$f_s \le \mu_s N$ and $f_k = \mu_k N$ are **empirical** approximations, not exact laws. Real coefficients change with water, dust, temperature and wear, and a wet skid pan has far lower values than the dry tarmac above. Tyres in particular bend the rule: grip really does depend on how wide the contact patch is and how warm the rubber is, which is why racing tyres are broad and are deliberately heated. The sharp step in the graph is idealised too — a tyre at its very best is neither purely rolling nor fully sliding but slipping slightly, which is past this course. Anti-lock brakes simply release and reapply the brakes many times a second to hold the tyre just below that step.

## Key takeaway

Static friction rises to match whatever tries to slide a body, up to its limit $\mu_s N$; beyond that the body slides and the smaller kinetic friction $\mu_k N$ takes over. A rolling wheel grips through static friction, so locking the wheels swaps the larger coefficient for the smaller one and lengthens the stop. Rolling friction is far smaller than sliding friction, and lubrication cuts friction by keeping sliding surfaces apart.
