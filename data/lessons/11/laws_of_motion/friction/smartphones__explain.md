---
concept_id: friction
interest: smartphones
format: explain
title: Glass back or silicone case on the dashboard
check:
  question: |-
    A $0.20\,\text{kg}$ phone lies on a level desk. The coefficients of friction are $\mu_s = 0.50$ and $\mu_k = 0.40$. A finger pushes it sideways with a steady $0.80\,\text{N}$. Taking $g = 10\,\text{m/s}^2$, what happens?
  options:
    A: |-
      It stays put, and the friction on it is $0.80\,\text{N}$
    B: |-
      It stays put, and the friction on it is $1.0\,\text{N}$
    C: |-
      It slides, because the push reaches the kinetic friction of $0.80\,\text{N}$
    D: |-
      It stays put, and the friction on it is zero because it isn't moving
  answer: A
  explanation: |-
    The limit of static friction is $\mu_s N = 0.50 \times 2.0 = 1.0\,\text{N}$. The push of $0.80\,\text{N}$ is below it, so the phone stays at rest and static friction adjusts to exactly $0.80\,\text{N}$, balancing the push.
  misconceptions:
    B: |-
      Treats $\mu_s N$ as the friction that always acts. It is only the *maximum*; static friction is self-adjusting and equals the push until that limit is reached.
    C: |-
      Compares the push with *kinetic* friction to decide whether sliding starts. A resting body starts to slide only when the push exceeds the larger limiting static friction, $1.0\,\text{N}$ here.
    D: |-
      Thinks friction needs motion. Static friction acts on a body at rest whenever something tries to slide it; without it, the $0.80\,\text{N}$ push would be unbalanced and the phone would accelerate.
author: claude-code/opus-5
written: 2026-09-25
---
## The story

![A study room at night: a camera drone hovers pushing air down, a phone tumbles off a shelf towards the tiles, and a power bank dangles off a desk by its cable](scenes/smartphones/laws_of_motion.svg "The phone on the desk is sliding because the cable's pull beat the grip of the desk. Whether grip wins or loses is the whole of this lesson.")

Samira is in the back seat of her aunt's car on the way to a wedding in Jaipur. At a petrol pump, both her aunt and her uncle drop their phones on the flat part of the dashboard: her uncle's has a bare, glossy glass back, her aunt's is in a matte silicone case.

The car pulls away from the pump briskly. The uncle's phone glides backwards along the dashboard and drops off the edge into his lap. The aunt's phone doesn't move at all.

"Mine's heavier," her uncle says. "That's why it slid."

"Mine's in a thick case," says her aunt. "If anything, mine is the heavier one."

Samira has seen the first law — the car pulls away, and a phone stays behind unless something drags it along. But then something *did* drag the aunt's phone along. Why could that something manage one phone and not the other?

## The physics

**Friction** opposes sliding, or attempted sliding, between surfaces in contact, and acts along them.

- **Static friction** acts when there is no sliding yet. It is **self-adjusting**: it equals whatever is needed to prevent sliding, up to a maximum called **limiting friction**:
$$f_s \le \mu_s N$$
- **Kinetic friction** acts once sliding starts, and is roughly constant:
$$f_k = \mu_k N$$
For almost every pair of surfaces, $\mu_k < \mu_s$.
- **Rolling friction**, on a wheel rolling without slipping, is far smaller again — which is why a robot vacuum rolls on wheels rather than sliding on pads.

Here $N$ is the normal force, and $\mu_s$, $\mu_k$ are coefficients that depend on the two surfaces, not on the area of contact.

To decide whether a body slides: **work out the friction needed to keep it with its surface, and compare it with $\mu_s N$.** If the need is less, it stays put and friction equals the need. If the need is more, it slides and kinetic friction takes over.

![Graph of friction against the horizontal push on a resting body: friction rises along a straight line equal to the push until it reaches its limit, then drops abruptly to a smaller constant value once sliding starts](figures/friction/friction-vs-push.svg "Drawn for a heavy box, but the shape is the dashboard's: friction matches the need exactly up to the limit, then drops to the smaller kinetic value once sliding starts.")

On the dashboard, the only horizontal force that can give a phone the car's acceleration is static friction. Silicone grips much better than glass, so its limit is far higher.

**Lubrication** works by keeping two surfaces apart with a thin layer of oil or grease, so they slide over the fluid instead of catching on each other's high points. The sealed bearings in a laptop's cooling fan are lubricated for exactly this reason.

## Worked example

**Given:** each phone has mass $0.20\,\text{kg}$, so $N = mg = 2.0\,\text{N}$ taking $g = 10\,\text{m/s}^2$. The car accelerates at $3.0\,\text{m/s}^2$. Glass on the dashboard has $\mu_s = 0.20$; silicone has $\mu_s = 0.80$ (illustrative).
**Find:** whether each phone slides.

1. *Friction needed.* To accelerate with the car, a phone needs
$$f = ma = 0.20 \times 3.0 = 0.60\,\text{N}$$

2. *Glass back.* The limit is $\mu_s N = 0.20 \times 2.0 = 0.40\,\text{N}$. That is less than $0.60\,\text{N}$, so the phone slides back relative to the dashboard.

3. *Silicone case.* The limit is $0.80 \times 2.0 = 1.6\,\text{N}$, well above $0.60\,\text{N}$. The phone stays put, and the friction on it is just $0.60\,\text{N}$ — not $1.6\,\text{N}$.

**Sanity check:** mass cancels from the comparison ($ma$ against $\mu_s mg$), so the uncle was wrong to blame the weight — a phone slides when $a > \mu_s g$, whatever it weighs.

## Where the picture breaks

A dashboard is not flat: it tilts, so part of the weight acts along it. The coefficients above are illustrative — real values depend on dust, heat and how clean the glass is. $f = \mu N$ is an empirical rule, not a fundamental law, and it only holds roughly. And real acceleration isn't steady: a sudden jerk can briefly exceed the limit, which is why even a silicone-cased phone sometimes shifts.

## Key takeaway

Static friction adjusts to prevent sliding, up to a limit $\mu_s N$; once sliding starts, the smaller kinetic friction $\mu_k N$ acts, and rolling friction is smaller still. To decide whether something slides, compare the friction it needs with $\mu_s N$. Lubricants lower friction by separating the surfaces.
