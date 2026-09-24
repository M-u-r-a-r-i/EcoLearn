---
concept_id: capacitors_combination
interest: gaming
format: explain
title: Building the value you need from the ones you have
check:
  question: |-
    A $3\,\mu\text{F}$ and a $6\,\mu\text{F}$ capacitor are joined in **series** across a $9\,\text{V}$ supply. What charge sits on the $3\,\mu\text{F}$ capacitor?
  options:
    A: |-
      $27\,\mu\text{C}$
    B: |-
      $81\,\mu\text{C}$
    C: |-
      $9\,\mu\text{C}$
    D: |-
      $18\,\mu\text{C}$
  answer: D
  explanation: |-
    In series $1/C_s = 1/3 + 1/6 = 1/2$, so $C_s = 2\,\mu\text{F}$ and $Q = C_sV = 2 \times 9 = 18\,\mu\text{C}$ — and in series that same charge sits on **each** capacitor.
  misconceptions:
    A: |-
      Uses $Q = 3\,\mu\text{F} \times 9\,\text{V}$, as though the full supply voltage appeared across the $3\,\mu\text{F}$ capacitor. In series the $9\,\text{V}$ is shared, and the smaller capacitor takes the larger share.
    B: |-
      Adds the capacitances as $3 + 6 = 9\,\mu\text{F}$, which is the *parallel* rule. In series the reciprocals add, and the combination is always smaller than the smallest capacitor in it.
    C: |-
      Works out the right total charge and then splits it between the two capacitors. Charge is not shared out in series — the isolated middle section forces $+Q$ on one plate and $-Q$ on the facing one, so every capacitor in the chain carries the *same* charge.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A gaming desk with a monitor showing rings of equal potential around a charge, a phone with a fingertip on its screen, an old picture tube on the bench and an opened power supply with two big capacitors](scenes/gaming/potential_capacitance.svg "Open almost any piece of gaming hardware and you find capacitors in groups, not alone. The reason is in this lesson.")

Zoya's home arcade cabinet has started flickering, and Kabir has traced it to one swollen capacitor on the power board with its top domed and split.

The problem is the shop. They have walked to two and neither stocks that value; one of them sells a bag of thirty identical capacitors, all the same size, and nothing else.

"We're stuck," Kabir says.

Zoya isn't so sure. She remembers doing resistors last term — two of them side by side behaved like one bigger one, two in a row like one smaller. "There must be a rule for these too. If we've got thirty, we can probably make whatever number we want."

Kabir's objection is a fair one. "Two in a row halves it or doubles it. Which?" Neither of them can remember, and guessing wrong on a power board is an expensive mistake. So: what does joining capacitors actually do — and is it the same rule as for resistors, or the reverse?

## The physics

![Series: three capacitors in a chain with the same charge on each and voltages adding. Parallel: three side by side with the same voltage across each and charges adding.](figures/capacitors_combination/series-and-parallel.svg "Series: same Q, voltages add. Parallel: same V, charges add. The rules are the reverse of those for resistors.")

**In series** — capacitors in a chain, one after the next. The section of conductor between two neighbouring capacitors is **isolated**: it was uncharged to begin with, and charge cannot leak on or off it. So when $+Q$ appears on the first plate, $-Q$ is induced on the plate facing it, leaving $+Q$ on the next plate along, and so on. **Every capacitor carries the same charge $Q$.** The potential differences add up to the supply voltage:

$$V = V_1 + V_2 + V_3 = \frac{Q}{C_1} + \frac{Q}{C_2} + \frac{Q}{C_3}$$

Dividing by $Q$:

$$\frac{1}{C_s} = \frac{1}{C_1} + \frac{1}{C_2} + \frac{1}{C_3}$$

The equivalent capacitance is **smaller than the smallest** capacitor in the chain — putting them in series is like widening the gap.

**In parallel** — capacitors side by side, all bridging the same two points. Now the **voltage $V$ across each is the same**, and the charges add:

$$Q = Q_1 + Q_2 + Q_3 = C_1V + C_2V + C_3V$$

so

$$C_p = C_1 + C_2 + C_3$$

which is **larger than the largest** — like joining the plates into one big pair.

That is Kabir's answer, and note the sting in it: these are the **reverse** of the resistor rules. Resistances add in series; capacitances add in parallel. If you remember one pair you can derive the other from $C = Q/V$ against $R = V/I$.

## Worked example

Zoya has three identical $6.0\,\mu\text{F}$ capacitors. She connects two of them in series, then puts the third **in parallel** across that pair, and applies $10\,\text{V}$.

**Find:** the equivalent capacitance, and the total charge drawn.

**Step 1 — the series pair.**

$$\frac{1}{C_s} = \frac{1}{6.0} + \frac{1}{6.0} = \frac{2}{6.0} \quad \Rightarrow \quad C_s = 3.0\,\mu\text{F}$$

Two equal capacitors in series give half of one — smaller than either, as promised.

**Step 2 — the third in parallel with that pair.**

$$C_\text{eq} = C_s + 6.0 = 3.0 + 6.0 = 9.0\,\mu\text{F}$$

**Step 3 — the charge.**

$$Q = C_\text{eq}V = 9.0\times10^{-6} \times 10 = 9.0\times10^{-5}\,\text{C} = 90\,\mu\text{C}$$

**Sanity check:** with three $6\,\mu\text{F}$ parts, the answer had to lie between $2\,\mu\text{F}$ (all three in series) and $18\,\mu\text{F}$ (all three in parallel). $9\,\mu\text{F}$ sits comfortably inside that range.

## Where the picture breaks

Zoya can indeed build new values from a bagful, but a power board asks for more than a number. Each capacitor has a **voltage rating**, and in series the supply voltage divides between them in the ratio $1/C$ — so an unequal pair does not share it equally, and the smaller one can quietly sit above its rating. Real capacitors also carry a tolerance of ten or twenty per cent, so $1/C_s = 1/C_1 + 1/C_2$ gives a value with the same uncertainty baked in. And a swollen capacitor in a power supply is usually there for a job — smoothing a rapidly changing voltage — that depends on properties this chapter never mentions, like its internal resistance. The rules above are exact for ideal capacitors in electrostatics; they are the starting point of a repair, not the whole of it.

## Key takeaway

In **series** every capacitor carries the same charge and the voltages add, giving $1/C_s = 1/C_1 + 1/C_2 + \dots$ — always less than the smallest. In **parallel** every capacitor has the same voltage and the charges add, giving $C_p = C_1 + C_2 + \dots$ — always more than the largest. These are the reverse of the resistor rules, so name the connection before you reach for a formula.
