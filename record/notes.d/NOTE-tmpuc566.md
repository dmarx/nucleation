---
status: Read
paper: LIT-tmpp6b7j
title: 'Bernstein and Newhouse — Modular duality'
version: 1
history:
- version: 1
  date: '2026-11-21'
  note: >-
    Read on 2026-11-21 by a delegated reader from arXiv 2410.21265v2 (6
    Dec 2024): the whole text (§§1–7, Table 1, references). Running notes
    on the branch claude/readers/modular-duality (ADR-108). Quotations the
    filing leans on rechecked by the filer by script against the
    downloaded text.
date: '2026-11-21'
summary: >-
  A duality map for any network, induced recursively through the modular
  norm from per-layer operator norms; for a linear layer under the RMS→RMS
  norm it is √(d_out/d_in)·UVᵀ, every singular value the same;
  Newton–Schulz approximates it. No experiments of its own; nothing on the
  order of learning.
---
<!-- inactive-ok-file: ADR-108 — Proposed; cited in the readings of 2026-11-21 -->
<!-- inactive-ok-file: CLAIM-tmpmugkp CLAIM-tmpqwoxz QUESTION-tmpvcusw — Proposed, Deferred or new; filed in this contribution of 2026-11-21 or the ones it builds on -->

# NOTE-tmpuc566: Bernstein and Newhouse — Modular duality

## Contribution

A recursive duality map over the modular norm; closed-form maps for Linear, Embed and Conv2D; the observation that the linear map carries μP's spectral scaling and is Shampoo without accumulation; GPU-friendly approximations.

## Key results

1. **The linear map** (§3.3, Table 1): "the corresponding duality map is given by" √(d_out/d_in) × UVᵀ for G = UΣVᵀ.
2. **Links** (§4.1): the √(d_out/d_in) factor "recovers spectral update scaling (Yang et al., 2023) that leads to µP"; G ↦ UVᵀ "is equivalent to Shampoo without accumulation".
3. **Steepest descent** (Prop. 1): the exact steepest step scales dualize(g) by the dual norm of the gradient; the working update is weight − LR·dualize(grad) (eq. 2).
4. **Equal singular values** (§6.4): dualization projects gradients to scaled semi-orthogonal matrices "for which all singular values have the same magnitude".
5. **Newton–Schulz** (§5.3): X_{t+1} = (3/2)X_t − (1/2)X_tX_tᵀX_t converges to UVᵀ as t → ∞; no finite-step bound, tuned coefficients suggested.
6. **Stable rank** (§6.5): dualization "ramps up the stable rank of updates".
7. **Mass** (Definition 4(b)): used "to set the proportion of feature learning that this module contributes to any supermodule", citing the modular norm paper's proof.

## Assumptions and concepts

A squared norm models higher-order terms; RMS-scale inputs; well-normed modules; claims argued, not proved; no experiments. Concepts: duality map, dual norm, steepest descent on a normed space, induced operator norm, Newton–Schulz.

## Bearing on the record

- **CLAIM-tmpmugkp** (supports the mechanism; qualifies). The map is the polar factor, scaled by √(d_out/d_in) (1 for the claim's square layers), and every singular value of the update has the same magnitude. Qualifications: the claim's √(s/2)/lr uses the fixed-rate update of eq. 2, not Proposition 1's exact steepest step; practical updates use Newton–Schulz, exact only in the limit; non-square layers or unequal masses give unequal steps between layers. The paper says nothing about the order of learning, so the claim's result is neither confirmed nor contested.
- **QUESTION-tmpvcusw** (supports its premise): the text gives Newton–Schulz convergence only in the limit.
- **CLAIM-tmpqwoxz** (supports its sentence on dualization; mass second-hand).
- **Recheck**: THEORY-427 (Shampoo, held) is the natural neighbour; Carlson and colleagues' spectral descent and Flynn's duality-structure gradient descent are not held.

## Limitations

A position paper without experiments; no Newton–Schulz error bounds; no analysis of training dynamics, momentum or noise; the links to μP and Shampoo informal.
