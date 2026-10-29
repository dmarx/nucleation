---
status: Skimmed
paper: LIT-tmpbihhf
title: 'Sarkar, Mukherjee and Sato — Relational composition as parallel transport'
version: 1
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Skimmed from the arXiv PDF 2610.34945v1 (31 pp.), extracted with
    `pdftotext -layout`. Read: the abstract, §1, §2 (2.1–2.3, Theorems 1
    and 2), §5.3, §7, Appendix A.1 and the opening of A.2, and Appendix
    B.4 with Table 5. Not read: §§3–4 (the width law, covers, ceilings
    and certificates), §§5.1–5.2, and the rest of Appendices A and B.
    Pages are the preprint's.
date: '2026-10-29'
summary: >-
  The companion paper's premise, stated by its authors: per-entity frame
  freedom is "a chosen inductive bias, not a consequence of fresh names".
  Under it, scores go through ⟨xᵢ, Tᵢⱼxⱼ⟩ and transports must be supplied.
  Its parsed-benchmark controls show the premise's orthogonality helping
  on StepGame and costing 64.6 points on CLUTRR.
---
<!-- inactive-ok-file: CLAIM-098 — Proposed; the claim this reading bears on, cited as open -->

# NOTE-tmp4j67k: Sarkar, Mukherjee and Sato — Relational composition as parallel transport

## Contribution

It takes per-entity frame freedom as a symmetry of the representation and
derives the node-level form of attention under it: transport, then
compare. It shows that a transport cannot be computed from the two
endpoints' own vectors, and it ties the width and readout a mechanism needs
to the representation theory of the relational algebra it must compose.
The skimmed parts cover the first and the parsed-benchmark controls.

## Key insight

"A dot product is meaningful only when the two vectors are written in the
same coordinate system" (p. 2). A fresh entity has no coordinates of its
own, so its relation to another must arrive as an operator that carries
one frame into the other. Standard attention is the case where every
entity "already speaks the same one" (p. 2).

## Assumptions

- **The premise is chosen.** "This is an inductive bias, not a claim that
  fresh names logically imply a physical symmetry" (p. 2); "This is a
  modeling premise, not a derived fact ... the paper adopts it as an
  inductive bias and derives its consequences" (App. A.1, p. 12); "The
  premise itself is a chosen inductive bias, not a consequence of fresh
  names" (App. A.2, p. 13).
- **O(d) frames** with transports Tᵢⱼ ↦ gᵢTᵢⱼgⱼ⁻¹ (eq. 1). "For
  nonorthogonal operators, further invariants and covariants are needed"
  (p. 3).
- **Parsed relations** on both benchmarks: "every model receives the same
  extracted relations", and the results "concern composition given
  relations, not text understanding" (p. 8).

## Key results

- **Theorem 1 (p. 3).** A continuous score is invariant iff
  sᵢⱼ = ϕ(‖xᵢ‖, ‖xⱼ‖, ⟨xᵢ, Tᵢⱼxⱼ⟩); a message is equivariant iff
  mᵢⱼ = αxᵢ + βTᵢⱼxⱼ with invariant α, β.
- **Theorem 2 (p. 3).** A covariant map computed only from endpoint
  channels Xᵢ, Xⱼ is XᵢC(XᵢᵀXᵢ, XⱼᵀXⱼ, e)Xⱼᵀ, of rank at most
  min(rank Xᵢ, rank Xⱼ): "one vector per endpoint supplies at most a
  rank-one carrier, never an orthogonal transport when d ≥ 2".
- **Flat sector (p. 4).** An inverse-consistent orthogonal connection has
  every cycle product I iff Tᵢⱼ = FᵢFⱼ⁻¹, and a standard head's W_QᵀW_K
  and W_OW_V are tensors on one common space. "This identifies the
  geometry; it does not restrict what a deep transformer can compute."
- **Table 5 (p. 28)**, mean out-of-distribution accuracy on parsed tasks:
  StepGame (trained k ≤ 5, tested 6–10): transformer 0.481, additive
  transport 0.753; within the probe readouts general linear 0.73 and
  rotations 0.82. CLUTRR (trained k ∈ {2, 3}, tested 4–10): transformer
  0.436, unconstrained matrix scan 0.848, orthogonal scan 0.202 while
  fitting its training data at about 0.98. "Hence the orthogonality
  intervention changes the OOD mean by 64.6 percentage points" (p. 29).
- **The authors' limit on that result (p. 29).** A nonidentity idempotent
  has no invertible faithful representation, but "The experiment does not
  establish that CLUTRR's typed composition rules form a particular
  monoid ... It therefore does not identify idempotence as the sole cause
  of the measured effect."
- **Anchored identification (p. 9).** "With exact matched anchors B = QA an
  orthogonal transport is identified only on the anchored subspace, since
  BA⁺ = QAA⁺ = QP_col(A)."

## Concepts

- **reset** — the paper's word for a non-invertible transport (p. 3).
- **flat sector** — connections with every cycle product the identity,
  gauge-equivalent to all Tᵢⱼ = I.
- **carrier** — the data a transport is computed from; endpoint carriers
  are rank-bounded (Theorem 2).

## Connections

It is ref. [1] of LIT-tmpr8qf7, which supplies the edge-level half and
re-describes this paper's premise as "the task's". The invariant theory is
Weyl's and Villar et al.'s (App. A.1). The algebraic motivation for the
CLUTRR result is Krohn–Rhodes.

## Bearing on the record

- **CLAIM-098 and CLAIM-035.** The CLUTRR control is a measured case of the
  claims' thesis that composition of relations need not be a group action.
  Imposing invertibility on a relational task with resets loses most of
  what unconstrained composition achieves. The authors decline to name
  the cause.
- **LIT-tmpr8qf7.** Its "the symmetry is the task's" (p. 2) contradicts this
  paper's statement of the same premise, and this paper's own data show
  the premise's orthogonality is task-relative.
- **QUESTION-130.** The anchored-identification remark is QUESTION-130's
  condition in another form: a transport estimated from matched anchors is
  fixed only where the anchors reach, so apparent holonomy in unanchored
  directions is the estimator's.

## Limitations

The benchmarks use parsed relations, and "their algebraic reading is
tentative" (p. 9). Only the parts listed in the history were read, so the
width law, the covers and the certificates are not assessed here.

## Open questions

What relational algebra does CLUTRR's kinship composition actually have,
and does a transport family with exactly that algebra recover the gap?
