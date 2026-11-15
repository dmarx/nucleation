---
status: Read
paper: LIT-tmpyijzd
title: 'Fang et al. — AlphaEdit'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Read on 2026-11-15 by a delegated reader from
    https://arxiv.org/pdf/2410.02355v4 ("arXiv:2410.02355v4 [cs.CL] 22 Apr
    2025", "Published as a conference paper at ICLR 2025"), text extracted
    with pdftotext. Read in full: §§1–7, the limitations, App. A.3–A.4,
    App. B (proofs) and App. C.2–C.9 with Tables 1–7. Skimmed: the
    references, App. A.2's metric definitions and the C.1 case studies.
    Not read: the figures beyond their captions, and App. D. The filer
    string-matched every quotation below and checked the baseline figures
    against Table 1.
date: '2026-11-15'
summary: >-
  Replaces MEMIT's preservation term with a projection of the update onto
  the left null space of the preserved keys K0, so that preserved outputs
  at the edited layer are unchanged. A one-line change to MEMIT's closed
  form. Strong sequential-editing results on three LLMs. The null space
  is numerical (eigenvalues of K0K0ᵀ at most 10⁻²), which makes the
  guarantee approximate; the residual is not measured. The account of why
  dropping the preservation term helps rests on t-SNE plots and
  distribution metrics, not on a theorem.
---

<!-- inactive-ok-file: THEORY-1039 THEORY-1011 — Proposed and Rejected; the key–value reading the paper assumes -->

# NOTE-tmpoaevu: Fang et al. — AlphaEdit

## Contribution

1. **A null-space-constrained editing objective and its closed form**
   (Eqs. 12–14). The method differs from MEMIT's closed form (Eq. 15) by
   a projector P.
2. **A cheap P.** It depends only on K0, so it is computed once and reused.
3. **A plug-in.** Adding P to MEMIT, PRUNE and RECT improves them.

## Key insight

Instead of trading error on preserved facts against fit to new ones,
remove the trade-off: confine the update to directions that cannot touch
the preserved keys. Then the objective only has to fit the new facts and
protect previously edited ones.

## Assumptions

- **The key–value reading of the MLP output projection** (Geva et al.),
  with edit layers chosen by causal tracing.
- **K0 stands for the model's preserved knowledge.** It is estimated from
  "100, 000 (s, r, o) triplets from Wikipedia" (§2.2), as in MEMIT.
- **Protecting keys at the edited layers protects general ability.** This
  is shown empirically on GLUE-type tasks, not derived.
- **WKp = Vp after earlier edits** (§3.3).

## Key results

- **§3.1–3.2, the guarantee.** "This implies that the projected ∆ will not
  disrupt the key-value associations of the preserved knowledge", and
  "This shows the projection matrix P ensures that the model edits occur
  without interference with the preserved knowledge" (Eq. 10).
- **§3.2, how P is built.** "we adopt the null space of the non-central
  covariance matrix K0K0ᵀ ... This matrix's null space is equal to that
  of K0". P = ÛÛᵀ, from the eigenvectors left after removing those of
  non-zero eigenvalues. Footnote 1: "Given that eigenvalues are rarely
  strictly zero in practical applications, in our experiments, we remove
  the eigenvectors corresponding to the eigenvalues above 10⁻²."
- **Table 1, LLaMA3-8B, 2,000 sequential edits in batches of 100**
  (CounterFact efficacy / generalization / specificity; ZsRE efficacy):

  | Method | CF Eff | CF Gen | CF Spe | ZsRE Eff |
  |---|---|---|---|---|
  | ROME | 64.40 | 61.42 | 49.44 | 2.01 |
  | MEMIT | 65.65 | 64.65 | 51.56 | 34.62 |
  | RECT | 66.05 | 63.62 | 61.41 | 86.05 |
  | AlphaEdit | 98.90 | 94.22 | 67.88 | 94.47 |
  | Pre-edit | 7.85 | 10.58 | 89.48 | — |

  On GPT-J, MEMIT holds up (CounterFact efficacy 98.55) and AlphaEdit
  reaches 99.75.
- **§4.2, Obs. 1**: "average improvement of 12.54% and 16.78%,
  respectively, over the best baseline". The LLaMA3 figures quoted,
  32.85 and 30.60, are differences from RECT (98.90 − 66.05;
  94.22 − 63.62). Fine-tuning has efficacy 83.33 and generalization 67.79
  in the same table, so "best baseline" is misstated.
