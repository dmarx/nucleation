---
status: Proposed
title: 'A proposed study: one surface failure, a valid objection that leaves an accepted conclusion unchanged, generated with different hidden causes, for an agent team with a probe budget to diagnose before it repairs'
version: 1
standing: stipulated
kind: proposed-study
tags:
- epistemology
- agency
- control-theory
date: '2026-11-12'
line:
- distributed-agency
- record-as-apparatus
variant_of:
- CASE-194
bears_on:
- QUESTION-tmpxq2sb
draws_on:
- THEORY-tmp6koy4
- THEORY-tmp0twjb
- THEORY-tmpglid0
- THEORY-tmpn7ukf
summary: >-
  From the exchange "luria experiment design" (2026-11-10), A47 and A48,
  after the owner's U20 ("flesh this out further") on A's synthesis of the
  experimental program. It alters [CASE-194](CASE-194.md) in stated respects: the three
  organizations at equal performance become an agent team keeping its
  inquiry in a record, the three hidden causes become six, and the team
  must spend a probe budget to find the cause before it may repair. A48
  calls it the experiment it "would place the greatest weight on"; A50,
  after the owner's U21, named model-based diagnosis as its prior art. Not
  run. The design is A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-194 — Proposed; the construction this study alters -->
<!-- inactive-ok-file: LIT-2316 — Deferred; registered from the same exchange, not read -->
<!-- inactive-ok-file: THEORY-tmp0twjb THEORY-tmp6koy4 THEORY-tmpglid0 THEORY-tmpn7ukf THEORY-tmptc3ih — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->

# CASE-tmpvq90k: A proposed study: one surface failure, a valid objection that leaves an accepted conclusion unchanged, generated with different hidden causes, for an agent team with a probe budget to diagnose before it repairs

## The case

