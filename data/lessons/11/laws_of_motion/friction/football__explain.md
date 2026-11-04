---
concept_id: friction
interest: football
format: explain
title: Why the sprint sled sticks but the ball rolls on
check:
  question: |-
    A player pulls horizontally with $100\,\text{N}$ on a $25\,\text{kg}$ training sled resting on level turf. For sled and turf, $\mu_s = 0.50$ and $\mu_k = 0.40$; take $g = 9.8\,\text{m/s}^2$. What happens?
  options:
    A: |-
      It slides, and the friction on it is $98\,\text{N}$
    B: |-
      It stays at rest, and the friction on it is $122.5\,\text{N}$
    C: |-
      It stays at rest, and there is no friction because nothing is moving
    D: |-
      It stays at rest, and the friction on it is $100\,\text{N}$
  answer: D
  explanation: |-
    $N = mg = 245\,\text{N}$, so the limiting static friction is $\mu_s N = 0.50 \times 245 = 122.5\,\text{N}$. The $100\,\text{N}$ pull is below this, so the sled stays put, and static friction adjusts to balance the pull exactly: $100\,\text{N}$.
  misconceptions:
    A: |-
      Compares the pull with kinetic friction ($\mu_k N = 98\,\text{N}$) to decide whether sliding starts. To start a body sliding you must beat the larger static limit, $\mu_s N$.
    B: |-
      Thinks static friction always equals $\mu_s N$. That is only its maximum; below the limit, it is exactly as big as needed to stop sliding.
    C: |-
      Thinks friction appears only once things move. Static friction acts on a body at rest whenever something tries to slide it.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![Under floodlights, a striker follows through after a shot while the ball flies towards the goalkeeper](scenes/football/laws_of_motion.svg "Every sprint, turn and slide on this pitch depends on friction between boots, ball and grass.")

Pre-season fitness, and Anjali is harnessed to a weighted sprint sled on the club's grass pitch. When the whistle goes, she drives forward and nothing happens. The strap goes taut, her boots dig in, and the sled sits there. She leans in harder, and it suddenly breaks free and scrapes along behind her. Oddly, keeping it moving feels easier than getting it started.

Afterwards, her teammate Nikhil rolls a ball across the same grass with one gentle tap of his foot. It travels twenty metres. "Your sled weighs as much as seventy footballs," he says, "but I don't think that's the whole story. The ball rolls. The sled scrapes."

Then it starts to rain, and within minutes players are slipping over on the turns. The groundsman, Mr Iyer, is out oiling the squeaky wheels of the line-marking trolley.

Sticking, sliding, rolling, slipping, oiling: is there one idea behind all of it?

## The physics

**Friction** is the force that opposes relative sliding (or attempted sliding) between two surfaces in contact, and it acts along the surfaces. Even smooth-looking surfaces touch only at tiny high points, where they cling to each other.

**Static friction** acts when the surfaces are *not* sliding but something is trying to slide them. It adjusts itself to match the push, up to a maximum, the **limiting friction**:

$$f_s \le \mu_s N$$

where $N$ is the normal force and $\mu_s$ the **coefficient of static friction**. While Anjali's pull was below the limit, static friction matched it exactly and the sled stayed put.

**Kinetic friction** acts once the surfaces slide. It is roughly constant over ordinary speeds:

$$f_k = \mu_k N$$

For most surfaces $\mu_k < \mu_s$, which is why the sled was easier to keep moving than to start.

**Does it slide?** Compare the applied force with $\mu_s N$. Below it: no sliding, and static friction equals the applied force. Above it: the body slides, and friction drops to $\mu_k N$.

![Graph of friction against horizontal push for a 40 kg trunk: friction rises in a straight line equal to the push up to 196 N, then drops to a constant 157 N once the trunk slides](figures/friction/friction-vs-push.svg "Drawn for a 40 kg load, but the shape holds for any sled: friction matches the pull up to the static limit, then falls to the smaller kinetic value once sliding starts.")

**Rolling friction** acts when a body rolls rather than slides, like the ball on the grass. The contact point doesn't slide; the resistance comes mainly from the ball and turf squashing slightly. For the same load, rolling friction is far smaller than sliding friction.

Static friction is also what lets you run. Your studs push back on the grass without slipping, and static friction from the grass pushes you forward. Rain puts a film of water between boot and grass, which lowers $\mu_s$; on a sharp turn the grip needed exceeds the limit, and players slip.

**Lubrication.** At the line-marker's axle, metal slides on metal. Oil puts a thin fluid layer between the surfaces so their high points don't touch directly, and the friction there drops sharply. Ball bearings go further, replacing sliding at the axle with rolling.

## Worked example

**Given:** sled $m = 30\,\text{kg}$ on level turf; $\mu_s = 0.60$, $\mu_k = 0.45$ (illustrative values); $g = 9.8\,\text{m/s}^2$.
**Find:** what happens with a horizontal pull of (a) $150\,\text{N}$ and (b) $200\,\text{N}$.

Nothing moves vertically, so $N = mg = 30 \times 9.8 = 294\,\text{N}$.

Limiting static friction: $\mu_s N = 0.60 \times 294 = 176.4\,\text{N}$.

(a) $150\,\text{N} < 176.4\,\text{N}$: no sliding. Static friction is $150\,\text{N}$, backwards; the net force is zero.

(b) $200\,\text{N} > 176.4\,\text{N}$: the sled slides. Friction is now kinetic: $f_k = 0.45 \times 294 = 132.3\,\text{N}$.

$$a = \frac{F - f_k}{m} = \frac{200 - 132.3}{30} = \frac{67.7}{30} \approx 2.3\,\text{m/s}^2$$

**Sanity check:** in (b), friction ($132\,\text{N}$) is less than the pull, so the sled speeds up, as it should. If Anjali eased off to exactly $132\,\text{N}$ once it was moving, the sled would slide on at constant velocity.

## Where the picture breaks

$f_s \le \mu_s N$ and $f_k = \mu_k N$ are **empirical** rules, not exact laws. On real grass, $\mu$ changes with the length of the grass, dew, rain and how the turf has been cut, and a sled's runners dig in a little, which is more than simple surface friction. Kinetic friction isn't perfectly constant with speed either, and the sharp drop on the graph is idealised; the change from sticking to sliding is often jerky. Studs also work partly by pushing into the ground, not only by surface friction.

## Key takeaway

Static friction matches any push up to its limit $\mu_s N$; a body slides only when the applied force exceeds that limit, and then kinetic friction $\mu_k N$, usually smaller, takes over. Rolling friction is far smaller than sliding friction, and lubrication reduces friction by separating sliding surfaces with a fluid layer.
