---
number: 767
status: Read
formerly:
- NOTE-tmp7fp7t
paper: LIT-998
title: 'Tononi, Sporns & Edelman — A measure for brain complexity'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the five scanned page images of the PNAS article
    (pp. 5033–5037) on PubMed Central, article PMC43925, read as images:
    abstract, introduction, Theory (Eqs. 1–6), Computer Implementations,
    Results (Figs. 1–3 and captions), Discussion and the 20 references.
    PMC's PDF link and Europe PMC's render returned a browser challenge,
    not a file. The scans are clear for the text and equations; the axis
    labels and some in-figure values of Figs. 1 and 3 are too faint to
    read, so only values printed legibly (Fig. 2D) are quoted.
date: '2026-10-14'
summary: >-
  Defines neural complexity C_N as the summed shortfall of average subset
  integration below a linear increase with subset size, equivalently the
  average mutual information across bipartitions summed over sizes. It is
  zero for independent parts, low for uniformly dependent ones and high
  when the two coexist. In simulated cortex, patchy grouped connectivity
  gives higher C_N than the same connections spread randomly. One number
  for a whole system, with no partition, threshold or penalty.
---
<!-- inactive-ok-file: CLAIM-157 THEORY-097 THEORY-063 THEORY-222 THEORY-262 — Proposed; the block criterion this measure is compared with, a finding on block duration, two Tononi-line accounts named for lineage, and the account filed from this reading -->

# NOTE-767: Tononi, Sporns & Edelman — A measure for brain complexity

## Contribution

The paper gives one information-theoretic quantity for the old dispute
between localizationist and holist views of the brain. Neural complexity,
C_N, is built from the integration of subsets of every size. It rewards a
system whose small subsets are nearly independent while its large subsets
are strongly dependent. Simulations then tie high C_N to features of
cortical wiring: dense connections, local grouping, patchy long-range
connections and reciprocal links.

## Key insight

Segregation and integration are not two ends of one scale. They are
measured at different sizes of subset. Integration, the multi-information
I(X), is computed for every subset size k and averaged. Its average
should rise linearly in k if the system were "integrated the same way at
every scale". C_N is how far the actual curve falls below that straight
line. A crystal and a gas both sit on or near the line. A brain-like
system sits well below it.

## Assumptions

- **An isolated system.** "Consider an isolated neural system X with n
  elementary components (neuronal groups)." Extrinsic input is excluded:
  "we concentrate on the intrinsic properties of a neural system and,
  hence, do not consider extrinsic inputs from the environment."
- **Stationarity.** Activity is "a stationary multidimensional stochastic
  process", and the anatomical connectivity "is fixed".
- **Gaussian activity for computation.** Under it, all deviations from
  independence are in the covariances, and
  I(X) = Σᵢ ln(2πe vᵢ)/2 − ln[(2πe)ⁿ|COV(X)|]/2 = −ln|CORR(X)|/2 =
  −Σᵢ ln(λᵢ)/2, with vᵢ the variance of component i and λᵢ the
  eigenvalues of the correlation matrix.
- **Statistical sense only.** Entropy and mutual information are used
  "purely in their statistical connotation ... no assumption is made about
  messages, codes, or noisy channels".
- **Individual systems.** The measure is meaningful only for a system in
  which "no bipartition yields two statistically independent subsets
  (i.e., MI(X_j^k; X − X_j^k) ≠ 0 for all j and k)".
- **The unit is the neuronal group**, not the neuron, and the components
  are treated as homogeneous. The Discussion concedes the measure "does not
  explicitly consider the heterogeneity of the actual components".

## Key results

- **Mutual information of a bipartition (Eq. 1).**
  MI(X_j^k; X − X_j^k) = H(X_j^k) + H(X − X_j^k) − H(X). Zero if the two
  parts are independent, positive otherwise.
- **Integration (Eq. 2).** I(X) = Σᵢ H(xᵢ) − H(X), the total deviation
  from independence among the n components.
- **Integration splits over a bipartition (Eq. 3).**
  I(X) = I(X_j^k) + I(X − X_j^k) + MI(X_j^k; X − X_j^k). So
  ⟨I(X_j^{k+1})⟩ ≥ ⟨I(X_j^k)⟩: average integration rises monotonically
  with subset size, from ⟨I(X_j^1)⟩ = 0 to ⟨I(X_j^n)⟩ = I(X). Averages
  are over all n!/(k!(n − k)!) subsets of size k.
