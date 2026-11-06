---
number: 1303
status: Active
formerly:
- THEORY-tmp2uvxp
title: 'For an uncertain linear program, a decision fixed before the data are revealed must satisfy every realization at once (the robust counterpart, ∃ solution ∀ data), while a decision that may adjust after them need only have a feasible adjustment for each (the adjustable robust counterpart, ∀ data ∃ adjustment); the second is never more conservative and can be feasible where the first is not, the two coincide when each constraint''s uncertainty is its own, and decisions may be restricted between them by what part of the data they read or by the form of the rule'
version: 1
tags:
- operations-research
- mathematics
date: '2026-11-03'
source:
- LIT-1975
summary: >-
  Ben-Tal, Goryashko, Guslitzer and Nemirovski (2004), [LIT-1975](../literature.d/LIT-1975.md), read
  in [NOTE-1503](../notes.d/NOTE-1503.md). Active: the definitions, the two worked examples
  (checked by hand), Theorem 2.1 and its proof, and the reported inventory
  results with their sizes. It does not say the information-basis case is
  solved in general (the paper asserts it extends), nor that affine rules
  lose nothing.
---

# THEORY-1303: For an uncertain linear program, a decision fixed before the data are revealed must satisfy every realization at once (the robust counterpart, ∃ solution ∀ data), while a decision that may adjust after them need only have a feasible adjustment for each (the adjustable robust counterpart, ∀ data ∃ adjustment); the second is never more conservative and can be feasible where the first is not, the two coincide when each constraint's uncertainty is its own, and decisions may be restricted between them by what part of the data they read or by the form of the rule

## Source

Ben-Tal et al. (2004), [LIT-1975](../literature.d/LIT-1975.md), Math. Program. 99: 351–376; read in
[NOTE-1503](../notes.d/NOTE-1503.md).

## What was actually shown

- **Definitions** (eqs. 5–6): RC min_u {cᵀu : ∃v ∀ζ ∈ Z: Uu + Vv ≤ b}; ARC
  min_u {cᵀu : ∀ζ ∈ Z ∃v: Uu + Vv ≤ b}.
- **Strict gaps** (Example 1.2; the example after Theorem 2.1): RC
  infeasible where ARC is feasible for every u; RC value 0 against ARC −1.
  Both checked.
- **Theorem 2.1**: constraint-wise uncertainty (rows depending on disjoint
  blocks of a product set) and bounded adjustments make RC = ARC; proved by
  a minimax argument (appendix).
- **Two intermediate restrictions.** An information basis, "a prescribed
  portion ζᵢ of the true data" (p. 353), and the affine rule v = w + Wζ
  (AARC, eq. 8), "in-between" RC and ARC and tractable with fixed recourse
  (Theorem 3.1).
- **Inventory** (Table 2, θ = 20%, 100 simulations): cost 34,583 with on-line
  information, 35,121 with past demands, infeasible with a four-period delay
  and with none.

## What this does not say

- That the information-basis case has been worked out beyond the
  black-and-white case and Remark 4.1's linear maps.
- That the AARC equals the ARC.
- Bearing: [CLAIM-537](../claims.d/CLAIM-537.md)'s conditions I and II are this paper's ARC and RC
  in a feasibility problem; its III is an information basis given by a
  general h; [CLAIM-354](../claims.d/CLAIM-354.md)'s legibility-limited policies are this paper's
  information bases.
