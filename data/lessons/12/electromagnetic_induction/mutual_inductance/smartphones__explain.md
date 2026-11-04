---
concept_id: mutual_inductance
interest: smartphones
format: explain
title: When a phone lends its charge to a pair of earbuds
check:
  question: |-
    A short coil sits coaxially inside the middle of a long outer solenoid. The outer solenoid is rewound with **twice as many turns** over the same length; the inner coil is unchanged. The current in the **inner** coil is then changed at the same rate as before. How does the emf induced in the outer solenoid compare with before?
  options:
    A: |-
      Four times as large
    B: |-
      Unchanged, because only the inner coil's current is changing
    C: |-
      Twice as large
    D: |-
      Half as large
  answer: C
  explanation: |-
    $M = \mu_0 N_1 N_2 A / l$ is proportional to $N_1$, so doubling the outer turns doubles $M$. Since $M$ is the same whichever coil is driven, the emf in the outer coil, $M\,dI_2/dt$, also doubles.
  misconceptions:
    A: |-
      Squares the number of turns as in self-inductance; mutual inductance contains $N_1 N_2$, so it is linear in each coil's turns.
    B: |-
      Thinks the emf depends only on the coil being driven; the emf appears in the outer coil's turns, so more turns there link more flux and give more emf.
    D: |-
      Thinks the same flux is shared among more turns so each gets less; in fact every turn of the outer coil links the inner coil's flux.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A desk at night with a phone on a wireless charging pad, a shake torch, a hand-crank charger, wired earbuds and a coin beside the pad](scenes/smartphones/electromagnetic_induction.svg "Every gadget on this desk depends on changing magnetic fields. This lesson is about two coils that pass energy to each other without touching.")

Two hours into the bus ride to Pune, Aditya's earbuds give a sad little beep and die. Their case is flat too, and his cable is in the bag under the bus.

Pooja, in the next seat, opens her phone's settings and switches on battery sharing. "Put the case on my back," she says, turning her phone face-down on her knee. Aditya balances the earbuds case on it. Its small light starts to pulse: charging.

Aditya frowns. Pooja's phone charges every night on a wireless pad â€” he has seen it. The coil in the back of her phone is the one that *receives* energy. Now the very same coil is *sending* energy out, to a coil in a case it has never met.

Does a pair of coils care which one is doing the pushing? Would the case charge the phone just as well as the phone charges the case?

## The physics

Put two coils near each other and send a current $I_1$ through coil 1. Its field sends some flux through coil 2, and doubling $I_1$ doubles that flux. So the flux linkage of coil 2 is proportional to $I_1$:

$$N_2\Phi_2 = MI_1$$

The constant $M$ is the **mutual inductance** of the pair, measured in **henry** (H). Change $I_1$ and, by Faraday's law, an emf appears in coil 2:

$$\varepsilon_2 = -M\frac{dI_1}{dt}$$

The key fact, and the answer to Aditya's question: $M$ belongs to the **pair**, not to either coil. Drive coil 2 instead, and a changing $I_2$ induces $\varepsilon_1 = -M\,dI_2/dt$ in coil 1 with the **same** $M$: $M_{12} = M_{21}$. $M$ depends only on the turns, the shared area, the separation and alignment, and what is between the coils â€” never on the current.

The case you must be able to calculate is **two coaxial solenoids**: a long outer solenoid of $N_1$ turns and length $l$, with a shorter coil of $N_2$ turns near its middle enclosing area $A$.

![A long outer solenoid carrying a changing current with a shorter inner coil wound coaxially inside it, connected to a galvanometer](figures/mutual_inductance/coaxial-solenoids.svg "The outer solenoid's field threads the inner coil, so a changing current in one induces an emf in the other. M is the same whichever one you drive.")

The outer field is uniform, $B = \mu_0 N_1 I_1 / l$, and each of the $N_2$ inner turns links a flux $BA$:

$$N_2\Phi_2 = N_2\cdot\frac{\mu_0 N_1 I_1}{l}\cdot A \qquad\Longrightarrow\qquad M = \frac{\mu_0 N_1 N_2 A}{l}$$

This holds for a **long** air-cored solenoid, with the inner coil well inside it so end effects don't matter. The formula is symmetric in $N_1$ and $N_2$ â€” a first hint that $M$ doesn't care which coil is driven.

Pooja's phone and the earbuds case are two flat coils, not solenoids, but the same rule holds. Whether the phone drives the case or a pad drives the phone, the coupling is fixed by how much flux the two coils share.

![Three side views of a driving coil and a pick-up coil: aligned and close, lifted apart, and slid to one side, with fewer field lines through the pick-up coil each time](figures/mutual_inductance/coupling-and-alignment.svg "M is set by how much flux the two coils share. Lift the case away or let it slide off-centre and M falls, and so does the charging.")

## Worked example

**Given:** an outer solenoid of $N_1 = 400$ turns over $l = 0.2\,\text{m}$, and an inner coil of $N_2 = 100$ turns enclosing $A = 4\times10^{-4}\,\text{m}^2$ (the area of a $2\,\text{cm}$ by $2\,\text{cm}$ square).
**Find:** $M$, and the emf in each coil when the other's current changes at $1000\,\text{A/s}$.

**Step 1 â€” the geometry.**

$$\frac{N_1 N_2 A}{l} = \frac{400\times100\times4\times10^{-4}}{0.2} = 80\,\text{m}$$

**Step 2 â€” the mutual inductance.**

$$M = 4\pi\times10^{-7}\times80 \approx 1.0\times10^{-4}\,\text{H} = 0.1\,\text{mH}$$

**Step 3 â€” drive the outer coil.** $|\varepsilon_2| = M\,\dfrac{dI_1}{dt} = 1.0\times10^{-4}\times1000 = 0.1\,\text{V}$ in the inner coil.

**Step 4 â€” swap roles.** Drive the inner coil at the same $1000\,\text{A/s}$ and the outer coil gets $|\varepsilon_1| = 0.1\,\text{V}$ â€” exactly the same, because $M$ is the same.

**Sanity check:** a tenth of a volt from a hand-sized pair of air-cored coils is small, which is why real chargers use alternating current at a very high frequency, making $dI/dt$ enormous.

## Where the picture breaks

The coaxial formula assumes all of the outer coil's flux passes through the inner one. Two flat coils back to back share only part of their flux, so their $M$ is much smaller than a coaxial pair of similar size would give.

Equal $M$ does **not** mean the case could charge the phone as well as the phone charges the case. The *coupling* is symmetric; the circuits are not. The phone has a big battery and electronics built to drive its coil, while the case has a tiny battery and electronics built only to receive. Reverse charging is also slow and wasteful: part of the energy heats nearby metal through eddy currents instead of reaching the earbuds.

And a steady current in either coil induces nothing. The phone must drive its coil with a rapidly alternating current for any energy to cross the gap.

## Key takeaway

Mutual inductance $M$ measures how well two coils share flux: $N_2\Phi_2 = MI_1$, and $\varepsilon_2 = -M\,dI_1/dt$. It is a property of the **pair** â€” the same value whichever coil is driven â€” and depends only on geometry and alignment, not on current. For two coaxial solenoids, $M = \mu_0 N_1 N_2 A / l$.