- **Neural complexity (Eq. 4).**
  C_N(X) = Σ_{k=1}^{n} [(k/n) I(X) − ⟨I(X_j^k)⟩], and C_N(X) ≥ 0.
- **In entropies (Eq. 5).** C_N(X) = Σ_{k=1}^{n} [⟨H(X_j^k)⟩ − (k/n) H(X)].
- **In mutual information (Eq. 6).**
  C_N(X) = Σ_{k=1}^{n/2} ⟨MI(X_j^k; X − X_j^k)⟩: the average mutual
  information between a subset and the rest, summed over bipartition
  sizes. So C_N is high when, on average, every part shares much
  information with the rest.
- **The two extremes (Fig. 1).** Gaussian Toeplitz covariance matrices,
  n = 64, with correlation length σ varied from 10^−0.5 (independence) to
  10^5 (all coefficients near 1), plus 10% uncorrelated noise. C_N is very
  low at both ends and maximal in between, "when the coefficients in the
  matrix spanned the entire range between 0 and 1". C_N rises with I from
  0 to a maximum and then falls. *Holds for:* this one family of
  covariance matrices; it is a worked example, not a theorem.
- **Simulated visual cortex (Fig. 2).** 512 neuronal groups in two 16 × 16
  arrays, each group 40 excitatory and 20 inhibitory units, driven by
  Gaussian noise with no external input; C_N computed on the central
  12 × 12 of each array over 10,000 time steps. Read from Fig. 2D:
  - the model's patchy pattern (case b) gives C_N = 2244.7;
  - the same pattern at half the connection density (case a) gives
    C_N = 542.35, with little synchrony and low I(X);
  - the same number and strength of intergroup connections spread
    uniformly (case c) gives C_N = 1240.2. Here I(X) is highest: the
    groups lock "in a globally synchronized state".
  *Holds for:* one connectivity model taken from the authors' earlier
  work (ref. 11), one realisation of each case.
- **Patchiness in linear systems (Fig. 3A).** Linear systems with n = 8,
  each component receiving fixed total weight w = 0.9 from m others.
  Covariance is solved analytically: with Q = [1 − CON(X)]⁻¹,
  COV(X) = Qᵀ·Q for uncorrelated unit noise. Normalised complexity
  C_N/I rises as connections concentrate from uniform (m → 7) to patchy
  (m → 1). Each point is the mean ± SD over 1,000 random networks.
- **Reciprocity (Fig. 3B).** In 10,000 random linear systems (n = 8,
  m = 2, w = 0.9), C_N and I vary widely and are "dissociated". At
  constant I, C_N tends to rise with the number of reciprocal pairs; I
  does not. At lower w both rise with reentrant circuits ("data not
  shown").
- **Grouping.** Dissolving group structure by redistributing local
  collaterals "resulted in a marked decrease of C_N (data not shown)".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | C_N can be written equivalently as integration shortfall, entropy excess, or summed bipartition mutual information | strong | algebra from Eqs. 1–3 (Eqs. 4–6) |
| C2 | C_N is low for independent and for uniformly dependent components and high in between | moderate | one Toeplitz family, Fig. 1; consistent with the definition |
| C3 | In a simulated visual area, patchy grouped connectivity yields higher C_N than the same connections spread uniformly | moderate | one simulation per case, Fig. 2 |
| C4 | Concentrating a fixed amount of connection on fewer partners raises C_N/I in small linear systems | moderate | 1,000 random networks per point, Fig. 3A |
| C5 | At constant integration, more reciprocal connections go with higher C_N | weak | a tendency in one population of 10,000 networks, Fig. 3B inset |
| C6 | Grouping of neurons raises C_N | weak | "data not shown" |
| C7 | Human neuroimaging covariance will show high C_N, and conscious waking will show higher C_N than slow-wave sleep | weak | a prediction; preliminary data unpublished |

## Method

1. Fix the components (neuronal groups) and obtain the covariance or
   correlation matrix of their stationary activity, from simulation or
   analytically for linear systems.
2. For each subset size k, compute I(X_j^k) = −ln|CORR(X_j^k)|/2 for
   every subset (k ≤ 8) or a small random sample (k > 8), and average.
3. Sum the shortfall of the averages below the line (k/n)·I(X).

Computed in MATLAB 4.1; simulations ran on an nCUBE parallel computer.

## Concepts

- **Functional segregation.** "Relative statistical independence of small
  subsets of the system".
- **Functional integration.** "Significant deviations from independence of
  large subsets". Formally I(X), the multi-information of the whole.
- **Neural complexity C_N.** The summed difference between the linear
  expectation and the observed average integration over subset sizes.
  Roughly, "how much more integrated the whole is than its parts".
- **Neuronal group.** A local collective of "strongly interconnected cells
  sharing inputs, outputs, and response properties" (from Edelman's
  neuronal group selection). The paper's component.
