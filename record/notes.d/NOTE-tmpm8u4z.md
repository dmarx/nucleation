---
status: Read
paper: LIT-tmp18mi5
title: 'Sullivan, Dulac and others (2025 preprint) — Brain-immune interactions generate pathogen-specific sickness states'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 for the reading pass the owner asked for ("read the
    works you can reach"), from a reader's draft the filer verified against
    the downloaded text. Copy and extent: - Europe PMC full-text XML of
    PMC12713759 (the preprint as deposited in PMC; JATS article-type
    "original-preprint"), via
    https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12713759/fullTextXML,
    fetched 2026-11-12, converted to text. Read: abstract, introduction, all
    Results sections, Discussion, "Limitations of the study", figure
    captions. Skimmed by heading only: Methods (models, assays, FOS
    pipeline, MERFISH). Not read: figures and supplementary tables
    themselves, references. Outcome as the reader gave it: **Read** (main
    text in full; Methods skimmed by heading; figures by caption only).
date: '2026-11-12'
summary: >-
  In mice, five sterile immune challenges modelling bacterial infection
  (LPS), viral infection (poly I:C), parasite infection (soluble
  *Toxoplasma* antigen, STAg), allergy (bee-venom PLA2) and colitis (DSS)
  produce distinct "sickness states" at three scales: organismal
  (temperature, food intake, locomotion, metabolism, social behaviour,
  ultrasonic vocalizations), cellular (whole-brain FOS activity, which a
  classifier uses to predict the challenge) and molecular (a 940-gene
  MERFISH atlas of the preoptic and paraventricular hypothalamus). The
  states cluster: LPS with poly I:C; STAg with DSS; PLA2 apart. STAg and DSS
  unexpectedly *increased* social interaction and activated hypothalamic
  "isolation" neurons that promote social drive. The authors conclude the
  brain, like the immune system, represents pathogen classes specifically.
---
<!-- inactive-ok-file: CASE-tmp10ykm CLAIM-tmpoxhqq — Proposed; filed from the same exchange -->
<!-- inactive-ok-file: LIT-tmpk1h9j — Unfetched; filed from the same exchange -->
<!-- inactive-ok-file: THEORY-413 — Proposed; cited as on the record -->
<!-- inactive-ok-file: LIT-tmpawef9 — Deferred; filed from the same exchange -->

# NOTE-tmpm8u4z: Sullivan, Dulac and others (2025 preprint) — Brain-immune interactions generate pathogen-specific sickness states

## Contribution

A multi-scale comparison across challenge types, against the field's
reliance on LPS; evidence against a "generic" brain representation of
infection; a hypothalamic immune-gene atlas as a resource.

## Key results

1. **Specificity across scales (Abstract).** "immune challenges elicited
   unique repertoires of changes across all scales."
2. **Clusters (Discussion, "Pathogen-specific sickness states across
   biological scales").** "one including LPS and pI:C (modeling bacterial and
   viral infection), one including STAg and DSS (modeling parasite infection
   and colitis), and the third, PLA2 (modeling allergic inflammation), most
   distinct from the other conditions".
3. **Pro-social sickness (Results, social behavior).** "STAg- and
   DSS-challenged animals showed significantly higher levels of social
   interaction than did saline controls"; "STAg and DSS elicited fos activity
   in MPNMc4r+ isolation neurons suggesting enhanced social drive."
4. **Brain classifier (Results, brain-wide signatures; Fig. 4).** A
   regularized logistic regression on 36 (male) or 25 (female) selected
   regions predicts the sickness state from FOS; confusion matrices show
   "Clear diagonal dominance".
5. **Against generic representation (Discussion).** The findings "challenge
   the notion of a generic representation of pathogens in the brain."
6. **Adaptive vs pathological undetermined (Limitations).** The sterile
   models do not "enable us to address which changes we observe are adaptive
   versus pathological"; doses could not be equated across compounds.

## Assumptions

Sterile ligands stand in for pathogens; FOS indexes neural activation; a
single time point per assay (4 h, or day 3 for DSS) represents the state;
the targeted MERFISH library captures relevant genes.

## Concepts

Sickness behaviour; pathogen-associated molecular patterns and pattern
recognition receptors; type-1 vs type-2 immunity; sickness state; whole-brain
FOS mapping; MERFISH spatial transcriptomics; hypothalamic social-need
circuits (isolation and reunion neurons).

## Bearing on the record

**On the LIT's and the exchange's characterization.** A21's account ("a preprint reporting that different inflammatory challenges
elicit distinct behavioural, brain-activity and hypothalamic transcriptional
sickness states in mice") is **accurate**, including "preprint".

- **[CLAIM-tmpoxhqq](../claims.d/CLAIM-tmpoxhqq.md)** (manipulating parasites control host behaviour through
  the host's own machinery; evolutionary goal-directedness and causal
  control come apart from intentional agency; host execution does not show
  the host's governance is independent): **qualifies, by supplying the
  rival that has to be ruled out**. The challenges are sterile, so every
  behavioural change here is generated by the *host's* own detection and
  response programmes, none by a pathogen acting. Yet the changes are
  pathogen-specific, and STAg, a *Toxoplasma* preparation, increased social
  interaction. So pathogen-specific behaviour change, even one that might
  favour a parasite's spread, is not by itself evidence of manipulation
  (sense 2 of the claim): host sickness programmes produce it too, and the
  claim's step 2 needs evidence that the change serves the parasite and is
  caused by its adaptations rather than the host's. This supports the
  claim's caution at its first step and complicates inferences in [CASE-tmp10ykm](../cases.d/CASE-tmp10ykm.md).
  The paper itself does not discuss manipulation; the link is the record's
  inference.

Other held entries it bears on (found on recheck):
- **[CASE-tmp10ykm](../cases.d/CASE-tmp10ykm.md)** (on the branch: *Toxoplasma* and ant-manipulating
  fungi): the STAg pro-social result is a host response to parasite antigen
  without live parasite; relevant to separating host defence from
  manipulation in the *Toxoplasma* case.
- **[LIT-tmpk1h9j](../literature.d/LIT-tmpk1h9j.md)** (Sparling, Florsheim and Sullivan 2026, "Scaling immunity:
  sickness as a host defense strategy", branch, unread) and
  **[LIT-tmpawef9](../literature.d/LIT-tmpawef9.md)** (*C. elegans* sickness behaviour, branch, unread): same
  line of work; the Trends commentary may restate this preprint's thesis.
- **[THEORY-413](../theory.d/THEORY-413.md)** (beneficiary among the roles of a unit of selection): the
  authors' framing is that sickness states are host adaptations (host as
  beneficiary), with adaptiveness explicitly not yet tested.

Searched origin/main and the branch for: sickness behavio(u)r, Toxoplasma,
Dulac, neuroimmune, the DOI. Main holds nothing on these; the branch holds
[CASE-tmp10ykm](../cases.d/CASE-tmp10ykm.md), [LIT-tmpk1h9j](../literature.d/LIT-tmpk1h9j.md) and [LIT-tmpawef9](../literature.d/LIT-tmpawef9.md). **Not already held** under
another LIT ([LIT-tmpk1h9j](../literature.d/LIT-tmpk1h9j.md) is a different, related work by an overlapping
author).

## Limitations

Preprint, not peer reviewed; sterile models, not live infections; single
time points; non-equivalent doses; mice only; correlational at the neural
level (no circuit manipulation linking the hypothalamic changes to the
behaviours); adaptiveness not assessed.