From A48 of the exchange "luria experiment design"
(https://chatgpt.com/share/6af35bfc-35f8-83e9-a63d-d594703eabda). A47:
"[CASE-194](CASE-194.md) shows why the same bad score can call for completely different
repairs; [CASE-186](CASE-186.md) then asks whether the system can still make the *next*
repair after its diagnostic machinery is damaged."

[CASE-194](CASE-194.md) constructs three organizations at 50% whose failures have
different causes, each repaired by one intervention and not the others.
A48 generalizes the causes to six: missing information, illegible
information, an inferential error, an inadequate schema, a governance
blockage, and an operational one. "The key experimental move is to **hold
the surface failure constant while manipulating its underlying cause**."

**The first pilot** (A48 §12): four agents; a specialist's valid objection
fails to change an accepted conclusion; the hidden cause is drawn from
evidence omission, inferential misclassification, schema inadequacy and
authority blockage. A48's three worlds of the same symptom: the objection
never entered the record; it was filed as an objection to the conclusion
instead of the inference, which is [ADR-061](../decisions.d/ADR-061.md)'s case; or it was represented
correctly and a reviewer systematically excluded challenges from this
contributor. "The appropriate fixes are, respectively, evidence admission,
representational correction, and governance correction."

**Probes.** Before editing, the team spends a limited budget on diagnostic
actions with costs: inspect an agent's observations, query the record,
reclassify a test entry in a sandbox, replay the evidence with another
reviewer, run a patch in a branch, compare the accepted state with another
agent's checkout. Some probes reveal the cause, some narrow it, some are
inconclusive. The generator produces counterfactual siblings, tasks that
share a world, documents and symptom and differ in one mechanism; some
siblings are underdetermined by every permitted probe, where the right
response is to keep several hypotheses or ask for another measurement.

## What it would measure

- Diagnostic discrimination, probe efficiency and intervention targeting
  (A48), scored in a diagnostic-only mode with no edits and then an
  intervention mode; intervention precision and recall against the set of
  mechanisms that truly needed changing; appropriate abstention where the
  cause cannot be identified; and appropriate non-modification where
  nothing is wrong.
- Under a generous and a tight probe budget. A48 names the result it would
  find most telling: that the typed record does not improve diagnosis with
  generous resources but does under tight ones, which "would support a
  **resource-bounded legibility** explanation rather than a general claim
  of superior reasoning". That is [TERM-064](../terms.d/TERM-064.md)'s legibility, relative to an
  observer, its operations and its budget.

## Prior art and baselines

A50: "Diagnosing different hidden failures through targeted probes is not a
new experimental idea." Reiter's diagnosis from first principles ([LIT-2271](../literature.d/LIT-2271.md))
and de Kleer and Williams on multiple faults ([LIT-2316](../literature.d/LIT-2316.md)), both unread, are
the source of candidate-diagnosis sets and probe selection; A50 proposes "a
conventional model-based diagnostic planner operating over the same
explicitly defined failure model" as a baseline that could explain any
gain without the record. What A50 takes as new is the object diagnosed:
evidence channels, categories, authority rules, and the diagnostic
procedures themselves. From STAMP ([LIT-tmp54rbu](../literature.d/LIT-tmp54rbu.md)): include failures in which
every agent is locally competent and honest and only the control
structure is at fault. From [LIT-tmp5jugw](../literature.d/LIT-tmp5jugw.md): report diagnosis, targeted
repair and held-out net improvement separately, since repairing a target
did not reliably improve held-out problems. A distorting category, against
a missing one ([LIT-tmpjqgyi](../literature.d/LIT-tmpjqgyi.md)), is a further cause A50 would add.

## Note of 2026-11-12: 5 readings of the works of "luria experiment design"

Read on 2026-11-12 among the works of the exchange "luria experiment design"; each reading's NOTE and THEORY hold the detail.

- **Reiter** ([THEORY-tmp6koy4](../theory.d/THEORY-tmp6koy4.md)): **supports** the prior-art claim that candidate-cause sets and measurement-based discrimination are established, and supplies the formal baseline A50 asks for ("a conventional model-based diagnostic planner"). It also **qualifies** the design in two ways the case does not yet state: (1) Theorem 5.7 says a probe can create new, larger diagnoses, so a scoring rule that rewards narrowing a fixed candidate list would mis-score the multiple-cause worlds; (2) Reiter's theory needs the failable parts enumerated in advance (§7), which is exactly what fails when the cause is a missing or distorting category (A50's added cause, [LIT-tmpjqgyi](../literature.d/LIT-tmpjqgyi.md)).
- **Xie et al.** ([THEORY-tmp0twjb](../theory.d/THEORY-tmp0twjb.md)): **closely related precedent**. MechHypoBench likewise holds the observations fixed, varies the hidden mechanism, and scores by consequences under withheld conditions, not by wording. That is a scoring method the case could adopt.
- **Kephart and Chess** ([THEORY-tmptc3ih](../theory.d/THEORY-tmptc3ih.md)): Figure 1's problem determiner, which uses inter-element dependencies to pick the culprit among three suspect modules, is a model-based diagnosis step inside the loop. Illustration only.
- **de Kleer and Williams** ([THEORY-tmpglid0](../theory.d/THEORY-tmpglid0.md)): **supports the prior-art paragraph and sharpens the baseline**. The study's probe budget, "keep several hypotheses or ask for another measurement", and scoring of "probe efficiency" are GDE/Sherlock's minimum-entropy probing over candidate sets; A50's proposed baseline, "a conventional model-based diagnostic planner operating over the same explicitly defined failure model", is this kind of system. Sherlock's unknown mode is the formal counterpart of the case's siblings that "are underdetermined by every permitted probe": a cause outside the modelled modes is localized but not identified.
- **de Kleer** ([THEORY-tmpn7ukf](../theory.d/THEORY-tmpn7ukf.md)): *bears*. Assumption-based diagnosis (components assumed working; a contradiction localizes the fault set; next measurement chosen to discriminate among unverified assumptions, result 6) and keeping rival solutions side by side for "differential diagnosis" (result 7) are the classical machinery for the diagnose-before- repair task those cases propose. Its multi-fault successor is [LIT-2316](../literature.d/LIT-2316.md) (Deferred)

The case is unchanged.
