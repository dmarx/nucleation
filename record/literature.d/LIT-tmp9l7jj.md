---
status: Deferred
status_note: >-
  filed 2026-10-18, not read. Registered from the exchange of 2026-10-17, "Synthesis opportunities analysis" (workbench entries of 2026-10-18). No NOTE is filed.
title: 'Multiple-gradient descent algorithm (MGDA) for multiobjective optimization'
version: 1
history:
- version: 1
  date: '2026-10-18'
  note: >-
    Filed, not read. Citation checked against Crossref and OpenAlex on 2026-10-18. The DOI is the *Comptes Rendus Mathématique* note, online 2012-03-01. The algorithm first appeared under its own title in Désidéri's INRIA research report RR-6953, "Multiple-Gradient Descent Algorithm (MGDA)", dated June 2009 (HAL inria-00389811); by ADR-002's earlier-date rule `published:` is that month. The anthology holds no LIT for it; ANTH-NOTE-369 (Min-SNR weighting) cites "Désidéri's MGDA" for a Pareto-stationarity theorem. It is mathematics, not an instruction for ML practice, and is filed here; it carries `anthology-candidate` (ADR-005) because the anthology's training-optimization topic could hold an optimizer that its multi-task papers build on. Not held in the Anthology of the SOTA: a grep of its record/ (clone of 2026-10-18, commit d1573d2) for the authors and the title found nothing.
tags:
- mathematics
- operations-research
- anthology-candidate
date: '2026-10-18'
published: '2009-06-01'
doi: '10.1016/j.crma.2012.03.014'
first_author: 'Désidéri'
keywords:
- 'multiobjective optimization'
- 'Pareto stationarity'
- 'steepest descent'
- 'common descent direction'
implementations: []
summary: >-
  Désidéri (2012; first as an INRIA report, 2009). When a design point is not Pareto-optimal, a descent direction common to all smooth criteria exists and can be constructed (the minimum-norm element of the convex hull of the gradients); steepest descent along it converges to a Pareto-stationary point.
---

# LIT-tmp9l7jj: Multiple-gradient descent algorithm (MGDA) for multiobjective optimization

Désidéri, J.-A. (2012). Multiple-gradient descent algorithm (MGDA) for multiobjective optimization. *Comptes Rendus Mathématique* 350(5–6): 313–318. doi:10.1016/j.crma.2012.03.014. First as INRIA Research Report RR-6953, "Multiple-Gradient Descent Algorithm (MGDA)", June 2009.

Not read. The summary is drawn from the abstract or from what the work is
standardly cited for. A reading should check it first.

## Why this is here

A33 of the exchange used its criterion, without a source: "If zero lies in the convex hull of the task gradients, there is no common strict first-order descent direction" (0 ∉ conv{g_1,…,g_n}). A34's dual certificate and A35's residual build on it. Bears on CLAIM-tmpuia0a (common first-order descent is invariant under reparameterization; the sign of a gradient inner product is not) and CLAIM-tmpue67e (the residual's dual certificate and governance regret).
