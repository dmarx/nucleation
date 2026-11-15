---
status: Active
status_note: >-
  read 2026-11-15 ([NOTE-tmpoaevu](../notes.d/NOTE-tmpoaevu.md)) from arXiv v4 (ICLR 2025), §§1–7 and
  Appendices B–C in full. Worth reading as the null-space form of
  locate-then-edit editing that MuEdit extends. It also settles how the
  "null space" is computed in practice: eigenvectors of K0K0ᵀ with
  eigenvalues at most 10⁻², a numerical, not exact, null space.
title: 'AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Registered and read on 2026-11-15 at the owner's request ("file those
    neighboring papers too"), as the method MuEdit (dmarx/nucleation#499)
    extends. Checked first: not held. Citation from the arXiv API and the
    PDF: Junfeng Fang, Houcheng Jiang, Kun Wang, Yunshan Ma, Jie Shi, Xiang
    Wang, Xiangnan He and Tat-Seng Chua, ICLR 2025 (Oral); v1 submitted
    2024-10-03, which is `published:`. Read by a delegated reader. The
    filer string-matched every quotation used and checked the "best
    baseline" figures against Table 1.
tags:
- representation-learning
- anthology-candidate
date: '2026-11-15'
published: '2024-10-03'
arxiv: '2410.02355'
first_author: 'Fang'
keywords:
- 'model editing'
- 'knowledge editing'
- 'null-space projection'
- 'sequential editing'
- 'locate-then-edit'
implementations: []
summary: >-
  Fang, Jiang, Wang, Ma, Shi, Wang, He & Chua (2025), ICLR. MEMIT-style
  editing trades error on new facts against error on preserved ones, and
  over sequential edits that trade-off drifts. AlphaEdit drops the
  preservation term and instead projects the weight update onto the null
  space of the preserved keys, so that (W + ΔP)K0 = WK0. The null space is
  taken from the eigenvectors of K0K0ᵀ (100,000 keys) whose eigenvalues
  are at most 10⁻², so the guarantee is approximate. Over 2,000 sequential
  edits on LLaMA3-8B, CounterFact efficacy is 98.90, against 65.65 for
  MEMIT and 64.40 for ROME, with general ability kept. Specificity still
  falls well below the pre-edit level.
---

# LIT-tmpyijzd: AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models

Junfeng Fang, Houcheng Jiang, Kun Wang, Yunshan Ma, Jie Shi, Xiang Wang,
Xiangnan He and Tat-Seng Chua, "AlphaEdit: Null-Space Constrained Knowledge
Editing for Language Models", ICLR 2025; arXiv:2410.02355.

## Key takeaways

*From the reading, [NOTE-tmpoaevu](../notes.d/NOTE-tmpoaevu.md).*

- **The guarantee.** "(W + ∆P)K0 = W K0 = V0. This shows the projection
  matrix P ensures that the model edits occur without interference with
  the preserved knowledge" (§3.2, Eq. 10).
- **How P is built.** P is taken from the SVD of K0K0ᵀ, whose "null space
  is equal to that of K0". In practice, "Given that eigenvalues are
  rarely strictly zero in practical applications", eigenvectors "above
  10⁻²" are removed (footnote 1). The null space is thus numerical, and
  the guarantee holds only approximately.
- **The results.** Over 2,000 sequential edits in batches of 100, on
  LLaMA3-8B: CounterFact efficacy 98.90 and generalization 94.22, against
  MEMIT's 65.65 and 64.65 (Table 1). General ability is kept up to 3,000
  edits. Specificity falls from 89.48 before editing to 67.88.
- **A misstated comparison.** The "average improvement ... over the best
  baseline" is computed against RECT, not against fine-tuning, the best
  baseline on efficacy.

## Standing in the record

Filed on 2026-11-15 at the owner's request, as the method MuEdit extends.
It continues the editing line the record holds: ROME ([LIT-1536](LIT-1536.md)), MEMIT
([LIT-1582](LIT-1582.md), [THEORY-1031](../theory.d/THEORY-1031.md)) and Hase et al. ([LIT-1578](LIT-1578.md), [THEORY-1024](../theory.d/THEORY-1024.md)).

Its footnote on the eigenvalue threshold answers the question MuEdit's
reading left open: MuEdit's "null spaces", and so its Conflict Index,
rest on a numerical rank criterion, presumably this one, which MuEdit
does not restate.

The method is machine-learning practice and carries the
`anthology-candidate` flag. Its account of preservation by projection is
filed here.
