---
number: 220
status: Open
formerly:
- QUESTION-tmpproc1
title: 'When are the optimal representations of an information-bottleneck or rate–distortion objective at two budgets nested, so that the coarser optimum is a (possibly noisy) function of the finer, X → Z₂ → Z₁, and when does raising the budget reorganize the optimum into a partition incomparable with the last?'
version: 1
tags:
- information-theory
- learning-theory
- representation-learning
date: '2026-10-19'
line: learned-structure
refines:
- QUESTION-217
summary: >-
  A2 of the exchange of 2026-10-19 on coarse-to-fine processes, which
  called it "the most consequential missing bridge". A hierarchy of
  optimal abstractions needs more than an optimum at each budget: it needs
  the optima to be compatible. [NOTE-676](../notes.d/NOTE-676.md) gets nesting by restricting the
  encoder to prunings of a fixed tree; nothing in the record says when it
  holds without that restriction. Rate–distortion theory's answer is
  successive refinability (Equitz and Cover, registered unread).
answered_by:
- THEORY-743
- THEORY-751
- CLAIM-387
- CLAIM-392
- THEORY-753
- THEORY-757
---
<!-- inactive-ok-file: THEORY-751 — Proposed; the successive-refinement reading, cited as open -->
<!-- inactive-ok-file: THEORY-163 — Proposed; open claims and readings named for context, nothing here rests on their being settled -->
# QUESTION-220: When are the optimal representations of an information-bottleneck or rate–distortion objective at two budgets nested, so that the coarser optimum is a (possibly noisy) function of the finer, X → Z₂ → Z₁, and when does raising the budget reorganize the optimum into a partition incomparable with the last?

## Why it is a question

A2: "Changing β does not, in general, guarantee that the new optimal
representation refines the previous one. The optimizer can reorganize
categories rather than simply subdivide them." The question is when there
are optima Z_{β₂} and Z_{β₁}, β₂ > β₁, with X → Z_{β₂} → Z_{β₁} a Markov
chain. If none exist, an optimal learner's trajectory may merge or
reshuffle categories rather than split them, and a coarse-to-fine reading
of it is wrong.

## What the record holds

- [NOTE-676](../notes.d/NOTE-676.md) (G-tree search, [LIT-868](../literature.d/LIT-868.md)): with the encoder restricted to
  prunings of a fixed quadtree, the compression trade-off gives nested
  coarse-grainings "by construction", and the tree that solves IB with
  side information is a pruning of the plain IB tree at the same β. The
  nesting is imposed, not found.
- [NOTE-631](../notes.d/NOTE-631.md) and [THEORY-163](../theory.d/THEORY-163.md) (colour naming): annealing β gives a hierarchy
  of categories with bifurcations. Whether those splits nest is not tested.
- Successive refinement of information ([LIT-1238](../literature.d/LIT-1238.md), read 2026-10-20 in
  [NOTE-988](../notes.d/NOTE-988.md); [THEORY-751](../theory.d/THEORY-751.md), Proposed). For finite alphabets, a source
  is refinable without loss iff *some* pair of optimal test channels forms
  the Markov chain X → X̂₂ → X̂₁. So the coarse description need only be a
  noisy function of the fine one. Gerrish's three-letter source fails:
  the finer optimum drops a rare letter the coarser one uses. The
  connection to the information bottleneck, as rate–distortion with
  reproductions in Δ(Y) under KL distortion, is the record's and is
  unproved.
- Deterministic encoders, answered in the negative ([CLAIM-387](../claims.d/CLAIM-387.md)). For a
  four-state source, the optimal partitions at two budgets are
  incomparable and not laminar. So no fixed tree holds both, and [NOTE-676](../notes.d/NOTE-676.md)'s
  nesting is bought by its restriction.
- Nesting with the top level ([THEORY-743](../theory.d/THEORY-743.md), from Shalizi and
  Crutchfield, [NOTE-976](../notes.d/NOTE-976.md)). Every IB optimum at every β is a stochastic
  coarsening of the causal (minimal sufficient) partition, which is the
  β → ∞ limit. So every finite optimum nests under the top. Whether two
  finite optima nest is open for stochastic encoders.
- Log-loss refinability does not close it ([NOTE-980](../notes.d/NOTE-980.md)). The known
  result (No and Weissman 2015) is for *direct* log-loss, where every
  channel at rate H − D is optimal and refinability is trivial. The
  information bottleneck is *remote* log-loss, scored on Y, and the two
  coincide only when Y is a function of X. On [CLAIM-387](../claims.d/CLAIM-387.md)'s example,
  erasure-degrading the β = 12 optimum to the β = 8 rate keeps 0.079 bits
  about Y, against 0.097 for the β = 8 optimum. The direct lead is
  Charvin, Catenacci Volpi and Polani (2023), a test by linear
  programming for exact IB refinability.
- Charvin, Catenacci Volpi and Polani (2023), read 2026-10-20
  ([NOTE-981](../notes.d/NOTE-981.md)):
  - **The criterion** ([THEORY-753](../theory.d/THEORY-753.md)). Refinable iff some pair of
    optimal encoders forms X → T₂ → T₁, iff the coarse encoder is a
    garbling of the fine one. Given a non-degenerate fine decoder, that is
    iff the coarse decoder points lie in the fine decoder's hull.
  - **Refinable at every pair of budgets** when Y = f(X), and when X and Y
    are both binary ([THEORY-757](../theory.d/THEORY-757.md)).
  - **The stochastic half, answered in the negative for one source**
    ([CLAIM-392](../claims.d/CLAIM-392.md)). For [CLAIM-387](../claims.d/CLAIM-387.md)'s source, the unique optima at β = 8 and
    12 fail the hull test. The certificate is numerical, and the cost of
    forcing nesting is small (0.49% of the budget in unique information).
- Still open: a structural condition beyond the special cases, a proof in
  exact arithmetic, whether the loss is always small, and whether
  [THEORY-163](../theory.d/THEORY-163.md)'s annealed colour hierarchy passes the test.

## What would count as an answer

A structural condition on P(X, Y) that guarantees nested IB optima, or a
small discrete distribution whose optima at two budgets are incomparable
partitions. A2's second project proposes the search: four to eight states,
all deterministic encoders enumerated by their partitions, optima found at
several β, and the refinement relation between them inspected. A2's own
limit: deterministic enumeration "does not settle the unrestricted
stochastic-encoder version of successive refinement." That half is now
done for deterministic encoders ([CLAIM-387](../claims.d/CLAIM-387.md)). The stochastic half
needs a stochastic P(Y|X): with Y a function of X the only optima are the
trivial encoder and the causal partition ([NOTE-976](../notes.d/NOTE-976.md)). It also needs a
certified optimum and a test for a degrading channel between optima.