- **Reentry.** "Ongoing recursive signaling among neuronal groups and areas
  across massively parallel paths", carried by reciprocal connections.
- **Patchiness.** Intergroup connections that cluster in a few discrete
  target patches ("axonal patches"), not spread uniformly.

## Connections

The paper builds on the authors' simulations of reentrant integration in
the visual system (Tononi, Sporns & Edelman 1992; Sporns, Tononi & Edelman
1991) and on Edelman's neuronal group selection. It takes entropy and
mutual information from Shannon and Papoulis, and the subset averages from
Gatlin. The Discussion places it among attempts in physics to define
complexity between randomness and regularity (Zurek's 1990 volume).
Later work by Tononi, Sporns and Edelman, the dynamic core and then
integrated information, descends from it. [THEORY-063](../theory.d/THEORY-063.md) cites Tononi and
Edelman's dynamic core, and [THEORY-222](../theory.d/THEORY-222.md) cites Hoel, Albantakis and Tononi
(2013) on effective information at macro scales. Neither rests on this
paper.

## Bearing on the record

- **[QUESTION-042](../questions.d/QUESTION-042.md).** [LIT-998](../literature.d/LIT-998.md) was filed as "the rival measure the
  Occam-priced block test must be compared with". The reading shows it is
  not a rival of the same kind.
  - **The block test partitions; C_N does not.** [CLAIM-157](../claims.d/CLAIM-157.md) and
    [CLAIM-154](../claims.d/CLAIM-154.md) pick out a block, a unit with a boundary, and price
    whether its gap beats the Occam factor. C_N is one number for a whole
    system whose components are already fixed. It averages over all
    subsets of a size and returns no boundary, no unit and no scale.
  - **It has no threshold and no penalty.** C_N is a population quantity
    computed from a known covariance matrix. Nothing in it prices
    estimation from data, so it cannot by itself say whether a structure
    is "worth naming".
  - **It does contain a unit criterion, without a price.** The paper
    treats a system as an individual only if "no bipartition yields two
    statistically independent subsets". That is a test of oneness: every
    cut must carry nonzero mutual information. It is the zero-threshold
    limit of the gap test, with no Occam factor. That is the point of
    contact with [CLAIM-157](../claims.d/CLAIM-157.md), and the comparison the question wants.
  - **What it adds.** A high C_N in Fig. 2 comes with grouped, patchy
    wiring, so near-decomposable blocks raise it. The measure detects
    that blocks exist, not where they are. It cannot answer the question's
    "at the anatomical boundaries" or "how long", and it assumes
    stationarity, so it cannot see blocks that last about 70 ms
    ([THEORY-097](../theory.d/THEORY-097.md)).
- **No THEORY or CLAIM cites this paper.** None misstates it.
- **Filed from this reading:** [THEORY-262](../theory.d/THEORY-262.md), the measure's two-extremes
  property and its link to patchy connectivity, at the strength the
  simulations give.
- No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- Every result is from simulation or from analytic linear systems. "A full
  validation ... requires their application to data obtained directly
  from brains in vivo." The neuroimaging claim rests on unpublished data.
- Fig. 1's two-extremes property is shown for one family of Gaussian
  matrices, not proved in general.
- Several key effects (grouping, reciprocity at lower w) are "data not
  shown".
- Stationary, Gaussian and isolated. The authors grant it "is not yet
  apparent" whether the measure extends to nonstationary conditions, and
  extrinsic input is excluded.
- The components are homogeneous, and their choice is taken as given.
  C_N depends on it, and the paper does not say how to choose them.
- C_N grows with n and with I. The paper normalises by I in Fig. 3A but
  gives no general normalisation.

## Open questions

- Is C_N high in recorded brains, and higher in waking than in slow-wave
  sleep, as predicted? That needs a covariance from recorded activity.
- Does the measure extend to temporal patterns and nonstationary activity?
  The authors leave it open.
- How does neural complexity change with extrinsic input and experience?
  The final paragraph asks "how neural complexity is altered by a
  succession of diverse signals from the world".
- For the record: on a recorded brain, would the components that maximise
  C_N match the blocks a gap-and-Occam test selects? Neither the paper
  nor the record computes both.
