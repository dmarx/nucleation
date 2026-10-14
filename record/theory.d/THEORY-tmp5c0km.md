---
status: Proposed
promote_when: >-
  A read proof of Vorob'ev's theorem (1962), or of the equivalent results
  of Kellerer (1964) or Malvestuto (1988). The review states and
  illustrates it and does not prove it. Wanted with its exact hypotheses:
  finite outcome sets, locally consistent marginals, and the
  running-intersection form of acyclicity. Refuted by a marginal scenario
  with an acyclic hypergraph and locally consistent marginals that admits
  no joint distribution. What cannot settle it: contextual examples on
  cyclic scenarios such as CHSH or KCBS, which the claim does not
  cover.
title: 'A measurement scenario whose compatibility hypergraph is acyclic admits no contextuality: locally consistent context distributions always glue to a global one, so a contextual scenario needs an induced cycle of length at least four'
version: 1
tags:
- contextuality
- mathematics
date: '2026-10-14'
source:
- LIT-263
summary: >-
  Vorob'ev (1962), as stated in Budroni, Cabello, Gühne, Kleinmann &
  Larsson (2022), [LIT-263](../literature.d/LIT-263.md), §V.B.2, Eq. 79, and App. A.6, read in
  [NOTE-tmpmru91](../notes.d/NOTE-tmpmru91.md). Distributions that agree on overlaps and sit on a
  hypergraph with the running-intersection property glue, step by step,
  to one joint distribution. For sharp measurements this means a chordal
  compatibility graph. So CHSH's square and KCBS's pentagon are the
  smallest contextual scenarios. Stated and illustrated in the review,
  not proved there.
---
<!-- inactive-ok-file: THEORY-tmpbf74l THEORY-013 — Proposed; the companion account filed from the same reading, and the account of context-dependent marginals named as outside this one -->

# THEORY-tmp5c0km: A measurement scenario whose compatibility hypergraph is acyclic admits no contextuality: locally consistent context distributions always glue to a global one, so a contextual scenario needs an induced cycle of length at least four

## Source

Budroni, Cabello, Gühne, Kleinmann & Larsson (2022), [LIT-263](../literature.d/LIT-263.md), §IV.A.2,
§V.B.1–2 (Eqs. 78–79) and App. A.6, read in [NOTE-tmpmru91](../notes.d/NOTE-tmpmru91.md). The theorem
is Vorob'ev (1962), with Kellerer (1964) and Malvestuto (1988), none
held.

## What was actually shown

Represent a marginal scenario as a hypergraph: observables are vertices,
contexts are hyperedges. Call it acyclic when its hyperedges can be
ordered E_1, …, E_n so that each E_i ∩ (E_1 ∪ … ∪ E_{i−1}) lies inside a
single earlier E_j (the running-intersection property, Eq. 78). An
equivalent condition is being the clique hypergraph of a chordal graph.
The review states Vorob'ev's theorem: "Any marginal scenario represented
by an acyclic hypergraph admits a joint probability distribution". The
surrounding text adds the hypothesis that the given distributions
coincide on their intersections.

The mechanism is gluing. For A − B − C with p₁(a,b) and p₂(b,c) agreeing
on B,

p(a,b,c) = p₁(a,b)p₂(b,c)/p(b) = p₁(a|b)p₂(c|b)p(b)  (Eq. 79),

which is Fine's construction for CHSH. The running-intersection order
lets this be repeated one context at a time.

Consequences drawn in the review:

- For sharp measurements, pairwise compatibility implies joint
  compatibility (Specker's principle). So a chordal compatibility graph
  always admits a noncontextual model.
- The smallest compatibility graphs that can be contextual contain an
  induced cycle of length ≥ 4. The square is CHSH, which needs dimension
  4 with sharp measurements. The pentagon is KCBS, the minimum in
  dimension 3 (§IV.A.2, §V.B.2, App. A.6).
- For nondegenerate observables, commutativity is transitive. The
  compatibility graph is then a disjoint union of cliques, and no
  contextuality is possible (Correggi & Morchio 2002; §V.F.2).

What could have failed: a tree-like scenario could have carried some
higher-order inconsistency that pairwise agreement misses. The theorem
says it cannot.

## What this does not say

- **Not proved in the source.** The review states the theorem, cites it
  and illustrates it on a path of three variables. Its strength here is
  that of a well-cited classical result, read secondhand.
- **Not a characterization.** Acyclicity is sufficient for every
  consistent family to glue, not necessary for a particular family to
  glue. Many behaviours on cyclic scenarios are noncontextual.
- **Not about data whose marginals disagree across contexts.** Local
  consistency is a hypothesis. With context-dependent marginals the
  question changes ([THEORY-013](THEORY-013.md); the review's §IV.C).
- **Not about Spekkens's generalized contextuality.** A qubit is
  preparation contextual ([THEORY-011](THEORY-011.md)), with no compatibility structure
  of this kind involved.

## Connections

- **[THEORY-012](THEORY-012.md)** states noncontextuality as the existence of a global
  section. This account says on which covers a global section exists for
  every consistent family: the acyclic ones. Put in sheaf terms, which
  is the reader's gloss and not the review's, acyclic covers carry no
  obstruction.
- **[CLAIM-141](../claims.d/CLAIM-141.md)** sets causal-loop consistency beside sheaf contextuality
  as local-to-global problems. Vorob'ev's theorem is the
  measurement-side statement that obstructions need cycles.
- **[THEORY-tmpbf74l](THEORY-tmpbf74l.md)**, from the same reading, is the operational
  precondition: the hypergraph means something only once contexts are
  fixed by more than joint measurability.
