---
concept_id: motional_emf
interest: gaming
format: explain
title: The slide-bar controller with no sensor in it
check:
  question: |-
    The slide-bar controller reads $40\,\text{mV}$ when a player pushes the bar at $4\,\text{m/s}$. Which single change would make the reading $80\,\text{mV}$?
  options:
    A: |-
      Sliding the bar at $2\,\text{m/s}$ instead.
    B: |-
      Fitting magnets that give twice the field, at the same speed.
    C: |-
      Sliding at the same speed along twice the length of rail, so it takes twice as long.
    D: |-
      Using a bar of twice the mass, at the same speed.
  answer: B
  explanation: |-
    In $\varepsilon = Blv$, the emf is proportional to $B$, to $l$ and to $v$, each to the first power — so doubling the field at the same length and speed doubles the emf.
  misconceptions:
    A: |-
      Inverts the relation. The emf is proportional to $v$, so halving the speed halves the reading to $20\,\text{mV}$.
    C: |-
      Treats emf as something that piles up over time. Emf is not an amount of anything; a longer slide at the same speed gives the same voltage for longer, not a bigger one.
    D: |-
      Assumes a heavier bar carries "more push". Mass does not appear in $\varepsilon = Blv$ — only the field, the length across the rails and the speed.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A gaming corner at night: a pinball game on the monitor, a headset charging on a pad, a controller cut away at its rumble motor, a tablet pen hovering over a tablet, and an arcade coin chute with a magnet](scenes/gaming/electromagnetic_induction.svg "Five gaming machines. This lesson takes the simplest generator there is: one metal bar, moving.")

The arcade cabinet at the college fest is plywood, and Ishita and her team built everything in it, including the controller. There is no joystick. Along the front there are two brass rails and a loose aluminium bar lying across them. The sign says: **SLIDE THE BAR**.

Push the bar slowly and the car on the screen crawls. Shove it and the car leaps forward. Shove it harder and the car goes faster still. The game clearly knows how fast your hand moved.

By the third hour Ishita has been accused of cheating four times, so she takes the front panel off. There is no timer. No light gate, no switch at either end, no camera. Inside there is a pair of magnets sitting under the middle of the rails, two wires, and a small circuit board.

Nothing in that box measures time, and nothing touches the bar except the rails it rides on. So how does it know your speed?

## The physics

The bar, the two rails and the circuit board form one closed conducting loop. Push the bar along and you change the **area** of that loop, so the flux through it changes, and Faraday's law says there must be an emf. This particular case has its own name: **motional emf**.

![A conducting rod sliding along two rails in a field into the page, with the magnetic force pushing positive charges up the rod and a current flowing round the circuit](figures/motional_emf/rod-on-rails.svg "The rod is the battery: the magnetic force pushes positive charges to one end, and that separation of charge is the emf.")

There are two ways to see where it comes from, and they agree.

**From the charges.** Every free charge $q$ in the bar is carried along at speed $v$, so it feels a magnetic force $F = qvB$ (with $\vec{v}$ perpendicular to $\vec{B}$), directed along the bar. Positive charge piles up at one end and negative at the other. Moving a charge the whole length $l$ takes work $W = qvB \times l$, so the work per unit charge — which is what emf means — is

$$\varepsilon = Blv$$

**From Faraday's law.** In a time $\Delta t$ the bar sweeps out extra area $\Delta A = l\,v\,\Delta t$, so $\Delta\Phi_B = Blv\,\Delta t$ and $|\varepsilon| = \Delta\Phi_B/\Delta t = Blv$. Same answer.

This form holds when $\vec{B}$, the bar $l$ and the velocity $\vec{v}$ are **mutually perpendicular** and $B$ is uniform. Tilt the velocity and only the perpendicular component counts.

Now rearrange it, and Ishita's stall gives up its secret:

$$v = \frac{\varepsilon}{Bl}$$

With $B$ and $l$ fixed by the hardware, the voltage *is* the speed. A voltmeter, in this geometry, is a speedometer — no clock required.

And because the loop is closed, a current flows, so the bar feels a force opposing its motion (Lenz's law). That faint drag is the reason the bar never quite slides for free.

## Worked example

**Given:** the rails are $l = 0.05\,\text{m}$ apart, the field between the magnets is $B = 0.2\,\text{T}$, and a player shoves the bar through at $v = 4\,\text{m/s}$ — a brisk swipe.
**Find:** the emf across the bar.

The three quantities are mutually perpendicular, so $\varepsilon = Blv$. Take the hardware first:

$$Bl = 0.2\,\text{T} \times 0.05\,\text{m} = 0.01\,\text{T}\,\text{m}$$

That is what the bar gives at one metre per second — a hundredth of a volt per unit of speed.

At four metres per second:

$$\varepsilon = 0.01 \times 4 = 0.04\,\text{V}$$

Forty millivolts: about a fortieth of a torch cell, which is why the board amplifies it before the game reads it.

**Sanity check:** the units work, since $\text{T}\times\text{m}\times\text{m/s} = \text{V}$, and a small magnet with a hand-speed bar giving tens of millivolts is the right size — a bar that made volts by hand would be a power station.

## Where the picture breaks

The field is only strong in the short stretch between the magnets, not along the whole rail. So the bar does not give a steady $40\,\text{mV}$: it gives a brief blip as it crosses, and the board has to catch the peak. The uniform-$B$ assumption in $\varepsilon = Blv$ is an idealisation of that.

The rails and the sliding contacts have resistance too, and they are not clean — a smear of dust changes the reading. A real controller would use a sealed sensor for exactly that reason.

If the player pushes the bar crooked, so it does not lie square across the rails, the effective length between the contacts shrinks and the reading drops, which the formula only handles once you use the perpendicular component.

And the fit to gaming is honest but narrow: this is a home-built controller, not something you would find inside a shop-bought one. The physics is genuine; the cabinet is just where it happens to live.

## Key takeaway

A conductor of length $l$ moving with speed $v$ across a magnetic field $B$ — all three mutually perpendicular — is a source of emf, $\varepsilon = Blv$. The magnetic force on the moving charges is what separates them. Stop the motion and the emf vanishes at once; double the speed and it doubles.
