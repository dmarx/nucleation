---
status: Read
paper: LIT-tmppyl6o
title: 'Sikder — FairCert: Certifiable Error Rate Fairness for ML and LLM Decision Systems'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 for the reading pass the owner asked for ("read the
    works you can reach"), from a reader's draft the filer verified against
    the downloaded text. Copy and extent: - Read: PMLR PDF,
    `https://raw.githubusercontent.com/mlresearch/v350/main/assets/sikder26a/sikder26a.pdf`
    (linked as `citation_pdf_url` from
    `https://proceedings.mlr.press/v350/sikder26a.html`), fetched
    2026-11-12, converted with pdftotext. - Read: abstract, introduction and
    contributions, related work, §3 (framework, subgroup discovery,
    black-box evaluation, certificates incl. Proposition 3.1, permutation
    test, bootstrap, calibration and compliance, multi-class), experiments
    (COMPAS, ACS Income, other tabular, vision, multi-class, subgroup
    discovery, three-method comparison, scale ablation, prompt/temperature
    ablation), discussion, limitations, conclusion. Skipped: references; the
    supplementary material (full proofs, full tables, prompts) on GitHub;
    Tables 2–9 numbers came through garbled and were read only via the
    text's own reporting. Outcome as the reader gave it: **Read** (full
    paper; tables' numeric contents only partly legible in text extraction;
    supplementary material not read).
date: '2026-11-12'
summary: >-
  FairCert is a black-box audit pipeline that turns per-group
  false-positive-rate (FPR) and true-positive-rate (TPR) gaps into
  finite-sample certificates. Five stages: a stratified split with a
  walled-off 15% audit set; LLM-guided discovery of candidate intersectional
  subgroups from aggregate training statistics (hypotheses), confirmed on
  the disjoint audit set; per-group error rates of the classifier's
  predictions; a certificate built from Clopper-Pearson exact intervals per
  group with a Bonferroni correction over K groups, which bounds the worst
  pairwise gap with probability at least 1−δ and passes if the bound is
  within tolerance ε; and, for failures, per-group threshold calibration
  with the TPR cost reported, plus a structured EU AI Act-oriented report. A
  permutation test (permuting group labels among actual negatives only,
  valid under differing base rates) and a bootstrap are offered as
  exploratory, not certifying. Experiments on eight datasets (COMPAS, ACS
  Income binary and 3-class, Credit Default, Law School, Bank Marketing,
  FairFace, UTKFace) with ML classifiers, seven open LLMs (3B–30B) and two
  image models show: certification depends heavily on sample size; LLM
  fairness is domain-dependent; intersectional groups can fail where single
  attributes pass; scale improves LLM accuracy but not fairness.
---
<!-- inactive-ok-file: LIT-tmpv9xn3 — Unfetched; filed from the same exchange -->

# NOTE-tmppe0ip: Sikder — FairCert: Certifiable Error Rate Fairness for ML and LLM Decision Systems

## Contribution

An assembly, explicitly not new statistics ("FairCert does not introduce new statistical tools"), of exact binomial intervals, family-wise correction and permutation inference into an audit that yields a pass/fail certificate at stated tolerance and confidence, applied to LLM classifiers and intersectional groups, with an LLM used only to propose subgroups.

## Key results

