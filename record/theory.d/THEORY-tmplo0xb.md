---
status: Active
title: 'In the mixed membership stochastic blockmodel the probability of an edge from p to q, given the memberships, is (1 − ρ)π_pᵀBπ_q, so the graph''s likelihood given the memberships is unchanged by π ↦ Rπ, B ↦ R⁻ᵀBR⁻¹ for any invertible R that keeps the memberships on the simplex and B in [0, 1], a continuum around any solution with B''s rates strictly between 0 and 1; and the sparsity parameter ρ enters only through (1 − ρ)B, so it is fixed by nothing but the bound B ≤ 1, and the paper''s printed estimator of it is the fraction of absent edges whatever the fit'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Active from NOTE-tmphwzim. The model and the estimators are the
    paper's §2–3 and Appendices A–B. The gauge, the confounding of ρ, and
    the reading of the printed estimator are the record's, re-derived
    below and checked numerically, which meets the condition for Active
    under ADR-047 v2. They contradict the paper's §5 statement that B and
    the memberships do not compete.
tags:
- network-science
- mathematical-statistics
- probabilistic-modeling
date: '2026-10-26'
source:
- LIT-tmpt5wer
summary: >-
  Airoldi, Blei, Fienberg and Xing (2008), LIT-tmpt5wer, read in
  NOTE-tmphwzim. The paper says the blockmodel and the memberships do not
  compete, because one is global and asymmetric and the other local and
  symmetric. Given the memberships they do: a change of block basis moves
  every node's memberships toward the centre and sharpens B, with the same
  edge probabilities. What can still separate them is the Dirichlet family
  assumed for memberships, not the graph. The confounding of ρ with B's
  scale is exact even in the marginal likelihood.
---
<!-- inactive-ok-file: CLAIM-135 — Proposed; the claim whose second achievement this bears on, open -->

# THEORY-tmplo0xb: In the mixed membership stochastic blockmodel the probability of an edge from p to q, given the memberships, is (1 − ρ)π_pᵀBπ_q, so the graph's likelihood given the memberships is unchanged by π ↦ Rπ, B ↦ R⁻ᵀBR⁻¹ for any invertible R that keeps the memberships on the simplex and B in [0, 1], a continuum around any solution with B's rates strictly between 0 and 1; and the sparsity parameter ρ enters only through (1 − ρ)B, so it is fixed by nothing but the bound B ≤ 1, and the paper's printed estimator of it is the fraction of absent edges whatever the fit

## Source

Airoldi, Blei, Fienberg and Xing (2008), *JMLR* 9:1981–2014, LIT-tmpt5wer,
read in full in NOTE-tmphwzim from the JMLR copy. The model is §2 and
§2.1, the estimators §3.2 and Appendix B. The paper's own statement, in
§5: B and the memberships are "apparently in competition for explaining
the data, possibly raising an identifiability issue. This is not the case,
however, as the blockmodel B captures global/asymmetric relations, while
the mixed membership vectors Πs capture local/symmetric relations. This
difference practically eliminates the issue, unless there is no signal in
the data to begin with." The derivations below are the record's.

## What was actually shown

**The edge probability.** For each ordered pair, z_{p→q} ~ Mult(π_p) and
z_{p←q} ~ Mult(π_q) independently, and Y(p, q) ~ Bernoulli(σ_pq) with
σ_pq = (1 − ρ) z_{p→q}ᵀ B z_{p←q}. Summing over the K² values of the two
indicators gives P(Y(p, q) = 1 | π_p, π_q) = (1 − ρ) Σ_{g,h} π_p(g) B(g, h)
π_q(h) = (1 − ρ) π_pᵀBπ_q. The indicators are drawn afresh for each pair,
so given the memberships the edges are independent (Appendix A), and the
likelihood of the graph given Π is Π_{p,q} of Bernoulli terms in
(1 − ρ)π_pᵀBπ_q.

**The gauge.** For invertible R, (Rπ_p)ᵀ(R⁻ᵀBR⁻¹)(Rπ_q) = π_pᵀBπ_q. So
(RΠ, R⁻ᵀBR⁻¹) gives the same likelihood given memberships whenever it is
a valid parameter: each Rπ_p on the simplex and R⁻ᵀBR⁻¹ in [0, 1].
Permutations always qualify, and the paper uses that freedom itself when
it "estimate[s] a permutation" of blocks to functions (§4.3.2). A
continuum qualifies too. Take R = (1 − ε)I + (ε/K)J. It is nonnegative
with columns summing to one, so it maps the simplex into itself. And
R⁻ᵀBR⁻¹ = B + O(ε), so it stays in [0, 1] for small ε when every rate of
B is strictly between 0 and 1. The change moves every membership toward
the simplex's centre and sharpens B to compensate.

