---
status: Read
paper: LIT-2992
title: 'Bak, Tang and Wiesenfeld, read for the sandpile and the claim that criticality is an attractor reached without tuning'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Read in full on 2026-11-22 by a delegated reader from a course
    handout (ADR-074, ADR-113): courses.physics.ucsd.edu/2016/Spring/physics235/BTW-PRL.pdf,
    linked from the handouts page of UCSD Physics 235, Spring 2016, as
    "Bak, Tang, Wisenfeld - Pile PRL"; HTTP 200, a four-page scan of the
    published letter. The text layer is garbled around equations and
    figures, so pages 382–384 were also rendered as images and read from
    them. All four pages read: text, Eqs. (1)–(2), Figs. 1–3 and
    captions, the references. Nothing skipped. The 1988 PRA (a different
    work) was fetched and not opened. Every quotation below rechecked by
    the filer against the text layer (de-hyphenated) and, for the
    exponents in Figs. 2–3 and their captions, against the page image.
    No email address sent (OpenAlex queried without one).
date: '2026-11-22'
summary: >-
  A four-page letter proposing that spatially extended dynamical systems
  "naturally evolve into a self-organized critical point": relaxation from
  a strongly unstable start stops at the first stable state, which is
  where clusters of minimally stable sites stop percolating, so no length
  scale remains. In a sandpile automaton on 50 × 50 and 20 × 20 × 20
  lattices it finds cluster sizes D(s) ~ s^(−τ) with τ ≈ 0.98 and 1.35,
  lifetimes D(t) ~ t^(−α) with α ≈ 0.42 and 0.90, and so spectra
  f^(−1.58) and f^(−1.1), and conjectures this is "the common underlying
  mechanism" of 1/f noise and fractals. Slow drive, separated time scales
  and conservation are not stated as conditions.
---
<!-- inactive-ok-file: THEORY-tmpehudh CLAIM-841 CLAIM-795 CLAIM-803 CLAIM-809 CLAIM-850 CLAIM-804 SYNTHESIS-119 TERM-142 CLAIM-tmpfwwrf ARG-tmp1zu0m — Proposed or new; the entries this reading bears on, its own reading, the reproduction and the arguments filed with it -->

# NOTE-tmpnl00y: Bak, Tang and Wiesenfeld, read for the sandpile and the claim that criticality is an attractor reached without tuning

## Contribution

It names and proposes self-organized criticality: a critical point that is
an attractor of the dynamics, reached with no tuned parameter. It gives the
minimal-stability and percolation heuristic for why, and introduces the
sandpile automaton as the model. The reading is [THEORY-tmpehudh](../theory.d/THEORY-tmpehudh.md).

## Key results

1. **No tuning** (p. 381): "The criticality in our theory is fundamentally
   different from the critical point at phase transitions in equilibrium
   statistical mechanics which can be reached only by tuning of a
   parameter, for instance the temperature. The critical point in the
   dynamical systems studied here is an attractor reached by starting far
   from equilibrium: The scaling properties of the attractor are
   insensitive to the parameters of the model."
2. **Generality** (p. 381): "We suggest that this self-organized
   criticality is the common underlying mechanism behind the phenomena
   described above" (1/f noise, fractals, turbulence).
3. **One dimension is trivial** (p. 382): "the system is stable with
   respect to small perturbations in one dimension and the dynamics is
   trivial."
4. **The mechanism, by percolation** (p. 382, italics in the original):
   "The system will become stable precisely at the point when the network
   of minimally stable states has been broken down to the level where the
   noise signal cannot be communicated through infinite distances. At this
   point there will be no length scale in the problem"; "similar to the
   critical point at a percolation transition".
5. **Details do not matter, asserted** (p. 382): "The arguments are quite
   general and do not depend on the details of the physical system at
   hand, including the details of the local dynamics and the presence of
   impurities".
6. **Lifetimes to spectrum**, Eq. (1) (p. 382): D(t) ~ t^(−α) gives
   S(ω) ≈ ω^(−2+α).
7. **The automaton** (p. 382): z → z − 4 and each neighbour +1 "if z
   exceeds a critical value K. There are no parameters since a shift in K
   simply shifts z", with z = 0 on the boundaries. "The system is set up
   with random initial conditions z ≫ K, and then simply evolves until it
   stops ... The dynamics is then probed by measurement of the response of
   the resulting state to small local random perturbations" (read from the
   page image).
8. **Cluster sizes** (p. 383): D(s) ~ s^(−τ), τ ≈ 0.98 in 2D (Fig. 2a,
   50 × 50, 200 samples), "The fact that the curve is linear over two
   decades indicates that the system is at a critical point with a
   scaling distribution of clusters"; τ ≈ 1.35 in 3D (20 × 20 × 20). "The
   data have been coarse grained."
