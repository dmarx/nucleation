---
status: Proposed
title: 'Where filing an argument costs at least twice what one reconstruction overpays, the break-even filing rule files it later than its second occurrence, and every reconstruction it pays for in between is a restatement with nothing filed to check it against: the cost-competitive rule and the drift-catching second-occurrence rule part exactly when filing is that dear, and the competitive guarantee prices none of the drift between them'
version: 1
history:
- version: 1
  date: '2026-11-08'
  note: >-
    Filed at the decision that a SYNTHESIS is an account (ADR-tmp72iro), as its
    demonstration. This derivation was version 2 of SYNTHESIS-016, the
    nucleating-argument line's synthesis, admitted by the derived route.
    What it adds to its premises is one claim, so it is filed here, and
    SYNTHESIS-016 becomes the line's account, which integrates it. Title, body,
    defeater and premises are carried over; the correction at filing, F ≥
    2d, is kept.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation or a premise it needs: CLAIM-308's rule does
  not file at use ⌊F/d⌋ + 1, or its identification of ADR-032's rule with
  the break-even rule when F is about d is wrong, so that the two rules do
  not part at F ≥ 2d; or a reconstruction counted as a use before filing
  cannot redefine silently, for instance because counting it needs a
  record that already anchors it (CLAIM-182), so that nothing between the
  two filing times is unanchored; or CLAIM-176's premise fails, that each
  failure CLAIM-177 lists needs a second occurrence and coding at it
  catches each one the first time it can happen. Also defeated as a
  claim of its own if a component or note already states that the
  break-even rule leaves drift unpriced, or if it only places CLAIM-176
  beside CLAIM-308.
tags:
- design-rationale
- epistemology
date: '2026-11-08'
line:
- nucleating-argument
rests_on:
- CLAIM-176
- CLAIM-308
- CLAIM-177
bears_on:
- QUESTION-098
summary: >-
  [ADR-032](../decisions.d/ADR-032.md)'s rule, coding an argument at its second occurrence, has two
  justifications on the record. [CLAIM-176](CLAIM-176.md)'s is that the drift [CLAIM-177](CLAIM-177.md)
  records needs a second occurrence; [CLAIM-308](CLAIM-308.md)'s is the break-even rule,
  which files at use ⌊F/d⌋ + 1 and so matches the second-occurrence rule
  only while filing costs between one and two reconstructions'
  overpayment. When filing costs more, the cost rule files later, and the
  reconstructions it pays for in between are where redefinition creeps
  in; no term of its guarantee prices them. It answers part of
  [QUESTION-098](../questions.d/QUESTION-098.md). Its premises [CLAIM-176](CLAIM-176.md) and [CLAIM-308](CLAIM-308.md) are Proposed and
  [CLAIM-177](CLAIM-177.md) is Active. The derivation is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: ADR-075 ADR-tmp72iro CLAIM-176 CLAIM-182 CLAIM-185 CLAIM-186 CLAIM-303 CLAIM-308 SYNTHESIS-016 — Proposed; premises, citations and the account that integrates this claim -->

# CLAIM-tmp476gw: Where filing an argument costs at least twice what one reconstruction overpays, the break-even filing rule files it later than its second occurrence, and every reconstruction it pays for in between is a restatement with nothing filed to check it against: the cost-competitive rule and the drift-catching second-occurrence rule part exactly when filing is that dear, and the competitive guarantee prices none of the drift between them

*Filed from version 2 of [SYNTHESIS-016](../syntheses.d/SYNTHESIS-016.md), the nucleating-argument line's synthesis, at [ADR-tmp72iro](../decisions.d/ADR-tmp72iro.md). That entry is now the line's account, and integrates this claim.*

## The claim

[ADR-032](../decisions.d/ADR-032.md)'s rule, coding a thing the second time it turns up, has two
justifications on the record, from different parts of the line.

- **Drift-catching, from the anchors part ([SYNTHESIS-013](../syntheses.d/SYNTHESIS-013.md)) and the drift
  part ([SYNTHESIS-014](../syntheses.d/SYNTHESIS-014.md)).** [CLAIM-176](CLAIM-176.md): "Every failure [CLAIM-177](CLAIM-177.md) lists needs
  a second occurrence, so coding at the second occurrence catches each
  failure the first time it could happen." The mechanism is [CLAIM-186](CLAIM-186.md)'s: "proposals that are never coded have to
  be restated, and restating is where redefinition creeps in". [CLAIM-185](CLAIM-185.md) says
  the same of "A claim with no persistent premise". [CLAIM-176](CLAIM-176.md)'s own defeater
  compares rules by drift for a given filing cost, so it treats drift and
  cost as separate axes.
