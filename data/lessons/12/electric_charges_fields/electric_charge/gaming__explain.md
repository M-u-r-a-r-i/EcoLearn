---
concept_id: electric_charge
interest: gaming
format: explain
title: The crackle before the graphics card goes in
check:
  question: |-
    Advait scuffs across the carpet and his hand ends up carrying $-16\,\text{nC}$. Take $e = 1.6 \times 10^{-19}\,\text{C}$, and assume his hand and the carpet exchanged charge only with each other. Which statement is correct?
  options:
    A: |-
      The carpet is left with $-16\,\text{nC}$ as well, because rubbing charges both surfaces the same way.
    B: |-
      The carpet is left with $+16\,\text{nC}$, because $1.0 \times 10^{11}$ electrons moved from the carpet onto his hand.
    C: |-
      The carpet is left with $+16\,\text{nC}$, because $1.0 \times 10^{11}$ protons moved from his hand into the carpet.
    D: |-
      The rubbing made $16\,\text{nC}$ of new negative charge on his hand, and the carpet stays neutral.
  answer: B
  explanation: |-
    Charge is conserved, so the carpet must hold $+16\,\text{nC}$, and it got that way by losing electrons: $16 \times 10^{-9} / 1.6 \times 10^{-19} = 1.0 \times 10^{11}$ of them.
  misconceptions:
    A: |-
      Thinks rubbing gives both surfaces the same kind of charge. Rubbing separates charge, so the two end up equal and opposite.
    C: |-
      Right answer, wrong mechanism: protons are locked inside nuclei and never transfer in rubbing. Only the loosely held outer electrons move.
    D: |-
      Thinks rubbing creates charge. It only moves charge that was already there, which is why the carpet cannot stay neutral.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A gaming desk at night during a PC build: a monitor running a field sandbox with two charges, a plasma globe, an antistatic bag sparking to a fingertip, and an open PC case with a graphics card going in](scenes/gaming/electric_charges_fields.svg "Every spark, every speck of clinging dust and every glowing filament in this picture is one chapter of physics.")

Advait has been saving for a year, and the box finally arrived this morning. His first build: a case with the side panel off, a motherboard, and a graphics card still sealed in its silver bag.

He rolls his chair back across the dry carpet in his socks, twice, reaching for the screwdriver. Then he picks up the bag and peels it open.

*Crack.* A blue thread of a spark jumps from his fingertip to the metal case, sharp enough to sting. Two crumbs of packing foam leap off the desk and stick to the bag. His older sister, watching from the doorway, says only, "You were supposed to touch the case first."

Advait rubs his stinging finger. He plugged nothing in. He switched nothing on. The carpet, his socks and the bag were all ordinary, boring, uncharged objects a minute ago. So where did that spark come from? Did rubbing *make* electricity?

## The physics

**Electric charge** is a basic property of matter, like mass. There are exactly **two kinds**, called positive and negative — the names are a convention we owe to Benjamin Franklin. **Like charges repel, unlike charges attract**, and a body is **neutral** when it holds equal amounts of both.

Matter is built from protons (positive), electrons (negative) and neutrons (uncharged). The protons sit locked inside nuclei. The outer electrons of some materials are held loosely, so when two different materials are rubbed together, **electrons move from one to the other**. Nothing else moves. That is what happened between Advait's socks and the carpet, and again between his fingers and the plastic bag.

Charge has three properties you must be able to state and use.

**1. Additivity.** Charge is a scalar, and a system's total charge is the algebraic sum of its parts, signs included. A body carrying $+5\,\text{nC}$, $-8\,\text{nC}$ and $+1\,\text{nC}$ has a total charge of $-2\,\text{nC}$.

**2. Quantisation.** Charge comes only in whole-number multiples of the basic unit $e$, the magnitude of the charge on an electron or a proton:

$$q = ne, \qquad n = 0, \pm 1, \pm 2, \ldots, \qquad e = 1.6 \times 10^{-19}\,\text{C}$$

No free object carries half an $e$. (Quarks do carry fractional charges, but they are never found on their own.)

**3. Conservation.** The total charge of an isolated system never changes. Charge can be handed from one body to another; it is never created or destroyed.

![Two blocks of material before and after rubbing: before, each is neutral; after, three electrons have crossed over, leaving one block at plus 3e and the other at minus 3e](figures/electric_charge/rubbing-transfers-electrons.svg "Only electrons move; the protons stay in their nuclei. One side goes negative by exactly as much as the other goes positive, so the total is still zero.")

So the rubbing made nothing. It **separated** charge that was already in the carpet and in Advait's socks. The spark was that separated charge jumping back across a thin gap of air to the earthed metal case.

## Worked example

**Given:** after the scuffing, Advait's hand carries $q = -16\,\text{nC}$ (an illustrative value). His hand and the carpet both started neutral.
**Find:** how many electrons crossed over, and what charge the carpet is left with.

First convert to coulombs: $16\,\text{nC} = 16 \times 10^{-9}\,\text{C} = 1.6 \times 10^{-8}\,\text{C}$.

Now use $q = ne$ to count them:

$$n = \frac{|q|}{e} = \frac{1.6 \times 10^{-8}}{1.6 \times 10^{-19}} = 1.0 \times 10^{11}$$

That is a hundred billion electrons — and $n$ comes out a whole number, as quantisation demands.

Those electrons came off the carpet, so the carpet is short of exactly that many:

$$q_\text{carpet} = +16\,\text{nC}$$

**Sanity check:** a hundred billion sounds enormous, but a fingertip already contains something like $10^{22}$ electrons, so only a tiny sliver of them moved — which is why Advait looks exactly the same afterwards.

## Where the picture breaks

Which way the electrons go depends on the pair of materials, not on one of them alone: socks on carpet may leave you negative, while a different pair could leave you positive. Treat "he ends up negative" as the illustration it is.

Real builds are not isolated systems either. Charge leaks away through damp air, through your skin and through anything earthed you brush against, so on a humid day you can scuff all you like and get no spark at all. And a spark is not "charge escaping into nothing": it is charge crossing to another body, where it still counts.

## Key takeaway

There are two kinds of charge; like repels like, unlike attracts. Charge is **additive** (add it with signs), **quantised** ($q = ne$, with $e = 1.6 \times 10^{-19}\,\text{C}$) and **conserved**. Rubbing never creates charge — it moves electrons from one body to the other, leaving equal and opposite charges behind.
