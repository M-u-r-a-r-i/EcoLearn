---
concept_id: potential_energy_conservative_forces
interest: motorsport
format: explain
title: The hill gives it back, the road never does
check:
  question: |-
    A car of mass $1000\,\text{kg}$ is driven from the paddock up to a viewpoint $50\,\text{m}$ higher, once by a short steep lane and once by a long gentle road. Take $g = 9.8\,\text{m/s}^2$. Which statement is correct?
  options:
    A: |-
      Gravity does more negative work on the long road, because the car travels much further.
    B: |-
      Gravity does $-490\,\text{kJ}$ on both routes, while friction and drag do more negative work on the long one.
    C: |-
      Gravity does $-490\,\text{kJ}$ on both routes, and friction does the same on both, because the start and end points are identical.
    D: |-
      Gravity does $-49\,\text{kJ}$ on both routes, since only the height gained matters.
  answer: B
  explanation: |-
    Gravity is conservative, so its work depends only on the height change: $-mgh = -(1000)(9.8)(50) = -490\,000\,\text{J}$ on either route. Friction and drag are non-conservative and charge for every metre travelled, so the longer road costs more.
  misconceptions:
    A: |-
      Treats gravity like friction, as if it billed by distance travelled. Gravity's work depends only on the change in height — the horizontal kilometres cost it nothing.
    C: |-
      Gets gravity right but extends path-independence to friction as well. That is exactly the property that separates conservative forces from non-conservative ones.
    D: |-
      Right idea, wrong arithmetic: $1000 \times 9.8 \times 50 = 490\,000\,\text{J}$, which is $490\,\text{kJ}$, not $49\,\text{kJ}$.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A race track scene: a car coasts down a hill road onto the circuit, a second car speeds along the straight with a velocity arrow, a third brakes with glowing red discs, and two people push a kart in the foreground](scenes/motorsport/work_energy_power.svg "The hill road at the left of the picture is a store of energy. Everything driven to the top of it can get that energy back.")

The club's hillclimb runs up an old ghat road, and the paddock is at the top. There are two ways up to it: the timed course itself, steep and short, and the public road that loops around the hill for five lazy kilometres.

Mehul drives up the long way with his fuel gauge under close observation, and arrives crosser than he left. "Five kilometres to gain the same hundred metres. That road robbed me."

Rohini took the steep lane and used noticeably less fuel, which Mehul finds insulting, because they are parked next to each other at exactly the same altitude.

Then, at the end of the day, both of them coast most of the way back down with the engine idling — and the car that went up the long way coasts just as far as the one that went up the steep way.

So the hill gave back the same to both of them, but the roads charged them differently. What is the difference between the two?

## The physics

Some forces keep a perfect account. A force is **conservative** if the work it does on a body moving between two points is the **same for every path** between them — equivalently, if the work it does around any closed loop is **zero**. Gravity and the force of an ideal spring are conservative. Friction, air drag and the push of an engine are **non-conservative**: their work depends on the route, and going out and back does not cancel.

![Two paths from A up to B: a short straight one and a long winding one. Gravity does minus m g h on both; friction does more negative work on the longer path](figures/potential_energy_conservative_forces/path-independence.svg "Gravity only cares about the height gained. Friction charges you for every metre of the route.")

Because a conservative force's work depends only on where you start and finish, you can attach a number to *position alone* and stop tracking paths. That number is the **potential energy** $U$, defined so that

$$W_\text{conservative} = -\Delta U = U_i - U_f$$

The minus sign is the bookkeeping: when a conservative force does positive work, the store goes down.

**Near the Earth's surface**, where $g$ is effectively constant, lifting a body of mass $m$ through a height $h$ means gravity does $-mgh$ of work, so the **gravitational potential energy** is

$$U = mgh$$

with $h$ measured from any level you choose. Only *changes* in $U$ have physical meaning, so pick the paddock, or sea level, or the pit lane floor — the differences come out the same. Conditions: this form needs $g$ constant, which is excellent over a hill and wrong over a satellite orbit.

Non-conservative forces get no potential energy, and that is the whole point. There is no "friction energy" you can look up from a position, because the road bill depends on how far you drove, not on where you ended up.

## Worked example

**Given** (illustrative): car plus driver $m = 1000\,\text{kg}$; the paddock at the top is $h = 100\,\text{m}$ above the start; $g = 9.8\,\text{m/s}^2$.
**Find:** the work gravity does on the way up, on the way down, and over the round trip.

*The store gained on the way up:*

$$\Delta U = mgh = 1000 \times 9.8 \times 100 = 980\,000\,\text{J}$$

So climbing the hill puts $980\,\text{kJ}$ into the gravitational store — by the steep lane or the long road, it makes no difference.

*Work done by gravity going up.* Gravity pulls down while the car rises, so its work is negative and equal to $-\Delta U$: $-980\,\text{kJ}$.

*Work done by gravity coming down:* $+980\,\text{kJ}$. Every joule is handed straight back, which is why both cars coast home.

*Round trip:* $-980 + 980 = 0\,\text{J}$. That zero is the definition of conservative, in one line.

Now the road. Suppose rolling resistance and drag together average about $400\,\text{N}$; over Mehul's $6\,\text{km}$ round trip that is $400 \times 6000 = 2.4\,\text{MJ}$ of negative work, and **none of it comes back**. Rohini's shorter route simply had fewer metres to be charged for.

**Sanity check:** $980\,\text{kJ}$ is the energy of lifting a whole car to the roof of a thirty-storey building — which is precisely what driving up a hundred-metre hill is.

## Where the picture breaks

Calling the hill a perfect energy store flatters it. Coasting back down, most of the returned $980\,\text{kJ}$ goes into drag and brake heat rather than speed, so you do not arrive at the bottom doing the $44\,\text{m/s}$ that a frictionless drop of $100\,\text{m}$ would give. An ordinary car cannot bank the energy at all; only an electric car with regenerative braking recovers a useful fraction, by running its motor as a generator, and even that loses some as heat in the process. The engine itself is non-conservative in a second sense too — it burns fuel whether the car climbs, cruises or idles at the top. And $U = mgh$ quietly assumes the car is a point at one height, which is fine for a hill and hopeless for anything the size of a mountain.

## Key takeaway

A **conservative** force does the same work along every path between two points, and zero work around a closed loop — so its effect can be stored as a **potential energy** $U$, with $W = -\Delta U$. Near the Earth's surface, gravitational potential energy is $U = mgh$, and only changes in it matter. Friction and drag are non-conservative: they bill you by the metre and return nothing.
