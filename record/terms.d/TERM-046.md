---
number: 46
status: Active
formerly:
- TERM-tmpgthc0
title: 'notation for the threshold, drive and unity criteria'
version: 1
tags:
- mathematics
- complex-systems
date: '2026-10-11'
summary: >-
  One place for the symbols used across the threshold criterion, the
  drive profile and the unity and persistence claims of 2026-10-11: δ, ε,
  τ, d′, Occam, D, G, Φ and γ. It records that δ/ε is used in two senses,
  a spectral gap against off-block coupling and a posterior effect against
  its uncertainty, and that treating them as one is an assumption carried
  over from [MOM-CLM-160](https://github.com/dmarx/mathematics-of-meaning/blob/main/record/claims.d/CLM-160.md).
used_by:
- CLAIM-153
- CLAIM-154
- CLAIM-157
- CLAIM-158
- CLAIM-161
- CLAIM-164
- CLAIM-174
---
<!-- inactive-ok-file: CLAIM-154 CLAIM-164 CLAIM-157 CLAIM-153 CLAIM-161 CLAIM-158 — claims whose symbols this term fixes, cited for their notation -->

# TERM-046: notation for the threshold, drive and unity criteria

## Definition

| symbol | meaning | where it is used |
|---|---|---|
| **δ (spectral)** | the gap separating a cluster of singular values, or a block of strong couplings, from the rest | [CLAIM-164](../claims.d/CLAIM-164.md); Simon's near-decomposability, [LIT-905](../literature.d/LIT-905.md) |
| **ε (spectral)** | the size of couplings across a block's edge, or of a perturbation | [CLAIM-164](../claims.d/CLAIM-164.md) (Davis–Kahan bound ‖δT‖/δ) |
| **δ (Bayesian)** | the posterior effect μ of a candidate direction | [CLAIM-154](../claims.d/CLAIM-154.md) |
| **ε (Bayesian)** | the posterior standard deviation σ of that direction | [CLAIM-154](../claims.d/CLAIM-154.md) |
| **d′** | δ/ε in the Bayesian sense, μ/σ | [CLAIM-154](../claims.d/CLAIM-154.md) |
| **Occam** | ln(s²/σ²): prior-to-posterior variance ratio, the information the data added | [CLAIM-154](../claims.d/CLAIM-154.md) |
| **τ** | the threshold, τ² = Occam; reify when d′ > τ | [CLAIM-154](../claims.d/CLAIM-154.md), [CLAIM-157](../claims.d/CLAIM-157.md) |
| **D** | downward causation: a macro-variable's unique power to predict individual parts' futures (ΦID) | [TERM-051](TERM-051.md), [CLAIM-158](../claims.d/CLAIM-158.md), [LIT-025](../literature.d/LIT-025.md) |
| **G** | causal decoupling: a macro-variable's unique power to predict its own future (ΦID) | same |
| **Φ** | monodromy around a cycle of contexts, α₁₂ + α₂₃ + α₃₁ | [CLAIM-153](../claims.d/CLAIM-153.md) |
| **γ** | a coherence measure whose conservation along the system's own dynamics is persistence | [CLAIM-161](../claims.d/CLAIM-161.md) |
| **V, X** | macro-variable and its micro-parts | [TERM-051](TERM-051.md) |

**The two senses of δ/ε.** The threshold criterion ([CLAIM-157](../claims.d/CLAIM-157.md)) joins
them. It uses the spectral sense to *find* a block, and the Bayesian sense
to *price* it. [MOM-CLM-160](https://github.com/dmarx/mathematics-of-meaning/blob/main/record/claims.d/CLM-160.md) identifies the two: ε as the posterior standard
deviation of a direction is its Cramér–Rao floor, and δ as the posterior
effect is the gap. That identification holds when the candidate direction
is a parameter of a fitted model, so the spectral gap of a coupling matrix
must first be expressed as an estimated parameter with a posterior. It is
an assumption of the criterion, stated here, and it is not shown in
general.

## What it is not

- **Not new mathematics.** It fixes symbols the claims already use. A claim
  that needs a symbol in a new sense adds a row here, or supersedes this
  term, rather than redefining the symbol in its own text.
