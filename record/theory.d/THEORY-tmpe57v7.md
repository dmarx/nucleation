---
status: Active
title: "The Belousov–Zhabotinsky oscillation is a relaxation cycle in which autocatalytic production of HBrO₂ oxidizes the catalyst until bromide, released as the oxidized catalyst is reduced by bromomalonic acid, switches the autocatalysis off; a closed batch oscillates only as a transient of up to several thousand cycles on its way to equilibrium, and only a continuous-flow reactor sustains it indefinitely"
version: 1
tags:
- natural-sciences
- complex-systems
date: '2026-10-16'
source:
- LIT-531
summary: >-
  Zhabotinsky (2007), [LIT-531](../literature.d/LIT-531.md), the Scholarpedia review by one of the
  reaction's eponyms, read in full in [NOTE-414](../notes.d/NOTE-414.md). The mechanism is supported by
  the primary kinetics and by phase-resetting with injected Br⁻, Ag⁺ and
  Ce⁴⁺. The closed/open distinction matters for any use of BZ as a
  dissipative structure: a closed batch is a long transient, and only a fed
  reactor holds it away from equilibrium. The Oregonator models oscillation
  and excitability qualitatively, not quantitatively. The "several thousand
  cycles" figure is uncited, and the primary papers were not read.
---

<!-- inactive-ok-file: LIT-524 — Unavailable: Nicolis & Prigogine 1977; cited only as the review's source for the far-from-equilibrium condition on oscillation -->

# THEORY-tmpe57v7: The Belousov–Zhabotinsky oscillation is a relaxation cycle in which autocatalytic production of HBrO₂ oxidizes the catalyst until bromide, released as the oxidized catalyst is reduced by bromomalonic acid, switches the autocatalysis off; a closed batch oscillates only as a transient of up to several thousand cycles on its way to equilibrium, and only a continuous-flow reactor sustains it indefinitely

## Source

Zhabotinsky (2007), "Belousov-Zhabotinsky reaction", [LIT-531](../literature.d/LIT-531.md) (*Scholarpedia*
2(9): 1435, revision of 21 October 2011), read in full in [NOTE-414](../notes.d/NOTE-414.md). The page
has later contributors, so not every sentence is certainly Zhabotinsky's.
The figures were read through their captions. The primary papers it cites
were not read.

## What was actually shown

**The core loop.** Zhabotinsky (1964) replaced Belousov's citric acid with
malonic acid and showed that the colour oscillation is the oscillation of
[Ce⁴⁺], that oxidation of Ce³⁺ by bromate is autocatalytic, that oscillation
starts once bromomalonic acid has accumulated, and that Br⁻ inhibits the
autocatalysis. The core scheme (Vavilin and Zaikin 1971) has HBrO₂
autocatalytically oxidizing the catalyst, HBrO₂ removed by Br⁻, and Br⁻
produced as the oxidized catalyst oxidizes bromomalonic acid.

**The test (Fig. 1).** Phase resetting: Br⁻ or Ce⁴⁺ injected while [Ce⁴⁺]
rises switches the system to the falling phase, and Ag⁺, which removes Br⁻,
switches it from falling to rising. That is what a fast positive feedback
switched off by a slower negative one predicts. [NOTE-414](../notes.d/NOTE-414.md) rates the
mechanism strong.

**Closed against open.** In a closed, stirred batch, oscillation occurs over
wide ranges of initial concentrations and "can generate up to several
thousand oscillatory cycles", then stops. In a continuous-flow stirred tank
reactor, "stationary oscillations can continue indefinitely", and bursting
and chaos appear.

**Unstirred media.** Thin layers carry trigger waves from point pacemakers,
forming target patterns (Zaikin and Zhabotinsky 1970). Colliding waves
annihilate, the fastest pacemaker entrains the rest, and broken fronts curl
into spirals, and in thick layers into scroll waves.

**The model.** The Oregonator "properly models oscillations and
excitability" but "is not a quantitative model": it leaves total catalyst
out, reproduces the waveform poorly and misses the oscillatory domains.
Taking the reversibility of the catalyst reactions into account corrects
these.

**What could have come out otherwise.** Injected bromide could have failed
to reset the phase, or reset it the wrong way. It did not.

## What this does not say

- **That a closed batch is a dissipative structure in Prigogine's
  steady-state sense.** It runs down. How long it stays near a quasi-steady
  state is an open question in [NOTE-414](../notes.d/NOTE-414.md).
- **A thermodynamic account.** The far-from-equilibrium condition is cited
  to Nicolis and Prigogine ([LIT-524](../literature.d/LIT-524.md)), unread. The review gives no entropy
  production, free-energy budget or stability analysis.
- **That the Oregonator is quantitatively right.** It is not, by the
  review's own account.
- **That BZ is alive, or organized like an organism.** It has rhythm,
  excitability, self-propagating signals and entrainment, but its
  organization is kept up by the experimenter's feed.
- **A precise cycle count.** "Several thousand" is uncited. Cross and
  Hohenberg ([LIT-527](../literature.d/LIT-527.md)) give under 100 periods for unstirred pattern
  experiments; the setups differ, and the figures do not conflict.

## Connections

- [THEORY-072](THEORY-072.md) holds that organisms differ from dissipative structures such
  as a candle flame by organisational differentiation, and names a BZ
  medium as one such structure. This account is why the comparison is with
  a fed reactor and not a batch. BZ in a flow reactor is the cleanest
  chemical case that thermodynamic and dynamical criteria alone do not
  separate from organisms ([NOTE-414](../notes.d/NOTE-414.md)).
- [THEORY-088](THEORY-088.md) compares spiral defects in slow cortical activity with BZ
  spirals and cites this review.
- Prigogine's lecture ([LIT-516](../literature.d/LIT-516.md)) has the Brusselator, with its inputs "held
  constant". BZ in a flow reactor is its experimental counterpart. Turing
  ([LIT-535](../literature.d/LIT-535.md)) did not cover excitable, strongly non-linear waves of this kind,
  and BZ in microemulsion has since given stationary Turing structures.
