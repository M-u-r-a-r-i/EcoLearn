---
concept_id: impulse
interest: smartphones
format: explain
title: Why a soft phone case saves the screen
check:
  question: |-
    A $0.20\,\text{kg}$ phone hits the floor at $4.0\,\text{m/s}$ and is brought to rest, without bouncing, in $10\,\text{ms}$. What is the average net force on it during the impact?
  options:
    A: |-
      $0.80\,\text{N}$
    B: |-
      $8.0\,\text{N}$
    C: |-
      $80\,\text{N}$
    D: |-
      $0.0080\,\text{N}$
  answer: C
  explanation: |-
    The impulse equals the change in momentum, $0.20 \times 4.0 = 0.80\,\text{N s}$. Spread over $10\,\text{ms} = 0.010\,\text{s}$, the average force is $0.80 / 0.010 = 80\,\text{N}$.
  misconceptions:
    A: |-
      Stops at the impulse, $0.80\,\text{N s}$, and reports it as a force. Impulse is force *times* time; to get the force you must still divide by the contact time.
    B: |-
      Converts $10\,\text{ms}$ to $0.1\,\text{s}$ instead of $0.010\,\text{s}$. A millisecond is a thousandth of a second, so the slip makes the force ten times too small.
    D: |-
      Multiplies the impulse by the time instead of dividing. Impulse $= F\Delta t$, so $F = \text{impulse}/\Delta t$ — a shorter time must give a *bigger* force, not a smaller one.
author: claude-code/opus-5
written: 2026-09-25
---
## The story

![A study room at night: a camera drone hovers pushing air down, a phone tumbles off a shelf towards the tiles, and a power bank dangles off a desk by its cable](scenes/smartphones/laws_of_motion.svg "The phone in the middle is about to meet the tiles. What decides the damage is how quickly it is stopped.")

Aditi leans across her bookshelf to unplug a charger and knocks her phone off the top shelf. It turns over once in the air and lands corner-first on the floor tiles with a sharp crack. She picks it up. A thin line now runs across one corner of the screen.

The worst part is that her brother Nikhil dropped his phone off the same shelf last week, onto the same tiles, and walked away with nothing. His phone wears a chunky case with soft, thick rubber corners that everyone teases him about.

"Both phones fell from the same height," Aditi says. "Both hit the same floor and both ended up lying still. The floor had to do the same job both times."

Nikhil taps his rubber corner. "Then why is only yours cracked?"

It's a fair question. If both phones lost exactly the same motion, what exactly did a few millimetres of rubber change?

## The physics

When a force $F$ acts on a body for a time $\Delta t$, the product is called the **impulse**, $J$:

$$J = F\,\Delta t$$

From Newton's second law, $F = \Delta p/\Delta t$ for a constant (or average) force, so

$$J = F\,\Delta t = \Delta p$$

**Impulse equals change in momentum.** Its unit is $\text{N s}$, which is the same as $\text{kg m/s}$. When the force varies during a collision, as it always does, the impulse is the **area under the force–time graph**, and $F$ above means the *average* force.

For a phone that falls and stops, $\Delta p$ is fixed by its mass and landing speed. The floor has to deliver exactly that impulse, however it is done. What the floor *can* change is how long it takes:

$$F_\text{avg} = \frac{\Delta p}{\Delta t}$$

Stretch $\Delta t$, and the average force falls in proportion. Hard tiles and a bare glass corner stop the phone in a couple of thousandths of a second. Soft rubber squashes, so the stop lasts several times longer and the peak force is several times smaller — often small enough to spare the glass.

![Force–time graph with two triangles of equal area: a tall narrow spike and a low wide hump lasting five times longer](figures/impulse/force-time-stiff-vs-soft.svg "Drawn for a different impact, but it is the bare phone against the rubber corner: equal areas mean equal impulses, and spreading the stop over five times the time cuts the peak force five times.")

## Worked example

**Given:** a phone of mass $0.20\,\text{kg}$ hits the tiles at $5.0\,\text{m/s}$ (roughly the speed after falling from a high shelf) and stops without bouncing. Bare, it stops in $2.0\,\text{ms}$; in a soft case, in $10\,\text{ms}$ (illustrative).
**Find:** the impulse, and the average net force in each case.

1. *Impulse.* Taking up as positive, the momentum goes from $0.20 \times (-5.0) = -1.0\,\text{kg m/s}$ to zero, so
$$J = \Delta p = 0 - (-1.0) = +1.0\,\text{N s}, \text{ upwards}$$
Both phones receive this same impulse.

2. *Bare phone.* $2.0\,\text{ms} = 0.0020\,\text{s}$:
$$F_\text{avg} = \frac{1.0}{0.0020} = 500\,\text{N}$$
That is about the weight of a $50\,\text{kg}$ person, concentrated on one corner of glass.

3. *Cased phone.*
$$F_\text{avg} = \frac{1.0}{0.010} = 100\,\text{N}$$
Five times the time, a fifth of the force.

**Sanity check:** a force of hundreds of newtons from a two-hundred-gram phone sounds huge, but it lasts only a couple of milliseconds — which is exactly why impacts break things that ordinary handling never does.

## Where the picture breaks

We used the *average* force; the real force rises and falls during the impact, and the peak is higher than the average. We also ignored the phone's weight during the stop — the floor must push an extra $2\,\text{N}$ or so to hold it up, tiny next to $100$–$500\,\text{N}$. Real phones often bounce, which makes the change in momentum *larger* than a plain stop. And a case protects glass partly by spreading the force over more area, not only by stretching the time. Impulse explains the time part; the rest is about materials.

## Key takeaway

Impulse is force times time, and it equals the change in momentum: $J = F\,\Delta t = \Delta p$. For a given change in momentum, lengthening the stopping time lowers the average force in proportion — which is why soft cases, airbags and bending your knees on landing all work.
