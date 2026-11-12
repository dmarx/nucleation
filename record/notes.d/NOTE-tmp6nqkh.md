---
status: Read
paper: LIT-tmp14en7
title: 'Boxer, McFowland and Neill (2026) — Auditing Predictive Models for Intersectional Biases'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 for the reading pass the owner asked for ("read the
    works you can reach"), from a reader's draft the filer verified against
    the downloaded text. Copy and extent: -
    https://cs.nyu.edu/~neill/papers/tmlr2026.pdf (Daniel Neill's NYU
    faculty page; the TMLR camera-ready, headed "Published in Transactions
    on Machine Learning Research (01/2026)"), fetched 2026-11-12, PDF
    converted with pdftotext. Read: abstract, §1 Introduction, §2 Methods
    (2.1 scan types in full; 2.2–2.4 estimation, scan and permutation test
    read for their structure, not checked in detail), §3 simulation design
    and results, §4 COMPAS case study with Table 3, §5 related work, §6
    limitations, §7 conclusion. Not read: appendices (B simulation details
    and robustness, C.1 full COMPAS tables and benchmark results, C.2 German
    Credit case study), figures (captions only), references. Outcome as the
    reader gave it: **Read** (main text in full; appendices not read).
date: '2026-11-12'
summary: >-
  Models can satisfy a group fairness criterion in aggregate for a protected
  class while being biased against a subgroup of it (e.g. Black women). The
  authors propose Conditional Bias Scan (CBS): for any group-fairness
  definition expressible as conditional independence (separation: P ⊥ A | Y,
  X; sufficiency: Y ⊥ A | P, X; for probabilistic predictions or binarized
  recommendations), estimate each protected individual's expected value
  under the null of no bias, search the exponentially many attribute-defined
  subgroups of the protected class with a multidimensional subset scan for
  the one whose observed values deviate most from that expectation compared
  to the same subgroup in the non-protected class, and test significance by
  permutation to adjust for the search. Semi-synthetic simulations (1,344
  data generating processes) show higher detection accuracy than GerryFair
  and MultiAccuracy Boost, especially for small subgroups. On COMPAS it
  finds, among others, a larger false-positive disparity for Black men than
  for Black defendants overall, gender biases against white women and young
  women, and miscalibration penalizing defendants with no priors.
---
<!-- inactive-ok-file: THEORY-575 THEORY-667 — Proposed; cited as on the record -->
<!-- inactive-ok-file: LIT-tmpv9xn3 — Unfetched; filed from the same exchange -->

# NOTE-tmp6nqkh: Boxer, McFowland and Neill (2026) — Auditing Predictive Models for Intersectional Biases

## Contribution

A flexible, interpretable subgroup auditor for separation and sufficiency
criteria with a multiple-testing correction for the search itself.

## Key results

1. **Problem (Abstract).** "Predictive models that satisfy group fairness
   criteria in aggregate for members of a protected class, but do not
   guarantee subgroup fairness, could produce biased predictions for
   individuals at the intersection of two or more protected classes."
2. **Why a scan (§1).** Fixed-subgroup auditing "does not scale to the
   exponential number of multidimensional subgroups" and "fails to account
   for the risk of identifying many false positives if many subgroups are
   tested".
3. **Simulations (§3.1).** All four CBS variants detect injected bias "with
   higher detection accuracy ... than GerryFair or MultiAccuracy Boost";
   "CBS is better at detecting smaller, more subtle subgroups Sbias than the
   competing methods."
4. **Base-rate shift (§3.1).** With well-calibrated predictions, a base-rate
   difference is picked up by separation scans and not by sufficiency scans,
   in line with Chouldechova (2017).
5. **COMPAS race (§4.1).** "the large FPR disparity of COMPAS against Black
   defendants is even more significant in the intersectional subgroup of
   Black males": FPR 0.44 vs 0.19 for non-Black males (all Black vs non-Black:
   0.42 vs 0.20).
