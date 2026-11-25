---
number: 124
status: Proposed
formerly:
- SYNTHESIS-tmpfxv00
title: 'Use-based budgets keep routes only if drilled'
statement: >-
  Keeping a route to reorganization under a budget rule that follows use, in
  the record: under the peak rule a capability stays funded exactly while
  every period mobilizes it, so a drill each period holds the budget as a
  reserve does; a redesigned transition is lost like the original unless its
  threshold is at most the holding cost, so redesign lowers the reserve it
  needs without replacing it, and is proposed to serve only the transitions
  that can use it where a reserve of one capacity serves every one within
  it; a reserve pays when a contingency's probability times its loss
  outweighs its cost, if readiness is known; and lock-in by allocation and
  by consolidation are two routes with different remedies, while what
  justifies a lock-in and how long one stays hidden are not settled
version: 3
history:
- version: 2
  date: '2026-11-23'
  note: >-
    LEAD-226 and LEAD-230 removed from integrates: an account
    integrates claims, terms, cases, readings, questions, arguments and
    accounts, not leads (docs-check). The body still names them as the
    leads that would extend the study.
- version: 3
  date: '2026-11-23'
  note: >-
    Integrates CASE-412, the manuscript's study now filed as an
    executed-study case (gap GC1). JC1 moves from "Not stated on the
    record" to the account, as held by that case. The cross-line audit is
    recounted over the integrated entries, which no longer include the
    two leads.
defeated_if: >-
  A component misstated or misattributed here, with its scope conditions;
  an in-force entry of the record that states part of this theme left out
  without a reason given; a link this account states that no component
  states; or a join of the manuscript governance-of-possibility in this
  scope (JC1, JC2, JC3, JC5, JC9, JC10, JC11) placed as stated when no entry
  states it, or as not stated when one does. Its standing is its
  components': a component retired takes its clause with it.
tags:
- operations-research
- society-and-governance
- learning-theory
date: '2026-11-23'
line:
- readiness
- realizability
- learned-structure
integrates:
- CLAIM-571
- CLAIM-577
- CLAIM-679
- CASE-200
- CLAIM-878
- CLAIM-1099
- CLAIM-1093
- CLAIM-1180
- CLAIM-579
- CLAIM-585
- TERM-115
- QUESTION-395
- CLAIM-561
- CLAIM-758
- TERM-131
- CLAIM-757
- TERM-164
- CLAIM-684
- QUESTION-526
- CLAIM-1108
- THEORY-1073
- CLAIM-478
- CLAIM-414
- CASE-412
summary: >-
  A thematic account, across lines, of the joins the manuscript
  governance-of-possibility makes on readiness under budget rules and on
  lock-in, and that no entry maps (JC1, JC5, JC10, JC11), with the joins
  of the same scope that entries state (JC2, JC3, JC9). It was filed for
  that manuscript at the owner's ruling of 2026-11-23: "the manuscript is a
  view over the argument. preferably, nothing in it is new. restatements
  are fine. if they aren't directly mappable to anything already on the
  record, instead of throwing them away just file them as syntheses." It
  integrates [CLAIM-878](../claims.d/CLAIM-878.md), [CLAIM-1099](../claims.d/CLAIM-1099.md), [TERM-164](../terms.d/TERM-164.md) and [THEORY-1073](../theory.d/THEORY-1073.md),
  which no account integrated before. JC5 passes [ADR-075](../decisions.d/ADR-075.md)'s test and is
  filed as [CLAIM-1180](../claims.d/CLAIM-1180.md). JC1 is a study, not a claim, and is held as CASE-412.
  JC10 and JC11 fail.
  The wording is the assistant's (Claude, in this session); adopting it is
  the owner's call.
---

<!-- inactive-ok-file: CASE-200 CLAIM-758 TERM-131 CLAIM-757 TERM-164 CLAIM-684 CLAIM-1108 THEORY-1073 CLAIM-478 SYNTHESIS-024 SYNTHESIS-027 SYNTHESIS-031 SYNTHESIS-105 SYNTHESIS-123 SYNTHESIS-121 — Proposed; components and neighbouring accounts, cited with their standing -->

# SYNTHESIS-124: Use-based budgets keep routes only if drilled

