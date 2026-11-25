---
number: 741
formerly:
- CLAIM-tmpol7nz
status: Proposed
title: 'Whether an arrangement respects a right that protects a choice is a property of its policy over the protected choices, not of any realized history: two arrangements can produce the same history whenever the right is not exercised against them and differ in respecting it, as two histories can reach the same endpoint and differ in whether a power was exercised; so an evaluation over endpoints or realized histories cannot represent such rights, which constrain policies and transition rules'
version: 2
history:
- version: 2
  date: '2026-11-18'
  note: >-
    Carries rightful-power after its own line(s) under ADR-085, taking
    part in its argument: bears_on QUESTION-486. No other change.
role: thesis
warrant: demonstrated
defeated_if: >-
  A representation of a right of refusal (or of appeal, or an easement)
  by a requirement on realized histories alone that classifies the two
  patient arrangements correctly on the history in which the patient
  consents; or an argument that rights of this kind protect only
  outcomes, so that an arrangement that would override a refusal does not
  fail to respect the right until it does. Not defeated by rights that
  are outcome requirements (a fishing quota, a water allocation), which
  the claim does not cover.
tags:
- ethics
- game-theory
- agency
date: '2026-11-17'
line:
- organizational-normativity
- will-organization
- rightful-power
grounds:
- CASE-283
complements:
- CLAIM-347
- CLAIM-523
- CLAIM-738
- CLAIM-720
bears_on:
- QUESTION-486
summary: >-
  A's, from the exchange "Assess Depp Heard Abuse" (2026-11-16 to 17):
  the endpoint–history separation first in A74 §3 and §10 (the same
  endpoint reached by a permitted and an unpermitted path), then A85 §11
  Case B ("Identical outcomes, different sources of authority")
  and A87 §11 (outcome against authority compatibility), then A90 VII
  (two histories to one endpoint), and A97 III, "The most important new
  refinement: Some rights protect choices, not predetermined outcomes",
  with the patient arrangements and the test E_r(s), Resp_N(r, e); A97 IX
  (powers and immunities as constraints on transition rules) and
  Proposition 2; restated with c, a and π_A(c) = c, π_B(c) = 1 in A102 §4
  and as a "conditional rights-respect test" in A106 §15. Demonstrated by
  the two constructions, checked ([CASE-283](../cases.d/CASE-283.md)). The record's
  compatibility complex ([CLAIM-347](CLAIM-347.md)) is over configurations and [CLAIM-523](CLAIM-523.md)'s
  standard over histories; neither can hold a right of this kind. The
  wording is A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-283 — filed from the same exchange, Proposed or new -->
<!-- inactive-ok-file: TERM-124 CLAIM-545 TERM-118 — Proposed; the record's dispositional reading of domination, cited with its standing -->

# CLAIM-741: Whether an arrangement respects a right that protects a choice is a property of its policy over the protected choices, not of any realized history: two arrangements can produce the same history whenever the right is not exercised against them and differ in respecting it, as two histories can reach the same endpoint and differ in whether a power was exercised; so an evaluation over endpoints or realized histories cannot represent such rights, which constrain policies and transition rules

## The claim

