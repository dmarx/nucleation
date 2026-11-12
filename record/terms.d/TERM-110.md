---
number: 110
status: Proposed
formerly:
- TERM-tmpbxjmx
title: "ratchet effect, in the incentive sense: a principal that cannot commit to future terms revises them on what an agent's performance reveals, so the agent distorts its performance to avoid worse terms; not Muller's ratchet"
version: 3
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Provenance only: NOTE-1599 went to Read in the twenty-ninth status
    review, so "skimmed in" becomes "read in" (1 place). The sense is
    unchanged.
- version: 3
  date: '2026-11-12'
  note: >-
    Now draws on THEORY-1378: "It can stop learning altogether". First
    application of draws_on (ADR-tmpcd2gu). No other change.
tags:
- game-theory
- society-and-governance
- agency
date: '2026-11-04'
line:
- readiness
summary: >-
  Filed at the owner's request on 2026-11-04, to account for an idea the
  readings of the pasted bibliography on emergency readiness surfaced and
  the record lacked: its "ratchet" hits were all Muller's ratchet,
  Axelrod's or thermodynamic ratchets, or figurative. Five readings use
  the incentive sense. Freixas, Guesnerie and Tirole name it ([LIT-2062](../literature.d/LIT-2062.md),
  Unfetched; abstract only); Gerardi and Maestri restate it for long
  relationships ([LIT-2046](../literature.d/LIT-2046.md)); Liebman and Mahoney ([LIT-2028](../literature.d/LIT-2028.md)) and
  Siemroth ([LIT-2103](../literature.d/LIT-2103.md)) name it as a motive for year-end spending and
  set it aside in their models; Ratliff and colleagues ([LIT-2097](../literature.d/LIT-2097.md))
  raise its logic as an open problem without the name. The wording is the
  filer's; adopting it is the owner's call.
draws_on:
- THEORY-1378
---
<!-- inactive-ok-file: ADR-tmpcd2gu — Proposed; the decision this entry's history note of 2026-11-12 applies -->
<!-- inactive-ok-file: LIT-2062 LIT-1573 — Unfetched; works cited for their published abstract or as the source of a sense, nothing here rests on them -->
<!-- inactive-ok-file: THEORY-1371 CASE-173 — Proposed; an account and a case cited as filed, nothing here rests on their being settled -->
<!-- inactive-ok-file: CASE-200 — Proposed or new; entries of 2026-11-05 filed from the pasted synthesis on constraint architectures, cited as open -->

# TERM-110: ratchet effect, in the incentive sense: a principal that cannot commit to future terms revises them on what an agent's performance reveals, so the agent distorts its performance to avoid worse terms; not Muller's ratchet

## Definition

A **ratchet effect**, in this record's incentive sense, holds between a
principal and an agent over repeated periods when three things hold:

1. the agent has private information about what it can do or what it
   needs (its cost, its productivity, its spending needs);
2. the principal sets each period's terms (a target, a schedule of
   payment, a budget) on what the agent's past performance has revealed,
   and cannot commit in advance not to; and
3. the agent, anticipating this, distorts its present performance so as
   not to reveal what would earn it worse terms.

The distortion goes whichever way hides the information. In the founding
case it is under-performance: by Freixas, Guesnerie and Tirole's abstract
([LIT-2062](../literature.d/LIT-2062.md), unread), revising the scheme on observed performance "this
induces firms to underproduce to avoid more demanding schedules in the
future—the ratchet effect", and the planner "cannot commit himself to a
revision procedure". In a budget it is over-spending: Liebman and Mahoney
([LIT-2028](../literature.d/LIT-2028.md), [NOTE-1553](../notes.d/NOTE-1553.md)) write that "If Congress interprets unspent
resources as a signal of reduced need, then unspent funding not only
produces a loss of value in the current period but may also lead to lower
budgets in the future", and Siemroth ([LIT-2103](../literature.d/LIT-2103.md), [NOTE-1594](../notes.d/NOTE-1594.md)) names
"the agent’s fear to have his budget cut next year if not all funds are
used, which is known as the ratchet effect".

The term separates two things the record would otherwise run together:
a measure that gives a wrong reading of an organization, and a measure
that the organization, knowing how it will be used, acts to make wrong.
The ratchet is the second, with a specific cause: the measurer's
inability to commit about how it will use what it learns.

## What the readings add

- **It can stop learning altogether.** Gerardi and Maestri ([LIT-2046](../literature.d/LIT-2046.md),
  read in [NOTE-1599](../notes.d/NOTE-1599.md); [THEORY-1378](../theory.d/THEORY-1378.md)): "The ratchet effect is in place
  since the firm has the incentive to change the terms of trade and offer
  more demanding contracts when it learns that the worker is highly
  productive." With patient parties, "If the prior probability of the
  worker being productive is low, the firm offers a pooling contract and
  no information is ever revealed." So the ratchet need not only distort
  output; it can leave the principal permanently ignorant. Their remedy is
  structural: "Our findings suggest that rehiring is another possible
  remedy to the ratchet effect."
