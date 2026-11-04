---
concept_id: spring_potential_energy
interest: smartphones
format: explain
title: Why the robot vacuum bounces off the sofa
check:
  question: |-
    A spring-loaded car phone mount has a spring of force constant $k = 500\,\text{N/m}$. You pull its arms open, stretching the spring by $4.0\,\text{cm}$. How much energy is stored in the spring?
  options:
    A: |-
      $0.80\,\text{J}$
    B: |-
      $10\,\text{J}$
    C: |-
      $0.40\,\text{J}$
    D: |-
      $4000\,\text{J}$
  answer: C
  explanation: |-
    Convert first: $x = 4.0\,\text{cm} = 0.040\,\text{m}$. Then $U = \tfrac{1}{2}kx^2 = \tfrac{1}{2} \times 500 \times 0.040^2 = 250 \times 0.0016 = 0.40\,\text{J}$.
  misconceptions:
    A: |-
      Uses $kx^2$ without the half ($500 \times 0.0016$). The spring force grows from zero to $kx$ as you stretch it, so the average force is only half of $kx$ — hence the $\tfrac{1}{2}$.
    B: |-
      Uses $\tfrac{1}{2}kx$ without squaring ($250 \times 0.040$). That isn't even an energy — its unit is the newton. The stored energy grows with the square of the stretch.
    D: |-
      Puts the stretch in centimetres ($250 \times 4.0^2$). With $k$ in newtons per metre, $x$ must be in metres, or the answer is out by a factor of ten thousand.
author: claude-code/opus-5
written: 2026-09-25
---
## The story

![A living room in the evening: a camera drone climbs straight up, a phone falls from a shelf towards a cushion, an earbuds case is whirled on a lanyard in a vertical circle, and a robot vacuum rolls towards a sofa leg](scenes/smartphones/work_energy_power.svg "The robot vacuum on the right is about to meet the sofa leg with its spring-loaded bumper first.")

Ishaan's family have just got a robot vacuum, and his little sister Diya has spent the morning following it round the flat, filming it on the family phone.

Her favourite part is when it reaches the sofa. It rolls straight into the leg, the front bumper squashes in a little, and the whole machine gives a tiny jolt backwards before it turns away.

"It's scared of the sofa," Diya says.

Ishaan flips the vacuum over. The bumper is a curved strip across the front that slides in when pressed, and behind it he can see small springs pushing it back out.

He wonders: when the vacuum rolls into the leg, where does its energy go for that instant when it is stopped? And how far must that bumper squash in to take it all?

## The physics

An ideal spring obeys **Hooke's law**: stretched or compressed by $x$ from its natural length, it pushes back with a force

$$F = -kx$$

where $k$ is the **force constant** (stiffness) in $\text{N/m}$, and the minus sign says the force always points back towards the natural length.

To compress it you must push with $kx$, a force that grows from zero as you go. The work you do is the area under the force–extension line — a triangle of base $x$ and height $kx$:

$$U = \tfrac{1}{2}kx^2$$

This work is stored as the spring's **elastic potential energy**. The spring force is **conservative**: let the spring go back and it returns the energy, and $U$ depends only on $x$, not on how the spring got there. Stretch or compress, $x^2$ is positive, so $U$ is positive either way.

![Left: the spring force rising in a straight line with compression, with the triangle under it equal to one half k x squared. Right: the stored energy rising as a parabola, four times larger when the compression doubles](figures/spring_potential_energy/spring-force-and-energy.svg "Drawn for one particular spring, but the shapes are general: the force grows in step with x, so the stored energy — the area under the force line — grows with x squared.")

In the story, the vacuum's kinetic energy goes into the bumper springs as it squashes in. At the moment it stops, all of it is stored as $\tfrac{1}{2}kx^2$. Then the springs push back, handing energy back — that is the jolt.

## Worked example

**Given:** the vacuum's mass is $m = 2.0\,\text{kg}$; it hits the leg at $v = 0.20\,\text{m/s}$; the bumper's springs together have $k = 800\,\text{N/m}$ (illustrative). Assume the wheels stop driving on contact and nothing else takes energy.
**Find:** how far the bumper squashes in.

1. *Energy arriving:* $K = \tfrac{1}{2} \times 2.0 \times 0.20^2 = 1.0 \times 0.040 = 0.040\,\text{J}$.
2. *All of it stored in the springs:* $\tfrac{1}{2}kx^2 = 0.040$, so $x^2 = \dfrac{2 \times 0.040}{800} = 0.00010\,\text{m}^2$.
3. *The squash:* $x = \sqrt{0.00010} = 0.010\,\text{m} = 1.0\,\text{cm}$ — about the width of a fingertip.

At full squash the springs push back with $kx = 800 \times 0.010 = 8.0\,\text{N}$, a little less than the weight of a one-litre bottle of water.

**Sanity check:** a centimetre is about how far such bumpers visibly move, and a slow machine giving a gentle jolt fits a few hundredths of a joule.

## Where the picture breaks

The bumper is a real spring, but the robot isn't a perfect energy-trading machine. Real bumpers mostly act as a switch: the moment they are pressed, the robot's software brakes and reverses the wheels, so the motors, not only the springs, decide what happens next. Some energy is also lost as sound and heat in the plastic, so the bounce-back is smaller than the arrival. And the bumper springs are light and stiff enough to count as "ideal" only for small squashes; press any spring too far and Hooke's law stops holding.

## Key takeaway

An ideal spring stretched or compressed by $x$ stores elastic potential energy $U = \tfrac{1}{2}kx^2$ — the area under its $F = kx$ line. Doubling the compression stores four times the energy. In energy problems, set it equal to the kinetic energy it absorbs or releases.
