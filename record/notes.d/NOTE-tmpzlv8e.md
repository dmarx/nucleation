---
status: Read
paper: LIT-1567
title: 'Karnkowska et al. — A eukaryote without a mitochondrial organelle'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Read for LEAD-138 from the in-press article PDF (Current Biology 26,
    1–11, the "Please cite this article in press" layout of the version
    of record) hosted on the University of Warsaw Faculty of Biology
    site, the first author's institution (biol.uw.edu.pl, file
    A_Karnkowska_A_Eukaryote_without_a_Mitochondrial_Organelle_160516.pdf),
    a faculty page admitted under ADR-074. Fetched 2026-11-22 and
    converted to text. Read: the highlights, summary, introduction, all
    of Results and Discussion, the conclusions, the captions of Figures
    1–4 and Table 1, and the opening of Experimental Procedures. Not
    read: the supplemental tables and figures, the remainder of the
    procedures, and the reference list. Europe PMC holds no copy, and
    cell.com answered with a Cloudflare challenge on the same day.
date: '2026-11-22'
summary: >-
  The draft genome of the oxymonad Monocercomonoides sp. PA203 (75 Mb,
  16,629 predicted genes, judged nearly complete) contains no gene for
  any hallmark mitochondrial protein: no import machinery, no metabolite
  carriers, no ISC pathway, no cardiolipin synthesis, no ERMES. Fe–S
  clusters are made by a cytosolic SUF system that an ancestor shared
  with Paratrimastix acquired from bacteria by lateral transfer. The
  loss is secondary, since the free-living sister lineage keeps
  mitochondrial homologues. The authors cannot exclude an organelle of
  wholly altered composition but find no positive evidence for one.
---
<!-- inactive-ok-file: LIT-1567 CASE-168 THEORY-tmpd9ysz — Unfetched, Proposed or new; the work read, the case it checks and the account filed from it -->

# NOTE-tmpzlv8e: Karnkowska et al. — A eukaryote without a mitochondrial organelle

## Contribution

The first genome of an oxymonad, and the first eukaryote for which a
comprehensive search finds no trace of a mitochondrion. It turns the
claim that every living eukaryote needs a mitochondrion or a related
organelle into a claim with a counterexample, and names the
substitution that made the loss possible: a cytosolic, bacterial-type
SUF system in place of the organelle's ISC pathway.

## Key results

- **Genome** (Results, "Genome Characteristics"; Table 1). About 75 Mb,
  16,629 predicted protein-coding genes, 2,095 scaffolds; 90% of
  CEGMA core genes once mitochondrial ones are excluded, over 95% of a
  163-gene phylogenomic set, 77 of 78 cytosolic ribosomal protein
  families. Phylogenomics (Figure 1) places it with *Paratrimastix
  pyriformis* among the Metamonada.
- **No mitochondrial proteins** (Summary; "Absence of Mitochondrial
  Proteins"). The organism "lacks all hallmark mitochondrial
  proteins". No TOM, TIM or SAM component, no mitochondrial carrier,
  no ISC component, no cardiolipin synthase, no ERMES; a Mitominer
  pipeline returned 76 candidates, none a hallmark protein, where every
  control organism yielded "at least a few". As a control on the
  method, Golgi-associated proteins were readily found.
- **Energy** ("Energy Metabolism without a Mitochondrion"). Extended
  glycolysis, PFOR and [FeFe]-hydrogenases, and the arginine deiminase
  pathway, all apparently cytosolic: "virtually identical to G.
  intestinalis and E. histolytica".
- **Fe–S clusters** ("Fe-S Cluster Assembly without a Mitochondrion";
  Figures 3–4). The ISC pathway, "thought to be conserved in virtually
  all eukaryotic cells, has been replaced by a cytosolic sulfur
  mobilization system (SUF) acquired by lateral gene transfer from
  bacteria" (Summary). SufB, SufC and a SufS–SufU fusion; introns and
  FISH place the genes in the nucleus; heterologous expression supports
  a cytosolic location. Phylogeny: acquired "by an ancestor of
  Monocercomonoides and Paratrimastix ... independently of all other
  SUF-containing eukaryotes".
- **Secondary loss** (Conclusions). "Because all known oxymonads are
  obligate animal symbionts, and mitochondrial homologs are present in
  the close free-living sister lineage Paratrimastix, the absence of
  mitochondrion in Monocercomonoides sp. must be secondary."
- **"The first example of a eukaryote lacking any form of a
  mitochondrion"** (Summary), "the first known truly secondarily
  amitochondriate eukaryote" (Conclusions).

## Assumptions

- Absence from a draft assembly is absence from the genome. The
  completeness measures support this but do not prove it for any one
  gene.
- Homology and targeting-signal searches would find a mitochondrion if
  one existed. The authors state the limit: "we cannot exclude the
  possibility that a mitochondrion exists ... whose protein composition
  has been altered entirely", which "could not be recognized as a
  mitochondrion homolog by any available means".
- Localization of SUF is inferred from heterologous expression in
  *Trichomonas* and yeast, not shown in *Monocercomonoides* itself.

## Concepts

- **MRO** — mitochondrion-related organelle: hydrogenosomes, mitosomes
  and other reduced derivatives.
- **ISC / SUF / CIA** — the mitochondrial iron–sulfur cluster assembly
  system; the bacterial and plastid sulfur mobilization system; the
  cytosolic iron–sulfur assembly system that finishes clusters for
  cytosolic and nuclear proteins.

## Bearing on the record

- **CASE-168** takes four facts from this work, from its abstract. All
  four hold against the text: every hallmark protein missing; ISC
  replaced by a cytosolic SUF acquired laterally from bacteria; the loss
  secondary on phylogeny; the first eukaryote known to lack any form of
  mitochondrion. Two refinements: the secondary-loss argument rests on
  the free-living sister lineage keeping mitochondrial homologues, as
  well as on phylogeny; and the SUF acquisition belongs to the ancestor
  shared with *Paratrimastix*, which kept its organelle, so it was a
  precondition and not by itself the cause of the loss. The latter is
  what LIT-1574 (NOTE-1243, THEORY-1098) already added; this paper's
  own model (Figure 4) agrees. The case's dated note says what held.
- **QUESTION-277** (evidence, through the case): the reading supports
  the case's use as the negative control. The integration of the
  mitochondrion was undone once a third-party gene set replaced its one
  universal job, and the cell that resulted is "a standard eukaryotic
  cell in other respects".
- The case's inference that a host gut was substituted for an internal
  partner finds a premise here: "all known oxymonads are obligate animal
  symbionts". The inference itself remains the record's.

## Limitations

- A draft genome from one strain; no proteomics or microscopy of the
  organelle's absence here (LIT-1574 adds FIB-SEM later, with its own
  caveat).
- The authors' sense of "first": the first shown, not that relatives
  lack it too; they say nothing about other oxymonads' genomes.
- Supplementary tables (S1–S6), where the searches are listed, were not
  read.
