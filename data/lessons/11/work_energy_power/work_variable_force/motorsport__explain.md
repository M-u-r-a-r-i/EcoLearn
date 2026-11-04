---
concept_id: work_variable_force
interest: motorsport
format: explain
title: Reading the energy off a crush test graph
check:
  question: |-
    A force acts along a kart's direction of motion. Its force–displacement graph is a straight line falling from $400\,\text{N}$ at $x = 0$ to $0\,\text{N}$ at $x = 5\,\text{m}$. How much work does this force do over those $5\,\text{m}$?
  options:
    A: |-
      $2000\,\text{J}$
    B: |-
      $80\,\text{J}$
    C: |-
      $0\,\text{J}$
    D: |-
      $1000\,\text{J}$
  answer: D
  explanation: |-
    The work is the area under the graph, here a triangle of base $5\,\text{m}$ and height $400\,\text{N}$: $W = \tfrac{1}{2} \times 5 \times 400 = 1000\,\text{J}$.
  misconceptions:
    A: |-
      Uses $W = Fd$ with the *largest* force, $400 \times 5$. That is the area of the whole rectangle, but the force only reaches $400\,\text{N}$ at the very start.
    B: |-
      Divides instead of multiplying ($400/5$). Work is force times distance, so the units must come out as $\text{N}\,\text{m}$, not $\text{N/m}$.
    C: |-
      Reads "the force ends at zero" as "no work done". The force was non-zero for almost the whole $5\,\text{m}$; only the last instant contributes nothing.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A race track scene: a car coasts down a hill road onto the circuit, a second car speeds along the straight with a velocity arrow, a third brakes with glowing red discs, and two people push a kart in the foreground](scenes/motorsport/work_energy_power.svg "Every car on this track carries a crushable nose designed to be destroyed once, slowly, on purpose.")

The scrutineering bay smells of resin. Nusrat is testing the crushable nose cone that has to sit in front of every car in the club's single-seater class: a cone of aluminium honeycomb, about half a metre long, that is supposed to fold up like a concertina in a crash instead of passing the impact on to the driver.

The rig pushes a flat plate into the cone, slowly, while a load cell records the force and a scale records how far the plate has moved. What comes out of the laptop is not a number. It is a graph — a line that climbs steeply as the honeycomb first buckles, runs almost flat across the middle as cell after cell folds at the same load, then drops away as the cone bottoms out.

Tanmay, who is holding the clipboard, wants one figure for the form. "Just tell me the force."

There isn't one. The force was different at every millimetre. So how do you get a single energy figure out of a line that never sits still?

## The physics

For a **constant** force along the motion, $W = Fd$ — the area of a rectangle on a graph of force against displacement. When the force **varies**, that rectangle is gone, but the area is not.

Cut the displacement into strips so narrow that within each one the force barely changes. Over a strip of width $\Delta x$ at a place where the force is $F(x)$, the work is very nearly $F(x)\,\Delta x$ — the area of a thin rectangle. Adding the strips gives the total:

$$W \approx \sum F(x)\,\Delta x$$

and in the limit of vanishingly narrow strips this sum becomes exact:

$$W = \int_{x_i}^{x_f} F(x)\,dx$$

which is precisely **the area under the force–displacement curve** between the start and the end.

![A force-displacement graph: force rises from zero, runs flat across the middle, then falls back to zero; dashed rectangular strips of equal width approximate the area under the line](figures/work_variable_force/area-under-force-displacement.svg "The area under the red line is the work. The dashed strips show the method: force times width, strip by strip, added up. The numbers here are a small-scale example — the shape is what matters.")

Three things to hold on to:

- **Only the component along the displacement counts.** If the force is at an angle, plot $F\cos\theta$ against $x$, not $F$.
- **Area below the axis is negative work.** A force that reverses direction takes energy back out.
- **You do not need a formula for $F(x)$.** A measured graph, or even graph paper and counting squares, gives the work just as well — which is exactly why Nusrat's rig plots one.

This is also the honest reason constant-force problems are a special case, not the general rule. Almost every real force — a spring, a tyre's grip, a crushing honeycomb, air drag — changes as things move.

## Worked example

**Given** (illustrative test values): the plate crushes the nose cone through a total of $0.5\,\text{m}$. The load rises from zero to a plateau of $20\,000\,\text{N}$, holds that plateau for $0.3\,\text{m}$, then falls back to zero at the end. So the graph is a trapezium: height $20\,000\,\text{N}$, base $0.5\,\text{m}$, flat top $0.3\,\text{m}$.
**Find:** the energy the nose cone absorbs.

The work is the area of that trapezium. A trapezium's area is the average of its two parallel sides times its height — here, the average of the base and the top, times the peak force:

$$W = \frac{0.5 + 0.3}{2} \times 20\,000 = 0.4 \times 20\,000 = 8000\,\text{J}$$

So the cone soaks up $8\,\text{kJ}$ — and notice what the shape is telling you. The *flat plateau* is the good part: it is where the structure is absorbing energy at the highest load it is allowed to reach. A cone that spiked to $40\,000\,\text{N}$ and then collapsed would enclose less area while hitting the driver twice as hard.

**Sanity check:** $8000\,\text{J}$ is roughly the work of lifting a $100\,\text{kg}$ motorcycle onto a roof eight metres up. Absorbing that much in half a metre of folding metal is a violent half-second, which is exactly what a crash is.

## Where the picture breaks

The rig crushes the cone slowly, over seconds; a real impact takes milliseconds, and honeycomb is not perfectly rate-independent, so the graph shifts a little at speed. The test is also strictly one-dimensional — plate straight on, nose straight back — while a real crash arrives at an angle and loads the structure in ways the rig never sees. And the area gives the energy *absorbed*, not the force felt by the driver: that depends on the plateau height, which is why regulations limit the peak as well as demanding the area. Finally, the graph says nothing about time. Two cones with identical areas can give completely different decelerations.

## Key takeaway

When a force varies, the work it does is the **area under its force–displacement graph**, $W = \int F(x)\,dx$, approximated as closely as you like by adding thin strips $F\,\Delta x$. No formula for the force is needed — a measured curve is enough. Area above the axis is positive work; area below it is negative.
