---
number: 105
status: Proposed
formerly:
- CLAIM-tmpukbg3
title: 'Translation may preserve local meanings while changing the global structure of meaning: reconstruction can keep most local judgements and change their global compatibility'
version: 1
role: thesis
defeated_if: >-
  Across reconstruction chains, preservation of the context-wise
  judgement distributions always carries preservation of their global
  compatibility (overlap consistency, global extension, contextual
  fraction), so that the global structure adds nothing to predict.
tags:
- contextuality
- philosophy-of-language
date: '2026-10-08'
line: pragmatic-transport
works:
- what-survives-translation
answers:
- QUESTION-004
rests_on:
- CLAIM-038
grounds:
- LIT-265
- THEORY-165
summary: >-
  A78's thesis for the paper, "potentially the most interesting
  connection we've found", with Δ_CF, the change in contextual fraction
  along a chain, as its measure. The manuscript keeps the thesis as its
  Abstract's last sentence but drops the measure and the worked examples
  (at C6, per the chunk-5 reader).
illustrated_by:
- CASE-037
objected_by:
- CLAIM-tmpbvk4j
- CLAIM-tmpji66i
- CLAIM-tmplkh2i
---
<!-- inactive-ok-file: THEORY-165 — Proposed; continuity of the contextual fraction, cited for what it implies here, not as settled -->
<!-- inactive-ok-file: THEORY-174 — Proposed; classical simulations never create contextuality, cited for what it implies here, not as settled -->
<!-- inactive-ok-file: CLAIM-005 CLAIM-038 — Proposed; open, and cited as open: the claim, argument or reading is under test, not settled -->

# CLAIM-105: Translation may preserve local meanings while changing the global structure of meaning: reconstruction can keep most local judgements and change their global compatibility

## The claim

A78: "This opens a novel research question: **Can communicative reconstruction
preserve most local pragmatic judgments while substantially changing their
global compatibility structure?** That would be much stronger than showing that
a telephone-game chain progressively changes its vocabulary or apparent speaker
stance." And: "**Translation may preserve local meanings while changing the
global structure of meaning.** That is a nontrivial, formally expressible
distinction—and potentially the most interesting connection we've found between
pragmatic translation and the sheaf-theoretic contextuality literature."

Its measures: D_sheaf(T) = Σ_C w_C d_C(T_C# e_i(C), e_(i+1)(τ(C))), "a graded,
directed measure of preservation of local observational structure", which is
the form of the manuscript's L_obs ([CLAIM-005](CLAIM-005.md)); and
Δ_CF = CF(e_(i+1)) − CF(e_i), the change in contextual fraction, "for
measurement scenarios to which the measure applies" (Abramsky, Barbosa and
Mansfield; [LIT-265](../literature.d/LIT-265.md) in the record, unread).

Manuscript Abstract: "The theory predicts when local content can survive while
the global pattern of communicative relationships changes." §11: "A transport
may preserve overlaps but change the available measurement cover."

Proposal v5 (U30) kept it: A81 §5.5, A82 §8.7 ("Distinguish increased ambiguity
from an increase in formal contextuality"), and A84's planned Appendix F
example, "Two locally similar empirical models with different global
compatibility". A81 §4.4 set the contextual fraction's role: "an observable
structural descriptor rather than ... the definition of translation fidelity".

## What was lost

Δ_CF and the worked example of two locally similar models with different global
compatibility. The chunk-5 reader finds both dropped at C6 when Appendix F
replaced the finite examples with a protocol, without critique. The manuscript's
Proposition 2 says when a global extension is preserved; nothing in it shows a
case where it is not.

C7 Appendix B states the limit a drift result would meet here: "A result about
state distributions is not automatically a result about a discontinuous
contextuality measure, whose stability requires separate assumptions." The
contextual fraction is such a measure.

## What the reading of the contextual fraction implies

The contextual fraction is now read ([LIT-265](../literature.d/LIT-265.md), [NOTE-236](../notes.d/NOTE-236.md)). Three consequences
for Δ_CF:

- **It is undefined at some steps.** Δ_CF is undefined at any step that makes
  the marginals depend on context, because the contextual fraction is defined
  only without signalling.
- **It cannot rise along free operations.** By the paper's Theorem 2, a free
  operation (relabelling, restriction or translation of measurements,
  coarse-graining, mixing with a noncontextual model) cannot raise the
  fraction. So Δ_CF ≤ 0 along such steps, and an increase needs a step of
  some other kind.
- **It does not jump within a scenario.** The premise quoted here, that the
  fraction is discontinuous, does not hold within a fixed scenario: it is
  Lipschitz in the probability table ([THEORY-165](../theory.d/THEORY-165.md), a derivation from the
  paper's linear programme). Only a change of scenario can make it jump.

## Note of 2026-10-10: A173's request, and the lost pair recovered

A173 asked the entry to acknowledge that classical transports preserve
noncontextuality. It already does (Theorem 2 of [LIT-265](../literature.d/LIT-265.md); [THEORY-174](../theory.d/THEORY-174.md)). A173's
"not merely to transport itself" holds only for increases. Coarse-graining
or mixing can lower contextuality by transport alone. The lost worked pair
is [CASE-037](../cases.d/CASE-037.md) with one context changed: two models that agree on two of
three contexts and on every marginal, with contextual fraction 1 and 0. The
headline thesis is still absent from v7 (A178), from the second
crystallized argument (A203) and from the October outline (A218).
