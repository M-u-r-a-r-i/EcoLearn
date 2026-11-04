---
concept_id: electron_emission
interest: smartphones
format: explain
title: What the old television in the store room knew about electrons
check:
  question: |-
    Metal X has a work function of $2.0\,\text{eV}$ and metal Y has a work function of $4.5\,\text{eV}$. Which statement is correct?
  options:
    A: |-
      Y emits electrons more readily, because a larger work function means the metal has more energy to hand to its electrons.
    B: |-
      Freeing even the most loosely held electron from Y takes more than twice the energy it takes for X, whichever method supplies it.
    C: |-
      Both need the same energy per electron; the work function only decides how many electrons come out, not how much energy each needs.
    D: |-
      The work function only matters when light is used; if the two metals are heated instead, no minimum energy applies.
  answer: B
  explanation: |-
    The work function is the minimum energy needed to pull an electron out through the surface, and it is a property of the metal, not of the method. $4.5\,\text{eV}$ is $2.25$ times $2.0\,\text{eV}$, so Y holds on to its electrons more than twice as firmly.
  misconceptions:
    A: |-
      Reads the work function as energy the metal gives away. It is the opposite: energy the electron must be given to escape, so a larger value means a tighter grip and harder emission.
    C: |-
      Mixes up the energy needed per electron with the number of electrons emitted. The work function is an energy per electron, and it differs from metal to metal.
    D: |-
      Thinks the work function belongs to the photoelectric effect alone. Heating, strong fields and light are just different ways of paying the same bill; thermionic emission needs electrons with at least $\varphi$ of energy too.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A phone beside a sunny window, its screen showing a UV-index meter, its flashlight beam drawn half as a wave and half as a stream of packets, and a magnified camera pixel where light frees electrons](scenes/smartphones/dual_nature.svg "Every sensor in the phone begins with the same event: light handing an electron enough energy to break loose.")

Tanvi is clearing the store room at her grandparents' flat in Pune when she finds it: a heavy old television with a deep, bulging back. Her grandfather taps the glass. "Inside this there was a gun. It fired electrons at the screen, and the screen glowed where they hit."

"Fired them from where?" Tanvi asks.

"From a little metal wire, heated till it glowed orange."

That evening she reads a review of a new phone camera. One line stops her: *each pixel turns light into electrons.* So the old television boiled electrons out of a metal with heat, and her phone frees them with light.

But a copper wire is full of electrons, and they never drip out of the charging cable on her desk. What keeps them in — and what does it take to get one out?

## The physics

A metal contains a huge number of **free electrons**, which move about inside it and carry current. They are free *inside* the metal, not free to leave it. Near the surface, the positive ions of the metal pull any escaping electron back.

So an electron needs a minimum amount of energy to escape. That minimum is the **work function**, $\varphi_0$ (often written just $\varphi$). It is the energy needed to take the most loosely held electron from inside the metal to just outside the surface.

![An energy diagram: filled electron levels inside a metal, a dashed vacuum level above, and a green arrow marking the work function gap between them](figures/electron_emission/work-function-barrier.svg "The work function is the gap from the highest filled level up to the outside world — the toll every escaping electron must pay.")

Work functions are a few electron volts. One **electron volt** is the energy an electron gains when it is accelerated through a potential difference of $1\,\text{V}$:

$$1\,\text{eV} = 1.6 \times 10^{-19}\,\text{J}$$

Caesium has one of the lowest work functions, about $2.1\,\text{eV}$; platinum one of the highest, about $5.7\,\text{eV}$. The value depends on the metal and on the state of its surface — a film of oxide or dirt changes it.

There are three main ways to hand an electron its escape energy, and the figure shows them side by side:

1. **Thermionic emission** — heat the metal. At high temperature some electrons are moving fast enough to get out. This was the television's heated wire.
2. **Field emission** — apply a very strong electric field, of the order of $10^8\,\text{V/m}$, which drags electrons out through the surface.
3. **Photoelectric emission** — shine light of high enough frequency on the metal. The light supplies the energy. The electrons that come out are called **photoelectrons**.

![Four panels showing thermionic, photoelectric, field and secondary emission, each freeing electrons from a metal surface](figures/electron_emission/emission-methods.svg "Four different energy sources, one identical bill to pay: the work function.")

Whatever the method, the bill is the same: at least $\varphi_0$ per electron.

## Worked example

**Given:** a metal with work function $\varphi_0 = 2.0\,\text{eV}$ (an illustrative value, close to caesium's). At room temperature a typical electron's thermal energy is about $0.025\,\text{eV}$.
**Find:** the work function in joules, and why the electrons stay put.

First, into SI units:

$$\varphi_0 = 2.0 \times 1.6 \times 10^{-19} = 3.2 \times 10^{-19}\,\text{J}$$

A tiny number — but that is the bill for *one* electron.

Next, compare it with what heat gives an electron at room temperature:

$$\frac{2.0\,\text{eV}}{0.025\,\text{eV}} = 80$$

A typical electron has only about one-eightieth of the energy it needs. Almost none escape, which is why your charging cable never drips electrons.

**Sanity check:** a single $1.5\,\text{V}$ torch cell gives an electron $1.5\,\text{eV}$ — the same size as a work function, which is why a work function counts as small in joules but not in electron volts.

## Where the picture breaks

The phone review was a little loose with its words. A phone's camera sensor is made of silicon, a semiconductor, not a metal. Light does free electrons inside it, but they stay *inside* the silicon and are collected there; none leave the surface into empty space. The energy that matters in silicon is its band gap, about $1.1\,\text{eV}$, not a work function. Physicists call this the internal photoelectric effect, and you will meet semiconductors later. The emission in this lesson — electrons leaving a metal altogether — happens in older devices like the television's electron gun and in photocells.

And "80 times short" describes a *typical* electron. Thermal energies are spread out, so a heated filament frees the rare few in the fast tail. That is why thermionic emission rises so steeply with temperature.

## Key takeaway

Free electrons are free only inside a metal; the pull of the positive ions keeps them in. The **work function** $\varphi_0$ is the minimum energy needed to get one out, a few electron volts, and it depends on the metal and its surface. Heat (thermionic), a strong field (field emission) and light (photoelectric) are three ways to pay that same bill.
