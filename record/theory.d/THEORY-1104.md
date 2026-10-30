---
number: 1104
status: Active
formerly:
- THEORY-tmpfoo2c
title: 'In Tobiasson, Luo, Wolf and Koonin''s constrained-tree survey of widespread eukaryotic protein families, Asgard archaea are the largest single prokaryotic source, with about half the likelihood weight in the best-resolved families and the lead in nearly every functional system, while Alphaproteobacteria contribute a small, coherent set centred on the mitochondrion and other bacteria about a third of families, scattered across functions with no pathway led by one donor except a narrow Myxococcota signal in nucleotide-sugar and nicotinate metabolism; the authors read this as one Asgard host lineage, one endosymbiont and piecemeal gene transfer rather than further symbioses'
version: 2
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed Proposed from NOTE-1242, the reading in full of the PubMed
    Central copy of Tobiasson et al. (2026). The composition result is
    robust within the paper to clustering, taxonomy and pangenome cutoff,
    but rests on sparse and biased genome sampling, which the authors put
    "above all" among their caveats. A rival analysis (Bernabeu et al.,
    LIT-1561) with a more permissive filter finds a much larger bacterial
    share. The reading of the scattered bacterial signal as transfer, not
    symbiosis, is an interpretation. Hence Proposed.
- version: 2
  date: '2026-10-30'
  note: >-
    Promoted by the twenty-second status review, at the status review's
    ruling (the owner delegated these rulings; ADR-065). The title
    reports what Tobiasson and colleagues' survey finds and how the
    authors read it; NOTE-1242 read the paper in full, and nothing in
    the record contradicts the report. What the condition asked beyond
    the title, that the authors be right, moves to THEORY-1197,
    Proposed, which extends this entry and keeps the condition word for
    word (ADR-065 §3). Narrowed first: "with no pathway from one donor"
    was a mis-statement, since by NOTE-1242 Myxococcota leads Asgard in
    nicotinate and nucleotide-sugar metabolism, so the title now names
    that signal (ADR-047 kind 3; dated note below). The record's own
    critique, "a reading the gene ancestries alone cannot establish", is
    split off as CLAIM-508 (kind 2). The old title: "In Tobiasson,
    Luo, Wolf and Koonin's constrained-tree survey of widespread
    eukaryotic protein families, Asgard archaea are the largest single
    prokaryotic source, with about half the likelihood weight in the
    best-resolved families and the lead in nearly every functional
    system, while Alphaproteobacteria contribute a small, coherent set
    centred on the mitochondrion and other bacteria about a third of
    families, scattered across functions with no pathway from one donor;
    the authors read this as one Asgard host lineage, one endosymbiont
    and piecemeal gene transfer rather than further symbioses, a reading
    the gene ancestries alone cannot establish". The answers edge on QUESTION-277 is
    moved to bears_on (ADR-060): the reading is evidence on the
    question, not an answer to it as posed. The old promote_when: "An
    independent reanalysis, on the genome sampling the authors call for
    (complete Asgard genomes, closer relatives of the mitochondrial
    ancestor, better-sampled bacterial phyla), that finds Asgard archaea
    the largest single source of LECA-traced families both under this
    paper's filters and under a more permissive pangenome filter such as
    Bernabeu et al.'s. The share must be measured in a way that can be
    compared across studies. For the further claim that the other
    bacteria were not partners, it also needs a criterion other than
    functional diffuseness that tells a symbiotic donor from a source of
    transferred genes. Larger surveys run through the same pipeline
    cannot settle it, and neither can further agreement on
    information-processing genes, since neither tests the filters or the
    reading. It is in trouble if the Asgard lead goes when the 50%
    pangenome floor or the 0.4–0.99 weight window is relaxed. It is also
    in trouble if one of the scattered bacterial donors turns out to
    have a functionally coherent, time-clustered contribution like the
    mitochondrion's."
