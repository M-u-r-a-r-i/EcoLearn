---
concept_id: ohms_law
interest: music
format: explain
title: Why big studio headphones sound quiet on a phone
check:
  question: |-
    A resistor inside a guitar effects pedal has $2.0\,\text{V}$ across it and carries $4.0\,\text{mA}$. The voltage across it is raised to $3.0\,\text{V}$, and it stays ohmic at the same temperature. The current becomes:
  options:
    A: |-
      $4.0\,\text{mA}$ — the resistor fixes the current
    B: |-
      $2.7\,\text{mA}$
    C: |-
      $6.0\,\text{mA}$
    D: |-
      $9.0\,\text{mA}$
  answer: C
  explanation: |-
    $R = V/I = 2.0/(4.0 \times 10^{-3}) = 500\,\Omega$, which stays constant for an ohmic conductor. At $3.0\,\text{V}$, $I = V/R = 3.0/500 = 6.0\,\text{mA}$ — current is proportional to voltage.
  misconceptions:
    A: |-
      Thinks a resistor sets a fixed current. It sets a fixed ratio of voltage to current; more voltage drives more current.
    B: |-
      Inverts the relationship, as if current fell when voltage rose ($I \propto 1/V$).
    D: |-
      Squares the voltage ratio, confusing current with power ($P = V^2/R$).
author: claude-code/opus-5
written: 2026-09-21
---
## The story

![A desk with a phone, big studio headphones plugged into it, an effects pedal and a guitar amplifier](scenes/music/current_electricity.svg "Expensive headphones, cheap phone — and a surprising silence.")

Ishaan saved for eight months to buy a pair of big studio headphones — the kind real producers wear. He gets home, plugs them into his phone, presses play on his favourite track and turns the volume all the way up.

It's… quiet. Thin. Barely louder than a whisper.

Confused, he unplugs them and tries the cheap earbuds that came free with the phone. Same phone, same song, same volume setting — and they're *loud*. Did he waste eight months of pocket money on a faulty pair? He checks the box. The headphones are fine. Printed on the side is a number he's never paid attention to: **300 Ω**. The earbuds say **32 Ω**.

What is that number, and why does it decide how loud the music is?

The headphone socket on a phone gives out only a small, fixed-ish voltage. Studio headphones are often built with a much higher **resistance** — say $300\,\Omega$ — while earbuds are typically nearer $32\,\Omega$. The same voltage drives very different currents through them, and the current in the headphone coil is what moves the air. The rule that connects voltage, current and resistance is Ohm's law.

## The physics

When a potential difference $V$ is applied across a conductor, a current $I$ flows. The **resistance** of the conductor is defined as

$$R = \frac{V}{I}$$

measured in ohms: $1\,\Omega = 1\,\text{V/A}$.

**Ohm's law** states that for a metallic conductor at constant temperature (and other physical conditions unchanged), the current is directly proportional to the potential difference:

$$V = IR, \quad \text{with } R \text{ constant}$$

Conductors that obey this are called **ohmic**. Their V–I graph is a straight line through the origin, whose slope (with $V$ on the vertical axis) is $R$. Many devices are **non-ohmic**: a filament lamp's resistance rises as it heats up, and a diode lets current through easily one way but hardly at all the other — their V–I graphs are curves.

![A V–I graph: a straight blue line through the origin for a 20 ohm resistor, and a red curve bending upwards for a filament lamp](figures/ohms_law/vi-ohmic-vs-lamp.svg "An ohmic resistor gives a straight line through the origin; a filament lamp's line curves as it heats and its resistance rises.")

The law is named after **Georg Simon Ohm**, a German schoolteacher who published it in 1827 after years of careful experiments with wires of different lengths and thicknesses. His work was coldly received at first; it took over a decade before scientists recognised it, and in 1841 the Royal Society in London awarded him its Copley Medal. The unit of resistance, the ohm, honours him.

![A black-and-white portrait of Georg Simon Ohm in a dark coat](famous/georg-simon-ohm-portrait.jpg "Georg Simon Ohm (1789–1854). Public domain, via Wikimedia Commons.")

Microscopically, the voltage sets up an electric field in the conductor that gives the free electrons a small drift velocity; resistance measures how strongly collisions inside the material hold that drift back.

Back to the headphones: for the same voltage $V$, current is inversely proportional to resistance, $I = V/R$. Ten times the resistance means about a tenth of the current.

## Worked example

**Given:** a phone headphone output of about $1.0\,\text{V}$ (illustrative), earbuds of $32\,\Omega$, studio headphones of $300\,\Omega$. Treat each as a simple resistance.
**Find:** the current through each.

$$I_\text{earbuds} = \frac{V}{R} = \frac{1.0}{32} \approx 0.031\,\text{A} = 31\,\text{mA}$$

$$I_\text{studio} = \frac{V}{R} = \frac{1.0}{300} \approx 0.0033\,\text{A} = 3.3\,\text{mA}$$

The studio pair gets roughly a tenth of the current — which is why it sounds so much quieter from a phone, and why studios drive such headphones from a dedicated amplifier that supplies a higher voltage.

**Sanity check:** $300/32 \approx 9.4$, and $31/3.3 \approx 9.4$. ✓

## Where the picture breaks

Headphones run on a constantly changing (AC) signal, and what their spec sheets call "impedance" is the AC version of resistance — it can vary with the pitch of the note. Treating them as a plain resistor with a steady voltage is a simplification that you'll refine in the chapter on alternating current. The phone's output also isn't a perfect fixed voltage: it has some internal resistance of its own, a topic coming up in this chapter. And loudness depends on power and on how efficiently each headphone turns current into sound, not on current alone.

## Key takeaway

Resistance is $R = V/I$. For an ohmic conductor at constant temperature, $R$ stays fixed, so current is proportional to voltage: $V = IR$, a straight-line V–I graph through the origin. For the same voltage, a higher resistance means a smaller current.
