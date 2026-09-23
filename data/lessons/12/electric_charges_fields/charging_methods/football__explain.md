---
concept_id: charging_methods
interest: football
format: explain
title: The bottle that rolled without being touched
check:
  question: |-
    Ritika holds a negatively charged plastic rod near one side of an isolated metal ball resting on an insulating stand, and briefly touches the far side of the ball with her finger. To leave the ball with a **positive** charge, what must she do next?
  options:
    A: |-
      Take the rod away first, then lift her finger off the ball.
    B: |-
      Lift her finger off the ball first, then take the rod away.
    C: |-
      Take the rod away and lift her finger off together — the order makes no difference.
    D: |-
      Touch the rod to the ball before removing either.
  answer: B
  explanation: |-
    While the rod is near, electrons are pushed to the far side and escape through her finger to earth. Breaking that path first traps the shortage of electrons on the ball, so it is left positive once the rod goes.
  misconceptions:
    A: |-
      Forgets that the electrons are still free to return. With the rod gone, the earthed ball simply pulls electrons back through the finger and ends up neutral.
    C: |-
      Thinks only the final state matters, not the order of the steps. In induction the order *is* the method: earth first, then break the earth, then remove the rod.
    D: |-
      Confuses induction with conduction. Touching a negative rod to the ball shares electrons onto it, leaving it negative, not positive.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A floodlit ground as a storm arrives: lightning above the stand, rain falling, a player peeling off a crackling nylon bib, and two players heading for the metal-roofed dugout](scenes/football/electric_charges_fields.svg "Nylon bibs, a plastic ball pump, aluminium bottles, steel goalposts — a kit room is a box of conductors and insulators.")

Ritika runs the kit room, and on rainy evenings she runs experiments on whoever is waiting for the bus.

She takes the plastic tube off the ball pump and rubs it hard down the sleeve of her fleece. Then she lays an empty aluminium water bottle on its side on the bench — the bottle is not charged, nobody has rubbed it — and brings the tube close to it without touching.

The bottle rolls. Slowly, then decidedly, straight towards the tube.

"You touched it," says Dhruv.

"I didn't." She does it again, a hand's width away, and the bottle rolls again. Then she carries the tube over to the steel goalpost frame stacked against the wall and holds it there. Nothing. She touches the frame with her other hand. Still nothing.

An uncharged bottle is pulled by a charged tube, but a metal frame standing on the concrete floor refuses to play. Why does it matter what the object is standing on?

## The physics

Materials split into two groups by how freely electrons move inside them.

- In a **conductor** (metals, the human body, damp earth) some electrons are free to travel through the whole object. Charge placed anywhere spreads out, and can drain away entirely if there is a path to earth.
- In an **insulator** (nylon, PVC, dry glass, rubber) electrons stay put where they are. Charge sits where you put it, which is why you can rub a spot on a plastic tube and it stays charged.

There are three ways to charge something.

**Friction.** Rub two different insulators; electrons move from one to the other. Both end up charged, equally and oppositely — the tube and the fleece.

**Conduction.** Touch a charged conductor to a neutral one. Free electrons flow until the charge is shared, and both objects are left with the **same sign**.

**Induction.** No contact at all, and this is the one that moved the bottle.

![Four panels showing charging a metal sphere by induction: neutral; negative rod near separates charge; far side earthed so electrons flow to earth; earth and rod removed leave the sphere positive](figures/charging_methods/induction-steps.svg "Induction in four steps. Order matters: break the earth connection before taking the rod away, or the electrons simply flow back.")

Bring a charged rod near an isolated conductor. Its free electrons are pushed away (by a negative rod) or pulled towards it (by a positive one), so the near face carries charge opposite to the rod and the far face carries the same sign as the rod. **The object is still neutral overall** — but the opposite charge is now nearer to the rod than the like charge, and because the electrostatic force weakens with distance, the attraction wins. That is why a neutral bottle rolls.

To keep the charge, earth the far face while the rod is held near, so the pushed-away electrons leave. Then **break the earth connection first**, and only then remove the rod. The object is left permanently charged, with the sign *opposite* to the rod.

The goalpost frame fails because it is a conductor touching the concrete floor: any charge separated in it drains straight to earth.

## Worked example

**Given:** an isolated metal ball carries $+8\,\text{nC}$. An identical, uncharged ball on an insulating stand is touched to it and separated.
**Find:** the charge on each, and on each of three identical balls after the second one is then touched to a third uncharged ball.

**Step 1 — first contact.** The two balls are identical, so the free charge shares equally between them. Total charge is conserved:

$$q_\text{each} = \frac{+8\,\text{nC}}{2} = +4\,\text{nC}$$

Both are now at $+4\,\text{nC}$, and the total is still $+8\,\text{nC}$.

**Step 2 — second contact.** Ball two ($+4\,\text{nC}$) touches an uncharged third ball: that $4\,\text{nC}$ halves again, giving $+2\,\text{nC}$ each.

So the three balls end at $+4$, $+2$ and $+2\,\text{nC}$, adding to $+8\,\text{nC}$ — the charge we started with, just spread thinner.

**Sanity check:** nothing was lost and nothing was made. Equal sharing needs the balls to be identical in size and far from everything else; unequal spheres share in proportion to their size, not half and half.

## Where the picture breaks

The bottle rolls because it is a conductor free to move on a bench — a real induction demonstration uses a metal sphere on an insulating stand, so it cannot dash to the rod and discharge. A paper ball or a thin stream of water is also attracted, and there the electrons are not free to travel; they only shift slightly inside each molecule. That is polarisation, not conduction, and you will meet it properly with dielectrics. Finally, "conductor" and "insulator" are ends of a range, not two boxes: humid air and a sweaty glove conduct far better than dry ones, which is why these demonstrations are moody.

## Key takeaway

Conductors let electrons roam and can be drained to earth; insulators hold charge where you put it. Friction moves electrons between two insulators, conduction shares charge on contact and leaves both the same sign, and induction charges a conductor without touching it — leaving the opposite sign, provided you break the earth connection **before** you remove the rod.
