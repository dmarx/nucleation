---
status: Active
status_note: >-
  read 2026-10-26 (NOTE-tmp6m8zr) in full, from arXiv v4, the NeurIPS 2023
  version; worth reading for the workflow it names behind manual circuit
  discovery, for ACDC as that workflow's patching step made into an
  algorithm, and for the first scoring of circuit-finding methods against
  circuits found by hand (THEORY-tmp77xju). Read it knowing that the
  hand-found circuits are themselves partial, that the results move with
  the metric, the ablation and the order of visiting edges, that sparse
  runs miss negative components, that an OR gate keeps one input
  (THEORY-tmp1bwxc), and that §4.1 claims a tracr-reverse lead its own
  Table 2 does not show.
title: 'Towards Automated Circuit Discovery for Mechanistic Interpretability'
version: 2
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed, not read, at the owner's request of 2026-10-26 to register and
    read the core circuits literature the record lacked. Checked on
    2026-10-26 against the arXiv record: Arthur Conmy, Augustine N.
    Mavor-Parker, Aengus Lynch, Stefan Heimersheim and Adrià
    Garriga-Alonso, arXiv 2304.14997, v1 submitted 28 April 2023, which is
    `published:`; the comment reads "NeurIPS 2023 Spotlight". The summary
    follows the arXiv abstract.
- version: 2
  date: '2026-10-26'
  note: >-
    Read in full (NOTE-tmp6m8zr) from arXiv v4 of 28 October 2023, whose
    footer names NeurIPS 2023: §§1–6 and Appendices B–N, figures from
    captions. Status Deferred → Active. Two accounts filed, both Active:
    THEORY-tmp77xju and THEORY-tmp1bwxc. The summary is checked against
    the reading and given the AUCs and the failure cases.
tags:
- representation-learning
- causality
- anthology-candidate
date: '2026-10-26'
published: '2023-04-28'
arxiv: '2304.14997'
first_author: 'Conmy'
keywords:
- 'automated circuit discovery'
- 'ACDC'
- 'activation patching'
- 'mechanistic interpretability'
- 'circuits'
implementations: []
summary: >-
  Conmy, Mavor-Parker, Lynch, Heimersheim & Garriga-Alonso (2023),
  arXiv:2304.14997, NeurIPS 2023. ACDC automates the patching step of
  circuit discovery: from the output back, it removes each edge of a
  model's computational graph whose replacement by a corrupted activation
  raises the KL divergence from the full model by less than a threshold.
  Against circuits found by hand it ranks edges with AUCs of 0.85–0.98 on
  IOI, Greater-Than and Docstring, above two adapted pruning methods, and
  on Greater-Than keeps 68 of about 32,000 edges, all in the reported
  circuit. It is sensitive to metric, ablation and visiting order, misses
  negative components at sparse thresholds, and recovers compiled tracr
  circuits only with zero activations.
---
<!-- inactive-ok-file: THEORY-tmpoirdq THEORY-802 — Proposed; a neighbouring account built on this family of methods and the account on several correct explanations, cited as open -->

# LIT-tmpoku9b: Towards Automated Circuit Discovery for Mechanistic Interpretability

Conmy, A., Mavor-Parker, A. N., Lynch, A., Heimersheim, S. &
Garriga-Alonso, A. (2023). Towards automated circuit discovery for
mechanistic interpretability. *Advances in Neural Information Processing
Systems 36 (NeurIPS 2023)*. arXiv:2304.14997.

Read in full on 2026-10-26 (NOTE-tmp6m8zr). Two accounts were drawn from
it: THEORY-tmp77xju and THEORY-tmp1bwxc.

## Why this is here

The owner asked on 2026-10-26 how the record stood on neural circuit
theory; the answer found it held almost none of the core circuits
literature, and the owner said "go ahead and register and read those".
ACDC is the reference algorithm for finding a circuit rather than
testing one, and the ancestor of the edge-attribution methods behind
LIT-tmpf4hwb (THEORY-tmpoirdq) and benchmarked by MIB (LIT-tmprlq7z),
which the record held without their source. It is the search counterpart
of causal scrubbing (LIT-tmpqtkua), runs on the induction setting of
LIT-tmpe7b5o and QUESTION-tmpivbso, and its OR-gate case bears on
THEORY-802's several correct explanations.
