---
number: 1098
status: Active
formerly:
- THEORY-tmp247k7
title: 'On Karnkowska and colleagues'' genome analysis, the oxymonad Monocercomonoides exilis lost its mitochondrion only after the organelle''s essential functions had been removed one by one, Fe–S cluster assembly to a bacterial-type SUF system shared with mitochondriate relatives and then the glycine cleavage system by loss, and the loss left the rest of the cell canonical, with no compensating changes found'
version: 2
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed Proposed from NOTE-1243, the reading in full of Karnkowska
    et al. (2019). The analysis is homology searches on a draft genome,
    the order of the preadaptations is inferred from their distribution
    among relatives, and "no compensating changes" is an absence bounded
    by annotation. The authors do not exclude a highly reduced mitosome
    below FIB-SEM resolution. Hence Proposed.
- version: 2
  date: '2026-10-30'
  note: >-
    Promoted by the twenty-second status review, at the status review's
    ruling (the owner delegated these rulings; ADR-065). The title
    reports what Karnkowska and colleagues' genome analysis finds and
    infers; NOTE-1243 read the paper in full, and nothing in the record
    contradicts the report. What the condition asked beyond the title,
    that the authors be right, moves to THEORY-tmpvjwpy, Proposed, which
    extends this entry and keeps the condition word for word (ADR-065
    §3). The answers edge on QUESTION-277 is moved to bears_on (ADR-060): the
    reading is evidence on the question, not an answer to it as posed.
    The old promote_when: "Evidence that dates the steps in the
    Monocercomonoides line: the SUF replacement, the loss of the glycine
    cleavage system and SHMT, and the loss of the organelle, placed in
    order on a tree of Preaxostyla with several more amitochondriate and
    MRO-bearing genomes, and a functional account of what the MRO of the
    closest relatives still does that M. exilis does without. Proteomic
    or tagged-marker evidence that M. exilis has no mitosome below
    microscopic resolution would close the other gap. A second
    annotation of the same draft genome cannot settle it. It is refuted
    if a reduced mitosome is found, or if genes that compensate for the
    organelle's absence turn up once the hypothetical proteins are
    characterized."
tags:
- endosymbiosis
- natural-sciences
date: '2026-10-27'
source:
- LIT-1574
bears_on:
- QUESTION-277
summary: >-
  Karnkowska et al. (2019), [LIT-1574](../literature.d/LIT-1574.md), read in [NOTE-1243](../notes.d/NOTE-1243.md). The SUF
  replacement of the mitochondrial Fe–S pathway is shared by all examined
  Preaxostyla, including relatives that keep a mitochondrion-related
  organelle, and those relatives' organelle still houses the glycine
  cleavage system that M. exilis lacks. So the organelle lost its jobs in
  at least two steps before it was lost. Apart from the mitochondrion,
  peroxisomes and mitophagy, the cell's systems are those of an ordinary
  eukaryote. The order is inferred, not dated, and absence is limited by
  annotation.
---
<!-- inactive-ok-file: THEORY-tmpvjwpy — Proposed; filed beside this reading by the twenty-second status review: the wider thesis it reports -->
<!-- inactive-ok-file: QUESTION-277 CASE-168 THEORY-1100 — Open or Proposed; the question, case and accounts set beside this, nothing here rests on them -->

# THEORY-1098: On Karnkowska and colleagues' genome analysis, the oxymonad Monocercomonoides exilis lost its mitochondrion only after the organelle's essential functions had been removed one by one, Fe–S cluster assembly to a bacterial-type SUF system shared with mitochondriate relatives and then the glycine cleavage system by loss, and the loss left the rest of the cell canonical, with no compensating changes found

## Source

Karnkowska et al. (2019), *Molecular Biology and Evolution* 36(10):
2292–2312, [LIT-1574](../literature.d/LIT-1574.md), read in full in [NOTE-1243](../notes.d/NOTE-1243.md) from the PubMed
Central copy. "Is the Absence of Mitochondrion Reflected in
Modifications of Any Cellular System?", the FIB-SEM section, and the
conclusions.

