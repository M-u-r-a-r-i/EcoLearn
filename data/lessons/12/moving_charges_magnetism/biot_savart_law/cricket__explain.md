---
concept_id: biot_savart_law
interest: cricket
format: explain
title: The loop of wire under the stand
check:
  question: |-
    A very short current element of length $dl$ carries a current $I$. At which nearby point does this element produce **no** magnetic field at all?
  options:
    A: |-
      At a point directly to the side of it, on the perpendicular through its middle.
    B: |-
      At a point straight ahead of it, on the line of the element itself.
    C: |-
      At a point on a line at $45°$ to the element.
    D: |-
      Nowhere — at a given distance the element's field is the same in every direction.
  answer: B
  explanation: |-
    $dB \propto \sin\theta$, and straight ahead of the element $\theta = 0$, so $\sin\theta = 0$. A current element sends out no field along its own direction.
  misconceptions:
    A: |-
      Swaps the roles of the angle. At $90°$, $\sin\theta = 1$ — that is where the element's field is *strongest*, not zero.
    C: |-
      Guesses that "in between" means "cancels". $\sin 45°$ is about $0.7$: the field there is real, just smaller than at $90°$.
    D: |-
      Treats the current element like a point charge, whose field has the same size in all directions. The Biot–Savart field depends strongly on direction, through both $\sin\theta$ and the cross product.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A cricket ground with an electric roller, a compass lying on a thick power cable, a bowling machine and a loudspeaker on a pole](scenes/cricket/moving_charges_magnetism.svg "The public address system on this ground can also be fed into a loop of wire hidden under the stand.")

Ayesha's grandmother has watched the club's matches from the same seat for thirty years, and for the last two she has not heard a word of the commentary. Her hearing aid whistles; the loudspeakers echo off the pavilion wall.

So the club is fitting a **hearing loop**: a single thick wire buried around the edge of the seating, carrying the commentary as a current. A hearing aid switched to its telecoil setting picks the sound straight out of the magnetic field the loop makes — no echo, no crowd noise.

The electrician is crouched over a plan of the stand, arguing with himself about where the corners should go. Ayesha offers the one rule she knows: grip the wire, thumb along the current, fingers give the field.

"That tells me which way it points," he says. "It doesn't tell me how strong it is in row F. And this wire isn't straight."

## The physics

The grip rule is a direction rule, and only for a long straight wire. To get sizes, and to handle wire of any shape, you need the law underneath it — found by **Jean-Baptiste Biot** and **Félix Savart** in 1820, within months of Oersted's discovery.

Their idea was to cut the circuit into pieces so short they count as straight, find the field of one piece, and add up all the pieces.

![A short element of a current-carrying wire, the vector r to a point P, the angle theta between them, and the resulting dB into the page at P](figures/biot_savart_law/current-element-dB.svg "One short piece of wire, one contribution. The whole field is the sum over every piece of the circuit.")

For a current element $I\,d\vec{l}$, the field it contributes at a point $P$ a distance $r$ away is

$$d\vec{B} = \frac{\mu_0}{4\pi}\,\frac{I\,d\vec{l} \times \hat{r}}{r^{2}}$$

with magnitude

$$dB = \frac{\mu_0}{4\pi}\,\frac{I\,dl\,\sin\theta}{r^{2}}$$

where $\theta$ is the angle between the element and the line to $P$, and $\hat{r}$ is the unit vector along that line. The constant is the **permeability of free space**,

$$\frac{\mu_0}{4\pi} = 10^{-7}\,\text{T}\,\text{m}/\text{A}$$

Read the formula as four separate statements:

- **Proportional to $I\,dl$** — more current, or a longer piece, gives more field.
- **Inverse square in $r$** — twice as far, a quarter as much.
- **$\sin\theta$** — an element gives its biggest contribution sideways, and *nothing at all* straight ahead along its own direction.
- **The direction is $d\vec{l} \times \hat{r}$** — perpendicular to both, which is what makes field lines wrap around a wire instead of spreading out from it.

The total field is the sum over the whole circuit, $\vec{B} = \sum d\vec{B}$, taken as a vector sum. That is where every other formula in this chapter comes from, including the straight-wire result and the loop in the next lesson. It holds in free space (and in air, near enough), for steady currents.

## Worked example

**Given:** a straight cable carries $10\,\text{A}$. Take one small piece of it $1.0\,\text{mm}$ long, and a point $P$ that is $0.10\,\text{m}$ away, square-on to that piece ($\theta = 90°$).
**Find:** the field that one piece contributes at $P$, and how it compares with the whole wire's field there.

**Step 1 — the one piece.**

$$dB = 10^{-7} \times \frac{(10)(1.0 \times 10^{-3})(1)}{(0.10)^{2}} = 10^{-7}\,\text{T}$$

A tenth of a microtesla: a couple of thousandths of the Earth's field, from a millimetre of wire.

**Step 2 — compare with the whole wire.** The complete long straight wire gives $2 \times 10^{-5}\,\text{T}$ at that distance (you will derive this two lessons from now). That is about **200 times** the single piece.

So a wire metres long behaves like roughly 200 of these millimetres. The rest contribute almost nothing, because they are further away (the $1/r^{2}$) and badly angled (the $\sin\theta$). **Nearly all of the field at a point comes from the stretch of wire closest to it.**

**Sanity check:** that is why the electrician cares where the *near* side of the loop runs and barely at all about the far side.

## Where the picture breaks

The diagram shows a single current element sitting on its own, and that is a fiction. Steady current cannot start and stop in mid-air; it must go round a closed circuit. So $d\vec{B}$ can never be measured by itself — only the total from a complete loop can. The law is tested by its sums, not its pieces.

It is also worth noticing how unlike Coulomb's law this is. Both fall off as $1/r^{2}$, but a charge's field points straight out along $\hat{r}$, while this one points *across* it, and dies away along the element's own direction. That single difference is why magnetic field lines close on themselves.

For Ayesha's grandmother, one more caution: the loop's field is far from even. It is strong near the wire and weaker in the middle of the stand, which is exactly the problem the electrician was chewing over.

## Key takeaway

The Biot–Savart law gives the field of one short piece of current: $dB = \dfrac{\mu_0}{4\pi}\dfrac{I\,dl\sin\theta}{r^{2}}$, directed along $d\vec{l} \times \hat{r}$. Add up the contributions of every piece of a circuit and you have its whole magnetic field — which is where all the standard results in this chapter come from.
