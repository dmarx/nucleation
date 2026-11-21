---
status: Read
paper: LIT-tmp9tr5w
title: 'Yang and Hu — Feature learning in infinite-width networks'
version: 1
history:
- version: 1
  date: '2026-11-21'
  note: >-
    Read on 2026-11-21 by a delegated reader from arXiv 2011.14522v3 (15
    Jul 2022, 65 pp.): the abstract, §§1–5, Appendices B, C, C.1, G and
    H.1 (definitions and the statement of Theorem H.17); §§6–9 (Tensor
    Programs derivations and experiments), Appendices A, D–F and the
    proofs in H.2–H.8 skipped. Running notes on the branch
    claude/readers/mup-yanghu (ADR-108). Quotations the filing leans on
    rechecked by the filer by script against the downloaded text.
date: '2026-11-21'
summary: >-
  abc-parametrizations of wide MLPs, classified by width exponents; each
  layer's update changes its output by Θ(n^(−r_l)); feature learning iff r
  = min r_l = 0, kernel regime iff r > 0 (the Dynamical Dichotomy); μP the
  unique stable parametrization with every r_l = 0 and the readout
  maximal. O(1) training time.
---
<!-- inactive-ok-file: ADR-108 CLAIM-478 THEORY-212 THEORY-813 — Proposed; cited in the readings of 2026-11-21 -->
<!-- inactive-ok-file: CLAIM-tmpqwoxz — Proposed, Deferred or new; filed in this contribution of 2026-11-21 or the ones it builds on -->

# NOTE-tmpl3qeq: Yang and Hu — Feature learning in infinite-width networks

## Contribution

A classification of width scalings by linear conditions on exponents; the Dynamical Dichotomy between feature learning and kernel limits; μP as the maximal feature-learning parametrization; a recipe for computing such limits.

## Key results

1. **The abc form** (§1): "We parametrize each weight as W^l = n^{−a_l} w^l … initialize each w^l_αβ ∼ N(0, n^{−2b_l}) … The SGD learning rate is ηn^{−c}"; holding a_l + b_l fixed "we effectively give layer l its own learning rate" (fn. 3).
2. **Feature change as a power of width** (Definition 3.2): r is "the exponent such that ∆x^L_t(ξ) = Θ(n^{−r}). Thus, to avoid activation blowup, we want r ≥ 0; to perform feature learning, we want r = 0."
3. **Per layer** (Proposition 5.3): each layer's update contributes Θ(n^{−r_l}) to its output; r is the minimum of the r_l, and "In µP, we can calculate that r_l = 0 for all l".
4. **The dichotomy** (Corollary 3.9): a nontrivial stable parametrization "admits feature learning iff it evolves the feature kernel iff r = 0"; it "is in kernel regime iff r > 0", which fixes all features and feature kernels (Theorem H.13.2).
5. **Kernel regime fits while features are fixed** (Appendix B): in the NTK limit ∆f = Θ(1) through the initial readout's interaction with vanishing feature changes.
6. **μP** (Theorem 5.6): every W^l "is updated maximally", the readout "also initialized maximally", and μP "is the unique stable abc-parametrization with this property".
7. **Uniform bodies** (Theorem G.4): parametrizations with every hidden layer at the same exponent r form an edge of the stable polyhedron, with μP at r = 0 and NTP at r = ½.
8. **Time window** (§2): "our results only concern training time independent of width"; [31] (Mei, Misiakiewicz and Montanari) observed that the NTK and mean field limits "can be thought of as short and long time-scale regimes".

## Assumptions and concepts

MLPs in the main text; SGD, batch 1, discrete time; width-independent training time; tanh or σ-gelu for the dichotomy. Concepts: abc-parametrization, stability, nontriviality, r and r_l, kernel regime, feature learning, maximal update, uniform body.

## Bearing on the record

- **[CLAIM-tmpqwoxz](../claims.d/CLAIM-tmpqwoxz.md)** (supports; defeater (a) not met; qualified). In every kernel-regime parametrization hidden features change by Θ(n^{−r}), r > 0, while the output changes by Θ(1): a width-growing rate difference, the ε^U form with ε = 1/n per layer. Qualifications, written into the claim's version 2: uniformity among hidden layers is not what μP adds (NTP has a uniform body too, at r = ½); what μP adds is no gap between body and readout; and the fixed hidden layers are not idle in fitting (they contribute through the initial readout), they are fixed as features and kernel. The separation is proved only over O(1) steps.
- **[CLAIM-478](../claims.d/CLAIM-478.md)** (version 5; supports by instance): the fixed kernel is the relation the slow degrees of freedom settle into, and the fast output follows kernel gradient descent in it.
- **[THEORY-813](../theory.d/THEORY-813.md)** (supports its premise): Theorem H.13 fixes all feature kernels in the kernel regime.
- **Recheck**: [THEORY-212](../theory.d/THEORY-212.md) (Dominé and colleagues, "From Lazy to Rich") is the held finite-size per-layer analogue and is added to [CLAIM-tmpqwoxz](../claims.d/CLAIM-tmpqwoxz.md)'s grounds; Mei, Misiakiewicz and Montanari's time-scale reading of NTK against mean-field is not held.

## Limitations

MLPs only in the main text; O(1) time; rates are width exponents of per-step activation changes, not continuous-time rates; the dichotomy needs tanh or gelu; depth not addressed.
