---
number: 508
status: Open
formerly:
- QUESTION-tmp3lkep
title: 'Why do some systems reach scale invariance without any parameter being tuned, while others show it only at a tuned critical point?'
version: 3
history:
- version: 2
  date: '2026-11-22'
  note: >-
    Edited in place on 2026-11-22 after Bak, Tang and Wiesenfeld
    (LIT-2992) was read (NOTE-2269, THEORY-2179): the
    feedback-onto-a-threshold answer is marked as the later framing of
    self-organized criticality, not the 1987 letter's, and the letter's
    own partial answer is added, relaxation stopping at marginal
    stability, by analogy with percolation, in two or more dimensions.
    The question and its status are unchanged.
- version: 3
  date: '2026-11-22'
  note: >-
    Edited in place on 2026-11-22 after Kardar, Parisi and Zhang
    (LIT-2978), Takeuchi and Sano (LIT-2982) and Toner and Tu (LIT-2970)
    were read, and Kosterlitz and Thouless (LIT-2969) through neighbours:
    four partial answers added (KPZ, Toner–Tu, BKT, and one system with
    both a tuned and an untuned regime), with the inferences that are the
    reader's marked so; the assistant's CLAIM-862, which states what
    three of them share, is named. The question and its status are
    unchanged.
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
  stops at marginal stability, by analogy with percolation, in d ≥ 2.
  The readings of 2026-11-22 add symmetry with the coupling's relevance
  (KPZ), symmetry with conservation (Toner and Tu), and U(1) symmetry
  with two dimensions (BKT). The
  wording
  is A's (the other assistant in the exchange "Rich Get Richer Power
  Laws", A6, A8, A23); adopting it is the owner's call.
---
<!-- inactive-ok-file: TERM-139 CLAIM-841 — filed with this question on 2026-11-21 -->
<!-- inactive-ok-file: LIT-2969 LIT-3060 — Unfetched or Deferred; Kosterlitz and Thouless, read through neighbours, and the directed-percolation letter registered from Takeuchi and Sano -->
<!-- inactive-ok-file: THEORY-2202 THEORY-2198 THEORY-2201 THEORY-2199 THEORY-2206 THEORY-2197 NOTE-2285 CLAIM-862 — Proposed, Skimmed or new; the readings of 2026-11-22 and the assistant's claim filed from them -->
<!-- inactive-ok-file: THEORY-2179 CLAIM-858 — Proposed or new; the reading of Bak, Tang and Wiesenfeld and the record's reproduction of the sandpile -->
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

## Partial answers (A's, the founding letter's, and the readings of 2026-11-22)

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
  Wiesenfeld, [LIT-2992](../literature.d/LIT-2992.md), p. 382; [THEORY-2179](../theory.d/THEORY-2179.md)). A pile relaxed from a
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

- **Symmetry, and whether the nonlinearity is relevant** (Kardar, Parisi
  and Zhang, [LIT-2978](../literature.d/LIT-2978.md), p. 889; [THEORY-2202](../theory.d/THEORY-2202.md)). The KPZ equation is
  invariant under h → h + const and under a small tilt. That the shift
  invariance forbids a restoring term ∝ h, and that the tilt symmetry is
  what keeps λ unrenormalized and fixes χ + z = 2, are the reader's
  inferences, the second later stated by Le Doussal ("Galilean
  invariance (i.e. the STS symmetry) ensures the relation χ = 2 − z",
  [THEORY-2198](../theory.d/THEORY-2198.md)); the letter itself says only that whether λ is
  relevant decides which scale-free class is reached: relevant for
  d < 2, marginally relevant at 2, and above two dimensions irrelevant
  when small, with a tuned strong-coupling threshold between two
  scale-invariant phases.
- **Symmetry plus conservation** (Toner and Tu, [LIT-2970](../literature.d/LIT-2970.md), pp. 46–50,
  63–64; [THEORY-2199](../theory.d/THEORY-2199.md)). Rotation invariance forbids a mass for the
  transverse velocity, which a compass restores; pseudo-Galilean
  invariance and exact mass conservation fix the d = 2 exponents; and
  the ordered phase's scaling belongs to "the low temperature fixed
  point", reached with nothing tuned.
