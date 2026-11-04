---
concept_id: acceleration_due_to_gravity
interest: gaming
format: explain
title: Should the mine level use a different gravity setting
check:
  question: |-
    A game has a level set at a depth of $1600\,\text{km}$ below the surface, one quarter of the planet's radius. Treating the planet as a uniform sphere with $g = 9.8\,\text{m/s}^2$ at the surface and $R = 6400\,\text{km}$, what value of $g$ should that level use?
  options:
    A: |-
      $9.8\,\text{m/s}^2$
    B: |-
      $7.4\,\text{m/s}^2$
    C: |-
      $4.9\,\text{m/s}^2$
    D: |-
      $0\,\text{m/s}^2$
  answer: B
  explanation: |-
    Below the surface, $g_d = g(1 - d/R) = 9.8 \times (1 - 0.25) = 7.35 \approx 7.4\,\text{m/s}^2$.
  misconceptions:
    A: |-
      Treats $g$ as a fixed constant everywhere; it has its largest value at the surface and falls off both above and below it.
    C: |-
      Uses the height formula $g(1 - 2d/R)$ for a depth; $g$ falls twice as fast with height as it does with depth, so this halves the answer instead of reducing it by a quarter.
    D: |-
      Thinks the rock overhead cancels gravity completely; only the shell *above* you gives no net pull, while the sphere below you still pulls.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A gaming desk at night: a monitor runs an orbit simulator with a planet and a ship, and a tablet shows a satellite above a planet](scenes/gaming/gravitation.svg "Every level in the game needs a number for g. Is it the same number everywhere?")

Devansh is the newest level designer on a small student team, and he has been handed three maps for the same planet: a coastal city at sea level, a space-jump level where the player falls from $64\,\text{km}$ up, and a mining level $3200\,\text{km}$ down, halfway to the core.

The engine has one field for gravity, and right now every level says $9.8$.

"Change it for the other two," says Ishita, the lead. "Up high you're further from the centre, so it should be weaker. Down the mine you've got the whole planet around you, so it should be stronger. Obviously."

Devansh isn't sure about the mine. If rock is pulling you from *above* as well as below, does that make gravity stronger, or does some of it cancel?

He needs real numbers for both levels, and he needs to know where $9.8$ came from in the first place.

## The physics

**Where $g$ comes from.** A body of mass $m$ at the surface feels the planet's pull $GMm/R^2$, where $M$ and $R$ are the planet's mass and radius. That pull is its weight, $mg$:

$$mg = \frac{GMm}{R^2} \quad\Rightarrow\quad g = \frac{GM}{R^2}$$

The body's own mass cancels, which is why everything falls with the same $g$ when you ignore air. For Earth, $M = 6.0 \times 10^{24}\,\text{kg}$ and $R = 6.4 \times 10^{6}\,\text{m}$ give $g \approx 9.8\,\text{m/s}^2$.

**Above the surface.** At height $h$ the distance from the centre is $R + h$:

$$g_h = \frac{GM}{(R + h)^2} = g\left(\frac{R}{R + h}\right)^2 \approx g\left(1 - \frac{2h}{R}\right) \quad (h \ll R)$$

**Below the surface.** Model the planet as a sphere of uniform density. At depth $d$, the shell of rock *above* you pulls you outwards in every direction at once, and those pulls cancel exactly — that is the part Ishita got wrong. Only the inner sphere of radius $R - d$ pulls you, and it has less mass in proportion to its volume, so

$$g_d = g\left(1 - \frac{d}{R}\right)$$

So $g$ is **largest at the surface**. Going up, it falls off as $1/r^2$. Going down, it falls off linearly, reaching zero at the centre — where you would float, pulled equally in all directions.

![A graph of g against distance from the centre: a straight line rising from zero at the centre to a peak at the surface, then a curve falling as one over r squared](figures/acceleration_due_to_gravity/g-vs-distance.svg "Inside a uniform planet g grows in proportion to r; outside it falls as 1/r². The peak is exactly at the surface.")

## Worked example

**Given:** $g = 9.8\,\text{m/s}^2$ at the surface and $R = 6400\,\text{km}$. The space-jump level is at $h = 64\,\text{km}$; the mine level is at $d = 3200\,\text{km}$.
**Find:** the value of $g$ for each level.

**The space-jump level.** Here $h$ is one hundredth of $R$, so the approximation applies:

$$\frac{2h}{R} = \frac{2 \times 64}{6400} = 0.02$$

The pull is weaker by $2\%$:

$$g_h = 9.8 \times (1 - 0.02) \approx 9.6\,\text{m/s}^2$$

**The mine level.** The depth is half the radius, so half the planet's radius of material is left below you:

$$g_d = 9.8 \times \left(1 - \frac{3200}{6400}\right) = 9.8 \times 0.5 = 4.9\,\text{m/s}^2$$

**Sanity check:** $64\,\text{km}$ up is a two percent change — a player would never feel it, and a falling crate lands almost exactly as it does in the city. Halfway to the centre, gravity is halved, and a jump there really would look like slow motion. Ishita had the mine backwards.

## Where the picture breaks

The uniform-density model is what makes the depth formula so simple, and the real Earth is not uniform: it has a dense iron core and a lighter crust, so $g$ actually rises slightly for the first few hundred kilometres of depth before falling. A game may keep the tidy formula; a geologist would not.

The space-jump number is also not the whole story for gameplay. At $64\,\text{km}$ the air is almost gone, so a falling player meets far less drag and reaches a much higher speed than at sea level — an effect far bigger than the $2\%$ change in $g$. Our formulas ignore air completely. Real planets also spin and bulge at the equator, so measured $g$ varies slightly with latitude.

## Key takeaway

$g = GM/R^2$ — the same for every falling body, set by the planet, not by what is falling. Above the surface $g_h = g(R/(R+h))^2 \approx g(1 - 2h/R)$; below it, for a uniform planet, $g_d = g(1 - d/R)$. Gravity is strongest at the surface, and it is zero at the centre, not infinite.
