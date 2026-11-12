---
status: Proposed
title: 'The record computes no withdrawals: retiring an entry reports what rests on it and leaves whether each dependant falls to a judgment, and, since its relations record support of unrecorded strength rather than justifications taken as sufficient, no rule reading only the support graph and the entries'' statuses could make that judgment correctly'
version: 2
history:
- version: 1
  date: '2026-11-12'
  note: Filed from the exchange "luria experiment design", in A's words.
- version: 2
  date: '2026-11-12'
  note: >-
    Narrowed after the readings of 2026-11-12 of de Kleer's ATMS
    (THEORY-tmpn7ukf), Doyle's TMS (THEORY-tmpd3j5r, standing in for
    LIT-2291) and Lesser and Erman's Hearsay-II retrospective
    (THEORY-tmpyxqep). Version 1 said no graph-only rule could decide
    withdrawals, without saying of which graphs. Where every edge is a
    justification taken as sufficient, a rule reading only the graph and
    which assumptions are retired does compute what still holds: that is
    what a truth maintenance system does, and the ATMS's labels are
    "consistent, sound, complete and minimal with respect to the
    justifications". The impossibility is now stated for the record's
    relations, which are not of that kind, and the two readings that mark
    the limit carry `bounds` to this claim. The derivation from CLAIM-293
    is unchanged. One decision, in place of three overlapping notes.
role: thesis
warrant: demonstrated
defeated_if: >-
  The configured record does retract a dependant automatically when what it
  rests on is retired, so the first half is false of it; or a rule that
  reads only the support graph and the entries' statuses decides correctly,
  in both of CASE-089's worlds, whether the conclusion should be withdrawn,
  which would contradict CLAIM-293. Also defeated if it only restates
  CLAIM-293 and CLAIM-479 with nothing added: the addition is that the
  reporting design is what CLAIM-293 requires of any record whose relations
  carry no weights, not a shortfall against a truth-maintenance system.
  Not defeated by a reasoner that reads more than the graph, likelihoods or
  dependence models, deciding correctly; the claim is about the graph. Not
  defeated by a truth maintenance system deciding correctly over
  justifications taken as sufficient (de Kleer, Doyle): the claim excludes
  that case. Defeated if the record's own relations are shown to be such
  justifications, so that retiring every `rests_on` and `grounds` target of
  a claim settles that it falls.
tags:
- epistemology
- logic
- design-rationale
date: '2026-11-12'
line:
- records-of-inquiry
- record-as-apparatus
rests_on:
- CLAIM-293
bears_on:
- QUESTION-tmps5iou
- QUESTION-108
summary: >-
  A's, stated four times in the exchange "luria experiment design"
  (2026-11-10): A20 §3, "Unlike a full truth-maintenance reasoner, Luria
  does not automatically calculate which beliefs should be withdrawn. It
  exposes structure and maintenance obligations to human judgment"; A27;
  A45 §9, citing [CLAIM-293](CLAIM-293.md); and A50 §7, against Doyle's and de Kleer's
  truth maintenance and AGM revision ([LIT-2291](../literature.d/LIT-2291.md), [LIT-2320](../literature.d/LIT-2320.md), [LIT-1050](../literature.d/LIT-1050.md)). A
  presents it as a boundary on what luria can claim. The derivation here
  makes it also a reason for the boundary: by [CLAIM-293](CLAIM-293.md), a rule reading
  only the unweighted graph would retract wrongly in one of two worlds the
  graph cannot tell apart. The wording is A's; adopting it is the owner's
  call.
---
<!-- inactive-ok-file: LIT-2291 THEORY-tmpn7ukf THEORY-tmpd3j5r THEORY-tmpyxqep — LIT-2291 Unfetched, Doyle's IJCAI-79 summary read in its place; the readings are Proposed, filed 2026-11-12 -->
<!-- inactive-ok-file: THEORY-tmp5vepa THEORY-tmp6koy4 THEORY-tmphaoty THEORY-tmpkjz86 THEORY-tmpo4vs4 — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->

# CLAIM-tmp8qsef: The record computes no withdrawals: retiring an entry reports what rests on it and leaves whether each dependant falls to a judgment, and no rule reading only the support graph and the entries' statuses could make that judgment correctly

## The claim

From the exchange "luria experiment design"
(https://chatgpt.com/share/6af35bfc-35f8-83e9-a63d-d594703eabda). A27:
"Luria is not a logical truth-maintenance engine. It can expose relevant
dependencies and status changes, but it cannot automatically decide that
every downstream conclusion is false." A45 §9: "Luria's typed relations and
validation mechanisms do not by themselves determine how rational belief
should change."

**What the record does.** The relation that carries dependence says what
retiring its target leaves and does nothing about it: `rests_on` is
"another of the record's own claims this one could not stand without …
Retired, it leaves this claim needing another route" (docs/record.md,
from luria.yaml). `corroborates` says the other claim "loses support, not
its footing" ([ADR-044](../decisions.d/ADR-044.md)). The `argument` chain walks the dependants. No status changes
because another did. A truth
maintenance system ([LIT-2291](../literature.d/LIT-2291.md), [LIT-2320](../literature.d/LIT-2320.md)) or an AGM revision operator
([LIT-1050](../literature.d/LIT-1050.md)) computes the new belief set instead.

