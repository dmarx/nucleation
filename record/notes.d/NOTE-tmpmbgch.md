---
status: Read
paper: LIT-tmpvrv55
title: 'Alfano, Cheong & Curry 2024, moral universals in 256 societies'
version: 1
history:
- version: 1
  date: '2026-10-02'
  note: >-
    Read in full (the version of record, Heliyon 10(6):e25940, CC
    BY-NC-ND 4.0, full-text XML of PMC10945118 from Europe PMC). The whole
    text, Tables 1–6, figure captions, footnotes 1–14 and references were
    read. The figures and the supplementary dictionary file were not seen.
    The quoted ethnographic passages were taken as quoted.
date: '2026-10-02'
summary: >-
  The Morality-as-Cooperation Dictionary (fourteen virtue and vice
  sub-dictionaries, built by brainstorming, colleague crowd-sourcing and
  WordNet expansion, culled by two coders at κ ≈ .65–.70) is run with LIWC
  over 9,653 eHRAF Ethics paragraphs from 256 societies. Most domains are
  detected in most societies. Region and subsistence matter significantly
  but slightly. Against the sixty-society hand codes, agreement is about 80%
  but κ only .08–.25, with false positives outnumbering true ones. The
  method cannot detect valence. A spot-check found admired theft in four
  societies and societies that do not value bravery or reciprocity.
---

<!-- inactive-ok-file: LIT-tmpvrv55 — Proposed: the paper this note reads, placed by it -->

<!-- inactive-ok-file: LIT-047 — Proposed: the sixty-society test this paper extends, whose verdict this reading bears on -->

<!-- inactive-ok-file: LIT-tmpps55m — Proposed: Moral Molecules, whose examples this paper reports, filed in the same batch -->

<!-- inactive-ok-file: LIT-tmp0moou — Proposed: the MAC-Q, filed in the same batch -->

# NOTE-tmpmbgch: Alfano, Cheong & Curry 2024, moral universals in 256 societies

## Contribution

The paper ([LIT-tmpvrv55](../literature.d/LIT-tmpvrv55.md)) builds a LIWC-format dictionary for the seven domains of
morality-as-cooperation (MAC-D). It runs the dictionary over the eHRAF
Ethics paragraphs of every society that has any (256 of 331), and checks
the machine codes against the hand codes of the sixty-society study
([LIT-047](../literature.d/LIT-047.md)). It is the first use of the programme's domains on the whole HRAF
corpus, and the first published MAC dictionary.

## Key insight

A dictionary can measure how much a paragraph talks about a domain, but not
whether it praises or condemns. So a machine-read replication of a
universality claim can scale up presence. It cannot scale up valence, which
is the part of the claim that made the sixty-society result look strong.

## Assumptions

- **Construction** (§3).
  - The authors and five colleagues "already familiar with MAC" brainstormed
    words, stems and n-grams for seven virtue and seven vice categories:
    371 virtue and 148 vice items.
  - WordNet expanded these. Two co-authors culled the false positives
    (κ = .70 virtue, .65 vice).
  - Antonyms were swapped between the virtue and vice lists by consensus.
  - Final sizes run from 35 items (fairness vice) to 477 (group virtue)
    (Table 1).
- **Corpus.** Only paragraphs labelled Ethics, unlike [LIT-047](../literature.d/LIT-047.md), which also
  used Norms and a keyword search (footnote 10). In all: 1,620,644 words,
  1,389 documents, 8 regions, 9 subsistence types.
- **Measure.** The percentage of a paragraph's words found in each
  sub-dictionary. Sub-dictionaries differ in size and base rate, so domains
  cannot be compared with one another, only across paragraphs (footnote 13).
- **Heroism** is coded as bravery or generosity, where [LIT-047](../literature.d/LIT-047.md) coded bravery
  only, so the two are "not directly comparable" (footnote 4).

## Key results

- **Distribution.** Median and mode are 0% for every domain. Means run from
  0.04% (fairness) to 0.92% (family) of words (Table 2).
- **PSF vs non-PSF.** Some differences are significant, but all are small
  (r ≤ .084).
- **Regions** (Table 3). All seven differ significantly (p < .001), with
  ε² from .004 (property) to .055 (heroism). Europe is high on group and
  heroism, and Asia on family.
- **Subsistence** (Table 4). Six of seven differ significantly, all with
  small effects. Reciprocity does not differ (p = .47).
- **Validation against the hand codes** (§4.2).
  - Each sub-dictionary is the best predictor of its own hand code (Table 5;
    odds ratios 1.82–4.43).
  - Dichotomised, the models are right about 80% of the time. But positives
    are rare (about 3%), so false positives swamp true ones: for family,
    469 false against 110 true.
  - κ: family .25, group .10, reciprocity .21, heroism .13, deference .16,
    fairness .08, property .23.
