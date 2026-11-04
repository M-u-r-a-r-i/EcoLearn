---
concept_id: solenoid_field
interest: gaming
format: explain
title: The bang under the pinball playfield
check:
  question: |-
    A long solenoid is unwound and rewound so that it has the **same number of turns** spread over **twice the length**, carrying the same steady current. What happens to the magnetic field in the middle of it?
  options:
    A: |-
      It is unchanged, since the number of turns and the current are the same.
    B: |-
      It is halved.
    C: |-
      It is doubled.
    D: |-
      It falls to a quarter.
  answer: B
  explanation: |-
    Ampère's law gives $B = \mu_0 n I$, where $n = N/L$ is the number of turns **per metre**. Keeping $N$ and doubling $L$ halves $n$, so it halves the field.
  misconceptions:
    A: |-
      Thinks the total number of turns is what counts. It is the crowding of the turns that matters — the Amperian rectangle encloses fewer of them per metre when the coil is stretched out.
    C: |-
      Has the length the wrong way up, as though stretching a coil concentrated its field. Spreading the turns out thins the field; packing them tighter strengthens it.
    D: |-
      Applies an inverse-square law, as if the solenoid were a distant point source. Inside a long solenoid the field is directly proportional to $n$, so it only halves.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A gaming workbench with a bartop arcade cabinet, a cutaway of a pinball flipper coil showing the turns, the field along the axis and the iron plunger being pulled in, a controller with its shell off, a PC case fan, and a phone on a power cable](scenes/gaming/moving_charges_magnetism.svg "The middle panel is this lesson: a coil, a field along its axis, and an iron rod being snatched inwards.")

The pinball machine at the end of the arcade has been dead a week, and Ritika turns up on the afternoon the owner finally has it open.

The playfield is tilted up on its hinges like a car bonnet. Bolted to the wood underneath, the thing that works the left flipper is not a motor. It is a fat cylinder of copper wire — thousands of turns wound tight around a hollow tube — with an iron rod sitting half inside it and a short link from the rod to the flipper.

The owner presses the button. The rod is yanked inwards with a bang Ritika feels through the floor, and the flipper snaps up.

She counts the parts. A coil. A rod. No magnet anywhere. And a flipper that has to fling a steel ball the length of a table, thousands of times a night, for twenty years.

How much magnetic field can a coil of wire really make?

## The physics

A **solenoid** is a wire wound in a close helix: a stack of circular loops sharing one axis. Each loop makes its own field along that axis, and inside the coil they all point the same way, so they add. Outside, each loop's return field spreads over a huge volume and, for a long solenoid, very nearly cancels.

That gives the two facts a long solenoid is famous for: **the field inside is uniform and along the axis, and the field outside is almost zero.** Assume those and Ampère's law hands you the size in three lines.

![A long solenoid in cross-section, with current out of the page along the top turns and into the page along the bottom, a uniform field inside, almost none outside, and a rectangular Amperian loop with one side inside and one outside](figures/solenoid_field/solenoid-field-and-amperian-rectangle.svg "Only the side of the rectangle lying inside the coil contributes to the integral; the outside side sits where B is zero, and the two short sides are perpendicular to B.")

Draw a rectangular Amperian loop with one long side of length $l$ **inside** the coil, running along the axis, and the opposite side **outside**. Go once round:

- the inside side contributes $B\,l$, since $\vec{B}$ lies along it and is the same size all the way;
- the outside side contributes nothing, because $\vec{B} \approx 0$ out there;
- the two short sides contribute nothing, because there $\vec{B}$ is perpendicular to the path.

If the winding has $n$ turns per unit length, the rectangle encloses $n\,l$ turns, each carrying $I$, so $I_\text{enclosed} = n\,l\,I$. Ampère's law then gives

$$B\,l = \mu_0\,n\,l\,I \qquad\Longrightarrow\qquad \boxed{B = \mu_0 n I}$$

Look at what has vanished. The length $l$ cancelled, so the answer is the same wherever you put the rectangle — the field really is uniform. And the coil's **diameter** never appeared at all: a fat solenoid and a thin one with the same turns per metre give the same field inside.

Direction: curl the fingers of your right hand the way the current runs round the turns, and your thumb points along $\vec{B}$ inside. This holds for a **long**, closely wound, air-cored solenoid carrying a steady current; near the ends the field sags to about half its middle value.

## Worked example

**Given:** a flipper coil about $10\,\text{cm}$ long with $800$ turns, taking a pulse of $3.0\,\text{A}$.
**Find:** the magnetic field inside it.

**Step 1 — turns per metre.**

$$n = \frac{N}{L} = \frac{800}{0.10\,\text{m}} = 8000\ \text{turns per metre}$$

**Step 2 — the field.**

$$B = \mu_0 n I = (4\pi\times10^{-7})(8000)(3.0) \approx 3.0\times10^{-2}\,\text{T}$$

**Step 3 — picture it.** Thirty millitesla is about **six hundred times** the Earth's magnetic field — and the same at the centre of the tube as just inside the windings, and the same whether the tube is a centimetre wide or three.

**Sanity check:** a coil you can hold in one hand, making hundreds of times the Earth's field, is the right sort of size. It is nothing like a hospital scanner's magnet, and it is easily enough to snatch a light iron rod.

## Where the picture breaks

$B = \mu_0 n I$ is for an **air-cored** solenoid, and the flipper coil has an iron rod down the middle. Soft iron multiplies the field inside a coil by a large factor, and that is where most of the bang comes from. Why iron does this belongs to the next chapter; the honest position here is that $\mu_0 n I$ is the field the current alone would make.

"Long solenoid" is also generous for a flipper coil, which is stubby. The uniform-inside, zero-outside picture is exact only in the limit of a coil far longer than it is wide; at the open end where the rod sits, the field is spreading out and dropping, and it is precisely *that* non-uniform end region which grips the rod and drags it in. A uniform field would pull it nowhere.

And the coil cannot take that current for long. Hold the button down and a single winding would cook itself in seconds — which is why a real flipper coil carries a second, much finer winding that takes over and holds the flipper up on a far smaller current once the kick is done.

## Key takeaway

Inside a long, closely wound solenoid the magnetic field is uniform, along the axis, and of size $B = \mu_0 n I$, where $n$ is the number of turns **per metre**. Outside, it is very nearly zero. Ampère's law gets you there with one rectangular loop — and the answer depends on neither the coil's diameter nor where inside you measure.
