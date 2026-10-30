---
number: 5
status: Proposed
formerly:
- CLAIM-tmp0wmy3
title: 'Pragmatic fidelity is the match between distributions of context-indexed communicative judgements across a correspondence of source and target contexts, not the similarity of one canonical meaning vector; the match constrains a translation only once one outcome correspondence is fixed across many items, and summed over source contexts alone it charges for loss and not for addition'
version: 3
history:
- version: 2
  date: '2026-10-29'
  note: >-
    Narrowed at the seventh status review (ADR-057, ADR-059) to record
    two granted objections. CLAIM-207: for one source–target pair a
    constant kernel makes L_obs zero and satisfies naturality, so the
    match constrains a translation only once one kernel family is
    fixed across many items. CLAIM-256: L_obs and D_obs sum over
    source contexts only, so a target context outside the image of τ
    appears in no term. Version 1's title read: Pragmatic fidelity is
    the match between distributions of context-indexed communicative
    judgements across a correspondence of source and target contexts,
    not the similarity of one canonical meaning vector. The repaired
    measures stay CLAIM-228 and CLAIM-257, Proposed; this claim does
    not rest on them. The defeated_if is unchanged.
- version: 3
  date: '2026-10-29'
  note: >-
    Defeat condition restated at the seventh status review, after the
    narrowing above. CLAIM-207: the distance is computed with one
    outcome correspondence fixed across a class of items and scored on
    held-out items, or a constant kernel passes it. CLAIM-238: a
    margin and a power are fixed before the data. CLAIM-226: the
    judges are a named population. Version 1's condition read:
    Embedding or propositional similarity between source and rendering
    predicts held-out human communicative-fidelity judgements as well
    as the context-indexed distribution distance does. CASE-184,
    CLAIM-233 and ARG-026 quote that version.
role: thesis
warrant: interpretive
defeated_if: >-
  Embedding or propositional similarity between source and rendering
  predicts held-out communicative-fidelity judgements, by a named
  population of judges, as well as the context-indexed distribution
  distance does, computed with one outcome correspondence fixed across a
  class of items and scored on held-out items, within an equivalence
  margin and at a power fixed before the data.
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
- CLAIM-207
- CLAIM-226
- CLAIM-244
- CLAIM-256
complements:
- CLAIM-202
- CLAIM-228
- CLAIM-257
---
<!-- inactive-ok-file: CLAIM-105 — Proposed; open, and cited as open: the claim, argument or reading is under test, not settled -->
<!-- inactive-ok-file: CLAIM-117 — Proposed; open, and cited as open: the claim, argument or reading is under test, not settled -->
<!-- inactive-ok-file: CLAIM-202 CLAIM-228 CLAIM-257 — Proposed; the distinctive test and the two restatements of this measure, cited as open -->

# CLAIM-005: Pragmatic fidelity is the match between distributions of context-indexed communicative judgements across a correspondence of source and target contexts, not the similarity of one canonical meaning vector; the match constrains a translation only once one outcome correspondence is fixed across many items, and summed over source contexts alone it charges for loss and not for addition

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

After the audit ([CLAIM-207](CLAIM-207.md), [CLAIM-230](CLAIM-230.md), [CLAIM-256](CLAIM-256.md)): for one
item, L_obs can be made zero by a constant kernel, so it is restated over a
class of items with one kernel family, fitted on some items and scored on
others ([CLAIM-228](CLAIM-228.md)), and over both covers, with the target's new
questions asked of the source too ([CLAIM-257](CLAIM-257.md)). Its distinctive test
against a static pragmatic profile is [CLAIM-202](CLAIM-202.md). The manuscript's
text quoted above is unchanged.

## Note of 2026-10-29: narrowed

The title now carries [CLAIM-207](CLAIM-207.md) and [CLAIM-256](CLAIM-256.md) instead of leaving them to the
note of 2026-10-10. For one pair the kernel can make the match perfect
whatever the translation did, and what a rendering adds is in no term. The
contrast with one canonical meaning vector stands.

## Note of 2026-10-30: what holds it back

The defeat condition still cannot tell this claim from its rivals. Version
3 fixed a margin and a power before the data (CLAIM-238), a named
population of judges (CLAIM-226) and one outcome correspondence across
items (CLAIM-207), but it still sets the distance only against embedding or
propositional similarity. Two rivals the record holds, Nida's dynamic
equivalence and a proposition with its illocutionary force, also predict a
pass (CLAIM-233, narrowed on 2026-10-30), and so does Gutt's interpretive
resemblance (CLAIM-501, Active). CLAIM-244 (Proposed, unanswered) objects
that the condition takes a task-free holistic judgement as ground truth.
Restating it is put to the owner, with the other defeat conditions queued
for restatement.
