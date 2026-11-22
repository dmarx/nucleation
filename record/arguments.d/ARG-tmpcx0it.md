---
status: Proposed
title: "Corominas-Murtra, Hanel and Thurner's induction proof, as a source, carries item 5 of the catalogue of feedback-free power-law mechanisms, the 1 over k visiting law of the uniform sample-space-reducing walk, though not their abstract's claim that such processes necessarily give Zipf's law"
version: 1
form: source
grounds:
- THEORY-tmpcfn5g
concludes:
- CLAIM-795
tags:
- probabilistic-modeling
- complex-systems
date: '2026-11-22'
line:
- formal-apparatus
summary: >-
  Whether Corominas-Murtra, Hanel and Thurner (LIT-2997), read in
  NOTE-tmpyqqhq, carry CLAIM-795's item 5. Their eq. 1, proved by
  induction, is the item exactly: a walk jumping uniformly to a lower
  state visits state k with probability 1/k, with no multiplicative,
  preferential or critical process. The item gains the tunable family
  i^(−λ). The abstract's "necessarily lead to Zipf's law" outruns the
  proof, which covers uniform jumps; the item claims only the uniform
  case. The wording is the assistant's (Claude, in this session); adopting
  it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-795 THEORY-tmpcfn5g ARG-tmp3ppjy — Proposed or new; the claim and the reading this argument joins -->

# ARG-tmpcx0it: Corominas-Murtra, Hanel and Thurner's induction proof, as a source, carries item 5 of the catalogue of feedback-free power-law mechanisms, the 1 over k visiting law of the uniform sample-space-reducing walk, though not their abstract's claim that such processes necessarily give Zipf's law

## The inference

CLAIM-795, item 5: a walk that jumps uniformly to a lower state until it
reaches 1 visits state k with probability 1/k. THEORY-tmpcfn5g: the proof
and the noisy family.

## Critical questions (source)

**Does the work say this, read in context?** Yes. The visiting
probability "can easily be shown to follow an exact Zipf's law,
PN(i) = 1/i" (p. 2, eq. 1), proved by induction on N, and the process is
offered "without the recourse to multiplicative, preferential, or
self-organised critical processes" (abstract). The reader's simulation
and the claim's own both match.

**Is it said within the scope the claim needs?** Yes, for the uniform
process, which is the case item 5 states and its `defeated_if` names.
Not for sample-space reduction in general: the abstract's "necessarily"
is wider than the proof. The claim's label, "sample-space reduction",
should be read as the uniform case.

**Does the claim lean on the reading for more than it holds?** No. It
holds less than the reading offers: the noisy mixture gives
p(i) ∝ i^(−λ), so the route reaches any rank exponent in (0, 1] and any
frequency exponent (1 + λ)/λ ≥ 2, which the item now notes.

## Verdict

Support for item 5. THEORY-tmpcfn5g replaces LIT-2997 in CLAIM-795's
`grounds`; the item no longer rests on the claim's own check alone.
ARG-tmp3ppjy's finding that Newman does not carry item 5 stands.
