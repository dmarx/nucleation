---
number: 464
status: Active
formerly:
- CLAIM-tmpdhkhm
title: 'An intervention can change what it would take to correct it: by altering the distribution of control, access, resources or enforcement before it is reviewed, it can make a specified corrective outcome costlier or unreachable while the standards that govern that outcome stay the same'
version: 6
history:
- version: 2
  date: '2026-10-30'
  note: >-
    Promoted at the eighteenth status review, at the status review's
    ruling (the owner delegated these rulings; ADR-057). The four
    criteria hold: its grounds CASE-170, CASE-175, CASE-176 and CASE-111
    are Active, no objection is on file, and nothing in the record meets
    its defeated_if. The claim is one of possibility, and CASE-170 is
    enough for it: the demolition is documented, keeping the old wing was
    a corrective outcome the demolition made unreachable before any court
    ruled, and the standard governing it did not change. The notes of
    2026-10-29 (the Abrego Garcia order, Scheppele, Fiss and Cover) add
    mechanisms and a rival explanation and do not meet the defeated_if.
    The claim is unchanged.
- version: 3
  date: '2026-11-15'
  note: >-
    A dated note added from the exchange "Assess Depp Heard Abuse"
    (2026-11-15): the owner's U13 restates this claim's idea and names two
    new cases, filed as CASE-278 (Hains Point) and CASE-276
    (third-country removals). Title, defeater and status unchanged.
- version: 4
  date: '2026-11-16'
  note: >-
    A dated note added: Cuéllar (LIT-2706) read on 2026-11-16, NOTE-2029. No change of status or title.
- version: 5
  date: '2026-11-16'
  note: >-
    A dated note added: Hong Kong Monetary Authority (LIT-2696) read on 2026-11-16, NOTE-2018. No change of status or title.
- version: 6
  date: '2026-11-17'
  note: >-
    A dated note: the owner's U13 of the exchange "Assess Depp Heard
    Abuse" restates the observation this claim was filed from, with
    Hains Point as a new example whose facts are unverified. No other
    change.
role: thesis
warrant: interpretive
defeated_if: >-
  Cases in which every rise in the difficulty of a remedy after review is
  matched by the same rise in the counterfactual without the intervention,
  compared at the same time and not against a frozen snapshot, so that the
  difficulty is history and not the act's; or an argument that the costs
  of a remedy in two states cannot be compared without a single scale that
  already decides the case, so that "costlier" says nothing. Not defeated
  by evidence that the actors did not intend the effect: the claim is about
  the effect.
tags:
- society-and-governance
- complex-systems
- agency
date: '2026-10-27'
line:
- distributed-agency
grounds:
- CASE-176
- CASE-175
- CASE-170
- CASE-111
complements:
- CLAIM-422
- CLAIM-462
- CLAIM-463
- CLAIM-523
- CLAIM-619
summary: >-
  A7 to A9 of the exchange of 2026-10-26, from the owner's U6 and U7: the
  police entry at USIP before any court ruled, the East Wing demolished
  before review, and transfers into foreign custody. A7 named it
  "endogenous remedial constraint", preferring that to fait accompli,
  which "describes an outcome but does not specify the causal mechanism".
  A possibility claim with three mechanisms: physical irreversibility,
  enforcement-mediated entrenchment and jurisdictional displacement. The
  edge: it says nothing about intent, and nothing about how much weight a
  court should give to risks the act created.
bears_on:
- QUESTION-278
---

# CLAIM-464: An intervention can change what it would take to correct it: by altering the distribution of control, access, resources or enforcement before it is reviewed, it can make a specified corrective outcome costlier or unreachable while the standards that govern that outcome stay the same

## The claim

The owner, at U7, quoting A6's "The means used to establish control can
therefore change the practical conditions under which that control can be
challenged": "another instance of this is the destruction of the East Wing
of the white house". A7 stated it: "The remedial reach of an institution
is a property of the current organization of effective control,
jurisdiction, enforcement, and available resources—not merely of its
formal authority to issue decisions. Interventions can alter that
organization before their legality is adjudicated, making subsequent
remedies costlier, less effective, or unavailable." A8 narrowed it to a
possibility: "an intervention can alter the distribution of control,
resources, information, or enforcement capabilities such that subsequent
correction becomes more costly or less feasible, even when the underlying
legal and normative standards remain unchanged."

