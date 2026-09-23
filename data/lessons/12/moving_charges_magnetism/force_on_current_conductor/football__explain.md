---
concept_id: force_on_current_conductor
interest: football
format: explain
title: The flag that makes a watch jump
check:
  question: |-
    A straight wire of length $0.20\,\text{m}$ carries a current of $3.0\,\text{A}$ at right angles to a uniform field of $0.50\,\text{T}$, and feels a force of $0.30\,\text{N}$. The wire is now turned until it lies **along** the field lines, with the same current flowing. The force on it becomes
  options:
    A: |-
      $0.30\,\text{N}$ still — the force does not depend on which way the wire points.
    B: |-
      zero.
    C: |-
      $0.30\,\text{N}$, but pushing the opposite way.
    D: |-
      larger than $0.30\,\text{N}$, because the wire is now lined up with the field.
  answer: B
  explanation: |-
    $F = BIL\sin\theta$, and a wire lying along the field has $\theta = 0$, so $\sin\theta = 0$ and the force vanishes. Only the part of the wire that cuts across the field feels a push.
  misconceptions:
    A: |-
      Remembers $F = BIL$ without the $\sin\theta$, and treats the force as a fixed property of the wire and the field rather than of their relative direction.
    C: |-
      Thinks turning the wire simply reverses the push. Reversing the force needs the *current* or the *field* reversed; turning the wire to lie along $\vec{B}$ removes the force altogether.
    D: |-
      Imports the idea that things line up with a field and are pulled along it, as a compass needle is. A current-carrying wire is pushed sideways, at right angles to both $I$ and $\vec{B}$, and feels nothing at all when it lies along the field.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A football ground with a coil traced around the goal frame, a pop-up sprinkler on a solenoid valve, an electric line-marking machine and a horn speaker on a pole with a compass lying on its supply cable](scenes/football/moving_charges_magnetism.svg "The horn speaker on the pole turns a current into a push, thousands of times a second.")

Imran is running the line at a school tournament, and he has been handed a flag with a button in the handle. Press it, the tournament director said, and the referee will know — even with two hundred people shouting.

He does not believe it. The referee is sixty metres away with his back turned, and Imran can see no wire, no lamp, no siren.

Late in the first half a striker strays half a metre offside. Imran raises the flag and presses. Nothing happens on his side at all: no click, no light, no sound. But across the pitch the referee stops dead, turns, and points for the free kick.

Afterwards the referee shows him the watch — the buzz came from there, a sealed box the size of a matchbox with no moving part you can see. Something inside it shoved hard enough to be felt through a wrist strap. So what, inside a sealed box, does the shoving?

## The physics

A wire carrying a current is full of charges in motion, and you already know a magnetic field pushes a moving charge. Add up that push over all the charges in a straight length $L$ of wire and you get a force on the wire itself:

> $$\vec{F} = I\,\vec{L} \times \vec{B}, \qquad F = BIL\sin\theta$$
> where $\vec{L}$ points along the wire in the direction of the conventional current, and $\theta$ is the angle between the wire and $\vec{B}$.

![A straight wire carrying current across a field into the page, with the force upwards; and the same wire tilted at an angle theta to the field, giving F = BIL sin θ](figures/force_on_current_conductor/force-on-current-wire.svg "Only the part of the wire that lies across the field counts: the force is greatest at 90° and vanishes when the wire lies along B.")

Three things to hold on to.

- **Direction.** Fingers of the right hand along the current, curl them towards $\vec{B}$; the thumb gives the force. It is perpendicular to the wire *and* to the field — never along either of them.
- **Only the crossing part counts.** $\sin\theta$ makes the force largest when the wire cuts straight across the field and zero when it lies along it.
- **Reverse either one and the push reverses.** Flip the current, or flip the field, and the force turns around. Flip both and it comes back to where it was.

That last line is the whole of a loudspeaker, and of the buzzer in the referee's watch. A coil of wire sits in the narrow gap of a small permanent magnet, so the field across it is fixed. Feed a current one way and the coil is shoved one way; reverse the current and it is shoved back. Reverse it a few hundred times a second and the coil, with a small weight or a diaphragm attached, hammers back and forth — a buzz you feel, or a sound you hear, with nothing visibly moving.

The condition of validity is worth stating: $F = BIL$ assumes the field is **uniform along that length** of wire and the wire is straight. For a bent wire, or a field that varies, you must add up the contributions piece by piece.

## Worked example

**Given:** a straight length $L = 0.20\,\text{m}$ of the coil's wire lies in a field $B = 0.50\,\text{T}$ and carries $I = 3.0\,\text{A}$, at right angles to the field.
**Find:** the force on it, and what is left of that force if the wire is tilted to $30°$ from the field.

**Step 1 — at right angles.** Here $\sin 90° = 1$:

$$F = BIL = (0.50)(3.0)(0.20) = 0.30\,\text{N}$$

That is about a fourteenth of the weight of a match ball — a small push, but it is acting on a coil weighing a few grams, so it moves it briskly.

**Step 2 — tilted to $30°$.** Now $\sin 30° = 0.5$, so the force is half as big: $0.15\,\text{N}$. The wire has not changed, the current has not changed, the field has not changed — only the part of the wire that cuts across the field has.

**Sanity check:** the force falls smoothly to zero as the wire swings into line with the field, which is exactly what $\sin\theta$ should do.

## Where the picture breaks

The buzzer's wire is not the straight segment in the diagram. It is a coil wound round and round, and the magnet's field in the gap is shaped so that the pushes on every turn point the same way and add up. Straightening the picture makes the equation usable but hides why a coil of a hundred turns pushes a hundred times harder than one.

The equation also treats the force as acting on "the wire", when strictly the field pushes the moving charges, and they drag the metal along through collisions with it. That distinction does not change the answer, but it is why the force appears on the wire even though only the electrons are moving.

Some watches buzz using a tiny motor with an off-centre weight instead of a coil in a gap. The equation is the same one; it makes a twist rather than a shove, which is the topic of a later lesson in this chapter.

## Key takeaway

A current-carrying wire in a magnetic field is pushed sideways: $\vec{F} = I\,\vec{L} \times \vec{B}$, of size $BIL\sin\theta$, perpendicular to both the wire and the field. The push is greatest when the wire crosses the field at right angles and zero when it lies along it, and reversing either the current or the field reverses it.
