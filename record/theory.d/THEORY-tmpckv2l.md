---
status: Proposed
promote_when: >-
  A test of whether rate-normalized stem length measures time of
  acquisition, made independently of this pipeline. That could be a
  method with an explicit rate model, applied to a dense sample of Asgard
  archaea and bacteria, that recovers alphaproteobacterial families as
  more recently diverged from their sisters than other bacterial
  families; or an independent dating of when the non-alphaproteobacterial
  genes entered the eukaryotic lineage. Re-running stem-length
  comparisons with more families or other LECA definitions cannot settle
  it, since they share the assumption at issue. It is refuted if the
  alphaproteobacterial-against-other-bacteria difference disappears with
  denser sampling of close relatives, or if the non-alpha bacterial genes
  are dated after the mitochondrion's entry.
title: 'On Pittis and Gabaldón''s stem-length analysis of the LECA proteome, families of alphaproteobacterial origin and mitochondrial location sit closer to their prokaryotic relatives, after correction for each family''s rate, than families of other bacterial origin, which sit closer than archaeal families, and the authors read this as late acquisition of the mitochondrion by a host whose proteome was already chimaeric; the reading of length as time assumes proportional rates before and after LECA, the alphaproteobacterial difference from other bacteria is marginal, and stem length also shortens when a closer relative is sampled'
version: 1
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed Proposed from NOTE-tmpjgenc, the reading in full of Pittis &
    Gabaldón (2016) from the PubMed Central author manuscript. The
    ordering is a statistical result on 1,064 families. Its reading as an
    order of acquisition rests on an assumed relation between rates
    before and after LECA, and the comparison on which the chimaeric host
    turns has P = 0.044. Hence Proposed.
tags:
- endosymbiosis
- natural-sciences
date: '2026-10-27'
source:
- LIT-1595
answers:
- QUESTION-277
summary: >-
  Pittis & Gabaldón (2016), [LIT-1595](../literature.d/LIT-1595.md), read in [NOTE-tmpjgenc](../notes.d/NOTE-tmpjgenc.md). Of 1,078
  LECA families, bacterial ones have shorter normalized stems than
  archaeal ones (P = 1.38e-25), and alphaproteobacterial ones shorter
  than other bacterial ones (P = 0.044). Origin tracks location:
  alphaproteobacterial with the mitochondrion, other bacterial with
  endomembranes, archaeal with the nucleus. A plastid control runs the
  right way. The sharp edges are that stem length measures distance to
  the closest sampled relative, so sampling can move it, and that the
  chimaeric host could have come from partners or from transfer, which
  the paper cannot tell apart.
---
<!-- inactive-ok-file: QUESTION-277 NOTE-tmpjgenc THEORY-tmp5wptr — Open, Deferred, Proposed or unmerged; the question this answers in part, the reading it comes from and the dating study set beside it, nothing here rests on them -->

# THEORY-tmpckv2l: On Pittis and Gabaldón's stem-length analysis of the LECA proteome, families of alphaproteobacterial origin and mitochondrial location sit closer to their prokaryotic relatives, after correction for each family's rate, than families of other bacterial origin, which sit closer than archaeal families, and the authors read this as late acquisition of the mitochondrion by a host whose proteome was already chimaeric; the reading of length as time assumes proportional rates before and after LECA, the alphaproteobacterial difference from other bacteria is marginal, and stem length also shortens when a closer relative is sampled

## Source

Pittis & Gabaldón (2016), *Nature* 531: 101–104, [LIT-1595](../literature.d/LIT-1595.md), read in full
in [NOTE-tmpjgenc](../notes.d/NOTE-tmpjgenc.md) from the PubMed Central author manuscript (PMC4780264),
not the version of record. The main text, the Methods ("Measurement of
the phylogenetic distance ...: stem lengths" above all), Table 1, and
the captions of Figures 1–3 and Extended Data Figures 1–8.

## What was actually shown

- **The measure.** For each LECA family, the branch to its closest
  prokaryotic sister group, divided by the family's median branch length
  inside eukaryotes. The correction removes rate differences only "Under
  the assumption that rates pre- and post-LECA are correlated".
- **The order.** Bacterial families are shorter than archaeal
  (P = 1.38e-25). Alphaproteobacterial families are the shortest
  bacterial ones, with Verrucomicrobia/Chlamydiales, and shorter than
  other bacterial families at P = 4.4e-2. A mixture model puts
  alphaproteobacterial, mitochondrial and energy-production families in
  the shortest component, and archaeal, nuclear and ribosomal ones in
  the longest two.
- **Origin, not function.** Families matched for function, dN/dS,
  connectivity or expression still differ by origin. Raw stem lengths
  give the same order.
- **Controls.** Cyanobacterial families in plants have shorter stems than
  alphaproteobacterial ones, as the later plastid predicts. Halving
  alphaproteobacterial sampling, removing Rickettsiales and stricter LECA
  definitions leave the alphaproteobacterial result. Transfer scenarios
  are argued not to produce the non-alpha signal.
- **Location.** Alphaproteobacterial families associate with the
  mitochondrion (P ≤ 1e-6). Other bacterial families associate with
  endomembranes. Archaeal families associate with the nucleus.

What could have failed: bacterial families could have had similar stems
whatever their source, as "a simple fusion model" predicts. They did
not, though the alphaproteobacterial separation from other bacteria is
narrow.

## What this does not say

- **Not that the host was structurally complex.** What is shown is that
  its genes were of mixed origin before the mitochondrion, on the
  method's assumptions. "Complex cell" in the conclusion means a genome
  with bacterial pathways in it.
- **Not how the chimaera arose.** "Serial symbiotic associations with
  different partners, the existence of prokaryotic consortia, or gradual
  waves of HGT" are all allowed.
- **Not that stem length is time.** It is time multiplied by an unknown
  ratio of rates, and it is distance to the closest sampled relative.
  The paper's own Lokiarchaeota analysis shows that adding a closer
  genome shortens stems (30 families). Archaea were sampled with 130
  genomes against 3,318 bacterial ones. The inference that sampling
  contributes to the archaeal–bacterial gap is mine.
- **Not that mitochondria ended bacterial transfer or gave a "definitive
  selective advantage".** Both are asserted in the last paragraph and
  not analysed.

## Connections

- **[QUESTION-277](../questions.d/QUESTION-277.md).** It bears on whether eukaryogenesis was one merger or
  a sequence. It is evidence that genes from several bacterial sources
  reached the host lineage before the mitochondrion, by partners or by
  transfer. It does not address D, R, C or S.
- **[LIT-1566](../literature.d/LIT-1566.md) ([THEORY-tmp5wptr](THEORY-tmp5wptr.md)).** Kay et al. agree that the
  mitochondrion came late, by dating duplications with a relaxed clock.
  They find most non-alphaproteobacterial duplications after the
  mitochondrion and argue against serial endosymbiosis. Duplication is
  not acquisition, so this is a tension, not a contradiction. The
  comparison is mine.
