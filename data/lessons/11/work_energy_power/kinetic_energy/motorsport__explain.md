---
concept_id: kinetic_energy
interest: motorsport
format: explain
title: Why push starting gets brutal at the end
check:
  question: |-
    A kart and driver of total mass $200\,\text{kg}$ is pushed from rest up to $20\,\text{m/s}$ on a level track. Ignoring friction and drag, how much work must the net force do — and what would it be for a target speed of $40\,\text{m/s}$ instead?
  options:
    A: |-
      $40\,\text{kJ}$, and $160\,\text{kJ}$ for the higher target
    B: |-
      $40\,\text{kJ}$, and $80\,\text{kJ}$ for the higher target
    C: |-
      $2\,\text{kJ}$, and $4\,\text{kJ}$ for the higher target
    D: |-
      $80\,\text{kJ}$, and $320\,\text{kJ}$ for the higher target
  answer: A
  explanation: |-
    The work needed from rest equals the kinetic energy gained: $K = \tfrac{1}{2}mv^2 = \tfrac{1}{2}(200)(20)^2 = 40\,000\,\text{J}$. Doubling $v$ multiplies $v^2$ by four, so $40\,\text{kJ}$ becomes $160\,\text{kJ}$.
  misconceptions:
    B: |-
      Gets the first figure right but treats energy as proportional to speed. Because $v$ is squared, doubling the speed multiplies the energy by four, not two.
    C: |-
      Uses $\tfrac{1}{2}mv$ instead of $\tfrac{1}{2}mv^2$ — the speed is squared. The units give it away: $\text{kg}\,\text{m/s}$ is momentum, not joules.
    D: |-
      Uses $mv^2$ and forgets the factor $\tfrac{1}{2}$. Every figure comes out exactly twice as large as it should.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A race track scene: a car coasts down a hill road onto the circuit, a second car speeds along the straight with a velocity arrow, a third brakes with glowing red discs, and two people push a kart in the foreground](scenes/motorsport/work_energy_power.svg "The car on the straight carries an enormous amount of energy purely because it is moving. That is what this lesson is about.")

The junior session at the karting club starts badly: the engine on kart 14 refuses to fire, so it has to be push-started. Pallavi and Girish take a side each and shove.

Getting it walking is nothing. In about ten strides the kart is rolling along at a comfortable walking pace, and they are barely breathing hard.

Then the instructor calls across that walking pace is not enough — this engine needs the kart at roughly *double* that, a decent jog, before the clutch will bite.

"Fine," says Girish. "Twice as fast, twice as much shoving. Ten more strides."

It is not ten more strides. By the time the engine finally catches, both of them are bent over the fence with their hands on their knees, and the second half of that push felt nothing like the first. Girish is certain the kart got heavier.

It didn't. So why does the last bit of speed cost so much more than the first?

## The physics

A moving body can do work on whatever it runs into — that stored ability is its **kinetic energy**. For a body of mass $m$ moving at speed $v$,

$$K = \frac{1}{2}mv^2$$

Kinetic energy is a **scalar**, measured in **joules**, and it is never negative: $v^2$ is positive whichever way the body is going. Check the units: $\text{kg} \times (\text{m/s})^2 = \text{kg}\,\text{m}^2/\text{s}^2 = \text{N}\,\text{m} = \text{J}$.

Where does the $\tfrac{1}{2}v^2$ come from? Push a body of mass $m$ from rest with a constant net force $F$ over a distance $d$. From the equation of motion $v^2 = 2ad$, we get $d = v^2/2a$, so the work done is

$$W = Fd = ma \times \frac{v^2}{2a} = \frac{1}{2}mv^2$$

The acceleration cancels. **The work needed to bring a body from rest to speed $v$ is exactly $\tfrac{1}{2}mv^2$, however gently or violently you do it.** That is the sentence that answers Pallavi and Girish.

![A curve of kinetic energy plotted against speed, both expressed as multiples of a reference value, marked where doubling the speed gives four times the energy and tripling it gives nine times](figures/kinetic_energy/ke-ratio-vs-speed-ratio.svg "The curve bends upwards because K depends on v squared. The extra energy needed for each extra metre per second keeps growing.")

Read the curve as a shopping bill. Going from rest to walking pace buys you the shallow bit at the bottom. Going from walking pace to jogging pace — the *same* increase in speed — costs three times as much again, because you are now climbing the steep part. Mass matters too, but only once: double the mass and you double the energy, while doubling the speed quadruples it.

## Worked example

**Given** (illustrative): kart plus driver, $m = 200\,\text{kg}$. The first push reaches $2\,\text{m/s}$ (a brisk walk); the second push reaches $4\,\text{m/s}$ (a jog).
**Find:** the energy at each speed, and how much of the total was spent on the second half of the job.

*At the end of the easy part:*

$$K_1 = \tfrac{1}{2}(200)(2)^2 = 100 \times 4 = 400\,\text{J}$$

*At the end of the hard part:*

$$K_2 = \tfrac{1}{2}(200)(4)^2 = 100 \times 16 = 1600\,\text{J}$$

Doubling the speed has given four times the energy — and the difference is the answer to Girish's complaint. Going from rest to a walk cost $400\,\text{J}$; going from a walk to a jog cost $1600 - 400 = 1200\,\text{J}$, **three times as much**, for the very same gain in speed.

**Sanity check:** $1600\,\text{J}$ is about what you would spend lifting the whole $200\,\text{kg}$ kart and driver to waist height, roughly $0.8\,\text{m}$ off the ground. Two people heaving a kart up to waist height — that feels about right for a hard push, and it explains the hands on the knees.

For scale, out on the circuit at $20\,\text{m/s}$ that same kart carries $40\,000\,\text{J}$ — twenty-five times the energy of the push start, from five times the speed.

## Where the picture breaks

$K = \tfrac{1}{2}mv^2$ treats the kart as a single lump sliding along. In truth its four wheels and the engine's internals are also *spinning*, and they store extra kinetic energy that this formula ignores — rotational energy is a later chapter. The formula is also written for one chosen frame of reference: the kart's kinetic energy measured from the pit wall and from a car driving alongside are different numbers, and neither is wrong. Finally, the push start is not frictionless. Some of what Pallavi and Girish put in went into rolling resistance, the chain and the clutch, so the real effort was more than $1600\,\text{J}$ — the kinetic energy is the minimum, not the bill.

## Key takeaway

Kinetic energy is $K = \tfrac{1}{2}mv^2$, in joules, and it is exactly the work needed to bring a body from rest to that speed. Because the speed is squared, energy grows far faster than speed: double the speed and you need four times the energy, triple it and you need nine times.
