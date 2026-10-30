---
number: 1151
status: Active
formerly:
- THEORY-tmpt1otv
title: 'A learned translation metric trained with synthetic hallucinations and diagnostic perturbations alongside human MQM flags most injected localized critical errors (all but 0 to 17 percent, by type and model size) and ranks fully detached hallucinations below other translations with AUROC up to 0.96, and without a reference it ranks hallucinations better than with one; how far this reflects the synthetic training data has not been separated from how far it generalises'
version: 2
history:
- version: 2
  date: '2026-10-30'
  note: >-
    Promoted by the twenty-second status review, at the status
    review's ruling (the owner delegated these rulings; ADR-065): the
    title reports what one study measured, with its hedge on
    generalisation kept, and NOTE-1341 read the paper in full. What
    the condition asked beyond the title, whether detection
    generalises past what training synthesised, moves to
    QUESTION-345, which this entry now bears on. The old
    promote_when: "Tests on errors and hallucinations produced by real
    translation systems in language pairs and kinds the training data
    did not synthesise (for instance a multilingual hallucination
    benchmark, or naturally occurring number and entity errors with
    human labels), showing whether detection stays at the level the
    synthetic tests report. Results on more synthetic perturbations of
    the trained kinds do not settle it."
tags:
- translation
date: '2026-10-29'
source:
- LIT-1816
bears_on:
- QUESTION-345
summary: >-
  Guerreiro et al. (TACL 2024), [LIT-1816](../literature.d/LIT-1816.md), §7 (Tables 6 and 8, Fig. 4),
  read in [NOTE-1341](../notes.d/NOTE-1341.md). Localized errors are SMAUG perturbations of
  English references; hallucinations are one de-en benchmark of real
  system outputs. The training data includes synthetic detached and
  oscillatory hallucinations and DEMETR perturbations. The localized-error
  table's "All" row is inconsistent with its rows. The larger model is
  worse on oscillatory hallucinations. Active as a report (ADR-065);
  whether detection generalises is QUESTION-345.
---

<!-- inactive-ok-file: QUESTION-345 — Open; the question this report leaves, cited as open -->

# THEORY-1151: A learned translation metric trained with synthetic hallucinations and diagnostic perturbations alongside human MQM flags most injected localized critical errors (all but 0 to 17 percent, by type and model size) and ranks fully detached hallucinations below other translations with AUROC up to 0.96, and without a reference it ranks hallucinations better than with one; how far this reflects the synthetic training data has not been separated from how far it generalises

## Source

Guerreiro et al. (2024), [LIT-1816](../literature.d/LIT-1816.md), §7 (pp. 987–989) of TACL 12; read in
[NOTE-1341](../notes.d/NOTE-1341.md).

## What was actually shown

**Localized errors.** SMAUG inserted text, negations, mask in-fills, number
swaps and named-entity swaps into WMT23 zh-en and he-en synthetic
references the metric had scored error-free. The share of perturbed
translations still predicted error-free ranges from 0.00% (he-en number
swaps, XXL) to 17.0% (zh-en mask in-fill, XXL) (Table 6, p. 987). The
predicted spans overlap the perturbation in 98% (XL) and 90.9% (XXL) of
cases (p. 987). Negation and number errors bring median score drops of
about 20 points (Fig. 4b, p. 988).

**Hallucinations.** On the de-en benchmark of Guerreiro et al. (2023),
over 3.4k translations by a real system, AUROC for ranking hallucinations
below other translations is 0.890 overall and 0.964 for fully detached
ones with xCOMET-XXL using the reference, and 0.902 overall without it
(Table 8, p. 989). Over 90% of fully detached hallucinations get scores
under 10 (p. 988). The authors attribute the reference-free advantage to
"the metric over-relying on the reference when it is available" (p. 989).

**What could have failed.** Number and entity errors were weaknesses of
earlier COMET metrics (p. 988); xCOMET could have kept them.

## What this does not say

- **That the robustness generalises beyond what was synthesised.** The
  training set includes synthetic detached and oscillatory hallucinations
  and DEMETR's diagnostic perturbations (p. 984), and the authors give
  that as "One plausible hypothesis for these improvements" (p. 988). The
  localized errors are synthetic, on English targets only.
- **That bigger is better here.** XXL is worse than XL on oscillatory
  hallucinations, 0.844 against 0.922 with the reference (Table 8).
- **The overall localized-error rate.** The table's "All" row does not
  agree with the count-weighted mean of its rows ([NOTE-1341](../notes.d/NOTE-1341.md)); the
  per-type figures are the ones to use.
- **That severity is well calibrated.** Within a sentence with several
  predicted spans, severities differ only about 35% of the time (p. 987).
- **Anything about omissions** or partial hallucinations beyond the
  benchmark's aggregate.

## Note of 2026-10-30: promoted

Promoted as a report of what the paper measured ([ADR-065](../decisions.d/ADR-065.md)). Whether its
robustness holds on real errors in pairs and kinds its training did not
synthesise is [QUESTION-345](../questions.d/QUESTION-345.md).
