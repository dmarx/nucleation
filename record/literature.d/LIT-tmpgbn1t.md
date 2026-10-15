---
status: Active
status_note: >-
  read in full 2026-10-15 from the copy in the University of Pennsylvania's repository
  (ScholarlyCommons cis_papers 1351, repository.upenn.edu/server/api/core/bitstreams/92340f91-673c-435e-9b4e-b24072d4d96b/content),
  the camera-ready text with printed pages 355–366. Worth reading as the one model
  the record holds in which staleness and upkeep are traded in a single objective:
  a cached interval of width W is escaped (a pushed refresh, cost C_vr) more often
  when narrow and is too loose for queries (an exact fetch, cost C_qr) more often
  when wide, and under the paper's model the least expected cost is where ρ·P_vr
  = P_qr with ρ = 2C_vr/C_qr ([THEORY-tmpsvwtz](../theory.d/THEORY-tmpsvwtz.md)); a rule that widens on one kind of refresh
  and narrows on the other came within 1–5% of the best fixed width in simulation
  and, restricted to exact copies, matched an adaptive cache-or-not algorithm ([THEORY-tmph9339](../theory.d/THEORY-tmph9339.md)).
  For [QUESTION-114](../questions.d/QUESTION-114.md) it prices staleness as refresh traffic, with no build cost, no
  stored answers and no cost of a wrong answer, since the source guarantees validity.
  For [CLAIM-303](../claims.d/CLAIM-303.md) it gives upkeep and per-use verification a common dial, but only
  where a source sees every change; for [CLAIM-308](../claims.d/CLAIM-308.md) its exact-caching case is a forecast-free
  counting rule justified in expectation, not in the worst case, and once staleness
  is admitted the two-state choice becomes a continuum with an interior optimum.
title: Adaptive Precision Setting for Cached Approximate Values
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Filed, not read. Citation checked on 2026-10-15: SIGMOD 2001. Crossref gives
    May 2001 only, so `published:` is the first of the month. Not held in the Anthology
    of the SOTA: a grep of its record/ (clone of 2026-10-15, commit d1573d2) for
    the title and authors found nothing. Read the same day (NOTE-tmparaq2).
tags:
- databases
- operations-research
date: '2026-10-15'
published: '2001-05-01'
doi: 10.1145/375663.375710
first_author: Olston
keywords: []
implementations: []
summary: >-
  Olston et al. (2001), SIGMOD 2001. Olston, Loo and Widom set the width of each
  cached interval adaptively to minimize total refresh traffic. A narrow interval
  is escaped often (value-initiated refreshes, cost C_vr); a wide one is too imprecise
  for queries more often (query-initiated refreshes, cost C_qr). Under a model in
  which these probabilities go as 1/W² and W, the expected cost rate is least where
  ρ·P_vr = P_qr, ρ = 2C_vr/C_qr, and a rule that widens on value-initiated and narrows
  on query-initiated refreshes, with probabilities set by ρ, reached within 1% to
  5% of the best fixed width in simulation. That the rule converges is argued, not
  proved. With exact copies required it matched an adaptive exact-caching algorithm,
  and where imprecision was allowed it beat it. Staleness is priced as refresh traffic
  only: there is no build cost, no cost of a wrong answer, and the interval is never
  wrong.
---

# LIT-tmpgbn1t: Adaptive Precision Setting for Cached Approximate Values

Olston, C., Loo, B. T. and Widom, J. (2001). Adaptive precision setting for cached approximate values. In *Proc. ACM SIGMOD 2001*, pp. 355–366. DOI 10.1145/375663.375710

## Key takeaways

Read in full ([NOTE-tmparaq2](../notes.d/NOTE-tmparaq2.md)). Olston, Loo and Widom set the width of each cached interval adaptively to minimize total refresh traffic. A narrow interval is escaped often (value-initiated refreshes, cost C_vr); a wide one is too imprecise for queries more often (query-initiated refreshes, cost C_qr). Under a model in which these probabilities go as 1/W² and W, the expected cost rate is least where ρ·P_vr = P_qr, ρ = 2C_vr/C_qr, and a rule that widens on value-initiated and narrows on query-initiated refreshes, with probabilities set by ρ, reached within 1% to 5% of the best fixed width in simulation. That the rule converges is argued, not proved. With exact copies required it matched an adaptive exact-caching algorithm, and where imprecision was allowed it beat it. Staleness is priced as refresh traffic only: there is no build cost, no cost of a wrong answer, and the interval is never wrong.

## Why this is here

[QUESTION-114](../questions.d/QUESTION-114.md) and [CLAIM-303](../claims.d/CLAIM-303.md): sets each cached interval's width to balance pushed refreshes against exact fetches by queries, the first model the record holds with upkeep and tolerated staleness in one objective and an optimum between them. It assumes a source that sees every change, which a filed argument lacks.