- **Predicted prevalence** (Table 6, PSF hand codes → PSF predicted). The
  dictionary overstates every domain except property:
  - family 78 → 88%;
  - group 73 → 95%;
  - reciprocity 72 → 88%;
  - heroism 53 → 92%;
  - deference 58 → 92%;
  - fairness 15 → 58%;
  - property 90 → 85%.
  
  The non-PSF predictions (78, 88, 69, 78, 81, 43, 76%) are read as
  overestimates "roughly the same" as in the PSF. The correction is asserted,
  not computed.
- **Spot-checks** (§4.3).
  - Confirming examples for all seven domains.
  - Counterexamples: Navajo "no conception of a moral obligation to
    reciprocate"; !Kung San who "attach no value to fighting"; admired theft
    among Bedouin, Greek (Sarakatsani), Pashtun and Wogeo.
  - Two moral molecules, filial piety and honour.
  - Two dilemmas, gratitude against prestige and feud against harmony.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Most of the seven morals are present in most of 256 societies, in all regions | weak–moderate | dictionary presence at κ .08–.25 against hand codes, with systematic over-detection |
| C2 | The 196 non-PSF societies have about the same prevalence as the 60 PSF societies | weak | inferred from similar paragraph-level means and an assumed common error; not hand-checked |
| C3 | Variation by region and subsistence is minor | moderate | significant but small effect sizes (Tables 3–4) |
| C4 | MAC-D is "validated" | weak | best-predictor-of-own-code holds; agreement is slight to fair, and the authors call the overall fit "fairly low" (§5) |
| C5 | The results are "evidence for moral universalism" (significance statement) | weak | the method cannot detect valence, and universalism of valence is the claim at issue |
| C6 | The counterexamples reflect "competition between the morals … rather than outright devaluation" | assertion | the same reading as [LIT-047](../literature.d/LIT-047.md)'s footnote 3; no criterion separates the two |

## Concepts

- **MAC-D.** Seven virtue and seven vice sub-dictionaries in LIWC's `.dic`
  format, released for LIWC, R (quanteda) and Python.
- **PSF60.** The HRAF Probability Sample Files societies hand-coded in
  [LIT-047](../literature.d/LIT-047.md).

## Connections

- **The sixty-society test ([LIT-047](../literature.d/LIT-047.md), [NOTE-034](NOTE-034.md)).** The paper restates [LIT-047](../literature.d/LIT-047.md)'s
  results, including "equal frequency across six cultural regions", as
  support for MAC. Its own regional tests then find significant
  differences. It bears on [NOTE-034](NOTE-034.md)'s verdict as the LIT entry sets out:
  - valence is untested;
  - the spot-checks found the negative cases the original design rarely
    registered, and the paper absorbs them as conflicts;
  - regional equality is not borne out;
  - non-cooperative content is still uncoded.
- **Purity ([LIT-101](../literature.d/LIT-101.md)).** There is no purity, sexual-conduct or harm dictionary,
  so the paper is silent on the commentaries' objection. The authors defer
  an MFT comparison until HRAF has hand codes for it (§3.1).
- **Moral molecules ([LIT-tmpps55m](../literature.d/LIT-tmpps55m.md)).** Filial piety and honour are reported as
  examples, not counted.
- **The MAC-Q ([LIT-tmp0moou](../literature.d/LIT-tmp0moou.md)).** Proposed as the instrument for the
  ecological-variation test the paper could not run (§5).

## Bearing on the record

There is no instruction for ML practice. The method is lexicon counting
from 2020 with WordNet expansion, and the authors point to BERT and LLMs as
future work, so it is not an anthology candidate. For the
morality-as-cooperation thread it should not be cited as a replication of
the 99.9% valence result. It replicates presence, roughly. It is better
evidence of variation by region and subsistence than of its absence.

## Limitations

- **Valence-blind** by design, as the authors state (§5).
- **Poor agreement** with the hand codes (κ ≤ .25), and systematic
  over-detection.
- **Ethics paragraphs only.** This narrows the corpus relative to [LIT-047](../literature.d/LIT-047.md).
- **Spot-checks are anecdotes.** Counterexamples were not counted. With the
  same reading, [LIT-047](../literature.d/LIT-047.md)'s one negative might have been several.
- **Ethnographers' words, mostly in English**, as the authors note (§5).

## Open questions

- With a valence-aware classifier validated against blind hand codes, what
  share of HRAF mentions of each domain are negative?
- How many societies admire some form of theft, cowardice or ingratitude?
  Does MAC predict which ones, beyond calling them conflicts?
- Run the same way, how much purity, sexual and dietary moral content does
  HRAF contain?

## Corrections

- none to a seeded skim (there was no seed)
- **The citation.** The owner's citation is correct: Alfano, Cheong and Curry
  (2024), *Heliyon* 10(6):e25940.
- **Internal inconsistencies.**
  - §4.1 compares the PSF60 with "the additional 256 non-PSF60 societies";
    there are 196 (abstract, Table 6).
  - §4.3 cites the sixty-society paper as "Curry et al. (2018)"; the
    reference list gives 2019.
  - The text gives ε² up to .056 for regions; Table 3's largest is .055.