A7's three mechanisms, one case each:

| mechanism | case | what changed before review |
|---|---|---|
| physical irreversibility | the East Wing ([CASE-170](../cases.d/CASE-170.md)) | the object of review no longer exists |
| enforcement-mediated entrenchment | USIP ([CASE-176](../cases.d/CASE-176.md)) | who held the building, and the risk of displacing them |
| jurisdictional displacement | CECOT ([CASE-175](../cases.d/CASE-175.md)) | whose custody the people were in, and whose cooperation return needed |

The measure is A9's. For a corrective objective J and an intervention a,
let x_t^a be the state reached after a and x_t^0 the state reached at the
same time without it, and C_J(x) the least cost of achieving J from x
under a declared set of admissible actions. Then

ΔC_J(a, t) = C_J(x_t^a) − C_J(x_t^0),

with infeasibility as infinite cost. A9: "The comparison must hold time
fixed. Comparing the post-intervention world with a frozen pre-intervention
snapshot would incorrectly attribute ordinary historical change to the
disputed action", and C_J may be "money, delay, physical danger, loss of
capability", better kept as a vector than added. The claim is that
ΔC_J > 0 occurs, with J's governing standards fixed.

The timing condition is A9's too: with t_action, t_review, t_loss and
t_effective remedy, the order t_action < t_loss < t_effective remedy means
"even a completely successful later judicial proceeding may be incapable
of preserving the interest that justified intervention in the first
place."

[CASE-111](../cases.d/CASE-111.md) is the formal possibility in one variable: past the fold,
returning the parameter does not restore maintenance, so restoration
costs more than preservation. This claim is the institutional form, where
what is changed is not a parameter of the system but the arrangement
through which the system can be corrected. [CLAIM-422](CLAIM-422.md) is the
neighbour inside one organization: a correction recorded is not a capacity
maintained. Here the capacity to correct is reduced by the thing to be
corrected.

## What it does not say

- **Intent.** A8: "demonstrating that costs rose is not sufficient to
  establish deliberate obstruction. Intent requires separate evidence."
  Scheppele's autocratic legalism ([LIT-1604](../literature.d/LIT-1604.md)) is the strategic rival
  explanation, and the claim is stated so as not to choose.
- **What a court should do with the risk.** A9 kept two questions apart:
  "What risks would reversing the current situation actually create?" and
  "What significance should those risks have when they were generated by
  the conduct whose legality is disputed?" The first is causal, the second
  normative and legal; this claim is the first. Courts weigh safety,
  irreparable harm and likelihood of success for good reasons, and
  Laycock ([LIT-1610](../literature.d/LIT-1610.md)) separates preliminary relief from final remedy.
- **Unlawfulness.** It applies to lawful and unlawful interventions alike
  (A6).
- **That any of the three cases is settled.** Their court histories are
  partly the exchange's and unchecked.

## Note of 2026-10-29: the order, Scheppele, Fiss and Cover, read

Four works this claim names or neighbours are now read.

- **The third mechanism, argued.** The Supreme Court's order in *Noem v.
  Abrego Garcia*, [LIT-1606](../literature.d/LIT-1606.md) ([NOTE-1376](../notes.d/NOTE-1376.md)), behind [CASE-175](../cases.d/CASE-175.md), names
  jurisdictional displacement as an argument the government made: that
  removal across the border ends a court's power, so that acting "before a
  court can intervene" escapes consequence. Three justices rejected it as
  law. The order does not reach the mechanism; it shows the argument was
  made and how it fared.
- **The strategic rival changes the standards.** Scheppele, [LIT-1604](../literature.d/LIT-1604.md)
  ([NOTE-1390](../notes.d/NOTE-1390.md)), supports keeping the two explanations apart, for a
  reason "What it does not say" does not give: they differ in what they
  change. This claim keeps the governing standards fixed. Scheppele's
  autocrats change the standards and the correctors: they amend
  constitutions "to make what was once unconstitutional into something
  constitutional", disable constitutional courts first, and pack the
  courts that would review them. One of her tactics is this claim's
  mechanism, though: enlarging a court and its jurisdiction at once, so
  that a flood of minor cases needs the new judges (Hungary, Turkey),
  raises the cost of review with no change of standard. Her intent is
  presumed from the pattern, which bears out A8's warning that rising
  costs do not show obstruction. And her precondition, a liberal order
  hollowed out before the leader arrives, is a non-strategic process
  inside her strategic account, so the two explanations are less
  exclusive than the claim's edge treats them.