A97 III of the exchange "Assess Depp Heard Abuse"
(https://chatgpt.com/share/6afcb46d-83a8-83e9-9c85-4a0c3604405b): "We've
repeatedly represented demands as acceptance sets" over histories, which
suits a fish stock or a deadline. "But it can be inadequate for rights
that protect **who is entitled to choose what happens**."

**First separation: endpoint and history** (A74 §3 and §10, restated A90
VII). A74 §10 holds the final configuration q* fixed and varies the route,
γ₁ ∈ H_N and γ₂ ∉ H_N: "The substantive outcome may be identical. The
provenance of authority is not." A90 VII's two histories,
proposal → authorization → change and unilateral change → foreclosed
alternatives → acceptance, can end in the same arrangement. "But the
histories may differ in whether the relevant Hohfeldian powers and
immunities were respected." An evaluation of endpoints cannot tell them
apart; one of histories can.

**Second separation: history and policy** (A97 III; A102 §4). With c = 1
consent, c = 0 refusal, a = 1 treat, a = 0 refrain, Arrangement A is
π_A(c) = c and Arrangement B is π_B(c) = 1. On the history in which the
patient consents, both give (c, a) = (1, 1). Under a right of refusal,
with Resp_N(r, 1) = {treat, refrain} and Resp_N(r, 0) = {refrain}, A meets
Resp_N for both choices and B fails it at c = 0. So any evaluation that is
a function of the realized history gives A and B the same verdict on that
occasion, and respect for the right does not. A102 §4: "An endpoint-only
evaluation of a history in which the individual consents cannot
distinguish the policies." The construction is [CASE-283](../cases.d/CASE-283.md), checked.

A's test for such a right r, with E_r(s) its protected exercises at s
(A97 III):

    ∀ e ∈ E_r(s):  Outcome(s, e, π) ∈ Resp_N(r, e).

"**Respecting a right may require preserving a conditional response to
choices that the holder never actually makes.**" An easement unused in a
period "does not demonstrate that it is effectively protected".

Two consequences A draws, which the claim carries:

- **Three kinds of requirement** (A97 III): "Outcome demands",
  "Conditional rights requirements" and "Authority requirements". "The
  last two may require evaluating policies and institutional *game
  forms*, rather than only individual achieved histories." A106 §4 calls
  the gap between them "Requirement compatibility" against "Normative
  compatibility".
- **Transition rules** (A97 IX): a power "Authorizes transitions between
  normative relationships", an immunity "Prohibits other actors from
  making specified normative changes", so "some rights are better modeled
  as constraints on the **transition rules** than as requirements on the
  end states". This is also why rights are not "infinitely weighted
  demands" (A95 §8): a right to a fair hearing conditions which procedures
  are authorized at all, and no weight on an acceptance set expresses
  that.

The claim is demonstrated: both separations are shown by constructions in
which every feature but the one at issue is held fixed. That the rights
it concerns exist, and which they are, is not part of it.

## How it sits with the record

- **[CLAIM-347](CLAIM-347.md)** (Active): the compatibility complex over configurations
  and acceptance sets. It is the endpoint level, and the record's
  representation of demands; this claim says where it stops.
- **[CLAIM-523](CLAIM-523.md)** (Active): 𝓗_N, the histories satisfying a standard. That
  is the history level. This claim says some standards are not sets
  of histories.
- **[CASE-128](../cases.d/CASE-128.md)** (Active): the same restriction delegated and imposed, "Both
  experience the same immediate restriction and may behave identically."
  It is a case of the first separation; [CLAIM-194](CLAIM-194.md) (Active) the general
  point that a boundary does not show whether it was made or imposed.
- **[TERM-124](../terms.d/TERM-124.md)**, **[CLAIM-545](CLAIM-545.md)** and **[TERM-118](../terms.d/TERM-118.md)** (Proposed) read
  domination and disposition off-path, as capacities "used or not". This
  claim is the rights-side counterpart: respect is a disposition over
  protected choices.
- **[CLAIM-353](CLAIM-353.md)** (Active) and **[LIT-285](../literature.d/LIT-285.md)** (Sen, 1970): decisive jurisdiction
  over pairs of options conflicts with Pareto. The literature that
  represents rights as game forms (A97 III cites it; Gaertner, Pattanaik
  and Suzumura's "Individual rights revisited", 1992, is its usual
  reference, not yet read here) grew out of that conflict. It is where
  the policy level has been worked out.
- **[CLAIM-738](CLAIM-738.md)** separates rights from demands; this claim says what a
  right of choice requires that no demand can express.

## What it does not say

- Not that every exercise of every right must be realizable together.
  A106 §15: "The relevant requirement is to preserve and respond
  appropriately to **jointly admissible, protected choices**".
- Not that observed histories are useless. They can refute respect (a
  refusal overridden) but cannot certify it.
- Not that all rights are of this kind. A claim-right to a delivery is an
  outcome requirement and fits an acceptance set.

## Note of 2026-11-25: defeated standing, from the manuscript governance-of-becoming, Article 8
<!-- inactive-ok-file: CLAIM-723 CLAIM-1155 CLAIM-1184 ARG-228 — Proposed; the held form of the wrong of defeated standing, the objection to it, its reply, and this claim's construction, cited with their standing -->

The manuscript's Article 8 (§8.4.4, join J8.1) joins this claim to
defeated standing, which no entry had done: none of [CLAIM-723](CLAIM-723.md), [CLAIM-1155](CLAIM-1155.md)
or [ARG-228](../arguments.d/ARG-228.md) cites it. The link, in its limited form:

- This claim's defeater counts "a right of refusal (or of appeal, or an
  easement)" among the rights it covers. Standing to contest an act is of
  that kind: it protects a choice, to object, not an outcome.
- In [CLAIM-723](CLAIM-723.md)'s case where "the objection would have failed", and in
  [ARG-228](../arguments.d/ARG-228.md)'s matched utilities, the arrangement that respects the standing
  and the one that defeats it reach the same realized outcome. By this
  claim's second separation, an evaluation over realized histories
  "cannot represent" the difference.
- So [CLAIM-723](CLAIM-723.md)'s "even where the objection would have failed" is what a
  policy-level right looks like when the outcome is fixed, not a paradox.

