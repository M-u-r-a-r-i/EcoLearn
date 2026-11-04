---
concept_id: gravitational_potential_energy
interest: motorsport
format: explain
title: What half a kilometre of climbing costs
check:
  question: |-
    A body of mass $m$ is carried from the Earth's surface ($r = R$) up to a height $h = R$. Using $U = -GMm/r$ and $g = GM/R^2$, how much gravitational potential energy does it gain?
  options:
    A: |-
      $mgR$ — the same as $mgh$ gives
    B: |-
      $\tfrac{3}{2}mgR$
    C: |-
      $\tfrac{1}{2}mgR$ — half of what $mgh$ gives
    D: |-
      $\tfrac{1}{4}mgR$
  answer: C
  explanation: |-
    $U(R) = -GMm/R = -mgR$ and $U(2R) = -GMm/2R = -\tfrac{1}{2}mgR$, so the gain is $\tfrac{1}{2}mgR$ — half of what $mgh$ would predict, because $g$ weakens all the way up.
  misconceptions:
    A: |-
      Uses $mgh$ at a height where it no longer applies. $mgh$ assumes $g$ is the same all the way up, but at $r = 2R$ the field is already down to a quarter of its surface value.
    B: |-
      Adds the sizes of the two potential energies, $mgR + \tfrac{1}{2}mgR$, instead of subtracting them. A change in energy is always the final value minus the initial one, signs included.
    D: |-
      Applies the inverse-square law to the energy: since $g$ falls to a quarter at $r = 2R$, assumes the energy does too. Force goes as $1/r^2$, but potential energy goes as $1/r$.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A pit lane at a hill-climb event: a car on a weighbridge, a team truck with a satellite dish on its roof, a GPS aerial on the car's engine cover and a drop-test rig beside the scrutineering bay](scenes/motorsport/gravitation.svg "A hill-climb car finishes half a kilometre higher than it started. Something has to pay for that height.")

Yusuf has converted an old shell into an electric hill-climb car, and the whole project now rests on one question: will the battery last the run?

The course climbs five hundred metres from the paddock to the finish. Yusuf has been budgeting energy for drag and for the corners, and has written nothing at all for the height.

Charu, who plans the team's strategy, points at the blank line. "You've costed the wind and the tyres and forgotten the hill. The hill *is* the event."

"It's a few metres a second of climb rate," Yusuf says. "How expensive can lifting be?"

"That depends," says Charu, "on whether lifting even works the way you think it does five hundred metres up."

Neither of them can put a number on it. How much energy does the height alone cost — and is the formula from Class 9 still the right one?

## The physics

Gravity is a **conservative** force: the work it does depends only on where you start and finish, never on the route. That lets us define a **gravitational potential energy** $U$, with the work done against gravity stored as a rise in $U$.

**Near the surface**, $g$ is effectively constant over the climb, the force is $mg$ everywhere, and lifting through a height $h$ costs

$$\Delta U = mgh$$

The zero of $U$ can sit anywhere — only changes matter.

**Far from the surface** that fails, because the force itself weakens. Integrating $GMm/r^2$ from infinity in, with $U$ chosen to be zero at infinity, gives

$$U(r) = -\frac{GMm}{r}$$

The minus sign is not a mistake. Infinity is the state of *most* energy, so everything closer in has less than zero. The **gravitational potential** is the same thing per kilogram, $V = U/m = -GM/r$, measured in $\text{J/kg}$.

![A graph of potential energy against distance from Earth's centre: the exact curve U = −GMm/r rising towards zero, and a straight mgh line that climbs away from it](figures/gravitational_potential_energy/u-vs-r-and-mgh.svg "The two agree just above the surface and part company higher up. By one Earth radius up, mgh has overcharged by a factor of two.")

**How the two are related.** Raising a mass from $R$ to $R + h$ changes $U$ by

$$\Delta U = GMm\left(\frac{1}{R} - \frac{1}{R+h}\right) = \frac{GMm\,h}{R(R+h)} = \frac{mgh}{1 + h/R}$$

using $GM = gR^2$. For $h \ll R$ the bracket is one and the formula collapses to $mgh$. That is the whole story of $mgh$: it is the exact expression with $h/R$ thrown away.

## Worked example

**Given:** an electric hill-climb car of total mass $m = 1000\,\text{kg}$ (illustrative) climbing $h = 500\,\text{m}$; $g = 9.8\,\text{m/s}^2$, $R = 6.4 \times 10^{6}\,\text{m}$.
**Find:** the energy the height alone demands, and how far wrong $mgh$ is.

**Step 1 — the climb.**

$$\Delta U \approx mgh = 1000 \times 9.8 \times 500 = 4.9 \times 10^{6}\,\text{J}$$

**Step 2 — picture it.** At $108\,\text{km/h}$ (that is $30\,\text{m/s}$) the same car carries $\tfrac{1}{2}mv^2 = 0.45 \times 10^{6}\,\text{J}$ of kinetic energy. The climb costs about **eleven times** that. Charu is right: the hill is the event.

**Step 3 — how wrong is $mgh$?** The correction factor is $1 + h/R$, and

$$\frac{h}{R} = \frac{500}{6.4 \times 10^{6}} = \frac{1}{12\,800}$$

so $mgh$ overcharges by $4.9 \times 10^{6}/12\,800 \approx 400\,\text{J}$ — about what it takes to lift a wheel and tyre onto the roof of the truck.

**Sanity check:** the climb is a ten-thousandth of the Earth's radius, so a correction of a ten-thousandth is exactly the size to expect. Use $mgh$ and sleep soundly.

## Where the picture breaks

Motorsport is the setting here, not the analogy. The hill climb is simply a real place where a big mass gains real height; nothing about racing explains why $U$ is negative.

Three honest limits. First, $\Delta U = mgh$ is about **height**, not distance along the road — ten kilometres of hairpins gaining five hundred metres cost the same as a vertical lift of five hundred metres. Second, the $4.9\,\text{MJ}$ is only the gravity bill; drag, rolling resistance and the heat in the motor are separate lines in Yusuf's budget and are all larger. Third, $U = -GMm/r$ takes the Earth as a uniform sphere and $r$ as the distance from its **centre**, so it does not apply inside the Earth, where the shells above you no longer pull you down.

## Key takeaway

Gravitational potential energy is $U = -GMm/r$ with the zero at infinity, negative because a bound body has less energy than one infinitely far away. Near the surface the change reduces to $\Delta U = mgh$, which is the exact result $mgh/(1 + h/R)$ with $h/R$ dropped — excellent for a hill, hopeless for an orbit.
