---
concept_id: free_body_diagrams
interest: motorsport
format: explain
title: Holding an engine still in mid-air
check:
  question: |-
    A $100\,\text{kg}$ engine hangs from a hoist chain. A mechanic pulls it sideways with a horizontal rope until the chain makes $45^\circ$ with the vertical, and holds it there at rest. Taking $g = 9.8\,\text{m/s}^2$, the tension in the chain is:
  options:
    A: |-
      $490\,\text{N}$
    B: |-
      $693\,\text{N}$
    C: |-
      $980\,\text{N}$
    D: |-
      $1386\,\text{N}$
  answer: D
  explanation: |-
    Only the vertical component of the chain's tension supports the weight: $T\cos 45^\circ = mg = 980\,\text{N}$, so $T = 980/0.707 \approx 1386\,\text{N}$.
  misconceptions:
    A: |-
      Splits the weight equally between the chain and the rope. The rope is horizontal, so it carries none of the weight at all.
    B: |-
      Resolves the *weight* along the chain, $mg\cos 45^\circ$, instead of resolving the *tension* into vertical and horizontal parts. Always resolve every force into the same two fixed directions.
    C: |-
      Assumes the chain always carries just the engine's weight. That is true only when it hangs vertically; pulled off vertical, the tension must be larger.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A race car in a braking zone with glowing brake discs, a skid mark and tyre smoke, a tyre barrier along the wall and a marshal with a yellow flag](scenes/motorsport/laws_of_motion.svg "On track the forces on a car change every instant. In the workshop, on something held still, they can be worked out exactly.")

The engine came out of the rally car an hour ago and is still hanging from the chain hoist in the middle of the workshop, turning gently. Bhavna's job is to guide it down onto the stand.

The trouble is that the stand is not directly underneath. Her cousin Imran loops a rope round the block and hauls it sideways until the chain is leaning clearly off vertical, then braces himself and holds it there while Bhavna drags the stand into place.

Her father, watching from the bench, puts his hand over the dial of the tension gauge spliced into the rope. "Before she gets there," he says, "tell me what this reads."

Imran guesses the engine's weight. Bhavna is not so sure: the engine is not being lifted, it is being held sideways — and the chain is pulling at an angle now, so it is not simply carrying the weight either. Three forces on one lump of metal, and nothing is moving at all.

How do you get a number out of that?

## The physics

The tool for this is the **free-body diagram**: a sketch of *one* body on its own, with an arrow for every force acting **on** it.

1. **Isolate the body.** Draw the engine alone, as a dot. The hoist, the rope, Imran and the floor all disappear.
2. **List every force on it.** Anything touching it can push or pull; gravity acts without touching. Here there are three: the weight $W = mg$ straight down, the tension $T$ in the chain pulling *along the chain*, and the horizontal pull $F$ of the rope.
3. **Draw each force** from the dot in its true direction. Forces the engine exerts on *other* things — its pull on the chain, for instance — belong on those bodies' diagrams, never on this one.
4. **Choose axes** and resolve any angled force into components along them.

![A body hanging from a beam on a cord at 30 degrees to the vertical, held aside by a horizontal string, next to its free-body diagram with the tension along the cord, the weight straight down, the horizontal pull, and the tension's two dashed components](figures/free_body_diagrams/ball-held-aside-fbd.svg "Three forces, one body. The dashed components of the tension are what you balance against the weight and the sideways pull. The mass shown is small for clarity; the method is the same for an engine.")

**Equilibrium.** The engine is at rest, so its acceleration is zero and, by Newton's second law, the net force on it must be zero. All three forces pass through one point — they are **concurrent** — so the whole condition is that their vector sum vanishes:

$$\vec{T} + \vec{W} + \vec{F} = 0$$

In components, each direction balances separately. With $\theta$ measured from the vertical:

$$\text{vertical: } T\cos\theta = mg \qquad \text{horizontal: } T\sin\theta = F$$

Dividing the second by the first eliminates $T$ and gives a tidy result: $F = mg\tan\theta$.

## Worked example

**Given:** engine mass $m = 100\,\text{kg}$ (illustrative); the chain is at $\theta = 30^\circ$ to the vertical; the rope is horizontal; $g = 9.8\,\text{m/s}^2$.
**Find:** the tension $T$ in the chain and the reading $F$ on the rope's gauge.

*Weight:* $W = mg = 100 \times 9.8 = 980\,\text{N}$, straight down.

*Vertical balance:* only the part of $T$ along the vertical holds the engine up.

$$T = \frac{mg}{\cos 30^\circ} = \frac{980}{0.866} \approx 1130\,\text{N}$$

So the chain is now carrying *more* than the engine's weight — pulling a hanging load sideways loads the chain harder, not less.

*Horizontal balance:*

$$F = T\sin 30^\circ = 1130 \times 0.500 \approx 570\,\text{N}$$

Imran is holding about $570\,\text{N}$, a little over half the engine's weight — heavy, but not the whole $980\,\text{N}$ he guessed.

**Sanity check:** the short route gives the same number, $F = mg\tan 30^\circ = 980 \times 0.577 \approx 570\,\text{N}$; and since $\tan\theta$ runs away as $\theta$ approaches $90^\circ$, no rope could ever hold the chain out horizontal, which matches everyday experience.

## Where the picture breaks

We treated the engine as a point, so all three forces meet at one spot. A real engine block is big and its weight acts at its centre of mass, so if the rope is looped high or low the forces no longer pass through one point and the block also **turns** — that needs torques, which come with rotational motion. We also assumed the chain and rope are light and perfectly still. A real hoisted engine swings a little, and the instant it accelerates the net force is no longer zero. And a real gauge has its own mass and its own zero error; $570\,\text{N}$ is the ideal reading.

## Key takeaway

A free-body diagram shows one body alone with every force acting **on** it, drawn in its true direction. If the body is in equilibrium the vector sum of those forces is zero, so the components balance separately in each direction. For three concurrent forces that is enough to find the unknowns: here $T = mg/\cos\theta$ and $F = mg\tan\theta$.
