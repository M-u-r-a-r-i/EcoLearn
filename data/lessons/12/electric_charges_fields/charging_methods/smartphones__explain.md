---
concept_id: charging_methods
interest: smartphones
format: explain
title: The wrist strap at the phone repair counter
check:
  question: |-
    A neutral metal phone stand sits on an insulating rubber mat. Kabir holds a **positively** charged plastic rod near it without touching, touches the far side of the stand with his finger, takes his finger away, and only then takes the rod away. What charge does the stand end up with?
  options:
    A: |-
      Positive, the same sign as the rod
    B: |-
      Negative
    C: |-
      Neutral, because the rod never touched the stand
    D: |-
      Neutral, because the finger let any extra charge drain away
  answer: B
  explanation: |-
    The positive rod attracts electrons towards it. While the finger is on the stand, extra electrons flow up from the earth through Kabir's body into the stand. Removing the finger traps them, so the stand is left negative, opposite to the rod: that is charging by induction.
  misconceptions:
    A: |-
      Mixes up induction with conduction. Touching the rod to the stand would share its positive charge; induction without contact always leaves the opposite sign.
    C: |-
      Thinks charge can only be given by contact with the charged object. In induction the charge comes from the earth; the rod only decides which way it flows.
    D: |-
      Thinks earthing always leaves a body neutral. With the rod still close, earthing lets electrons flow in until the rod's pull is balanced, and they stay once the earth link is broken.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A desk by a sunny window with a solar power bank on the sill, an opened phone box with foam beads clinging to the new phone, a film being peeled off a screen with dust jumping up to it, and a phone on a stand running a field-line app](scenes/smartphones/electric_charges_fields.svg "The foam beads by the box are clinging to the phone without touching anything charged on purpose. The same forces are at work at every repair counter.")

It's a cold December evening at Kabir's uncle's phone-repair counter. Before Mamaji opens any phone, he clips a black strap round his wrist; its wire runs to a screw on the earthed metal bench. Kabir has always thought it was just a habit.

While he waits, Kabir rubs his plastic phone case on his woollen sweater and holds it over the counter. Tiny curls of aluminium foil, stripped off an old cable, jump up to it. So do specks of paper from a torn receipt.

That puzzles him. The foil is a metal; the paper is not. Neither was charged, and he hasn't touched either one. Why are both pulled up? And why does his uncle, whose hands are the only thing touching the phone, need to be wired to the bench?

## The physics

**Conductors** are materials with **free electrons** that can move through the whole body: metals such as a phone's aluminium frame and the copper tracks on its circuit board, and also the human body and the earth. **Insulators** hold their electrons tightly to their atoms, so charge put on one spot stays there: glass, plastic cases, rubber, paper, dry air.

There are three ways to charge a body.

1. **By friction.** Rubbing two different insulators transfers electrons from one to the other. Kabir's case and his sweater end up with equal and opposite charges.
2. **By conduction (contact).** Touch a charged body to a neutral conductor and some of the charge spreads onto it. The conductor ends up with the **same sign** as the charged body.
3. **By induction.** Bring a charged body **near** a conductor without touching. Its free electrons shift: towards a positive body, away from a negative one. Earth the conductor for a moment and charge flows between it and the earth. Break the earth link first, then remove the charged body, and the conductor keeps a charge of the **opposite sign**.

![Four panels showing charging a metal sphere by induction: neutral; negative rod near separates the charge; far side earthed so electrons flow to earth; earth and rod removed leave the sphere positive](figures/charging_methods/induction-steps.svg "Induction in four steps. Break the earth link before taking the rod away, or the electrons simply flow back.")

The same shifting of charge explains the foil and the paper. Near the charged case, the neutral foil's electrons rearrange so the side facing the case carries the opposite sign. That side is closer, so its attraction beats the repulsion on the far side, and the foil jumps. In paper, electrons can't travel far, but each molecule's charges shift slightly (it **polarises**), with the same result: a net pull.

And the wrist strap? A technician walking about can pick up a large charge by friction. The strap is a conducting path to earth, so any charge on the body drains away gently instead of jumping as a spark into a tiny chip.

## Worked example

**Given (illustrative):** Kabir's rubbed case is negative. He holds it near a neutral aluminium phone stand on a rubber mat and touches the far side of the stand. Say $1.25 \times 10^{10}$ electrons are pushed off through his body into the earth. He lifts his finger, then takes the case away. ($e = 1.6 \times 10^{-19}\,\text{C}$.)
**Find:** the stand's final charge.

**Step 1 — which way do electrons go?** The negative case repels electrons, so they leave the stand through his finger. The stand is now short of electrons.

**Step 2 — how much charge left?** Charge carried away:
$$q = ne = 1.25 \times 10^{10} \times 1.6 \times 10^{-19} = 2.0 \times 10^{-9}\,\text{C}$$
The stand is left with $+2.0\,\text{nC}$.

**Step 3 — after removing the case.** The finger went first, so the electrons cannot come back. The $+2.0\,\text{nC}$ spreads over the stand's surface, opposite in sign to the case, which lost none of its own charge.

**Sanity check:** had Kabir touched the case to the stand instead, the stand would have gone negative, like the case; opposite signs mean induction, same signs mean conduction.

## Where the picture breaks

A human body is a fair conductor and is usually connected to the ground through shoes and floor, but not perfectly: rubber soles on a dry winter day are exactly why technicians use a strap instead of trusting their feet. Real straps also include a large resistor so that charge drains slowly and safely. And "conductor" and "insulator" are two ends of a range: damp paper or a sweaty hand conduct far better than dry ones, which is why static tricks work best on cold, dry days.

## Key takeaway

Conductors have free electrons that move through the body; insulators hold their charge where it is put. Friction moves electrons between two surfaces, conduction shares charge of the **same** sign by contact, and induction (near, earth, break earth, remove) leaves a conductor with the **opposite** sign without ever touching it.
