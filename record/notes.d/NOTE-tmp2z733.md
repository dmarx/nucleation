---
status: Read
paper: LIT-2974
title: 'Krapivsky, Redner and Leyvraz, Connectivity of Growing Random Networks, read for how the attachment kernel decides the degree distribution'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Read on 2026-11-22 by a delegated reader from the arXiv preprint
    (https://arxiv.org/pdf/cond-mat/0005139, v2 of 18 Sep 2000, the
    authors' manuscript, 4 pp.), in full: text, Figs. 1 and 2 and their
    captions, Eqs. 1 to 17 and the 21 references. Nothing skipped. The
    published Physical Review Letters version (85, 4629) was not consulted,
    so page numbers are the preprint's. Every quotation the filing leans on
    rechecked by the filer by script against the preprint's text. No email
    address sent to any service.
date: '2026-11-22'
summary: >-
  An exact rate-equation solution for a growing tree whose new sites attach
  with probability proportional to a kernel A_k. For A_k = k^γ: exponential
  at γ = 0, stretched exponential for 0 < γ < 1, a single "gel" site taking
  nearly all links for γ > 1 (with a cascade of transitions at
  γ = (m+1)/m), and a power law only at γ = 1. Within the linear case the
  exponent is not universal: A_k → a∞k gives ν = 1 + μ/a∞, anywhere in
  (2, ∞). The authors warn that for 0.8 ≲ γ ≲ 1 a stretched exponential
  and a power law are hard to tell apart up to k = 1000.
---
<!-- inactive-ok-file: CLAIM-817 CLAIM-806 CLAIM-830 CLAIM-803 CLAIM-796 ARG-149 THEORY-188 THEORY-tmpmsncg ARG-tmpqxprw SYNTHESIS-119 — Proposed or new; the reading of this work, the argument filed with it and the entries it bears on -->
<!-- inactive-ok-file: LIT-tmphxpqu — Deferred; Dorogovtsev, Mendes and Samukhin, registered from this reading and unread -->

# NOTE-tmp2z733: Krapivsky, Redner and Leyvraz, Connectivity of Growing Random Networks, read for how the attachment kernel decides the degree distribution

## Contribution

An exact solution, by rate equations, for the whole family of
degree-dependent attachment kernels in a growing tree. It shows that a
power-law degree distribution is the borderline case of linear attachment,
flanked by stretched exponentials below and condensation onto one site
("gelation") above, and that within the linear case the exponent is set by
the kernel's details, not fixed at 3. The reading is THEORY-tmpmsncg.

## Key results

Page numbers are the preprint's.

- **The model** (p. 1). At each step a new site joins and links to an
  earlier site with k links, chosen with probability A_k/ΣA_jN_j. The graph
  is a directed tree; k counts the k − 1 incoming links and the one
  outgoing link. The rate equation for N_k (Eq. 1) has a source term for
  "the continuous introduction of new sites with no incoming links".
- **Three regimes** (abstract): "For γ < 1, the number of sites with k
  links, N_k, varies as stretched exponential. For γ > 1, a single site
  connects to nearly all other sites. In the borderline case A_k ∼ k, the
  power law N_k ∼ k^−ν is found, where the exponent ν can be tuned to any
  value in the range 2 < ν < ∞."
- **Only γ = 1** (p. 1): "A power law distribution N_k ∼ k^−ν arises only
  for γ = 1. In this case, finer details of the dependence of the
  connection kernel on k affect the exponent ν."
- **Linear kernel exactly** (p. 2, Eq. 2): n_k = 4/[k(k+1)(k+2)] ∼ k^(−3),
  from n_k = n_{k−1}(k−1)/(k+2).
- **No preference** (p. 2): at γ = 0, μ = 1 and "the corresponding
  connectivity distributions are given by n_k = 2^−k".
- **Sublinear** (p. 2, Eq. 5): n_k ∼ k^(−γ) exp[−μk^(1−γ)/(1−γ)] for
  1/2 < γ < 1, with more terms in the exponent "Whenever γ decreases below
  1/m".
- **Hard to tell apart** (p. 2): for 0.8 ≲ γ ≲ 1 "n_k depends weakly on γ
  for 1 ≤ k ≤ 1000. Thus, it is difficult to discriminate between different
  γ's and even to distinguish a power law from a stretched exponential in
  the GRN model."
- **Tunable exponent** (p. 2, Eqs. 7 and 8). For A_k → a∞k, n_k ∼ k^(−ν)
  "with ν = 1 + µ/a∞". For A_1 = 1 and A_k = a∞k (k ≥ 2),
  ν = (3 + √(1 + 8/a∞))/2, which "can indeed be tuned to any value larger
  than 2". Checked with python3 -I: a∞ = 1 gives ν = 3, the pure linear
  kernel; a∞ = 2 gives 2.618 and a∞ = 1/2 gives 3.562; ν → 2 as a∞ → ∞.
- **Superlinear: gelation** (pp. 1, 3). "The case γ > 1 leads to
  phenomenon akin to gelation [19] in which a single “gel” site connects
  to nearly every other site of the graph. For γ > 2, this phenomenon is so
  extreme that the number of connections between other sites is finite in
  an infinite graph." For 1 < γ < 2, "the remaining t links must all
  connect to a single site which has t connections" (p. 3); and "for γ > 2
  there is a non-zero probability that the initial site connects to all
  other sites" (p. 3, Eq. 9).
- **A cascade of transitions** (p. 3): "for (m+1)/m < γ < m/(m−1), the
  number of sites with more than m links is finite", with "Logarithmic
  corrections" at the transition points themselves. The paper's own name
  for γ > 1 is "winner take all".
- **Largest degree** (p. 3, Eq. 13): k_max ∼ (ln t)^(1/(1−γ)) for sublinear
  kernels, t^(1/(ν−1)) for asymptotically linear ones, t for superlinear.
  On ISI citation data (783,339 papers, the most cited with 8,904): "This
  accords with the first line of Eq. (13) for γ ≈ 0.86, and also with the
  second when ν ≈ 2.5."
- **Age** (p. 4, Eqs. 14 to 17): for A_k = k the joint age and degree
  distribution is self-similar in a/t, and "old sites are better
  connected". The kernel has no explicit aging.

## Assumptions

- One link per new site, so the graph is a tree.
- A kernel depending on degree only: no fitness, no aging.
- Continual entry, one site per unit time (the δ_k1 source term). The
  no-entry case is never run.
- Mean-field rate equations for the averages N_k; fluctuations are not
  treated, except the γ > 2 probability P.
- k counts the outgoing link, so A_k = k is Barabási–Albert attachment on
  total degree with m = 1.
- The long-time limit.

## Concepts

Connection kernel A_k; homogeneous kernel k^γ; asymptotically linear
kernel; rate (master) equation for N_k; the amplitude μ of
M_γ = Σk^γN_k = μt; stretched exponential; gelation and the "gel" site;
"winner take all"; connectivity transitions at γ = (m+1)/m; the most
popular site k_max; the age-and-connectivity distribution c_k(t, a).

## Connections

Reference 20 is Dorogovtsev, Mendes and Samukhin (cond-mat/0004434,
Physical Review Letters 85, 4633), with overlapping results for the linear
case, registered here as LIT-tmphxpqu and unread. Reference 16, Redner's
citation data, is not held.

## Bearing on the record

- **CLAIM-817** (supports the kernel half; leaves open the entry half).
  The claim's four regimes are the paper's, derived exactly, and "A power
  law distribution N_k ∼ k^−ν arises only for γ = 1". The exchange's last
  row ("potentially winner-take-all") is too weak: the paper says "winner
  take all" without hedging, and the claim's correction, condensation onto
  one node, is the paper's. The paper always has entry, so the claim's
  "together with continual entry" is not tested here. The `grounds` entry
  ARG-149 said the regimes rest on; ARG-tmpqxprw.
- **CLAIM-806** (supports the marginality; qualifies the table). The paper
  calls γ = 1 "the borderline case" and γ > 1 "akin to gelation". The
  table's "k^(−3)" holds only for A_k = k; the borderline is the class of
  asymptotically linear kernels, with ν anywhere above 2, which is the
  claim's "line in a larger space of kernels" with the exponent now checked
  (ν = 1 + μ/a∞). Above the boundary is a cascade of transitions, not a
  single regime. Its `defeated_if` is not met: no γ ≠ 1 tail is a power
  law. ARG-tmpqxprw.
- **CLAIM-796** (contrast). The claim CLAIM-806 objects to; "the
  borderline case" is evidence for the objection.
- **ARG-149** (supports its verdict). The argument says the kernel regimes
  rest on this work; read, they do.
- **NOTE-2237** (parallel). Mitzenmacher's mixing model moves the exponent
  by mixing uniform with linear attachment, c_j ∼ j^(−(2−α)/(1−α)); this
  paper's asymptotically linear kernel moves ν the same way. Two routes to
  one fact, a non-universal exponent within linear attachment.
- **CLAIM-830** (supports the role of entry in the solution; leaves the
  no-entry case open). The source term is "the continuous introduction of
  new sites", and "old sites are better connected" fits the age mechanism.
- **CLAIM-803** (supports one clause). The indistinguishability remark and
  the ISI fit that fits both a stretched exponential and a power law are
  instances of "a power law does not identify its mechanism".
- **QUESTION-505** (bears on it). ν − 1 = μ/a∞ is another ratio, the
  normalisation's growth rate over the kernel's asymptotic slope, and one
  the kernel tunes; also a counterweight, since μ depends on the whole
  kernel (Eq. 8), not on two named rates.
- **SYNTHESIS-119** (background). Its cumulative-advantage line rests on
  CLAIM-817, which this reading grounds.
- **NOTE-678**, **THEORY-188** (background). NOTE-678 names "the standard
  master-equation treatment of growing networks" of this paper; no new
  bearing.

## Limitations

- Mean-field rate equations for averages; trees only; degree-only kernels.
- The stretched-exponential asymptotics are worked for γ > 1/3, with the
  pattern stated beyond.
- The γ > 1 analysis is leading order, with the logarithmic corrections at
  transition points not worked out.
- The ISI test fits k_max with two different models (γ ≈ 0.86 or
  ν ≈ 2.5), which by the authors' own account does not separate them.
- A four-page letter; the general-kernel age solution is deferred to a
  longer paper (ref. 21), not read.
