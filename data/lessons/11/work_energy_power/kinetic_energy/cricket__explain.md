---
concept_id: kinetic_energy
interest: cricket
format: explain
title: Twice as fast, four times the energy
check:
  question: |-
    A spinner's delivery leaves the hand at $72\,\text{km/h}$. The ball's mass is $0.16\,\text{kg}$. What is its kinetic energy?
  options:
    A: |-
      $415\,\text{J}$
    B: |-
      $1.6\,\text{J}$
    C: |-
      $32\,\text{J}$
    D: |-
      $64\,\text{J}$
  answer: C
  explanation: |-
    Convert first: $72\,\text{km/h} = 72/3.6 = 20\,\text{m/s}$. Then $K = \tfrac{1}{2}mv^2 = \tfrac{1}{2} \times 0.16 \times 20^2 = 0.08 \times 400 = 32\,\text{J}$.
  misconceptions:
    A: |-
      Puts the speed in km/h straight into $\tfrac{1}{2}mv^2$ ($0.08 \times 72^2 \approx 415$); the joule is built on metres per second, so the speed must be converted first.
    B: |-
      Forgets to square the speed ($0.08 \times 20$); kinetic energy grows with the square of speed, not in proportion to it.
    D: |-
      Leaves out the factor of one half ($0.16 \times 20^2$); the $\tfrac{1}{2}$ comes from the work needed to build up the speed from rest.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A cricket ground by day: a batter watches a ball climb high, a fielder waits under it, a player runs up the stadium steps and a groundsman pushes a roller](scenes/cricket/work_energy_power.svg "Every ball in play carries energy, and the faster it moves, the more it carries.")

At the academy nets, Imran has been told to field at short leg — crouched a couple of metres from the bat, helmet on, pads strapped to his shins. For the first half-hour a spinner is bowling, at about $72\,\text{km/h}$. Then Arjun, the quickest bowler in the squad, takes the ball and starts touching $144\,\text{km/h}$.

"It's only twice as fast," Imran says, trying to sound brave.

The academy physio, standing nearby, shakes her head. "Twice as fast means *four* times the energy if it hits you. Keep your helmet on."

Imran frowns. How can doubling the speed quadruple anything? The ball is the same ball. What exactly is this energy, and why does speed count twice?

## The physics

A moving body can do work — a moving ball can push back a glove, bend a stump or dent a helmet's padding. The energy a body has **because of its motion** is its **kinetic energy**:

$$K = \tfrac{1}{2}mv^2$$

where $m$ is the mass and $v$ the speed. It is a scalar, measured in joules, never negative, and it doesn't depend on the direction of motion.

**Where the formula comes from.** Push a body of mass $m$, starting at rest, with a constant net force $F$ along a straight line for a distance $d$. Its acceleration is $a = F/m$, and from the equations of motion, $v^2 = 0 + 2ad$. The work done is

$$W = Fd = (ma)d = m \cdot \frac{v^2}{2} = \tfrac{1}{2}mv^2$$

So $\tfrac{1}{2}mv^2$ is exactly the work needed to bring the body from rest to speed $v$. Stopping it again requires the same amount of work to be taken away.

The $v^2$ explains the physio's warning. Speed appears twice: a faster ball needs a larger force for the same distance, *and* it covers more distance while that force acts. Double the speed and the energy goes up by $2^2 = 4$.

![A curve of kinetic energy against speed for a 0.16 kilogram ball: 32 joules at 20 metres per second and 128 joules at 40 metres per second](figures/kinetic_energy/ke-vs-speed.svg "The curve bends upwards because K depends on v squared. Doubling the speed from 20 to 40 m/s multiplies the energy by four.")

## Worked example

**Given:** ball mass $m = 0.16\,\text{kg}$ (within the Laws' range of $155.9$–$163\,\text{g}$); spinner at $72\,\text{km/h}$; Arjun at $144\,\text{km/h}$.
**Find:** each ball's kinetic energy, and the average force Arjun's hand applies if it builds up the ball's speed over about $1.6\,\text{m}$ (illustrative).

Convert: $72/3.6 = 20\,\text{m/s}$ and $144/3.6 = 40\,\text{m/s}$.

$$K_\text{spin} = \tfrac{1}{2} \times 0.16 \times 20^2 = 0.08 \times 400 = 32\,\text{J}$$

$$K_\text{fast} = \tfrac{1}{2} \times 0.16 \times 40^2 = 0.08 \times 1600 = 128\,\text{J}$$

The ratio is $128/32 = 4$, as promised.

The ball starts from rest in Arjun's hand, so his hand must do $128\,\text{J}$ of work on it. Over $1.6\,\text{m}$:

$$F_\text{avg} = \frac{W}{d} = \frac{128}{1.6} = 80\,\text{N}$$

**Sanity check:** the ball's weight is $0.16 \times 9.8 \approx 1.6\,\text{N}$, so the hand pushes with about 50 times the ball's weight — a big force from a whole-body action, which is plausible. Units: $\text{kg} \times (\text{m/s})^2 = \text{kg m}^2/\text{s}^2 = \text{J}$.

## Where the picture breaks

A real delivery doesn't use a constant force along a straight line. The hand swings through an arc and the force rises and falls, so $80\,\text{N}$ is only an average along the path. The ball also spins, which stores a little extra energy of rotation that $\tfrac{1}{2}mv^2$ leaves out — you'll meet rotational kinetic energy later. Speed also depends on who's measuring: to the batter, the ball carries $128\,\text{J}$; to someone moving alongside it, it carries less. And kinetic energy isn't "hurt": how much a blow harms depends on how quickly, and over how small an area, the energy is removed. That's why a helmet's padding matters.

## Key takeaway

Kinetic energy is the energy of motion, $K = \tfrac{1}{2}mv^2$. It equals the work needed to bring a body from rest to speed $v$, and the work needed to stop it again. Because it depends on $v^2$, doubling the speed quadruples the energy.
