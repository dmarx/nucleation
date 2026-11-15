---
status: Read
paper: LIT-tmpp9037
title: 'Ma et al. — PRUNE'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Read in full on 2026-11-15 by a delegated reader from
    https://arxiv.org/pdf/2405.16821v3 (27 pp., "arXiv:2405.16821v3
    [cs.CL] 3 Mar 2025", ICLR 2025), text extracted with pdftotext. Read:
    §§1–6 and Appendices A (all proofs), B and C; Appendix D skimmed. Most
    figures are images, and their values were not recovered; numbers come
    from Tables 1, 2, 4 and 6 and the prose. The filer string-matched
    every quotation below.
date: '2026-11-15'
summary: >-
  Ties the decline of general abilities under sequential single-fact
  editing to the condition number of the edited MLP matrix, via standard
  least-squares perturbation bounds, and shows the condition number rising
  with edits on LLaMA-2. PRUNE shrinks the large singular values of the
  accumulated update once, post hoc, and preserves downstream and editing
  performance across MEND, ROME and MEMIT on three LLMs. The account is an
  upper bound plus a correlation; the bound concerns a proxy (how far a
  key must move), and its side conditions are never checked.
---

<!-- inactive-ok-file: THEORY-1039 THEORY-1030 — Proposed; the key–value reading the paper assumes -->

# NOTE-tmpqcif3: Ma et al. — PRUNE

## Contribution

1. **An account of damage**, from matrix perturbation theory, that ties
   sequential-editing damage to the condition number of the edited
   matrix.
2. **A plug-in remedy**: post-hoc spectral restraint of the accumulated
   edit update, usable with any editor that modifies parameters.
3. **Experiments**: 3 editors × 3 LLMs × 4 downstream tasks, and a study
   of conceptual edits.

## Key insight

Each edit is small, but sequential edits pile up in a few shared
directions ("editing overfitting"), so the accumulated update's top
singular value grows. That inflates the edited matrix's largest singular
value while its smallest stays put. The matrix becomes ill-conditioned,
and every stored association becomes more sensitive to the next change.

## Assumptions

- **One layer analysed.** Only one layer's MLP output matrix W is
  analysed as edited. W is full rank, and each edit is small against
  ‖W‖.
- **A linear key–value memory** with Wk_i = v_i (Geva et al.; Meng et
  al.).
- **Side conditions of the theorems.** The perturbation is "acute",
  preserving rank, and γ = 1 − κ‖ΔE11‖/‖W‖ > 0. Neither is checked for
  real edits, and γ > 0 may fail exactly when κ is large.
- **Single-fact sequential edits only**; batch editing is excluded.

## Key results

- **Thm 3.1** (§3.2): the relative change of the key that keeps a value,
  ‖Δk‖/‖k‖, is bounded by terms each involving κ̂: "Each term on the
  right-hand side involves" it.
- **Thm 3.2**: κ̂ ≤ κ/γ, with κ = ‖W‖‖W†‖. Hence "the larger κ is, the
  greater the upper bound on the perturbation of the vector k."
- **§3.3, Fig. 2**: "regardless of the editing methods employed, the
  condition number of the edited matrix exhibited a rapid increase as the
  number of edits increased".
- **§4, Table 1** (LLaMA-2, CounterFact): the largest singular value of
  the summed update at 200 edits is 57.61 for ROME, 935 for MEMIT and
  191.04 for MEND. The maximum singular value of the edited matrix "is
  constantly increasing, while the minimum singular value is basically
  unchanged".
- **§4, the restraint**: singular values of the summed update above
  max σ(W) become log_α σ̂ − log_α max σ + max σ, so they are "not to
  obviously exceed the maximum singular value of W". The vectors are
  kept, and α is tuned per setting (1.2, 1.5 or e). "the PRUNE proposed
  here is only used once in Section 5, but can actually be used multiple
  times".
