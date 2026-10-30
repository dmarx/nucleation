---
number: 1103
status: Active
formerly:
- THEORY-tmpehubi
title: 'On Shigenobu and colleagues'' genome of Buchnera sp. APS, the aphid symbiont keeps the genes for the amino acids its host cannot make and has lost almost all of those its host can, uses host-made glutamate and aspartate as precursors, and lacks phospholipid synthesis and nearly all its own transcriptional regulators, so that its metabolism interlocks with the host''s and it presumably lives only inside the bacteriocyte, a state reached by gene loss from an E. coli-like ancestor'
version: 2
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed Proposed from NOTE-1236, the reading in full of Shigenobu,
    Watanabe, Hattori, Sakaki & Ishikawa (2000) from the publisher's free
    PDF. Every functional statement is inferred from gene content in one
    strain. Host supply of precursors is supported by earlier physiology
    the paper cites; host supply of lipids is a hypothesis. Hence
    Proposed.
- version: 2
  date: '2026-10-30'
  note: >-
    Promoted by the twenty-second status review, at the status review's
    ruling (the owner delegated these rulings; ADR-065). The title
    reports what Shigenobu and colleagues' genome shows and what they
    infer from it; NOTE-1236 read the paper in full, and nothing in the
    record contradicts the report. What the condition asked beyond the
    title, that the authors be right, moves to THEORY-1219,
    Proposed, which extends this entry and keeps the condition word for
    word (ADR-065 §3). The answers edge on QUESTION-277 is moved to bears_on
    (ADR-060): the reading is evidence on the question, not an answer to
    it as posed. The old promote_when: "Direct measurement in the
    aphid–Buchnera system, not more gene inventories: labelling or
    metabolite-flux evidence that host-supplied glutamate or aspartate
    is converted by Buchnera into essential amino acids that return to
    the host; lipid analysis showing that Buchnera's membranes are built
    from host-made phospholipid; and evidence that the pattern of
    retained and lost pathways recurs across Buchnera of other aphid
    lineages. It is refuted if Buchnera proves to make the non-essential
    amino acids or its own phospholipids by unannotated or divergent
    genes, or if its essential-amino-acid output does not depend on host
    precursors."
tags:
- endosymbiosis
- natural-sciences
date: '2026-10-27'
source:
- LIT-1596
bears_on:
- QUESTION-277
summary: >-
  Shigenobu et al. (2000), [LIT-1596](../literature.d/LIT-1596.md), read in [NOTE-1236](../notes.d/NOTE-1236.md). The first
  complete genome of an obligate insect endosymbiont: 640,681 bp, a
  subset of E. coli's. What is shown is gene content. The interlocking
  of host and symbiont metabolism is inferred from it and from earlier
  physiology. That Buchnera cannot live outside the bacteriocyte, and
  that the host supplies its membrane lipids, are the authors'
  inferences. The paper names no mechanism of loss beyond a homeostatic
  niche: it says nothing of drift.
---
<!-- inactive-ok-file: THEORY-1219 — Proposed; filed beside this reading by the twenty-second status review: the wider thesis it reports -->
<!-- inactive-ok-file: QUESTION-277 CASE-173 LIT-1573 — Open, Proposed or Unfetched; the question, case, account and unread work this is set beside, nothing here rests on them -->
# THEORY-1103: On Shigenobu and colleagues' genome of Buchnera sp. APS, the aphid symbiont keeps the genes for the amino acids its host cannot make and has lost almost all of those its host can, uses host-made glutamate and aspartate as precursors, and lacks phospholipid synthesis and nearly all its own transcriptional regulators, so that its metabolism interlocks with the host's and it presumably lives only inside the bacteriocyte, a state reached by gene loss from an E. coli-like ancestor

## Source

Shigenobu, Watanabe, Hattori, Sakaki & Ishikawa (2000), *Nature* 407:
81–86, [LIT-1596](../literature.d/LIT-1596.md), read in full in [NOTE-1236](../notes.d/NOTE-1236.md) from the publisher's free
PDF. The whole letter, Table 1, the captions of Figures 1–3, and the
Methods.

## What was actually shown

- **The sequence.** One chromosome of 640,681 bp with 583 ORFs, and two
  plasmids carrying leucine and tryptophan genes. 500 ORFs have an
  assigned function and only 4 are unique to *Buchnera*. Gene order in
  *E. coli* operons is conserved.
- **Amino acids (Fig. 2).** Genes for the amino acids essential to aphids
  are present, with a few gaps (ilvE, dapC). Genes for the non-essential
  ones "are almost completely missing", cysteine excepted. Glutamate and
  aspartate, which *Buchnera* cannot make, are precursors of essential
  amino acids.
- **What else is missing.** Phospholipid synthesis except cls; LPS
  synthesis except lpcA and kdtB; every transcriptional regulator except
  dnaA; recA, uvrABC, lexA, umuCD; restriction and methylation genes.
  The genes the lost regulators once controlled are kept.
- **Loss, not a small ancestor.** The gene set is "a small subset" of the
  inferred ancestor shared with *E. coli* and *H. influenzae*, with no
  lineage-specific duplications.

What could have failed: *Buchnera* could have kept a broad,
*E. coli*-like biosynthetic repertoire, or lost the essential-amino-acid
pathways as parasites lose theirs. The gene set could have been a small
ancestor's, with duplications of its own. None of these is what the
sequence shows.

## What this does not say

- **Not that neither partner can reproduce alone.** That is the paper's
  opening sentence, cited to earlier work. The genome speaks to the
  symbiont's side only.
- **Not that the host supplies membrane lipids.** The authors offer two
  routes, import of host phospholipid or host enzymes "like mitochondria
  do", and test neither.
- **Not that the host controls the symbiont's genes.** The symbiont has
  lost its own regulators. Nothing here shows the host regulating it.
- **Not how the genome shrank.** The paper names no population-genetic
  mechanism. Drift and Muller's ratchet are [LIT-1573](../literature.d/LIT-1573.md)'s account, not this
  paper's.
- **Not gene transfer to the host.** The host genome is not studied, so
  transfer in either direction is neither found nor excluded.

## Connections

- **[QUESTION-277](../questions.d/QUESTION-277.md).** The clearest worked instance in the record of the
  distribution of essential functions (G) between two genomes, interlocked
  by shared precursors. It shows the symbiont's dependence (D) from gene
  content and asserts the host's. It shows loss of the symbiont's
  self-regulation, which is not yet host control (C).
- **[THEORY-1049](THEORY-1049.md).** At 641 kb, *Buchnera* APS has already lost
  phospholipid synthesis and almost all of LPS synthesis, while keeping
  fatty-acid, murein and sec genes. So envelope erosion begins above the
  400 kb threshold, which then marks complete loss. The comparison is
  mine.
- **[CASE-173](../cases.d/CASE-173.md)** is the case this account documents.

## Note of 2026-10-30: promoted, and the wider thesis filed beside it

The twenty-second status review promoted this reading under [ADR-065](../decisions.d/ADR-065.md): it reports what Shigenobu and colleagues' genome shows and what they infer from it, and [NOTE-1236](../notes.d/NOTE-1236.md) read the paper in full. Whether Buchnera's metabolism interlocks with its host's as inferred is [THEORY-1219](THEORY-1219.md)'s question, Proposed, which keeps this entry's old promote_when.
