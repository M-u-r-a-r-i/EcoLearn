---
concept_id: second_law_thermodynamics
interest: gaming
format: explain
title: The self-powered PC that can never be built
check:
  question: |-
    A café owner is offered a "self-powered PC": a thermoelectric sheet over the exhaust vent takes $200\,\text{J}$ of heat per second from the hot exhaust air and returns $200\,\text{J}$ per second of electrical energy to the machine, with nothing else changing. What is wrong with it?
  options:
    A: |-
      Nothing — the energy taken in equals the energy given out, so it is allowed.
    B: |-
      It breaks the first law, because it creates energy out of nothing.
    C: |-
      Nothing in principle; it would work once the sheet was made of a material with no electrical resistance.
    D: |-
      It breaks the second law: no cyclic device can take heat from a single reservoir and turn all of it into work.
  answer: D
  explanation: |-
    The proposal balances energy exactly, so the first law is satisfied. What it claims is complete conversion of absorbed heat into work with no other effect, which is precisely what the Kelvin–Planck statement forbids. Some heat must be rejected to something colder.
  misconceptions:
    A: |-
      Treats energy conservation as the only rule. The first law says how much; the second law says which direction, and this machine is ruled out by the second.
    B: |-
      Blames the wrong law. $200\,\text{J}$ in and $200\,\text{J}$ out creates nothing, so the first law is obeyed.
    C: |-
      Thinks machines fall short of 100% only because of friction and resistance. Even a perfect, frictionless, resistance-free device must reject heat to a colder reservoir.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A gaming desk at night: a monitor showing GPU and CPU temperatures, a tower PC with a heat sink and fans, hot air leaving the top and cool air drawn in, a can of compressed-air duster, a mini fridge under the desk and a backup generator outside the window](scenes/gaming/thermodynamics.svg "All that hot air leaving the top of the tower is energy. Why can't the machine have it back?")

Yash has a plan, and he has drawn it on the back of his physics notebook.

"Look at where the heat goes," he says, holding a hand over the top of his tower, where the air comes off warm enough to feel from half a metre away. "That's energy. It came out of the wall socket and I'm just throwing it at the ceiling. So: a thermoelectric sheet over the vent. It takes that heat and turns it back into electricity. Feed it to the power supply. The PC runs on its own waste."

His friend Shruti, who has just finished the first-law chapter, checks it. Heat in, the same energy out as electrical work. Nothing created, nothing destroyed. She cannot find the flaw.

"And the mini fridge," Yash adds, warming up. "Unplug it. Heat just flows out of the drinks into the warm room on its own. Done."

Shruti frowns. The second idea is obviously ridiculous. The first sounds almost sensible. Yet the café down the road still pays an electricity bill, and every PC in it still has a fan.

If the first law permits both machines, what is it that forbids them?

## The physics

The first law says energy is conserved. It says nothing at all about **which way** a process can run. The **second law of thermodynamics** supplies that missing rule, and it has two standard statements.

**Kelvin–Planck statement:** No process is possible whose sole result is the absorption of heat from a reservoir and the complete conversion of that heat into work.

**Clausius statement:** No process is possible whose sole result is the transfer of heat from a colder body to a hotter body.

![Black-and-white portrait photograph of a bearded man in a dark coat](famous/rudolf-clausius.jpg "Rudolf Clausius (1822–1888), who put the second law in terms of the direction of heat flow, and later named entropy. Public domain, via Wikimedia Commons.")

![Two crossed-out machines: an engine turning all of the heat Q from a hot reservoir into work W equal to Q with nothing rejected, and a fridge moving heat Q from a cold reservoir to a hot one with no work put in](figures/second_law_thermodynamics/forbidden-machines.svg "Left: Yash's self-powered PC. Right: his unplugged fridge. Both balance the energy books; the second law rules out both.")

The words **sole result** are doing real work in those sentences. A gas expanding isothermally *does* turn all the heat it absorbs into work — but it ends up at a larger volume, so that is not the sole result, and it cannot be repeated without compressing the gas again. A refrigerator *does* move heat from cold to hot — but only by consuming work.

The two statements are equivalent: a machine violating one could be combined with an ordinary machine to violate the other.

**Why no engine can be 100% efficient.** A heat engine runs its working substance in a cycle, absorbing $Q_1$ from a hot reservoir, doing work $W$ and rejecting $Q_2$ to a cold one. Over a cycle $\Delta U = 0$, so $W = Q_1 - Q_2$ and $\eta = W/Q_1$. Kelvin–Planck forbids turning all of $Q_1$ into work, so $Q_2 > 0$ always, and therefore

$$\eta = 1 - \frac{Q_2}{Q_1} < 1$$

This has nothing to do with friction or sloppy engineering. Even an ideal, perfectly reversible engine must reject heat. In the same way, Clausius forbids $W = 0$ for a refrigerator, so its coefficient of performance $\alpha = Q_2/W$ is always finite.

That settles both of Yash's inventions. The self-powered PC takes heat from one reservoir — the exhaust air — and claims to turn all of it into work: forbidden by Kelvin–Planck. To get *any* work out of that warm air he would need something colder to reject heat into, and then he would recover only a fraction. The unplugged fridge moves heat from the cold drinks to the warmer room with nothing else happening: forbidden by Clausius.

## Worked example

**Given:** four machines are claimed, each per cycle (illustrative):
P — engine: absorbs $30\,\text{kJ}$, does $9\,\text{kJ}$ of work, rejects $21\,\text{kJ}$.
Q — engine: absorbs $30\,\text{kJ}$, does $12\,\text{kJ}$ of work, rejects $21\,\text{kJ}$.
R — engine: absorbs $30\,\text{kJ}$, does $30\,\text{kJ}$ of work, rejects nothing.
S — cooler: moves $4\,\text{kJ}$ from a cold box into a warm room, using no work.
**Find:** which are possible, and which law each impossible one breaks.

**P:** the energy balances, $9 + 21 = 30\,\text{kJ}$, and heat is rejected to a cold reservoir. Its efficiency is $9/30 = 30\%$. **Possible.**

**Q:** the energy does not balance: $12 + 21 = 33\,\text{kJ}$ comes out of $30\,\text{kJ}$ going in. **Breaks the first law.**

**R:** the energy balances, $30 = 30$, but every joule absorbed leaves as work with nothing rejected. **Breaks the second law** (Kelvin–Planck).

**S:** energy is conserved — the $4\,\text{kJ}$ simply arrives somewhere else — but it has gone from cold to hot as the sole result. **Breaks the second law** (Clausius).

**Sanity check:** the only survivor is the one that both balances its energy *and* has somewhere colder to dump heat into. That pair of requirements is what every real engine has to meet.

## Where the picture breaks

The second law as stated here says only that *some* heat must be rejected, not how much. The actual ceiling depends on the two reservoir temperatures, through the ideal Carnot engine you may meet later. Yash's idea is also not hopeless in every form: a thermoelectric sheet really can make electricity from an exhaust, because its other face sits in cooler room air — a second reservoir — but it recovers only a small fraction. What it can never do is run on one reservoir alone, or return more than it took.

## Key takeaway

The second law says which way processes can run. Kelvin–Planck: no cyclic machine can turn all the heat it absorbs into work. Clausius: heat will not flow from cold to hot by itself. So every engine must reject heat, making $\eta = 1 - Q_2/Q_1 < 1$, and every refrigerator must be paid for in work.
