---
status: Read
paper: 'LIT-tmpbs8e0'
title: 'Mirth et al. — Energy landscapes by sublevelset persistent homology'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Read on 2026-11-05 from the arXiv v2 PDF of 19 March 2021
    (https://arxiv.org/pdf/2011.00918v2), which states it is the version
    published in The Journal of Chemical Physics; text extracted by
    pdftotext, which garbles the binomial coefficients (read from the
    proofs). Read in full: the abstract, introduction, §II (sublevelset
    persistent homology and its advantages), §III (analytical landscape, MD
    simulations, computation), §IV (pentane, butane to octane, MD data,
    topological distances), §V (Theorems 1 and 2 and the proof sketch) and
    the conclusions. Skimmed: appendices A–D (proofs, Morse complex,
    Künneth formula, Morse–Smale complex).
date: '2026-11-05'
summary: >-
  Sublevelset persistent homology of a potential energy landscape: its
  zero-dimensional barcode carries the disconnectivity graph, and its
  higher-dimensional bars record transition paths the graph omits and,
  for a Morse function, critical points of every index. For the alkane
  torsional landscape on the n-torus the barcode is proved in closed form
  in every dimension; barcode distances compare analytical and MD-sampled
  landscapes and grow where sampling is poor.
---
<!-- inactive-ok-file: THEORY-tmpqzxwh CLAIM-555 CLAIM-354 THEORY-109 — Proposed or new; cited from the reading of Mirth et al. (2021) as open -->

# NOTE-tmpwvb9j: Mirth et al. — Energy landscapes by sublevelset persistent homology

## Contribution

A dictionary between the chemist's disconnectivity graph and
zero-dimensional sublevelset persistence, extended to higher dimensions; a
complete characterization of the persistent homology of the analytical
alkane landscape (Theorems 1 and 2); and barcode distances as a measure of
agreement between landscapes, even of different dimension, used to
quantify sampling.

## Key insight

The usual summary of an energy landscape, which minima merge at which
barrier, is the zero-dimensional part of a larger invariant. The lowest
barrier between two minima is where their components first join; any
other route between them, over a higher saddle, is invisible in that
summary and shows up as a loop in dimension one.

## Assumptions

- **Gas-phase single molecules**, bonds and angles fixed, nonbonded terms
  ignored, so the landscape depends only on the n = m − 3 dihedral angles
  (OPLS-UA torsion terms).
- **A Morse function** for the correspondence between bars and critical
  points; sampled landscapes are so only approximately.
- **Computation** on a cubical grid or a periodic Delaunay triangulation of
  downsampled MD frames, with the lower-star filtration.

## Key results

- **The motivation (abstract).** "there is more information to be gained
  by also considering the topology of each connected component at
  different energy thresholds (or sublevelsets)".
- **Connectivity (introduction).** "two configurations are in the same
  connected component if there is a path between the configurations that
  does not exceed the chosen energy barrier".
- **The graph's limit (introduction).** "Though disconnectivity graphs
  encode the energy barrier of the minimal energy pathway between two local
  minima, they do not represent multiple transition pathways."
- **Dimension zero (§II.B).** "indeed, the disconnectivity graph of an EL
  completely determines its 0-dimensional sublevelset persistent homology".
- **Timescales (§II.B).** "Therefore, the timescale computed from a
  disconnectivity graph alone will be an overestimate to a certain
  degree."
- **Stability (§II.B).** Persistent homology "is stable, meaning that small
  changes to the input produce only small changes in the persistent
  homology".
- **Morse–Smale (§II.B).** "it contains strictly more topological
  information than the sublevelset persistent homology", but is hard to
  visualize beyond three dimensions.
- **Counting (§IV.A).** "the number of critical points of index k in the
  energy landscape is equal to the number of k-dimensional persistent
  homology bars, plus the number of finite (i.e., not semi-infinite)
  (k − 1)-dimensional bars".
- **Theorems 1 and 2 (§V).** f_n on the n-torus is Morse with
  3^n·C(n, k) critical points of index k; its barcode has
  C(n, k) + (3^n − 1)·C(n − 1, k) bars in dimension k, C(n, k) of them
  semi-infinite and the rest of one finite length (transcribed from the
  proof, since the extracted text garbles the binomials).
- **Distances (§IV.C–D).** "An advantage of defining distances between ELs
  using persistent homology is that ELs of different dimensionality can be
  compared in this way."; for hexane, "insufficient sampling of its energy
  landscape leads to a barcode with shorter bars and delayed births".

## Concepts

- **Sublevelset**: the configurations with energy at most r.
- **Sublevelset persistent homology**: how the homology of sublevelsets
  changes as r rises, shown as a barcode.
- **Disconnectivity graph (merge tree)**: leaves at minima, internal nodes
  at the index-1 critical values that first merge them.
- **Bottleneck and 1-Wasserstein distances** between barcodes: the largest,
  or the summed, cost of the best matching. Not the synthesis's
  "bottleneck", which is a threshold over paths.

## Connections

It rests on Morse theory and the stability theorem for persistence, and
cites the use of multi-parameter persistence for robust clustering of MD
data (its ref. 22), "though this summary is only of 0-dimensional
homology". The record's minimum-energy-path and mode-connectivity works,
[LIT-653](../literature.d/LIT-653.md) and [THEORY-109](../theory.d/THEORY-109.md), measure the barrier between minima along a path,
which is this paper's merge level; it says what that summary leaves out.

## Bearing on the record

- **The synthesis's description.** The pasted synthesis on constraint
  architectures names R6 only as an unidentified arXiv paper on
  sublevel-set persistent homology of molecular energy landscapes; this
  paper fits.
  - **The bottleneck budget is the zero-dimensional merge level.** The
    synthesis's B*(A, B), the infimum over paths of the largest resource
    use along the path, is exactly the threshold at which A and B first
    lie in one component of a sublevelset: the merge level in the
    disconnectivity graph and the death of a zero-dimensional bar. Its toy
    example, two components at 1.0 merging at 1.3, is a correct use of
    dimension zero. That level keeps only the lowest barrier; alternative
    paths and their barriers are in the one-dimensional bars, which the
    synthesis does not use.
  - **Several resources at once need multi-parameter persistence.** The
    synthesis's multi-resource budgets, upward-closed sets with a Pareto
    frontier, are a multi-parameter filtration. The paper treats one
    scalar energy and mentions multi-parameter persistence only in passing,
    in a citation; it gives no support for that extension.
  - **Disconnection.** The synthesis's B* = +∞ corresponds to points never
    joined at any finite level, different components of the whole domain;
    on the paper's tori this never happens.
- **[CLAIM-555](../claims.d/CLAIM-555.md) (acceptance sets as sublevel sets; the complex as their
  nerve).** Supports as method: the paper gives the standard tool for how
  one loss's sublevel sets change topology with the threshold, and its
  stability. The claim's nerve over several losses is a step the paper
  does not take.
- **[CLAIM-354](../claims.d/CLAIM-354.md) (degrees compared by inclusion of what is viably
  reachable).** Weak: sublevelset inclusion is an order on what is
  reachable under an energy cap, a scalar case of the inclusion the claim
  uses.
- **[CLAIM-079](../claims.d/CLAIM-079.md), [THEORY-134](../theory.d/THEORY-134.md).** A zero-dimensional bar's length is a stability
  margin, how high one must climb to leave a minimum, not viability; a
  sublevelset is a constraint set, but the paper asks how its topology
  changes with r, not which states can stay in it.
- **[LIT-653](../literature.d/LIT-653.md), [THEORY-109](../theory.d/THEORY-109.md).** Their barrier along a minimum energy path is the
  zero-dimensional merge level; this paper names what that summary omits.
- Filed: [THEORY-tmpqzxwh](../theory.d/THEORY-tmpqzxwh.md).

## Limitations

- **One model family**, chosen because its landscape is a sum of identical
  one-dimensional terms; general landscapes will have no closed form.
- **Sampling**: hexane already shows gaps; all-atom hexane is omitted; "The
  computational cost of MD sampling necessary to compare the OPLS-UA and
  OPLS-AA PEL within higher-chain alkanes was prohibitive".
- **Simplified physics**: fixed bonds and angles, no nonbonded terms, gas
  phase.
- **Cost**: meshing a high-dimensional domain; the richer Morse–Smale
  complex cannot be visualized beyond three dimensions.
