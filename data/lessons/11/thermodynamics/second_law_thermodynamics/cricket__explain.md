---
concept_id: second_law_thermodynamics
interest: cricket
format: explain
title: The fuel-free scoreboard that can never be built
check:
  question: |-
    An inventor claims her new generator for cricket grounds absorbs $20\,\text{kJ}$ of heat from burning fuel in each cycle and delivers $20\,\text{kJ}$ of electrical work, rejecting no heat at all. Which judgement is correct?
  options:
    A: |-
      Possible, because the energy output equals the energy input, so energy is conserved.
    B: |-
      Impossible, because it breaks the Kelvin–Planck statement: some heat must be rejected to a colder body.
    C: |-
      Impossible, because it breaks the first law: it produces more energy than it takes in.
    D: |-
      Possible in principle, if all friction inside the machine could be eliminated.
  answer: B
  explanation: |-
    The claim obeys the first law ($20\,\text{kJ}$ in, $20\,\text{kJ}$ out), but converting all the heat absorbed into work, with nothing else happening, is exactly what the Kelvin–Planck statement forbids. A real engine must reject some heat, so its efficiency is below 100%.
  misconceptions:
    A: |-
      Thinks energy conservation is the only rule. The first law is satisfied here; the second law is what the claim breaks.
    C: |-
      Blames the wrong law. Input and output are both $20\,\text{kJ}$, so no energy is created; the first law is obeyed.
    D: |-
      Thinks engines fall short of 100% only because of friction and poor design. Even an ideal, frictionless engine must reject heat to a cold reservoir.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A hot afternoon at a cricket ground: blazing sun, a board showing 38 degrees, a bowler polishing the ball, a generator with hot exhaust and an ice box of drinks](scenes/cricket/thermodynamics.svg "The air is at 38 °C, full of thermal energy. The generator still needs diesel. Why?")

Between innings on a 38-degree day, Aditya is sketching an invention on the back of a scorecard. His sister Kavya, who has just finished the first-law chapter in Class 11, leans over to look.

"Look at all this heat," Aditya says, waving at the shimmering outfield. "The air is full of energy. My machine sucks in hot air, takes its heat, and turns *all* of it into electricity for the scoreboard. No diesel. The air comes out a little cooler, that's all."

Kavya checks it against the first law. Energy in as heat, the same energy out as work. Nothing created, nothing destroyed. She can't find the flaw.

"And for the dressing room," Aditya goes on, "a fridge with no plug. Heat just flows out of the drinks into the warm room by itself."

Kavya frowns. The second idea sounds absurd; the first sounds almost reasonable. Yet out by the boundary, the club's generator is still burning diesel. If the first law allows both machines, what forbids them?

## The physics

The first law says energy is conserved. It says nothing about **which way** processes can run. The **second law of thermodynamics** adds that missing rule. It has two standard statements.

**Kelvin–Planck statement:** No process is possible whose sole result is the absorption of heat from a reservoir and the complete conversion of that heat into work.

**Clausius statement:** No process is possible whose sole result is the transfer of heat from a colder object to a hotter object.

![Two crossed-out machines: an engine turning all heat Q from a hot reservoir into work W equal to Q with no heat rejected, and a fridge moving heat Q from a cold reservoir to a hot one with no work](figures/second_law_thermodynamics/forbidden-machines.svg "Left: Aditya's scoreboard engine. Right: his plugless fridge. Both obey the first law; the second law rules out both.")

The words **sole result** matter. A gas expanding isothermally does turn all the heat it absorbs into work, but the gas ends up at a larger volume, so that is not the sole result; it cannot be repeated in a cycle without compressing the gas again. A fridge does move heat from cold to hot, but only by using work, so that is not the sole result either.

The two statements can be shown to be equivalent: a machine that broke one could be combined with an ordinary machine to break the other.

**Why no engine can be 100% efficient.** A heat engine runs a working substance in a cycle: it absorbs heat $Q_1$ from a hot reservoir, does work $W$ and rejects heat $Q_2$ to a cold one. Over a cycle $\Delta U = 0$, so $W = Q_1 - Q_2$, and its efficiency is $\eta = W/Q_1$. By the Kelvin–Planck statement, it cannot turn all of $Q_1$ into work, so it must reject some heat $Q_2 > 0$ to a colder reservoir. Therefore

$$\eta = 1 - \frac{Q_2}{Q_1} < 1$$

This is not about friction or poor engineering; even an ideal, reversible engine must reject heat. In the same way, by the Clausius statement, a refrigerator needs $W > 0$, so its coefficient of performance $\alpha = Q_2/W$ is finite.

That settles Aditya's inventions. His scoreboard engine takes heat from one reservoir, the air, and turns it all into work: forbidden by Kelvin–Planck. To extract work from the hot air at all, he would need a colder reservoir to reject heat into. His plugless fridge moves heat from cold drinks to a warmer room with nothing else happening: forbidden by Clausius.

## Worked example

**Given:** four claimed machines, per cycle (illustrative):
P: engine, absorbs $20\,\text{kJ}$, does $6\,\text{kJ}$ of work, rejects $14\,\text{kJ}$.
Q: engine, absorbs $20\,\text{kJ}$, does $8\,\text{kJ}$ of work, rejects $14\,\text{kJ}$.
R: engine, absorbs $20\,\text{kJ}$, does $20\,\text{kJ}$ of work, rejects nothing.
S: fridge, moves $5\,\text{kJ}$ from its cold inside to the room, using no work.
**Find:** which are possible, and which law each impossible one breaks.

P: $6 + 14 = 20\,\text{kJ}$ (first law obeyed), and heat is rejected. $\eta = 6/20 = 30\%$. **Possible.**
Q: $8 + 14 = 22\,\text{kJ} \neq 20\,\text{kJ}$. Energy out exceeds energy in: **breaks the first law.**
R: $20 = 20$ (first law obeyed), but all heat becomes work: **breaks the second law** (Kelvin–Planck).
S: energy is conserved, but heat goes from cold to hot as the sole result: **breaks the second law** (Clausius).

**Sanity check:** only P has both an energy balance and a rejected heat, $Q_2 > 0$; that is what every real engine needs.

## Where the picture breaks

The second law does not say how much heat must be rejected; the limit depends on the reservoir temperatures, which you may meet later through the ideal Carnot engine. Aditya's machine isn't hopeless in every form: a real engine *could* draw heat from hot air if it had a colder reservoir, such as deep cool ground, to reject heat into. It just can't run on one reservoir alone.

## Key takeaway

The second law says which processes can happen. Kelvin–Planck: no cyclic machine can turn all the heat it absorbs into work. Clausius: heat cannot flow from cold to hot by itself. So every engine must reject heat, $\eta = 1 - Q_2/Q_1 < 1$, and every refrigerator needs work.