9. **The cutoff is finite size** (p. 383): "The falloff at the largest
   cluster sizes is due to finite-size effects, as we checked by comparing
   simulations for different array sizes." No data for the comparison are
   shown.
10. **Lifetimes**, Eq. (2) (p. 383): α ≈ 0.42 (2D) and 0.90 (3D), "These
    curves are less impressive than the corresponding cluster-size
    curves"; Fig. 3's caption gives a "1/f" spectrum f^(−1.58) in 2D and
    f^(−1.1) in 3D.
11. **1/f as the signature** (p. 384): "Our picture of 1/f spectra is that
    it reflects the dynamics of a self-organized critical state" (the
    text layer drops the hyphen at a line break; the page image has it),
    after "The resulting power-law spectrum is S(ω) ≈ ω^(−2+α) ≈ ω^(−1.58)
    in 2D and ω^(−1.1) in 3D"; and the hedge "More numerical work is
    clearly needed to improve accuracy".

The reader checked Eq. (2)'s algebra: with s = t^(1+γ) and D(s) = s^(−τ),
(s/t)·s^(−τ)·(1+γ)t^γ ∝ t^(2γ − (1+γ)τ), as printed; −2 + 0.42 = −1.58 and
−2 + 0.90 = −1.10.

## Assumptions

- Local threshold dynamics on a lattice of dimension d ≥ 2.
- Fixed boundaries z = 0. Toppling conserves z in the bulk, but the paper
  does not name conservation or boundary loss as a condition.
- Protocol: relax from z ≫ K, then probe with single local perturbations.
  Whether the probes accumulate (which would make it a slowly driven
  steady state) is not said; the words "slow drive" and "separation of
  time scales" do not appear.
- The power law is judged by eye on a coarse-grained log-log plot over two
  decades, with no fit, error bars or alternatives.

## Concepts

Self-organized criticality; locally minimally stable state; the domino
effect or avalanche; the critical state as an attractor; percolation of
minimally stable clusters; the sandpile cellular automaton; finite-size
cutoff; 1/f noise; universality (left open).

## Bearing on the record

- **[QUESTION-508](../questions.d/QUESTION-508.md)**: one partial answer, relaxation stopping at marginal
  stability by analogy with percolation, needing d ≥ 2; the slow-drive,
  time-scale and conservation conditions the question lists are the later
  framing, not this paper's.
- **[CLAIM-841](../claims.d/CLAIM-841.md)**: supports its bullet that SOC reaches a critical point
  without outside tuning (result 1); contrasts with its thesis, since the
  paper infers criticality from a straight log-log line (result 8) and
  makes SOC the common mechanism of turbulence too (result 2). [ARG-tmp1zu0m](../arguments.d/ARG-tmp1zu0m.md).
- **[CLAIM-692](../claims.d/CLAIM-692.md)**: a contrast; the paper offers 1/f as SOC's signature
  (result 11), though its own spectra are f^(−1.58) and f^(−1.1).
- **[LEAD-211](../leads.d/LEAD-211.md)**: a precedent; the finite-size check is asserted (result 9)
  and not shown. The record's reproduction, [CLAIM-tmpfwwrf](../claims.d/CLAIM-tmpfwwrf.md), shows it.
- **[CLAIM-795](../claims.d/CLAIM-795.md), [CLAIM-803](../claims.d/CLAIM-803.md), [LEAD-209](../leads.d/LEAD-209.md), [SYNTHESIS-119](../syntheses.d/SYNTHESIS-119.md)** (notes left to the
  filers holding them): τ ≈ 0.98 and 1.35 without any rich-get-richer
  rule; the paper reads mechanism from the distribution's shape, which
  [CLAIM-803](../claims.d/CLAIM-803.md) warns against, and runs one dynamical check.
- **[CLAIM-809](../claims.d/CLAIM-809.md), [CLAIM-850](../claims.d/CLAIM-850.md)**: background; their "marginal stability" is a
  scalar map near a → 1, BTW's "minimally stable" a spatial percolation
  threshold.
- **[CLAIM-804](../claims.d/CLAIM-804.md), [THEORY-1348](../theory.d/THEORY-1348.md), [TERM-142](../terms.d/TERM-142.md)**: background, and [TERM-142](../terms.d/TERM-142.md)'s sense
  of "scale-free" spans both a heavy-tailed marginal and a spectrum, as
  this paper's results do.

## Limitations

- Simulations on 50 × 50, 100 × 100 (Fig. 1) and 20 × 20 × 20 lattices
  over two decades, coarse-grained, with no fit and no error estimate.
- The finite-size check is asserted, not shown.
- τ ≈ 0.98 < 1 is not normalizable without the cutoff; the paper does not
  remark on it. τ here counts affected sites after a probe of the relaxed
  state, which is not the toppling count under slow drive used later.
- Generality and universality are argued, not shown; the empirical
  systems named in the first paragraph are not compared with the model.
