---
number: 761
status: Active
formerly:
- CLAIM-tmpqpd2p
title: 'A stabilized constraint can be stored work: by replacing later work with cheaper operations it changes which activities are realizable within a fixed per-task budget, so amortization becomes capability expansion without any added degrees of freedom or resources; the expansion is conditional on the costs of constructing, keeping, retrieving, verifying and revising the constraint and on the distribution of later demands, and the persistence that buys it can entrench'
version: 3
history:
- version: 2
  date: '2026-11-20'
  note: >-
    Promoted at the status review's ruling (the owner delegated these
    rulings; ADR-057). Its premises CLAIM-303, CLAIM-475 and CLAIM-582 are
    Active and nothing objects to it. The step from amortization to
    capability was re-checked: if a task is feasible when its least
    per-task cost, retrieval and verification included, is within the
    budget B, then stored work that cuts that cost from 12 to 3 makes the
    task feasible at B = 5 whatever the 100 its construction cost, and B is
    unchanged. CLAIM-475, Active, gives the instance the record already
    holds, a stabilized specification that makes questions cheaper to ask,
    and its entrenchment. Nothing meets the defeated_if. In the witnesses
    offered the acquired organization lowers the least cost; the gain is
    not CLAIM-582's reliability under a fixed mechanism, since the claim
    counts a cost-lowering constraint as a change of mechanism, as
    CLAIM-582 does; and the third disjunct, read as a gain that could be
    had without the work of forming the constraint, is not met, since
    each witness stipulates that the framework is acquired at a cost.
    CLAIM-755, which the body cites for the two separations, stays
    Proposed and is not a premise. Interpretive. The title is unchanged.
- version: 3
  date: '2026-11-23'
  note: >-
    Joins the work governance-of-possibility (ADR-144) at its
    membership pass of 2026-11-23, under ADR-104's rule: the revised
    manuscript in scratch/manuscripts/governance-of-possibility/ states
    its proposition or uses it as a step, in §11.1. No other change.
role: thesis
warrant: interpretive
defeated_if: >-
  The claim says this can happen, so one case without stored work does
  not refute it. It is defeated by an operational failure in every
  witness offered: the acquired organization does not lower the least
  cost of executing the task, retrieval and verification included,
  enough to change what is feasible under the declared per-task budget;
  or the gain is CLAIM-582's improvement of reliability under a fixed
  mechanism rather than a lower least cost; or it is had equally from a
  constraint imposed with no history. It is not defeated by an economic
  failure, lifetime savings that never repay construction and upkeep:
  that defeats only the stronger reading that the investment was
  worthwhile, which the claim does not make. Not defeated by a constraint
  that persists and saves nothing (CLAIM-443), which the claim allows.
  (Rewritten at ChatGPT's reviews of 2026-11-19, forwarded by the owner:
  first to match the claim's quantifier, then to separate operational
  from economic failure.)
tags:
- complex-systems
- information-theory
- learning-theory
date: '2026-11-19'
line:
- realizability
- learned-structure
works:
- governance-of-possibility
- cost-structure-of-possibility
rests_on:
- CLAIM-303
- CLAIM-475
- CLAIM-582
complements:
- CLAIM-478
- CLAIM-443
- CLAIM-675
- CLAIM-352
- CLAIM-576
- CLAIM-755
bears_on:
- QUESTION-095
- QUESTION-392
summary: >-
  The owner's thesis, in A's wording. At U17 of the exchange "Topological
  protection explained" (2026-11-18) the owner called A37's sentence,
  "Selective contraction can expand capabilities when the stabilization of
  some relationships reduces the resources needed to realize valuable
  alternatives, or makes possible new forms of coordinated action", "an
  excellent formalization of something else Nucleation has tried to
  develop: a theory of how constraint can relate to amortization of work,
  and the tradeoff between memory (amortizing a value) and computation
  (rederiving it just in time)". A39 then stated it as "Constraints as
  amortized realizations". The record held the parts: filing moves work
  across time ([CLAIM-303](CLAIM-303.md)), the owner's stored inquiry ([CLAIM-475](CLAIM-475.md)), the
  owner's conjecture that retrieval is amortized computation ([QUESTION-095](../questions.d/QUESTION-095.md)),
  and the limit that an added hard constraint enlarges nothing under a
  fixed mechanism ([CLAIM-582](CLAIM-582.md)). No claim joined constraint, amortization and
  capability.
---
<!-- inactive-ok-file: CLAIM-755 — Proposed; cited in this filing of 2026-11-19 -->

# CLAIM-761: A stabilized constraint can be stored work: by replacing later work with cheaper operations it changes which activities are realizable within a fixed per-task budget, so amortization becomes capability expansion without any added degrees of freedom or resources; the expansion is conditional on the costs of constructing, keeping, retrieving, verifying and revising the constraint and on the distribution of later demands, and the persistence that buys it can entrench

## The claim

