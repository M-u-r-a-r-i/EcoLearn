---
concept_id: superposition_of_forces
interest: gaming
format: explain
title: The bug that let the nearest node win
check:
  question: |-
    In Tanish's puzzle game, a charged token feels a force of $0.80\,\text{N}$ due east from one node and $0.60\,\text{N}$ due north from another. What is the magnitude of the net electric force on the token?
  options:
    A: |-
      $1.4\,\text{N}$
    B: |-
      $0.20\,\text{N}$
    C: |-
      $0.80\,\text{N}$
    D: |-
      $1.0\,\text{N}$
  answer: D
  explanation: |-
    Forces add as vectors. At right angles, $F_\text{net} = \sqrt{0.80^2 + 0.60^2} = \sqrt{1.00} = 1.0\,\text{N}$, pointing north of east.
  misconceptions:
    A: |-
      Adds the magnitudes as plain numbers. That is only correct when the two forces point the same way.
    B: |-
      Subtracts the magnitudes, as if the two forces opposed each other. They are at right angles, so neither cancels the other.
    C: |-
      Thinks the stronger charge's pull overrides the weaker one, so only one force acts. Every force acts independently and all of them count.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A gaming desk at night during a PC build: a monitor running a field sandbox with two charges, a plasma globe, an antistatic bag sparking to a fingertip, and an open PC case with a graphics card going in](scenes/gaming/electric_charges_fields.svg "Add a third charge to the sandbox on the screen and the arrows all change. Why?")

Tanish's puzzle game has one rule: the player drags a glowing token through a maze of charged nodes, some pushing and some pulling, and has to land it in a slot without touching the walls.

Level seven is where the bug lives. He drops the token between a pushing node on its right and a pulling node above it — and the token slides straight left, as if the pulling node were switched off. Every tester finds it. Every tester calls it unfair.

He opens the code and finds what his tired self wrote at the jam: *find the nearest node, apply its force.* One node, one force. The nearest one wins.

Tanish is not sure that is wrong, though, and that is what bothers him. When a charge sits between two others, does the stronger one somehow shield the weaker? Does the nearer pull get in the way of the further push? Or do the two somehow act at once?

## The physics

The answer is the **principle of superposition**:

> The force on any charge due to several other charges is the **vector sum** of the forces each of the others would exert on it alone.

$$\vec{F}_1 = \vec{F}_{12} + \vec{F}_{13} + \cdots + \vec{F}_{1n}$$

Each $\vec{F}_{1j}$ is worked out from Coulomb's law exactly as if no other charge existed. Nothing blocks, shields or uses up an electric force: putting $q_3$ into the picture does not change the force between $q_1$ and $q_2$ by so much as a newton. Tanish's "nearest node wins" is therefore wrong in the strongest possible way — *every* node acts, always, all at once.

The catch is in the word **vector**. You add the forces with their directions, and that is where marks are lost. The method, every time:

1. Draw each force on the chosen charge, with its direction: away for a like charge, towards for an unlike one.
2. Find each magnitude from $F = k|q_1 q_2| / r^2$.
3. Resolve them along axes you choose, add the components separately, then recombine.

**Continuous charge.** If the charge is spread out — along a wire, over a plate, through a block — split it into tiny pieces $dq$, treat each piece as a point charge, and add by integration. With charge per unit length $\lambda$, per unit area $\sigma$ and per unit volume $\rho$, the piece is $dq = \lambda\,dl$, $\sigma\,dA$ or $\rho\,dV$, and

$$\vec{F} = \frac{q}{4\pi\varepsilon_0}\int \frac{dq}{r^2}\,\hat{r}$$

Same principle; just infinitely many terms.

## Worked example

**Given (illustrative):** a token of charge $q_0 = +2.0\,\mu\text{C}$ at the origin O. A node $q_1 = +3.0\,\mu\text{C}$ sits $0.30\,\text{m}$ to its right, and a node $q_2 = -4.0\,\mu\text{C}$ sits $0.40\,\text{m}$ directly above it.
**Find:** the net force on the token.

Take $+x$ to the right and $+y$ upwards.

**Step 1 — the push from $q_1$.** Like charges, so it points in the $-x$ direction:

$$F_1 = \frac{9.0 \times 10^9 \times (2.0 \times 10^{-6})(3.0 \times 10^{-6})}{(0.30)^2} = \frac{0.054}{0.090} = 0.60\,\text{N}$$

**Step 2 — the pull from $q_2$.** Unlike charges, so it points in the $+y$ direction, towards $q_2$:

$$F_2 = \frac{9.0 \times 10^9 \times (2.0 \times 10^{-6})(4.0 \times 10^{-6})}{(0.40)^2} = \frac{0.072}{0.16} = 0.45\,\text{N}$$

Notice that the bigger charge gives the *smaller* force here, because it is further away — a good reason never to trust "the nearest one wins".

**Step 3 — add them.** The two are at right angles, so

$$F_\text{net} = \sqrt{(0.60)^2 + (0.45)^2} = \sqrt{0.5625} = 0.75\,\text{N}, \qquad \tan\phi = \frac{0.45}{0.60} \Rightarrow \phi \approx 37^\circ$$

The token is pushed up and to the left, at about $37^\circ$ above the leftward direction — a direction neither node would have given on its own.

![A charge at a corner feels 0.60 N to the left from a charge 0.30 m to its right and 0.45 N upwards from a charge 0.40 m above; the two add head to tail to a net 0.75 N at 37 degrees](figures/superposition_of_forces/right-angle-superposition.svg "Each force is found alone, then the two are added head to tail. The net force points along neither of them.")

**Sanity check:** $0.60 : 0.45 : 0.75$ is the familiar $4:3:5$ triangle, and the answer sits between the larger single force and the plain sum $1.05\,\text{N}$, exactly where two perpendicular forces should land.

## Where the picture breaks

The game treats the nodes as fixed points, and this calculation does too. Real charges feel the forces they exert: $q_1$ and $q_2$ would fly apart unless something held them, and once anything moves, every distance in the working changes.

The token is also not really a point — and in a game none of this is physics anyway, since a jam entry can use whatever rule feels good. What carries over exactly is superposition itself, which is one of the most reliable rules in all of physics: electrostatic forces simply add, with no interference between them.

## Key takeaway

Every charge exerts its own Coulomb force, unaffected by the presence of the others, and the net force is their **vector sum**: $\vec{F}_1 = \vec{F}_{12} + \vec{F}_{13} + \cdots$. Resolve into components, add, recombine. Nothing shields or blocks an electric force, and for spread-out charge you split it into pieces $dq$ and integrate.
