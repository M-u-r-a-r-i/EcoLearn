---
concept_id: charging_methods
interest: cricket
format: explain
title: Why grass clippings jump onto the pitch cover
check:
  question: |-
    Farhan holds a negatively charged polythene sheet near, but not touching, a neutral metal sphere on an insulating stand. While the sheet is there, he touches the far side of the sphere with his finger, then takes his finger away. Finally the sheet is removed. What charge is left on the sphere?
  options:
    A: |-
      Positive, because electrons pushed away by the sheet escaped through Farhan to the earth
    B: |-
      Negative, because some of the sheet's charge crossed over to the sphere
    C: |-
      Zero, because the sheet never touched the sphere
    D: |-
      Negative, because electrons flowed from Farhan into the sphere
  answer: A
  explanation: |-
    The negative sheet repels the sphere's free electrons to the far side; touching that side lets them escape to earth. With the finger removed first, the sphere is left short of electrons, so it is positive: charging by induction always gives the opposite sign to the inducing charge.
  misconceptions:
    B: |-
      Confuses induction with conduction. Without contact, no charge passes from the sheet to the sphere; the sheet keeps all its charge.
    C: |-
      Thinks a body can only be charged by contact. Earthing lets charge leave while the sheet holds the rest in place, so the sphere ends up charged.
    D: |-
      Gets the direction of electron flow backwards. The negative sheet repels electrons, so they flow out of the sphere into the earth, not in.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A storm over a cricket ground: dark clouds, distant lightning, players walking off, groundstaff dragging a plastic cover and a team bus waiting](scenes/cricket/electric_charges_fields.svg "The groundstaff drag a plastic cover over dry grass: a giant rubbing experiment.")

It's a hot, dry afternoon before the monsoon, and clouds are building. Farhan's aunt Meena is the head groundsperson, and today he's her helper. Together they drag the big polythene cover across the freshly mown outfield towards the practice pitch.

When Farhan lifts a corner of the sheet, something strange happens. Dry grass clippings leap up off the ground and cling to the plastic, as if it were a magnet. His forearm hairs rise towards it too.

Curious, he rubs the steel handle of the heavy roller hard with his handkerchief and holds it near the clippings. Nothing. Not one clipping moves.

Two puzzles. The clippings were never rubbed, so why are they pulled up to the sheet? And why can a sheet of plastic be charged by rubbing, while a steel handle, rubbed just as hard, stays stubbornly uncharged?

## The physics

**Conductors and insulators.** In a **conductor** some electrons are free to move through the material: metals, the human body, the earth, and anything damp. In an **insulator** (plastic, glass, rubber, dry grass) the electrons are bound to their atoms, so charge placed on it stays where it was put.

That explains the roller. Rubbing the steel *does* move charge, but the steel is a conductor, and Farhan is holding it. Any charge flows straight through the metal, through his body and into the ground. Mounted on an insulating handle, the same steel could be charged. The polythene, an insulator, keeps the charge that rubbing on the grass gave it.

There are three ways to charge a body.

1. **Friction.** Rubbing two different materials transfers electrons from one to the other, leaving them with equal and opposite charges. This charged the cover.
2. **Conduction.** Touching a charged body to an uncharged conductor lets charge flow between them. The shared charge has the **same sign** as the original.
3. **Induction.** A charged body is brought *near* a conductor without touching. Its field pushes the conductor's free electrons to one side, leaving the near side with the **opposite** charge. If the far side is then connected to earth, the repelled charge escapes; disconnect the earth, remove the charged body, and the conductor is left with a charge **opposite** to the inducing one. The charged body loses nothing.

![Four panels showing charging a metal sphere by induction: neutral; negative rod near separates charge; far side earthed so electrons flow to earth; earth and rod removed leave the sphere positive](figures/charging_methods/induction-steps.svg "Induction in four steps. Order matters: break the earth connection before taking the rod away, or the electrons simply flow back.")

**Now the clippings.** A dry clipping is an insulator, so its electrons can't flow to one end. But inside each molecule the charges shift slightly under the sheet's charge: the side facing the sheet takes on a slight opposite charge and the far side a slight like charge. The clipping is **polarised** while staying neutral overall. Its opposite-charged side is *nearer* the sheet, and electric forces weaken with distance, so the attraction beats the repulsion. The net pull lifts the light clipping.

This is why attraction alone never proves an object is charged: a charged body attracts neutral ones too. **Repulsion** is the sure test, because only a like charge repels.

## Worked example

**Given:** three identical metal spheres, A, B and C, on insulating stands. A carries $+12\,\text{nC}$; B and C are neutral.
**Find:** the charges after A touches B and is pulled away, and then B touches C.

Identical conducting spheres in contact share charge equally, by symmetry.

A touches B: total $= +12 + 0 = +12\,\text{nC}$, so each gets $+6.0\,\text{nC}$.

B touches C: total $= +6.0 + 0 = +6.0\,\text{nC}$, so each gets $+3.0\,\text{nC}$.

Final: A $= +6.0\,\text{nC}$, B $= +3.0\,\text{nC}$, C $= +3.0\,\text{nC}$.

**Sanity check:** the total is $6.0 + 3.0 + 3.0 = 12\,\text{nC}$, exactly what we started with. Conduction redistributes charge; it never changes the total, and every sphere gets the same sign as the original.

## Where the picture breaks

The equal-sharing rule works only for *identical* conductors; a large sphere touching a small one takes more than half. Real grass isn't perfectly dry or perfectly insulating either, and on a humid day the sheet's charge leaks away through the moist air and grass, so the clippings stop jumping. The cricket ground is the setting here, not an analogy: this is the physics of charging, seen on a real outfield.

## Key takeaway

Conductors let charge move freely; insulators hold it in place. Bodies are charged by **friction** (equal and opposite charges), **conduction** (same sign, shared by contact) or **induction** (opposite sign, no contact, via earthing). A charged body also attracts neutral ones by polarising them, so only repulsion proves a charge.