- **§4.3, general ability**: "AlphaEdit maintains the original model
  performance across all metrics, even after editing 3,000 samples",
  while the baselines' "metrics are rapidly approaching zero".
- **§4.4, representations**: hidden states "remain consistent with the
  original distribution" (t-SNE; metrics in C.3).
- **§4.5, plug-in**: "an average improvement of 28.24% on editing
  capability and 42.65% on general capability".
- **C.8, the size of K0**: "When the dataset size is limited to just 10%
  ... Specificity drop by 11.76%" (LLaMA3 CounterFact, 67.88 to 56.12).
- **C.9, cost**: 223.24 s per 100 edits, against MEMIT's 222.51 s.

## Concepts

- **Left null space of K0** and the **projector P = ÛÛᵀ**.
- **Preserved, current and previously edited keys** (K0, K1, Kp), and the
  **residual R = V1 − WK1**.
- **Sequential editing**, and the **distribution shift of hidden
  representations**.

## Connections

AlphaEdit takes MEMIT's closed form, its layers, its λ and its K0
statistic ([LIT-1582](../literature.d/LIT-1582.md), [THEORY-1031](../theory.d/THEORY-1031.md); [NOTE-1197](NOTE-1197.md) records MEMIT's
C0 = λ·E[kkᵀ] from 100,000 samples). It follows Adam-NSCL (Wang et al.
2021) in using the null space of the uncentred covariance. MuEdit (Liang
et al. 2026, LIT-tmpy7s15) extends it to several domains.

## Bearing on the record

- **MuEdit's Conflict Index** (LIT-tmpy7s15, NOTE-tmps6dyd). That
  reading found the index degenerate as defined unless null spaces are
  numerical. Footnote 1 supplies the numerical criterion. MuEdit says it
  shares AlphaEdit's preprocessing, so its null spaces are presumably
  these thresholded ones.
  - The threshold is absolute, and the paper does not say whether K0K0ᵀ
    is a sum or a mean. So the null-space dimension, and with it the
    index, depend on a scale the papers do not report.
- **[THEORY-1031](../theory.d/THEORY-1031.md)** (MEMIT). AlphaEdit reports MEMIT collapsing under
  sequential editing on LLaMA3 but holding on GPT-J. [THEORY-1031](../theory.d/THEORY-1031.md)
  concerns one batch of 10,000 on GPT-J, a different regime, so there
  is no conflict. No note filed.
- **[THEORY-1039](../theory.d/THEORY-1039.md) / [THEORY-1011](../theory.d/THEORY-1011.md).** The key–value reading is assumed, not
  tested. AlphaEdit's success is edit success, which [THEORY-1039](../theory.d/THEORY-1039.md)'s
  promote_when says cannot settle storage. No note filed.
- **[LIT-968](../literature.d/LIT-968.md) / [NOTE-782](NOTE-782.md)** (Makelov et al.). That illusion concerns
  directions in the null space of W_out, in the output space. AlphaEdit's
  null space is in key space, W_out's input side, so the two do not
  touch.

## Limitations

- **The guarantee is approximate.** With 100,000 keys against a key
  dimension in the thousands, K0K0ᵀ is generically full rank, so the
  exact null space is {0}, and the method works through the 10⁻²
  threshold. The leakage ‖ΔPK0‖ is neither bounded nor measured. The
  reader derived ‖ΔPK0‖²_F ≤ 10⁻²‖ΔP‖²_F, an inference the filer agrees
  with, since P spans eigenvalues at most 10⁻².
- **The null-space dimension, the spectrum, and the scaling of K0K0ᵀ are
  not reported.**
- **Specificity stays far below the pre-edit level** and depends on the
  size of the K0 sample (C.8).
- **The "best baseline" figures are misstated** (above).
- **λ is listed in App. A.3 but has no place in the closed form.**
- **No theorem explains why dropping the preservation term prevents
  distribution shift.** The evidence is t-SNE and ad hoc metrics.
- **Up to 3,000 edits only, and no heterogeneous-domain test**, the
  failure MuEdit later reports.

## Open questions

- How large is the numerical null space at each edited layer, and how
  much do preserved outputs actually move?
