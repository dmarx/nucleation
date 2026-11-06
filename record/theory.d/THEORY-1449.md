---
number: 1449
status: Proposed
formerly:
- THEORY-tmpnzxug
promote_when: >-
  An independent replication of mutant takeover in a templated, enzyme-free
  origami replicator fed monomers each cycle, or a fit of the species
  fractions over cycles by a first-order master equation in growth and
  mutation rates published with its parameters, showing that a species
  produced only by mutation of a few percent per copy reaches dominance
  within about ten cycles when it grows faster, and that species growing
  alike approach equal shares.
title: 'Zhou, Sha, Ni, Seeman and Chaikin show that, in a non-enzymatic DNA origami dimer replicator fed fresh monomers each thermal and UV cycle, a species arising only by a designed mutation of about 3.5% per copy reaches parity within five cycles and dominates after about nine when its growth rate per cycle is higher, growth rate being the only fitness the system has, while two species that grow alike approach equal shares'
version: 1
tags:
- natural-sciences
- complex-systems
date: '2026-11-05'
source:
- LIT-2126
summary: >-
  Zhou, Sha, Ni, Seeman and Chaikin (2021), [LIT-2126](../literature.d/LIT-2126.md), read in
  [NOTE-1628](../notes.d/NOTE-1628.md), as the stand-in for He et al. (2017), [LIT-2132](../literature.d/LIT-2132.md),
  whose replicator it extends. The 3.5% is computed from a 16% per-monomer
  mismatch rate measured by AFM counts; the takeover is one run of 13
  cycles counted by AFM, with the fit's equations and per-cycle rates in
  an SI not read. Fitness here is assigned by the recognition-strand
  design, and monomers, temperatures and UV are supplied every cycle, so
  it says nothing of a population that maintains its own conditions.
---
<!-- inactive-ok-file: LIT-2132 — Unavailable or Proposed; cited from the reading of Zhou et al. (2021) as open -->

# THEORY-1449: Zhou, Sha, Ni, Seeman and Chaikin show that, in a non-enzymatic DNA origami dimer replicator fed fresh monomers each thermal and UV cycle, a species arising only by a designed mutation of about 3.5% per copy reaches parity within five cycles and dominates after about nine when its growth rate per cycle is higher, growth rate being the only fitness the system has, while two species that grow alike approach equal shares

## Source

Zhou, Sha, Ni, Seeman and Chaikin (2021), [LIT-2126](../literature.d/LIT-2126.md); read in
[NOTE-1628](../notes.d/NOTE-1628.md). It stands in for He et al. (2017), [LIT-2132](../literature.d/LIT-2132.md), which was
not reached.

## What was actually shown

- **Mutation** (Fig. 2): with three mismatched bases, "we obtain 16%
  mutated binding" per monomer; as both monomers must mismatch to
  cross-link, about 3.5% of new dimers are CD.
- **Equal growth** (Fig. 3): at "approximately equal at 3.7 and 3.9 per
  cycle", the AB and CD shares converge over 15 cycles, fitted by a
  first-order master equation (SI, not read).
- **Unequal growth** (Fig. 4): AB held to the one-sided design, at most 2
  per cycle, CD forming ladders; "the mutated CD dimers reached the same
  level as the AB dimers within only five cycles", "reaching a plateau
  after nine cycles"; 1,635 dimers counted by AFM.
- **Growth rate as fitness** (Results): "Since the growth rate is the only
  competitiveness in this artificial self-replication, the mutated CD
  dimers with a higher growth rate eventually dominated the system
  independent of the initial seed."
- **Could have come out otherwise**: mismatched ends could have failed to
  template CD at a measurable rate, mutants could have stayed rare against
  the seeded species' head start, or the fit could have failed; and near
  saturation it does deviate, which the authors attribute to sterile,
  untemplated dimers.

## What this does not say

- That the system evolves anything new: both species and their growth
  rates are designed, and mutation only moves between them.
- That anything in the population maintains its replication: monomers,
  temperatures, UV and sample splitting are supplied every cycle, so it is
  multiplication without regeneration in the sense of [CLAIM-566](../claims.d/CLAIM-566.md).
- That errors are corrected: the error rate is tuned, not repaired.
- Anything about He et al.'s own selection experiment, which neither this
  paper nor any other open source read here describes.
- That the timing is precise: the abstract says "approximately six
  generations", the Results parity at five and plateau after nine.
