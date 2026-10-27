---
status: Read
paper: LIT-1571
title: 'McCutcheon, Garber, Spencer & Warren — How do bacterial endosymbionts work with so few genes?'
version: 1
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Read in full from the PubMed Central copy of the version of record
    (PMC11020763, CC BY), fetched on 2026-10-27 as full-text XML through
    the Europe PMC REST service and converted to text. Read: both
    abstracts, the introduction, "Features of endosymbionts with reduced
    genomes" and its three subsections, the four "unsolved mystery"
    sections, the conclusions, and the captions of Figures 1–4. Figures
    2 and 3 were read from their captions and the text; the gene matrix
    and the PCA themselves (data on Zenodo, record 10780716) were not
    re-analysed. References were not read. It is an "Unsolved Mystery"
    essay: one new descriptive analysis (Figures 2–3), no experiment.
date: '2026-10-27'
summary: >-
  An essay on the endosymbionts with genomes under about 200 kb, which the
  authors call "tipping-point endosymbionts". Below about 400 kb,
  symbionts almost always lose the genes to build their own envelope and
  to move proteins across it. Below about 200 kb, even translation
  erodes: ribosomal proteins, tRNAs and aminoacyl-tRNA synthetases go.
  Their proteomes are among the most compositionally biased in bacteria.
  The paper asks four questions it cannot answer: where their membranes,
  transporters, missing translation parts and protein stability come
  from. Its best guess is from the host, as in organelles. The thresholds
  come from a hand-picked set of genomes, and the composition analysis is
  called preliminary.
---
<!-- inactive-ok-file: THEORY-tmpf67xs — Proposed; filed from this reading -->
<!-- inactive-ok-file: QUESTION-277 CASE-173 CASE-171 CASE-174 CASE-167 LIT-1559 LIT-1560 LIT-1569 LIT-1572 LIT-1596 — Open, Proposed or Deferred; the question, cases and unread works this reading is set beside, nothing here rests on them -->

# NOTE-tmpx2qkq: McCutcheon, Garber, Spencer & Warren — How do bacterial endosymbionts work with so few genes?

## Contribution

It draws a line inside the class of reduced endosymbionts. The earlier
picture ([LIT-1559](../literature.d/LIT-1559.md), unread here) was of degenerate genomes that "retain
only the most essential functions", with information processing the last
to go. This paper shows that past about 200 kb, even translation, "the
most tightly conserved process", starts to erode. Past about 400 kb, the
cell can no longer build or control its own boundary. It turns that
observation into four concrete open problems about how the host must be
supplying what the symbiont no longer encodes.

## Key insight

Genome reduction comes in two thresholds, and past the second the
symbiont cannot be self-sufficient in the most basic sense: "Tipping-point
endosymbiont genomes encode no genes for making their own cell membranes
or for producing the lipid molecules from which membranes are assembled
or the enzymatic machinery that enables transport". "But their membranes
exist ... and apparently work, so where do they come from?" The authors'
answer is the host, "just as in mitochondria, chloroplasts, and plastids".
If so, a bacterium that was never given a protein-import system is being
built and supplied by its host in the ways that define an organelle. The
paper calls host-directed protein import "a major milestone in the
evolution of a bona fide organelle".

## Assumptions

- **Genome content is a proxy for capacity.** A gene absent from the
  genome is a function the symbiont lacks on its own. Gene presence was
  called from annotations, the literature and HMMER searches. Some
  genomes are drafts, so "the exact gene patterns should be considered
  tentative" (Figure 2 caption).
- **The genome set is representative.** Figure 2's organisms were
  "manually" selected from GenBank: every genome under 1 Mb, but only the
  largest and smallest of each genus.
- **The 200 kb cutoff is "somewhat arbitrary"** (Figure 3 caption, on
  *Zinderia* just missing it).

## Key results

- **Diverse origins.** Bacteria with genomes under 1 Mb are "almost
  exclusively" symbionts. They come from 10 bacterial groups, and those
  under 200 kb from 5 (Alpha-, Beta- and Gammaproteobacteria, Bacteroidia,
  Verrucomicrobiota), whose common ancestor is near the origin of
  cellular life. The authors read the shared features as convergent.