**Why no graph-only rule could replace the judgment.** [CLAIM-293](CLAIM-293.md), from
[CASE-089](../cases.d/CASE-089.md): two records with the same edges, E₁ → H ← E₂, where discounting
E₁ leaves H at odds of 20:1 in one and 1.1:1 in the other. Take any rule
that decides, from the support graph and the entries' statuses alone,
whether H is withdrawn when E₁ is retired. The two records give it the
same input, so it gives the same verdict in both, and the verdict is wrong
in one of them under any standard that keeps H at 20:1 and withdraws it at
1.1:1. So a record
whose relations carry no weights cannot compute withdrawals correctly
from them, and reporting the dependants for a judgment that reads the
evidence is what such a record can soundly do.

**Where a graph-only rule does suffice.** The argument needs the edges to
carry evidence whose strength the graph does not record. Where every edge
is a justification taken as sufficient, a graph-only rule exists and is
the truth maintenance system. In Doyle's TMS a node "is believed if at
least one of these justifications is valid", and a support-list
justification is valid "if each node in its inlist is in"
(THEORY-tmpd3j5r); de Kleer's ATMS keeps each datum's label "consistent,
sound, complete and minimal with respect to the justifications"
(THEORY-tmpn7ukf). Both are correct relative to justifications the
problem solver supplies and stipulates sufficient; neither weighs them.
Even there the choice of what to withdraw on a contradiction is a choice:
Doyle's backtracker "may be mistaken in its assignment of blame to that
assumption". The record's relations are not justifications of that kind.
`rests_on` names a premise a claim "could not stand without", a necessary
premise and not a sufficient one, and `corroborates` and `grounds` carry
evidence of unrecorded strength, which is CASE-089's situation. So the
impossibility holds for the record as configured, and would fail for a
record whose relations were redefined as sufficient justifications; that
redefinition, not a cleverer rule, is what a truth-maintenance reading of
the record would need.

Practice points the same way without testing the claim. Hearsay-II's
designers built automatic re-evaluation of credibility through the
support network and dropped it: in the later configuration "hypothesis
credibility is never modified in an explicit sense; rather, new and
different hypotheses are created", since the state held at a hypothesis
"does not adequately characterize the state(s) of the hypothesis
network(s) connected to it" (THEORY-tmpyxqep). That is an automatic
propagation scheme over weighted support given up in use, not a proof
that none is correct.

## What it does not say

- Not that the record should weight its edges. [CLAIM-293](CLAIM-293.md) leaves that as a
  design question, and the owner objected to turning to it.
- Not that the judgment is made well. [CLAIM-479](CLAIM-479.md): a relation's rigidity is
  "not evidence that the dependency it records is sound". The record only
  says where a judgment is owed.
- Not that a reasoner over richer records could not compute withdrawals.
  A50's proposed test, a plain record, the record, a truth-maintenance
  system and the record with an external reasoner on formally specified
  tasks, would separate "what the record preserves from what the reasoning
  algorithm computes".

## Note of 2026-11-12: the readings on withdrawal

Read on 2026-11-12 among the works of the exchange "luria experiment design"; each reading's NOTE and THEORY hold the detail.

Version 2 narrows the claim on de Kleer's, Doyle's and the Hearsay-II
readings; its history says how. The other readings that touch it:

- **Jung et al.** (THEORY-tmpo4vs4): MEME's Absence task is this claim's
  situation, a support changed and no rule saying what follows, where the
  correct state is "uncertain"; its Cascade task is the case where a stated
  rule decides. Systems that fail hold the dependency and never surface it,
  which supports the value of reporting dependants.
- **Reiter** (THEORY-tmp6koy4) and **Hu, Wang and McAuley**
  (THEORY-tmp5vepa): a logical rule computes which assumptions to withdraw
  given a complete system description; a test in which a newer fact
  withdraws an older one measures what the record leaves to judgment.
  Contrast classes, not evidence against the claim.
- **Xu et al.** (THEORY-tmpkjz86): A-MEM rewrites neighbouring notes
  automatically, the propagation this claim says the record declines, and
  reports no check of whether the rewrites are right.
- **Wilie et al.** (THEORY-tmphaoty): Belief-R's items are logical, the
  setting where a structural rule suffices; it does not reach weighted
  evidence.
