---
concept_id: electrical_power
interest: smartphones
format: explain
title: Why fast chargers raise the voltage instead of the current
check:
  question: |-
    During fast charging, a phone takes $9.0\,\text{V}$ at $2.0\,\text{A}$ from its charger for $30$ minutes. How much electrical energy does it take in?
  options:
    A: |-
      $540\,\text{J}$
    B: |-
      $32.4\,\text{kJ}$
    C: |-
      $3.6\,\text{kJ}$
    D: |-
      $8.1\,\text{kJ}$
  answer: B
  explanation: |-
    The power is $P = VI = 9.0 \times 2.0 = 18\,\text{W}$, and energy is power times time in seconds: $E = 18 \times 1800 = 32\,400\,\text{J} = 32.4\,\text{kJ}$.
  misconceptions:
    A: |-
      Multiplies the power by the time in minutes. A watt is a joule per *second*, so $30$ minutes must be entered as $1800\,\text{s}$.
    C: |-
      Multiplies the current by the time, $It$. That gives the *charge* delivered, $3600\,\text{C}$, not the energy; each coulomb carries $9\,\text{J}$, so the voltage is still missing.
    D: |-
      Divides the voltage by the current, $V/I = 4.5$, and treats that as the power. $V/I$ is a resistance in ohms; power is the product $VI$.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A charging corner: a phone on a wall charger, a power bank charging an earbuds case through a small USB meter, and a smartwatch on its charging puck, with current arrows on the cables](scenes/smartphones/current_electricity.svg "The meter on the cable shows volts and amps; multiply them and you have the rate at which energy is flowing.")

Diya's new fast charger came with a tiny USB meter from a friend who likes gadgets. She plugs it in between charger and phone and watches.

The old charger showed $5\,\text{V}$ on the meter. The new one starts at $5\,\text{V}$ too — then, a second later, the phone and charger seem to agree on something, and the display jumps to $9\,\text{V}$. The current barely changes.

Her friend Aditya is sceptical. "If you want faster charging, just push more amps. Why fiddle with the voltage?"

Diya notices one more thing: the cable from the old charger used to get warm when she used the phone while charging. The new one, on the same phone, stays cool — even though far more energy is going through it.

More energy through the same kind of cable, and less heat in it. Why would raising the voltage do that?

## The physics

A potential difference $V$ gives each coulomb of charge $V$ joules of energy. A current $I$ moves $I$ coulombs every second. So the energy transferred per second — the **power** — is

$$P = VI$$

in watts ($1\,\text{W} = 1\,\text{J/s}$). For a resistance $R$, where $V = IR$, this can be written two more ways:

$$P = I^2 R = \frac{V^2}{R}$$

![Three equivalent forms of electrical power, P = VI, P = I squared R and P = V squared over R](figures/electrical_power/power-three-forms.svg "All three are the same physics; choose the form whose quantities you know and that stay fixed in the comparison you are making.")

The **energy** transferred in time $t$ is

$$E = Pt = VIt$$

in joules. Electricity bills use the kilowatt-hour: $1\,\text{kWh} = 1000\,\text{W} \times 3600\,\text{s} = 3.6 \times 10^6\,\text{J}$.

Now the charger. The phone needs a certain *power*. The cable, though, is just a small resistance $R$ carrying the current, and the power it wastes as heat is $I^2 R$. For a fixed delivered power $P = VI$, raising $V$ lowers $I$ in proportion — and the waste in the cable falls with the *square* of $I$. That is why fast-charging standards negotiate a higher voltage, such as $9\,\text{V}$, rather than simply pushing more current through the same thin copper.

## Worked example

**Given:** a phone is to take $P = 20\,\text{W}$ through a cable whose conductors have a total resistance $R = 0.2\,\Omega$. Compare delivering it at $5\,\text{V}$ and at a higher, illustrative $10\,\text{V}$.
**Find:** the current and the power wasted in the cable in each case.

At $5\,\text{V}$ the current must be $I = P/V = 20/5 = 4\,\text{A}$. The cable then wastes

$$I^2 R = 4^2 \times 0.2 = 3.2\,\text{W}$$

At $10\,\text{V}$, the current needed is only $20/10 = 2\,\text{A}$, and the cable wastes

$$I^2 R = 2^2 \times 0.2 = 0.8\,\text{W}$$

Doubling the voltage halved the current and cut the heating in the cable to a quarter. Over a half-hour charge ($1800\,\text{s}$), the $5\,\text{V}$ cable turns $3.2 \times 1800 \approx 5800\,\text{J}$ into heat, against about $1400\,\text{J}$ at $10\,\text{V}$ — the difference between a warm cable and a cool one.

**Sanity check:** $3.2\,\text{W}$ spread along a metre of cable is like a small night-light's worth of heat — enough to feel, not enough to be dangerous.

## Where the picture breaks

The numbers are illustrative, and the real system is cleverer. The phone cannot use $9$ or $10\,\text{V}$ directly — its battery charges at around $4\,\text{V}$ — so a converter inside the phone steps the voltage down and the current up. That conversion is efficient but not perfect, and some heat appears inside the phone instead of the cable.

Also, $P = I^2 R$ and $P = V^2/R$ apply to a resistance. $P = VI$ is the general one: it gives the power delivered to *any* device, including a battery being charged, which is not a simple resistor at all.

Finally, the charging power is not constant: it drops as the battery fills, so the half-hour energy is a rough figure.

## Key takeaway

Electrical power is the rate of energy transfer, $P = VI$, which for a resistance is also $I^2R$ and $V^2/R$; energy is $E = Pt$. Heat wasted in a wire grows as $I^2$, so delivering the same power at a higher voltage and lower current wastes far less — the reason fast chargers raise the voltage.
