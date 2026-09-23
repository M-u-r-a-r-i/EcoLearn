---
concept_id: electric_charge
interest: football
format: explain
title: The bib that crackles when you pull it off
check:
  question: |-
    Aarav's training bib ends up with a charge of $-3.2\,\text{nC}$ after he pulls it off over his shirt. Both were uncharged before. Which statement is correct?
  options:
    A: |-
      The shirt now carries $+3.2\,\text{nC}$, because electrons moved from the shirt to the bib.
    B: |-
      The shirt is still uncharged; the bib picked up its charge from the damp air.
    C: |-
      The shirt now carries $-3.2\,\text{nC}$ too, because rubbing gives both surfaces the same charge.
    D: |-
      The shirt now carries $+3.2\,\text{nC}$, because protons moved from the shirt to the bib.
  answer: A
  explanation: |-
    Charge is conserved and only electrons move in rubbing. The bib gained electrons, so the shirt is left short of exactly the same amount of charge: $+3.2\,\text{nC}$.
  misconceptions:
    B: |-
      Treats charge as something created out of the surroundings. Rubbing never makes new charge; it only moves electrons from one surface to the other, so the two must end up with equal and opposite charges.
    C: |-
      Thinks rubbing charges both objects the same way. The two surfaces cannot both gain electrons — whatever one gains, the other loses.
    D: |-
      Gets the right number for the wrong reason. Protons are locked inside nuclei and never move in rubbing; the shirt becomes positive by *losing* electrons, not by handing over protons.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A floodlit ground as a storm arrives: lightning above the stand, rain falling, a player peeling off a crackling nylon bib, and two players heading for the metal-roofed dugout](scenes/football/electric_charges_fields.svg "Rubbing, sparks and lightning — the whole chapter is in this one picture.")

The floodlights cut out halfway through Thursday's session, and for about ten seconds the ground is properly dark. That is when Aarav decides to swap out of his yellow bib.

He drags it up over his dry nylon shirt, and the whole team hears it: a papery crackle, and — in the dark — a spray of tiny blue sparks along his shoulder. Someone yells. Aarav stands there with the bib halfway over his head, feeling the hairs on his forearm lift.

"Do it again," says Meera from the goal line.

He does. Same crackle, same faint sparks, and now the bib is clinging to his arm as though someone had smeared it with glue.

Nothing has been plugged in. Nothing is burning. Two clean pieces of cloth have been rubbed together, and something has clearly been moved from one to the other. What is it — and how much of it?

## The physics

Rubbing does not create anything new. It **transfers electrons** from one surface to the other. The surface that gains electrons is left with **negative charge**; the one that loses them is left with an equal **positive charge**. Those are the only two kinds of charge there are: like charges repel, unlike charges attract.

![Before rubbing, cotton and polyester are each neutral; after rubbing, three electrons have moved to the polyester, making it minus 3e and the cotton plus 3e](figures/electric_charge/rubbing-transfers-electrons.svg "Rubbing moves electrons, never protons. One side ends positive, the other negative, and the total stays zero.")

Charge, measured in **coulombs (C)**, obeys three rules you will use for the rest of this chapter.

- **Additivity.** Charge adds like an ordinary number, taking signs into account. A bib at $-3\,\text{nC}$ touching one at $+1\,\text{nC}$ gives a system of $-2\,\text{nC}$.
- **Quantisation.** Charge comes in whole multiples of the elementary charge $e = 1.6 \times 10^{-19}\,\text{C}$:
  $$q = ne, \qquad n = 0, \pm 1, \pm 2, \dots$$
  An electron carries $-e$, a proton $+e$. You cannot have half an electron's worth of charge on the bib.
- **Conservation.** In any isolated system the total charge stays the same. Aarav's shirt and bib started at zero together, so they must still add to zero.

Protons sit locked in nuclei and do not move between everyday objects, so **only electrons are ever transferred**. That single fact is what makes the two charges equal and opposite.

## Worked example

**Given:** after one pull, the bib carries $q = -1.6\,\text{nC}$, and the shirt was uncharged before.
**Find:** how many electrons crossed, and the shirt's charge.

**Step 1 — put the charge in SI units.** $1\,\text{nC} = 10^{-9}\,\text{C}$, so $q = -1.6 \times 10^{-9}\,\text{C}$. The minus sign says the bib gained electrons.

**Step 2 — use quantisation.** The number of electrons is the charge divided by the charge on one:

$$n = \frac{1.6 \times 10^{-9}}{1.6 \times 10^{-19}} = 1.0 \times 10^{10}$$

Ten thousand million electrons — and yet a bib holds something like $10^{25}$ electrons altogether, so roughly one electron in $10^{15}$ has moved. The cloth is still, to every test you could do, ordinary cloth.

**Step 3 — use conservation.** The pair started at zero, so the shirt is left with $+1.6\,\text{nC}$.

**Sanity check:** everyday static sits in the nanocoulomb range, while a lightning flash moves whole coulombs — a thousand million times more. A crackle, not a strike, is exactly what we saw.

## Where the picture breaks

The sparks look like the charge "escaping", but they are air breaking down and conducting briefly — the charge goes somewhere, it is not destroyed. The crackle also depends on the evening: on a humid day a thin film of water on the fibres carries the charge away as fast as rubbing builds it up, which is why the trick works on a dry night and fails after rain. And "the bib is at $-1.6\,\text{nC}$" is a total; the charge is not spread evenly over it, and it sits only where the two surfaces actually rubbed.

## Key takeaway

There are two kinds of charge, and rubbing only ever moves electrons from one surface to the other — so the two objects end up equal and opposite. Charge is additive (signs included), conserved in any isolated system, and quantised as $q = ne$ with $e = 1.6 \times 10^{-19}\,\text{C}$.