The paper's reason does not block this. R⁻ᵀBR⁻¹ is still one global,
possibly asymmetric matrix, and Rπ_p is still one vector per node, used
for both directions of its edges. The split between "global/asymmetric"
and "local/symmetric" is kept by the transformation.

**What can still separate them.** If π_p ~ Dirichlet(α), then Rπ_p is not
Dirichlet-distributed for a non-permutation R. So the marginal likelihood
p(Y | α, B, ρ), with the memberships integrated out, is not shown to be
invariant, and (α, B) may be identified through the Dirichlet family. If
so, the identification is the prior's shape doing the work, not the
graph.

**ρ and B's scale.** σ_pq depends on ρ and B only through (1 − ρ)B, before
any marginalization. So for c > 1, (ρ′, cB) with 1 − ρ′ = (1 − ρ)/c gives
the same distribution of the graph, in the likelihood given memberships
and in the marginal likelihood alike, as long as cB ≤ 1. ρ is therefore
fixed only by the bound: any ρ with 1 − ρ ≥ max_{g,h} (1 − ρ)B(g, h) fits
equally well.

**The printed estimator.** ρ̂ = Σ_{p,q} (1 − Y(p, q))(Σ_{g,h} φ_{p→q,g}
φ_{p←q,h}) / Σ_{p,q} Σ_{g,h} φ_{p→q,g} φ_{p←q,h}. Each φ vector is
normalized to sum to one, so the inner sum is 1 for every pair, and ρ̂ is
the fraction of ordered pairs with no edge, whatever the fitted φ.
Footnote 9 says this equals the density-based ρ̃ = 1 − d̂ "in the case of
single membership". As printed, they are always equal.

**Checks.** With N = 6, K = 3, random memberships, B uniform on
[0.1, 0.9] and ε = 0.05: the transformed memberships summed to one and
stayed positive, R⁻ᵀBR⁻¹ stayed between 0.177 and 0.910, and every edge
probability changed by at most 2.2 × 10⁻¹⁶. The marginal of the
per-interaction indicators matched π_pᵀBπ_q. The ρ–scale trade was exact
to 6 × 10⁻¹⁷. For random normalized φ, the printed ρ̂ equalled the
fraction of zeros.

What could have failed: the per-interaction indicators could have tied
the memberships to B in a way the bilinear form does not show. They do
not, because each pair's indicators are summed out independently.

## What this does not say

- **Not that MMSB is unidentified in its marginal likelihood.** The
  Dirichlet assumption may identify (α, B) up to permutation. That is
  open, and would be shown by a theorem on the Dirichlet family or a
  counterexample.
- **Not that the paper's fits are wrong.** Its predictions of edges depend
  on π_pᵀBπ_q, which the gauge leaves alone. The readings of blocks and of
  how mixed a node is are what it touches. The school network's "few
  students display mixed membership" is a statement about one point of the
  orbit.
- **Not about the de-noising use with the indicators kept.** With the
  indicators Z fixed, the complete-data likelihood is not invariant under
  R, since Z is an assignment and not a vector to transform.

## Connections

- **CLAIM-148.** This is its gauge in bilinear form, X = ΠᵀBΠ, with the
  simplex and [0, 1] in place of nonnegativity. Like the NMF case, the
  freedom is data-dependent and larger than the permutations.
- **THEORY-tmp7wy54.** The author–topic model's gauge between topics and
  author profiles is the same kind, with the authorship matrix known.
- **CLAIM-135.** The paper's readings of blocks as factions, grades and
  protein functions reach the first achievement and, through the
  Dirichlet family, perhaps the second. §5 claims the second without an
  argument.
- **QUESTION-tmpixgs8.** A mixed-membership blockmodel of the
  communication and authority graph is the baseline its condition 4
  needs. Readings of how far each member takes part in each block of that
  baseline inherit this gauge, so any comparison should be on predictions
  of edges and outcomes, not on memberships.
