---
status: Proposed
title: 'Where filing an argument costs at least twice what one reconstruction overpays, the break-even filing rule files it later than its second occurrence, and every reconstruction it pays for in between is a restatement with nothing filed to check it against: the cost-competitive rule and the drift-catching second-occurrence rule part exactly when filing is that dear, and the competitive guarantee prices none of the drift between them'
version: 2
history:
- version: 2
  date: '2026-11-07'
  note: >-
    Restructured before merge, at the owner's review: version 1 was the
    unadmitted account of the whole line before it was split (ADR-
    tmpyb8vm). Its parts are now the accounts SYNTHESIS-tmp7nvem,
    SYNTHESIS-tmp5p7lm and SYNTHESIS-tmp9cgig, and the two new lines'
    accounts SYNTHESIS-tmpnakke and SYNTHESIS-tmp4csi2. Version 2 is the
    line's synthesis over its three parts, admitted by derivation; its
    regime is corrected to F ≥ 2d.
role: thesis
admission: admitted
route: derived
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
  synthesis of its own if a component or note already states that the
  break-even rule leaves drift unpriced, or if it only places CLAIM-176
  beside CLAIM-308.
tags:
- design-rationale
- epistemology
date: '2026-11-07'
line:
- nucleating-argument
integrates:
- SYNTHESIS-tmp7nvem
- SYNTHESIS-tmp5p7lm
- SYNTHESIS-tmp9cgig
- CLAIM-176
- CLAIM-177
- CLAIM-185
- CLAIM-186
- CLAIM-303
- CLAIM-308
premises:
- CLAIM-176
- CLAIM-308
- CLAIM-177
bears_on:
- QUESTION-098
- QUESTION-037
summary: >-
  The nucleating-argument line's synthesis, over the accounts of its three
  parts: drift (SYNTHESIS-tmp7nvem), anchors (SYNTHESIS-tmp5p7lm) and the
  costs of anchoring (SYNTHESIS-tmp9cgig). It joins the anchors part's
  reason for coding at the second occurrence, CLAIM-176's that the drift
  CLAIM-177 records needs a second occurrence, to the costs part's break-
  even rule, CLAIM-308's, which files at use ⌊F/d⌋ + 1 and so matches the
  second-occurrence rule only while filing costs between one and two
  reconstructions' overpayment. When filing costs more, the cost rule
  files later, and the reconstructions it pays for in between are where
  redefinition creeps in; no term of its guarantee prices them. Admitted
  by derivation; its premises CLAIM-176 and CLAIM-308 are Proposed and
  CLAIM-177 is Active. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: ADR-075 ADR-tmpyb8vm ADR-tmpyihxy CLAIM-176 CLAIM-182 CLAIM-185 CLAIM-186 CLAIM-191 CLAIM-192 CLAIM-301 CLAIM-303 CLAIM-308 SYNTHESIS-tmp4csi2 SYNTHESIS-tmp5p7lm SYNTHESIS-tmp7nvem SYNTHESIS-tmp9cgig SYNTHESIS-tmpnakke — Proposed; components and citations, with their standing -->

# SYNTHESIS-tmpllsy7: Where filing an argument costs at least twice what one reconstruction overpays, the break-even filing rule files it later than its second occurrence, and every reconstruction it pays for in between is a restatement with nothing filed to check it against: the cost-competitive rule and the drift-catching second-occurrence rule part exactly when filing is that dear, and the competitive guarantee prices none of the drift between them

*The synthesis of the nucleating-argument line, over the syntheses of its three parts (ADR-tmpyihxy, version 2). Its version 1 was the unadmitted account of the whole line before the line was split (ADR-tmpyb8vm).*

## The integration

ADR-032's rule, coding a thing the second time it turns up, has two
justifications on the record, from different parts of the line.

- **Drift-catching, from the anchors part (SYNTHESIS-tmp5p7lm) and the drift
  part (SYNTHESIS-tmp7nvem).** CLAIM-176: "Every failure CLAIM-177 lists needs
  a second occurrence, so coding at the second occurrence catches each
  failure the first time it could happen." The mechanism is CLAIM-186's: "proposals that are never coded have to
  be restated, and restating is where redefinition creeps in". CLAIM-185 says
  the same of "A claim with no persistent premise". CLAIM-176's own defeater
  compares rules by drift for a given filing cost, so it treats drift and
  cost as separate axes.
- **Cost, from the costs part (SYNTHESIS-tmp9cgig).** CLAIM-308 prices filing
  at F against an overpayment d per reconstruction. Its rule "reconstructs k
  = ⌊F/d⌋ times and files at use k + 1", and "ADR-032's second-occurrence rule
  is the break-even rule when F is about one reconstruction's overpayment".

