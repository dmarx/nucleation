---
number: 108
status: Active
formerly:
- CASE-tmp4nzjz
title: 'Robust governance under internal compromise: four governance architectures over cooperative, honestly dissenting and adversarial specialists, scored on attack success and on what the safeguards cost, with a variant that compromises the evaluators'
version: 2
history:
- version: 2
  date: '2026-10-23'
  note: >-
    Note of 2026-10-23 added: external analogues for the honest-dissent
    arm, from abstracts. The proposal is unchanged.
standing: stipulated
kind: proposed-study
tags:
- self-governance
- agency
- society-and-governance
date: '2026-10-18'
line: distributed-agency
illustrates:
- CLAIM-359
summary: >-
  A41's proposed study, from the exchange of 2026-10-17, on the owner's
  U41 question about insider threats. A multitask learner with three kinds
  of specialist (cooperative, honest but dissenting, adversarial) is run
  under unrestricted, reliability-weighted, role-limited and adaptive
  governance, and scored on lost legitimate capability, suppressed honest
  minorities, cost of safeguards and repair of governance after failure,
  as well as on attack success. Its sharpest variant compromises the
  processes that evaluate the others' competence, which tests [CLAIM-342](../claims.d/CLAIM-342.md)'s
  independent scoring. Federated learning is the natural testbed. Not run.
---

<!-- inactive-ok-file: CLAIM-288 CLAIM-342 CLAIM-359 — Proposed; the claims this proposed study would test or is bounded by, cited as open -->

# CASE-108: Robust governance under internal compromise: four governance architectures over cooperative, honestly dissenting and adversarial specialists, scored on attack success and on what the safeguards cost, with a variant that compromises the evaluators

## The case

A41 §8 names it "Robust Governance Under Internal Compromise", with the
research question: "Under what conditions can a distributed organization
preserve essential functions and its capacity for self-revision when some
constituent processes are faulty, adversarial, or pursuing divergent
objectives?"

The design (A41 §7). Extend the planned multitask learner "with three types
of constituent processes: ordinarily cooperative specialists, honest but
systematically dissenting specialists, and adversarially manipulated
specialists." Compare four architectures:

| Architecture | Governing mechanism | Potential failure (A41) |
|---|---|---|
| Unrestricted influence | All processes can shape aggregate updates | "Vulnerability to manipulation" |
| Reliability-weighted influence | Historical performance determines authority | "Self-reinforcing capture or unfair suppression" |
| Role-limited governance | Separate authority for proposing, criticizing, approving and auditing | "Coordination cost or collusion" |
| Adaptive governance | Role limitations plus internally revisable safeguards | "Manipulation of the revision mechanism itself" |

Measures: "not only attack success but also the loss of legitimate
capabilities, suppression of honest minorities, cost of safeguards, and the
ability to revise governance after failures."

Two variants:

1. **Compromised evaluators.** "One particularly revealing experiment would
   compromise the processes responsible for evaluating other processes'
   competence. That tests whether the organization has any genuinely
   independent means of checking its own allocation of authority." This is
   [CLAIM-342](../claims.d/CLAIM-342.md)'s thesis put to an attack: what keeps a loop from confirming
   itself is evidence whose arrival or scoring does not pass through what
   it tests. Here the scorer is itself the insider.
2. **A legitimate novelty that looks like an attack.** "introduce a novel
   task whose solution initially resembles suspicious behavior. A resilient
   but rigid organization may reject it; an adaptively robust organization
   may find a bounded way to test and eventually incorporate it."

**Testbed.** A41 §6: in federated learning, participants send model updates
to a shared learner and some may be wrong, biased or malicious. Local
update maps to a process's proposed transformation, aggregation weight to
effective influence, robust aggregation to governance under compromise, and
"Distributed but valid minority signal" to "Productive difference that
should not automatically be suppressed". The robust-aggregation literature
A41 cited is the anthology's ([ANTH-LIT-257](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-257.md), [ANTH-LIT-344](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-344.md) hold Byzantine-robust
learning there).

Held fixed across arms: the tasks, the population of specialists and the
attack class.

## What it can show

That safeguards which block capture cost legitimate learning, and how much,
for each architecture: the trade-off [CLAIM-359](../claims.d/CLAIM-359.md) asserts, measured. A
positive result for adaptive governance would show the trade-off can be
moved, not that it is absent. The evaluator variant would show whether
role-limited audit gives independent scoring or only relocates the single
point of failure.

It is stipulated and unrun. It shows nothing yet. Its results would be about
the designed population, whose objectives the modeller fixes, so by
[CLAIM-288](../claims.d/CLAIM-288.md) it can test the governance claims and not that the organization
constitutes itself. Which specialists count as "honest but dissenting" is
fixed by the designer, which is exactly the judgment a real organization
lacks ([QUESTION-087](../questions.d/QUESTION-087.md)).

## Note of 2026-10-23: the honest-dissent arm has a human analogue

Cited at A5 of the exchange of 2026-10-23, "Framework Overview Request". In three-person human groups, prediscussion
dissent improved hidden-profile decisions even when the dissent was itself
wrong, and its size did not matter (Schulz-Hardt et al., [LIT-1409](../literature.d/LIT-1409.md));
making members' preferences known degraded attention to the information
(Mojzisch and Schulz-Hardt, [LIT-1403](../literature.d/LIT-1403.md)). Both are Unavailable and read
from abstracts ([QUESTION-089](../questions.d/QUESTION-089.md)'s note). So suppressing honest minorities has
a measurable cost in people. They say nothing about adversarial members or
governance architectures. A5 also cited a comparison of Byzantine-robust
federated-learning methods under heterogeneous data, which was not
identified with confidence and is not filed. [CASE-144](CASE-144.md) proposes the
evaluator-compromise test in a form that bears on this case and [CASE-092](CASE-092.md)
at once.
