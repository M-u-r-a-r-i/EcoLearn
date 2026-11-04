---
concept_id: significant_figures_arithmetic
interest: smartphones
format: explain
title: Whose phone screen is really bigger
check:
  question: |-
    A phone screen is measured as $6.85\,\text{cm}$ wide and $14.9\,\text{cm}$ tall. The calculator gives the area as $102.065\,\text{cm}^2$. Reported correctly, the area is:
  options:
    A: |-
      $102.065\,\text{cm}^2$
    B: |-
      $102.07\,\text{cm}^2$
    C: |-
      $102.1\,\text{cm}^2$
    D: |-
      $102\,\text{cm}^2$
  answer: D
  explanation: |-
    A product keeps as many significant figures as the factor with the fewest. Both $6.85$ and $14.9$ have three, so the area is $102\,\text{cm}^2$.
  misconceptions:
    A: |-
      Copies the calculator display. The last digits are meaningless: neither length was measured finely enough to support six significant figures.
    B: |-
      Uses the decimal-places rule (meant for addition) and copies the two decimal places of $6.85$. In multiplication, what matters is significant figures, not decimal places.
    C: |-
      Uses the decimal-places rule and copies the one decimal place of $14.9$, giving four significant figures. Multiplication keeps the fewest significant figures, which is three.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A study desk with a phone held in a digital caliper, a phone on a scale and a charger](scenes/smartphones/units_measurement.svg "A caliper reads to a hundredth of a millimetre; a plastic ruler doesn't. The answer can't be sharper than the rougher tool.")

Arjun and Kiran have been arguing all week about whose phone has the bigger screen. Today they settle it in the physics lab at lunch.

Arjun measures his screen with care: the digital caliper across the width, $6.85\,\text{cm}$, and a metre scale down the length, $14.9\,\text{cm}$. His calculator says the area is $102.065\,\text{cm}^2$.

Kiran is in a hurry and grabs a plastic ruler for both sides: $6.9\,\text{cm}$ by $14.8\,\text{cm}$. His calculator says $102.12\,\text{cm}^2$.

"$102.12$ beats $102.065$," Kiran announces. "Mine's bigger. The numbers don't lie."

Arjun isn't ready to give up. The difference is about $0.055\,\text{cm}^2$ — a patch smaller than a lentil. Can two measurements made with a ruler and a caliper really tell apart two screens that closely? How many of those calculator digits have either of them actually earned?

## The physics

When you calculate with measured values, the result can't be more precise than the data. NCERT gives two rules.

**Multiplying or dividing:** keep as many **significant figures** as the value with the fewest significant figures.

**Adding or subtracting:** keep as many **decimal places** as the value with the fewest decimal places.

![Left: 20.12 plus 1.5 gives 21.62, rounded to 21.6 because 1.5 has one decimal place. Right: 20.12 times 3.05 gives 61.366, rounded to 61.4 because 3.05 has three significant figures](figures/significant_figures_arithmetic/add-vs-multiply-rules.svg "Adding: the unknown hundredths digit of 1.5 spoils the hundredths of the sum. Multiplying: the answer keeps the significant figures of the least precise factor.")

Why two different rules? In a sum, what matters is the **position** of the last reliable digit — if one length is only known to a tenth of a millimetre, the sum can't be known to a hundredth. In a product, what matters is the **relative** precision of each factor, and significant figures are a rough measure of that.

**Rounding off (NCERT):** look at the first digit you're dropping.

- More than $5$: raise the preceding digit by $1$ ($102.07 \to 102.1$).
- Less than $5$: leave it unchanged ($102.065 \to 102$ when keeping three figures, because the dropped part starts with $0$).
- Exactly $5$ with nothing after it: leave an even preceding digit, raise an odd one ($3.45 \to 3.4$, $3.35 \to 3.4$).

**Exact numbers** — counted or defined, like "two screens" or the $1000$ in $1\,\text{m} = 1000\,\text{mm}$ — never limit a result. In a calculation with several steps, carry one extra digit in the middle and round only at the end.

## Worked example

**Given:** Arjun's screen $6.85\,\text{cm} \times 14.9\,\text{cm}$ (three significant figures each); Kiran's $6.9\,\text{cm} \times 14.8\,\text{cm}$ ($6.9$ has two). Arjun's phone is $7.92\,\text{mm}$ thick and a case adds $1.5\,\text{mm}$ at the back.
**Find:** (a) both areas, reported correctly; (b) the thickness with the case on.

(a) Multiplication, so fewest significant figures:

$$A_\text{Arjun} = 6.85 \times 14.9 = 102.065 \approx 102\,\text{cm}^2 \quad (3\text{ s.f.})$$

$$A_\text{Kiran} = 6.9 \times 14.8 = 102.12 \approx 1.0 \times 10^2\,\text{cm}^2 \quad (2\text{ s.f.})$$

Kiran's result is only known to about $\pm 1$ in the second figure — roughly the nearest $10\,\text{cm}^2$. The two screens are equal as far as these measurements can tell. Nobody wins.

(b) Addition, so fewest decimal places — one, from $1.5\,\text{mm}$:

$$7.92\,\text{mm} + 1.5\,\text{mm} = 9.42\,\text{mm} \approx 9.4\,\text{mm}$$

**Sanity check:** reverse (a): $102 \div 14.9 = 6.85$, which returns Arjun's width, so the multiplication itself is right.

## Where the picture breaks

The significant-figure rules are a quick guide, not a full error calculation — the next lesson on errors does this properly and can say *how* uncertain Kiran's area is. The model also treats the screen as a perfect rectangle; real screens have rounded corners and sometimes a camera cut-out, so the true display area is a little less than width times height.

## Key takeaway

Multiplying or dividing: keep the fewest significant figures of the data. Adding or subtracting: keep the fewest decimal places. Round only at the end, and never let a calculator's extra digits pretend to be measurements.
