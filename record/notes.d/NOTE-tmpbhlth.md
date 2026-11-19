---
status: Read
paper: LIT-tmpfodg5
title: 'Ito and colleagues — Compositional generalization through abstract representations in human and artificial neural networks'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    Read on 2026-11-19 by a delegated reader from arXiv 2209.07431v3 (PDF),
    compared with the NeurIPS 2022 version: the main text, appendices
    A.1–A.10 and the captions of supplementary figures 1–9; plotted values
    not read. Running notes on the branch claude/readers/task-composition
    (ADR-108). Quotations rechecked by the filer by script against the
    downloaded text.
date: '2026-11-19'
summary: >-
  Rule primitives pretrained first make a compositional rule task cheaper
  to learn and generalize zero-shot; abstraction measured by a parallelism
  score; order of pretraining decisive. Correlational for mechanism.
---
<!-- inactive-ok-file: LEAD-006 CLAIM-756 CLAIM-754 THEORY-2065 THEORY-2081 — Proposed or newly filed; entries this reading bears on -->

# NOTE-tmpbhlth: Ito and colleagues — Compositional generalization through abstract representations in human and artificial neural networks

## Key results

1. **Zero-shot.** "the Vanilla ANN performed near chance (acc=23.25%";
   "Combined pretraining had excellent zero-shot performance on the entire
   C-PRO task (acc=92.15%" (§3.4).
2. **Cost, pretraining counted.** A vanilla network trained to match
   "required up to 4.23x training samples to match the performance of the
   Combined model", and "the 4.23x more training samples included all
   possible samples (pretraining and C-PRO samples)" (§3.4). No spread is
   given.
3. **Equal criterion, different outcome.** "This was despite the fact that
   all ANNs had the same stopping criteria (i.e., 90% accuracy on the
   C-PRO training set)"; "pretrained ANNs became more sample efficient as
   the training set expanded, even after accounting for total number of
   (pretraining and C-PRO) samples" (§3.5–3.6).
4. **Mechanism, correlational.** Parallelism and generalization during
   pretraining "were highly correlated (r=0.88" (§3.4).
5. **Order.** With the stages reversed, "generalization performance was
   reduced to chance" (A.8).

## Bearing on the record

- **LEAD-006**, partial: primitives are g and three-rule contexts are
  compositions over them; (a) loosely, with pretraining counted; (b)
  weakly, regimes compared through an abstraction score with no
  memorizing arm, though all stop at the same criterion; no (c). A cheap
  testbed (CPU minutes per network) for adding the intervention, the
  reader's suggestion.
- **CLAIM-756**, weak corroboration: an earlier acquisition lowers later
  cost with its own cost counted.
- **CLAIM-754** and **CLAIM-675**, parallel: networks at the same criterion
  on trained contexts differ in what they can reach on novel ones.
- **QUESTION-039**, supports: the order of acquisition decides whether
  generalization appears at all.
- **THEORY-2065** (Skill-it), contrast: prerequisites lower a target's
  cost there too, but sequence did not matter there and decides everything
  here.
- **THEORY-794**, parallel on compositional generalization with factored
  representations; **THEORY-2081**, a caution: counted samples, not
  compute.

## Limitations

Seed count not stated; the 4.23 figure has no error bar; results in figures
only for the incremental curriculum; small MLPs with one-hot inputs.
