---
concept_id: mechanical_energy_conservation
interest: smartphones
format: explain
title: How fast is a phone falling off the top bunk
check:
  question: |-
    A camera drone is hovering at rest $5.0\,\text{m}$ above the ground when its battery cuts out and it falls. Ignoring air resistance and taking $g = 9.8\,\text{m/s}^2$, how fast is it moving just before it reaches the ground?
  options:
    A: |-
      $7.0\,\text{m/s}$
    B: |-
      $98\,\text{m/s}$
    C: |-
      $5.0\,\text{m/s}$
    D: |-
      $9.9\,\text{m/s}$
  answer: D
  explanation: |-
    Only gravity does work, so $mgh = \tfrac{1}{2}mv^2$ and $v = \sqrt{2gh} = \sqrt{2 \times 9.8 \times 5.0} = \sqrt{98} \approx 9.9\,\text{m/s}$. The mass cancels.
  misconceptions:
    A: |-
      Drops the 2 and uses $v = \sqrt{gh} = \sqrt{49}$. The 2 comes from the half in $\tfrac{1}{2}mv^2$: set $mgh$ equal to $\tfrac{1}{2}mv^2$, not to $mv^2$.
    B: |-
      Finds $v^2 = 2gh = 98$ and forgets to take the square root, so the answer has units of $\text{m}^2/\text{s}^2$, not $\text{m/s}$.
    C: |-
      Works out the fall time (about $1.0\,\text{s}$) and divides the height by it. That gives the *average* speed; a falling body speeds up all the way, so it hits the ground at about twice the average.
author: claude-code/opus-5
written: 2026-09-25
---
## The story

![A living room in the evening: a camera drone climbs straight up, a phone falls from a shelf towards a cushion, an earbuds case is whirled on a lanyard in a vertical circle, and a robot vacuum rolls towards a sofa leg](scenes/smartphones/work_energy_power.svg "The phone falling from the shelf is losing height and gaining speed — and nothing else is happening to its energy.")

It is past midnight in the hostel room. Varun is on the top bunk, holding his phone above his face, when he dozes off. The phone slides out of his hand, over the edge of the mattress, and drops.

His roommate Joseph, awake on the lower bunk, hears the crack of it on the floor. The screen has a spider-web in one corner.

In the morning, the argument starts. "It was only a bunk," Varun says. "It can't have been going that fast."

"Your *tablet* fell off the same bunk last month," Joseph points out, "and that was heavier. Heavier things fall faster, so this should've been gentler."

Varun isn't sure that's how it works. How fast was the phone actually going when it hit — and would the heavier tablet really have been faster?

## The physics

The **mechanical energy** of a body is the sum of its kinetic and potential energies, $E = K + U$.

If **only conservative forces do work** (gravity, ideal springs), mechanical energy is **conserved**:

$$K_i + U_i = K_f + U_f$$

Every joule of potential energy that disappears reappears as kinetic energy, and vice versa. Near the Earth's surface, for a body falling from rest through height $h$:

$$mgh = \tfrac{1}{2}mv^2 \quad\Rightarrow\quad v = \sqrt{2gh}$$

The mass cancels. A phone and a tablet dropped from the same height, with air resistance negligible, land at the same speed. Joseph's heavier tablet had more energy, but it also had more mass to share it among.

![Left: kinetic and potential energy plotted against the height still to fall, as fractions of the total, crossing at half and half with a flat dashed total. Right: speed as a fraction of the final speed, a curve that reaches 71 per cent halfway down](figures/mechanical_energy_conservation/energy-and-speed-down-a-drop.svg "Energy changes form at a steady rate, metre by metre, and the total never moves. Speed doesn't keep pace: it goes as a square root, so by halfway down the phone already has 71 per cent of its final speed.")

## Worked example

**Given:** the phone's mass is $m = 0.20\,\text{kg}$; it falls from rest through $h = 1.25\,\text{m}$ from the mattress to the floor (illustrative); $g = 9.8\,\text{m/s}^2$; air resistance ignored.
**Find:** its speed on landing.

1. *Energy at the top:* all potential, $U = mgh = 0.20 \times 9.8 \times 1.25 = 2.45\,\text{J}$; $K = 0$.
2. *Energy at the floor:* all kinetic, so $\tfrac{1}{2}mv^2 = 2.45\,\text{J}$.
3. *Speed:* $v = \sqrt{2 \times 2.45 / 0.20} = \sqrt{24.5} \approx 4.9\,\text{m/s}$ — about $18\,\text{km/h}$, the pace of someone cycling.
4. *Halfway down:* half the energy has turned into kinetic, so $v = \sqrt{2 \times 1.225 / 0.20} \approx 3.5\,\text{m/s}$ — already 71 per cent of the landing speed.

**Sanity check:** $v = \sqrt{2gh}$ gives the same $4.9\,\text{m/s}$ straight away, with no mass needed — which settles Joseph's argument.

## Where the picture breaks

The phone is a real case, and for a short fall like this air resistance really is small, so the answer is close. But the moment the phone touches the floor, conservation of mechanical energy stops applying: the floor's push and the crushing glass are not conservative, and the $2.45\,\text{J}$ becomes sound, heat and a cracked screen. Over long falls — a phone dropped from a balcony — air drag stops being negligible, and a flat tablet feels more of it than a compact phone, so the "same speed" result would no longer hold exactly.

## Key takeaway

When only conservative forces do work, the total mechanical energy $K + U$ stays constant: height lost becomes speed gained. For a fall from rest, $mgh = \tfrac{1}{2}mv^2$, so $v = \sqrt{2gh}$, whatever the mass.