- **Forces outside the court.** Fiss, [LIT-1600](../literature.d/LIT-1600.md) ([NOTE-1364](../notes.d/NOTE-1364.md)): a
  structural remedy depends on forces outside the court that can withdraw
  (white flight) or withhold (unions, legislatures). That is a mechanism
  beside this claim's by which the cost of a corrective outcome rises
  while the governing standard stays fixed, and Fiss adds that the
  standard itself then bends.
- **The inverse case.** Cover, [LIT-1601](../literature.d/LIT-1601.md) ([NOTE-1384](../notes.d/NOTE-1384.md)): in *Tiede*, a
  court that could not rely on independent enforcement changed its
  sentence, so the conditions of enforcement changed what the court would
  order while the governing law stayed fixed.

The claim is unchanged and stays Proposed.

## Note of 2026-11-05: the constraint-architecture readings

Jules et al. ([NOTE-1617](../notes.d/NOTE-1617.md)), from the pasted synthesis on constraint architectures, give a structural analogue. A shift moves a defect in a stack of Kresling barrels to a stiffer module and enlarges the defect loop, irreversibly, so which states are reachable afterwards changes while the loading rules stay as they were. That echoes the claim: an operation alters what a later correction would take, the governing rules unchanged. It is mechanics, not intervention or review; nothing in it concerns control, access or enforcement, and the defects themselves were made by hand, outside the loading protocol. No status changes.

## Note of 2026-11-12: from available to unattainable, from "Medical Ethics and Media Enshitification"

A39 §5 of the exchange (2026-11-11) gives this claim a progression in
compatibility terms: "Available but ignored" to "Neglected" to "No longer
attainable". A newsroom that declines to investigate while it can, and after
enough disinvestment cannot. A39 §7 reads the third of its answerability
cases the same way: "answerability was initially compatible, but the
organization changed itself so that it no longer is", so that "present
infeasibility may be part of the object of normative evaluation rather than
an excuse that ends it". That is this claim with [CLAIM-518](CLAIM-518.md)'s histories. No
new claim filed; mapped here.

## Note of 2026-11-15: the owner's U13, two more cases, from "Assess Depp Heard Abuse"


