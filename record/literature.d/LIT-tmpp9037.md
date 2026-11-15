---
status: Active
status_note: >-
  read in full 2026-11-15 (NOTE-tmpqcif3) from arXiv v3 (ICLR 2025).
  Worth reading as the record's first account of why sequential model
  editing erodes general abilities, through the condition number of the
  edited matrix. The account rests on an upper bound and a correlation,
  not on an intervention.
title: 'Perturbation-Restrained Sequential Model Editing'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Registered and read on 2026-11-15 at the owner's request ("file those
    neighboring papers too"), as the other sequential editor MuEdit
    (dmarx/nucleation#499) groups itself with. Checked first: not held.
    Citation from the arXiv API and the PDF: Jun-Yu Ma, Hong Wang,
    Hao-Xiang Xu, Zhen-Hua Ling and Jia-Chen Gu, ICLR 2025; v1 submitted
    2024-05-27, which is `published:`. Read by a delegated reader. The
    filer string-matched every quotation used.
tags:
- representation-learning
- anthology-candidate
date: '2026-11-15'
published: '2024-05-27'
arxiv: '2405.16821'
first_author: 'Ma'
keywords:
- 'sequential model editing'
- 'condition number'
- 'matrix perturbation theory'
- 'general abilities'
- 'singular value restraint'
implementations:
- 'PRUNE (github.com/mjy1111/PRUNE)'
summary: >-
  Ma, Wang, Xu, Ling & Gu (2025), ICLR. Sequential single-fact edits by
  MEND, ROME and MEMIT erode an LLM's general abilities. The authors tie
  this to the condition number of the edited MLP matrix: perturbation
  bounds on how far a key must move to keep its value scale with it, and
  measured on LLaMA-2 7B it rises steeply with edits as the largest
  singular value grows. PRUNE shrinks, logarithmically, the singular
  values of the accumulated update that exceed the original matrix's
  largest, and keeps downstream and editing scores far higher than
  unrestrained editing. The link from condition number to damage is a
  bound and a correlation, not an intervention.
---

# LIT-tmpp9037: Perturbation-Restrained Sequential Model Editing

Jun-Yu Ma, Hong Wang, Hao-Xiang Xu, Zhen-Hua Ling and Jia-Chen Gu,
"Perturbation-Restrained Sequential Model Editing", ICLR 2025;
arXiv:2405.16821.

## Key takeaways

*From the reading, NOTE-tmpqcif3.*

- **The thesis.** "the factor affecting the general abilities in
  sequential model editing lies in the condition number of the edited
  matrix" (abstract). In §1 it is introduced as an assumption: "we
  assume that the bottleneck ... lies in the escalating value of the
  condition number."
- **The bound.** In the perturbation bound on a key's adjustment, "Each
  term on the right-hand side involves" κ̂, and κ̂ ≤ κ/γ (Thms 3.1–3.2).
- **The measurement.** "regardless of the editing methods employed, the
  condition number of the edited matrix exhibited a rapid increase as the
  number of edits increased" (§3.3). The largest singular value grows
  while the smallest is "basically unchanged".
- **The remedy.** PRUNE shrinks, logarithmically, singular values of the
  summed update above σmax(W), keeping their vectors. With it, MEMIT
  after 100 edits keeps downstream performance "close to that of the
  unedited model", where unrestrained it falls to nearly 0.

## Standing in the record

Filed on 2026-11-15 at the owner's request, beside AlphaEdit
(dmarx/nucleation#501) and MuEdit (dmarx/nucleation#499). It extends the
record's editing line (ROME, LIT-1536; MEMIT, LIT-1582 and THEORY-1031;
Hase et al., LIT-1578). It also adds the record's first account of why
editing accumulates damage. The method is practice and carries the
`anthology-candidate` flag.