tags:
- endosymbiosis
- natural-sciences
date: '2026-10-27'
source:
- LIT-1558
bears_on:
- QUESTION-277
summary: >-
  Tobiasson, Luo, Wolf & Koonin (2026), [LIT-1558](../literature.d/LIT-1558.md), read in [NOTE-1242](../notes.d/NOTE-1242.md).
  In 4,290 well-resolved eukaryotic–prokaryotic clusters, Asgard takes
  50% of likelihood weight and leads in almost every functional class.
  Alphaproteobacteria account for mitochondrial translation, oxidative
  phosphorylation and 4Fe-4S assembly. About a third of clusters point
  elsewhere, with no functional pattern except a narrow Myxococcota
  signal. The authors infer a complex Asgard ancestor, a late
  mitochondrion and "no indication of another symbiotic event". The
  composition is shown; the scenario is read off it.
---
<!-- inactive-ok-file: THEORY-1197 CLAIM-508 — Proposed; filed beside this reading by the twenty-second status review: the wider thesis it reports, and the record's own critique split from its title -->
<!-- inactive-ok-file: NOTE-1242 NOTE-1237 — filed in the same batch of readings and not yet merged; the reading this comes from and the accounts it is set beside -->
# THEORY-1104: In Tobiasson, Luo, Wolf and Koonin's constrained-tree survey of widespread eukaryotic protein families, Asgard archaea are the largest single prokaryotic source, with about half the likelihood weight in the best-resolved families and the lead in nearly every functional system, while Alphaproteobacteria contribute a small, coherent set centred on the mitochondrion and other bacteria about a third of families, scattered across functions with no pathway led by one donor except a narrow Myxococcota signal in nucleotide-sugar and nicotinate metabolism; the authors read this as one Asgard host lineage, one endosymbiont and piecemeal gene transfer rather than further symbioses

## Source

Tobiasson, Luo, Wolf & Koonin (2026), *Nature* 650: 141–149, [LIT-1558](../literature.d/LIT-1558.md), read
in full in [NOTE-1242](../notes.d/NOTE-1242.md) from the PubMed Central copy (PMC12872458). The
sections "Origins of eukaryotic proteins" through "Sparse contributions from
other bacteria", the Discussion, Methods, Figures 1, 2 and 4, and Extended
Data Figures 1–9, read from captions.

## What was actually shown

- **The data.** 13,500 eukaryotic–prokaryotic orthologous clusters (EPOCs)
  built by HMM profile searches. The genomes are 47,545 complete prokaryotic
  ones plus 63 Asgard assemblies, and 993 eukaryotic species. Prokaryotic
  genes were filtered to those in at least 50% of a class's species, to keep
  out late transfer.
- **The statistic.** For each eukaryotic clade, up to 12 nearby prokaryotic
  clades are each forced to be its sister, and expected likelihood weights
  (ELW) are compared. The core set keeps 4,290 EPOCs whose best sister has
  0.4 < ELW < 0.99.
- **Asgard leads.** It has the highest average weight overall, and 50% of
  all weight in the core set. That held under tree-based re-clustering,
  under GTDB phyla in place of NCBI classes, and across pangenome cutoffs
  of 0–67%.
- **Function.** Information processing is "almost exclusively of Asgard
  descent". Asgard also leads in trafficking, glycosylation, GPI anchors,
  sphingolipids and the mevalonate pathway. Alphaproteobacteria lead only in
  mitochondrial translation, oxidative phosphorylation, ubiquinone and
  4Fe-4S assembly. Outside the mitochondrion even Fe–S handling is Asgard.
- **Other bacteria.** They are strongest for 600 of 2,100 KOGs and 1,580 of
  4,290 EPOCs, spread thinly over most pathways. Only Myxococcota, for
  nucleotide-sugar phosphatases and transferases, beats Asgard in a
  pathway with more than 20 EPOCs besides Alphaproteobacteria in oxidative
  phosphorylation. In a strict subset, 33 of 130 EPOCs are bacterial, with
  "no clear functional trend".
