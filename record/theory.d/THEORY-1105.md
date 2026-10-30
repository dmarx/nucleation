---
number: 1105
status: Active
formerly:
- THEORY-tmphywi5
title: 'In Bernabeu, Manzano-Morales, Marcet-Houben and Gabaldón''s reconstruction of the last eukaryotic common ancestor''s proteome, two bacterial phyla besides the mitochondrial ancestor, Myxococcota and Planctomycetota, each account for a share of the proteome comparable to that of Alphaproteobacteria and Asgard archaea under thresholds calibrated on those accepted partners, and stem-length distributions order the acquisitions as waves, Asgard first, then Planctomycetota, then the mitochondrial ancestor and Myxococcota together; the authors read this as serial associations with several partners, while conceding that their data cannot say whether any donor was a symbiont'
version: 3
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed Proposed from NOTE-1237, the reading in full of the PubMed
    Central copy of Bernabeu et al. (2026). The donor result is consistent
    across three datasets, with controls reported in a supplement not read
    here. The ordering rests on stem lengths as relative times, which
    Tobiasson et al. dispute on their own data (THEORY-1101). The step
    from gene donors to partners is one the authors themselves do not
    take as shown. Hence Proposed.
- version: 2
  date: '2026-10-30'
  note: >-
    Promoted by the twenty-second status review, at the status review's
    ruling (the owner delegated these rulings; ADR-065). The title
    reports what Bernabeu and colleagues' reconstruction finds and how
    the authors read it; NOTE-1237 read the paper in full, and nothing
    in the record contradicts the report. What the condition asked
    beyond the title, that the authors be right, moves to
    THEORY-1215, Proposed, which extends this entry and keeps the
    condition word for word (ADR-065 §3). The answers edge on QUESTION-277 is moved
    to bears_on (ADR-060): the reading is evidence on the question, not
    an answer to it as posed. The old promote_when: "Two kinds of result
    are needed, one per half of the claim. For the donors: the
    Myxococcota and Planctomycetota signals recovered by an independent
    pipeline under a strict pangenome filter (such as Tobiasson et al.'s
    50% of species per class), and shown not to be genes carried into
    the eukaryotic lineage by the Asgard or alphaproteobacterial
    partner. For the waves: a clock other than stem length, or a
    validation of stem length on genes of known common acquisition, that
    orders Planctomycetota before the mitochondrion. Neither half
    establishes that any donor was a partner in an association. That
    would need evidence of a kind gene ancestries do not give, such as a
    cell-biological or physiological trace of a third partner. More
    stem-length analyses, or more donors found by the same calibrated
    thresholds, cannot settle it. It is in trouble if the extra donors
    vanish under the stricter filter, or if an independent clock puts
    their genes after the mitochondrion's."
- version: 3
  date: '2026-10-30'
  note: >-
    LIT-1595 is read (NOTE-1240), so the Connections entry that called it
    unread now names the reading. Picked up by the twenty-third status
    review (LU-DP-011).
tags:
- endosymbiosis
- natural-sciences
date: '2026-10-27'
source:
- LIT-1561
bears_on:
- QUESTION-277
summary: >-
  Bernabeu, Manzano-Morales, Marcet-Houben & Gabaldón (2026), [LIT-1561](../literature.d/LIT-1561.md), read
  in [NOTE-1237](../notes.d/NOTE-1237.md). Under thresholds chosen to maximize assignments to
  Alphaproteobacteria and Asgard, Myxococcota (3.92% of the proteome) and
  Planctomycetota (2.24%) pass in every dataset, beside Alphaproteobacteria
  (3.99%) and Asgard (3.28%). A control removing Alphaproteobacteria from
  the database does not reproduce their pattern. Stem lengths put
  Planctomycetota before the mitochondrion. The authors "challenge models
  depicting eukaryogenesis as a one-off event resulting from a binary
  symbiotic interaction", and also say their data "do not provide
  information on the host or endosymbiotic nature of any partner".
---
<!-- inactive-ok-file: THEORY-1215 — Proposed; filed beside this reading by the twenty-second status review: the wider thesis it reports -->
<!-- inactive-ok-file: NOTE-1237 NOTE-1242 — filed in the same batch of readings and not yet merged; the reading this comes from and the accounts it is set beside -->
# THEORY-1105: In Bernabeu, Manzano-Morales, Marcet-Houben and Gabaldón's reconstruction of the last eukaryotic common ancestor's proteome, two bacterial phyla besides the mitochondrial ancestor, Myxococcota and Planctomycetota, each account for a share of the proteome comparable to that of Alphaproteobacteria and Asgard archaea under thresholds calibrated on those accepted partners, and stem-length distributions order the acquisitions as waves, Asgard first, then Planctomycetota, then the mitochondrial ancestor and Myxococcota together; the authors read this as serial associations with several partners, while conceding that their data cannot say whether any donor was a symbiont

## Source

Bernabeu, Manzano-Morales, Marcet-Houben & Gabaldón (2026), *Nature* 656:
399–405, [LIT-1561](../literature.d/LIT-1561.md), read in full in [NOTE-1237](../notes.d/NOTE-1237.md) from the PubMed Central copy
(PMC13468126). The sections "Determining the ancestries of LECA" and "Donor
relative timing and metabolism", the Discussion, Methods ("Stress test",
"Verticality test", "Inferring the acquisition waves"), Figures 2–3 and
Extended Data Figures 2–3, read from captions.

