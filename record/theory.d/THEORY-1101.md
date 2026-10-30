---
number: 1101
status: Active
formerly:
- THEORY-tmpbinho
title: 'Tobiasson, Luo, Wolf and Koonin find, on 5,850 eukaryotic gene stems, that normalized stem length does not behave as a clock of acquisition time: alphaproteobacterial stems are longer than Asgard ones for the 70% of stems below 0.3 and shorter only above 0.35, oxidative-phosphorylation genes presumed acquired together vary by more than two orders of magnitude, and information-processing genes have short stems; they conclude that even normalized stem lengths are set primarily by factors other than acquisition time, at least over the long timescales analysed, and suggest that adaptation after acquisition lengthens stems'
version: 2
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed Proposed from NOTE-1242, the reading in full of the PubMed
    Central copy of Tobiasson et al. (2026). The observations are shown on
    the paper's data, with 20 technical replicates. The proposed cause,
    post-acquisition adaptation, is suggested and only "at least partially
    supported". Users of the method (Bernabeu et al.) defend it with
    analyses in a supplement not read here. Hence Proposed.
- version: 2
  date: '2026-10-30'
  note: >-
    Promoted by the twenty-second status review, at the status review's
    ruling (the owner delegated these rulings; ADR-065). The title
    reports what Tobiasson and colleagues find and conclude; NOTE-1242
    read the paper in full, and nothing in the record contradicts the
    report. What the condition asked beyond the title, that the authors
    be right, moves to THEORY-tmp60tmj, Proposed, which extends this
    entry and keeps the condition word for word (ADR-065 §3). Narrowed
    first (ADR-047's routing): the authors' hedge "at least across the
    long evolutionary timescales analysed here" is restored, and the
    closing clause, which applied the result to orderings the paper does
    not itself address, is dropped. Its general form goes to
    THEORY-tmp60tmj (kind 1), and its application to particular
    orderings to CLAIM-tmppxk4w (kind 2). The old title: "Tobiasson,
    Luo, Wolf and Koonin find, on 5,850 eukaryotic gene stems, that
    normalized stem length does not behave as a clock of acquisition
    time: alphaproteobacterial stems are longer than Asgard ones for the
    70% of stems below 0.3 and shorter only above 0.35,
    oxidative-phosphorylation genes presumed acquired together vary by
    more than two orders of magnitude, and information-processing genes
    have short stems; they suggest that adaptation after acquisition
    lengthens stems, so that relative timings drawn from stem lengths
    alone, including mitochondrion-late orderings and transfer waves,
    are not supported by the method". The answers edge on QUESTION-277 is moved to
    bears_on (ADR-060): the reading is evidence on the question, not an
    answer to it as posed. The old promote_when: "A test of normalized
    stem length on eukaryotic gene sets whose acquisition times are
    known independently to be equal or to differ, such as genes moved
    together from one endosymbiont, with enough families to measure
    their spread. It must show whether co-acquired genes have stems as
    dispersed as reported here, and identify what sets the spread
    (adaptation after acquisition, rate variation, sampling). Agreement
    or disagreement with an independent clock, such as dated gene
    duplications, would also bear on it. Further stem-length analyses
    that assume the clock, or functional classes giving overlapping
    distributions, cannot settle it, since the dispute is whether a
    factor other than time dominates. It is refuted if co-acquired
    genes, after correction for the identified factors, cluster tightly
    in stem length, or if stem-length orderings match an independent
    clock across donors."
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
  They test the stem-length method of Pittis and Gabaldón on their own
  trees and reproduce its mitochondrion-late signal only for long stems.
  Below 0.3, where 70% of stems lie, the order reverses, and genes
  presumably acquired together scatter widely. They conclude that "even
  normalized stem lengths are determined primarily by factors other than
  the gene acquisition time". The paper still favours a late mitochondrion, on
  other grounds.
---
<!-- inactive-ok-file: THEORY-tmp60tmj CLAIM-tmppxk4w — Proposed; filed beside this reading by the twenty-second status review: the wider thesis it reports, and the record's own critique split from its title -->
<!-- inactive-ok-file: NOTE-1242 NOTE-1237 — filed in the same batch of readings and not yet merged; the reading this comes from and the accounts it is set beside -->
# THEORY-1101: Tobiasson, Luo, Wolf and Koonin find, on 5,850 eukaryotic gene stems, that normalized stem length does not behave as a clock of acquisition time: alphaproteobacterial stems are longer than Asgard ones for the 70% of stems below 0.3 and shorter only above 0.35, oxidative-phosphorylation genes presumed acquired together vary by more than two orders of magnitude, and information-processing genes have short stems; they conclude that even normalized stem lengths are set primarily by factors other than acquisition time, at least over the long timescales analysed, and suggest that adaptation after acquisition lengthens stems

## Source

Tobiasson, Luo, Wolf & Koonin (2026), [LIT-1558](../literature.d/LIT-1558.md), read in full in [NOTE-1242](../notes.d/NOTE-1242.md).
The section "Ancestral stem lengths", Figure 3 and its caption, and Extended
Data Figure 10b,c, read from captions.

## What was actually shown

- **The method tested.** Pittis and Gabaldón's normalized stem length: the
  branch from the last common ancestor of eukaryotes and their prokaryotic
  sister (FECA) to LECA, divided by the median LECA-to-tip branch. Since
  LECA-to-present is the same time for all genes, a longer stem is read as
  an earlier acquisition.
- **The distribution.** 5,850 stems, with a sharp peak near 0.05, "highly
  reminiscent of previous findings".
- **The reversal.** "Alphaproteobacterial stems shorter than 0.3 (70% of all
  stems) were significantly longer than those of Asgard origin, but
  alphaproteobacterial stems longer than 0.35 were instead shorter than
  Asgard on average." This was reproducible over 20 full technical
  replicates of 200 stems (Extended Data Fig. 10b). Cyanobacterial stems
  follow a weaker version of the same trend. Pittis and Gabaldón "analysed
  primarily stems within that range", the long one.
