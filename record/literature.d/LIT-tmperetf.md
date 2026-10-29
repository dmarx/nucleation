---
status: Active
status_note: >-
  read in full 2026-10-29 (NOTE-tmp4gy4z); the citable description of the
  POT library as of 2021. Worth citing for the library, with the version
  used, but not for fused or partial Gromov–Wasserstein or co-optimal
  transport, which this paper does not describe.
title: 'POT: Python Optimal Transport'
version: 2
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Filed, not read, from A5, A6 of the exchange "Paper assessment"
    (2026-10-28 to 29). `published:` is the PDF's "Published 4/21",
    April 2021 only (JMLR 22(78), 1–8); no arXiv copy or DOI was found
    (ADR-002).
- version: 2
  date: '2026-10-29'
  note: >-
    Read in full from the JMLR PDF, 8 pp., in NOTE-tmp4gy4z. No THEORY:
    a software paper. Summary corrected: the paper names
    Gromov–Wasserstein and partial OT, not fused, partial or unbalanced
    GW, nor co-optimal transport; those are in later releases of the
    library (checked in POT 0.9.7). Tagged anthology-candidate (ADR-005):
    its content is tooling for machine-learning practice. The citation
    stands.
tags:
- mathematics
- anthology-candidate
date: '2026-10-29'
published: '2021-04-01'
url: 'https://jmlr.org/papers/v22/20-451.html'
first_author: 'Flamary'
keywords:
- 'optimal transport'
- 'Python toolbox'
- 'Sinkhorn algorithm'
- 'Wasserstein barycenters'
- 'open source'
implementations:
- 'https://github.com/PythonOT/POT'
summary: >-
  Flamary et al. (2021). A software paper for POT, an MIT-licensed Python
  library of optimal transport solvers as of 2021: exact transport by a
  C++ solver, entropic transport by Sinkhorn and stabilized variants,
  Wasserstein barycenters, partial and unbalanced transport, regularized
  transport with generic solvers, Gromov–Wasserstein, sliced Wasserstein
  and domain adaptation, tested to 92% line coverage. It compares
  features with OTT, OTJulia and GeomLoss and reports no benchmarks.
  Fused and partial Gromov–Wasserstein and co-optimal transport are not
  in it.
---

# LIT-tmperetf: POT: Python Optimal Transport

Flamary, R., Courty, N., Gramfort, A., et al. (2021). POT: Python optimal transport. *Journal of Machine Learning Research*, 22(78), 1–8.

Read in full in NOTE-tmp4gy4z.

## Key takeaways

- A citable description of the library, its solvers and its engineering;
  no results and no benchmarks.
- What POT offers depends on the version; this paper fixes the 2021 set.

## Why this is here

Named by A5 and A6 as the tool for every transport arm of CASE-tmph0fxi: GW, fused and partial GW, and co-optimal transport (`ot.coot`). Registered as the paper that stands for the software.

The paper covers less than that. It names GW and partial OT, not fused GW,
partial GW or `ot.coot`, which later releases added. For those arms the
methods' own papers (LIT-tmpjs7kp, LIT-tmpbnbe3) and the POT version used
should be cited beside this one (NOTE-tmp4gy4z).