## What was actually shown

- **The proteome.** Three 100-proteome eukaryotic datasets, LECA families
  defined by spread across supergroups, and maximum-likelihood trees with
  the closest prokaryotic and viral homologues from order-level
  pangenomes. About 53% of families are acquisitions from outside
  eukaryotes.
- **Calibration.** Support thresholds were chosen to maximize the share of
  trees assigned to Alphaproteobacteria and Asgard, "assuming that the
  selected thresholds properly removed noise and kept only the reliable
  signals".
- **Donors at those thresholds:** Alphaproteobacteria 3.99%, Myxococcota
  3.92%, Asgard 3.28%, Planctomycetota 2.24% of the proteome. Chloroflexota
  and Gammaproteobacteria failed in some datasets.
- **Controls, reported in the main text, run in the supplement.**
  - Trees for the new donors were not harder to resolve.
  - With Alphaproteobacteria removed from the database, alphaproteobacterial
    genes were assigned mainly to Gammaproteobacteria, then to more distant
    groups. The Myxococcota and Planctomycetota signals do not follow that
    pattern.
- **Waves.** Posterior modes of each donor's normalized stem-length
  distribution give the order: Asgard, "the most ancestral signal"; then
  Planctomycetota; then "the mitochondrial ancestor and Myxococcota, with
  largely overlapping transfer waves". The order was consistent across
  datasets and stringencies.
- **The reading.** "our data support premitochondrial waves of gene
  acquisitions from additional major prokaryotic donors as the most likely
  scenario". The results "challenge models depicting eukaryogenesis as a
  one-off event resulting from a binary symbiotic interaction". And: "our
  data do not provide information on potential types of interaction
  (endosymbiotic, ectosymbiotic, parasitic, and so on)".

What could have failed: the extra donors could have failed the calibrated
thresholds, or tracked the pattern expected of misplaced alphaproteobacterial
genes, and they did neither. The waves could have had the same mode for
every donor. They did not, though the method that measures them is the one
in dispute.

## What this does not say

- **Not that there were more than two symbiotic partners.** The donors are
  sources of genes. The authors say "different forms of interactions
  beyond symbiosis could explain this genetic exchange".
- **Not that the donors' genes came to eukaryotes directly.** The verticality
  test addresses misplacement of alphaproteobacterial genes. It does not
  address bacterial genes that reached the Asgard ancestor first, which
  Tobiasson et al. propose, and which would also leave a donor signal.
  The inference is mine.
- **Not a timing result independent of stem length.** If stem length is not
  a clock ([THEORY-1101](THEORY-1101.md)), the order of waves, and with it the claim that
  Planctomycetota preceded the mitochondrion, falls back to unknown.
- **Not that Asgard contributed only 3% of LECA.** That figure is the share
  passing strict thresholds. It is not comparable with Tobiasson et al.'s
  50% of likelihood weight. The two measure different things.
- **Not a reconstruction of the donors.** Their metabolisms are prevalences
  in living relatives, "incomplete and indirect".

## Connections

- **[THEORY-1104](THEORY-1104.md) (Tobiasson et al.): rival on the donors, compatible on
  the mitochondrion.** The two disagree on whether the
  non-alphaproteobacterial genes form a few major donors' waves or diffuse
  transfer, and on the Asgard share. Tobiasson et al. attribute this paper's
  larger bacterial signal to "more liberal criteria for core pangenome
  construction" (15% of genera per order here, against 50% of species per
  class there). Both papers have the mitochondrion arriving late and
  bacterial genes arriving before it. Neither has data on the kind of
  interaction.
- **[THEORY-1101](THEORY-1101.md): rival.** It disputes the method that orders the waves.
- **[THEORY-1109](THEORY-1109.md) (Santana-Molina et al.): partly compatible.** In central
  carbon metabolism, Planctomycetota–Verrucomicrobiota and Myxococcota–
  Desulfobacterota both appear as sisters, as this account would expect.
  But that paper finds "no additional dominant source of gene donations".
- **[LIT-1595](../literature.d/LIT-1595.md) (Pittis & Gabaldón 2016, read in NOTE-1240).** This is that programme's
  continuation, now with named donors.
- **[QUESTION-277](../questions.d/QUESTION-277.md).** This is the "distributed" side of the record's live
  disagreement. The distribution shown is of gene donors, so it bears on G.
  It bears on the question's routes to dependence only if the donors were
  partners, and the paper leaves that open.

## Note of 2026-10-30: promoted, and the wider thesis filed beside it

The twenty-second status review promoted this reading under [ADR-065](../decisions.d/ADR-065.md): it reports what Bernabeu and colleagues' reconstruction finds and how the authors read it, and [NOTE-1237](../notes.d/NOTE-1237.md) read the paper in full. Whether Myxococcota and Planctomycetota were major donors in waves is [THEORY-1215](THEORY-1215.md)'s question, Proposed, which keeps this entry's old promote_when.
