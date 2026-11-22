---
status: Skimmed
paper: LIT-tmpahs2x
title: 'Calvet, Reulet & Rouat — The connectivity degree controls the difficulty of RBN reservoir design'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    From the arXiv v1 PDF of 2312.08522, fetched 2026-11-22 without
    obstacle, text extracted with pdftotext. Read: the abstract, the
    introduction's citations of Bertschinger and Natschläger (2004), and
    the Discussion (pp. 25–26). Skipped: the methods, the results and their
    figures, the appendices. Read as a supplement to the reading of
    LIT-2991 (ADR-114), by a reader subagent; filed by a second one, which
    rechecked the quotes used here against the extracted text. No email
    address sent.
date: '2026-11-22'
summary: >-
  In random Boolean network reservoirs, the best-performing region
  coincides with the critical region when the excitatory–inhibitory
  balance is positive and lies inside the disordered region when it is
  negative; the paper presents this as refining the 2004 edge-of-chaos
  result.
---
<!-- inactive-ok-file: LIT-2991 CLAIM-809 ARG-tmps7n0g — Unavailable, Proposed or new; the work it qualifies, the stand-in read for that work, and the claim and argument it bears on -->

# NOTE-tmpt3dxa: Calvet, Reulet & Rouat — The connectivity degree controls the difficulty of RBN reservoir design

## Contribution

A study of random Boolean network reservoirs (N up to 10 000) that varies
the connectivity degree K, the excitatory–inhibitory balance b and N, and
measures memory and prediction against the critical region and attractor
statistics. Only its Discussion was read.

## Key results (Discussion, pp. 25–26)

- "Our study reveals that the edge of chaos, or the critical region, does
  not consistently align with the peak performance region (Gallicchio,
  2020), and this alignment is contingent upon the sign of
  excitatory-inhibitory balance b. For b > 0, as previously observed
  (Calvet u. a., 2023), the critical region coincides with the highest
  performance. However, for b < 0, the region of optimal performance does
  not coincide with the critical region when the connectivity degree K is
  optimally selected."
- "Refining initial literature (Bertschinger und Natschläger, 2004; ...),
  the highest-performing region is characterized by a preponderance of
  irregular attractors within the disordered region."
- With K = 4, "the optimal balance is near, but not at, perfect symmetry"
  (b → 0 gives zero performance).

## Assumptions

Random Boolean networks as reservoirs with a trained readout; the
critical region located by attractor statistics; tasks of memory and
prediction. Details not read.

## Concepts

Reservoir computing; random Boolean network; excitatory–inhibitory
balance; connectivity degree; critical region; attractor diversity.

## Bearing on the record

- **CLAIM-809**: supports the clause that the best distance from the
  transition depends on the system, here on the sign of the balance:
  peak performance at the critical region for b > 0, inside the
  disordered region for b < 0 (ARG-tmps7n0g). It is a later qualification
  of Bertschinger and Natschläger's "only near the critical boundary"
  (LIT-2991, read through LIT-tmpdsowv and NOTE-tmpi5t3r), not a
  restatement of it.

## Limitations

Only the Discussion was read; the measures, task definitions, how the
critical region is located and the sizes of the effects are not known
here. A preprint; no journal is given on arXiv.
