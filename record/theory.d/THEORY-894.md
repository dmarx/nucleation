---
number: 894
status: Active
formerly:
- THEORY-tmp4zhyp
title: 'A flow of pairwise comparisons on a graph splits orthogonally and uniquely into a gradient part, the l2-best global ranking, and a cyclic part, which splits into curl (local) and harmonic (global) inconsistency; a finite game''s flow of unilateral payoff differences has no curl part, so every finite game is uniquely a potential game plus a harmonic game plus a nonstrategic remainder, and potential games are exactly those with no harmonic part; the decomposition is cardinal'
version: 1
tags:
- mathematics
- game-theory
- mathematical-statistics
date: '2026-10-23'
source:
- LIT-1439
- LIT-1442
summary: >-
  Jiang, Lim, Yao & Ye (2011), [LIT-1439](../literature.d/LIT-1439.md), Theorems 4.7, 4.8 and 5.1:
  the Hodge/Helmholtz decomposition of edge flows, and HodgeRank's
  least-squares ranking with its curl and harmonic residuals. Candogan,
  Menache, Ozdaglar & Parrilo (2011), [LIT-1442](../literature.d/LIT-1442.md), Theorems 4.1 and
  5.1: every finite game is P ⊕ H ⊕ N, and potential games are P ⊕ N.
  Both read from arXiv; the proofs were followed. Settled as mathematics.
  Whether its shares measure a negotiation's potential depends on
  cardinal assumptions that the record's orderings do not supply.
supports:
- CLAIM-434
- CLAIM-444
---
<!-- inactive-ok-file: TERM-076 CLAIM-440 CLAIM-436 QUESTION-268 — Proposed, Open or draft; the term, claims and question this result bears on, and the ordinal result filed with it -->

# THEORY-894: A flow of pairwise comparisons on a graph splits orthogonally and uniquely into a gradient part, the l2-best global ranking, and a cyclic part, which splits into curl (local) and harmonic (global) inconsistency; a finite game's flow of unilateral payoff differences has no curl part, so every finite game is uniquely a potential game plus a harmonic game plus a nonstrategic remainder, and potential games are exactly those with no harmonic part; the decomposition is cardinal

## Source

- Jiang, Lim, Yao and Ye (2011), *Statistical ranking and combinatorial
  Hodge theory*, [LIT-1439](../literature.d/LIT-1439.md). Theorem 4.7 (p. 18), Theorem 4.8 (p. 19),
  Theorem 5.1 (pp. 21–22) and Theorem 5.2 (p. 24), as read in
  [NOTE-1099](../notes.d/NOTE-1099.md) from arXiv 0811.1067v2.
- Candogan, Menache, Ozdaglar and Parrilo (2011), *Flows and
  Decompositions of Games*, [LIT-1442](../literature.d/LIT-1442.md). Theorem 3.1 (p. 11), eq. (25)
  (p. 14), Theorem 4.1 (pp. 17–18), Theorem 5.1 (p. 22) and Theorems
  6.1–6.2 (pp. 35–36), as read in [NOTE-1116](../notes.d/NOTE-1116.md) from arXiv 1005.2405v2.
  The journal versions were not seen, and their numbering may differ.

## What was actually shown

**Flows.** On a graph, an edge flow is an antisymmetric function on
ordered adjacent pairs. The gradient of a function s on nodes is (grad
s)(i, j) = s_j − s_i. The curl of a flow on a triangle is X_ij + X_jk +
X_ki.

**Theorem 4.8 of Jiang et al. (Helmholtz decomposition).** For an
undirected graph G with clique complex K_G, the edge flows split
orthogonally as im(grad) ⊕ ker(Δ₁) ⊕ im(curl*). The middle term, the
harmonic flows, is ker(curl) ∩ ker(div): "an edge flow is harmonic iff it
is both curl-free and divergence-free". Theorem 4.7 is the general Hodge
decomposition of k-cochains, proved in the paper. Candogan et al.'s
Theorem 3.1 states the same split for flows on any graph.

**Theorem 5.1 of Jiang et al. (HodgeRank).** For a weighted flow Ȳ, the
weighted least-squares score s* = −Δ₀† div Ȳ gives the gradient part. The
residual R* is divergence-free and is the sum of a curl part, "a local
cyclic ranking accounting for local inconsistencies", and a harmonic part,
"a harmonic ranking accounting for global inconsistencies". On a complete
graph with equal weights, s* is the Borda count. By Theorem 5.2, when the
3-clique complex has β₁ = 0, every curl-free flow is a gradient.

**Games (Candogan et al.).** A finite game's flow is the unilateral payoff
difference on the graph of strategy profiles. It is always curl-free
(eq. 25), because every triangle of that graph lies within one player's
deviations. Pulling the Helmholtz decomposition back through the map from
payoffs to flows gives Theorem 4.1: "The space of games GM,E is a direct
sum of the potential, harmonic and nonstrategic subspaces". The components
are given in closed form, and the potential function is φ = δ₀†Du. Theorem
5.1: "The set of potential games is equal to the subspace P ⊕ N". The
subspaces do not depend on an inner product. Their orthogonality, and the
closest potential game of Theorem 6.2, are taken under a weighted l2 inner
product.

The reader followed both proofs. Candogan et al.'s pull-back argument and
Jiang et al.'s proof of Theorem 4.7 are each a page of linear algebra, and
neither has a gap the reader found.

## What this does not say

- **That the shares are ordinal.** Everything is cardinal. Jiang et al.
  are explicit that their inconsistency "is a cardinal condition" and
  differs from intransitivity (p. 30), and that the ordinal analogue of
  Theorem 5.2 fails (p. 24). Two checks in the record make the point
  concrete.
  - A perfectly transitive binary tournament has cyclic share (n − 2)/3n
    ([NOTE-1099](../notes.d/NOTE-1099.md)).
  - The baseline holds only for a complete tournament contesting every
    pair once; a transitive record on a sparse graph leaves a different
    share ([CLAIM-434](../claims.d/CLAIM-434.md), part 6).
  - The gradient can reverse a comparison the record settles: margins A
    over B by 1, B over C by 10 and A over C by 1 put B above A (part 4).
  - A 2×2 game whose norm is 61% harmonic has no improvement cycle
    ([NOTE-1116](../notes.d/NOTE-1116.md)).

  The ordinal counterpart of "potential exists" is [THEORY-896](THEORY-896.md), and
  it is not a share of anything.
- **That the share is invariant.** Shares depend on how comparisons are
  aggregated, on the weights and on the inner product. For games they
  depend on each player's cardinal payoff scale.
- **That a game's potential is a collective ranking.** In Candogan et
  al., φ is a function on joint profiles that tracks unilateral
  incentives. In Jiang et al., s is a ranking of alternatives fitted to
  comparisons. They are the same mathematics on different graphs, and
  they answer different questions about a negotiation ([NOTE-1116](../notes.d/NOTE-1116.md)).
- **That the published cyclicity ratios can be trusted as given.**
  Orthogonality bounds C_p by 1, but the arXiv Table 1 reports 1.15
  ([NOTE-1099](../notes.d/NOTE-1099.md)).

## Connections

Supplies the measure the renamed [TERM-076](../terms.d/TERM-076.md) and [QUESTION-268](../questions.d/QUESTION-268.md)
need, subject to the limits above. [CLAIM-436](../claims.d/CLAIM-436.md) is the reason those
limits matter: an ordering is not a currency, and both decompositions
need a currency as input.
