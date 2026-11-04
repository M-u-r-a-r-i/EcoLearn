---
concept_id: charging_methods
interest: gaming
format: explain
title: Why the technician touches the case first
check:
  question: |-
    Ishita holds a negatively charged plastic panel near one side of a metal PC case standing on rubber feet. With the panel still in place she touches the far side of the case with a finger. Then she takes the **panel** away first, and only afterwards lifts her finger. What is the case left with?
  options:
    A: |-
      A positive charge, because the electrons that escaped to earth cannot come back.
    B: |-
      A negative charge, because some of the panel's charge spreads onto the case as it leaves.
    C: |-
      No charge at all, because with her finger still touching, electrons flow back from the earth as the panel leaves.
    D: |-
      A negative charge, because her finger keeps feeding electrons in for as long as it touches.
  answer: C
  explanation: |-
    Induction only leaves a charge behind if the earth connection is broken **while** the charged body still holds the opposite charge in place. Remove the panel first and the leftover positive charge simply pulls electrons back up through her finger, leaving the case neutral.
  misconceptions:
    A: |-
      Treats the earthing step as final, forgetting that the finger is still an open path to earth, so charge can flow back the moment the panel's hold is released.
    B: |-
      Confuses induction with conduction. Without contact no charge crosses from the panel, and the panel keeps all of its own charge throughout.
    D: |-
      Thinks earthing pumps electrons in continuously. Electrons flow only while something attracts or repels them; the flow stops the instant the case is neutral.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A gaming desk at night during a PC build: a monitor running a field sandbox with two charges, a plasma globe, an antistatic bag sparking to a fingertip, and an open PC case with a graphics card going in](scenes/gaming/electric_charges_fields.svg "Look at the wrist strap clipped to the bare metal of the case, and at the dust stuck to the screen.")

The school's esports room is being set up for a weekend tournament, and Ishita, who runs the club, has volunteered to clean twelve machines before the teams arrive.

The monitors infuriate her. She wipes a screen, and an hour later it has a fresh grey bloom of dust on it, while the metal desk frame beside it stays clean. Meanwhile the plastic keyboard covers cling to her hands and to each other.

The technician arrives with the last graphics card. Before he opens the case he clips a wrist strap to the bare metal of the chassis. "Cheap insurance," he says. Ishita, curious, rubs a steel chair leg hard with her dusting cloth and holds it over the dust. Nothing. Not one speck moves.

Two puzzles. The dust was never rubbed on anything, so why is it attracted to the screen? And why can plastic be charged by rubbing while steel, rubbed just as hard, stays stubbornly dead?

## The physics

**Conductors and insulators.** In a **conductor** some electrons are free to roam through the material: metals, the human body, the earth, anything damp. In an **insulator** — plastic, glass, rubber, dry dust — the electrons are bound to their own atoms, so charge stays exactly where it is put.

That settles the chair leg. Rubbing steel *does* move electrons, but steel is a conductor and Ishita is holding it, so the charge runs straight through the metal, through her, and into the ground. Mounted on an insulating stand, the same steel would charge nicely. The plastic covers, being insulators, keep whatever rubbing gives them.

There are three ways to charge a body.

1. **Friction.** Rubbing two different materials transfers electrons one way, leaving them with equal and opposite charges.
2. **Conduction.** Touching a charged body to an uncharged conductor lets charge flow across. Both end up with the **same sign**.
3. **Induction.** A charged body is brought *near* a conductor without touching. It pushes the conductor's free electrons to one side, so the near side takes the **opposite** charge. Earth the far side and the repelled charge escapes; break the earth connection, then take the charged body away, and the conductor is left with a charge **opposite** to the inducing one — which never lost any of its own.

![Four panels showing a metal sphere charged by induction: neutral, then a negative rod nearby separates the charge, then the far side is earthed so electrons escape, then the earth and the rod are removed leaving the sphere positive](figures/charging_methods/induction-steps.svg "Induction in four steps. The order matters: break the earth connection before the rod is taken away, or the electrons simply flow back.")

**Now the dust.** A dust speck is an insulator, so its electrons cannot travel to one end. But inside each molecule the charges shift a little in the screen's field: the side facing the charged screen takes a slight opposite charge, the far side a slight like charge. The speck is **polarised** while staying neutral overall. Its opposite side is the *nearer* one, and electric forces weaken with distance, so the attraction beats the repulsion and the speck is pulled in.

This is why attraction never proves that something is charged — a charged body attracts neutral things too. **Repulsion is the sure test**, because only a like charge repels.

## Worked example

**Given (illustrative):** the plastic panel carries $-20\,\text{nC}$. Ishita earths the case, lifts her finger, then removes the panel, and the case is left with $+8.0\,\text{nC}$.
**Find:** how many electrons left through her finger, and what the panel now carries.

Every electron carries $e = 1.6 \times 10^{-19}\,\text{C}$, and $8.0\,\text{nC} = 8.0 \times 10^{-9}\,\text{C}$, so

$$n = \frac{8.0 \times 10^{-9}}{1.6 \times 10^{-19}} = 5.0 \times 10^{10}$$

Fifty billion electrons went down to earth — and because they *left*, the case is positive, the opposite sign to the panel that pushed them.

The panel touched nothing, so it still carries $-20\,\text{nC}$. Induction costs the inducing body nothing at all.

**Sanity check:** the case ends up with less charge than the panel, which is right — the panel only repels some of the free electrons far enough to reach the finger, not all of them.

## Where the picture breaks

The case is not a neat isolated conductor: it sits on rubber feet here, but plug in the power cable and it is earthed permanently, so induction has nothing to hold. Nor is the case the real reason a wrist strap works. The strap protects the card by keeping *you* and the case at the same charge, so no spark can jump between you — not by charging the case up.

And "dry dust is an insulator" is a fair-weather rule. On a humid day a film of water makes dust and plastic slightly conducting, charge leaks away, and the screen stays clean by itself.

## Key takeaway

Conductors let charge move; insulators pin it in place. You can charge a body by **friction** (equal and opposite charges), by **conduction** (same sign, shared on contact) or by **induction** (opposite sign, no contact, using an earth connection that you break first). A charged body also attracts neutral objects by polarising them, so only repulsion proves a charge.
