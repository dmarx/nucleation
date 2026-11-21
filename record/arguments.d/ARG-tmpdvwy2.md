---
status: Rejected
title: "Lau and colleagues' calibration of the local learning coefficient estimator in deep linear networks supports the reading that an estimate at finite sample size counts unresolved sloppy directions as flat"
version: 1
form: evidence
grounds:
- THEORY-tmpousrw
concludes:
- CLAIM-tmpcg4uu
tags:
- learning-theory
- information-geometry
date: '2026-11-21'
line:
- formal-apparatus
- learned-structure
summary: >-
  CLAIM-tmpcg4uu reads a learning-coefficient estimate at finite n as
  counting unresolved sloppy directions as flat, and cited Lau et al.
  (LIT-tmpnbl2d) unread for the estimate. Read (NOTE-tmp92pjh), the paper
  neither states nor tests that reading. Its calibration underestimates
  mostly, which would fit it, but the authors attribute underestimation to
  an unsettled sampler, and the deep linear networks are not sloppy in a
  known way. Rejected as evidence for the claim; the estimator's form
  supports the claim's reading by derivation (the filer's), not by the
  paper's data. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpcg4uu THEORY-tmpousrw — Proposed or Rejected entries filed on 2026-11-21 from the exchange "Rich Get Richer Power Laws" and from the readings of its works, or Deferred works not yet read -->

# ARG-tmpdvwy2: Lau and colleagues' calibration of the local learning coefficient estimator in deep linear networks supports the reading that an estimate at finite sample size counts unresolved sloppy directions as flat

## The inference

CLAIM-tmpcg4uu, "where they meet (2)": at finite n a direction too sloppy to
resolve contributes to the learning coefficient no more than a flat one,
so a single estimate cannot tell a sloppy regular model from a singular
one. Lau et al. (THEORY-tmpousrw) calibrate their estimator in deep linear
networks, and Fig. J.2's relative errors (λ − λ̂)/λ lie mostly between 0 and
+0.8: the estimate falls short of the exact coefficient, as unresolved
directions counted flat would make it.

## Critical questions

- **Would the evidence be expected if the claim were false?** Yes. "If the
  step size is too low, the sampler may not equilibriate, leading to
  underestimation"; "a slow upwards slope can still be indicative of
  significant underestimation" (App. H). An unsettled sampler explains the
  shortfall without any sloppy direction.
- **Does it tell the claim apart from its rivals?** No. The deep linear
  networks' spectra near their minima are not reported, so whether they
  have directions with curvature below γ log n/n is unknown; nothing in
  the runs varies n, β* or γ, which is what would separate the claim's
  mechanism from sampler bias.
- **Does the measure measure what it is said to?** By its form, yes in the
  claim's sense: on a quadratic loss λ̂ = Σ ½ te_i/(te_i + γ) with
  t = n/log n (NOTE-tmp92pjh, checked by Monte Carlo), so a direction with
  e_i ≪ γ log n/n contributes nothing. That is a derivation from the
  estimator's definition, the filer's, not evidence from the paper; and it
  shows γ is a second cut-off the claim had not named (corrected there).

## Verdict

The paper does not show the claim. Its estimator, analysed, behaves as the
claim says, which the claim may cite as a derivation; its calibration data
do not discriminate. Rejected as evidence. The claim's inverse temperature
(β* = 1/log n, effective sample size n/log n, not "of order n") is
corrected in a dated note there.
