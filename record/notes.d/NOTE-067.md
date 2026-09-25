---
number: 67
status: Skimmed
formerly:
- NOTE-tmpn3pug
paper: LIT-034
title: 'The sound of an axon''s growth'
version: 1
date: '2026-09-25'
summary: >-
  The authors propose that an axon can regulate its length by reading the spectral composition, rather than the frequency, of motor-generated oscillating signals whose period grows with length. Coupling that signal to growth-cone extension and actin contraction produces a stable length. In some parameter regions fewer motors make axons longer, as experiments show.
---

<!-- inactive-ok-file: LIT-034 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-25 -->

# NOTE-067: The sound of an axon's growth

## Contribution

Axons range from tens of micrometres to metres in length, and besides external cues their length is set by unknown internal mechanisms. Earlier work proposed that kinesin and dynein motors moving in opposite directions generate oscillations whose frequency depends on axon length and could serve as a length gauge. The authors present a mechanism in which the axon's length is determined through the spectral decomposition of that oscillatory signal, coupled to the axon's mechanics.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- Setup (Fig. 1): a signal I is carried to the growth cone by kinesin and triggers dynein transport of a signal O back to the soma, where O suppresses I. With delayed feedback, the period grows with length L. I promotes actin polymerization (extension), and a response R drives contraction.
- Key observation (eqs 1–3, Fig. 2): for a Hill-type response to a periodic input, the time-averaged response does not depend on the period, only on the fraction of the period spent above threshold. So frequency alone cannot be read out by averaging, but the response's spectrum can.
- Oscillations (Fig. 3): below a critical length the oscillations vanish (minimum length L_min, eq. 7), and the frequency falls with L.
- Growth dynamics (Fig. 4, eq. 10): the equations have a state-dependent delay. The length settles to a steady value (about 125 µm for the chosen parameters, with sub-µm oscillation) through a laser-like balance of gain and loss with phase-locking. The mean length rises as motor influx J₀ falls in some regimes, consistent with experiments (refs 20, 22).
- Closing: such small length oscillations would probably be masked by noise in real axons. A spatially resolved description of contractility is needed.

## Open questions

- A neat example of biological size control by frequency-to-amplitude transduction. It is a physics-of-living-systems paper, not ML.
- A deeper reading should check how finely tuned the parameters are, and what experimental test would tell this mechanism apart from gradient-based length sensing.