- **The reading.** "we interpret these diffuse associations with diverse
  bacteria as indications of several bacterial contributions, each with a
  limited functional scope, probably originating from isolated HGT events
  rather than additional endosymbioses." And: "we obtained no indication of
  another symbiotic event contributing to eukaryogenesis."

What could have failed: the Asgard lead could have depended on the
clustering, the taxonomy or the pangenome cutoff, and by the paper's checks
it did not. The bacterial remainder could have shown pathway-level coherence
for some donor, as the mitochondrion's does, and apart from a narrow
Myxococcota signal it did not.

## What this does not say

- **Not that most LECA genes are Asgard-derived by count.** The 50% is a
  share of likelihood weight among families with prokaryotic homologues
  that pass a confidence window. Bernabeu et al., on a different measure,
  put Asgard at 3.28% of the whole proteome. The two figures are not
  comparable.
- **Not that no other partner existed.** Diffuse transfer is what the
  authors infer from the absence of functional coherence. A partner whose
  genes were mostly lost, or replaced, or spread thin, would also leave a
  diffuse trace. The inference is mine.
- **Not a timing result.** That the cytoskeleton and endomembranes evolved
  in the Asgard lineage before the mitochondrion is the scenario the
  composition is "most compatible with". The paper times nothing, and
  argues that stem lengths cannot ([THEORY-1101](THEORY-1101.md)).
- **Not robust to the sampling the authors flag.** They allow that better
  sampling "might lead to a substantial modification of the model". They
  also allow that the Myxococcota signal may be only "part of a principal
  signal".

## Connections

- **[THEORY-1105](THEORY-1105.md) (Bernabeu et al.): rival on two points, compatible on
  two.** Rival on whether the non-alphaproteobacterial genes are diffuse or
  form a few major donors' waves, and on the size of the Asgard share. On
  the first, Tobiasson et al. say the other's larger bacterial signal may
  be late transfer let in by "more liberal criteria for core pangenome
  construction". Compatible on a mitochondrion acquired late and on
  bacterial genes arriving before it. Neither can show what kind of
  interaction moved the genes.
- **[THEORY-1109](THEORY-1109.md) (Santana-Molina et al.): compatible, with a tension.**
  Both find the alphaproteobacterial contribution mitochondrial. In central
  carbon metabolism, that paper counts more alphaproteobacterial than Asgard
  enzymes (17 to six), against this paper's Asgard lead across "large parts
  of the core metabolic network". The measures differ.
- **[THEORY-1101](THEORY-1101.md)**, from the same paper, is why this one makes no timing
  claim of its own.
- **[LIT-1566](../literature.d/LIT-1566.md) (Kay et al., unread).** The record summarizes it as a complex
  archaeal host before a late mitochondrion. That is this paper's scenario,
  not its rival.
- **[QUESTION-277](../questions.d/QUESTION-277.md).** It bears on G: on this account the host lineage supplies
  nearly every essential function except the mitochondrion's energy and
  Fe–S machinery. It does not bear on D, R, C or S.

## Note of 2026-10-30: the Myxococcota signal

The old title said the other bacteria's genes were scattered "with no pathway from one donor". By the paper as read in [NOTE-1242](../notes.d/NOTE-1242.md), Myxococcota beats Asgard in nicotinate and nucleotide-sugar metabolism, in pathways with more than 20 EPOCs, though the signal reduces to nucleotidases and phosphoribosyltransferases. The title now names it; the authors' reading of the remainder as diffuse transfer is unchanged.

## Note of 2026-10-30: promoted, and the wider thesis filed beside it

The twenty-second status review promoted this reading under [ADR-065](../decisions.d/ADR-065.md): it reports what Tobiasson and colleagues' survey finds and how the authors read it, and [NOTE-1242](../notes.d/NOTE-1242.md) read the paper in full. Whether eukaryogenesis had one host lineage, one endosymbiont and piecemeal transfer is [THEORY-1197](THEORY-1197.md)'s question, Proposed, which keeps this entry's old promote_when. The record's own critique, once in the title, is now [CLAIM-508](../claims.d/CLAIM-508.md), Proposed.
