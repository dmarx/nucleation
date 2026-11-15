---
status: Proposed
promote_when: >-
  Two results. (1) An independent replication, at fixed update norm, that
  across merges of models fine-tuned from one start the variance of
  low-frequency amplitude in the 2D spectra of the tasks' weight updates
  goes with lower merged accuracy, and that high-pass filtering each
  update before adding beats task arithmetic and TIES. (2) A test that the
  effect belongs to the computation, not to the weight layout: apply one
  random function-preserving permutation of hidden units to the
  pretrained model and every fine-tuned model, and repeat the
  measurement and the merge. If the correlation and the advantage
  survive, the account holds as stated. If they vanish, the effect
  depends on the arbitrary index order and the title's "low frequencies"
  name nothing about the updates themselves.
title: 'Zheng and Wang: for models fine-tuned from one pretrained start, the 2D Fourier spectra, taken over the row and column order of each weight matrix, of different tasks'' weight updates differ most in amplitude at low frequencies, that difference goes with lower merged accuracy, and removing the low frequencies from each update before adding them improves data-free merging over task arithmetic and TIES'
version: 1
tags:
- loss-landscapes
- mathematics
- anthology-candidate
date: '2026-11-15'
source:
- LIT-tmppnktu
summary: >-
  Zheng & Wang (2025), LIT-tmppnktu, read in NOTE-tmpkleq4. Amplitude
  variance across tasks is largest at low index-grid frequencies and
  correlates negatively with normalized merged accuracy; FR-Merging
  (high-pass then magnitude-weighted sum) reaches 78.1 on ViT-B/32 with 8
  tasks against 70.1 for task arithmetic and 73.6 for TIES. The
  frequencies are over the arbitrary order of rows and columns and change
  under a function-preserving permutation of hidden units, which the
  paper does not test. The wording is the reader's; adopting it is the
  owner's call.
---
<!-- inactive-ok-file: LIT-tmppnktu NOTE-tmpkleq4 THEORY-107 THEORY-tmp6ikb6 THEORY-tmpqv3ve — new tmp codes, or Proposed; source, reading and neighbouring accounts, named and not leaned on -->

# THEORY-tmp3lla6: Zheng and Wang: for models fine-tuned from one pretrained start, the 2D Fourier spectra, taken over the row and column order of each weight matrix, of different tasks' weight updates differ most in amplitude at low frequencies, that difference goes with lower merged accuracy, and removing the low frequencies from each update before adding them improves data-free merging over task arithmetic and TIES

## Source

Zheng & Wang (2025), LIT-tmppnktu, read in NOTE-tmpkleq4: §§1–7,
Appendix D.1–D.5.

## The result

- **Spectral mismatch** (§4, Fig. 2a): task vectors of one ViT-B/32
  attention head, Fourier transformed over their index grid, differ most
  in amplitude near the centre of the spectrum.
- **Correlation** (Fig. 2b, App. D.1): across groups of merged ViT-B/32
  models, and Flan-T5 on GLUE, higher amplitude variance goes with lower
  normalized merged accuracy.
- **Merge** (Table 2): high-pass filtering each task vector and adding
  them with magnitude-based coefficients gives 78.1 on ViT-B/32 with 8
  tasks, against 70.1 for task arithmetic and 73.6 for TIES. Low-pass
  filtering degrades badly (§6.6).

## What it does not show

- **That the frequencies are about the computation.** The transform runs
  over the arbitrary order of a weight matrix's rows and columns.
  Permuting hidden units leaves the function unchanged and changes the
  spectrum, so the quantity is not invariant to permutations. Within one
  start all models share the order, so the effect is well defined there,
  but it is not shown to mean anything beyond the layout. The
  promote_when's permutation test would settle it. The singular-value
  accounts (THEORY-tmp6ikb6, THEORY-tmpqv3ve) do not have this problem.
- **That amplitude mismatch causes the loss.** The measure is defined by
  the authors and supported by a correlation; FR-Merging lowers it by
  filtering it.
- **That filtering, not rescaling, makes the gain.** FR-Merging also
  reweights the tasks by magnitude. Like TIES (THEORY-107), the method
  bundles steps the evidence does not separate.
- **Anything for FREE-Merging's headline.** Its 89.7 needs routed experts
  stored per task, which is not a static merge and not Fourier.
- **Physics.** Nothing here is wave mathematics in a physical sense.
