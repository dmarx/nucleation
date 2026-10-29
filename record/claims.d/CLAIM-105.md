---
number: 105
status: Proposed
formerly:
- CLAIM-tmpukbg3
title: 'In documented reconstruction chains, steps that keep most local judgements commonly change their global compatibility: translation preserves local meanings while changing the global structure of meaning'
version: 4
history:
- version: 2
  date: '2026-10-10'
  note: >-
    Restated on 2026-10-10 after CLAIM-238, CLAIM-219 and
    CLAIM-245. Version 1's 'always carries' could not be
    established by a study, and read of exact preservation it holds by
    definition, since global compatibility is a function of the local
    tables. The restatement concerns steps that keep most contexts, and
    allows for signalling and for coding (CLAIM-245).
    CLAIM-219 is conceded; CLAIM-201 states the form the data
    leave open. The manuscript's text quoted below is unchanged. Version
    1's condition read: "Across reconstruction chains, preservation of
    the context-wise judgement distributions always carries preservation
    of their global compatibility (overlap consistency, global
    extension, contextual fraction), so that the global structure adds
    nothing to predict."
- version: 3
  date: '2026-10-19'
  note: >-
    Title restated on 2026-10-19 by the promotion audit, batch 034
    (ADR-047). Version 2 made the defeat condition a prevalence test
    over documented chains after CLAIM-238, and the split of
    2026-10-15 moved the constructed possibility to CLAIM-320, but
    the title kept the possibility's "may" and "can". It now states
    the thesis about documented chains that the condition tests; the
    defeat condition is unchanged. Version 2's title read:
    'Translation may preserve local meanings while changing the
    global structure of meaning: reconstruction can keep most local
    judgements and change their global compatibility'. Status and
    warrant unchanged.
- version: 4
  date: '2026-10-29'
  note: >-
    Eleventh status review (ADR-057, ADR-059). CLAIM-235, an Active
    counter to this claim since 2026-10-10, was written into version 2's
    defeat condition without being named there. The contextual
    fraction is defined only without signalling, and raw tables
    signal, so the condition tests contextuality in the
    Contextuality-by-Default sense, with signalling accounted for and
    changes counted beyond sampling error. 'What the reading of the
    contextual fraction implies' gives the undefinedness. No other
    change.
role: thesis
warrant: interpretive
defeated_if: >-
  In documented reconstruction chains, with signalling accounted for and
  the coding of outcomes fixed in advance, steps that keep the judgement
  distributions of most contexts within sampling error change neither
  global extendability nor contextuality in the Contextuality-by-Default
  sense beyond sampling error, except at a rate no greater than one
  fixed in advance.
tags:
- contextuality
- philosophy-of-language
date: '2026-10-08'
line: pragmatic-transport
works:
- what-survives-translation
rests_on:
- CLAIM-038
- CLAIM-320
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
- CLAIM-219
- CLAIM-235
- CLAIM-238
complements:
- CLAIM-201
bears_on:
- QUESTION-004
---
<!-- inactive-ok-file: CLAIM-201 — Proposed; the narrowing of the headline after the audit, cited in the history -->
<!-- inactive-ok-file: THEORY-174 — Proposed; classical simulations never create contextuality, cited for what it implies here, not as settled -->
<!-- inactive-ok-file: CLAIM-005 — Proposed; open, and cited as open: the claim, argument or reading is under test, not settled -->

# CLAIM-105: In documented reconstruction chains, steps that keep most local judgements commonly change their global compatibility: translation preserves local meanings while changing the global structure of meaning

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

## Note of 2026-10-10: a documented case

[CLAIM-201](CLAIM-201.md), this headline's narrowing to a change of cover, now has a
documented case, [CASE-072](../cases.d/CASE-072.md): Hafez's "Shirazi Turk", whose ungendered
beloved four English translators render as a maid, as God and as a boy.
It shows a rendering deciding what the source left open, on the question
of who is addressed. It supplies nothing for this entry's own form, a
change of global compatibility at small local distortion within a fixed
scenario: it has no contextual data and no measured distortion, and its
evidence is translators' and scholars', not readers' agreement.

## Note of 2026-10-10: a documented case

[CASE-053](../cases.d/CASE-053.md), found by a search the owner asked for, collects the
documented tests of contextuality on elicited human judgements. It supplies
the evidence that this headline's fixed-scenario form still lacks a case:
no study of pragmatic or meaning judgements finds contextuality proper at an
adequate sample size. [LIT-264](../literature.d/LIT-264.md) and Wang's thesis (2024) find none;
Lo, Sadrzadeh and Mansfield's Winograd schemas (2023), the one test with
pragmatic content, find a violation of about one standard deviation, with
no-signalling forced by the response format. The positive results that are
reliable, Cervantes and Dzhafarov's "Snow Queen" and its follow-up, have
instructed matching as content, not pragmatics, and are disputed. It does
not supply a contextual model for this entry, and it does not show that
none exists: what it documents is that the adequate test has not been
run. A powered rerun of Lo et al.'s design, under CbD, is what would
decide the fixed-scenario form, and could be the contextuality arm of
[CASE-055](../cases.d/CASE-055.md).

## Note of 2026-10-15: split under [ADR-043](../decisions.d/ADR-043.md)

[ADR-043](../decisions.d/ADR-043.md)'s full classification found this claim compound: that a
reconstruction can keep most local judgements and change their global
compatibility is shown possible by a constructed pair, [CASE-037](../cases.d/CASE-037.md) with one
context changed, which is demonstrated, while that documented
reconstruction chains do this, which is what the defeat condition
tests, has no observation under it, so it is interpretive. The
constructed possibility is now [CLAIM-320](CLAIM-320.md) (demonstrated), on which this claim
rests. This claim keeps the thesis about translation and reconstruction
chains, and its measures. Its title states that thesis and is kept; its
warrant stays interpretive.

## Note of 2026-10-19: the title restated as prevalence

The promotion audit's batch 034 found the title behind its own defeat
condition. The condition tests a rate over documented reconstruction
chains, after [CLAIM-238](CLAIM-238.md), and the note above moved the constructed
possibility to [CLAIM-320](CLAIM-320.md). The title still said translation "may" do
this and reconstruction "can", which [CLAIM-320](CLAIM-320.md)'s pair already settles.
It now states the thesis this entry keeps, about documented chains. The
manuscript's wording quoted above is unchanged. The warrant stays
interpretive: [CASE-053](../cases.d/CASE-053.md) documents that the adequate test has not been
run.

## Note of 2026-10-29: what holds it back

Its defeat condition counts
changes beyond sampling error, which needs a signalling estimator with bias
correction and a stated sampling error, and [CLAIM-235](CLAIM-235.md) finds none in the
line. [CASE-053](../cases.d/CASE-053.md) documents that no adequately powered CbD test on pragmatic
judgements has been run.
