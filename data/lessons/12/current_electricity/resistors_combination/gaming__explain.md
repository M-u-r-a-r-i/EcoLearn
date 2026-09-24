---
concept_id: resistors_combination
interest: gaming
format: explain
title: Two case fans, one supply, and the trick that makes them quiet
check:
  question: |-
    Three identical $30\,\Omega$ case fans are connected in parallel across a supply. The equivalent resistance of the combination is:
  options:
    A: |-
      $90\,\Omega$
    B: |-
      $30\,\Omega$
    C: |-
      $10\,\Omega$
    D: |-
      $0.1\,\Omega$
  answer: C
  explanation: |-
    For $n$ identical resistances in parallel, $R_p = R/n = 30/3 = 10\,\Omega$ — always less than any one of them, because the extra branches give the charge more paths.
  misconceptions:
    A: |-
      Adds the resistances, which is the rule for series. In parallel it is the *conductances* that add, so the total resistance goes down, not up.
    B: |-
      Assumes identical resistors in parallel behave like one of them. Each branch draws its own current from the same voltage, so the supply sees three times the current — a third of the resistance.
    D: |-
      Works out $1/R_p = 3/30 = 0.1$ and stops there. That number is in $\Omega^{-1}$; it still has to be inverted to give $R_p$.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A night gaming desk with a monitor showing a frame counter, a controller charging over a USB cable with current arrows, and an open PC case holding a fan, a graphics card and an LED strip](scenes/gaming/current_electricity.svg "Inside the case, the fan and the LED strip are wired across the same supply — and one loud fan can be tamed by how it is connected.")

Arjun's new case fans are loud. Not slightly loud — the kind that makes his brother shout from the next room during a late session.

A forum post promises a fix with no software and no new parts: wire the two fans **in series** with each other instead of giving each its own connector. Arjun likes it immediately. Nisha, who sits next to him in physics, does not. "You'll halve the voltage across each one," she says. "They might not even start."

They try it. The fans do start, slowly, and the room goes quiet. Then Arjun, pleased with himself, wonders aloud whether wiring them **in parallel** would do the opposite and make them spin faster than normal — and Nisha says that is not how it works either.

One five-volt supply, two identical fans, two ways to wire them. Both work, and they do completely different things. Which is which, and by how much?

## The physics

**In series**, components are joined end to end so there is only one path. The same current passes through every one of them, and the potential differences across them add up to the supply's:

$$R_s = R_1 + R_2 + R_3 + \dots$$

![Two resistors in series on a single loop, with the same current arrow through both](figures/ohms_law/series-circuit-same-current.svg "One path means one current: whatever flows through the first component flows through the second.")

The equivalent resistance is always **larger** than the largest single resistance, so the supply delivers less current — which is exactly why Arjun's fans went quiet.

**In parallel**, components are connected across the same two points. Each has the *full* supply voltage across it, and their currents add:

$$\frac{1}{R_p} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3} + \dots$$

![Resistors drawn in series and in parallel, with the current path and the voltage across each shown](figures/resistors_combination/series-and-parallel.svg "Series shares the current and splits the voltage; parallel shares the voltage and splits the current.")

The equivalent resistance is always **smaller** than the smallest single resistance. For $n$ identical resistances, $R_s = nR$ and $R_p = R/n$.

For a **combination**, reduce the innermost group first and redraw. Two $20\,\Omega$ fans in parallel become one $10\,\Omega$ block; put a $10\,\Omega$ speed-control resistor in series with that block and the supply sees $10 + 10 = 20\,\Omega$, drawing $5/20 = 0.25\,\text{A}$ — and now only half the supply voltage reaches the fans.

## Worked example

**Given:** two identical case fans, each behaving as a $20\,\Omega$ resistor, connected to the $5\,\text{V}$ USB supply — first in series with each other, then in parallel.
**Find:** the current drawn from the supply in each case.

**Series.** The resistances add:

$$R_s = 20 + 20 = 40\,\Omega \qquad I = \frac{5}{40} = 0.125\,\text{A}$$

The two fans share the $5\,\text{V}$ equally, so each has $2.5\,\text{V}$ across it — Nisha's halved voltage, and the reason they turn slowly and quietly.

**Parallel.** For two identical resistances, $R_p = 20/2 = 10\,\Omega$:

$$I = \frac{5}{10} = 0.5\,\text{A}$$

Four times the series current, and each fan now gets the full $5\,\text{V}$ and its own $0.25\,\text{A}$.

**Sanity check:** in parallel each fan draws $5/20 = 0.25\,\text{A}$, and $0.25 + 0.25 = 0.5\,\text{A}$ — matching the total. Parallel is simply the fans running normally; series is the quiet mod. Arjun's hope of "faster than normal" was never available, because no wiring can put more than the supply's $5\,\text{V}$ across a fan.

## Where the picture breaks

Calling a fan "a $20\,\Omega$ resistor" is the weak link. A fan is a motor: as it spins it generates a back-emf, so the current it draws depends on how fast it is already turning, and its effective resistance at $2.5\,\text{V}$ is not the value it had at $5\,\text{V}$. The numbers above are the right shape and the right story, but a real pair of fans in series will not sit at exactly half speed.

Two practical limits as well. Many fans refuse to start at all below some voltage — they hum and stall, which is worse for them than running — so the series trick is not free. And the supply is treated here as a perfect $5\,\text{V}$ source; draw enough current and its own internal resistance pulls that voltage down, which is the next lesson.

## Key takeaway

Series means one path: the current is common, resistances add, and $R_s$ exceeds every individual resistance. Parallel means several paths: the voltage is common, reciprocals add, and $R_p$ is smaller than the smallest branch. Reduce any network by collapsing the innermost series or parallel group first, then redrawing.
