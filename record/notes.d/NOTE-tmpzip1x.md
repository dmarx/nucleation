---
status: Read
paper: LIT-tmp4b6aq
title: 'Large, Liu, Huh, Bahng, Isola and Bernstein — The modular norm'
version: 1
history:
- version: 1
  date: '2026-11-21'
  note: >-
    Read on 2026-11-21 by a delegated reader from arXiv 2405.14813v1 (23
    May 2024): the abstract, §§1–5 and Appendices A.2–A.4, B.1, B.2
    (start), B.4, B.5, D.2, D.4, D.6 and E; B.6–B.7, C and the D.5 sweeps
    skipped. Running notes on the branch claude/readers/modular-norm
    (ADR-108). Quotations the filing leans on rechecked by the filer by
    script against the downloaded text.
date: '2026-11-21'
summary: >-
  A norm on a network's weights built recursively from per-module norms,
  masses and sensitivities; mass bounds each module's share of the output
  change (Proposition 3), and zero mass freezes a module. Width is handled
  by each atom's norm, depth by fixing mass; a 1/L residual construction
  has depth-independent sharpness.
---
<!-- inactive-ok-file: ADR-108 THEORY-1640 — Proposed; cited in the readings of 2026-11-21 -->
<!-- inactive-ok-file: CLAIM-tmp2yj4t CLAIM-tmpqwoxz — Proposed, Deferred or new; filed in this contribution of 2026-11-21 or the ones it builds on -->

# NOTE-tmpzip1x: Large, Liu, Huh, Bahng, Isola and Bernstein — The modular norm

## Contribution

A compositional, non-asymptotic metrization of networks; mass as a per-module allocation of learning; a residual scaling with depth-independent sharpness; the loss gradient Lipschitz in the modular norm.

## Key results

1. **Mass** (Definition 1): a module's mass "will turn out to set the proportion of feature learning that this module contributes to any supermodule".
2. **Apportioned learning** (Proposition 3): each module's contribution to the linearized output change is bounded by its share of the total mass times the norm of the update.
3. **Regulated rates** (§2.3): "Normalization in the modular norm essentially forces individual layers to learn at specified, regulated rates", with masses giving "precise control over the relative learning speed in different submodules".
4. **Freezing** (B.1): "Setting an atom's mass to zero has the effect of freezing its weights under normed optimization."
5. **Depth** (D.6): without fixing mass the input and output layers' share shrinks with depth; "for good learning rate transfer with depth we must fix a mass."
6. **Residual construction** (Proposition 4): ((L−1)/L·Identity + 1/L·M)^L has sharpness independent of depth; the GPT block uses 1/2L, against nanoGPT's 1/√L (D.4).
7. **Not asymptotic** (§1.1): "our framework eschews any kind of limiting or probabilistic analysis".

## Assumptions and concepts

Well-normed atoms, not maintained during training; sharpness bounds for atoms; unit-sensitivity blocks; Proposition 3 an upper bound. Concepts: module, mass, sensitivity, well-normed, sharpness, tare.

## Bearing on the record

- **CLAIM-tmpqwoxz** (supports; defeater (b) not met; qualified). Mass is a free per-module parameter apportioning update size, and zero mass freezes a module, the claim's limiting case of a slow module as constraint. Qualification written into version 2: masses set O(1) ratios and depth shares; width exponents are set by each atom's norm. The paper aims at balance and says nothing about levels or the lazy regime.
- **CLAIM-tmp2yj4t** (qualifies): the paper uses a 1/L branch multiplier at initialization as well, justified by sharpness and unit sensitivity, not by drift; on the claim's table random contributions at initialization would then vanish as √L/L, which the paper neither discusses nor measures.
- **Recheck**: THEORY-082 (steepest descent defined only relative to a metric) is the held ground for reading the modular norm as a choice of metric; THEORY-1640 (LoRA: frozen weights plus a low-rank update) is a practical instance of mass-zero freezing.

## Limitations

Proposition 3 is an inequality; well-normedness not maintained in training; mass must be tuned; evidence from learning-rate sweeps; the asymptotic regimes not analysed.