1. Abstract: "A small FPR gap on one test set does not certify a classifier as fair. A point estimate has no confidence bound, so the observed gap may just be sampling noise."
2. §3.4, Proposition 3.1: with Clopper-Pearson intervals at α′ = δ/K, "if ∆FPR ≤ ε, then the classifier is certified at tolerance ε with confidence 1 − δ." (Proof sketch by Bonferroni's inequality; full proof in the supplement.)
3. §3.4.2: the permutation guarantee "is conditional on H0 (unlike Bonferroni’s unconditional CIs)".
4. Abstract: "Mistral-24B has an FPR gap of 0.259 on COMPAS but only 0.009 on ACS Income."
5. Abstract: "On Credit Default dataset, certification passes for a single sensitive attribute but fails in the intersectional settings." (Text: Bonferroni bound 0.064 fails at ε = 0.05 for K = 4, sex × age.)
6. ACS Income: "With 29, 350 audit samples (37x COMPAS), all classifiers pass certification at all ε levels".
7. Scale ablation: "Only the 3B model passes certification, trivially due to near-random predictions."
8. Subgroups: LLM-discovered "Caucasian females with high priors" (FPR=1.0, n = 13) is "too small for formal certification" and treated as exploratory.
9. Prompt sensitivity (Mistral 24B, COMPAS): FPR gaps 0.097 to 0.266 across three templates; "certification outcomes depend on the prompt".
10. Discussion: "General LLM fairness benchmarks are insufficient for regulatory compliance, and each deployment domain requires its own assessment."
11. Calibration: "equalizing FPR costs 9.8% TPR for Black defendants" (COMPAS).

## Assumptions

- The audit set is an i.i.d. sample of the deployment population; group labels are known on it.
- The fairness criterion is fixed in advance as FPR parity / equalized odds; the paper notes Chouldechova's impossibility result but does not justify the choice for each domain.
- ε is supplied externally ("accepting any ε set by notified bodies or domain regulators").
- LLM classifiers are queried deterministically (temperature 0) or over a few seeds; prompt choice is a nuisance factor.
- Degenerate classifiers (positive rate outside 5–95%) are flagged rather than certified.

## Concepts

Error-rate parity (FPR parity, equalized odds); finite-sample certificate; tolerance ε and confidence 1−δ; Clopper-Pearson exact intervals; Bonferroni / union bound; permutation inference within Y = 0; bootstrap inconsistency for the non-smooth max-gap functional; intersectional subgroups and multiple-comparison cost; discover-then-confirm (hypothesis generation vs testing on disjoint data); degeneracy flag; threshold calibration and its TPR cost; EU AI Act Arts 9, 10, 15, 43.

## Bearing on the record

**On the LIT's and the exchange's characterization.** A's account ("finite-sample certificates for error-rate differences across protected and intersectional groups") is **accurate**. It omits that the certificate is conservative (Bonferroni), that small intersectional groups typically cannot be certified at all, that LLMs only propose subgroups, and that the author disclaims statistical novelty.

- **QUESTION-tmpuftum** (how the demand set an organization's compatibility is judged against can be fixed defensibly, when who counts, how demands are inferred and what they mean are shaped by the organization's governance): **bears on all three failures, mostly as illustration; supports the first.**
  1. *Who is represented*: the Credit Default result is a direct, quantified instance of the question's first failure: a demand (FPR parity) met for each single attribute is not certified for the sex × age groups. The paper adds a second mechanism the question does not name: small groups are not refused, they are *uncertifiable* (n_g < 30), so a group can be both at risk and statistically illegible; the auditor's sample size decides whether its demand can be checked at all.
  2. *How demands are inferred*: the LLM-guided discover-then-confirm design is a procedural answer to one part of the worry: group hypotheses generated by one process are tested on data that process did not see. It does not address who chooses the candidate groups' attributes in the first place.
  3. *What demands mean*: the paper fixes the criterion (FPR/TPR parity) and lets ε be set by a regulator; the choice among incompatible criteria (Chouldechova, cited) is outside the tool. It shows how much rides on that choice (calibration buys FPR parity at a reported TPR cost) without resolving it.
- **CLAIM-537** (tolerance-bounded compatibility under disturbance; existence for every disturbance vs one configuration serving all; selection depends on what the agent can read): **leaves open; a statistical analogue only.** FairCert certifies a tolerance (|gap| ≤ ε) under sampling uncertainty, and whether a classifier can be *certified* depends on what the auditor can observe (per-group negatives), not only on the true gap: the same distinction between a property holding and its being selectable/checkable on what one can read. But the paper has no graph, cycles, offsets or adjustable vs non-adjustable configurations; the mapping is by analogy, and the filer should not cite it as support for the claim's conditions.
- **CLAIM-351** (found on recheck: an aggregate can hide unreconciled demands): the single-attribute-pass, intersectional-fail result is a measured case of an aggregate hiding a failing part.
- **LIT-tmpv9xn3** (meta-metrics in intersectional fairness, Deferred) and **LIT-tmp14en7** ("Auditing Predictive Models for Intersectional Biases", Deferred) (found on recheck): the closest held works; FairCert would sit beside them.

Searched record/ (batch ref) for "Sikder/FairCert", "intersectional", "Chouldechova", "equalized odds", "COMPAS", "AI Act", "Clopper/Bonferroni", "gerrymander". Not held under another LIT. Related held: LIT-tmpv9xn3, LIT-tmp14en7 (Deferred), LIT-1331 (Active; recommender epistemic welfare, mentions the AI Act). Hardt et al. (equalized odds), Chouldechova (2017) and Kearns et al. (fairness gerrymandering) were not found as LITs by these searches.

## Limitations

Single-author conference paper; methods are standard; results on standard benchmarks with a fixed split (seed variation only in model training); LLM variance study covers one model; Bonferroni is conservative for large K, so "fail" can reflect conservatism rather than unfairness (the author says so); full proofs and tables are in the supplement, which I did not read; numbers in the tables were not legible in extraction, so only figures stated in the text are quoted.