## What was actually shown

- **No organelle seen.** FIB-SEM of two cells, fixed two ways, found no
  mitochondria or MROs. The authors "acknowledge that the resolution of
  the microscopy could still allow for undetected highly reduced
  mitosomes".
- **Two preadaptations, by distribution among relatives.**
  - "The ISC pathway, otherwise considered to be an essential
    house-keeping pathway in eukaryotes, was functionally replaced in
    all examined Preaxostyla by the SUF pathway". A full set of
    essential Fe–S proteins (70 candidates) is served by the cytosolic
    SUF and CIA systems.
  - *M. exilis* lacks the glycine cleavage system and SHMT, "which are
    both present in its close relative Paratrimastix pyriformis, where
    they localize into the MRO". Their loss "removed another essential
    function from the MRO ..., preadapting it for loss of the organelle",
    and "took place after the split from the P. pyriformis lineage".
- **One concomitant loss.** No mitophagy or pexophagy orthologs: "an
  example of a system likely lost together with mitochondria".
  Peroxisomes are also gone but are lost in many anaerobes.
- **No postadaptation.** Energy metabolism resembles that of
  mitosome-bearing anaerobes, with "no indication that they were
  affected by the complete loss". None of the functionally annotated
  genes unique to *M. exilis* is "clearly related to the loss of
  mitochondrial function". The cytoskeleton, kinetochore, membrane
  trafficking, autophagy, oxidative stress response, calcium flux and
  metabolism are not "significantly altered relative to eukaryotes with
  mitochondria".

What could have failed: the genome could have been reduced or unusual
in ways tied to the loss, such as new cytosolic versions of
mitochondrial pathways or a collapse of the systems that interact with
mitochondria. The SUF replacement could have been unique to *M.
exilis*, making it the single trigger.

## What this does not say

- **Not that SUF alone made the organelle dispensable.** It is shared
  with relatives that kept MROs. The 2016 framing, a single
  preadaptation, is widened here to two.
- **Not when the steps happened.** The order comes from which relatives
  have what. No step is dated.
- **Not what the last MRO did.** The paper names no function remaining
  after GCS and SHMT were gone.
- **Not that the cell has no mitosome.** Below FIB-SEM resolution, the
  question is open.
- **Not that the lost organelle was replaced.** The functions were
  replaced or dropped; nothing took the organelle's place as a
  compartment.
- **Not that complex cells existed before the mitochondrion.** That is
  the paper's closing suggestion, from a secondary loss.

## Connections

- **[QUESTION-277](../questions.d/QUESTION-277.md).** The negative control, made more exact. The
  partner's functions were moved to a third-party gene or dropped until
  no dependence on the partner remained, and then the partner was lost.
  It is the host-compensation route run to dissolution, and it says
  that integration as deep as a mitochondrion's can be undone one
  function at a time. The reading in the question's terms is mine.
- **[CASE-168](../cases.d/CASE-168.md).** The case's "one indispensable job" should read "two
  essential functions, removed in turn".
- **[THEORY-1100](THEORY-1100.md).** Organelles are made by moving functions onto
  host-encoded proteins. This is the same accounting from the other end:
  the organelle persists while some function still needs it.
- **[THEORY-1049](THEORY-1049.md).** McCutcheon et al. find the host supplying what a
  shrinking symbiont lacks. Here the host supplies everything the
  organelle once did, and the organelle goes.

## Note of 2026-10-30: promoted, and the wider thesis filed beside it

The twenty-second status review promoted this reading under ADR-065: it reports what Karnkowska and colleagues' genome analysis finds and infers, and NOTE-1243 read the paper in full. Whether Monocercomonoides lost its mitochondrion in this way is THEORY-tmpvjwpy's question, Proposed, which keeps this entry's old promote_when.
