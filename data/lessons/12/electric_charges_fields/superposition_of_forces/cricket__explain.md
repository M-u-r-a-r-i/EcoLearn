---
concept_id: superposition_of_forces
interest: cricket
format: explain
title: Three magnets on the captain's tactics board
check:
  question: |-
    On the tactics board, a charge feels a force of $0.30\,\text{N}$ due north from one neighbouring charge and $0.30\,\text{N}$ due east from another. What is the magnitude of the net electric force on it?
  options:
    A: |-
      $0.60\,\text{N}$
    B: |-
      $0.42\,\text{N}$
    C: |-
      $0\,\text{N}$
    D: |-
      $0.30\,\text{N}$
  answer: B
  explanation: |-
    Forces add as vectors. Two perpendicular forces of $0.30\,\text{N}$ give $\sqrt{0.30^2 + 0.30^2} = 0.30\sqrt{2} \approx 0.42\,\text{N}$, pointing north-east.
  misconceptions:
    A: |-
      Adds the magnitudes as plain numbers, ignoring direction; that only works when both forces point the same way.
    C: |-
      Thinks two equal forces always cancel; they cancel only if they point in opposite directions, not at right angles.
    D: |-
      Thinks one charge's force blocks or replaces the other's, so the charge feels only one force. Each force acts independently and both count.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A storm over a cricket ground: dark clouds, distant lightning, players walking off, groundstaff dragging a plastic cover and a team bus waiting](scenes/cricket/electric_charges_fields.svg "Rain means a night in the team hotel, and time to plan tomorrow's field.")

The final has been pushed to the reserve day by rain. In the team hotel lobby, Ananya, the captain, is setting tomorrow's field on a magnetic tactics board: slip, gully, a short leg for the left-hander.

Her older brother Rohan, deep in exam preparation, wanders over and peels three coloured magnets off the side of the board.

"Your fielders are easy," he says. "Each one only cares about where the ball goes. Watch this." He sticks one magnet at a corner and calls it a positive charge. A second, also positive, goes $30\,\text{cm}$ to its right. A third, negative, goes $40\,\text{cm}$ above it.

"The corner charge feels a push from one and a pull from the other, at the same time, in different directions. Which way does it actually go, and how hard?"

Ananya stares at the board. Does one charge's pull get in the way of the other's push? Or do they somehow combine?

## The physics

The answer is the **principle of superposition**:

> The force on any charge due to several other charges is the **vector sum** of the forces each of them would exert on it alone.

$$\vec{F}_1 = \vec{F}_{12} + \vec{F}_{13} + \cdots + \vec{F}_{1n}$$

Each $\vec{F}_{1j}$ is found from Coulomb's law as if the other charges weren't there. The presence of $q_3$ doesn't change the force between $q_1$ and $q_2$; nothing "blocks" or "uses up" an electric force. Then you add the forces **as vectors**, with direction, which is where most mistakes happen.

The method, every time:

1. Draw each force on the chosen charge, with its direction (repel for like, attract for unlike).
2. Find each magnitude with $F = k|q_1 q_2|/r^2$.
3. Resolve into components along axes you choose, add each component, and recombine.

**Continuous charge.** If charge is spread out (along a rod, over a sheet, through a volume), split it into tiny pieces $dq$, treat each as a point charge, and add by integration. The charge per unit length is $\lambda$, per unit area $\sigma$, and per unit volume $\rho$, so $dq = \lambda\,dl$, $\sigma\,dA$ or $\rho\,dV$, and

$$\vec{F} = \frac{q}{4\pi\varepsilon_0}\int \frac{dq}{r^2}\,\hat{r}$$

It's the same principle, with a sum over infinitely many small pieces.

## Worked example

**Given:** Rohan's board, with illustrative charges. $q_0 = +2.0\,\mu\text{C}$ at the corner O; $q_1 = +3.0\,\mu\text{C}$ at $0.30\,\text{m}$ to the right; $q_2 = -4.0\,\mu\text{C}$ at $0.40\,\text{m}$ above O.
**Find:** the net force on $q_0$.

Take $+x$ to the right and $+y$ upwards. Convert: $1\,\mu\text{C} = 10^{-6}\,\text{C}$.

Force from $q_1$ (like charges, so repulsion, pushing $q_0$ in the $-x$ direction):

$$F_1 = \frac{9.0 \times 10^9 \times (2.0 \times 10^{-6})(3.0 \times 10^{-6})}{(0.30)^2} = \frac{0.054}{0.090} = 0.60\,\text{N}$$

Force from $q_2$ (unlike charges, so attraction, pulling $q_0$ towards $q_2$, in the $+y$ direction):

$$F_2 = \frac{9.0 \times 10^9 \times (2.0 \times 10^{-6})(4.0 \times 10^{-6})}{(0.40)^2} = \frac{0.072}{0.16} = 0.45\,\text{N}$$

Add the components: $F_x = -0.60\,\text{N}$, $F_y = +0.45\,\text{N}$.

$$F_\text{net} = \sqrt{0.60^2 + 0.45^2} = \sqrt{0.5625} = 0.75\,\text{N}$$

$$\tan\phi = \frac{0.45}{0.60} = 0.75 \quad\Rightarrow\quad \phi \approx 37^\circ$$

So the net force is $0.75\,\text{N}$, pointing up and to the left, at $37^\circ$ above the $-x$ direction.

![The corner charge feels 0.60 N to the left from the right-hand charge and 0.45 N upwards from the upper charge; the net force is 0.75 N up and to the left at 37 degrees](figures/superposition_of_forces/right-angle-superposition.svg "Each force is worked out on its own, then added head-to-tail. The net force points in neither of the original directions.")

**Sanity check:** $0.60 : 0.45 : 0.75$ is a $4 : 3 : 5$ right triangle. And the net force is bigger than either force alone but smaller than their plain sum, $1.05\,\text{N}$, as it must be for two forces at right angles.

## Where the picture breaks

The tactics board is only the setting. Fielders don't push or pull one another; a real field placing has nothing to do with superposition. The charges are also treated as points fixed in place. In reality $q_1$ and $q_2$ feel forces too and would move unless something held them, and in a real board of magnets the forces would be magnetic, not electric. Superposition itself, though, is exact for electrostatic forces; it's one of the most reliable rules in physics.

## Key takeaway

Each charge exerts its own Coulomb force, unaffected by the others, and the net force is their **vector sum**: $\vec{F}_1 = \vec{F}_{12} + \vec{F}_{13} + \cdots$. Resolve into components, add, recombine. For spread-out charge, split it into pieces $dq$ and integrate.
