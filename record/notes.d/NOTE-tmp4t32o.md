---
status: Read
paper: LIT-tmprdmjg
title: 'Wang and colleagues — Data Shapley in One Training Run'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    Read on 2026-11-19 by a delegated reader from arXiv 2406.11011v3 (PDF,
    ICLR 2025): abstract, §§1–6, appendices A.2–A.3, B and E.1–E.5 in full;
    Figures 3 and 11 read as images; proofs and derivations skipped. Running
    notes on the branch claude/readers/scheduling-followups (the procedure
    proposed in pull request 537). Quotations rechecked by the filer by
    script against the downloaded text.
date: '2026-11-19'
summary: >-
  In-Run Data Shapley: per-step contribution to a validation loss, summed.
  General web text helps a math target only in the opening steps;
  specialised text dominates; per-point value decays with training. No
  order intervention.
---
<!-- inactive-ok-file: CLAIM-756 CLAIM-596 LEAD-tmpjdtrl — Proposed or newly filed; entries this reading bears on -->

# NOTE-tmp4t32o: Wang and colleagues — Data Shapley in One Training Run

## Contribution

A Shapley value for one training run, computed as cheaply as training
itself: by linearity, "individual data points’ Shapley values equals the
overall loss reduction" (§3); the first-order term is "equivalent to the
TracIN-Ideal score" (§4.1).

## Key results

1. **Domain value toward math, early training** (§5.3.2). General corpora
   "tend to have a large contribution in the beginning of training"; the
   composition "changes rapidly at the beginning of training and
   stabilizes". Read from Figure 3 by the reader: Pile-CC about a fifth of
   positive value at step 0, gone by about step 800, inside the 2000-step
   warmup; ArXiv dominant from then on.
2. **Value decays.** "the magnitude of data value scores converges" toward
   zero, aligning "with the diminishing returns property of neural network
   training" (App. E.4).
3. **Curation.** Removing negatively valued data reaches a target loss
   with "around 25% fewer training iterations" (§5.3.1): a removal, not an
   ordering.
4. **No order intervention** anywhere; the only prescriptive use is
   filtering.

## Assumptions

Small steps for a Taylor expansion; SGD formulas on an AdamW run; utility
defined step by step, against a validation set fixed in advance.

## Concepts

In-Run Data Shapley; local utility; TracIN-Ideal; ghost dot-product;
model-specific against algorithm-level attribution.

## Bearing on the record

- **CLAIM-756**, background with one point the record should keep: this
  is the own-direct-return accounting the claim says misses an
  acquisition's effect on later costs. An early step that only eases later
  learning gets zero or negative value here, so this attribution family
  cannot test the claim.
- **CLAIM-596**, analogy: per-step attribution, like a yield, cannot
  separate a contribution that speeds a later step from one that does not.
- **LEAD-tmpjdtrl**: not the owner's recalled result, and by construction
  it cannot be.
- **QUESTION-039**, weak parallel: which domains help a target shifts in
  the opening steps, and per-point value decays.
- **TERM-131**, background: a per-step counterfactual inside one
  trajectory, not the whole-run counterfactual the term asks for.
- **THEORY-tmpd6smn**, **THEORY-tmpd6l4a**, **THEORY-279**, **CASE-294**:
  parallels or background.

## Limitations

One run, one math target, the first 10k steps at batch 16, the web-crawl
effect inside warmup; negative-value domains dropped from the plot.