6. **COMPAS calibrated in aggregate but not in a subgroup (§4.1).**
   "predictions are well-calibrated between older and younger defendants, in
   aggregate, but not for the detected subgroup of older males with 0 to 5
   priors."
7. **Not sociological intersectionality (§5.4).** "an intersectional bias
   detected by CBS cannot interchangeably be used to refer to instances of
   sociological intersectionality without further analysis and
   contextualization."
8. **Outcome-label bias (§6).** Re-arrest as the outcome "most likely under-
   and over-represents certain subpopulations of defendants".
9. **Beyond model correction (§6).** "We endorse exploring larger policy
   shifts (not limited to model correction) to address biases that auditing
   tools like CBS might unearth".

## Assumptions

Group fairness as conditional independence; covariates discretized into
categorical subgroups; well-specified propensity and outcome models for the
null expectations; a constant additive log-odds shift as the alternative
(robustness to other shifts checked in simulation); the observed outcome
label is taken as ground truth for the audit (a limitation the authors name).

## Concepts

Separation vs sufficiency; predictions vs recommendations; intersectional vs
contextual bias; multidimensional subset scan; log-likelihood ratio scan
statistic; permutation testing for searched subgroups; GerryFair,
MultiAccuracy Boost, Bias Scan; aggregate fairness hiding subgroup bias.

## Bearing on the record

**On the LIT's and the exchange's characterization.** A42's account ("proposes Conditional Bias Scan for detecting intersectional
subgroup biases that aggregate fairness checks miss") is **accurate**.
Attribution to Neill alone is incomplete (Boxer is first author).

- **QUESTION-tmpuftum** (how the demand set an organization is judged against
  can be fixed defensibly, when who counts as a claimant is shaped by the
  organization): **supports the question's first failure mode and offers a
  partial procedure**. The paper is a worked instance of "An aggregate can
  hide a small group's failure": aggregate calibration or error-rate parity
  can coexist with a significant subgroup violation (results 5, 6). CBS is a
  procedure that searches all attribute-defined subgroups rather than fixing
  them in advance, with a correction for that search, which partly answers
  "who is represented" without the auditor choosing the subgroups. It does
  not answer the question: the protected attribute, the covariates that
  define subgroups and the fairness definition (separation or sufficiency)
  are still chosen by the auditor, and the outcome label may itself be
  biased by the institution (result 8), which is the question's worry that
  the evidence is shaped by the governance being judged.

Other held entries it bears on (found on recheck):
- **CLAIM-351** (a zero aggregate gradient does not show the demands it
  aggregates are reconciled; nonzero gradients can cancel): the same
  structure in fairness auditing: aggregate parity can hide offsetting
  subgroup violations.
- **CLAIM-361** (relief judged against a fixed reference set): CBS's
  protected class and covariates are such a fixed reference set; the paper
  does not discuss how it is chosen.
- **CLAIM-404** (governance through the evidence an organization's
  procedures receive): result 8, re-arrest as outcome, is evidence shaped by
  the policing being evaluated.
- **THEORY-575** (organized vs feature social groups): CBS subgroups are
  feature groups defined by attribute values; the authors' §5.4 caution
  parallels the distinction.
- **LIT-tmpv9xn3** (meta-metrics in intersectional fairness, branch, unread):
  the neighbour on the same question from the same exchange.

Searched origin/main `record/` for: COMPAS (case-sensitive: only NOTE-723,
in passing), intersectional (THEORY-575, THEORY-667, LIT-486, social
ontology), subset scan and Chouldechova (none), fairness (unrelated uses).
Found CLAIM-351 as the closest structural analogue. **Not already held**:
no LIT carries this title or URL; the record holds no algorithmic-fairness
methods paper.

## Limitations

Audits only group-level conditional-independence criteria (not individual or
counterfactual fairness); depends on model specification for null
expectations; COMPAS data issues (race coding, missing inputs, biased
outcome label); simulations use the authors' generative schemes; appendices
(including German Credit results) not read here.