- **First threshold, about 400 kb (Figure 2).** Genes for fatty acids,
  phospholipids and cell wall, for transport across the envelope (BAM
  complex, sec translocon), and for envelope proteins (ATP synthase) are
  "generally lost in concert". Below about 400 kb, endosymbionts "almost
  universally lose the autonomous ability to build and to control the
  transport of molecules across their cellular envelope". Severe erosion
  can start at 0.6–0.7 Mb in candidate phyla radiation bacteria.
- **Second threshold, about 200 kb (Figure 2).** Above it, genomes keep
  enough tRNAs to decode all codons, enough aaRSs to charge them, and
  about 50 ribosomal proteins. Below it, many of each are lost. One cicada
  endosymbiont lacks tRNA genes for eight amino acids it still encodes. Up
  to 20 ribosomal proteins can be missing.
- **Composition (Figure 3).** A PCA of amino-acid frequencies across
  98,966 proteomes:
  - PC1, 85% of the variance, tracks genomic GC content, recovered from
    amino-acid frequencies alone;
  - tipping-point endosymbionts lie "well off the main cloud";
  - extremophiles (except halophiles) do not.

  The authors conclude that "mutational and population genetic forces can
  be more powerful in driving outlier proteome compositional biases than
  physical forces". *Zinderia*'s proteome is almost 50% lysine,
  isoleucine and asparagine, against bacterial averages of 5%, 6% and 4%.
  The analysis is "preliminary".
- **The four mysteries, each with the host as the candidate.**
  - **Envelope.** Many tipping-point endosymbionts show three bilayers:
    two inherited, one from the host's engulfment. Building them may use
    membrane contact sites, as organelles do. Pathogen-style effector
    secretion cannot be the route, since the symbionts can no longer
    secrete effectors.
  - **Transport.** Sap-feeding insects have evolved symbiosis-specific
    amino-acid transporters by gene duplication, and enrich the vacuolar
    membrane with them. How molecules cross the symbiont's own two
    membranes "is unknown".
  - **Translation.**
    - No bacterial tRNA gene transferred to a host nucleus has been
      reported as imported by an endosymbiont or organelle.
    - No new transfer of aaRS genes has been found.
    - The candidates are imported host tRNAs, imported aaRSs, or imported
      charged tRNAs.
    - Ribosomes may be shrinking to a functional core, or acquiring
      host-encoded proteins as mitochondrial ribosomes did.
  - **Protein function.** Endosymbiont RNAs and proteins are predicted to
    be less stable. Endosymbionts are more heat-sensitive than their
    hosts. High GroEL expression may buffer this.
- **Import already observed.** Host-encoded proteins have been found by
  immunofluorescence in the cytoplasm of aphid and mealybug endosymbionts
  (references 55 and 61, not read here). These studies looked at "just one
  protein each", and the mechanism is unknown. Large-scale import is
  established in pre-tipping-point endosymbionts of protists (references
  59–60), which is the *Paulinella* case.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Below about 400 kb, endosymbionts almost always lose the genes to build their envelope and to transport across it, and these losses go together | moderate | the Figure 2 matrix over a hand-picked set; patterns "tentative" |
| C2 | Below about 200 kb, translation-related genes (tRNAs, aaRSs, ribosomal proteins) erode, where above it they are retained | moderate | Figure 2; the threshold's precise value is "somewhat arbitrary" |
| C3 | Tipping-point endosymbionts have among the most compositionally biased proteomes in bacteria, beyond extremophiles | moderate | a PCA of about 99,000 proteomes; "preliminary" |
| C4 | Mutational and population-genetic forces can shape proteome composition more strongly than physical environment | weak to moderate | inferred from C3, given the stable intracellular environment |
| C5 | The membranes, transport and missing translation components of tipping-point endosymbionts are supplied by the host | weak | the organelle analogy, three-membrane micrographs, and single-protein import observations; the mechanisms are unknown |
| C6 | Host-encoded proteins are imported into insect endosymbionts | moderate for existence, weak for scale | two cited single-protein studies, and an expectation that "the total number ... is likely to be much higher" |

## Concepts