- **Commitment is the remedy the budget papers give.** Siemroth: "Principals
  should therefore publicly commit to not cut budgets if funds are
  returned or saved." Liebman and Mahoney's rollover result likewise needs
  the budget-setter's commitment ([NOTE-1553](../notes.d/NOTE-1553.md)).
- **Its absence is a modelling choice.** Liebman and Mahoney say "the model
  does not exhibit a ratchet effect phenomenon", because the pattern of
  spending reveals relative, not absolute, need; Siemroth says "This model
  does not exhibit a ratchet effect", because needs are independent across
  years, and asks "How do the optimal budget rules change once a ratchet
  effect sets in?" Both name it and set it aside, so neither result
  carries over to a setting where performance is informative about later
  need.
- **The learning version is open.** Ratliff, Dong, Sekar and Fiez
  ([LIT-2097](../literature.d/LIT-2097.md), [NOTE-1566](../notes.d/NOTE-1566.md); [THEORY-1371](../theory.d/THEORY-1371.md)) raise, without citing this
  literature, "an agent who interacts with the principal for multiple
  rounds may seek to benefit by resorting to low effort levels if it can
  influence the payment mechanism offered in subsequent rounds."

## Bearing on emergency readiness

The pasted bibliography's proposition was that measuring a maintained
capability by its observed use can destroy it. The ratchet is one route
by which that measurement acts through the measured party's own
response, not only through the principal's misreading: a unit whose
standby capability goes unused, under a principal who cuts what goes
unused, has reason to manufacture use, or to give the capability up
before it is cut. That carrying-over, from a firm hiding productivity to
an organization keeping a capability for rare events, is the filer's
analogy and A's, not any of these works' claim. Whether it holds is
open in the record (for example, A's question on allocation by observed
activity, [QUESTION-386](../questions.d/QUESTION-386.md)).

## What it is not

- **Muller's ratchet** ([LIT-1573](../literature.d/LIT-1573.md), Unfetched; [CASE-173](../cases.d/CASE-173.md)): the irreversible
  accumulation of mildly deleterious mutations in an asexual lineage. No
  agent, no principal and no information.
- **The other ratchets the record holds**: the evolutionary-stability
  ratchet of Axelrod's *The Evolution of Cooperation* ([NOTE-411](../notes.d/NOTE-411.md)) and the
  thermodynamic ratchets of the Landauer notes ([NOTE-310](../notes.d/NOTE-310.md)). Both are
  one-way mechanisms with no strategic party.
- **Reactivity of measures** in Espeland and Sauder's sense ([LIT-1330](../literature.d/LIT-1330.md),
  [NOTE-1050](../notes.d/NOTE-1050.md)): the broader family, of measures that change what they
  measure. The ratchet is a particular case, in which the measured party
  anticipates the measurer's revision of its terms and the measurer cannot
  commit not to make it.
- **Governance regret** ([CLAIM-357](../claims.d/CLAIM-357.md)): a governor revising what it asks of
  subordinates with no strategic subordinate. Its note of 2026-11-04
  records that the ratchet adds one.
- **Precommitment within one agent** ([CASE-128](../cases.d/CASE-128.md)): the commitment problem
  of a self binding its own later choice. The ratchet's is a principal's
  toward another agent; the structure is shared, the parties are not.

## What would settle it

Adopting the term needs a claim of the record's own stated in it, or a
reading of Freixas, Guesnerie and Tirole that confirms the founding sense
against the abstract. Adopting it is the owner's call.

## Note of 2026-11-05: a ratchet that forecloses a transition

In the constructed [CASE-200](../cases.d/CASE-200.md), any cut on unspent funds or any expiry leaves the next budget below the 1.3 the transition needs; Siemroth's commitment not to cut is what keeps it possible. No status changes.

## Note of 2026-11-05: a test for the pinning claim

[CLAIM-577](../claims.d/CLAIM-577.md) gives a ratchet's effect on reachability in its pure form: a budget set to last period's peak spending falls to the holding cost and stays there, so every transition that needs reconfiguration slack is lost without any choice to give it up. No status changes.

## Note of 2026-11-06: what holds it back

No claim of the record's own is stated in it, its settle condition, and Freixas, Guesnerie and Tirole ([LIT-2062](../literature.d/LIT-2062.md)) are Unfetched; [CLAIM-577](../claims.d/CLAIM-577.md) left its uses because its spend-matching organization does not anticipate the rule. Its uses now say which part they mean: [TERM-106](TERM-106.md) and [CASE-200](../cases.d/CASE-200.md) cite its revision rule alone.

## Note of 2026-11-06: Gerardi and Maestri, read

The full reading ([NOTE-1599](../notes.d/NOTE-1599.md) v2) supports "It can stop learning altogether". Both quotations are the abstract's, verbatim. The mechanism is Lemma 3, checked from the journal's supplement: once the parties are patient enough, no pair of contracts both separates the two types and keeps both employed. [THEORY-1378](../theory.d/THEORY-1378.md) is now Active. No status changes; what holds the term back is unchanged.