*A thematic account, across lines, of the joins of the manuscript
governance-of-possibility (scratch/manuscripts/governance-of-possibility/,
§§9 and 11) on keeping a route to reorganization under a budget rule, and
on lock-in. Its scope covers the joins no entry maps (JC1, JC5, JC10,
JC11) and, so that the scope is whole, those an entry states (JC2, JC3,
JC9). It was filed for that manuscript at the owner's ruling of 2026-11-23
("if they aren't directly mappable to anything already on the record,
instead of throwing them away just file them as syntheses"), on the
synthesis-review skill's stage 4. Its components come from readiness,
realizability and learned-structure, and some also carry formal-apparatus
and dependence-and-domination ([ADR-129](../decisions.d/ADR-129.md)). It adds nothing; its standing is
its components'.*

*Accounts checked first. [SYNTHESIS-024](SYNTHESIS-024.md) (reaching and paying for
configurations under budgets) and [SYNTHESIS-027](SYNTHESIS-027.md) (keeping a rare capability
and judging its worth) are the two parts of the readiness line, and
[SYNTHESIS-031](SYNTHESIS-031.md) is the line's account over them. These joins draw on both
parts at once, and on learned-structure's overconsolidation, which
[SYNTHESIS-105](SYNTHESIS-105.md) maps. So no one existing account's scope covers them, and
this is a new account rather than a revision. The review of 2026-11-23
(Part B) found [CLAIM-878](../claims.d/CLAIM-878.md) and [CLAIM-1099](../claims.d/CLAIM-1099.md) integrated by no account,
though both are in readiness's part on reaching and paying. This account
integrates them. Whether [SYNTHESIS-024](SYNTHESIS-024.md) should integrate them too, at its
next version, is left to the next synthesis review. JC7, which accounts
have declined, is not taken up here.*

## The account

**The rule and its corollary.**
- **The rule.** "A budget set each period to the peak resource spent the
  period before never rises", and "any transition whose threshold exceeds
  the cost of holding the current configuration is lost after one period
  spent holding it, unless the budget is raised from outside by at least
  the difference" ([CLAIM-577](../claims.d/CLAIM-577.md), Active, demonstrated; the assistant's). "The
  loss leaves no trace in output." The threshold is the least peak over
  admissible paths ([CLAIM-571](../claims.d/CLAIM-571.md), Active, demonstrated; A's). Cutting held
  resource toward the holding cost removes "exactly the transitions whose
  threshold lies between the old holding and the new" ([CLAIM-679](../claims.d/CLAIM-679.md), Active,
  demonstrated; A's sentence).
- **Carry-over.** Under carry-over the transition survives, and under
  expiry or a cut on unspent funds it does not ([CASE-200](../cases.d/CASE-200.md), Proposed; the
  filer's reading of A's recursion).
- **The corollary.** A capability "stays funded exactly as long as every
  period contains a mobilization at its cost, whether a use, a drill, a
  false alarm or a cancelled dispatch" ([CLAIM-878](../claims.d/CLAIM-878.md), Proposed, demonstrated;
  the assistant's, from [CASE-315](../cases.d/CASE-315.md)).

**The drill as a reserve (JC2, stated).** [CLAIM-878](../claims.d/CLAIM-878.md)'s "What it adds":
"Maintenance as spending. A drill each period holds the budget". Its note
of 2026-11-23 reports the manuscript's model, in which a drill each period
and a reserve held at the same level cost the same (1.00025 above holding
in both) and have readiness curves the dominance test reports "equal". The
same note gives two differences. The drill needs no commitment from
whoever sets the budget, and skipping one period's drill loses the route.
[CLAIM-1099](../claims.d/CLAIM-1099.md)'s note of 2026-11-23 corrects its own "third mechanism" by
that: it "is [CLAIM-878](../claims.d/CLAIM-878.md)'s, already held". **JC2 is stated by [CLAIM-878](../claims.d/CLAIM-878.md) and
the note on [CLAIM-1099](../claims.d/CLAIM-1099.md).**

**Reserve against redesign (JC5).**
- **A's claim.** "Maintaining a reserve and redesigning a transition are
  distinct routes to readiness: one keeps enough capacity to cross an
  existing transition barrier, the other lowers the barrier itself"
  ([CLAIM-1093](../claims.d/CLAIM-1093.md), Proposed, interpretive; A's).
- **The objection.** Under the peak rule "a redesigned transition is lost
  like the original unless its threshold is at most the cost of holding
  the present configuration". So redesign "lowers the reserve a transition
  needs by the fall in its threshold" and replaces the reserve only at zero
  slack ([CLAIM-1099](../claims.d/CLAIM-1099.md), Proposed, demonstrated, counter; the assistant's).
  Its note of 2026-11-23 adds that, in the manuscript's model, redesign
  without a reserve did worse than no redesign.
- **The scope of each.** With one capacity usable at every configuration,
  a reserve at B keeps every transition with threshold at most B. A
  redesign lowers only the thresholds whose least-peak path can use it. So
  trading reserve for redesign loses the transitions above the new
  threshold that do not use the redesign ([CLAIM-1180](../claims.d/CLAIM-1180.md), Proposed,
  demonstrated; the assistant's). **JC5 is that claim**, filed for this
  account. It passed [ADR-075](../decisions.d/ADR-075.md)'s test by derivation, with a discriminating
  prediction.
- **Its limits.** "A reserve is described by where in a configuration
  space it can be applied, not only by how much there is" ([CLAIM-579](../claims.d/CLAIM-579.md),
  Active, interpretive; the assistant's). With several resources "no
  threshold on a weighted total of the resources describes it" ([CLAIM-585](../claims.d/CLAIM-585.md),
  Active, demonstrated; the filer's construction). "A reserve serves any"
  holds only outside both, as [CLAIM-1180](../claims.d/CLAIM-1180.md) states. [LEAD-230](../leads.d/LEAD-230.md) (Open;
  the assistant's, gap GC7) would test "how the ranking of reserve against
  redesign changes" with two resources.

**When a reserve pays (JC3, stated).**
- **The question.** [QUESTION-395](../questions.d/QUESTION-395.md) (Open; A's) asks how to tell a warranted
  reserve from waste and how that evidence "is weighed against the
  capability's cost".
- **The break-even.** [QUESTION-395](../questions.d/QUESTION-395.md)'s first note of 2026-11-23: "The
  missing parameter is the contingency's probability times its loss
  against the reserve's cost per period". [LEAD-226](../leads.d/LEAD-226.md) (Open; the
  assistant's) designs the sweep in the same terms. [QUESTION-395](../questions.d/QUESTION-395.md)'s second
  note gives the manuscript model's break-even pL* by deadline and
  probability. It also says pL* "moves with p, because under the peak rule
  a use is a mobilization ([CLAIM-878](../claims.d/CLAIM-878.md))", and that readiness observed in
  operation differs from readiness under an imposed contingency, so "the
  identification half of this question ... stays open".
- **The same form, elsewhere.** Provisional mobilization can minimize
  expected loss "even when the resource is more likely to be canceled than
  used" ([CLAIM-561](../claims.d/CLAIM-561.md), Active, demonstrated; A's, with the threshold 0.143
  in its case). Readiness is "the probability that an organization operating
  under a specified policy can deliver an effective response to a
  specified contingency within its deadline" ([TERM-115](../terms.d/TERM-115.md), Active; A's).
  **JC3 is stated by [QUESTION-395](../questions.d/QUESTION-395.md)'s notes**, with its identification half
  open.

**Two routes to lock-in (JC9, stated).**
- **The term.** Destructive lock-in is "specialization that removes or
  makes unaffordable the pathways to alternatives those demands need while
  current operation stays successful, and whose loss the benefits of
  consolidation do not justify" ([TERM-164](../terms.d/TERM-164.md), Proposed; A's). It names
  [CLAIM-758](../claims.d/CLAIM-758.md) as its sense and [CLAIM-679](../claims.d/CLAIM-679.md) as its mechanism.
- **The consolidation route.** [CLAIM-758](../claims.d/CLAIM-758.md) (Proposed, interpretive; the
  owner's generalization in A's wording): continued stabilization of a
  learner "can keep improving its present objective while raising the
  budget it needs to acquire" a declared family. Learning needs "a declared
  system over a declared horizon" and excludes relaxation ([TERM-131](../terms.d/TERM-131.md),
  Proposed; A's). Whether practice can relieve overconsolidation depends on
  how the capacity to acquire was lost, by disuse or by use ([CLAIM-757](../claims.d/CLAIM-757.md),
  Proposed, interpretive; the assistant's).
- **The two kept apart.** [TERM-164](../terms.d/TERM-164.md)'s note of 2026-11-23 (the
  assistant's, gap GC10) separates "Lock-in by allocation", which needs no
  learner and is restored by outside money of at least the slack, from
  "Lock-in by consolidation", which needs a learner in [TERM-131](../terms.d/TERM-131.md)'s sense and
  "money may not reverse". It adds: "A diagnosis under it should say which
  route it found." **JC9 is stated by that note.** As a claim it would
  pass by a separating case, [CLAIM-577](../claims.d/CLAIM-577.md)'s loss with no learner. It is held
  as a qualification of a Proposed term, and whether to lift it into a
  claim is the owner's call.

**What justifies a lock-in (JC10).**
- **A burden that rises.** "The burden of justifying it should rise with
  the size and the irreversibility of the narrowing" ([CLAIM-684](../claims.d/CLAIM-684.md), Proposed,
  interpretive; A's).
- **An optimum needs declared commitments.** "There is no optimal
  regulation until the demand specification, the instruments, the horizon
  and the trade-offs among demands are declared" ([CLAIM-1108](../claims.d/CLAIM-1108.md),
  Proposed, interpretive, counter; A's).
- **The open question.** [QUESTION-526](../questions.d/QUESTION-526.md) (Open; the assistant's, gap
  GC11) asks what standard makes the loss of a pathway justified. It names
  two partial candidates: [CLAIM-684](../claims.d/CLAIM-684.md)'s burden, and "The break-even of the
  manuscript's §9.6, reversed", which "needs the readiness it compares to
  be known ([QUESTION-395](../questions.d/QUESTION-395.md)) and the trade-offs among demands declared first
  ([CLAIM-1108](../claims.d/CLAIM-1108.md))".

**How long a lock-in stays hidden (JC11).**
- **Flack's limit.** A much slower aggregate "becomes an environment the
  components tune to whether or not it summarizes the underlying
  regularities well". If it summarizes them poorly, "the system likely
  fails in the end, later the larger the separation" ([THEORY-1073](../theory.d/THEORY-1073.md),
  Proposed; Flack 2017, informal: "No model is given"). [CLAIM-478](../claims.d/CLAIM-478.md)
  (Proposed) records it, in its note of 2026-10-27, as "a limit the claim
  lacks".
- **Evidence by intervention.** Matched ordinary trajectories can conceal
  differences that a specified intervention exposes ([CLAIM-414](../claims.d/CLAIM-414.md), Active,
  demonstrated). [TERM-115](../terms.d/TERM-115.md)'s readiness is defined under an imposed
  contingency.

**The study (JC1, held as a case).** [LEAD-226](../leads.d/LEAD-226.md) (Open; the assistant's)
designs one model with "a redesign arm, a sweep of reserve sizes between
holding cost and threshold, and a harm absent from the demand
specification introduced mid-run". [CASE-412](../cases.d/CASE-412.md) (Proposed, executed
study; the assistant's) is that model, run and reproduced: it puts
[CLAIM-571](../claims.d/CLAIM-571.md)'s paths, [CLAIM-577](../claims.d/CLAIM-577.md)'s rule, [CASE-200](../cases.d/CASE-200.md)'s carry-over, [CLAIM-878](../claims.d/CLAIM-878.md)'s
drill and [CLAIM-1099](../claims.d/CLAIM-1099.md)'s reserve into one model. Ordinary output is
matched by construction while readiness at a deadline of six periods
ranges from 0.147 to 0.894; the conditions of [CLAIM-577](../claims.d/CLAIM-577.md) and
[CLAIM-1099](../claims.d/CLAIM-1099.md) hold exactly; and the reserve is most ready at every
deadline while the cheapest regime changes with the deadline. Its
novel-demand arm is [CASE-397](../cases.d/CASE-397.md), mapped by [SYNTHESIS-121](SYNTHESIS-121.md) (JD4).
**JC1 is held by [CASE-412](../cases.d/CASE-412.md)**, as an executed study, not a sentence.

## The components

| Code | Voice | Status, warrant |
|---|---|---|
| [CLAIM-571](../claims.d/CLAIM-571.md) | A's | Active, demonstrated |
| [CLAIM-577](../claims.d/CLAIM-577.md) | the assistant's | Active, demonstrated |
| [CLAIM-679](../claims.d/CLAIM-679.md) | A's sentence | Active, demonstrated |
| [CASE-200](../cases.d/CASE-200.md) | the filer's reading of A's recursion | Proposed |
| [CLAIM-878](../claims.d/CLAIM-878.md) | the assistant's | Proposed, demonstrated |
| [CLAIM-1099](../claims.d/CLAIM-1099.md) | the assistant's, counter | Proposed, demonstrated |
| [CLAIM-1093](../claims.d/CLAIM-1093.md) | A's | Proposed, interpretive |
| [CLAIM-1180](../claims.d/CLAIM-1180.md) | the assistant's, filed for this account | Proposed, demonstrated |
| [CLAIM-579](../claims.d/CLAIM-579.md) | the assistant's | Active, interpretive |
| [CLAIM-585](../claims.d/CLAIM-585.md) | the filer's construction from A's | Active, demonstrated |
| [TERM-115](../terms.d/TERM-115.md) | A's | Active |
| [QUESTION-395](../questions.d/QUESTION-395.md) | A's | Open |
| [CLAIM-561](../claims.d/CLAIM-561.md) | A's, from the exchange on emergency readiness | Active, demonstrated |
| [LEAD-226](../leads.d/LEAD-226.md) | the assistant's | Open |
| [LEAD-230](../leads.d/LEAD-230.md) | the assistant's | Open |
| [CLAIM-758](../claims.d/CLAIM-758.md) | the owner's generalization, A's wording | Proposed, interpretive |
| [TERM-131](../terms.d/TERM-131.md) | A's | Proposed |
| [CLAIM-757](../claims.d/CLAIM-757.md) | the assistant's | Proposed, interpretive |
| [TERM-164](../terms.d/TERM-164.md) | A's; the note on two routes the assistant's | Proposed |
| [CLAIM-684](../claims.d/CLAIM-684.md) | A's | Proposed, interpretive |
| [QUESTION-526](../questions.d/QUESTION-526.md) | the assistant's | Open |
| [CLAIM-1108](../claims.d/CLAIM-1108.md) | A's, counter | Proposed, interpretive |
| [THEORY-1073](../theory.d/THEORY-1073.md) | Flack (2017), read | Proposed |
| [CLAIM-478](../claims.d/CLAIM-478.md) | the owner's prompt, A's synthesis; Flack in a note | Proposed, interpretive |
| [CLAIM-414](../claims.d/CLAIM-414.md) | A's, re-run | Active, demonstrated |
| [CASE-412](../cases.d/CASE-412.md) | the assistant's, executed study | Proposed |

## Not stated on the record

Each item gives the join, what no component states, and its verdict under
[ADR-075](../decisions.d/ADR-075.md), step 5.

- **JC10, the break-even reversed as part of a standard for justified
  lock-in.** [QUESTION-526](../questions.d/QUESTION-526.md) holds it as a partial candidate, not as
  held. *Verdict: fails, a free parameter.* "Justified" still classifies
  nothing until the trade-offs among demands are declared
  ([CLAIM-1108](../claims.d/CLAIM-1108.md)), and the break-even needs readiness known, which is
  [QUESTION-395](../questions.d/QUESTION-395.md)'s open half. [QUESTION-526](../questions.d/QUESTION-526.md) is where it stays.
- **JC11, that the slower the consolidated structure, the longer a lock-in
  goes unnoticed.** No entry draws a link from [THEORY-1073](../theory.d/THEORY-1073.md) to lock-in.
  *Verdict: fails.* It carries an informal, hedged reading ("it seems
  likely"; "No model is given") to a different object. The record also
  holds a realistic case in which the reading's premise holds and the
  join fails. In the allocation route, the loss "leaves no trace in
  output" ([CLAIM-577](../claims.d/CLAIM-577.md)) after one holding period, with no separation of
  timescales at all. How long it goes unnoticed is the time until the
  contingency, or until an imposed test ([CLAIM-414](../claims.d/CLAIM-414.md), [TERM-115](../terms.d/TERM-115.md)), not how slow
  anything is. So the case shows the join to be separate from its premise,
  and false as a general statement about lock-in. It would need a model of
  the consolidation route.
- **JC5's generality.** "A reserve serves any transition" is not stated,
  and as a general statement it is false where reserves have a location
  ([CLAIM-579](../claims.d/CLAIM-579.md)) or there are several resources ([CLAIM-585](../claims.d/CLAIM-585.md)). [CLAIM-1180](../claims.d/CLAIM-1180.md)
  states only the one-resource form.

## Cross-line audit ([ADR-129](../decisions.d/ADR-129.md))

Its 24 integrated components come from seven lines. Counted by script
over their `line` fields: readiness 18, realizability 10,
formal-apparatus 7, learned-structure 3, dependence-and-domination 2,
distributed-agency 2, evidence-for-experience 1 ([THEORY-1073](../theory.d/THEORY-1073.md) has none).

- **An unheld question.** No. Readiness's blurb names "budget rules that
  remove options no one chose to give up", and the reserve and its worth.
  Lock-in by consolidation is learned-structure's overconsolidation.
- **Recurrence.** Yes. The theme recurs in this manuscript, in
  [SYNTHESIS-024](SYNTHESIS-024.md)'s "How a budget rule removes options", and in
  [TERM-164](../terms.d/TERM-164.md), which rests on components from several lines.
- **Findability.** No. A reader looking for reserves, drills and budget
  rules finds them under readiness.

*Verdict: a bridge.* The account stays cross-line. It fails the first and
third questions, since readiness holds the theme and learned-structure
holds the consolidation route.

## What it does not say

That any industrial ecosystem has configurations with such costs, or budget
rules of the pure peak type. Every result here is a model's, and [CLAIM-878](../claims.d/CLAIM-878.md)
says its limit for budgets in money or hours stands. The manuscript's
other joins are mapped by [SYNTHESIS-123](SYNTHESIS-123.md) (timing of response and
revision) and [SYNTHESIS-121](SYNTHESIS-121.md) (correction, answerability and harmony).

## Note of 2026-11-23: the study filed

JC1, which this account listed as a study to be filed as a CASE, is now
filed as [CASE-412](../cases.d/CASE-412.md), with its novel-demand arm as [CASE-397](../cases.d/CASE-397.md); this
version integrates the first. The note is the assistant's (Claude, in
this session); adopting it is the owner's call.

## Note of 2026-11-25: three ways of losing a route under use-following budgets, unjoined
<!-- inactive-ok-file: CLAIM-1288 — not in force; cited in the note of 2026-11-25 with their standing -->

The manuscript governance-of-possibility cites [CLAIM-921](../claims.d/CLAIM-921.md) (Active,
demonstrated) and [CLAIM-1288](../claims.d/CLAIM-1288.md) (A's, Proposed) beside [CLAIM-577](../claims.d/CLAIM-577.md) (Active,
demonstrated), and no account relates them (the audit of what was left out (2026-11-25), B20). This account
integrates [CLAIM-577](../claims.d/CLAIM-577.md) and neither of the others. The three are distinct
mechanisms, and governance-of-possibility keeps them apart (its §5: one
"concerns loss of affordable transition pathways; the other concerns loss
of the underlying capability", A51 §3):

- [CLAIM-577](../claims.d/CLAIM-577.md): under the peak rule a transition whose threshold exceeds the
  holding cost is lost after one period of holding; the capability to hold
  is untouched.
- [CLAIM-921](../claims.d/CLAIM-921.md): under a budget that follows observed use, competence that
  decays without funded maintenance reaches a state in which it is "never
  used or funded again"; the capability itself is lost.
- [CLAIM-1288](../claims.d/CLAIM-1288.md): reactive work and the engineering that would remove its
  cause draw on one budget, the reactive work takes precedence, and the
  capacity to transform is consumed while operation succeeds.

A link no entry states: the remedies of the second and third have one
form, funding held apart from current use ([CLAIM-921](../claims.d/CLAIM-921.md)'s "maintenance
funded apart from use"; [CLAIM-1288](../claims.d/CLAIM-1288.md)'s "standing reservation of
capacity for transformation"), and this account's reserve held as budget
may be the same form for the first. Whether that is one remedy for three
mechanisms, or three remedies that share a shape, is for the next
synthesis review, with the [ADR-075](../decisions.d/ADR-075.md) test. The account is not revised here.
No change of status. The wording is the assistant's (Claude, in this session); adopting it is the owner's call.
