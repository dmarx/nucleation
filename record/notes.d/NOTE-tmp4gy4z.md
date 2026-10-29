---
status: Read
paper: 'LIT-tmperetf'
title: 'Flamary et al. — POT'
version: 1
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Read in full from the JMLR PDF (volume 22, paper 20-451; "Submitted
    5/20; Revised 1/21; Published 4/21"), 8 pp., CC BY 4.0, extracted with
    `pdftotext -layout`. Table 1's check marks did not survive extraction,
    so p. 3 was rendered and read as an image. Read: abstract, §§1–5, both
    code samples, Table 1, footnotes, acknowledgements and references. No
    THEORY is filed: the paper reports software, not a result. As a check
    of the record's description, not of the paper, POT 0.9.7 installed from
    PyPI has `ot.coot.co_optimal_transport`,
    `ot.gromov.fused_gromov_wasserstein` and
    `ot.partial.partial_gromov_wasserstein`; none of these is named in the
    2021 paper.
date: '2026-10-29'
summary: >-
  A software paper for POT, an MIT-licensed Python library of optimal
  transport solvers: exact transport by a C++ solver,
  entropic transport by Sinkhorn and stabilized variants, Wasserstein
  barycenters, partial and unbalanced transport, regularized transport,
  Gromov–Wasserstein, sliced Wasserstein and domain adaptation, with tests
  covering 92% of lines. It reports no experiments. Fused and partial
  Gromov–Wasserstein and co-optimal transport, which the record uses POT
  for, are not in this paper; they came in later releases.
---

# NOTE-tmp4gy4z: Flamary et al. — POT

## Contribution

It documents the Python Optimal Transport library as of early 2021 and
gives it a citable reference. It states what the library solves, how it
is engineered and maintained, and how it compares with three other OT
packages. It proves nothing and runs no benchmark.

## Key insight

The paper's own pitch is breadth and reliability, not speed: "generic
solvers that can be used for conducting novel fundamental research"
(abstract, p. 1), tests on every contribution, and closed-form cases used
to check correctness (p. 4). For deep-learning use of Sinkhorn losses the
authors point elsewhere: GeomLoss "is currently a better alternative to
POT for using Sinkhorn losses in deep learning architectures" (p. 3).

## Assumptions

- Discrete measures throughout: histograms a, b and a cost matrix M
  (eq. 1, p. 3).
- Dependencies NumPy, SciPy, Cython over C++; Pymanopt and Autograd for
  some sub-modules; CuPy for GPU entropic OT (p. 5).

## Key results

- **Problems solved (§3, pp. 3–4):** the Kantorovich linear program
  W_M(a, b) = min ⟨T, M⟩ over Π(a, b) (eq. 1); its entropic and squared-L2
  regularizations; Wasserstein barycenters, entropic by Bregman projections
  or exact by LP (eq. 2, Sample 2). "ot.gromov and ot.partial contain
  respectively solvers for Gromov-Wasserstein and partial OT problems"
  (p. 4); ot.da for domain adaptation with a scikit-learn API; ot.optim for
  user-specified regularizers.
- **Table 1 (p. 3), POT's column:** EMD, Sinkhorn, stabilized Sinkhorn,
  unbalanced/partial OT, regularized OT, Wasserstein barycenter,
  Gromov–Wasserstein, sliced Wasserstein and domain adaptation checked;
  GPU partial; multiscale EMD not. In the table only POT has
  Gromov–Wasserstein.
- **Engineering (§4, pp. 4–5):** PEP8; tests for every contribution "with a
  line coverage of 92% of the code"; continuous integration; "more than 20
  collaborators"; "more than 25 examples"; the exact solver is a C++ one by
  Bonneel et al. (2011). A PyTorch backend was "currently underway"
  (p. 5).
- **Uptake:** "more than 5K downloads each month on PyPI" (p. 2).
- **Others (§2, pp. 2–3):** OTT is "still considered a preliminary
  version"; OTJulia wraps POT for exact EMD.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | POT implements the solvers listed in Table 1 | strong | the paper's description; the code is public |
| C2 | All functions and classes are tested, 92% line coverage | moderate | stated (p. 4); not checked |
| C3 | POT is the broadest of the four packages compared | moderate | Table 1, the authors' own comparison, as of 2021 |

## Concepts

- **Wasserstein distance** — the optimal value of eq. (1) when M is a
  metric: "When the ground cost is a metric, the optimal value of the OT
  problem is also a metric" (p. 3).
- **Transport plan** — T ≥ 0 with T1 = a and Tᵀ1 = b (p. 3).

## Connections

It packages methods the record holds as papers: Gromov–Wasserstein
averaging (Peyré, Cuturi and Solomon 2016; [LIT-tmpprsxm](../literature.d/LIT-tmpprsxm.md)) and the GW
machinery behind network GW ([LIT-tmpu05fk](../literature.d/LIT-tmpu05fk.md)). Later POT releases add fused
GW ([LIT-tmpjs7kp](../literature.d/LIT-tmpjs7kp.md)) and co-optimal transport ([LIT-tmpbnbe3](../literature.d/LIT-tmpbnbe3.md)), which are not
in this paper. HOT ([LIT-tmpko4oy](../literature.d/LIT-tmpko4oy.md)) and AvAtar ([LIT-tmpe5bbx](../literature.d/LIT-tmpe5bbx.md)) use their
own code.

## Bearing on the record

- **[CASE-tmph0fxi](../cases.d/CASE-tmph0fxi.md): the LIT overstates what this paper covers.** The
  exchange named POT as the tool for every transport arm of the case, "GW,
  fused and partial GW, and co-optimal transport (`ot.coot`)". The 2021
  paper names Gromov–Wasserstein and partial OT (p. 4), not fused GW, not
  partial GW, not co-optimal transport. The library has them now (checked
  in POT 0.9.7), so the case's tooling is right; the citation that stands
  for it should be this paper for the library and the methods' own papers,
  [LIT-tmpjs7kp](../literature.d/LIT-tmpjs7kp.md) and [LIT-tmpbnbe3](../literature.d/LIT-tmpbnbe3.md), for those arms, with the POT version
  stated.
- **No THEORY.** The paper reports software and makes no claim about what
  is true of any system.
- **Practice.** Its content is tooling for machine-learning practice, a
  library and how to use it. If the anthology wants it, that is its
  question; the LIT carries anthology-candidate.

## Limitations

- No benchmarks, no timings, no comparison of accuracy with other packages;
  Table 1 compares features only, as the authors saw them in 2021.
- It describes a moving target ("evolves quickly", p. 5). Which functions
  exist depends on the version, which the paper's citation does not fix.

## Open questions

- None about the paper. For the record: which POT version a study used
  should be stated wherever POT is cited for a method this paper does not
  describe.
