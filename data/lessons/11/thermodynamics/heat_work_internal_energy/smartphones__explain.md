---
concept_id: heat_work_internal_energy
interest: smartphones
format: explain
title: Two warm charging cables and a thermal camera that can't tell them apart
check:
  question: |-
    Two identical charging cables start in the same state. Cable P carries a large charging current, which does $40\,\text{J}$ of electrical work on it, while it loses $10\,\text{J}$ of heat to the air. Cable Q carries no current and is warmed only by sunlight, with no work done on it. Both cables end in the same state. How much heat did cable Q absorb?
  options:
    A: |-
      $50\,\text{J}$
    B: |-
      $10\,\text{J}$
    C: |-
      $40\,\text{J}$
    D: |-
      $30\,\text{J}$
  answer: D
  explanation: |-
    Cable P's internal energy rose by $40 - 10 = 30\,\text{J}$. Cable Q ends in the same state, so its internal energy also rose by $30\,\text{J}$, and with no work done on it, all of that came in as heat: $30\,\text{J}$.
  misconceptions:
    A: |-
      Adds the heat lost to the work done ($40 + 10$). Heat that leaves a body lowers its internal energy, so it must be subtracted, not added.
    B: |-
      Thinks only heat can be compared with heat, so copies cable P's $10\,\text{J}$ of heat. But heat and work both change internal energy, and it is the change in internal energy that the two cables share.
    C: |-
      Ignores the heat cable P lost to the air, as if all $40\,\text{J}$ of work stayed in the cable. The internal energy change is the energy in minus the energy out.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A sunny room: a phone sealed in a puffed-up waterproof pouch on a windowsill, a phone charging on a desk seen through a clip-on thermal camera, an icy can of compressed air, and a wall air conditioner controlled from a phone app](scenes/smartphones/thermodynamics.svg "In the middle: a charging cable glowing warm on a thermal camera's screen.")

Ishita has just bought a clip-on thermal camera for her phone, and she is pointing it at everything in her hostel room. The kettle glows yellow. Her roommate's feet glow orange. And on her desk, two identical charging cables both glow the same warm orange.

One of them has been charging her laptop at full speed all afternoon, in the shade. The other isn't plugged into anything; it has just been lying in a patch of sunlight from the window.

Her roommate Dev looks over her shoulder. "The one carrying current is full of electrical energy. The sunny one is full of heat. I bet your camera can tell them apart if you look closely."

Ishita zooms in, changes the colour scale, and tries again. The two cables look exactly the same.

Is the camera just not good enough? Or is there really nothing to tell apart?

## The physics

Every body is made of molecules that jiggle, vibrate and pull on each other. The total of their kinetic and potential energies, measured in the frame where the body as a whole is at rest, is its **internal energy** $U$. A cable being swung around also has kinetic energy as a whole, but that is not part of $U$; the random jiggling of its atoms is.

Energy can be added to a body in two different ways:

- **Heat** $Q$: energy transferred because of a temperature difference. Sunlight falling on the sunny cable delivers energy this way.
- **Work** $W$: energy transferred by any other means, such as a force acting through a distance, or an electric current pushed through the body by a voltage. The charger's voltage drives current through the cable's copper, and that **electrical work** ends up as random jiggling of its atoms.

Energy is conserved, so the change in internal energy equals the heat that came in plus the work done on the body. (You will soon meet this as the first law, with a sign convention.)

![Two routes from State 1 to State 2: left in the sun with 60 J of heat in and no work; rubbed hard with 80 J of work done and 20 J of heat lost; both give a change in internal energy of 60 J](figures/heat_work_internal_energy/two-routes-same-state.svg "Different amounts of heat and work, the same change in internal energy. Only U belongs to the state.")

Here is the key distinction:

- $U$ is a **state variable**. It depends only on the body's present condition (its temperature, pressure, volume and so on), not on its history. Same state means same $U$.
- $Q$ and $W$ are **not** state variables. They describe a *process*: energy crossing the boundary. Once across, both simply become internal energy, and the body keeps no record of the route. Saying a cable "contains heat" or "contains electrical work" is meaningless, the way a bank balance does not remember whether the money came in as cash or by transfer.

That answers Dev. The two cables are in the same state, so they have the same internal energy, and no camera, however good, can reveal which route each one took. The thermal camera sees temperature, which belongs to the state, and that is all there is to see.

## Worked example

**Given (illustrative):** both cables start at room temperature and end at the same warmer state.
Cable A (sunny): absorbs $30\,\text{J}$ of heat from sunlight; no work is done on it.
Cable B (charging): the current does $50\,\text{J}$ of electrical work on it, and it loses $20\,\text{J}$ of heat to the air.
**Find:** the change in internal energy of each.

**Step 1: cable A.** Only heat came in:

$$\Delta U_A = 30 + 0 = 30\,\text{J}$$

**Step 2: cable B.** Work came in, and some heat went out:

$$\Delta U_B = 50 - 20 = 30\,\text{J}$$

**Step 3: compare.** Both rose by $30\,\text{J}$. The heat was $+30\,\text{J}$ for A and $-20\,\text{J}$ for B; the work was $0$ for A and $50\,\text{J}$ for B. Heat and work were completely different, yet the change in $U$ was the same, because the start and end states were the same.

**Sanity check:** $30\,\text{J}$ is about what it takes to lift a laptop from the floor to the top of a tall cupboard, a small amount spread through a whole cable, so a gentle warmth is the right size.

## Where the picture breaks

Real cables are not perfectly identical, and "the same state" means the same temperature *everywhere* along them, which two real cables in different light never quite manage; the sunny side of a cable can be warmer than its shady side. A thermal camera also reads surface temperature from infrared light, and shiny and matte surfaces can fool it by a few degrees. The numbers here are illustrative, not measurements of any real cable or charger. None of this changes the principle: if two bodies really are in the same state, nothing about them records whether they got there by heat or by work.

## Key takeaway

Heat is energy transferred because of a temperature difference; work is energy transferred by any other means, including an electric current. Internal energy $U$ is a state variable: it depends only on the present state. Heat and work depend on the path, so a body never "contains" either, only internal energy.
