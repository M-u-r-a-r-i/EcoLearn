---
concept_id: second_law_thermodynamics
interest: smartphones
format: explain
title: The phone case that promised to charge from room heat
check:
  question: |-
    An inventor claims his new engine for a portable generator converts all the heat it absorbs from burning fuel into work, because he has removed every source of friction. What does the second law of thermodynamics say about this claim?
  options:
    A: |-
      It is possible in principle; real engines fall short of 100% only because of friction and other losses.
    B: |-
      It is impossible: any heat engine must reject some heat to a colder reservoir, so its efficiency is less than 100%.
    C: |-
      It is impossible, because turning all the heat into work would create energy and break energy conservation.
    D: |-
      It is possible, as long as the burning fuel keeps the hot reservoir at a high enough temperature.
  answer: B
  explanation: |-
    By the Kelvin–Planck statement, no process can have as its sole result the absorption of heat from a reservoir and its complete conversion into work. Every heat engine must reject some heat $Q_2$ to a colder reservoir, so $\eta = 1 - Q_2/Q_1 < 1$, even with no friction at all.
  misconceptions:
    A: |-
      Thinks the limit on efficiency is only an engineering problem of friction and losses. Even a perfect, frictionless engine must reject heat; that limit comes from the second law itself.
    C: |-
      Right conclusion, wrong reason. Turning $Q$ joules of heat into $Q$ joules of work conserves energy perfectly, so the first law allows it; it is the second law that forbids it.
    D: |-
      Thinks a hotter source can make the rejected heat zero. A hotter source can raise the efficiency, but some heat must always be rejected to a colder reservoir, so it never reaches 100%.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A sunny room: a phone sealed in a puffed-up waterproof pouch on a windowsill, a phone charging on a desk seen through a clip-on thermal camera, an icy can of compressed air, and a wall air conditioner controlled from a phone app](scenes/smartphones/thermodynamics.svg "A room full of warm air and warm gadgets. Could that warmth alone charge a phone?")

Harpreet is scrolling through videos late at night when an advert stops her thumb. A smiling presenter holds up a sleek phone case. *Never charge again! Our case captures the heat energy all around you, in the air of your room, and turns it into electricity. No sun needed. No plug. Just warmth.*

"The air in my room is full of energy," she says to her cousin Manav, who is revising for his Class 11 exams. "Molecules zooming around at hundreds of metres a second. That's true, right?"

"True," Manav admits.

"And energy can be converted from one form to another. Also true."

"Also true."

"So the case works."

Manav opens his mouth, stops, and frowns. Everything she said is correct. The case wouldn't create any energy; it would only convert some. Yet he is sure the advert is nonsense. Which law does it break?

## The physics

The first law says energy is conserved. It does not say which way energy can flow, or how much heat can become work. The **second law of thermodynamics** does. It has two classic statements.

**Kelvin–Planck statement:** no process is possible whose sole result is the absorption of heat from a reservoir and the complete conversion of that heat into work.

**Clausius statement:** no process is possible whose sole result is the transfer of heat from a colder object to a hotter object.

![Two crossed-out machines: an engine turning all heat Q from a hot reservoir into work W equal to Q with no heat rejected, and a fridge moving heat Q from a cold reservoir to a hot one with no work](figures/second_law_thermodynamics/forbidden-machines.svg "Left: the room-heat phone case. Right: an air conditioner with no power supply. Both obey the first law; the second law rules out both.")

The two statements can be proved equivalent: if you could build either forbidden machine, you could use it to build the other.

![Black-and-white portrait photograph of a bearded man in a dark coat](famous/rudolf-clausius.jpg "Rudolf Clausius (1822–1888), who put the second law in terms of the direction of heat flow, and later named entropy. Public domain, via Wikimedia Commons.")

**Why no engine can be 100% efficient.** For a heat engine, $\eta = 1 - Q_2/Q_1$. An efficiency of 100% needs $Q_2 = 0$: all the heat absorbed turned into work, with nothing rejected. That is exactly what Kelvin–Planck forbids. So every heat engine must reject some heat to a colder reservoir, and $\eta < 1$ always. This is a law of nature, not a limit of today's engineering.

Now the advert. The case sits in a room where everything is at one temperature. It would take heat from a single reservoir, the room air, and turn it into electrical work, with nowhere colder to reject any heat. That is the forbidden machine on the left. Energy in the room is plentiful; what the case lacks is a *temperature difference*. Work can be drawn only from heat flowing from hotter to colder.

## Worked example

**Given (illustrative):** two gadgets.
Gadget 1 (the advert): takes $100\,\text{J}$ of heat from room air and delivers $100\,\text{J}$ of electrical energy, rejecting nothing.
Gadget 2 (a real thermoelectric wristband): sits between warm skin and cooler air, takes $100\,\text{J}$ of heat from the skin, and rejects $99\,\text{J}$ to the air.
**Find:** whether each obeys the first and second laws, and the efficiency of Gadget 2.

**Step 1: Gadget 1 and the first law.** Energy in, $100\,\text{J}$; energy out, $100\,\text{J}$. The first law is happy.

**Step 2: Gadget 1 and the second law.** It rejects no heat, so $\eta = 100/100 = 100\%$, from a single temperature. Kelvin–Planck forbids this: the gadget is impossible.

**Step 3: Gadget 2.** The electrical work is $W = 100 - 99 = 1\,\text{J}$, so

$$\eta = \frac{1}{100} = 1\%$$

Only one joule in a hundred becomes electricity, a trickle, but a real one, because the skin is warmer than the air. Both laws are satisfied.

**Sanity check:** the only difference between the two gadgets is the rejected heat and the need for two temperatures, and the second law says those are exactly what can never be left out.

## Where the picture breaks

A thermoelectric band is not a piston engine running in cycles; it is a solid device with no moving parts. But it is still a heat engine in the second law's sense: heat flows through it from hot to cold, and a little of that flow becomes work. Skin and room air differ by only about ten degrees, so even a perfect device could turn only a few percent of the heat into work, and real ones manage only a fraction of that; the $1\%$ here is illustrative. None of this rescues the advert: with no temperature difference at all, the second law allows zero.

## Key takeaway

Kelvin–Planck: no process can turn heat from a single reservoir entirely into work. Clausius: heat cannot, by itself, flow from colder to hotter. So every engine must reject some heat to a colder reservoir, and no engine can be 100% efficient. Work comes from heat only when it flows between two temperatures.
