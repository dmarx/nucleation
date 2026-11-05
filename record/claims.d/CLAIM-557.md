---
number: 557
status: Proposed
formerly:
- CLAIM-tmp42yq0
title: 'More resource for observing splits what can be told apart, and more resource for acting merges what can be turned into one another, so a system''s budgeted individuation runs in opposite directions from outside and from inside and is indexed by a pair of budgets, not one'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in either monotonicity: a case, under nested probe families, in
  which a larger observing budget rejoins objects a smaller one told apart
  (against CLAIM-574), or one, under peak costs and reversible moves,
  in which a larger acting budget splits configurations a smaller one made
  mutually reachable (against CLAIM-581). Not defeated by systems whose
  observing and acting budgets are the same resource, which the claim
  covers as a diagonal of the pair, nor by a reading of "individuation" in
  a sense other than descriptive and reachable classes.
tags:
- individuation
- mathematics
- epistemology
date: '2026-11-05'
line:
- realizability
- formal-apparatus
rests_on:
- CLAIM-574
- CLAIM-581
complements:
- CLAIM-577
bears_on:
- QUESTION-393
summary: >-
  The assistant's own proposition, filed on 2026-11-05 at the owner's
  invitation to contribute. Two results filed in this pull request run in
  opposite directions. [CLAIM-574](CLAIM-574.md): as nested probe families grow,
  restricted profiles only split objects apart. [CLAIM-581](CLAIM-581.md) (and
  [CLAIM-590](CLAIM-590.md)'s sublevel groupoid): as the budget for acting grows, the
  classes of mutually reachable configurations only merge. So "what an
  observer can tell apart" and "what a system can turn into one another"
  are two partitions of the same configurations, one refining and one
  coarsening with resources. A system's budgeted individuation is then
  indexed by a pair, an observing budget and an acting budget, and the two
  can be traded or decoupled. [CLAIM-577](CLAIM-577.md) is one decoupling: a budget
  rule that shrinks the acting budget fragments what the organization can
  become while leaving what observers see unchanged. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-210 CLAIM-574 CLAIM-577 CLAIM-581 CLAIM-590 TERM-088 — Proposed or Skimmed; entries filed in this pull request, cited as open -->

# CLAIM-557: More resource for observing splits what can be told apart, and more resource for acting merges what can be turned into one another, so a system's budgeted individuation runs in opposite directions from outside and from inside and is indexed by a pair of budgets, not one

## The claim

Fix a set of configurations of one system.

- **From outside.** Let o be an observing budget and ~_o the relation
  "no probe affordable at o distinguishes them". Under nested probe
  families, larger o only splits classes: o ≤ o′ implies ~_o′ refines ~_o
  ([CLAIM-574](CLAIM-574.md)).
- **From inside.** Let a be an acting budget and ≈_a the relation "each can
  be turned into the other within a". Under peak costs and reversible
  moves, larger a only merges classes: a ≤ a′ implies ≈_a refines ≈_a′
  ([CLAIM-581](CLAIM-581.md)).

So with more resource the outside partition gets finer and the inside
partition gets coarser. Neither is the system's individuation; the pair is.

## What it adds

- **A two-parameter object.** Budgeted individuation is a family indexed by
  (o, a), monotone in opposite directions in its two arguments. That is a
  bifiltration, and the multiparameter readings filed here (Vipond,
  Botnan and Lesnick) warn that such objects lack complete discrete
  invariants in general.
- **Decoupling.** The two budgets can move separately. [CLAIM-577](CLAIM-577.md)'s
  spend-matching rule shrinks a while o is untouched: the organization
  loses transitions, its inside classes fragment, and nothing an outside
  observer could afford to check need change. [CLAIM-302](CLAIM-302.md)'s pseudorandom
  ensembles are the converse limit: inside, the two ensembles are as
  different as can be; outside, at polynomial budget, they are one class.
- **Where the two meet.** A configuration that is its own class from
  outside but merged with others from inside is one the system can leave
  without anyone noticing; one that is merged from outside but alone from
  inside is one the system cannot leave though observers cannot tell it
  from others. Both are candidates for the readiness cases of this pull
  request ([CASE-210](../cases.d/CASE-210.md)'s two departments are the second kind).

## What it does not say

- It concerns the descriptive and reachable senses of individuation only,
  not the constitutive or organizational senses of [TERM-088](../terms.d/TERM-088.md).
- The inside monotonicity needs peak costs and reversible moves; with
  additive costs or one-way moves the inside relation is not an
  equivalence and the picture is less clean.
- Whether actual systems trade one budget for the other is empirical.

## Note of 2026-11-05: the DNA origami readings

Read on the owner's request to connect the record's realizability inquiry to DNA origami; the works were chosen by the assistant.

**Wagenbauer, Wachauf and Dietz, "Quantifying quality in DNA self-assembly".** Wagenbauer, Wachauf and Dietz (2014), LIT-tmpduceb, read in NOTE-tmpmw05j, support the observing
half empirically: spending on a de Bruijn defect label (an extra incubation and an ice-cold gel)
splits samples that TEM averaging and gel mobility merge, those with 0, 5 and 15 of 207 staples
missing. It leaves open the acting half and whether the extra spending is ordered as the claim's
budget is.

**Majikes et al., "Revealing thermodynamics of DNA origami folding via affine transformations".** Majikes et al. (2020), LIT-tmp0hqya, read in NOTE-tmperio5, support the observing half of the claim concretely. Bulk methods (UV-Vis and DSC, which "measure signal from all DNA in the sample", and gels) cannot single out one staple fold of the scaffold; a designed FRET reporter can. What can be told apart grows with replicates and instrument precision. At the paper's budget, persistence-length differences show in melting temperature but not in ΔH, ΔS or ΔCp, and better "would require equipment with a temperature control precision better than 0.3°C, and with a data sampling density greater than one measurement per 0.6°C." The paper leaves the acting half untouched.

No status changes.
