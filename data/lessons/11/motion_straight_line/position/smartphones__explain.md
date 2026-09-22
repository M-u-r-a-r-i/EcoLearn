---
concept_id: position
interest: smartphones
format: explain
title: Three kilometres or forty-seven, where is the fuel station
check:
  question: |-
    A delivery app tracks a rider on a straight road. Its origin is the restaurant, with the positive direction pointing towards the customer's building, which is at $x = +900\,\text{m}$. The rider is at $x = +350\,\text{m}$. The customer's own app describes the same road with the origin at her building and the positive direction pointing towards the restaurant. What is the rider's position in the customer's description?
  options:
    A: |-
      $x' = +350\,\text{m}$
    B: |-
      $x' = -550\,\text{m}$
    C: |-
      $x' = +550\,\text{m}$
    D: |-
      $x' = +1250\,\text{m}$
  answer: C
  explanation: |-
    Measured from the customer's building, the rider is $900 - 350 = 550\,\text{m}$ away, towards the restaurant — which is the new positive direction. So $x' = +550\,\text{m}$.
  misconceptions:
    A: |-
      Thinks a position belongs to the rider, so it stays the same when the origin moves. A position is always measured from a chosen origin.
    B: |-
      Gets the right size but gives it a minus sign, forgetting that the new positive direction points towards the restaurant — the side the rider is on.
    D: |-
      Adds the two numbers, $900 + 350$, as if the rider were on the far side of the restaurant. The rider is between the two buildings, so the distances subtract.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![An evening street: a phone shows a live-tracking map of a straight road, while a delivery scooter rides past kilometre markers](scenes/smartphones/motion_straight_line.svg "A map app, a road, and numbered kilometre markers: three different ways of saying where things are along one line.")

The family car is on a long, straight highway, and the tank is nearly empty. Ritvik's father asks him to find a fuel station.

Ritvik checks the navigation app on the dashboard phone. "Fuel station in three kilometres."

His sister Sana has an offline map open on her own phone. "No — mine says the fuel station is at kilometre forty-seven."

"Forty-seven?" their father groans. "We'll never make it."

Ritvik looks out of the window. A white kilometre stone flashes past with *44* painted on it. The two phones are describing the same fuel station, on the same road, at the same moment. Neither app has crashed, and neither sister nor brother misread a screen.

So which number is the fuel station's real position — and what would the two apps need to agree on before their numbers could match?

## The physics

To say where something is along a straight line, you need three choices:

1. An **origin** — the point you call zero.
2. A **positive direction** — which way along the line counts as "plus".
3. A **unit** — metres, or kilometres on a highway.

Once these are fixed, the **position** of an object is one signed number, $x$: how far it is from the origin, with a plus sign on the positive side and a minus sign on the other side. The line together with its origin, direction and scale is a **frame of reference** for one-dimensional motion; NCERT calls it the $x$-axis.

Sana's offline map uses the kilometre stones: the origin is the stone marked zero, back in the city the highway starts from, and positive points away from that city. In that frame the fuel station is at $x = +47\,\text{km}$.

The navigation app does something clever: it puts the origin **at the car**, with positive pointing straight ahead, and moves the origin along with you. The car is at stone 44, so in the app's frame the fuel station is at $x = 47 - 44 = +3\,\text{km}$.

Both are correct. A position number means nothing until the origin and the positive direction have been said.

![Two number lines showing the same points P and Q: with origin O and positive to the right P is at +4 m and Q at −3 m; with origin O′ at the right end and positive to the left, P is at +2 m and Q at +9 m](figures/position/origin-and-direction.svg "Moving the origin or flipping the positive direction changes the numbers, not the places. The gap between P and Q is 7 m in both frames.")

Notice two things in the figure. A negative position is not "wrong" or "less real" — it only means "on the other side of the origin". And the **separation** between two points is the same in every frame.

## Worked example

**Given:** kilometre-stone frame, origin at stone 0, positive away from the city. The car is at $44\,\text{km}$, the fuel station at $47\,\text{km}$, and a roadside dhaba the family passed is at $39\,\text{km}$ (illustrative).
**Find:** each position in a new frame with the origin at the car and the positive direction pointing **back** towards the city — the frame of a "places behind you" list.

A point at $x$ in the stone frame is $44 - x$ kilometres from the car, measured in the new positive direction. So $x' = 44 - x$:

$$x'_\text{fuel} = 44 - 47 = -3\,\text{km}$$
$$x'_\text{dhaba} = 44 - 39 = +5\,\text{km}$$
$$x'_\text{city} = 44 - 0 = +44\,\text{km}$$

The fuel station now has a negative position, because it lies ahead of the car and "ahead" is now the negative direction.

**Sanity check:** the gap between the dhaba and the fuel station is $47 - 39 = 8\,\text{km}$ in the stone frame, and $5 - (-3) = 8\,\text{km}$ in the new one. The places didn't move, so the gap mustn't change — and it doesn't.

## Where the picture breaks

A real highway is never perfectly straight. Map apps really work with latitude and longitude — two numbers on a curved Earth — and then measure distance *along the road*; we have treated the road as one straight line, which is exactly the simplification this chapter makes. A phone's location fix also has an uncertainty of several metres, so "the car's position" is really a small blur, not a point. And the kilometre stones are just one agreed origin; a toll plaza, your house or the fuel station itself would work equally well, as long as everyone says which they chose.

## Key takeaway

Position is a signed number $x$ that only makes sense after you choose an origin and a positive direction. Change either one and every number changes — but the places, and the distances between them, stay the same. The fuel station is at $+47\,\text{km}$ from stone zero and $+3\,\text{km}$ from the car: two frames, one place.
