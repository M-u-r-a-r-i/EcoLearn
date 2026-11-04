---
concept_id: mechanical_energy_conservation
interest: motorsport
format: explain
title: The engineless race where weight buys nothing
check:
  question: |-
    Two gravity racers — one $60\,\text{kg}$ and one $120\,\text{kg}$, including driver — are released from rest at the top of the same smooth $20\,\text{m}$ drop. Ignoring friction and air resistance, and taking $g = 9.8\,\text{m/s}^2$, what speeds do they reach at the bottom?
  options:
    A: |-
      Both about $20\,\text{m/s}$.
    B: |-
      The heavier one about $28\,\text{m/s}$, the lighter one about $20\,\text{m/s}$.
    C: |-
      The heavier one about $40\,\text{m/s}$, the lighter one about $20\,\text{m/s}$.
    D: |-
      Both about $392\,\text{m/s}$.
  answer: A
  explanation: |-
    $mgh = \tfrac{1}{2}mv^2$, and the mass cancels, leaving $v = \sqrt{2gh} = \sqrt{2 \times 9.8 \times 20} = \sqrt{392} \approx 19.8\,\text{m/s}$ for both.
  misconceptions:
    B: |-
      Assumes the extra mass shows up as $\sqrt{2}$ more speed. The heavier racer does arrive with twice the kinetic energy, but it also needed twice as much to reach any given speed, so the speed is unchanged.
    C: |-
      Reads "more mass means more energy" as "more mass means more speed". Mass appears on both sides of $mgh = \tfrac{1}{2}mv^2$ and cancels completely.
    D: |-
      Stops at $v^2 = 2gh = 392$ and forgets the square root. Check the units: $392$ is in $\text{m}^2/\text{s}^2$, not $\text{m/s}$.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A race track scene: a car coasts down a hill road onto the circuit, a second car speeds along the straight with a velocity arrow, a third brakes with glowing red discs, and two people push a kart in the foreground](scenes/motorsport/work_energy_power.svg "The car rolling down the hill road has no engine running. The hill is doing all the work.")

Once a year the car club closes a quiet slope on the edge of town and runs a gravity race: home-built four-wheeled carts, no engines, no pedals, one push over the line at the top and gravity for the rest.

Vinay has spent three weekends on his. It is built out of angle iron and a tractor seat, and it is *heavy*. "Heavier means more energy," he says, slapping the frame. "More energy means more speed. Simple."

Aparna's cart is plywood and bicycle wheels and weighs about as much as a suitcase. Her father, who has done this before, only laughs.

They line up. The flag drops. And for the first two hundred metres the two carts run side by side so evenly that the timekeeper at the bottom has to look twice.

Vinay is furious. All that steel, and it bought him nothing. Where did his extra energy go?

## The physics

Define the **mechanical energy** of a body as its kinetic energy plus its potential energy:

$$E = K + U$$

If **only conservative forces do work** — gravity, an ideal spring — then the work–energy theorem says $W_\text{net} = \Delta K$, and for a conservative force $W = -\Delta U$. Putting them together:

$$\Delta K = -\Delta U \quad\Rightarrow\quad \Delta(K + U) = 0 \quad\Rightarrow\quad E = K + U = \text{constant}$$

This is the **conservation of mechanical energy**. Energy is not created or destroyed as the body moves; it is simply moved between the kinetic account and the potential account. The condition in bold is not optional: as soon as friction or drag does work, $E$ falls.

![Left: kinetic and potential energy plotted against the height still to fall, as fractions of the total, crossing at half and half with a flat dashed total. Right: speed as a fraction of the final speed, a curve that reaches 71 per cent halfway down and half the final speed a quarter of the way down](figures/mechanical_energy_conservation/energy-and-speed-down-a-drop.svg "Every metre dropped moves the same amount of energy from U to K, so the total never changes. Speed is different: it goes as the square root, so most of it arrives early.")

For a body **released from rest** and dropping a height $h$ with no friction:

$$mgh = \tfrac{1}{2}mv^2 \quad\Rightarrow\quad v = \sqrt{2gh}$$

Look at what just happened to Vinay. **The mass cancels.** It appears on both sides because the same $m$ that collects the gravitational energy is the $m$ that has to be accelerated. A heavier cart really does arrive with more energy — but it needs proportionally more energy for every metre per second, so the speed comes out identical.

Notice also that $h$ is the **vertical drop only**. It does not matter whether the slope is straight, curved, steep then shallow, or a loop — with no friction, only the change in height counts. That is the whole payoff of using energy instead of forces: you never have to know the shape of the road.

## Worked example

**Given:** a gravity racer released from rest; the course drops $h = 20\,\text{m}$ from the start line to the finish; friction and air resistance ignored; $g = 9.8\,\text{m/s}^2$.
**Find:** the speed at the finish, and the speed halfway down.

*At the finish*, all $mgh$ has become $\tfrac{1}{2}mv^2$:

$$v = \sqrt{2gh} = \sqrt{2 \times 9.8 \times 20} = \sqrt{392} \approx 19.8\,\text{m/s}$$

About $20\,\text{m/s}$, which is roughly $71\,\text{km/h}$ — and the same number for Vinay's steel cart and Aparna's plywood one, because no mass appears anywhere in that line.

*Halfway down*, the drop so far is $10\,\text{m}$:

$$v = \sqrt{2 \times 9.8 \times 10} = \sqrt{196} = 14\,\text{m/s}$$

Half the hill, but **not** half the speed — $14$ out of $19.8$ is about $71\%$ of it. Half the *energy* has been delivered, and speed goes as the square root of energy.

**Sanity check:** a cart with no engine reaching motorway speed down a twenty-metre hill sounds high, and it is: this is the frictionless ceiling, the fastest the hill could possibly make it go.

## Where the picture breaks

That ceiling is the honest limit of this picture. Real gravity racers reach perhaps half the frictionless speed, because air drag, rolling resistance and bearing friction are all doing negative work all the way down, and mechanical energy is **not** conserved when they act — the missing joules turn into heat in the wheels and swirling air, and they never come back. Mass matters once drag enters, because a heavy cart has more energy to spend against the same air resistance. It matters again for the hidden kinetic energy in the *spinning* wheels, which this formula ignores. And a cart is treated here as a point at a single height, so nothing in $mgh$ knows that a low, long cart handles the corners better than a tall one.

## Key takeaway

When only conservative forces do work, the mechanical energy $E = K + U$ stays constant: energy simply shifts between the two accounts. For a body released from rest through a drop $h$, this gives $v = \sqrt{2gh}$ — independent of mass, and independent of the shape of the path. The moment friction or drag does work, the total falls and this shortcut no longer applies.
