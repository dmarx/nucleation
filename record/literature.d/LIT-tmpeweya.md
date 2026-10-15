---
status: Active
status_note: >-
  read in full 2026-10-15 from the publisher's open-access PDF on OpenProceedings
  (openproceedings.org/2016/conf/edbt/paper-12.pdf, pp. 461–466, CC BY-NC-ND 4.0),
  the URL DataCite registers for the DOI. Worth reading as the source of the vocabulary
  of read, update and space amplification, each a ratio to the base data alone with
  a floor of 1.0, and of the conjecture that bounding two forces a lower bound on
  the third. It is a vision paper: the conjecture is unproved, its formal wording
  does not say how large the forced bound is, and its evidence is three extreme
  designs on an integer array, which show conflicts between particular pairs (read
  against space, update against read) rather than a symmetric triangle, since the
  space-minimal design is also update-minimal. For [QUESTION-tmplg07t](../questions.d/QUESTION-tmplg07t.md) it shows that
  "organizing ahead" is two trades, auxiliary structure paid in space and sorting
  the base data paid in upkeep, but it has no workload, no build cost inside the
  trade and no time, so it is not the joint cost model the question lacks. For [CLAIM-tmpjmtw0](../claims.d/CLAIM-tmpjmtw0.md)
  and [CLAIM-tmp6u639](../claims.d/CLAIM-tmp6u639.md) it supports counting search as read overhead (items examined
  per item wanted), puts a bin budget nearer read cost on a directory than memory
  cost, and has no term for items that pop out, which both claims turn on.
title: 'Designing Access Methods: The RUM Conjecture'
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Filed, not read. Citation checked on 2026-10-15: the DOI is registered with
    DataCite, not Crossref, which gives 2016 only; EDBT 2016 opened on 15 March,
    which `published:` uses. Not held in the Anthology of the SOTA: a grep of its
    record/ (clone of 2026-10-15, commit d1573d2) for the title found nothing. Read
    the same day (NOTE-tmp4jlib).
tags:
- databases
date: '2026-10-15'
published: '2016-03-15'
doi: 10.5441/002/edbt.2016.42
first_author: Athanassoulis
keywords: []
implementations: []
summary: >-
  Athanassoulis et al. (2016), EDBT. The paper names three per-operation overheads
  of an access method, each a ratio to the base data alone (read, update and space
  amplification, each minimum 1.0), and conjectures that bounding any two forces
  a lower bound on the third. Its evidence is three one-line propositions about
  extreme designs over an integer array (a direct-address array, an append-only
  log, an unindexed dense array), a placement of known structures on a triangle,
  and a table of asymptotic I/O costs; nothing is proved, and the formal statement
  does not say how large the forced bound is, so as worded it is close to empty.
  The extremes themselves show the overheads are not symmetric: the space-minimal
  design is also update-minimal, and the read-minimal design keeps updates at 2.0,
  so the clean conflicts are read against space and update against both. Build cost
  appears in the table but is outside the triangle, there is no workload weighting,
  no time or deadline, and no cost of examining an item other than reading it.
---

# LIT-tmpeweya: Designing Access Methods: The RUM Conjecture

Athanassoulis, M., Kester, M., Maas, L., Stoica, R., Idreos, S., Ailamaki, A. and Callaghan, M. (2016). Designing access methods: the RUM conjecture. In *Proceedings of the 19th International Conference on Extending Database Technology (EDBT 2016)*. DOI 10.5441/002/edbt.2016.42

## Key takeaways

Read in full ([NOTE-tmp4jlib](../notes.d/NOTE-tmp4jlib.md)). The paper names three per-operation overheads of an access method, each a ratio to the base data alone (read, update and space amplification, each minimum 1.0), and conjectures that bounding any two forces a lower bound on the third. Its evidence is three one-line propositions about extreme designs over an integer array (a direct-address array, an append-only log, an unindexed dense array), a placement of known structures on a triangle, and a table of asymptotic I/O costs; nothing is proved, and the formal statement does not say how large the forced bound is, so as worded it is close to empty. The extremes themselves show the overheads are not symmetric: the space-minimal design is also update-minimal, and the read-minimal design keeps updates at 2.0, so the clean conflicts are read against space and update against both. Build cost appears in the table but is outside the triangle, there is no workload weighting, no time or deadline, and no cost of examining an item other than reading it.

## Why this is here

[QUESTION-tmplg07t](../questions.d/QUESTION-tmplg07t.md): is sorting a collection amortized search, and does physical database design give the joint cost model the question on amortized retrieval lacks?
