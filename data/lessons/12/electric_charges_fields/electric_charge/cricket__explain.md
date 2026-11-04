---
concept_id: electric_charge
interest: cricket
format: explain
title: The crackle when the jersey comes off
check:
  question: |-
    After a rain-hit day, Kabir pulls his polyester jersey off over a cotton vest. Afterwards the jersey carries $-32\,\text{nC}$. Assuming the jersey and vest were both neutral before and exchanged charge only with each other, what charge does the vest carry?
  options:
    A: |-
      $+32\,\text{nC}$, because about $2.0 \times 10^{11}$ protons moved from the jersey into the vest
    B: |-
      $-32\,\text{nC}$, because rubbing gives both materials the same kind of charge
    C: |-
      $+32\,\text{nC}$, because the vest lost about $2.0 \times 10^{11}$ electrons to the jersey
    D: |-
      Zero, because only the synthetic jersey gets charged when the two are rubbed
  answer: C
  explanation: |-
    Charge is conserved: the total was zero before, so it is zero after, and the vest must be $+32\,\text{nC}$. It got that charge by losing electrons: $32 \times 10^{-9} / 1.6 \times 10^{-19} = 2.0 \times 10^{11}$ electrons.
  misconceptions:
    A: |-
      Gets the right charge but the wrong mechanism: thinks protons move during rubbing. Protons are locked in the nuclei; only electrons transfer.
    B: |-
      Thinks rubbing charges both objects alike. Rubbing separates charge, so the two objects end with opposite charges.
    D: |-
      Thinks only one of the two rubbed materials becomes charged, forgetting that the charge the jersey gained had to come from somewhere.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A storm over a cricket ground: dark clouds, distant lightning, players walking off, groundstaff dragging a plastic cover and a team bus waiting](scenes/cricket/electric_charges_fields.svg "Rain has stopped play. Rubbing, sparks and lightning: this whole chapter is in the picture.")

Rain stops play just after tea. In the dressing room the lights flicker and then go out, and the room is dim while the groundstaff scramble outside.

Kabir, soaked from fielding at deep square leg, peels off his polyester training jersey over the cotton vest underneath. There's a sharp *crackle*, and in the gloom everyone sees tiny blue sparks run across the fabric. His hair lifts and follows the jersey.

"You're charging up like a thundercloud," laughs Nikhil, the wicket-keeper.

Kabir isn't laughing. He's curious. The jersey and the vest were both perfectly ordinary a second ago, and he didn't plug anything in. So where did the electricity come from? Was it *made* by the rubbing? And if the jersey is now charged, what happened to the vest?

## The physics

**Electric charge** is a basic property of matter, like mass. There are exactly **two kinds**, named positive and negative (the names are a convention, due to Benjamin Franklin). **Like charges repel; unlike charges attract.** A body is **neutral** when it has equal amounts of both.

Ordinary matter is built from protons (positive), electrons (negative) and neutrons (no charge). The protons sit deep inside the nuclei. The outer electrons of some atoms are held loosely, and when two different materials are rubbed together, **electrons move from one to the other**. That's what happened to Kabir's clothes: electrons were transferred between vest and jersey. Which way they go depends on the pair of materials; for polyester rubbed on cotton, the polyester usually ends up negative.

Charge has three properties you must be able to state and use.

**1. Additivity.** Charge is a scalar, and the total charge of a system is the algebraic sum of its parts, signs included. A body holding $+5\,\text{nC}$, $-8\,\text{nC}$ and $+1\,\text{nC}$ has total charge $-2\,\text{nC}$.

**2. Quantisation.** Charge comes only in whole-number multiples of a basic unit $e$, the magnitude of the charge on an electron or proton:

$$q = ne, \qquad n = 0, \pm1, \pm2, \ldots, \qquad e = 1.6 \times 10^{-19}\,\text{C}$$

No free object carries $0.5e$ or $1.5e$. (Quarks do carry fractional charges, but they are never found alone.)

**3. Conservation.** The total charge of an isolated system never changes. Charge can be *transferred* from one body to another, but it is not created or destroyed by rubbing.

![Before rubbing, cotton and polyester are each neutral; after rubbing, three electrons have moved to the polyester, making it minus 3e and the cotton plus 3e](figures/electric_charge/rubbing-transfers-electrons.svg "Rubbing moves electrons, never protons. One side ends positive, the other negative, and the total stays zero.")

So the answer to Kabir's question: the rubbing didn't make charge. It **separated** charge that was already there. The crackle and sparks are the separated charges jumping back across tiny gaps of air.

## Worked example

**Given:** after the jersey comes off, it carries $q = -32\,\text{nC}$ (an illustrative value). Both garments started neutral.
**Find:** (a) how many electrons were transferred; (b) the charge on the vest.

(a) Convert first: $32\,\text{nC} = 32 \times 10^{-9}\,\text{C} = 3.2 \times 10^{-8}\,\text{C}$. From $q = ne$:

$$n = \frac{|q|}{e} = \frac{3.2 \times 10^{-8}}{1.6 \times 10^{-19}} = 2.0 \times 10^{11}\ \text{electrons}$$

(b) By conservation, total charge before $=$ total after $= 0$:

$$q_\text{vest} + (-32\,\text{nC}) = 0 \quad\Rightarrow\quad q_\text{vest} = +32\,\text{nC}$$

The vest *lost* those $2.0 \times 10^{11}$ electrons, so it is positive.

**Sanity check:** $n$ must be a whole number; $2.0 \times 10^{11}$ is, to the precision given. Reversing, $2.0 \times 10^{11} \times 1.6 \times 10^{-19} = 3.2 \times 10^{-8}\,\text{C}$, as we started.

## Where the picture breaks

Two hundred billion electrons sounds like a lot, but a shirt contains roughly $10^{24}$ or more electrons in total, so only a tiny fraction moved. That's why quantisation is invisible in everyday charges: steps of $1.6 \times 10^{-19}\,\text{C}$ are far too small to notice, and charge seems continuous.

Real clothes aren't a tidy isolated pair either. Charge leaks away through damp air and your skin; on a humid day you often get no crackle at all. The "polyester goes negative" rule depends on surface condition and humidity, so treat it as a tendency, not a law.

## Key takeaway

There are two kinds of charge: like charges repel, unlike attract. Charge is **additive** (add with signs), **quantised** ($q = ne$, with $e = 1.6 \times 10^{-19}\,\text{C}$) and **conserved**. Rubbing doesn't create charge; it moves electrons from one body to another, leaving equal and opposite charges behind.