The join stops there. This claim is about representation, what an
evaluation over histories can see. It does not say that failing a
policy-level constraint wrongs anyone beyond expected harm: an
instrumentalist can accept it and still judge policies by the harm they
are expected to cause, which is [CLAIM-1184](CLAIM-1184.md)'s second premise. So the
policy test explains why a defeat of standing is invisible in outcomes,
not why it is a wrong. Whether it is one stays with [CLAIM-723](CLAIM-723.md),
[CLAIM-1155](CLAIM-1155.md) and the owner's ruling on [CLAIM-1184](CLAIM-1184.md). The join has not yet
been put to an independent reader under [ADR-075](../decisions.d/ADR-075.md).

<!-- inactive-ok-file: CLAIM-745 SYNTHESIS-102 — Proposed; the categorical gate and the account whose Arm B declined its join with this claim, cited as precedent -->

**Correction of 2026-11-25 (the review of Part III, Part B).** The
second bullet above is wrong. The review's independent reader of the
joins tested J8.1 under ADR-075 and found that it misstates this claim.
CLAIM-723's defeat is "Foreclosure", T_foreclosure < T_opportunity: the
act made the standing ineffective "before it could be exercised", which
is an event in the realized history. Where "the objection would have
failed", the arrangement that respects the standing and the one that
defeats it reach the same endpoint by different histories, the objection
heard and refused in one and foreclosed in the other. ARG-228 is the
same: in O₂ "the objection arrives and is filed as a non-incident", which
is again in the history. That is this claim's *first*
separation, between endpoint and history, which an evaluation of
histories can represent (a standard over histories, CLAIM-523's 𝓗_N,
can require that no act be made irreversible before an objection can take
effect), not its second. The policy level is
reached only on a history in which no objection is made, where the two
arrangements differ only in what they would have done with one. The
corrected sentence:

> Where the objection would have failed, respecting and defeating a
> standing to contest reach the same endpoint by different histories
> (CLAIM-741's first separation), so an evaluation of endpoints cannot
> represent the defeat and one of histories can; only where no objection
> is made does the difference lie in policy alone (its second
> separation).

The third bullet follows it: CLAIM-723's "even where the objection would
have failed" is what a constraint on histories looks like when the
endpoint is fixed, and a policy-level constraint only on the history with
no objection. The link applies this claim to CLAIM-723 and adds no
inference. SYNTHESIS-102's Arm B is the precedent: it tested CLAIM-745
with this claim (a categorical gate failing a right "at the level of
policy") and did not file it, as "a substitution instance of CLAIM-741's
second separation in CLAIM-745's model, an inference CLAIM-741 already
holds". The paragraph after the bullets stands: the claim explains why a
defeat of standing is invisible to an evaluation of endpoints, not why it
is a wrong. (The review's Part A, §1.3, numbers the two separations in
the order of this claim's title; the body numbers them as here, and Part
B follows the body.) No change of status. The wording is the assistant's
(Claude, in this session); adopting it is the owner's call.

## Note of 2026-11-25: what holds it back
<!-- inactive-ok-file: CLAIM-735 CLAIM-908 CLAIM-tmp9xge5 — Proposed or new; entries that use this claim, cited as evidence of reliance -->

A note for the targeted promotion review (write-manuscript step 6a), from
the same draft.

- **No premise.** It rests on no claim. Its only ground is [CASE-283](../cases.d/CASE-283.md)
  (Proposed, construction, stipulated), whose "Checked" section is its
  filer's.
- **No objection.** No claim objects to it and no ARG concludes or
  undercuts it; the record has not tested it dialectically.
- **Checked only by its filer.** No history note, case or fact-check
  records a second session rechecking the two constructions, as the
  promotions delegated on 2026-11-24 for independently recomputed
  demonstrated claims require.
- **Its defeater is open, and narrow.** It asks for a history-only
  representation that separates the two patient arrangements on the
  consenting history, which the construction rules out, or an argument
  that such rights protect only outcomes. No such argument is on the
  record.

What would clear it: a recheck of [CASE-283](../cases.d/CASE-283.md) by another session, and an
objection filed and answered (the outcome-only reading of rights of
refusal is the natural one). Several entries use it ([CLAIM-725](CLAIM-725.md),
[CLAIM-735](CLAIM-735.md), [CLAIM-908](CLAIM-908.md), [CLAIM-571](CLAIM-571.md)'s note, [CLAIM-tmp9xge5](CLAIM-tmp9xge5.md)), so its use is
evidence of reliance, not of truth. A candidate for promotion, not a
promotion: that is the owner's call. The wording is the assistant's
(Claude, in this session); adopting it is the owner's call.
