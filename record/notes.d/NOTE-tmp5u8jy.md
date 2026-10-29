---
status: Read
paper: 'LIT-1123'
title: 'Jansma and Hoel — Engineering emergence'
version: 1
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Read in full on 2026-10-29 from arXiv's own copy, v2 of 14 October
    2025 (https://arxiv.org/pdf/2510.02649, 29 pages), text extracted
    with pdftotext. Read: the abstract, §§1–4, the supplement S1–S3 with
    its three algorithms, the figure captions and the 46 references.
    Figures 1–6 were read from their captions and the text only; no
    number was taken from a chart, and no TPM is printed, so no example
    was recomputed. Checked: the partition counts 2, 5, 15, 52, 877 and
    4,140 are the Bell numbers B₂–B₅, B₇ and B₈; Figure 2's microscale
    and right-hand macroscale CP values equal determinism − degeneracy,
    and the left-hand one does not (see Limitations). v1 (3 October
    2025) was not compared.
date: '2026-10-29'
summary: >-
  Extends causal emergence 2.0 from one micro→macro path to the whole
  lattice of partitions of a Markov chain's states: a partition's ∆CP is
  its CP minus the largest CP of any finer partition, and the partitions
  with ∆CP > 0 form the "emergent hierarchy". Shown on 5- and 8-state
  chains by enumeration and on 40-state preferential-attachment chains by
  a greedy sampler, where the spread of ∆CP within and across levels
  peaks near linear attachment; cycles let a single emergent scale be
  placed at any level. No theorem; the dynamical-consistency filter of
  CE 2.0 is dropped.
---
<!-- inactive-ok-file: THEORY-257 — Proposed; named as related work the paper cites, nothing here rests on it -->

# NOTE-tmp5u8jy: Jansma and Hoel — Engineering emergence

## Contribution

CE 2.0 ([LIT-1136](../literature.d/LIT-1136.md)) credited causal contribution along one chosen path of
coarse-grainings. This paper removes the choice: every partition of the
state space is scored against every finer partition, so a scale counts
only if it beats all scales below it on any path. The surviving
partitions form a sublattice the authors call the emergent hierarchy. It
then defines two entropies over that hierarchy, ties their product to
preferential attachment, and builds chains whose hierarchy has exactly
one member.

## Key insight

Among the Bell-number many partitions of a state space, almost all
coarse-grainings make transitions noisier; the few that make them more
deterministic or less degenerate than everything beneath them are a small
lattice. Where that lattice puts its weight (near the microscale, near the
top, or spread across levels and within them) is a property of the
dynamics, and it can be designed.

## Assumptions

- **A known, Markovian, ground-truth TPM** with no hidden confounders, so
  p(X_{t+1} | do(X_t = x)) = p(X_{t+1} | X_t = x) (S1).
- **Uniform intervention distribution at every scale** (§4), as in CE 2.0.
- **Partitions of states only**, not of variables or mechanisms (S1).
- **No consistency check.** Unlike CE 1.0 and 2.0, partitions that are not
  dynamically consistent are kept, because filtering "did not alter our
  results in a significant way (data not shown)" (§4).

## Key results

- **Causal primitives (§2).** determinism = 1 − H(E | C)/log₂ n,
  degeneracy = 1 − H(E)/log₂ n, CP = determinism + specificity − 1 =
  determinism − degeneracy, "equivalent to the effectiveness" of Hoel et
  al. 2013.
- **∆CP over the lattice (§3.1, Algorithm 1).** ∆CP(P) = CP(P) − max CP
  over the partitions refining P; the emergent hierarchy is {P : ∆CP > ε}.
  On a 5-state source–cycle–sink chain, 5 of the 52 partitions survive
  and the intuitive (source)(cycle)(sinks) one has the largest ∆CP.
  Summed ∆CP is "generally not" 1.
- **A taxonomy (Fig. 4).** Five 8-state chains give top-heavy,
  bottom-heavy, mesoscale-peaked and single-scale ("balloon")
  hierarchies.
- **Two complexity terms (§3.2).** S_path, the mean entropy of normalized
  ∆CP along paths through the hierarchy (CE 2.0's emergent complexity,
  averaged), and the row negentropy log₂ L − S_row, high when ∆CP differs
  between partitions of the same size.
- **Preferential attachment (§3.3, Fig. 5).** 40-node trees grown with
  attachment exponent α and m = 1, made into TPMs by normalizing
  out-links, five networks per α, 100 sampled paths: bottom-heavy for
  α < 1, top-heavy for α > 1.5, with the product of the two terms
  highest near α = 1. The authors call this "literal scale-freeness" and
  say it overlaps with, but is likely not identical to, the
  degree-distribution sense.
- **Pinpoint emergence (§3.4, Fig. 6).** A cycle has no intermediate
  simplifying scale, so a level-l chain built from one c-cycle (c ≤ l)
  plus l − c permutations, or from l disjoint cycles, has a single
  contributing macroscale among 877 partitions (7 states; stay 0.2,
  advance 0.8).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Scoring each partition against all finer ones leaves a small "emergent hierarchy" | moderate | definition; enumeration on 5- and 8-state chains |
| C2 | Hierarchies differ in shape (top-heavy, bottom-heavy, mesoscale, single) | moderate | five hand-built 8-state chains |
| C3 | Emergent complexity peaks near linear preferential attachment | weak | 40-state networks, five per α, greedy sampling, no error model for the sampler |
| C4 | Cycles and permutations place a single emergent scale at any chosen level | moderate | construction, Fig. 6 |
| C5 | Dropping dynamical consistency does not change the results | weak | "data not shown" |

## Method

Algorithm 1 enumerates all partitions, coarse-grains the TPM by each,
builds the refinement lattice and takes ∆CP relative to the best
ancestor (finer partition). Algorithms 2–3, for larger chains, start at
the microscale, try every pairwise merge of blocks, keep the best few,
complete each greedily to the top, and score only the partitions visited.
The authors say it runs in subexponential time; no bound is given.

## Concepts

- **Emergent hierarchy**: the partitions with positive ∆CP, ordered by
  refinement.
- **Ancestor**: in Algorithm 1, a finer partition, i.e. one below P on
  some micro→macro path.
- **Literal scale-freeness**: no one scale of description dominating the
  causal workings, as measured by the two entropies.
- **Pinpoint emergence**: a hierarchy with one member.

## Connections

It extends CE 2.0 ([LIT-1136](../literature.d/LIT-1136.md)) and through it Hoel, Albantakis and Tononi
2013 ([LIT-1038](../literature.d/LIT-1038.md)). It cites Zhang et al.'s dynamical reversibility
([LIT-1129](../literature.d/LIT-1129.md)) as an alternative to CE 1.0 that "will likely need to be
expanded", Mediano et al.'s information-decomposition review ([LIT-025](../literature.d/LIT-025.md)),
Rosas et al.'s "software in the natural world" ([LIT-1306](../literature.d/LIT-1306.md)) and Barnett and
Seth's dynamical independence ([THEORY-257](../theory.d/THEORY-257.md)) as other approaches to
macroscales, and Jansma's Möbius-inversion mereology and Forré and
Jansma's Shapley values as possible apportioning schemes that would
conserve total CP (neither registered).

## Bearing on the record

- **[QUESTION-115](../questions.d/QUESTION-115.md).** This is the candidate the record filed for A10's
  "2024/2025" paper "on searching for coarse-grainings rather than
  assuming them". It does search: every partition is scored, and the
  output is a set of scales rather than one. Read against the question,
  it searches partitions of one system's states, not system–environment
  boundaries, and it prices nothing: there is no Occam term, and a
  partition survives on any positive margin over ε. The question's
  "profile across criteria" is matched here by a profile across scales
  under one criterion.

No instruction for machine-learning practice; nothing for the anthology.
The discussion's remarks on brain–computer interfaces and human autonomy
are not argued.

## Limitations

- **Small systems.** 5, 7 and 8 states by enumeration; 40 by the greedy
  sampler, whose coverage of the lattice is not measured.
- **Not an apportioning.** ∆CP values do not sum to the total CP, which
  the authors concede, and the text then says "in practice the sum of
  ∆CP reflects the total possible CP" without showing it.
- **Inconsistent macroscales are admitted**, so some scored scales do not
  describe the microscale's dynamics.
- **Errors and slips.** Figure 2's left-hand macroscale is given
  determinism 0.24 and degeneracy 0.09, which make CP 0.15 (0.14–0.16
  allowing for rounding), but the text gives 0.13; the other two panels
  agree with CP = determinism − degeneracy (0.74 − 0.11 = 0.63,
  0.84 − 0.00 = 0.84). S_path is called the average of the path
  entropies but written as their sum. The row negentropy subtracts S_row
  from log₂ L, the log of the number of levels, though the entropy of a
  row is bounded by the log of the number of partitions in that row, so
  the "negentropy" is not bounded below by zero by construction. Eq. (1)
  writes p(e|c) with T_ce = p(e|c), and eq. (3) then writes T_ec.

## Open questions

- Would an apportioning that conserves total CP (Möbius or Shapley, as
  the authors suggest) keep the same hierarchy?
- Does the α ≈ 1 peak survive larger networks, m > 1, and the
  consistency filter?
- Can the emergent hierarchy pick out a boundary of a system embedded in
  an environment, which is what the record's individuation questions
  need?
