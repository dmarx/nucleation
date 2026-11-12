---
status: Proposed
title: 'The trap construction shows that reachability by a budget-dependent process can fall as the budget rises while path reachability does not'
version: 1
form: existence
grounds:
- CASE-tmp3431v
concludes:
- CLAIM-tmpff0cq
tags:
- mathematics
- operations-research
date: '2026-11-12'
line:
- realizability
summary: >-
  The assistant's, at the owner's acceptance on 2026-11-12 of the ideas
  offered after filing the exchange "Medical Ethics and Media
  Enshitification". One three-state construction carries the claim's
  non-monotone half; the monotone half is proved in the claim. The wording
  is the assistant's (Claude, in this session); adopting it is the owner's
  call.
---
<!-- inactive-ok-file: CASE-tmp3431v — Proposed; filed in the same follow-up -->

# ARG-tmp01cfq: The trap construction shows that reachability by a budget-dependent process can fall as the budget rises while path reachability does not

## The inference

[CASE-tmp3431v](../cases.d/CASE-tmp3431v.md): a path to g exists at every budget from 1, and the process
reaches g at budget 1 only. So process reachability need not be monotone
while path reachability is.

## Critical questions

- **Is the case coherent?** Yes. Three states, two moves and a policy that
  is a function of the state and the remaining budget, enumerated by
  python3 -I.
- **Does it separate the very things the conclusion says can come apart?**
  Yes: the architecture, and so its path reachability, is the same at
  every budget, and only the process's dependence on the remaining budget
  differs from the monotone case. The exhaustive check of the 27
  stationary maps confirms that this dependence is what breaks
  monotonicity on three states.

## Verdict

Proposed; the existence holds.
