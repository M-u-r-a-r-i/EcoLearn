---
concept_id: second_law_thermodynamics
interest: football
format: explain
title: The floodlight generator that can never be built
check:
  question: |-
    An inventor claims a generator for floodlights that absorbs $25\,\text{kJ}$ of heat from the warm evening air in each cycle and delivers $25\,\text{kJ}$ of electrical work, rejecting no heat at all. Which judgement is correct?
  options:
    A: |-
      Impossible: it breaks the Kelvin–Planck statement, because some heat must be rejected to a colder body.
    B: |-
      Possible, because the energy delivered equals the energy absorbed, so energy is conserved.
    C: |-
      Impossible, because it breaks the first law by delivering more energy than it takes in.
    D: |-
      Possible in principle, once all the friction inside the machine has been eliminated.
  answer: A
  explanation: |-
    The claim obeys the first law ($25\,\text{kJ}$ in, $25\,\text{kJ}$ out), but taking heat from one reservoir and converting all of it into work, with nothing else happening, is exactly what the Kelvin–Planck statement forbids.
  misconceptions:
    B: |-
      Treats energy conservation as the only rule a machine must obey. The first law is satisfied here; it is the second law that the claim breaks.
    C: |-
      Blames the wrong law. Input and output are both $25\,\text{kJ}$, so no energy is created and the first law is untouched.
    D: |-
      Thinks engines fall short of $100\%$ only because of friction and rough engineering. Even a perfect, frictionless, reversible engine must reject heat to a colder reservoir.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A training ground on a hot day: a board reading 36 degrees Celsius, an ice box of drinks, a player inflating a ball with a hand pump, and a mower with a hot exhaust](scenes/football/thermodynamics.svg "The air here is at 36 °C and full of thermal energy. The club still pays for fuel. Why?")

The club's evening session runs on floodlights, and the floodlights run on a diesel generator, and the diesel bill is the reason Ravi's uncle keeps threatening to close the ground.

Ravi, who is halfway through Class 11, sketches a solution on the back of a team sheet. "Look at all this heat," he says, waving at the shimmering pitch. "The air out there is at thirty-six degrees. It is *full* of energy. My machine pulls the warm air in, takes the heat, and turns all of it into electricity. The air comes out a little cooler. No diesel, no bill."

His teacher, Sunita, reads it twice and cannot fault the energy accounting. Heat in, the same amount of energy out as work. Nothing created, nothing destroyed.

"And for the drinks," Ravi adds, "a crate that cools itself. Heat just leaves the bottles and goes into the warm store room, no plug needed."

Sunita laughs at the second one immediately. The first one she cannot laugh at — and yet out by the fence, the generator is still burning diesel. If the first law allows both machines, what is stopping them?

## The physics

The first law says energy is conserved. It says nothing at all about **which way** a process is allowed to run. The **second law of thermodynamics** supplies that missing rule, in two standard statements.

**Kelvin–Planck statement:** No process is possible whose sole result is the absorption of heat from a reservoir and the complete conversion of that heat into work.

**Clausius statement:** No process is possible whose sole result is the transfer of heat from a colder body to a hotter body.

![Black-and-white portrait photograph of a bearded man in a dark coat](famous/rudolf-clausius.jpg "Rudolf Clausius (1822–1888), who put the second law in terms of the direction of heat flow and later named entropy. Public domain, via Wikimedia Commons.")

![Two crossed-out machines: an engine turning all heat Q from a hot reservoir into work W equal to Q with no heat rejected, and a fridge moving heat Q from a cold reservoir to a hot one with no work](figures/second_law_thermodynamics/forbidden-machines.svg "Left: Ravi's floodlight generator. Right: his self-cooling crate. Both obey the first law; the second law rules out both.")

The words **sole result** carry the weight. A gas expanding isothermally does turn all the heat it absorbs into work — but it ends up occupying a larger volume, so that is not the sole result, and it cannot be repeated without compressing the gas again. A refrigerator does move heat from cold to hot — but only by consuming work, so that is not the sole result either.

The two statements look unrelated and are in fact equivalent: a machine breaking one could be coupled to an ordinary machine to break the other.

**Why no engine reaches $100\%$.** An engine absorbs $Q_1$ from a hot reservoir, does work $W$ and rejects $Q_2$ to a cold one, with $\Delta U = 0$ over a cycle, so $W = Q_1 - Q_2$ and $\eta = W/Q_1$. Kelvin–Planck forbids turning all of $Q_1$ into work, so $Q_2 > 0$ always, and

$$\eta = 1 - \frac{Q_2}{Q_1} < 1$$

This has nothing to do with friction or sloppy building: even an ideal reversible engine must throw heat away. In the same way, Clausius forces a refrigerator to use $W > 0$, so its coefficient of performance $\alpha = Q_2/W$ stays finite.

That settles both of Ravi's inventions. The generator takes heat from a single reservoir — the air — and turns all of it into work: forbidden by Kelvin–Planck. The self-cooling crate moves heat from cold bottles to a warmer room with nothing else happening: forbidden by Clausius.

## Worked example

**Given:** four machines are claimed, each per cycle (illustrative):
P: engine, absorbs $30\,\text{kJ}$, does $9\,\text{kJ}$ of work, rejects $21\,\text{kJ}$.
Q: engine, absorbs $30\,\text{kJ}$, does $12\,\text{kJ}$ of work, rejects $21\,\text{kJ}$.
R: engine, absorbs $30\,\text{kJ}$, does $30\,\text{kJ}$ of work, rejects nothing.
S: chiller, moves $8\,\text{kJ}$ from the cold drinks to the warmer room, using no work.
**Find:** which are possible, and which law each impossible one breaks.

P: $9 + 21 = 30\,\text{kJ}$, so the energy balances, and heat is rejected. $\eta = 9/30 = 30\%$. **Possible.**

Q: $12 + 21 = 33\,\text{kJ}$, but only $30\,\text{kJ}$ went in. Energy would be created: **breaks the first law.**

R: $30 = 30$, so energy balances — but all the heat absorbed becomes work: **breaks the second law** (Kelvin–Planck).

S: energy balances too, yet heat moves from cold to hot as the sole result: **breaks the second law** (Clausius).

**Sanity check:** only P has both a balanced energy account *and* some heat thrown away, which is exactly the pair of conditions every real engine satisfies.

## Where the picture breaks

The second law as stated here says only that $Q_2 > 0$, not how large it has to be; the actual limit depends on the reservoir temperatures, through the ideal Carnot engine you may meet later. Ravi's idea is not hopeless in every form either: a machine really could draw heat from the warm evening air if it had something colder — deep cool ground, say — to reject heat into. What it cannot do is run on one reservoir alone. And notice that neither statement mentions football, floodlights or diesel: they are claims about every machine ever built.

## Key takeaway

The second law decides which processes can actually happen. Kelvin–Planck: no cyclic machine can convert all the heat it absorbs into work. Clausius: heat will not flow from cold to hot by itself. So every engine must reject heat, giving $\eta = 1 - Q_2/Q_1 < 1$, and every refrigerator needs work.