At U13 of the exchange "Assess Depp Heard Abuse"
(https://chatgpt.com/share/6afa2a8d-2598-83ea-8d1a-d9ceb992a99c) the owner
quoted A23, "The speed at which an institution can act imposes an upper
bound on the practical effectiveness of anyone else's right to intervene",
and called it "a concise characterization of how the executive branch under
trump has attempted to bypass oversight and regulation, e.g. third country
deportations, the eastwing/ballroom, haines point...". That is this claim's
idea from 2026-10-26 arrived at again by another route (A's sentence came
out of the owner's U11 on procedural friction), so no new claim is filed.
The owner's "attempted to bypass" is a claim of intent, which this claim
leaves aside; it is recorded in the cases, not here.

- **Hains Point** ([CASE-278](../cases.d/CASE-278.md)) adds a mechanism to the three in the
  table: trees cut while the government's position in court was that no
  final, reviewable plan existed, until the court found one had. Acting
  while denying that there is a decision to review raises the cost of a
  remedy without changing the standard, which is this claim's effect. It is
  also a partial counter-instance: a notice requirement and an injunction
  kept the remaining alternatives open.
- **Third-country removals** ([CASE-276](../cases.d/CASE-276.md)) are jurisdictional
  displacement again, beside CECOT, with the difference that the window for
  a prior hearing was closed by the Supreme Court's own stays, not by
  disregard of an order.

A35 §4 of the same exchange reads this claim's measure and A9's
same-time comparison back correctly, and adds a name, "the second-order form
of a fait accompli": an act that changes "the other actor's capacity to
restore or reopen those options", not only the options. That is what the
claim already says; mapped, not filed.

## Note of 2026-11-16: Cuéllar, read

The exchange (A25) cited Cuéllar beside the cases this claim names.
Read, he does not treat the claim's mechanism, an intervention that raises
the cost of its own correction. What he gives is the claim's timing
condition: the White House can "mount seriatim at[tacks]" that a court may
thwart "eventually" but that cost "those targeted in the meantime." (p. 647).
In note 225, universities won back some funding streams while disruption
still imposed costs. That is loss before effective remedy, not a raised
cost of the corrective outcome. His notes 154 and 167 cite the Abrego Garcia
order and the district court's finding of willful noncompliance,
and he uses them as grounds for relaxing the presumption of
regularity, not for jurisdictional displacement. Relation: none.

## Note of 2026-11-16: Hong Kong Monetary Authority, read

The HKMA's materiality test holds this claim's logic in miniature: "a failed
gate on a reversible action still / allows correction, but a failed gate on
an irreversible action does not." (§8.1, p. 43), with payment finality as the
standard example. An irreversible act removes the correction later review
would have allowed. Relation: none.

## Note of 2026-11-17: the owner's observation restated, and Hains Point, from "Assess Depp Heard Abuse"
<!-- inactive-ok-file: CASE-tmpdn372 CLAIM-tmpgh3v2 — filed from the exchange "Assess Depp Heard Abuse" on 2026-11-17 -->

At U13 of the exchange "Assess Depp Heard Abuse" (2026-11-15) the owner
quoted A23 §3's "**The speed at which an institution can act imposes an
upper bound on the practical effectiveness of anyone else's right to
intervene.**" and wrote: "this is a concise characterization of how the
executive branch under trump has attempted to bypass oversight and
regulation, e.g. third country deportations, the eastwing/ballroom, haines
point..." That is the observation this claim was filed from (the owner's
U6 and U7 of 2026-10-26), made again. The East Wing is [CASE-170](../cases.d/CASE-170.md) and
transfers into foreign custody [CASE-175](../cases.d/CASE-175.md). A25 credited the owner with adding
"a temporal dimension" to Cuéllar's argument; the temporal principle is
A23's, and the owner's addition, now as before, is the application to
these actions.

A25 calls the mechanism "*fait accompli*": "creating a new reality before
others can prevent it, then making them confront the costs of undoing it."
This claim chose its own name over that one in 2026-10 because fait
accompli "describes an outcome but does not specify the causal mechanism".
A25's "**The act of proceeding can generate new costs of stopping, which
may subsequently weigh in favor of allowing further proceedings.**" is
this claim's physical-irreversibility and project-as-argument route (see
[CASE-170](../cases.d/CASE-170.md)'s note of today). A30 §8 offers the idea as a "Possible new claim" without citing this one.

**Hains Point** is the owner's new example. A25's account, unverified
here: crews removed "more than 400 trees on October 10, 2026"; Judge Ana
Reyes's opinion of 26 October 2026 found conflicting accounts of whether a
final plan existed, with government lawyers maintaining that "the relevant
agency had not yet adopted a final plan"; and on 14 November she
"temporarily blocked a planned November 15 closure of East Potomac Park".
If those facts hold, the case adds a route this claim does not list beside
physical irreversibility, enforcement-mediated entrenchment and
jurisdictional displacement: acting through steps the actor maintains are
preliminary, so that a reviewable decision is not yet there to challenge.
A25: "the government exercises effective control through preliminary
actions, while opponents must establish that those actions are legally
ripe for review." A25 also counts the 14 November order as "an important
counterexample to an overly deterministic version of our theory". No case
is filed until the facts are checked.

A25's limiting questions fit this claim's edge on intent: "whether
pre-action review was required, whether urgency was genuine, whether less
irreversible alternatives were available, and whether the government
preserved meaningful opportunities for legally authorized oversight." A
study that varies only an acting institution's speed is proposed as
[CASE-tmpdn372](../cases.d/CASE-tmpdn372.md); the slow-rule counterpart is [CLAIM-tmpgh3v2](CLAIM-tmpgh3v2.md).

No status changes.
