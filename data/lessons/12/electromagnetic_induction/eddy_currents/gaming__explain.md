---
concept_id: eddy_currents
interest: gaming
format: explain
title: The token that crawls past the magnet in the coin chute
check:
  question: |-
    A brass token and a plastic disc of the same size and weight are dropped down the arcade's coin chute, past the same magnet. The brass one crawls through; the plastic one falls straight down. Why?
  options:
    A: |-
      Brass is attracted to the magnet, and that attraction holds it back.
    B: |-
      The magnet magnetises the brass, and the two then cling to each other.
    C: |-
      Brass conducts, so the changing flux drives eddy currents in it, and by Lenz's law they oppose its motion.
    D: |-
      The magnet's field passes straight through the plastic and pushes it down faster.
  answer: C
  explanation: |-
    A changing flux drives closed loops of current inside any conductor. Those eddy currents oppose the change that made them, so the brass is dragged; plastic carries no current, so nothing happens to it.
  misconceptions:
    A: |-
      Confuses "metal" with "magnetic". Brass is not attracted by a magnet at all — hold one against a brass fitting and nothing happens. What matters here is that brass *conducts*.
    B: |-
      The same confusion in another form. Brass cannot be magnetised; the interaction exists only while the flux through it is changing, and it stops the moment the token stops.
    D: |-
      Reads the plastic's behaviour as the magnet acting on it. A magnet does nothing to an insulator — the plastic is simply falling normally, and it is the brass that is the odd one out.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A gaming corner at night: a pinball game on the monitor, a headset charging on a pad, a controller cut away at its rumble motor, a tablet pen hovering over a tablet, and an arcade coin chute with a magnet](scenes/gaming/electromagnetic_induction.svg "Five gaming machines. This lesson is about currents that swirl inside solid metal — including in the coin chute on the right.")

Rehan's friend has brought a plastic disc to the arcade, cut to exactly the size of the arcade's brass tokens and weighted to match. He is very pleased with himself. The machine takes one look and spits it back out.

The owner has seen this trick before. Instead of throwing them out he opens the coin door and shows them the chute — a sloping channel with a small magnet clamped beside it.

He drops a real brass token in. It visibly *crawls* past the magnet, as if it had hit something soft, then carries on. He drops the plastic disc in. It rattles straight through, no hesitation at all. The machine, he says, is simply timing them.

Here is what Rehan cannot make sense of. Brass is not magnetic. Hold a magnet against a brass tap and nothing happens — he checks, and nothing happens. So what exactly slowed that token down?

## The physics

Faraday's law does not care whether the conductor is a tidy loop of wire. **A changing flux drives a current round any closed conducting path** — and inside a solid piece of metal, those paths are closed loops swirling in the metal itself. They are called **eddy currents**.

As the brass token falls past the magnet, the flux through it rises and then falls, so eddy currents flow inside it. Lenz's law still applies: they flow so as to oppose the change that made them, which means opposing the token's motion. And because the metal has resistance, they dissipate energy as heat at a rate $P = I^2R$.

Two conditions decide whether anything happens at all. The material must **conduct** — brass, copper and aluminium all work, even though none of them is attracted to a magnet, while plastic does nothing. And the flux through it must be **changing**: a token held still beside the magnet feels no force whatsoever.

That gives eddy currents two faces.

**Where they are wanted**

- **Magnetic braking.** A metal disc moving through a field is slowed smoothly, with no contact and nothing to wear out. The resistance knob on a gym bike — the kind that drives a cycling game on screen — usually just moves magnets closer to the aluminium flywheel.
- **Induction heating**, where the metal being heated is its own heating element.
- **Coin and token validators**, like this one, and **metal detectors** at a venue gate, which sense the field produced by eddy currents in whatever passes through.

**Where they are a nuisance**

In transformers and motors — including the one that makes a controller rumble — the iron core sits in a changing flux, so eddy currents flow in the core and waste energy as heat. The cure is to break up their paths: build the core from thin **laminations**, each insulated from the next, so the current is left with narrow, high-resistance routes.

![A solid metal plate swinging between magnets with large eddy-current loops, and the same plate cut into slots with only small loops](figures/eddy_currents/solid-vs-slotted-plate.svg "The solid plate is braked hard by big eddy loops; slots leave only narrow high-resistance paths, so the slotted plate swings on.")

## Worked example

**Given:** a gym bike with a magnetic brake is driving a cycling game. You pedal at a steady $60\,\text{W}$ for one minute, and the flywheel's speed does not change. Nothing touches the flywheel.
**Find:** the energy dumped as heat in the aluminium.

Steady speed is the key phrase: the flywheel's kinetic energy is the same at the end as at the start, so none of your work went into speeding it up. Ignoring friction and air drag, all of it went into the eddy currents:

$$E = Pt = 60\,\text{W} \times 60\,\text{s} = 3600\,\text{J}$$

**Sanity check:** $3600\,\text{J}$ is roughly what it takes to warm a small cup of water by under ten degrees — a noticeable amount of heat for one minute's pedalling, and far too little to make the flywheel glow.

## Where the picture breaks

"Little whirlpools of current" is a useful image, not a precise one. The real pattern depends on the shape of the conductor, how fast the flux changes and how deeply the field reaches into the metal.

A real token validator also does more than this one test. It checks size, and it checks how the token responds to a magnet as well — a steel slug behaves quite differently from brass, because steel *is* attracted. The chute Rehan was shown isolates one effect out of several.

Eddy braking can also never hold anything still. It opposes *motion*, and at zero speed there is no changing flux and therefore no force — which is why this kind of brake always eases the token through rather than gripping it.

And the gaming is the setting, not an analogy. An arcade coin door is simply a convenient place to meet a magnetic brake.

## Key takeaway

A changing magnetic flux drives swirling currents inside solid conductors — eddy currents — which by Lenz's law oppose the change and turn energy into heat. They power magnetic brakes, induction heating and coin validators, and they are the reason transformer and motor cores are built from thin insulated laminations.