The owner, at U17 of the exchange "Topological protection explained"
(https://chatgpt.com/share/6afe6dd0-9d78-83ea-9782-f55680665dcf), on A37's
sentence:

> this is an excellent formalization of something else Nucleation has tried to develop: a theory of how constraint can relate to amortization of work, and the tradeoff between memory (amortizing a value) and computation (rederiving it just in time).

A39 §10, "Constraints as amortized realizations — proposed hypothesis":

> A stable constraint may embody a history of costly learning, coordination, or computation. When maintained across repeated use, it can replace future work with cheaper operations, thereby changing which activities are realizable within a given resource budget. This can expand effective capabilities without increasing the system's fundamental degrees of freedom or available physical resources.

## The step from amortization to capability

A39 §1's example: a question costs 12 units to formulate and investigate
from scratch and 3 with an acquired framework. With a per-task budget of
5 the first is out of reach and the second within it. "This is the point
where amortization becomes capability expansion." [CLAIM-303](CLAIM-303.md) prices
amortization by totals, worth it when reuse covers the cost. With a
per-task ceiling the same stored work does something else: it moves a
task across the budget line, whether or not its construction has yet
been repaid (A62 §2). That is [CLAIM-571](CLAIM-571.md)'s point that a threshold is a
peak, not a total.

## Guards it keeps

- **[CLAIM-582](CLAIM-582.md).** An added hard constraint, under a fixed dynamical model,
  cannot enlarge what is reachable or lower the least cost of reaching it.
  A stabilized constraint that does lower the cost has changed the
  mechanism: it supplies cheaper operations (a procedure, an index, a
  framework) and not only a restriction. This claim is about those.
- **[CLAIM-443](CLAIM-443.md).** Persistence is not amortization. A constraint amortizes
  only when keeping and using it costs less than re-solving.
- **Conditions.** The gain depends on construction, retention, retrieval,
  verification and revision costs, on what is later demanded, and on use
  outside the conditions it was formed in (A39 §10, second paragraph). A
  stabilized specification "can make other questions harder" ([CLAIM-475](CLAIM-475.md)),
  and A39 §7 notes that the cost of revision can keep a classification in
  use despite evidence against it. [CLAIM-755](CLAIM-755.md) separates this economic
  separation of time scales from the dynamical one.
- **Which costs bear on what.** Two failures are kept apart. Whether the
  stored work expands what is feasible depends on the cost of using it,
  retrieval and verification included, against the per-task budget, and
  on its upkeep being met so that it is still there. Whether it was worth
  acquiring depends also on its construction cost, its revision cost and
  how often it will be used: [CLAIM-303](CLAIM-303.md)'s break-even. A procedure that
  costs 100 to acquire and cuts a task from 12 to 3 makes the task
  feasible under a budget of 5 whether or not the 100 is ever repaid
  (ChatGPT's example at its second review, forwarded by the owner).

## The stronger reading it invites and does not support

That every emergent organization is such an investment (A39's closing
sentence, "An emergent organization can be understood as a historically
accumulated investment that changes the cost structure of future
possibility", which the owner asked to develop at U18). Some persistent
structure saves no work ([CLAIM-443](CLAIM-443.md), [CASE-116](../cases.d/CASE-116.md)'s unread slow register). That
the expansion is an expansion of freedom: whether newly affordable
operations widen substantive freedom, and for whom, is [CLAIM-352](CLAIM-352.md)'s
question, and A37 itself kept it open.

## Note of 2026-11-22: the separation, applied to three cases
<!-- inactive-ok-file: CASE-326 CLAIM-891 — new; filed by LEAD-108's run of 2026-11-22 -->

[LEAD-108](../leads.d/LEAD-108.md)'s model keeps feasibility, lifetime cost and who pays apart, as
this claim does, and the three cases show them parting ([CASE-326](../cases.d/CASE-326.md)). A
LEGO bin for a kind held in twenty copies is not needed to meet the
deadline but still pays over ten uses. The cockpit's bugs make final
approach feasible whether or not their lifetime saving is positive.
[CLAIM-891](CLAIM-891.md) adds a third route besides reuse and feasibility: a store
can pay by moving work to a moment when work is cheaper, with total work
unchanged. No status change.

## Note of 2026-11-22: learned scroll parameters as amortized coordination, from the exchange "Explain First Contact RL"
<!-- inactive-ok-file: CASE-419 CLAIM-1122 ARG-240 — Proposed or Rejected; filed 2026-11-22 from the exchange "Explain First Contact RL" -->

A8 §4 of that exchange reads the parameters an adaptive scroll interface
learns ([CASE-419](../cases.d/CASE-419.md)) through this claim: repeated interaction exposes a
mismatch, the interface learns a mapping, the mapping becomes a stable
constraint, and later interactions are easier "without fresh inference",
"a small piece of **amortized sensorimotor coordination**". A11 §5 says the
same of the cached controller. This is an analogy, so no edge: the claim's
step needs a fixed per-task budget whose feasible set the stored constraint
enlarges, and a scroll interface works without it at any parameter value,
so the reading is of cost lowered, not of capability expanded ([ARG-240](../arguments.d/ARG-240.md), Rejected as support). The
separation of fast loop and slow learning that the analogy rests on is
[CLAIM-1122](CLAIM-1122.md) (A's). No status change.
