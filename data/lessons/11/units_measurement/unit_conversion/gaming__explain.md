---
concept_id: unit_conversion
interest: gaming
format: explain
title: Porting a racing game to a centimetre world
check:
  question: |-
    A game engine measures mass in grams and length in centimetres. A wooden crate in the game should have a density of $600\,\text{kg/m}^3$. What value should be entered, in $\text{g/cm}^3$?
  options:
    A: |-
      $6000$
    B: |-
      $6 \times 10^{-4}$
    C: |-
      $0.6$
    D: |-
      $6 \times 10^{11}$
  answer: C
  explanation: |-
    Density is $[\text{M}\,\text{L}^{-3}]$, so $n_2 = 600 \times (10^3)^1 \times (10^2)^{-3} = 600 \times 10^3 \times 10^{-6} = 0.6$. A gram per cubic centimetre is a much bigger unit, so the number gets smaller.
  misconceptions:
    A: |-
      Converts the length ratio with power $-1$ instead of $-3$, as if a volume were a length: $600 \times 10^3 \times 10^{-2}$. A cubic metre is $10^6$ cubic centimetres, not $100$.
    B: |-
      Converts the volume correctly but forgets to convert kilograms to grams, changing only one of the two base units.
    D: |-
      Uses the power $+3$ for length instead of $-3$. Length appears in the denominator of density, so its ratio must be raised to $-3$.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A gaming desk: a monitor showing a racing game with a speed readout of 216 km/h and a 144 FPS counter](scenes/gaming/units_measurement.svg "The speedometer talks in km/h. The engine underneath may talk in something else entirely.")

Pranav and Diya are porting their school racing game to a new engine for a game jam. Their car has a top speed of $216\,\text{km/h}$ on the speedometer, and the old code kept everything in metres, kilograms and seconds.

The new engine doesn't. Its manual says lengths are in **centimetres** and masses in **grams**. Every number has to be re-entered: the car's top speed, the strength of gravity, the density of the crates that fly when the car hits them.

"Easy," says Diya. "A metre is a hundred centimetres. Multiply everything by $100$."

Pranav isn't so sure. A speed has a length *and* a time in it. A density has a mass and a length *cubed*. Can one factor of $100$ possibly be right for all of them? Or is there a single method that works for any quantity, whatever it's made of?

## The physics

A quantity is a number times a unit: $Q = n_1 u_1 = n_2 u_2$. A bigger unit needs a smaller number, and vice versa.

Every unit is built from base units following the quantity's dimensional formula $[\text{M}^a\,\text{L}^b\,\text{T}^c]$, so its size is $u = M^a L^b T^c$, where $M$, $L$, $T$ are the base units of that system. Because $n_1 u_1 = n_2 u_2$:

$$n_2 = n_1 \left[\frac{M_1}{M_2}\right]^a \left[\frac{L_1}{L_2}\right]^b \left[\frac{T_1}{T_2}\right]^c$$

System 1 is the one you have; system 2 is the one you want. Each base-unit ratio gets the **same power** it has in the dimensional formula. That is why Diya's single factor fails: the power of $L$ is different for every quantity.

For a speed, $[\text{L}\,\text{T}^{-1}]$: $a = 0$, $b = 1$, $c = -1$. The familiar km/h to m/s step is just this formula with $L_1/L_2 = 1000$ and $T_1/T_2 = 3600$:

![A chain of boxes: 144 km/h, times 1000, divided by 3600, gives 40 m/s; below it, the same step written with the dimensional formula](figures/unit_conversion/conversion-chain-kmh-ms.svg "Convert the length and the time separately; the dimensional formula sets each factor's power. The same two steps work for 216 km/h.")

For anything with a squared or cubed length, the length factor is squared or cubed too:

![A square metre split into 10 000 square centimetres and a cubic metre into a million cubic centimetres, with the density conversion below](figures/unit_conversion/area-volume-conversion.svg "A metre is 100 cm, but a cubic metre is a million cubic centimetres. So 1 g/cm³ is 1000 kg/m³.")

## Worked example

**Given** (illustrative values, SI to the engine's system of g, cm, s): top speed $216\,\text{km/h}$; $g = 9.8\,\text{m/s}^2$; crate density $800\,\text{kg/m}^3$.
**Find:** each value in the engine's units.

(a) **Speed**, $[\text{L}\,\text{T}^{-1}]$, from km/h to cm/s: $L_1/L_2 = 1\,\text{km}/1\,\text{cm} = 10^5$; $T_1/T_2 = 1\,\text{h}/1\,\text{s} = 3600$.

$$n_2 = 216 \times (10^5)^1 \times (3600)^{-1} = \frac{2.16 \times 10^7}{3600} = 6000\,\text{cm/s}$$

(b) **Gravity**, $[\text{L}\,\text{T}^{-2}]$: $L_1/L_2 = 10^2$, $T_1/T_2 = 1$.

$$n_2 = 9.8 \times (10^2)^1 \times 1^{-2} = 980\,\text{cm/s}^2$$

(c) **Density**, $[\text{M}\,\text{L}^{-3}]$: $M_1/M_2 = 1\,\text{kg}/1\,\text{g} = 10^3$, $L_1/L_2 = 10^2$.

$$n_2 = 800 \times (10^3)^1 \times (10^2)^{-3} = 800 \times 10^{-3} = 0.8\,\text{g/cm}^3$$

So the three factors were $\times 27.8$, $\times 100$ and $\times 0.001$ — nothing like one universal $100$.

**Sanity check:** (a) by the shortcut, $216/3.6 = 60\,\text{m/s} = 6000\,\text{cm/s}$. And (c) makes sense: wood lighter than water should come out below $1\,\text{g/cm}^3$, water's density.

## Where the picture breaks

The engine's centimetre is only a label: the engine never measures anything, so "converting" there just means keeping your numbers consistent with its convention. In the real world, a conversion changes units, never precision: $216\,\text{km/h}$ (three significant figures) becomes $60.0\,\text{m/s}$, not a more exact value. And the method works only for units that differ by a scale factor; temperatures in $^\circ\text{C}$ and $^\circ\text{F}$ have different zeros, which no power of a ratio can fix.

## Key takeaway

To convert a quantity with dimensional formula $[\text{M}^a\,\text{L}^b\,\text{T}^c]$, use $n_2 = n_1 (M_1/M_2)^a (L_1/L_2)^b (T_1/T_2)^c$. Each base-unit ratio takes the same power as in the dimensional formula, so a density needs the length ratio cubed: $1\,\text{g/cm}^3 = 1000\,\text{kg/m}^3$.