- **Tipping-point endosymbiont**: one with a genome under about 200 kb,
  where translation genes begin to be lost.
- **Host-beneficial endosymbiosis**: "an organism stably maintains an
  unrelated organism inside some or all of its cells", to the host's
  benefit.
- **Three-membrane envelope**: the two inherited membranes of a
  gram-negative ancestor, plus the host-derived vacuolar membrane.
- **Membrane contact site**: a protein junction between closely spaced
  membranes through which lipids pass, used by mitochondria and plastids.

## Connections

It updates McCutcheon & Moran's 2012 review ([LIT-1559](../literature.d/LIT-1559.md), unread). The
mealybug symbiont *Tremblaya* is its Figure 4, which links it to
[LIT-1569](../literature.d/LIT-1569.md) and [LIT-1572](../literature.d/LIT-1572.md), both unread. Its protein-import mystery is the
subject of Sørensen et al. ([LIT-1560](../literature.d/LIT-1560.md), unread), and its Shigenobu-era
picture of *Buchnera* ([LIT-1596](../literature.d/LIT-1596.md), unread) is a symbiont well above
the tipping point.

## Bearing on the record

- **[QUESTION-277](../questions.d/QUESTION-277.md), regulatory control (C) and gene distribution (G).** The
  question placed host control with gene transfer and import, the
  *Paulinella* route ([CASE-174](../cases.d/CASE-174.md)). This reading shows control arising
  another way in insect symbioses. Below the thresholds, a symbiont that
  cannot build its membrane or charge its tRNAs is supplied by the host
  whether or not genes moved. The host's control is then forced by the
  symbiont's losses, not won by transfer. G and C are therefore not
  independent: losses in the symbiont's genome create the host's role.
  The inference is mine.
- **[CASE-173](../cases.d/CASE-173.md) (aphid–*Buchnera*).** The case says the abstracts it rests on
  report no gene transfer to the host. This reading adds that a
  host-encoded protein has been found in *Buchnera*'s cytoplasm (its
  reference 55). It does not say the protein is a transferred *Buchnera*
  gene: the paper speaks of horizontally transferred bacterial genes on
  host genomes in general. A dated note goes on the case.
- **[CASE-171](../cases.d/CASE-171.md) (mealybugs).** *Tremblaya* is a tipping-point endosymbiont
  with a three-membrane envelope (Figure 4), and a host-encoded protein
  has been seen in a mealybug endosymbiont. A dated note goes on the case.
- **[CASE-167](../cases.d/CASE-167.md) (nitroplast) and [CASE-174](../cases.d/CASE-174.md) (*Paulinella*).** These are the
  "pre-tipping-point" endosymbionts in protists where import is
  established "on a large scale". The paper's milestone language, import
  as the mark of "a bona fide organelle", is the criterion those cases
  rest on.
- Filed as [THEORY-tmpf67xs](../theory.d/THEORY-tmpf67xs.md). No instruction for machine-learning practice.

## Limitations

- **Thresholds from a curated sample.** The 400 kb and 200 kb boundaries
  are read off a hand-picked matrix with draft genomes. No statistical
  test locates them.
- **Composition analysis preliminary,** by the authors' word. PC2 is
  uninterpreted.
- **Host supply is analogy.** Every proposed mechanism (contact sites,
  imported tRNAs, imported aaRSs, host ribosomal proteins) is a
  hypothesis. The only observations are three-membrane micrographs and
  two single-protein import studies, neither read here.
- **Gene absence is not function absence.** The paper's own point about
  promiscuous enzymes and host supply cuts both ways: a gene absent from
  the symbiont may be present elsewhere in the system.

## Open questions

- Is the 200 kb boundary sharp, and what sets it? The paper locates it
  without a mechanism.
- How many host proteins are imported into tipping-point endosymbionts,
  and by what machinery? Proteomics of isolated symbionts, as done for
  *Paulinella*, would answer it.
- Do insect hosts import tRNAs into their symbionts?
- Does host supply precede the symbiont's losses, allowing them, or follow
  them as rescue? This is the order question [QUESTION-277](../questions.d/QUESTION-277.md) asks of host
  compensation.
