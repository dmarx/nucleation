---
status: Proposed
title: 'Over a fixed scenario, a change of global compatibility at small local distortion needs contextual judgements, which the behavioural data read so far lack; the form of the headline those data leave open is a change of cover, in which a rendering makes some of the source''s questions undecidable for its readers and decides others the source left open'
version: 1
role: thesis
defeated_if: >-
  In the interlingual and retelling arms of the discriminating study
  (CASE-tmp1uzfn), the contexts on which readers' judgements are
  determinate (agreement above a threshold fixed in advance) are the same
  for source and rendering on all but a share of items no larger than a
  rate fixed in advance.
tags:
- contextuality
- translation
- philosophy-of-language
date: '2026-10-10'
line: 'pragmatic-transport'
grounds:
- LIT-264
- CASE-037
- CASE-tmpxnd3y
complements:
- CLAIM-105
- CLAIM-tmpx3m7e
uses:
- TERM-043
summary: >-
  The record's narrowing, on 2026-10-10, of [CLAIM-105](CLAIM-105.md) after
  [CLAIM-tmpbvk4j](CLAIM-tmpbvk4j.md). It concedes that the record's reading of [LIT-264](../literature.d/LIT-264.md) finds no
  contextual behavioural data, so the fixed-scenario form of "Translation
  may preserve local meanings while changing the global structure of
  meaning" has no case but a constructed one. It shows why the fixed-scenario
  form is sharp and why it needs contextuality. It keeps the form the record
  already names: "Only a change of scenario can make it jump" ([CLAIM-105](CLAIM-105.md)),
  and manuscript §11's "A transport may preserve overlaps but change the
  available measurement cover". A proposal; its test is the discriminating
  study.
---
<!-- inactive-ok-file: CLAIM-105 — Proposed; the headline this claim narrows, open -->
<!-- inactive-ok-file: THEORY-165 — Proposed; continuity of the contextual fraction, cited for its scenario-dependent constant, not as settled -->
<!-- inactive-ok-file: CLAIM-tmpx3m7e — Proposed; the measure of a change of cover, cited as a companion proposal -->

# CLAIM-tmp1rlu5: Over a fixed scenario, a change of global compatibility at small local distortion needs contextual judgements, which the behavioural data read so far lack; the form of the headline those data leave open is a change of cover, in which a rendering makes some of the source's questions undecidable for its readers and decides others the source left open

## The claim

This is the record's reply of 2026-10-10 to [CLAIM-tmpbvk4j](CLAIM-tmpbvk4j.md), and a narrowing
of [CLAIM-105](CLAIM-105.md). The derivation below is decisive and checkable; the claim
that a change of cover is the headline's surviving form is a proposal, to
be tested by the discriminating study ([CASE-tmp1uzfn](../cases.d/CASE-tmp1uzfn.md)).

[CLAIM-105](CLAIM-105.md)'s headline is "Translation may preserve local meanings while
changing the global structure of meaning", in the regime A78 named: "preserve
most local pragmatic judgments while substantially changing their global
compatibility structure". The objection's dilemma takes "global
compatibility" as either contextuality proper or overlap consistency.

## The fixed-scenario form is sharp, but needs contextuality

Within one scenario, global compatibility can change maximally while most
local judgements are kept exactly. Take n odd, n ≥ 3, and observables
a_1, …, a_n with outcomes ±1. The contexts are C_i = {a_i, a_(i+1)} for
i = 1, …, n, indices mod n, so that C_n = {a_n, a_1}. Weight every context
1/n.

- **Model e.** In every context the two observables disagree: the outcomes
  (+, −) and (−, +) each have probability 1/2. A global assignment
  consistent with every context's support would need a_(i+1) = −a_i for
  every i, so going round the cycle a_1 = (−1)^n a_1 = −a_1, since n is odd.
  No ±1 value satisfies that, so no global assignment is consistent with the
  supports. The model is strongly contextual, and its contextual fraction
  is 1.
- **Model e′.** The same, except in C_n, where a_n = a_1: the outcomes
  (+, +) and (−, −) each have probability 1/2. Now the constraints are
  a_(i+1) = −a_i for i = 1, …, n − 1 and a_n = a_1. The first n − 1 give
  a_n = (−1)^(n−1) a_1 = a_1, since n − 1 is even, so they agree with the
  last. The two assignments a_i = s(−1)^(i−1), s = +1 or −1, satisfy every
  constraint. Their equal mixture reproduces every context: in C_i for
  i < n it gives (s(−1)^(i−1), −s(−1)^(i−1)), which is (+, −) or (−, +)
  with probability 1/2 each; in C_n it gives (s, s), which is (+, +) or
  (−, −) with probability 1/2 each. So e′ has a global distribution, and
  its contextual fraction is 0.