- **Restricted to clear cases.** Ribosomal proteins (archaeal) and oxidative
  phosphorylation (alphaproteobacterial) accentuate both trends.
- **Spread among co-acquired genes.** Oxidative-phosphorylation stems,
  "assumed to have been acquired simultaneously", vary over more than two
  orders of magnitude.
- **Function.** Information-processing genes, expected to be the oldest
  residents, have shorter-than-average stems.
- **Conclusion.** "even normalized stem lengths are determined primarily by
  factors other than the gene acquisition time, at least across the long
  evolutionary timescales analysed here."
- **Suggested cause.** "the amount of evolution post-acquisition, necessary
  to adjust an acquired gene to a new biological environment." Asgard genes
  were pre-adapted, and genes from distant bacteria had to change. This is
  "at least partially supported" by long stems among diverse bacterial
  donors (Extended Data Fig. 10c).

What could have failed: alphaproteobacterial stems could have been shorter
across the whole distribution, and co-acquired genes could have clustered.
Neither happened on these data.

## What this does not say

- **Not that the mitochondrion came early.** The paper still holds that
  "mitochondrial acquisition was a relatively late event", on gene-content
  grounds ([THEORY-1104](THEORY-1104.md)). It takes away one line of evidence for that
  view, not the view.
- **Not what does set stem length.** Post-acquisition adaptation is a
  suggestion. Rate variation along branches and unsampled donor lineages
  are other candidates, and the paper does not test among them.
- **Not shown on Bernabeu et al.'s pipeline.** They model the mode of each
  donor's distribution, discard long-stemmed outliers, and cite a functional
  control (their Supplementary Fig. 13, not read here) in its favour. The two
  datasets appear to disagree even on the basic pattern. Here Asgard stems
  are mostly shorter than alphaproteobacterial ones. There Asgard is "the
  most ancestral signal". Whether that is a difference in data or in
  summary statistic is not settled by either paper. The comparison is mine.

## Connections

- **[THEORY-1105](THEORY-1105.md) (Bernabeu et al.): rival.** Its ordering of transfer
  waves, and its claim that some bacterial transfers preceded the
  mitochondrion, rest on stem lengths read as relative times. If this
  account holds, that ordering is not established by its method.
- **[LIT-1595](../literature.d/LIT-1595.md) (Pittis & Gabaldón 2016, unread).** The method's origin. This
  account reproduces its result only in the regime it mostly sampled.
- **[LIT-1566](../literature.d/LIT-1566.md) (Kay et al., unread).** It times eukaryogenesis by dated gene
  duplications, a different clock. If its ordering agrees with stem-length
  orderings, that would count against this account. If it agrees with
  gene-content scenarios and not with stem lengths, that would count for it.
- **[QUESTION-277](../questions.d/QUESTION-277.md).** The question distinguishes a single merger from a
  sequence of associations. Any sequence needs a clock. This account says
  the clock most used for the purpose is unreliable.

## Note of 2026-10-30: promoted, and the wider thesis filed beside it

The twenty-second status review promoted this reading under [ADR-065](../decisions.d/ADR-065.md): it reports what Tobiasson and colleagues find and conclude, and [NOTE-1242](../notes.d/NOTE-1242.md) read the paper in full. Whether normalized stem length is in general no clock of acquisition is [THEORY-tmp60tmj](THEORY-tmp60tmj.md)'s question, Proposed, which keeps this entry's old promote_when. The record's own critique, once in the title, is now [CLAIM-tmppxk4w](../claims.d/CLAIM-tmppxk4w.md), Proposed.
