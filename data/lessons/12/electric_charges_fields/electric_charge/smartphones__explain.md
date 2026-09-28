---
concept_id: electric_charge
interest: smartphones
format: explain
title: The crackle when you peel a new screen film
check:
  question: |-
    A phone and its factory film start out neutral. As the film is peeled off, it ends up with a charge of $-6.4\,\text{nC}$. No charge leaks away to the air or to anyone's hand. What charge is left on the phone's screen?
  options:
    A: |-
      $+6.4\,\text{nC}$
    B: |-
      Zero, since only the film was charged by the peeling
    C: |-
      $-6.4\,\text{nC}$, the same as the film
    D: |-
      $+3.2\,\text{nC}$, half of the film's charge
  answer: A
  explanation: |-
    Charge is conserved: the film and screen together had zero charge before, so they have zero after. Electrons moved from the screen to the film, so the screen is short of exactly as many electrons as the film gained: $+6.4\,\text{nC}$.
  misconceptions:
    B: |-
      Thinks peeling created charge on the film out of nothing. Charge is never created; the film's extra electrons had to come from somewhere, and here they came from the screen.
    C: |-
      Thinks rubbing or peeling gives both surfaces the same kind of charge. Electrons move one way, so one side gains them (negative) and the other loses them (positive).
    D: |-
      Thinks the charge is shared out or halved in the transfer. Every electron the film gains is one the screen lost, so the two charges are equal in size.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A desk by a sunny window with a solar power bank on the sill, an opened phone box with foam beads clinging to the new phone, a film being peeled off a screen with dust jumping up to it, and a phone on a stand running a field-line app](scenes/smartphones/electric_charges_fields.svg "Look at the middle of the desk: as the film comes off, dust specks leap up to it. Something on the film was not there a second ago.")

Aanya has waited three months for this phone. The box is open, the foam beads are everywhere, and now comes the best part: peeling off the factory film.

She pulls it slowly. There is a faint crackle, and in the quiet room she's sure she saw a tiny blue spark near the corner. Then something odd: specks of dust from the desk jump up and stick to the peeled film, as if it were pulling them.

"You just made electricity," says her younger brother Vihaan, very impressed. "Out of nothing. By peeling."

Aanya isn't so sure. The phone was off. The film is just plastic. Nobody plugged anything in. If the film suddenly has electric charge on it, where did that charge come from? Was it really made from nothing, or was it already there, hiding?

## The physics

**Electric charge** is a basic property of matter, like mass. There are exactly **two kinds**, named **positive** and **negative** by Benjamin Franklin's convention. Like charges repel; unlike charges attract. The dust leaping to the film is that attraction at work.

All ordinary matter is built from protons (charge $+e$), electrons (charge $-e$) and neutrons (no charge). An object is **neutral** when it has equal numbers of protons and electrons. When two surfaces touch and separate, as the film and the glass did, some **electrons** move from one surface to the other. Protons stay locked in the nuclei and never move in this process.

![Before rubbing, two cloths are each neutral; after rubbing, three electrons have moved from one to the other, leaving one at plus 3e and the other at minus 3e](figures/electric_charge/rubbing-transfers-electrons.svg "Only electrons move, and the total stays zero. Film and glass behave exactly like these two cloths.")

Charge has three properties you need to know:

- **Additivity.** Charges add like ordinary numbers, **with their signs**: $q_\text{total} = q_1 + q_2 + q_3 + \dots$ A body carrying $+2\,\text{nC}$ and $-5\,\text{nC}$ on different parts has a total of $-3\,\text{nC}$.
- **Quantisation.** Every charge is a whole-number multiple of the **elementary charge** $e = 1.6 \times 10^{-19}\,\text{C}$:
$$q = ne, \qquad n = 0, \pm 1, \pm 2, \dots$$
You can't have half an electron's worth of charge on the film. The steps are so tiny that everyday charges look smooth, the way sand looks smooth from far away.
- **Conservation.** The total charge of an isolated system never changes. Charge is not created by peeling; it is **moved**. Whatever the film gains, the screen loses.

The SI unit of charge is the **coulomb** (C). Everyday static charges are only nano-coulombs ($1\,\text{nC} = 10^{-9}\,\text{C}$).

## Worked example

**Given (illustrative):** after peeling, say the film carries $q = -3.2\,\text{nC}$. The film and phone started neutral, and no charge escaped.
**Find:** how many electrons moved, and the screen's charge.

**Step 1 — convert.** $3.2\,\text{nC} = 3.2 \times 10^{-9}\,\text{C}$.

**Step 2 — count the electrons.** From $q = ne$:
$$n = \frac{3.2 \times 10^{-9}}{1.6 \times 10^{-19}} = 2.0 \times 10^{10}$$
So twenty billion extra electrons sit on the film. It is a whole number, as quantisation demands.

**Step 3 — the screen.** Those electrons came off the glass, so the screen is short of $2.0 \times 10^{10}$ electrons: its charge is $+3.2\,\text{nC}$.

**Step 4 — add them up.** $(-3.2) + (+3.2) = 0\,\text{nC}$, the same total as before peeling.

**Sanity check:** twenty billion sounds huge, but the glass holds far more than a million million times as many electrons, so only a tiny fraction of its electrons moved, which is why the screen looks and works exactly the same.

## Where the picture breaks

Which surface ends up negative depends on the two materials (and on moisture and dirt), so "the film goes negative" is an assumption for the example, not a rule. The film and screen are not truly isolated either: charge slowly leaks away through humid air and your fingers, which is why the dust effect fades within minutes. The spark Aanya saw is charge jumping through the air over a tiny gap; the total is still conserved, it has just moved somewhere else.

## Key takeaway

There are two kinds of charge; like charges repel and unlike attract. Charge adds with its sign, comes only in whole-number multiples of $e$ ($q = ne$), and is always conserved: peeling a film does not create charge, it moves electrons from the screen to the film, leaving equal and opposite charges behind.
