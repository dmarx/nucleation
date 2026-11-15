---
status: Skimmed
paper: 'LIT-tmp40uoi'
title: 'Fel, Kowal et al. — Shaping and monitoring models through their internal representations'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Skimmed on 2026-11-15 by a delegated reader. The paper,
    arXiv:2611.07071v1, https://arxiv.org/pdf/2611.07071v1 (82 pp.), text
    by pdftotext, was skimmed: the "This work" contributions list
    (pp. 2–3), the §4 passage "Behavioral control and monitorability"
    (p. 19), the opening of §6 "Monitoring under Circumvention" with
    Proposition 1 (pp. 24–25) and the matching appendix sentence. Not
    read: §§1–3 and 5 in detail, the proofs (Appendix J) and most figures.
    The summary page, https://www.goodfire.ai/research/mechanistic-shaping
    (HTML, text extracted by script), was read in full; the hierarchy and
    the vision results below come from it. Skimmed, since the paper was
    skimmed and only the page read. The filer rechecked every quotation
    below against a fresh text extraction of the PDF and the page's text;
    all were found.
date: '2026-11-15'
summary: >-
  Training against a probed concept can degrade the original probe
  (0.98 → 0.57 in the worst reward-hacking variant) while a refitted probe
  recovers it (0.97–0.98); in every experiment the concept stayed readable
  by some rung of a five-level hierarchy of probes, and a linear toy
  theory has the concept regrow along the readout's core directions.
---
<!-- inactive-ok-file: THEORY-292 — Proposed; a held reading cited as a neighbour, nothing rests on it -->

# NOTE-tmp88irq: Fel, Kowal et al. — Shaping and monitoring models through their internal representations

## Contribution

"Mechanistic shaping": a training penalty on a concept direction found by
interpretability tools. Reliance shaping penalizes the output's
dependence on the concept; expression shaping penalizes its presence.
Applied to confounded vision (Waterbirds, chest drains in CheXpert), DPO
sycophancy (OLMo-3, 7B to 32B), Countdown reward hacking (Qwen3.5-9B) and
harmfulness. The paper then asks whether training against a probe breaks
the probe, and answers with a hierarchy of monitors and a toy theory.

## Key insight

Whether a shaped concept is still monitorable depends on the class of
monitors allowed. The paper ranks them: L1 reuse the probe, L2 refit a
linear probe, L3 fit a nonlinear one, L4 probe another layer, L5 use a
separate model on inputs and outputs. Shaping usually moves the concept
rather than removing it.

## Assumptions

- Concept directions are estimated (difference of means, probes, SAE
  features).
- The theory uses linear or residual toy models under a fixed projection.
- The experiments go up to 32B parameters.

## Key results

- **Page**: "In all of our experiments, the concept being trained against
  remained monitorable, either with the original probe or a retrained
  one. A few cases required new probes with greater expressivity or at
  different layers." The page's summary: "Either the original probe kept
  working (L1) or a new probe recovered the signal (L2, L3, and L4)"; L5
  was not needed.
- **Reward hacking** (paper §4, p. 19): "When gradients flow through the
  probe score, its original balanced accuracy falls from 0.98 to 0.57 by
  update 150, whereas the other variants retain 0.87–0.90. Refitting a
  probe recovers 0.97–0.98 in every checkpoint". The page classes it L2.
- **Sycophancy** (§6, p. 25): the original direction's AUROC goes from
  0.981 to 0.931 while "a refitted linear probe stays perfect".
- **Vision** (page): "repeatedly removing the linear form of the concept
  at an intermediate layer (with frequent refitting of its direction)
  left only a nonlinear form of the concept at that layer (L3). Two layers
  later, however, the concept was linearly readable again". With some
  reliance penalties at the last layer, the page adds, the concept was
  partly erased at that layer, which the theory did not predict, and
  stayed recoverable at earlier layers.
- **Proposition 1** (§6): under a fixed projection P "the ablated
  component receives no gradient"; a new encoding of the unwanted feature
  "starts to grow right away" along "the direction the head already uses
  to read the core features". Refits made early in this rebuild remove
  core directions, and "accuracy falls close to chance".
- **Contributions list**: "projecting out and LEACE (Belrose et al., 2023)
  can leave information in the covariance that a quadratic reader
  recovers (Section 2.1)." §2.1 was not read.

## Concepts

- **Reliance vs expression shaping**: "don't rely on this" against "don't
  do this".
- **Circumvention**: the paper's preferred term over "obfuscation"
  (footnote 1, as the reader reports).
- **Regrowth**: re-encoding of an ablated concept along new directions.
- **Hierarchy of monitorability**: L1–L5 above.

## Bearing on the record

- **TERM-064**: the hierarchy is a ladder of observer classes, and
  "remained monitorable" means legible to some rung. The page's remark
  that "probes only need to be as powerful as the remainder of the model"
  is an upper bound on the observer class needed, close to the term's
  bound by what the source makes possible.
- **THEORY-281** and **THEORY-1827**: projection erases linearly; the
  concept left in the covariance for a quadratic reader is exactly what
  LEACE's linear guarantee does not cover, and is far from the
  independence THEORY-281 assumes.
- **QUESTION-010**: the best fit in the batch for the chain form. Erasure
  at one layer under continued training has later layers rebuild the
  concept, and a refit early in the rebuild destroys core features
  instead. A learning dynamic, not a fixed reconstruction chain; evidence,
  not an answer.
- **THEORY-846**: re-readability at later layers is usable information
  created by computation.
- **THEORY-292** (co-occurring attributes give aligned directions): bears
  on the entanglement of desired and undesired directions (cosine up to
  about 0.45 in some vision experiments, per the page).

## Connections

Proposition 1's over-damage, refits removing core features, is the
mechanism of Kumar, Tan & Sharma's collapse of a clean classifier under
INLP, reached by an independent route.

## Limitations

Skimmed: the proofs were not checked, and the hierarchy and the vision
results come from the page. A lab's own report of its own method; its
encouraging verdict on monitorability covers the settings it ran.
