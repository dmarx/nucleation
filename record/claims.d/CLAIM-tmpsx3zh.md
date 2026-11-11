---
status: 'Proposed'
title: "A correspondence fitted from two structures' internal similarities alone is identified only up to their symmetries: Gromov–Wasserstein and co-optimal transport cost every coupling the same as its composite with a symmetry, and anchors break only the ties that move them, so such a fit cannot by itself validate a correspondence and an anchor validates it only against the symmetries it moves"
version: 1
role: 'thesis'
warrant: 'demonstrated'
defeated_if: >-
  An error in one of the three results it joins: a pair of similarity
  structures and a coupling whose Gromov–Wasserstein cost changes when it
  is composed with an automorphism of either structure; a pair of
  co-optimal transport plans whose cost changes under a joint relabelling
  of rows and columns that leaves the matrix unchanged; or, in fused
  Gromov–Wasserstein with α strictly between 0 and 1, an anchor fixed by
  some automorphism that nonetheless removes that automorphism from the
  zero-cost matchings. Also defeated as an entry if it only restates
  CASE-185's design: it must state, as a result the argument can rest on,
  what the case names only as a threat to one study.
tags:
- mathematics
- translation
date: '2026-11-11'
line:
- pragmatic-transport
grounds:
- THEORY-1133
- THEORY-1155
- THEORY-1129
corroborates:
- CLAIM-143
summary: >-
  Raised by the reading review of 2026-11-11 (by topic, mathematics;
  ADR-091). Three readings in force that no line used each show one
  structure-matching objective blind to the symmetries of what it
  matches. CASE-185 names them as the threat to identification in its
  correspondence arm, and CLAIM-143's proviso asks that a correspondence
  be "independently anchored and empirically validated"; no claim stated
  the result between them. It is the readings' results joined, applied
  to fitted correspondences. The wording is the assistant's (Claude, in
  this session); adopting it is the owner's call.
---

# CLAIM-tmpsx3zh: A correspondence fitted from two structures' internal similarities alone is identified only up to their symmetries: Gromov–Wasserstein and co-optimal transport cost every coupling the same as its composite with a symmetry, and anchors break only the ties that move them, so such a fit cannot by itself validate a correspondence and an anchor validates it only against the symmetries it moves

## The claim

Three readings, each proved and checked, show the same blindness in three
objectives used to fit a correspondence between two structures without a
map between their spaces:

- **Gromov–Wasserstein** sees each space only through its within-space
  similarity matrix and weights. Any coupling composed with an automorphism
  of either structure costs exactly what it did, and the entropic version
  inherits the tie (THEORY-1133). On a tree with three identical branches,
  entropic GW from twenty random starts never found the true labelling.
- **Co-optimal transport** couples samples and features jointly. Its
  plans are identified at best up to the joint symmetries of the matrices,
  which can exchange a block of samples together with its block of
  features when neither exchange alone is a symmetry (THEORY-1155).
- **Anchors in fused Gromov–Wasserstein**, with α strictly between 0 and
  1, leave as zero-cost matchings exactly the automorphisms that fix every
  anchor (THEORY-1129). Two antipodal anchors on a 6-cycle still leave
  a reflection.

Joined: a fit that minimizes structural disagreement returns one member of
an orbit and has nothing in its objective to prefer it to the others. So
the fit alone cannot validate the correspondence it returns, and anchors
validate it only against the symmetries they move. Which symmetries a set
of anchors leaves can be decided from the structure before any fit.

This is CLAIM-143's proviso met in one formal setting. The claim says a
correspondence "fitted to make the disagreement disappear decides
nothing" and must be "independently anchored and empirically validated".
Here the fitted correspondence is not even unique, and the readings say
what anchoring must do to fix it. CASE-185's correspondence arm names
the same three results as "a second threat", identification, to a
proposed study of translation routes.

## What it does not say

- **That real response structures have exact symmetries.** The readings
  say exact symmetries are rare in noisy data. They give near-ties instead
  (THEORY-1155: with noise the next-best plan cost only 5.4 × 10⁻⁴ more).
  How near is not bounded here.
- **That structure-matching is useless.** On a generic structure without
  symmetry, entropic GW recovered a hidden permutation exactly
  (THEORY-1133).
- **That anchors which break every symmetry make the correspondence
  right.** They make it unique under the objective. Whether it is the
  correspondence a task needs is CLAIM-143's second step, validation
  on other tasks.
- **Anything about the solvers**, which reach only stationary points.
