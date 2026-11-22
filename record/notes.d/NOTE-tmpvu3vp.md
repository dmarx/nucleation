---
status: Read
paper: LIT-2989
title: "Bui and colleagues, Learning Along the Arrow of Time: Hyperbolic Geometry for Backward-Compatible Representation Learning, read for how entailment cones between model generations constrain updated embeddings"
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Read on 2026-11-22 by a delegated reader from the arXiv PDF
    (https://arxiv.org/pdf/2506.05826, v1 of 6 Jun 2025, the only
    version, with the ICML 2025 / PMLR 267 header; 14 pp.), via
    pdftotext: pp. 1–9 (§§1–7, the limitations included) and Appendix A
    (the ablations) in full; the references only skimmed. Metadata from
    the arXiv API. The cone's radial consequence, which the paper does
    not state, was checked numerically by the filer (CLAIM-tmpxcy5s).
    Every quotation the filing leans on rechecked by the filer by script
    against the text. No email address sent to any service.
date: '2026-11-22'
summary: >-
  Backward-compatible retrieval: a new encoder must be able to query a
  gallery embedded by an old one without re-embedding it. HBCT lifts both
  models' embeddings into the Lorentz model, reads uncertainty from the
  radius, and trains the new model with a classification loss plus an
  entailment-cone hinge that penalises a new embedding for leaving the
  cone apexed at the same item's old embedding and an uncertainty-weighted
  contrastive loss. On CIFAR100 and TinyImageNet it improves cross-model
  compatibility over Euclidean baselines at little cost to the new model,
  most of all when the architecture changes. The clipping radius has to
  be raised at each update, and the authors list unbounded norm growth as
  the method's limitation.
---
<!-- inactive-ok-file: THEORY-tmpe9367 CLAIM-tmpxcy5s CLAIM-839 CLAIM-816 CLAIM-800 THEORY-188 ARG-153 ARG-tmpf206e ARG-tmpotmon — Proposed or new; the reading of this work, the claim and argument filed with it and the entries it bears on -->

# NOTE-tmpvu3vp: Bui and colleagues, Learning Along the Arrow of Time: Hyperbolic Geometry for Backward-Compatible Representation Learning, read for how entailment cones between model generations constrain updated embeddings

## Contribution

§1: "To the best of our knowledge, this is the first attempt to leverage
embedding geometry for maintaining consistency in updating models." Old
to new is made a partial order: "we employ the entailment loss (Ganea et
al., 2018) to enforce a partial-order constraint between the old and new
models. This constraint requires the new embeddings to remain within the
entailment cone of their older counterparts". The reading is
[THEORY-tmpe9367](../theory.d/THEORY-tmpe9367.md).

## Key results

1. **Time as confidence** (abstract): "we treat time as a natural axis
   for capturing a model's confidence and evolution." Eq. 10:
   Uncertainty(h) = 1 − ‖h_space‖/h_time = 1 − (1/√K) tanh(√K‖z‖), a
   decreasing function of distance from the origin, "the same formulation
   as the Pointcaré uncertainty measure" of Franco et al. 2023 and Atigh
   et al. 2022.
2. **Unseen classes sit nearer the origin** (§4.1, Fig. 2): a ResNet18
   trained on 50 CIFAR100 classes embeds the other 50 with images that
   "exhibit higher uncertainty and lower norms".
3. **The cone** (§4.2). It "constrains the region where new embeddings
   can 'descend' from old embeddings"; "the cone represents the set of
   permissible embedding adjustments as the model evolves." Eq. 11:
   aper(h_o) = sin⁻¹(2ε/(√K‖h_o,space‖)), ε "a small constant (e.g. 0.1)";
   L_entail = max(0, ext(h_o, h_n) − aper(h_o)), with
   ext = π − ∠(O, h_o, h_n). "as ho becomes more uncertain (lower norm),
   its cone 'widens', granting greater freedom for the evolutionary
   expansion".
4. **The constraint is soft** (Eq. 13): L = L_base + λ(L_entail +
   L_contrast), λ = 0.3. §4.3: "the entailment cone restricts only the
   spatial coordinate changes of the embedding, without preserving
   pairwise distance relationships".
5. **Compatibility** (§5.2): "HBCT improves CMC@1 compatibility of the
   new model by 21.4% compared to the strongest Euclidean baseline", and
   "yields a 44.8% increase in mAP compatibility", averages of relative
   gains over the eight cells of Table 1.
6. **The cone term matters most across architectures** (§5.4, Table 1):
   without it, "a significant drop in terms of backward compatibility in
   scenarios where we update the architecture". CIFAR100 CMC@1 P_com with
   and without it: new architecture 0.937 against −0.178; both changed
   0.324 against −0.487; extended classes 0.495 against 0.435; extended
   data 0.956 against 0.847.
7. **Five sequential updates** (§5.3, Fig. 5): HBCT "demonstrates superior
   compatibility maintenance with prior models across multiple updates",
   over every pair of earlier and later models.
8. **Uncertainty falls** (§5.4, Fig. 6): "As the model improves, the
   uncertainty in the gallery embeddings decreases."
9. **The radius must grow** (§4.4; App. A, Table 4; §7). The new model's
   clipping threshold is raised, ζ_n = ζ_o + 0.2, "to account for the
   evolution in the embedding space"; keeping ζ_n = 1.0 harms cross-model
   compatibility. §7: "we gradually increase the clipping norm threshold.
   This may lead to instability as norms grow (e.g., ≥ 10.). A potential
   solution is to backfill and rescale the time dimension after a set
   number of updates".