- **Cost, from the costs part ([SYNTHESIS-015](../syntheses.d/SYNTHESIS-015.md)).** [CLAIM-308](CLAIM-308.md) prices filing
  at F against an overpayment d per reconstruction. Its rule "reconstructs k
  = ⌊F/d⌋ times and files at use k + 1", and "[ADR-032](../decisions.d/ADR-032.md)'s second-occurrence rule
  is the break-even rule when F is about one reconstruction's overpayment".

**The derivation.**

1. The second-occurrence rule files at use 2. The break-even rule files at
   use ⌊F/d⌋ + 1. The two coincide exactly when ⌊F/d⌋ = 1, that is, for
   d ≤ F < 2d, which is [CLAIM-308](CLAIM-308.md)'s case of F about d.
2. For F ≥ 2d, ⌊F/d⌋ ≥ 2, so the break-even rule reconstructs at the second
   occurrence and at every use up to the ⌊F/d⌋-th with nothing filed.
3. Each of those reconstructions is a restatement with no persistent premise
   to check it against, which [CLAIM-185](CLAIM-185.md) and [CLAIM-186](CLAIM-186.md) name as where
   redefinition creeps in. Counting a reconstruction as a recurrence
   does not stop that: [CLAIM-177](CLAIM-177.md)'s redefinitions were of things recognized
   as the same ("will" redefined five or more times). Recognition guards
   only against an item being re-derived as though new.
4. So for F ≥ 2d the break-even rule leaves open, at each item reused that
   often, failures that the second-occurrence rule catches the first time
   they can happen. The two rules choose different filing times exactly when
   filing is that dear.
5. [CLAIM-308](CLAIM-308.md)'s guarantee is stated over F, c_r, c_a and u, with staleness
   left out. A silently redefined reconstruction costs the same effort as a
   faithful one, so no term prices it. The guarantee bounds effort, not
   drift: the drift the second-occurrence rule catches and the break-even
   rule does not lies outside it.
6. For F < d, ⌊F/d⌋ = 0 and the break-even rule files at the first use,
   sooner than the second-occurrence rule. The two then part only on
   [ADR-032](../decisions.d/ADR-032.md)'s throttle, which [CLAIM-308](CLAIM-308.md) sets aside ("Anything about [ADR-032](../decisions.d/ADR-032.md)'s
   other reason").

**Consequences.**

- [CLAIM-308](CLAIM-308.md)'s title clause, that recurrence weighted by reconstruction cost
  "is the filing criterion, not only evidence for one", holds for effort.
  For a record whose reason for the rule is [CLAIM-176](CLAIM-176.md)'s, it is not the whole
  criterion.
- The same holds for [CLAIM-303](CLAIM-303.md). It prices reusing a stale filed argument
  ("the cost of incorrectly reusing an obsolete argument may exceed the cost
  of recomputing it"), not reconstructing an unfiled one wrongly.
- It answers part of [QUESTION-098](../questions.d/QUESTION-098.md): when filing is dear, a cost rule
  under-files relative to drift.
- Folding drift into c_r would keep [CLAIM-308](CLAIM-308.md)'s guarantee only if drift had a
  fixed, known cost per restatement, which no component states.

## Admission

Derived route ([ADR-075](../decisions.d/ADR-075.md) step 5).

- **Valid.** It follows from [CLAIM-308](CLAIM-308.md)'s own statement of the rule and its
  regime, [CLAIM-176](CLAIM-176.md)'s statement of what the second-occurrence code catches,
  and [CLAIM-177](CLAIM-177.md)'s kind of failure.
- **Nontrivial.** Two justifications the record gives for one rule recommend
  different filing times in a stated regime, and [CLAIM-308](CLAIM-308.md)'s title clause is
  limited by it.
- **Not held.** [CLAIM-308](CLAIM-308.md)'s disclaimers name staleness, drifting costs,
  recognition and the throttle, not drift. [CLAIM-176](CLAIM-176.md) never mentions the
  break-even rule. No entry joins the two; the reader searched record/ on
  2026-11-07.
- **Corrected at filing.** The reader's draft put the parting at F greater
  than about d. By [CLAIM-308](CLAIM-308.md)'s own formula the rules coincide for
  d ≤ F < 2d, and part from F ≥ 2d.

Its premises keep their own standing: [CLAIM-176](CLAIM-176.md) and [CLAIM-308](CLAIM-308.md) are Proposed,
and [CLAIM-177](CLAIM-177.md) is Active.

## What it does not say

- How much drift the break-even rule lets through, or that filing that dear
  is common on this record. Neither is measured.
- That the second-occurrence rule is right. It says only that [CLAIM-308](CLAIM-308.md)'s
  guarantee does not cover [CLAIM-176](CLAIM-176.md)'s reason for the rule.
