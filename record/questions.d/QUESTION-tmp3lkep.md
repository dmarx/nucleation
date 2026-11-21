---
status: Open
title: 'Why do some systems reach scale invariance without any parameter being tuned, while others show it only at a tuned critical point?'
version: 1
tags:
- complex-systems
- natural-sciences
- thermodynamics
date: '2026-11-21'
line:
- formal-apparatus
summary: >-
  A's open question, asked three times in the exchange "Rich Get Richer
  Power Laws": A6's close ("why do some systems naturally approach
  scale-invariant states, while others require extremely precise
  tuning?"), A8's ("can systems naturally evolve to spend most of their
  time near that point?", the motive of self-organized criticality), and
  A23 §10's ("Is there a general theory explaining which scale-free
  structures can persist in systems that are constantly exchanging energy,
  matter, or information with their environments?"). A24 §4 and A27 give
  partial answers: feedback onto an absorbing-state threshold, broken
  continuous symmetry, a line of fixed points, sustained flux. The wording
  is A's (the other assistant in the exchange "Rich Get Richer Power
  Laws", A6, A8, A23); adopting it is the owner's call.
---
<!-- inactive-ok-file: TERM-tmpt3vht CLAIM-tmpsr8r4 — filed with this question on 2026-11-21 -->
<!-- inactive-ok-file: LIT-tmpl2b2l LIT-tmpd6yec LIT-tmp6l8le — registered 2026-11-21, Deferred, unread -->
<!-- inactive-ok-file: THEORY-1095 — Proposed; Toner–Tu long-range order in two dimensions -->

# QUESTION-tmp3lkep: Why do some systems reach scale invariance without any parameter being tuned, while others show it only at a tuned critical point?

## Why it is a question

In the language of [TERM-tmpt3vht](../terms.d/TERM-tmpt3vht.md), a fixed point with relevant directions
is reached only by tuning them: the Ising critical point needs the
temperature and the field set. Yet the exchange collects scale-invariant
laws that need no tuning: the transverse correlations of an ordered
magnet, r^(−(d−2)) throughout the phase (A27 §3); the 2D XY phase with a
temperature-dependent exponent η(T) (A12 §7, A27 §5; Kosterlitz and
Thouless, [LIT-tmp6l8le](../literature.d/LIT-tmp6l8le.md)); the growing interface of the KPZ equation
(A24 §3, [LIT-tmpd6yec](../literature.d/LIT-tmpd6yec.md)); the turbulent inertial range (A23 §2); the ordered
flock (A26 §4, A27 §7; [THEORY-1085](../theory.d/THEORY-1085.md), [THEORY-1095](../theory.d/THEORY-1095.md)); and the sandpile of
self-organized criticality (A3, A24 §4; Bak, Tang and Wiesenfeld,
[LIT-tmpl2b2l](../literature.d/LIT-tmpl2b2l.md)). [CLAIM-tmpsr8r4](../claims.d/CLAIM-tmpsr8r4.md) holds that these are scale-free without a
tuned transition. What it does not hold is why: what a system must have
for its long-distance behaviour to sit at a fixed point with no relevant
direction left to tune.

## A's partial answers

- **Symmetry removes the restoring term** (A27 §2, §6). A broken
  continuous symmetry forbids a θ² term, so long-wavelength distortions
  cost ∝ k² and stay soft everywhere in the ordered phase. An explicit
  field μ²θ² restores a scale ξ ∼ √ρ_s/μ. Here symmetry, not tuning,
  holds the relevant direction at zero.
- **A line of fixed points** (A12 §7). A marginal direction gives a
  family of scale-invariant states, so a whole range of temperature is
  scale-free.
- **Flux through a range of scales** (A23 §2, A24 §5). A constant
  transfer rate between injection and dissipation scales fixes a power law
  across the range between them, with nothing tuned.
- **Feedback onto a threshold** (A24 §4). Slow drive h and activity-driven
  dissipation, dE/dt = h − ερ(E), can hold E near an absorbing-state
  threshold E_c. A's caveat: "Self-regulation explains why a system might
  approach a particular operating point. Critical scaling explains why that
  operating point exhibits fluctuations across many scales. They are
  separate claims, and each requires evidence." It needs separated drive
  and relaxation timescales, and conservation or transport of the right
  kind; ordinary negative feedback gives a finite relaxation time instead.

A gives no criterion to check those conditions in a given system, and
A12 §8's third row, "stable scale-free dynamics", is never defined beyond
these examples.

## What would answer it

A criterion, stated on the RG flow of a class of systems, that says
whether each relevant direction of the governing fixed point is held at
zero by a symmetry, by a conservation law, by feedback with a stated
separation of timescales, or not at all, and so predicts which systems in
the class show scale invariance without tuning. It would be tested
against the cases above and against a counterexample: a system meeting
the criterion's conditions with a finite correlation length, or a
scale-free one that meets none. [LEAD-tmpng7or](../leads.d/LEAD-tmpng7or.md)'s protocol would tell which
case an observed system is in; it would not by itself answer why.

A partial answer for one mechanism (for instance, that an absorbing-state
transition with a conserved field and slow drive self-organizes to its
critical point) narrows the question and is filed as a claim that
`bears_on` it.