- **§5.4, downstream** (LLaMA-2, zsRE): "when MEMIT was coupled with
  PRUNE and subjected to 100 edits, its downstream tasks performance
  remained close to that of the unedited model", where unrestrained it
  falls to nearly 0. With MEND, PRUNE helps only to about 20 edits: "it
  does have an upper limit determined by the unrestrained editing
  method." And "with 300 edits, MEMIT's performance on GPT2-XL remained
  largely unchanged, whereas it dwindled to nearly 0 on LLaMA-2 and
  LLaMA-3."
- **§5.6, Table 2** (ConceptEdit, ROME on LLaMA-2, 200 edits, ROME →
  ROME + PRUNE): Reasoning 0 → 72.9, NLI 0 → 46.15, Locality 5.31 →
  46.65. "conceptual knowledge is more abstract and more difficult to
  edit than factual knowledge".
- **C.5, Fig. 16**: "a dramatic increase in the condition number is often
  accompanied by a rapid decline in general abilities". This is the only
  direct evidence linking κ to the decline, and it is correlational.

## Concepts

- **Condition number** κ = σmax/σmin of the edited matrix.
- **Acute perturbation; the generalized inverse; key adjustment Δk.**
- **Editing overfitting**: edit updates aligning, so the top singular
  value of their sum grows.
- **Restraint on the upper bound**: logarithmic shrinkage of large
  singular values of the accumulated update.

## Connections

PRUNE edits on top of MEND, ROME and MEMIT ([LIT-1536](../literature.d/LIT-1536.md), [LIT-1582](../literature.d/LIT-1582.md)),
assuming their key–value reading ([LIT-1576](../literature.d/LIT-1576.md), [THEORY-1030](../theory.d/THEORY-1030.md); [THEORY-1039](../theory.d/THEORY-1039.md)).
AlphaEdit (LIT-tmpyijzd) adds its projector to PRUNE as a
plug-in and reports gains. MuEdit (LIT-tmpy7s15) groups it with
AlphaEdit as a sequential editor and finds it weaker across domains.

## Bearing on the record

- **[THEORY-1031](../theory.d/THEORY-1031.md)** (MEMIT, one batch of 10,000 on GPT-J). PRUNE runs
  MEMIT one fact at a time and finds it collapsing downstream by 100
  edits on LLaMA-2. A different regime, so no conflict, but any account
  of MEMIT's scaling should say that sequential MEMIT is fragile. No note
  filed.
- **[THEORY-1039](../theory.d/THEORY-1039.md) / [THEORY-1030](../theory.d/THEORY-1030.md)** (the key–value reading). It is assumed,
  not tested. Damage tracking the update's spectrum would occur whether
  or not the layer stores facts. No note filed.
- **[NOTE-1197](NOTE-1197.md)** (the MEMIT reading). Its scaling note, sequential ROME
  "holds to about n = 10 and degrades from n = 32", is the record's
  earlier evidence of sequential degradation, and agrees with this one.

## Limitations

- **A bound and a correlation, not a cause.** That the bound's constant
  rises does not show the actual perturbation rises, nor that κ drives
  the decline. No intervention changes κ while holding the update's size
  fixed.
- **The bound's quantity is a proxy.** Keeping fact i needs ‖ΔW·k_i‖
  small, with the key fixed by the forward pass. The paper bounds
  instead how far the least-squares key must move to keep v, and the
  link is not argued.
- **Side conditions unchecked**: γ > 0 and acuteness.
- **Analysis and remedy do not line up.** The theory is about
  sensitivity to the next edit, while PRUNE, applied once, shrinks the
  accumulated update after all edits. It also does nothing to σmin, so
  it does not provably bound κ, and its lowering κ is shown for MEMIT
  only.
- **α is tuned per setting,** with no held-out procedure described.
- **Downstream results are mostly in figures.** The reader could not
  recover them as numbers.
- **The overclaim noted above.** The abstract's "theoretically analyzes"
  outruns §1's "assume".

## Open questions

- Would an intervention that changes only the condition number (shrinking
  σmax, or raising σmin) at a fixed update norm move general ability as
  the account predicts?
