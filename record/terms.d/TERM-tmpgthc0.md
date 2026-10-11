---
status: Active
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
- CLAIM-tmp3u2m7
- CLAIM-tmp45kkg
- CLAIM-tmp8tsw5
- CLAIM-tmp99nuu
- CLAIM-tmpdqsrb
- CLAIM-tmpjsasy
- CLAIM-tmpwv313
---
<!-- inactive-ok-file: CLAIM-tmp45kkg CLAIM-tmpjsasy CLAIM-tmp8tsw5 CLAIM-tmp3u2m7 CLAIM-tmpdqsrb CLAIM-tmp99nuu — claims whose symbols this term fixes, cited for their notation -->

# TERM-tmpgthc0: notation for the threshold, drive and unity criteria

## Definition

| symbol | meaning | where it is used |
|---|---|---|
| **δ (spectral)** | the gap separating a cluster of singular values, or a block of strong couplings, from the rest | [CLAIM-tmpjsasy](../claims.d/CLAIM-tmpjsasy.md); Simon's near-decomposability, [LIT-tmp6qp14](../literature.d/LIT-tmp6qp14.md) |
| **ε (spectral)** | the size of couplings across a block's edge, or of a perturbation | [CLAIM-tmpjsasy](../claims.d/CLAIM-tmpjsasy.md) (Davis–Kahan bound ‖δT‖/δ) |
| **δ (Bayesian)** | the posterior effect μ of a candidate direction | [CLAIM-tmp45kkg](../claims.d/CLAIM-tmp45kkg.md) |
| **ε (Bayesian)** | the posterior standard deviation σ of that direction | [CLAIM-tmp45kkg](../claims.d/CLAIM-tmp45kkg.md) |
| **d′** | δ/ε in the Bayesian sense, μ/σ | [CLAIM-tmp45kkg](../claims.d/CLAIM-tmp45kkg.md) |
| **Occam** | ln(s²/σ²): prior-to-posterior variance ratio, the information the data added | [CLAIM-tmp45kkg](../claims.d/CLAIM-tmp45kkg.md) |
| **τ** | the threshold, τ² = Occam; reify when d′ > τ | [CLAIM-tmp45kkg](../claims.d/CLAIM-tmp45kkg.md), [CLAIM-tmp8tsw5](../claims.d/CLAIM-tmp8tsw5.md) |
| **D** | downward causation: a macro-variable's unique power to predict individual parts' futures (ΦID) | [TERM-tmpuyzeb](TERM-tmpuyzeb.md), [CLAIM-tmp99nuu](../claims.d/CLAIM-tmp99nuu.md), [LIT-025](../literature.d/LIT-025.md) |
| **G** | causal decoupling: a macro-variable's unique power to predict its own future (ΦID) | same |
| **Φ** | monodromy around a cycle of contexts, α₁₂ + α₂₃ + α₃₁ | [CLAIM-tmp3u2m7](../claims.d/CLAIM-tmp3u2m7.md) |
| **γ** | a coherence measure whose conservation along the system's own dynamics is persistence | [CLAIM-tmpdqsrb](../claims.d/CLAIM-tmpdqsrb.md) |
| **V, X** | macro-variable and its micro-parts | [TERM-tmpuyzeb](TERM-tmpuyzeb.md) |

**The two senses of δ/ε.** The threshold criterion ([CLAIM-tmp8tsw5](../claims.d/CLAIM-tmp8tsw5.md)) joins
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
