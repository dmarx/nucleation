---
number: 508
status: Open
formerly:
- QUESTION-tmp3lkep
title: 'Why do some systems reach scale invariance without any parameter being tuned, while others show it only at a tuned critical point?'
version: 2
history:
- version: 2
  date: '2026-11-22'
  note: >-
    Edited in place on 2026-11-22 after Bak, Tang and Wiesenfeld
    (LIT-2992) was read (NOTE-tmpnl00y, THEORY-tmpehudh): the
    feedback-onto-a-threshold answer is marked as the later framing of
    self-organized criticality, not the 1987 letter's, and the letter's
    own partial answer is added, relaxation stopping at marginal
    stability, by analogy with percolation, in two or more dimensions.
    The question and its status are unchanged.
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
  continuous symmetry, a line of fixed points, sustained flux. Bak, Tang
  and Wiesenfeld's own answer, read on 2026-11-22, is relaxation that
  stops at marginal stability, by analogy with percolation, in d ≥ 2. The
  wording
  is A's (the other assistant in the exchange "Rich Get Richer Power
  Laws", A6, A8, A23); adopting it is the owner's call.
---
<!-- inactive-ok-file: TERM-139 CLAIM-841 — filed with this question on 2026-11-21 -->
<!-- inactive-ok-file: LIT-2978 LIT-2969 — registered 2026-11-21, Deferred, unread -->
<!-- inactive-ok-file: THEORY-tmpehudh CLAIM-tmpfwwrf — Proposed or new; the reading of Bak, Tang and Wiesenfeld and the record's reproduction of the sandpile -->
<!-- inactive-ok-file: THEORY-1095 — Proposed; Toner–Tu long-range order in two dimensions -->

# QUESTION-508: Why do some systems reach scale invariance without any parameter being tuned, while others show it only at a tuned critical point?

## Why it is a question

In the language of [TERM-139](../terms.d/TERM-139.md), a fixed point with relevant directions
is reached only by tuning them: the Ising critical point needs the
temperature and the field set. Yet the exchange collects scale-invariant
laws that need no tuning: the transverse correlations of an ordered
magnet, r^(−(d−2)) throughout the phase (A27 §3); the 2D XY phase with a
temperature-dependent exponent η(T) (A12 §7, A27 §5; Kosterlitz and
Thouless, [LIT-2969](../literature.d/LIT-2969.md)); the growing interface of the KPZ equation
(A24 §3, [LIT-2978](../literature.d/LIT-2978.md)); the turbulent inertial range (A23 §2); the ordered
flock (A26 §4, A27 §7; [THEORY-1085](../theory.d/THEORY-1085.md), [THEORY-1095](../theory.d/THEORY-1095.md)); and the sandpile of
self-organized criticality (A3, A24 §4; Bak, Tang and Wiesenfeld,
[LIT-2992](../literature.d/LIT-2992.md)). [CLAIM-841](../claims.d/CLAIM-841.md) holds that these are scale-free without a
tuned transition. What it does not hold is why: what a system must have
for its long-distance behaviour to sit at a fixed point with no relevant
direction left to tune.

## Partial answers (A's, and the founding letter's)

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
  These conditions are the later framing of self-organized criticality
  (A24 §4's), not the founding letter's: Bak, Tang and Wiesenfeld
  ([LIT-2992](../literature.d/LIT-2992.md)) state none of slow drive, time-scale separation or
  conservation as a condition (see the next item).
- **Relaxation that stops at marginal stability** (Bak, Tang and
  Wiesenfeld, [LIT-2992](../literature.d/LIT-2992.md), p. 382; [THEORY-tmpehudh](../theory.d/THEORY-tmpehudh.md)). A pile relaxed from a
  strongly unstable start stops at the first stable state, and "The
  system will become stable precisely at the point when the network of
  minimally stable states has been broken down to the level where the
  noise signal cannot be communicated through infinite distances. At this
  point there will be no length scale in the problem", "similar to the
  critical point at a percolation transition". It needs two or more
  dimensions: in one "the dynamics is trivial". It asserts independence
  of details and leaves universality open ("More numerical work is
  clearly needed", p. 384), and gives no criterion of the kind asked for
  below.

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
scale-free one that meets none. [LEAD-209](../leads.d/LEAD-209.md)'s protocol would tell which
case an observed system is in; it would not by itself answer why.

A partial answer for one mechanism (for instance, that an absorbing-state
transition with a conserved field and slow drive self-organizes to its
critical point) narrows the question and is filed as a claim that
`bears_on` it.

## Note of 2026-11-22: Bak, Tang and Wiesenfeld, read

Bak, Tang and Wiesenfeld ([LIT-2992](../literature.d/LIT-2992.md), read in full in [NOTE-tmpnl00y](../notes.d/NOTE-tmpnl00y.md); the
reading is [THEORY-tmpehudh](../theory.d/THEORY-tmpehudh.md)) **give one partial answer and leave the
general question open.** Their answer, now listed above, is a
stopping-at-marginal-stability argument by analogy with percolation, not
A24 §4's feedback balance, and it adds a condition the list lacked,
d ≥ 2. Their protocol is relaxation from z ≫ K, then probing with local
perturbations; the slow-drive, time-scale and conservation conditions
the question attributes to SOC come from later work. The record's
reproduction of the sandpile under slow drive ([CLAIM-tmpfwwrf](../claims.d/CLAIM-tmpfwwrf.md)) shows a
cutoff growing with lattice size and nothing tuned, which is the
phenomenon the question asks about, not its explanation. [THEORY-tmpehudh](../theory.d/THEORY-tmpehudh.md)
`bears_on` this question. Version 2.