**The derivation.**

1. The second-occurrence rule files at use 2. The break-even rule files at
   use ⌊F/d⌋ + 1. The two coincide exactly when ⌊F/d⌋ = 1, that is, for
   d ≤ F < 2d, which is CLAIM-308's case of F about d.
2. For F ≥ 2d, ⌊F/d⌋ ≥ 2, so the break-even rule reconstructs at the second
   occurrence and at every use up to the ⌊F/d⌋-th with nothing filed.
3. Each of those reconstructions is a restatement with no persistent premise
   to check it against, which CLAIM-185 and CLAIM-186 name as where
   redefinition creeps in. Counting a reconstruction as a recurrence
   does not stop that: CLAIM-177's redefinitions were of things recognized
   as the same ("will" redefined five or more times). Recognition guards
   only against an item being re-derived as though new.
4. So for F ≥ 2d the break-even rule leaves open, at each item reused that
   often, failures that the second-occurrence rule catches the first time
   they can happen. The two rules choose different filing times exactly when
   filing is that dear.
5. CLAIM-308's guarantee is stated over F, c_r, c_a and u, with staleness
   left out. A silently redefined reconstruction costs the same effort as a
   faithful one, so no term prices it. The guarantee bounds effort, not
   drift: the drift the second-occurrence rule catches and the break-even
   rule does not lies outside it.
6. For F < d, ⌊F/d⌋ = 0 and the break-even rule files at the first use,
   sooner than the second-occurrence rule. The two then part only on
   ADR-032's throttle, which CLAIM-308 sets aside ("Anything about ADR-032's
   other reason").

**Consequences.**

- CLAIM-308's title clause, that recurrence weighted by reconstruction cost
  "is the filing criterion, not only evidence for one", holds for effort.
  For a record whose reason for the rule is CLAIM-176's, it is not the whole
  criterion.
- The same holds for CLAIM-303. It prices reusing a stale filed argument
  ("the cost of incorrectly reusing an obsolete argument may exceed the cost
  of recomputing it"), not reconstructing an unfiled one wrongly.
- It answers part of QUESTION-098: when filing is dear, a cost rule
  under-files relative to drift.
- Folding drift into c_r would keep CLAIM-308's guarantee only if drift had a
  fixed, known cost per restatement, which no component states.

## The line it sits in

The three part accounts state the rest of the line. Drift
(SYNTHESIS-tmp7nvem) says what fails at a restatement. Anchors
(SYNTHESIS-tmp5p7lm) says that coding at the second occurrence stops it. Costs
(SYNTHESIS-tmp9cgig) says when filing pays. This synthesis is where they meet.
The line's other two former parts are now lines of their own, with accounts
SYNTHESIS-tmpnakke and SYNTHESIS-tmp4csi2.

## Admission

Derived route (ADR-075 step 5).

- **Valid.** It follows from CLAIM-308's own statement of the rule and its
  regime, CLAIM-176's statement of what the second-occurrence code catches,
  and CLAIM-177's kind of failure.
- **Nontrivial.** Two justifications the record gives for one rule recommend
  different filing times in a stated regime, and CLAIM-308's title clause is
  limited by it.
- **Not held.** CLAIM-308's disclaimers name staleness, drifting costs,
  recognition and the throttle, not drift. CLAIM-176 never mentions the
  break-even rule. No entry joins the two; the reader searched record/ on
  2026-11-07.
- **Corrected at filing.** The reader's draft put the parting at F greater
  than about d. By CLAIM-308's own formula the rules coincide for
  d ≤ F < 2d, and part from F ≥ 2d.

Its premises keep their own standing: CLAIM-176 and CLAIM-308 are Proposed,
and CLAIM-177 is Active.

## What it does not say

- How much drift the break-even rule lets through, or that filing that dear
  is common on this record. Neither is measured.
- That the second-occurrence rule is right. It says only that CLAIM-308's
  guarantee does not cover CLAIM-176's reason for the rule.
- **Links across the parts it does not make**, each tested and not admitted:
  - CLAIM-191 with CLAIM-192: a free parameter, what counts as beyond the
    members;
  - built-on with productive anchors, and one criterion of persisting, being
    addressable and being reused: a free parameter, the target, comparator
    and horizon;
  - CLAIM-186's damping with CLAIM-595's deadline: the same free parameter;
  - CLAIM-301's case for CLAIM-192: a scope mismatch, question drift within
    one exchange;
  - CASE-183's count as silent on productivity: trivial.