- **U(1) symmetry together with two dimensions** (BKT, through
  Kosterlitz's lecture, [LIT-3053](../literature.d/LIT-3053.md), and Drouin-Touchette, [LIT-3055](../literature.d/LIT-3055.md);
  [THEORY-2206](../theory.d/THEORY-2206.md), [THEORY-2197](../theory.d/THEORY-2197.md)). A free vortex's energy and its
  entropy both grow as ln L, so below T_KT the fugacity, the one relevant
  candidate, flows to zero on a line of fixed points. The symmetry alone
  does not do it: the logarithm is a two-dimensional fact. A finite
  interaction range, the penetration depth λ of a charged film, cuts off
  the logarithm and frees vortices "at any T > 0" (lecture, p. 98).
- **One system, both regimes** (Takeuchi and Sano, [LIT-2982](../literature.d/LIT-2982.md);
  [THEORY-2201](../theory.d/THEORY-2201.md)). Nematic electroconvection shows tuned
  directed-percolation criticality at the DSM1–DSM2 threshold
  ("spatiotemporal intermittency", p. 2; [LIT-3060](../literature.d/LIT-3060.md), registered,
  unread, known by its title) and untuned KPZ growth well above it, which
  the authors credit to local growth, intrinsic noise and no quenched
  disorder. So the answer is not a property of a system as a whole but
  of a regime.

The assistant's [CLAIM-862](../claims.d/CLAIM-862.md) states what the first three share: a
protection, and a perturbation that undoes it; it bears on this question
and leaves the feedback, flux and growth routes aside.

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

Bak, Tang and Wiesenfeld ([LIT-2992](../literature.d/LIT-2992.md), read in full in [NOTE-2269](../notes.d/NOTE-2269.md); the
reading is [THEORY-2179](../theory.d/THEORY-2179.md)) **give one partial answer and leave the
general question open.** Their answer, now listed above, is a
stopping-at-marginal-stability argument by analogy with percolation, not
A24 §4's feedback balance, and it adds a condition the list lacked,
d ≥ 2. Their protocol is relaxation from z ≫ K, then probing with local
perturbations; the slow-drive, time-scale and conservation conditions
the question attributes to SOC come from later work. The record's
reproduction of the sandpile under slow drive ([CLAIM-858](../claims.d/CLAIM-858.md)) shows a
cutoff growing with lattice size and nothing tuned, which is the
phenomenon the question asks about, not its explanation. [THEORY-2179](../theory.d/THEORY-2179.md)
`bears_on` this question. Version 2.

## Note of 2026-11-22: Kardar, Parisi and Zhang, and Takeuchi and Sano, read

KPZ ([LIT-2978](../literature.d/LIT-2978.md), [NOTE-2287](../notes.d/NOTE-2287.md), [THEORY-2202](../theory.d/THEORY-2202.md)) **gives a partial answer
for interfaces**, listed above, and marks a limit: the untuned reach of
the class is d ≤ 2. Takeuchi and Sano ([LIT-2982](../literature.d/LIT-2982.md), [NOTE-2284](../notes.d/NOTE-2284.md),
[THEORY-2201](../theory.d/THEORY-2201.md)) **give a contrast within one system** and conditions
(locality, intrinsic noise, no quenched disorder) for that system only.
Both THEORYs `bears_on` this question. Version 3.

## Note of 2026-11-22: Toner and Tu (1998), read

Toner and Tu ([LIT-2970](../literature.d/LIT-2970.md), [NOTE-2285](../notes.d/NOTE-2285.md), [THEORY-2199](../theory.d/THEORY-2199.md)) **give a partial
answer for flocks**, listed above: symmetry plus conservation, the
answer A's "Symmetry removes the restoring term" bullet gives, with a
conservation law added. [THEORY-2199](../theory.d/THEORY-2199.md) `bears_on` this question.

## Note of 2026-11-22: Kosterlitz and Thouless, through two neighbours

The lecture and the notes ([THEORY-2206](../theory.d/THEORY-2206.md), [THEORY-2197](../theory.d/THEORY-2197.md)) **narrow the
line-of-fixed-points answer**: it is not "symmetry removes θ²" alone but
symmetry with dimension, and a finite interaction range ends it, which
has the shape of the counterexample the question asks for, an
introduced length ending an untuned phase. Both THEORYs `bears_on` this
question.

