---
concept_id: gravitational_potential_energy
interest: football
format: explain
title: The drone drop and the ball with negative energy
check:
  question: |-
    Taking potential energy to be zero at infinity, a football resting on the Earth's surface has gravitational potential energy $U_0$ (a negative number). What is its potential energy at a height $R$ above the surface, where $R$ is the Earth's radius?
  options:
    A: |-
      $U_0/4$
    B: |-
      $U_0/2$
    C: |-
      $2U_0$
    D: |-
      $0$
  answer: B
  explanation: |-
    $U = -GMm/r$. At the surface $r = R$ and $U_0 = -GMm/R$; at height $R$, $r = 2R$, so $U = -GMm/2R = U_0/2$. It is still negative, but half as large in size.
  misconceptions:
    A: |-
      Uses $1/r^2$, the way the force depends on distance; potential energy goes as $1/r$.
    C: |-
      Thinks the potential energy becomes more negative as the ball goes higher; $U$ rises towards zero with height.
    D: |-
      Adds $mgh$ with $h = R$: since $U_0 = -mgR$, this gives zero. But $mgh$ holds only for $h \ll R$ and overestimates the rise here.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A night match: the goalkeeper's long kick at the top of its arc, the Moon and a satellite overhead, and a dish on the stand roof aimed at the satellite](scenes/football/gravitation.svg "A ball high above the pitch has more potential energy than one on the grass. But how much does the ball on the grass have?")

The academy has a new training drill. A drone carries a ball forty metres above the pitch and releases it, and the goalkeepers take turns catching it cleanly. Priyanka takes the first one: a hard sting in the gloves, but she holds it.

On the touchline, Dev is doing sums. "Forty metres, $0.43$ kilograms. That's $mgh$, about $170$ joules of potential energy, all turned into kinetic energy by the time it hit your gloves."

Priyanka takes off her gloves and picks up Dev's physics textbook. "This says the potential energy of a ball on the ground is about minus twenty-seven *million* joules."

"Minus? It's just sitting on the grass!"

"And it says $mgh$ is only an approximation."

"Approximation of what?" says Dev. "It works for your catch."

Can energy really be negative? And if $mgh$ isn't the whole story, when does it fail?

## The physics

The formula $mgh$ assumes that $g$ stays the same all the way up. For forty metres that's fine. But gravity weakens with distance from the Earth, so for large heights we need a better formula.

The **gravitational potential energy** of a mass $m$ at distance $r$ from the centre of a body of mass $M$ ($r$ at or outside its surface) is

$$U = -\frac{GMm}{r}$$

with the **zero at infinity**, where the two bodies no longer interact. $U$ is the work done by an external agent in bringing $m$ slowly from infinity to $r$. Gravity pulls $m$ inward the whole way, so the agent must hold it back, and that work is negative:

$$U(r) = \int_{\infty}^{r} \frac{GMm}{x^2}\,dx = -\frac{GMm}{r}$$

Negative doesn't mean "less than nothing". It means the ball is **bound**: you would have to *supply* energy to pull it free of the Earth. As $r$ increases, $U$ rises towards zero.

The **gravitational potential** is the potential energy per unit mass, $V = U/m = -GM/r$, measured in $\text{J/kg}$.

**Where $mgh$ comes from.** Raise the ball from the surface ($r = R$) to height $h$:

$$\Delta U = GMm\left(\frac{1}{R} - \frac{1}{R+h}\right) = \frac{GMm\,h}{R(R+h)}$$

When $h \ll R$, $R + h \approx R$, and with $GM/R^2 = g$ this becomes $\Delta U \approx mgh$. So $mgh$ is the near-surface approximation to the *change* in potential energy.

![A graph of U against r over R: a red curve rising from minus one towards zero, and a grey dashed straight line leaving the surface along the curve then climbing too fast](figures/gravitational_potential_energy/u-vs-r-and-mgh.svg "Near the surface, the straight mgh line hugs the true curve. Far out, it climbs much too fast.")

## Worked example

**Given:** ball $m = 0.43\,\text{kg}$; $g = 9.8\,\text{m/s}^2$; $R = 6.4 \times 10^{6}\,\text{m}$; use $GM = gR^2$.
**Find:** (a) $U$ on the grass; (b) the rise in $U$ for the $40\,\text{m}$ drone drop; (c) the rise in $U$ to a height $h = 3R$, exactly and by $mgh$.

(a)
$$U = -\frac{GMm}{R} = -mgR = -0.43 \times 9.8 \times 6.4 \times 10^{6} \approx -2.7 \times 10^{7}\,\text{J}$$

(b) Here $h/R \approx 6 \times 10^{-6}$, so $mgh$ is essentially exact: $\Delta U = 0.43 \times 9.8 \times 40 \approx 169\,\text{J}$.

(c) Exactly, from $r = R$ to $r = 4R$:
$$\Delta U = mgR^2\left(\frac{1}{R} - \frac{1}{4R}\right) = \tfrac{3}{4}\,mgR \approx 2.0 \times 10^{7}\,\text{J}$$
By $mgh$: $mg \times 3R = 3mgR \approx 8.1 \times 10^{7}\,\text{J}$, four times too big.

**Sanity check:** the units of $mgR$ are $\text{kg} \times \text{m/s}^2 \times \text{m} = \text{J}$. In (c), the true rise must be less than $mgh$, because $g$ weakens on the way up. It must also be less than $2.7 \times 10^{7}\,\text{J}$, the energy needed to reach infinity. Both hold.

## Where the picture breaks

No drone or kick could lift a ball thousands of kilometres; the huge height in (c) is only there to show where $mgh$ fails. The drop in (b) also ignores air drag, so Priyanka's catch actually carried slightly less than $169\,\text{J}$ of kinetic energy.

The $-GMm/r$ formula assumes a uniform, spherical Earth and a point at or outside its surface. The zero at infinity is a choice: only *changes* in $U$ can be measured. Dev's $mgh$ (zero on the grass) and the textbook's $-GMm/r$ (zero at infinity) are both valid, as long as you don't mix them in one calculation.

## Key takeaway

Gravitational potential energy is $U = -GMm/r$: zero at infinity and negative everywhere else, because energy must be supplied to separate the bodies. Near the surface, the change in $U$ is approximately $mgh$. Far from the surface, $mgh$ overestimates it, because $g$ gets weaker with height.
