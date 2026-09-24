---
concept_id: meter_bridge
interest: gaming
format: explain
title: Measuring a salvaged resistor with a ruler
check:
  question: |-
    A metre bridge has a known $R = 8\,\Omega$ in the left gap and an unknown $S$ in the right gap. The balance point is found at $l = 25\,\text{cm}$ from the left-hand end. The unknown resistance $S$ is:
  options:
    A: |-
      $2.7\,\Omega$
    B: |-
      $8\,\Omega$
    C: |-
      $32\,\Omega$
    D: |-
      $24\,\Omega$
  answer: D
  explanation: |-
    At balance $\dfrac{R}{S} = \dfrac{l}{100-l}$, so $S = R\,\dfrac{100-l}{l} = 8 \times \dfrac{75}{25} = 24\,\Omega$.
  misconceptions:
    A: |-
      Uses the ratio upside down, calculating $8 \times 25/75$. The balance point is close to the left end, so the left-hand arm is the *short* one — meaning the left-hand resistance is the smaller.
    B: |-
      Assumes the balance point only locates the unknown on the wire and says nothing about its size. The whole instrument rests on the balance length being fixed by the ratio of the two resistances.
    C: |-
      Uses the full $100\,\text{cm}$ instead of the far segment $100 - l$. The right-hand arm is only the wire beyond the jockey, which is $75\,\text{cm}$, not the whole wire.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A night gaming desk with a monitor showing a frame counter, a controller charging over a USB cable, a USB power meter, and an open PC case with an LED strip](scenes/gaming/current_electricity.svg "An LED strip needs a series resistor of the right value — and a salvaged resistor with its markings burnt off is no help at all.")

The retro gaming club has an arcade cabinet, a marquee to light, and a shoebox of parts salvaged from three dead machines. Lakshmi is trying to decide which of the salvaged resistors to put in series with the LED strip, and not one of them is readable — the colour bands have been cooked off.

The lab's digital ohmmeter would settle it in two seconds. Its battery is flat, and the store cupboard is locked until Monday.

What is not locked is the **metre bridge** on the back shelf: a wooden board, a metre of thin wire stretched along a ruler, two gaps for resistors, a cell, and a galvanometer on a sliding contact.

Her teacher, who refuses to simply tell her the answer, says the board can measure that resistor better than the broken meter could — and that the only number she will read off is a length in centimetres.

A resistance, measured with a ruler. How?

## The physics

A metre bridge is a Wheatstone bridge with two of its arms replaced by the two halves of a single wire.

![A Wheatstone bridge as a diamond of four resistors with a galvanometer across the middle](figures/wheatstone_bridge/wheatstone-bridge-balanced.svg "The parent circuit: at balance no current crosses the galvanometer, and the four arms are locked into a ratio.")

The board carries a uniform resistance wire exactly $100\,\text{cm}$ long between two points A and C. The known resistance $R$ sits in the left gap and the unknown $S$ in the right gap; a cell drives current from A to C, and a **jockey** — a sliding contact connected through the galvanometer — is tapped along the wire until the galvanometer reads zero.

![A metre bridge: a metre of uniform wire on a scale, a known resistance in one gap, the unknown in the other, and a jockey sliding to the balance point](figures/meter_bridge/metre-bridge-setup.svg "The two stretches of wire on either side of the jockey are the bridge's ratio arms — and their ratio is simply the ratio of their lengths.")

Here is why the ruler is enough. The wire is uniform, so from $R = \rho L/A$ each centimetre of it has the same resistance; call it $\sigma$ ohms per centimetre. If the balance point is a distance $l$ from A, the two stretches of wire have resistances $\sigma l$ and $\sigma(100 - l)$, and they are the bridge's ratio arms. The balance condition $\dfrac{P}{Q} = \dfrac{R}{S}$ becomes

$$\frac{\sigma l}{\sigma (100-l)} = \frac{R}{S}$$

and $\sigma$ cancels:

$$\boxed{S = R\,\frac{100 - l}{l}}$$

Nothing about the wire survives except its *uniformity* — not its material, not its thickness, not its temperature. You never need to know $\sigma$, which is exactly why a length in centimetres is a legitimate measurement of a resistance in ohms.

One practical rule follows from the algebra: the bridge is most sensitive when the balance point is near the **middle** of the wire, so choose a known $R$ of roughly the same size as the unknown. A balance at $3\,\text{cm}$ or $97\,\text{cm}$ is a bad measurement, because a millimetre of jockey error then shifts the answer enormously.

## Worked example

**Given:** Lakshmi puts a known $R = 8\,\Omega$ in the left gap and the salvaged resistor in the right gap. The galvanometer nulls with the jockey at $l = 25\,\text{cm}$ from the left-hand end.
**Find:** the salvaged resistor's resistance $S$.

The wire beyond the jockey is $100 - 25 = 75\,\text{cm}$ long, so the two arms are in the ratio $25 : 75$, or $1 : 3$ — the right-hand arm is three times the left.

$$S = R\,\frac{100 - l}{l} = 8 \times \frac{75}{25} = 24\,\Omega$$

Twenty-four ohms, from one reading on a ruler.

**Sanity check:** the balance point sits well left of centre, so the right-hand arm is the longer one, and $S$ must be the larger resistance — it is, by the same factor of three. (It also warns Lakshmi that $8\,\Omega$ was a poor choice of known resistance: something near $24\,\Omega$ would have balanced closer to the middle and measured more accurately.)

## Where the picture breaks

The board is a real instrument, and nothing about gaming resembles a bridge circuit; the arcade cabinet is only the reason for the measurement.

The real limits are in the apparatus. The formula assumes the resistance between A and C is entirely the metre of wire, but the thick copper strips and the screw terminals at each end add a little of their own — the **end corrections**, which are why careful work repeats the reading with $R$ and $S$ interchanged and averages. The wire is never perfectly uniform either, and it warms if you leave the current flowing, so the jockey is *tapped*, not dragged, and the key is opened between readings.

One more thing matters for Lakshmi's actual job. The bridge measures a plain resistor beautifully, but she cannot point it at the LED strip itself: an LED is non-ohmic, so it has no single resistance to find, and forcing a bridge current through it would tell her nothing useful.

## Key takeaway

A metre bridge is a Wheatstone bridge whose two ratio arms are the stretches of a uniform wire on either side of the balance point. Because the wire's resistance per centimetre cancels, the balance condition reduces to $S = R\,\dfrac{100-l}{l}$ — a resistance measured with a ruler. Choose $R$ so the balance falls near the middle of the wire, where the method is most sensitive.