## Assumptions

- Supervised classification training; the old model frozen, the new one
  trained afresh (§3, §7); D_new ⊇ D_old.
- The old and new embeddings of the same input are paired; each item's
  cone is apexed at its own old embedding. No hierarchy of concepts.
- A hybrid encoder with the exponential map at the origin; dimension 128;
  K = 1 in the main results.
- The norm is taken as uncertainty, after Atigh et al. 2022 and Khrulkov
  et al. 2020, and not calibrated against error here.

## Concepts

Backward-compatible training, backfilling, the Lorentz model and its time
and space coordinates, hyperbolic MLR, norm as uncertainty, the
entailment cone (Ganea's, as reworked for the Lorentz model by Desai et
al. 2023), half-aperture and exterior angle, RINCE, P_com and P_up, the
compatibility matrix.

## Connections

The cone is Ganea et al.'s ([LIT-866](../literature.d/LIT-866.md)), in the Lorentz form of Desai et
al. 2023 (not held). Eq. 11 is [THEORY-189](../theory.d/THEORY-189.md)'s widest transitive family: for
curvature −K, √K‖h_space‖ = sinh(√K·d(O, h)), so Eq. 11 reads
sinh(√K·d) sin ψ = 2ε, at K = 1 [THEORY-189](../theory.d/THEORY-189.md)'s sinh(d) sin ψ = 2K with ε for
Ganea's K. Model stitching (Bansal et al., [LIT-850](../literature.d/LIT-850.md)) is cited as related
work. The "Atigh et al. 2022" cited for norm as uncertainty is the same
first author's hyperbolic image segmentation (CVPR), not [LIT-2993](../literature.d/LIT-2993.md).
Not held, cited: Desai et al. 2023, Khrulkov et al. 2020, Shen et al. 2020
(BCT), Atigh et al. 2022.

## Bearing on the record

- **[CLAIM-839](../claims.d/CLAIM-839.md)** (supports in part; four qualifications). A33's fallback,
  temporal cone consistency "as ... a soft regularizer", is what HBCT
  implements, and it works, most where the architecture changes. But the
  constraint is a soft hinge weighted 0.3 and the paper never reports how
  many new embeddings lie inside their cones; the cones are per item, not
  cones of concepts; they link two separately trained models, the old one
  frozen, not checkpoints of one run; and the order is imposed by design,
  not observed in learning. Per item the generations form a chain, not a
  branching order. [ARG-tmpf206e](../arguments.d/ARG-tmpf206e.md).
- **The gap: cones force norm growth** ([CLAIM-tmpxcy5s](../claims.d/CLAIM-tmpxcy5s.md), the assistant's).
  Every point of a cone of this family lies farther from the origin than
  its apex, so a satisfied constraint raises each item's norm and lowers
  its uncertainty, whether or not the update is correct. Results 8 and 9
  are what that predicts; the paper treats them as empirical tuning and a
  limitation. It bears on [CLAIM-839](../claims.d/CLAIM-839.md)'s rule that narrowing counts only
  while correct ([ARG-tmpotmon](../arguments.d/ARG-tmpotmon.md)).
- **[THEORY-189](../theory.d/THEORY-189.md)** (parallel; an application). The same family in Lorentz
  form, and its radial monotonicity is the source of the gap above.
- **[THEORY-421](../theory.d/THEORY-421.md)** (contrast). Bui et al. read the norm as confidence, with
  unseen classes at lower norms, and never calibrate it against error;
  [THEORY-421](../theory.d/THEORY-421.md) holds that even trained for hierarchy, radius is only a
  partial reading of level. Under the cone constraint the norm also moves
  by construction, so as a confidence signal it is confounded with the
  number of updates.
- **[CLAIM-816](../claims.d/CLAIM-816.md)** (parallel). Bui et al. rescale ‖z‖ by √d and clip at ζ
  (§4.4), a practical answer to the same narrow-norm problem; their radius
  means uncertainty, not depth, and each update spends radial range.
- **[ARG-153](../arguments.d/ARG-153.md)** (leaves it open). Nothing on dimension; the aperture's
  dependence on radius (Eq. 11) agrees with its point that cost is set by
  radius as well as angle.
- **[CLAIM-800](../claims.d/CLAIM-800.md)** (supports by example; another filer's file, reported to
  the lead). Occupancy of old cones is what L_entail pushes up, by
  construction, and the paper rightly judges by an independent measure.
- **[LIT-866](../literature.d/LIT-866.md)** (background; applied). **[LIT-850](../literature.d/LIT-850.md)** (background; cited as
  related work on aligning representations). **[LIT-849](../literature.d/LIT-849.md)** (contrast):
  relative representations reach cross-model compatibility without an
  alignment loss; not cited.
- **[THEORY-188](../theory.d/THEORY-188.md)** (no bearing). Hyperbolic random graphs are a different
  use of the geometry.

## Limitations

- Small benchmarks (CIFAR100, TinyImageNet), supervised only.
- One run per configuration; no seeds or error bars.
- Baselines' hyperparameters were searched (ten runs each) and HBCT's
  fixed.
- The old models differ between the Euclidean and hyperbolic arms, so
  only P_com and P_up compare across them.
- Cone satisfaction is never measured, and neither is uncertainty
  calibration.
- Norm growth is unbounded across updates (§7).
- The 21.4% and 44.8% are averages of relative gains, sensitive to small
  P_com denominators.
