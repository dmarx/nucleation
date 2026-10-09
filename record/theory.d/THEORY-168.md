---
number: 168
status: Proposed
formerly:
- THEORY-tmpjdnxt
promote_when: >-
  Two things together. First, a checked second proof of the nominal-dominance
  theorem for one pair of content-sharing variables, for example from later
  Contextuality-by-Default work. Second, a worked system that shows the
  remaining asserted case: an inconsistently connected system that is
  noncontextual under maximal (CbD 1.0) couplings and has a contextual
  subsystem. A restatement in a survey does not count, and neither does
  a further example of the coarse-graining failure, which is already proved.
title: 'In Contextuality-by-Default, whether a fixed set of measurements is contextual depends on how the system is represented: which couplings are imposed, and which dichotomizations of the variables are included'
version: 1
tags:
- contextuality
- mathematics
date: '2026-10-09'
source:
- LIT-790
- LIT-831
- LIT-777
summary: >-
  Dzhafarov, Cervantes & Kujala (2017), [LIT-790](../literature.d/LIT-790.md), with Dzhafarov &
  Kujala's CbD 2.0 ([LIT-831](../literature.d/LIT-831.md)) and CbD 1.0 ([LIT-777](../literature.d/LIT-777.md)). The same
  measurements can receive different verdicts. Maximal and multimaximal
  couplings disagree when a content appears in three or more contexts.
  Multimaximal couplings of non-binary variables can be destroyed by
  coarse-graining. With every dichotomization kept, two content-sharing
  variables are contextual on their own unless one nominally dominates the
  other. The authors present the representation as the analyst's choice,
  not as a defect. What the record does not get from these papers is any
  rule for choosing it.
supports:
- CLAIM-069
---

<!-- inactive-ok-file: THEORY-013 — Proposed; its scope is what this theory bears on -->

# THEORY-168: In Contextuality-by-Default, whether a fixed set of measurements is contextual depends on how the system is represented: which couplings are imposed, and which dichotomizations of the variables are included

## Source

Dzhafarov, Cervantes & Kujala (2017), [LIT-790](../literature.d/LIT-790.md), Sections 1, 3–5 and the
supplement ([NOTE-640](../notes.d/NOTE-640.md)). Dzhafarov & Kujala (2017), [LIT-831](../literature.d/LIT-831.md),
Sections 1, 4 and 6 ([NOTE-643](../notes.d/NOTE-643.md)). Dzhafarov & Kujala (2016), [LIT-777](../literature.d/LIT-777.md),
Definition 3.4 ([NOTE-600](../notes.d/NOTE-600.md)).

## What was actually shown

Contextuality-by-Default gives each measurement a separate random
variable in each context. A system is noncontextual when some coupling of
the contexts restricts, on each content, to a prescribed coupling of that
content's copies. The verdict therefore depends on two choices: which
coupling is prescribed, and which variables are in the system. Each choice
has been made in more than one way:

1. **Maximal vs multimaximal couplings.** CbD 1.0 ([LIT-777](../literature.d/LIT-777.md)) prescribes a
   maximal coupling of each whole connection. CbD 2.0 ([LIT-831](../literature.d/LIT-831.md))
   prescribes a multimaximal one, with every subset (equivalently every
   pair) maximally coupled. The two agree for connections of two
   variables, hence for cyclic systems, and for consistently connected
   systems. The authors say they disagree on Kochen–Specker systems with
   more variables per connection. They state, without an example, that the
   1.0 definition is not hereditary.
2. **Coarse-graining non-binary variables.** Under multimaximality,
   coarse-graining can turn a noncontextual system into a contextual one.
   This is proved by example: a 6-valued connection with two multimaximal
   couplings becomes, after lumping, a 3-valued connection with none
   ([LIT-831](../literature.d/LIT-831.md), Examples 1–3).
3. **Which dichotomizations to include.** The canonical representation
   ([LIT-790](../literature.d/LIT-790.md)) replaces each variable by binary splits, and the analyst
   chooses which coarsenings to add. With all splits of two
   content-sharing k-valued variables, the pair is noncontextual if and
   only if Pr[R = x] < Pr[R′ = x] holds for at most one value x, in one
   direction or the other (Theorem 4.6, proved in the supplement). With
   only the k one-value splits, the same pair is always noncontextual.
   For continuous densities with all splits, any difference in
   distribution is contextual (Section 5, an argument rather than a
   theorem).

What could have come out otherwise: Theorem 4.6 could have found that the
all-splits system of one pair is always noncontextual, as the unsplit pair
is. The proof shows instead that the maximal couplings of the 1- and
2-splits over-determine the k × k joint table.

## What this does not say

- **Not that CbD is inconsistent.** Each version is internally coherent.
  The authors adopt multimaximality and the canonical form deliberately,
  and present the expansion as the analyst's statement of interest.
- **Not that every verdict in the CbD literature changes.** Binary cyclic
  systems, which carry most published analyses, are judged the same under
  1.0, 2.0 and the canonical form (their variables are already binary,
  and each connection has two). [THEORY-013](THEORY-013.md)'s findings are of this kind.
  They are untouched for binary data. They do not carry over to
  multi-valued responses analysed canonically, where Theorem 4.6 makes
  contextuality easy to find.
- **Not a statement about the sheaf framework.** There, a model is
  no-signalling by definition, and coarse-graining outcomes cannot raise
  the contextual fraction ([LIT-265](../literature.d/LIT-265.md), Theorem 2). The contrast concerns how
  each framework handles coarse-graining, and the papers do not compare
  them.
- **Not a rule for choosing.** The papers suggest that intervals or cuts
  may be more natural for ordered values. They do not develop it.
