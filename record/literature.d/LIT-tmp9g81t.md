---
status: Active
status_note: >-
  read in full 2026-10-15 ([NOTE-tmpam1do](../notes.d/NOTE-tmpam1do.md)) from the VLDB Endowment's copy of the 2003
  conference paper (www.vldb.org/conf/2003/papers/S13P01.pdf, 12 pp.; Crossref pages
  393–404), whose bitmap fonts made OCR necessary; the 2004 VLDB Journal version
  was not read. Worth reading as the first online view-selection algorithm that
  trades response time against a measured freshness: OVIS(θ) periodically moves
  up to a fixed number of page fragments between cached-and-invalidated and stored-and-refreshed,
  greedily, to keep the share of fresh fragments served above θ at the least response
  time, and materializes everything when it detects backlog. For [QUESTION-114](../questions.d/QUESTION-114.md) it
  is not the joint model: query savings and upkeep share one cost and staleness
  is measured, but staleness is a threshold, not a price, switching and storage
  are free, the greedy's optimality is asserted without proof, and the evidence
  is one synthetic simulation with fixed costs; set beside Bruno and Chaudhuri ([THEORY-332](../theory.d/THEORY-332.md)),
  which has build cost and no staleness, neither contains the other. For [CLAIM-303](../claims.d/CLAIM-303.md)
  it adds a third option, keep the result and invalidate it on change, and measures
  staleness as a share of uses, not a cost.
title: Balancing Performance and Data Freshness in Web Database Servers
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Filed, not read. Citation checked on 2026-10-15: VLDB 2003. Crossref gives 2003
    only; VLDB 2003 opened in Berlin on 9 September 2003, which `published:` uses.
    Not held in the Anthology of the SOTA: a grep of its record/ (clone of 2026-10-15,
    commit d1573d2) for the title and authors found nothing. Read the same day (NOTE-tmpam1do).
tags:
- databases
- operations-research
date: '2026-10-15'
published: '2003-09-09'
doi: 10.1016/b978-012722442-8/50042-2
first_author: Labrinidis
keywords: []
implementations: []
summary: >-
  Labrinidis and Roussopoulos (2003), VLDB 2003. The paper poses Online View Selection
  for a web server whose database takes updates while serving requests: choose,
  as the workload runs, which page fragments (WebViews) to keep stored and refreshed
  on every update and which to cache and invalidate, so as to minimize mean response
  time while the fraction of fresh fragments served (QoD) stays above a threshold
  θ. Its algorithm, OVIS(θ), estimates per fragment the response-time and QoD change
  of switching, and periodically switches up to MAX_CHANGE fragments greedily, spending
  a QoD surplus on speed or buying back a deficit; it materializes everything when
  it detects backlog. Nothing is proved: optimality of the greedy step is asserted,
  and the evidence is one synthetic simulation with fixed costs, in which OVIS kept
  QoD near θ, answered faster than caching alone, and recovered from overload. Upkeep
  and query savings share one cost, but staleness is a constraint set by the user,
  not a priced term, and build cost, switching cost and storage are absent.
---

# LIT-tmp9g81t: Balancing Performance and Data Freshness in Web Database Servers

Labrinidis, A. and Roussopoulos, N. (2003). Balancing performance and data freshness in web database servers. In *Proc. VLDB 2003*, pp. 393–404. DOI 10.1016/B978-012722442-8/50042-2

## Key takeaways

Read in full ([NOTE-tmpam1do](../notes.d/NOTE-tmpam1do.md)). The paper poses Online View Selection for a web server whose database takes updates while serving requests: choose, as the workload runs, which page fragments (WebViews) to keep stored and refreshed on every update and which to cache and invalidate, so as to minimize mean response time while the fraction of fresh fragments served (QoD) stays above a threshold θ. Its algorithm, OVIS(θ), estimates per fragment the response-time and QoD change of switching, and periodically switches up to MAX_CHANGE fragments greedily, spending a QoD surplus on speed or buying back a deficit; it materializes everything when it detects backlog. Nothing is proved: optimality of the greedy step is asserted, and the evidence is one synthetic simulation with fixed costs, in which OVIS kept QoD near θ, answered faster than caching alone, and recovered from overload. Upkeep and query savings share one cost, but staleness is a constraint set by the user, not a priced term, and build cost, switching cost and storage are absent.

## Why this is here

[QUESTION-114](../questions.d/QUESTION-114.md): switches page fragments between cached and materialized to minimize response time subject to a freshness threshold the application sets. It puts query savings, upkeep and measured staleness on one online schedule, but staleness is a constraint, not a price, and there is no build cost or guarantee. Named when registered as the nearest candidate to the joint model; the reading found it is not that model.
