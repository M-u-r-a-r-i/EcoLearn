---
concept_id: coulombs_law
interest: football
format: explain
title: Two foam balls that refuse to hang straight
check:
  question: |-
    Two small charged foam balls hang $0.20\,\text{m}$ apart and repel each other with a force of $0.018\,\text{N}$. Priya swaps one ball for a similar one carrying **three times** the charge, and moves the pair to $0.60\,\text{m}$ apart. What is the force now?
  options:
    A: |-
      $0.054\,\text{N}$
    B: |-
      $0.0020\,\text{N}$
    C: |-
      $0.0060\,\text{N}$
    D: |-
      $0.018\,\text{N}$, unchanged
  answer: C
  explanation: |-
    $F \propto q_1 q_2 / r^2$. Tripling one charge multiplies the force by 3; tripling the separation divides it by $3^2 = 9$. Together: $0.018 \times 3 / 9 = 0.0060\,\text{N}$.
  misconceptions:
    A: |-
      Applies the charge change but ignores the separation. Moving the balls three times further apart cannot leave the force untouched — the force depends on $r$.
    B: |-
      Applies the inverse-square fall-off but forgets that one charge was tripled, so the answer comes out nine times too small instead of three times.
    D: |-
      Treats the force as proportional to $q/r$ rather than $q/r^2$, so tripling both seems to cancel. The distance enters as a *square*, so the two changes cannot cancel.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A floodlit ground as a storm arrives: lightning above the stand, rain falling, a player peeling off a crackling nylon bib, and two players heading for the metal-roofed dugout](scenes/football/electric_charges_fields.svg "The lightning moves whole coulombs. A rubbed bib moves a few billionths of one.")

Play is abandoned at half-time, and the under-17s are stuck in the clubhouse with the rain drumming on the roof. Ms Pillai, who takes the warm-ups on Saturdays and teaches physics all week, produces two foam practice balls, two lengths of thread and a strip of nylon bib.

She rubs each foam ball with the bib, then hangs the two threads from the same hook on the door frame. The balls should hang side by side, touching. They don't. They swing apart and settle there, each thread leaning out at an angle, holding a gap of about a hand's width between them.

"Nothing's touching them," says Nikhil, waving his hand through the space between. "What's holding them apart?"

"Two things," says Ms Pillai. "How much you rubbed, and how far apart they are. Guess which one matters more."

Priya moves one thread along the door frame so the balls hang three times further apart. The angle collapses to almost nothing. Three times further, and the push has almost vanished — so how exactly does it fade?

## The physics

**Coulomb's law** (Charles-Augustin de Coulomb, 1785, measured with a torsion balance) gives the force between two **point charges** $q_1$ and $q_2$ held at rest a distance $r$ apart:

$$F = k\,\frac{|q_1 q_2|}{r^2}, \qquad k = \frac{1}{4\pi\varepsilon_0} = 9.0 \times 10^{9}\,\text{N m}^2\,\text{C}^{-2}$$

where $\varepsilon_0 = 8.85 \times 10^{-12}\,\text{C}^2\,\text{N}^{-1}\,\text{m}^{-2}$ is the **permittivity of free space**. Read the law in three parts.

- **Size.** Proportional to each charge, and inversely proportional to the **square** of the separation. Double $r$ and the force drops to a quarter; triple it and only a ninth is left.
- **Direction.** Along the straight line joining the charges — repulsive for like charges, attractive for unlike.
- **Pairs.** The force on $q_1$ from $q_2$ is equal in size and opposite in direction to the force on $q_2$ from $q_1$, exactly as Newton's third law demands, even though the two charges may be quite different in size.

![Like charges repel and unlike charges attract; in each pair the two forces are equal in size, opposite in direction and along the line joining the charges](figures/coulombs_law/force-pairs.svg "Equal and opposite, along the joining line: repulsion for like charges, attraction for unlike.")

In vector form, the force on $q_2$ due to $q_1$ is

$$\vec{F}_{21} = \frac{1}{4\pi\varepsilon_0}\,\frac{q_1 q_2}{r^2}\,\hat{r}_{21}$$

with $\hat{r}_{21}$ the unit vector pointing **from $q_1$ towards $q_2$**. Substitute the charges *with* their signs: a positive product gives a force away from $q_1$ (repulsion), a negative product gives one towards it (attraction).

**Conditions:** the charges must be at rest and small compared with $r$, so that each counts as a point. The constant $k$ is the vacuum value; air changes it by well under a percent.

## Worked example

**Given (illustrative):** the two foam balls carry $q_1 = +30\,\text{nC}$ and $q_2 = +20\,\text{nC}$, and hang $r = 0.30\,\text{m}$ apart.
**Find:** the force between them, and what it becomes at $0.60\,\text{m}$.

**Step 1 — into SI units.** $30\,\text{nC} = 3.0 \times 10^{-8}\,\text{C}$ and $20\,\text{nC} = 2.0 \times 10^{-8}\,\text{C}$. Both are positive, so the force will be a push apart.

**Step 2 — the top of the fraction.**

$$k\,q_1 q_2 = 9.0 \times 10^{9} \times (3.0 \times 10^{-8})(2.0 \times 10^{-8}) = 5.4 \times 10^{-6}\,\text{N m}^2$$

**Step 3 — divide by $r^2 = (0.30)^2 = 0.090\,\text{m}^2$.**

$$F = \frac{5.4 \times 10^{-6}}{0.090} = 6.0 \times 10^{-5}\,\text{N}$$

That is the weight of about $6\,\text{mg}$ — a coarse grain of sand resting on your palm. Small, but the balls are light, so the threads lean visibly.

**Step 4 — double the distance.** Nothing else changes, so the force falls by $2^2 = 4$: $1.5 \times 10^{-5}\,\text{N}$.

**Sanity check:** a rubbed bib carries a few nanocoulombs, and everyone knows static pushes hair around but does not knock a ball over — a force of a few grains of sand is the right size.

## Where the picture breaks

The foam balls are not points: the charge is smeared over their surfaces, and once they come close their charge shifts around, so $r$ measured centre to centre stops being exactly right. They are also not isolated — gravity and the threads set the angle at which everything balances, and the damp air quietly drains the charge, which is why the gap closes over a minute or two. Coulomb's law as written is exact only for point charges held at rest; for extended bodies you add up the contributions of many small pieces, which is the next concept.

## Key takeaway

Two point charges push or pull along the line joining them with $F = \dfrac{1}{4\pi\varepsilon_0}\dfrac{|q_1 q_2|}{r^2}$ — like repels like, unlike attracts, and the two forces are always equal and opposite. The inverse **square** is the part to remember: three times further apart means one-ninth of the force.