- **What changed.** In both models every observable is +1 or −1 with
  probability 1/2 in each context that measures it, so neither signals, and
  overlap consistency is the same. The contexts C_1, …, C_(n−1) are
  identical. C_n changed from support {(+, −), (−, +)} to the disjoint
  support {(+, +), (−, −)}, a total-variation distance of 1. With equal
  weights the weighted observational distortion is D_obs = (1/n) · 1 = 1/n.

For n = 3 this is [CASE-037](../cases.d/CASE-037.md) with the outcomes of one observable relabelled.
So within a fixed scenario the contextual fraction can fall from 1 to 0 at a
weighted local distortion of 1/n, which is as small as one likes for large
n. [THEORY-165](../theory.d/THEORY-165.md) says the fraction is Lipschitz within a scenario and that its
constant "depends on the scenario and is not bounded here". Measured against
weighted D_obs, the example shows the constant is at least n.

The objection's bound, that moving every context by at most ε moves each
overlap discrepancy by at most 2ε, is correct, and the example respects it:
no marginal moves at all. But it concerns overlap consistency and every
context moved a little, not global extension with most contexts kept
exactly. So the second horn does not close the fixed-scenario form.

The first horn does. Every such case needs a contextual model on one side:
here e. The record's reading of the behavioural data has none. [NOTE-235](../notes.d/NOTE-235.md):
"Behavioural data have plenty of the first and, so far, none of the
second", where the second is contextuality proper. So, on the evidence the
record holds, the fixed-scenario form has no case but a constructed one,
and that part of the objection is conceded.

## The form the data leave open: a change of cover

[CLAIM-105](CLAIM-105.md)'s own note says where else the headline can live: the contextual
fraction does not jump within a scenario, and "Only a change of scenario can
make it jump". The manuscript says it in §11: "A transport may preserve
overlaps but change the available measurement cover." A change of cover
needs no contextual data, because it is a change in which questions a
reader can answer at all.

Operationally, a context is a question whose answers readers give
determinately: agreement among them above a threshold fixed in advance. A
rendering changes the cover when a question that is determinate for source
readers is indeterminate for target readers, or the reverse.

- **The target decides what the source left open.** French tu and vous, or
  Japanese honorific marking, oblige the target to settle the
  speaker–addressee relation that an English source can leave open. Target
  readers answer "Are these two intimates?" determinately; source readers do
  not.
- **The source decides what the target cannot.** Villon wrote in criminal
  argot, and Henley rendered it in English underworld slang that is now
  "deliberately opaque" ([CASE-010](../cases.d/CASE-010.md)). Readers inside such a milieu can answer
  an insider question, who among the speakers belongs, that readers outside
  it cannot.

In neither case need any one context's distribution move: the change is in
which contexts exist for which readers. [CLAIM-tmpx3m7e](CLAIM-tmpx3m7e.md) gives the measure,
with the questions only one side can decide reported apart from the
distortion summed over the questions both can.

## What it answers

[CLAIM-tmpbvk4j](CLAIM-tmpbvk4j.md). Its first horn is conceded: no data the record holds are
contextual, so the fixed-scenario headline has no case but a constructed
one. Its second horn's bound is right but beside the headline's regime, as
derived above. Its own second remedy, "a restatement of [CLAIM-105](CLAIM-105.md) about a
change of cover or scenario", is taken.

## What it does not say

- It does not say contextual pragmatic data cannot exist. [LIT-264](../literature.d/LIT-264.md) offers
  their absence as a working hypothesis, and the record has read one paper's
  data sets.
- It does not say a change of cover is contextuality. A rendering that
  decides a question the source left open has changed which questions can be
  asked, not shown that the answers cannot be glued.
- It does not fix the threshold or the rate in its defeat condition. Both
  belong to the discriminating study's preregistration.

## Note of 2026-10-10: a documented case

[CASE-tmpxnd3y](../cases.d/CASE-tmpxnd3y.md) gives this claim a documented case for one half of a change
of cover, in place of the invented tu/vous illustration. Hafez's "Shirazi
Turk" leaves the beloved's sex and nature open in the Persian, and four
English renderings decide it three ways: a maid (Jones 1771, Bell 1897),
God (Clarke 1891, "His dark mole") and a boy (Davis 2012), with Davis
saying in print that his choice is arbitrary. The question decided is the
one this claim needs, who is addressed and in what relationship.

It does not supply the other half, a question the source decides that a
rendering makes undecidable; that half still rests on [CASE-010](../cases.d/CASE-010.md). Nor does
it measure reader agreement: the openness of the source is attested by
translators and scholars, and a defender can reply that genre convention
makes the beloved determinately male for Persian readers. The case's
reader test, which could be items in [CASE-tmp1uzfn](../cases.d/CASE-tmp1uzfn.md), would settle that.
