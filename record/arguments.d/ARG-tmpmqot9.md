---
status: Proposed
title: 'The barrier at 1.3 between two configurations that each cost 0.7 shows that the threshold for reaching a configuration need not equal its requirement'
version: 1
form: existence
grounds:
- CASE-tmpwln61
concludes:
- CLAIM-571
tags:
- mathematics
- operations-research
date: '2026-11-12'
line:
- realizability
- readiness
summary: >-
  Filed with ADR-tmpq0fhi's first application: the construction case now
  grounds CLAIM-571's existence clause, so the support is load-bearing and
  is argued here. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-tmpwln61 ADR-tmpq0fhi — Proposed; the case and the decision this inference is filed under -->

# ARG-tmpmqot9: The barrier at 1.3 between two configurations that each cost 0.7 shows that the threshold for reaching a configuration need not equal its requirement

## The inference

CASE-tmpwln61 gives one architecture in which the target costs 0.7 to
hold and the least peak over admissible paths to it is 1.3. One such case
shows that the threshold need not equal the requirement, which is the
first clause of CLAIM-571. The claim's other parts, the formula for the
threshold and its being infinite when no admissible path exists, rest on
the claim's own argument and the readings it cites, not on this case.

## Critical questions

- **Is the case coherent?** Yes: a continuous function on an interval,
  with the admissible paths declared. Its values were rechecked
  numerically on 2026-11-12.
- **Does it separate the very things the conclusion says come apart?**
  Yes. The target's requirement (0.7) and the threshold for reaching it
  (1.3) differ, with the architecture and the admissible paths held
  fixed.
