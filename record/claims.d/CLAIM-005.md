---
number: 5
status: Proposed
formerly:
- CLAIM-tmp0wmy3
title: 'Pragmatic fidelity is the match between distributions of context-indexed communicative judgements across a correspondence of source and target contexts, not the similarity of one canonical meaning vector'
version: 1
role: thesis
defeated_if: >-
  Embedding or propositional similarity between source and rendering
  predicts held-out human communicative-fidelity judgements as well as
  the context-indexed distribution distance does.
tags:
- philosophy-of-language
- probabilistic-modeling
date: '2026-10-08'
line: pragmatic-transport
works:
- what-survives-translation
answers:
- QUESTION-001
uses:
- TERM-021
summary: >-
  A24's D(τ), the origin of the transport framework, and the
  manuscript's L_obs (§6). One of three terms of the manuscript's
  fidelity functional.
objected_by:
- CLAIM-tmp6xxbf
- CLAIM-tmpdwfva
- CLAIM-tmpgetbr
- CLAIM-tmphn6za
- CLAIM-tmpqfgjl
- CLAIM-tmpwvljf
complements:
- CLAIM-tmp351uu
- CLAIM-tmpeqvy4
- CLAIM-tmpx3m7e
---
<!-- inactive-ok-file: CLAIM-105 — Proposed; open, and cited as open: the claim, argument or reading is under test, not settled -->
<!-- inactive-ok-file: CLAIM-117 — Proposed; open, and cited as open: the claim, argument or reading is under test, not settled -->
<!-- inactive-ok-file: CLAIM-tmp351uu CLAIM-tmpeqvy4 CLAIM-tmpx3m7e — Proposed; the distinctive test and the two restatements of this measure, cited as open -->

# CLAIM-005: Pragmatic fidelity is the match between distributions of context-indexed communicative judgements across a correspondence of source and target contexts, not the similarity of one canonical meaning vector

## The claim

A24: "we evaluate whether the translation preserves the pattern of
context-dependent communicative judgments, rather than whether it preserves one
canonical vector of meaning", with D(τ) = Σ_C w_C d(e_C^source,
e_τ(C)^target) ([TERM-021](../terms.d/TERM-021.md)). Manuscript §6: L_obs(T) = Σ_C w_C d_C[(K_C)#e_C^o,
e_τ(C)^t]. §10 Case I's success criterion is its defeat condition turned round:
"incremental prediction of held-out human communicative-fidelity judgments".

The form that reached the manuscript is A78's D_sheaf (U29):
Σ_C w_C d_C(T_C# e_i(C), e_(i+1)(τ(C))), "a graded, directed measure of
preservation of local observational structure", stated over the sheaf
scenario's contexts ([CLAIM-105](CLAIM-105.md)).

## What it does not say

A24's caveats: "the outcome categories must be made comparable across contexts,
and the correspondence between contexts cannot be assumed." It is not the whole
of fidelity: the manuscript adds a structural term and a decision term, and the
dynamical requirement is [CLAIM-117](CLAIM-117.md).

## Note of 2026-10-10: the contexts must be as fine as the pairing

A181 §4, after the owner's U50 pointer to FID: a generator may produce "the
correct overall proportions of smiling and stern-looking faces, but
assign[] them to the wrong prompts", and "Even a perfect measure of the
unconditional image distribution cannot detect a generator that preserves
the overall distribution while breaking the association between prompts
and images". An unconditional distance cannot see a transformation that
keeps the output distribution and breaks the pairing of inputs with
outputs.

D(τ) is context-indexed, so it is not unconditional. But the failure
returns inside a context. Within any context C that pools several source
items, a target that permutes their renderings leaves e_τ(C)^target
unchanged. So the contexts must be at least as fine as the pairing that
fidelity is meant to track. This is elementary, and the manuscript's L_obs
inherits it. The case beside it is [CASE-041](../cases.d/CASE-041.md).

## Note of 2026-10-10: the replies

After the audit ([CLAIM-tmp6xxbf](CLAIM-tmp6xxbf.md), [CLAIM-tmpflbi3](CLAIM-tmpflbi3.md), [CLAIM-tmpwvljf](CLAIM-tmpwvljf.md)): for one
item, L_obs can be made zero by a constant kernel, so it is restated over a
class of items with one kernel family, fitted on some items and scored on
others ([CLAIM-tmpeqvy4](CLAIM-tmpeqvy4.md)), and over both covers, with the target's new
questions asked of the source too ([CLAIM-tmpx3m7e](CLAIM-tmpx3m7e.md)). Its distinctive test
against a static pragmatic profile is [CLAIM-tmp351uu](CLAIM-tmp351uu.md). The manuscript's
text quoted above is unchanged.
