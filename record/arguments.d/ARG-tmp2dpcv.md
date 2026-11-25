---
status: Proposed
title: "The priority-inversion construction, as an existence case, shows that two arbitration rules alike on the ordinary course can part under contention for a lock, and that the high-priority process's missed deadline is governance-induced only while no other process needs to finish before the work is done"
version: 1
form: existence
grounds:
- CASE-tmptpna1
concludes:
- CLAIM-tmpersgx
tags:
- software-engineering
- agency
- complex-systems
date: '2026-11-24'
line:
- will-organization
- distributed-agency
summary: >-
  The case: [CASE-tmptpna1](../cases.d/CASE-tmptpna1.md), A16 §4's three processes on one processor, rerun
  with python3 -I. The step: one workload under two arbitration rules that
  agree on every schedule without lock contention and differ with it,
  which separates an arrangement's contracts from its ordinary behaviour
  ([CLAIM-tmpersgx](../claims.d/CLAIM-tmpersgx.md)). It also narrows A16's own reading of the case as
  governance-induced frustration relieved: that holds only while the
  medium-priority process has no deadline before 10, since every schedule
  meeting H's deadline finishes M at 10. The wording is the assistant's
  (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-tmptpna1 CLAIM-tmp7hqtl CLAIM-tmpersgx CLAIM-tmpkvzcn — Proposed; cited as filed or held beside this entry, whatever its standing -->
<!-- inactive-ok-file: LIT-tmphhs41 — Deferred; cited as filed or held beside this entry, whatever its standing -->

# ARG-tmp2dpcv: The priority-inversion construction, as an existence case, shows that two arbitration rules alike on the ordinary course can part under contention for a lock, and that the high-priority process's missed deadline is governance-induced only while no other process needs to finish before the work is done

## The argument

1. In [CASE-tmptpna1](../cases.d/CASE-tmptpna1.md), fixed priorities and priority inheritance are the
   same rule whenever no process is blocked on a lock held by a
   lower-priority one: inheritance raises a holder's priority only while it
   blocks a higher-priority process.
2. With the lock held by L and needed by H, they differ: H completes at 10
   under fixed priorities and at 5 under inheritance (checked by
   simulation).
3. So two arrangements of the same processes, with the same capabilities
   and demands, are indistinguishable on the ordinary course and part
   under contention. What differs is the relation that settles the
   contention, the contract in [CLAIM-tmpkvzcn](../claims.d/CLAIM-tmpkvzcn.md)'s sense, not any process.
4. Hence the conclusion of [CLAIM-tmpersgx](../claims.d/CLAIM-tmpersgx.md), that an organization's
   characteristic structure can include contracts its ordinary behaviour
   does not reveal, has at least one instance.

## Critical questions

- **Is the case coherent?** Yes; it is a standard real-time scheduling
  construction ([LIT-tmphhs41](../literature.d/LIT-tmphhs41.md)) and the schedules were computed.
- **Does it separate the very things the conclusion says can come apart?**
  It separates arbitration rules, which [CLAIM-tmpersgx](../claims.d/CLAIM-tmpersgx.md) counts as contracts
  only through [CLAIM-tmp7hqtl](../claims.d/CLAIM-tmp7hqtl.md)'s conditions. A scheduler's inheritance rule
  meets conditions 2 and 3 (it responds to a blocked claim and settles a
  conflict); whether it meets 1 and 4, reciprocal requirements and a
  mechanism of revision, depends on how the scheduler is built. So the
  case shows the separation for arbitration rules, and for contracts only
  as far as an arbitration rule is one. That is why the conclusion is
  "can include".
- **What the case does not show.** A16 reads its remedy as "Relief: The
  organization becomes capable of fulfilling the relevant commitments
  together" and as an instance of [CLAIM-357](../claims.d/CLAIM-357.md)'s governance-induced
  frustration. Ten units of work run on one processor; meeting H's
  deadline at 5 needs L's four units and H's one before 5, so M finishes
  at 10 under every schedule that meets it. With M given no deadline the
  reading stands. With M given any deadline before 10, no arbitration rule
  meets both, the frustration is structural, and inheritance selects which
  commitment fails. The case supports [CLAIM-357](../claims.d/CLAIM-357.md)'s separation only under
  that stipulation, which A16 leaves implicit.
