---
concept_id: second_law_thermodynamics
interest: motorsport
format: explain
title: The car that runs on hot air and can never be built
check:
  question: |-
    Four inventors describe the machines they want to fit to a race car. Which machine breaks the second law of thermodynamics but not the first?
  options:
    A: |-
      Each cycle, an engine takes $10\,\text{kJ}$ of heat from the hot exhaust and turns all $10\,\text{kJ}$ into work, rejecting no heat.
    B: |-
      Each cycle, an engine takes $10\,\text{kJ}$ of heat from the hot exhaust and delivers $12\,\text{kJ}$ of work.
    C: |-
      Each cycle, an engine takes $10\,\text{kJ}$ of heat from the hot exhaust, delivers $3\,\text{kJ}$ of work and rejects $7\,\text{kJ}$ to the air.
    D: |-
      Each cycle, a cooler uses $2\,\text{kJ}$ of work to move $5\,\text{kJ}$ of heat out of the cockpit and releases $7\,\text{kJ}$ to the hotter outside air.
  answer: A
  explanation: |-
    Machine A conserves energy ($10\,\text{kJ}$ in, $10\,\text{kJ}$ out), so the first law is satisfied, but turning all the heat into work with nothing rejected is exactly what the Kelvin–Planck statement forbids.
  misconceptions:
    B: |-
      Machine B does break a law, but it is the first law: $12\,\text{kJ}$ of work from $10\,\text{kJ}$ of heat creates energy. The question asks for a machine that is fine by the first law.
    C: |-
      Thinks a low efficiency, or any rejected heat, breaks a law. Rejecting heat is exactly what the second law demands; $3 + 7 = 10$, so the first law is satisfied too. This engine is allowed.
    D: |-
      Thinks heat can never go from cold to hot. The Clausius statement forbids it only when nothing else happens; here $2\,\text{kJ}$ of work is supplied, and $5 + 2 = 7\,\text{kJ}$ comes out, so it is an ordinary air conditioner.
author: claude-code/opus-5
written: 2026-09-25
---
## The story

![A pit lane in the afternoon sun: a stack of tyres in electric tyre blankets with a probe thermometer, a race car with a glowing front brake disc and a hot exhaust, and a compressed-air bottle feeding a wheel gun](scenes/motorsport/thermodynamics.svg "A hot afternoon: warm air everywhere, full of internal energy. Why can't a car simply run on it?")

Farah sends her cousin Rohan, who is in his second year of mechanical engineering, a video that has been going round her school's motorsport group. A confident man stands beside a gleaming prototype car. "Fuel is finished," he says. "The air around us is full of energy. My engine takes heat straight out of the warm air and turns every bit of it into motion. No fuel, no exhaust, no battery to charge. Cold air comes out of the back, and that's it."

"It sounds legit," Farah texts. "The air really is full of energy, right? We did internal energy last month. And he's not creating energy; he's just using what's there."

Rohan calls her back. "You're right that the air has energy, and you're right that he isn't breaking energy conservation. And his car still can't work."

"Then which law is he breaking?"

## The physics

The first law says energy is conserved. It does not say which way energy can flow, or how much heat can become work. The **second law of thermodynamics** does. It has two classic statements.

**Kelvin–Planck statement:** no process is possible whose sole result is the absorption of heat from a reservoir and the complete conversion of that heat into work.

**Clausius statement:** no process is possible whose sole result is the transfer of heat from a colder object to a hotter object.

![Two crossed-out machines: an engine turning all heat Q from a hot reservoir into work W equal to Q with no heat rejected, and a fridge moving heat Q from a cold reservoir to a hot one with no work](figures/second_law_thermodynamics/forbidden-machines.svg "Left: the air-powered car's engine. Right: an air conditioner with no power supply. Both obey the first law; the second law rules out both.")

The two statements can be proved equivalent: if you could build either forbidden machine, you could use it to build the other.

![Black-and-white portrait photograph of a bearded man in a dark coat](famous/rudolf-clausius.jpg "Rudolf Clausius (1822–1888), the German physicist who put the second law in terms of the direction of heat flow, and later named entropy. Public domain, via Wikimedia Commons.")

**Why no engine can be 100% efficient.** For a heat engine, $\eta = 1 - Q_2/Q_1$. An efficiency of 100% needs $Q_2 = 0$: all the heat absorbed turned into work, with nothing rejected. That is exactly what Kelvin–Planck forbids. So every heat engine must reject some heat to a colder reservoir, and $\eta < 1$ always. This is a law of nature, not a limit of today's engineering.

Now the video. The inventor's engine takes heat from one reservoir, the warm air, and turns it all into work. There is no colder reservoir for it to reject heat into. That is the forbidden machine on the left. His "cold air out of the back" does not rescue it: making the air colder than its surroundings, and getting work besides, is exactly the "sole result" the law rules out. A real engine needs *two* temperatures, a hot one to take heat from and a colder one to dump heat into, and work comes only from the heat flowing between them.

## Worked example

**Given (illustrative):** two engine designs, each per cycle.
Design 1 (the video): absorbs $Q_1 = 50\,\text{kJ}$ from the air and delivers $W = 50\,\text{kJ}$ of work, rejecting nothing.
Design 2 (a real petrol engine): absorbs $Q_1 = 50\,\text{kJ}$ from burning fuel and rejects $Q_2 = 35\,\text{kJ}$ to the air.
**Find:** whether each obeys the first and second laws, and the efficiency of Design 2.

**Step 1: Design 1 and the first law.** Over a cycle $\Delta U = 0$, so the first law needs $W = Q_1 - Q_2 = 50 - 0 = 50\,\text{kJ}$. It matches: the first law is happy.

**Step 2: Design 1 and the second law.** It rejects no heat, so $\eta = 50/50 = 100\%$. Kelvin–Planck forbids this: the design is impossible.

**Step 3: Design 2.** The work is $W = 50 - 35 = 15\,\text{kJ}$, so

$$\eta = \frac{15}{50} = 0.30 = 30\%$$

Less than a third of the heat becomes work, and the rest must go to the cooler air. Both laws are satisfied: this is an engine you can actually build.

**Sanity check:** the only difference between the two designs is the heat rejected, and the second law says that is the one number that can never be zero.

## Where the picture breaks

The video's machine is imaginary, and no real car is being described. Real petrol engines are internal combustion engines, not two fixed reservoirs, so the 30% is an illustrative round figure. A car *can* get energy from warm surroundings in one genuine way: a heat pump uses work to move heat from colder outside air into a warmer cabin. That obeys the second law because work is supplied. The second law also sets a hard upper limit on efficiency that depends only on the two temperatures; that result belongs to an ideal engine called the Carnot engine, which is beyond this lesson.

## Key takeaway

Kelvin–Planck: no engine can turn all the heat it absorbs into work. Clausius: heat never flows from cold to hot on its own. Both mean every heat engine must reject some heat to a colder reservoir, so its efficiency $\eta = 1 - Q_2/Q_1$ is always less than 100%. The first law says energy is conserved; the second says which way it can go.
