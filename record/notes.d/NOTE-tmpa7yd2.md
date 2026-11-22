---
status: Read
paper: LIT-2976
title: 'Newman, Power laws, Pareto distributions and Zipf''s law, read for how power laws are measured and the many mechanisms that make them'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Read on 2026-11-22 by a delegated reader from arXiv
    (arxiv.org/pdf/cond-mat/0412004, resolving to v3 of 29 May 2006, the
    author's manuscript, 28 pages), text extracted with pdftotext. Read in
    full: §§I–V and Appendices A (rank/frequency plots) and B (the
    maximum-likelihood exponent). Skimmed: the figure data and the
    reference list, consulted to identify Simon, Miller, Reed and Hughes,
    Carlson and Doyle, Sneppen and Newman, and Sibani and Littlewood. v3
    postdates the journal text (Contemporary Physics 46, 323–351, 2005);
    the differences were not checked, and Table I's exponents were not
    re-examined. Page numbers are the PDF's. Every quotation below
    rechecked by the filer by script against the downloaded text, and the
    exponent identities checked with python3 -I. No email address sent.
date: '2026-11-22'
summary: >-
  A tutorial review, not a source of new results: measure a power law with
  a cumulative plot and a maximum-likelihood exponent, not a least-squares
  line on a log-log histogram; and many mechanisms make one (combinations
  of exponentials, inverses, random-walk first return times, the Yule
  process, criticality, self-organized criticality, highly optimized
  tolerance, coherent noise, multiplicative processes with a floor, record
  dynamics), different ones in different cases. It covers four of the
  seven items of CLAIM-795, has nothing on branching processes or the
  hitting-time identity, and ranks the Yule process and criticality as
  the two most important.
---
<!-- inactive-ok-file: CLAIM-795 CLAIM-815 CLAIM-803 CLAIM-841 CLAIM-817 CLAIM-830 CLAIM-824 CLAIM-769 THEORY-2131 THEORY-2150 THEORY-tmp6jdas ARG-tmp3ppjy ARG-tmp275n1 TERM-tmpg1vx2 — Proposed; the entries this reading bears on, its own reading and the arguments and term filed with it -->
<!-- inactive-ok-file: LIT-3007 LIT-2992 LIT-2997 LIT-2962 LIT-tmp7g7aj LIT-tmppzucs LIT-tmp2octb LIT-tmp1db7e LIT-tmpf9hct — Deferred; works this reading names, registered and unread -->

# NOTE-tmpa7yd2: Newman, Power laws, Pareto distributions and Zipf's law, read for how power laws are measured and the many mechanisms that make them

## Contribution

A pedagogical synthesis in three parts: how to measure a power law (§II),
its mathematics (§III), and the mechanisms proposed for it (§IV). It put
the cumulative plot and the maximum-likelihood exponent into common use,
later superseded on the fitting side by Clauset, Shalizi and Newman
(LIT-2987), and set out the standard catalogue of mechanisms, holding
that "the conventional wisdom is that there are actually many different
mechanisms for producing power laws and that different ones are
applicable to different cases" (§II.A, p. 5). The reading is
THEORY-tmp6jdas.

## Key results

- **The log-log histogram is a poor test** (§II, p. 3): "Just making a
  simple histogram, however, and plotting it on log scales to see if it
  looks straight is, in most cases, a poor way proceed" [sic]. Least
  squares "is known to introduce systematic biases into the value of the
  exponent" (p. 4): on synthetic data with α = 2.5 it gives 2.26 ± 0.02,
  where the estimator α = 1 + n[Σ ln(x_i/x_min)]^(−1) (Eq. 5, error
  (α − 1)/√n) gives 2.500 ± 0.002.
- **Alternatives** (§II.B, p. 8): "a power-law model is only one of
  several possibilities for fitting it"; some of Fig. 4's identifications
  "should be considered unconfirmed" (p. 7).
- **Scale-free means power law** (§III.E, p. 11): "a power law is the
  only distribution that is the same whatever scale we look at it on",
  from p(bx) = g(b)p(x). And (p. 12) "most experimentally observed power
  laws are probably not the result of phase transitions—a variety of
  other mechanisms produce power-law behaviour as well".
- **Combinations of exponentials** (§IV.A, pp. 13–14): y exponential with
  rate a and x ∝ e^(by) give "a power law with exponent α = 1 − a/b".
  Miller's random typing gives α ≃ 2; Newman objects that real word
  lengths are not exponential, then "There may still be some merit in
  Miller's argument" once length is measured in information. Reed and
  Hughes: exponential growth observed at an exponentially distributed
  time gives a power law.
- **Inverses** (§IV.B, p. 14): x = 1/y with p(y = 0) finite gives
  p(x) ∝ x^(−2); x = y^(−γ) gives "α = 1+1/γ". To the objection that this
  "merely generates a power law by assuming another one", the input is a
  physical power-law relation, not a distribution. Simulated Ising
  magnetization fluctuations give α = 1.98 ± 0.04.
- **Random walks** (§IV.C, pp. 15–16): by generating functions, the first
  return to the origin of a symmetric ±1 walk has f_2n ∝ n^(−3/2), "So
  the distribution of return times follows a power law with exponent
  α = 3/2", with a divergent mean (gambler's ruin). Fossil genus
  lifetimes give α = 1.7 ± 0.3, which footnote 16 calls "tenuous".
- **The Yule process** (§IV.D, pp. 16–19). After Simon, p_k = (1 + 1/m)
  B(k, 2 + 1/m), α = 2 + 1/m; for flowering plants m ≃ 2 gives 2.5,
  matching Willis and Yule, but "Most likely this agreement is
  fortuitous" (p. 18). The general form, with initial value k0 and
  offset c, gives α = 2 + (k0 + c)/m; Barabási and Albert's c = m (with
  k0 = 0) gives α = 3, "but again there doesn't seem to be a good reason
  for this assumption" (p. 19). Names (p. 18): Simon "dubbed this type
  of “rich-get-richer” process the Gibrat principle"; also the Matthew
  effect, cumulative advantage and preferential attachment. "For several
  of the distributions shown in Fig. 4, especially citations, city
  populations and personal income, it is now the most widely accepted
  theory" (p. 19).
- **Criticality** (§IV.E, pp. 19–21): the need to tune "makes the
  divergence of length-scales an unlikely explanation for generic
  power-law distributions" (p. 19). Percolation at p_c = 0.5927462, and a
  coarse-graining argument for a scale-free cluster distribution ("I've
  had to fudge things around the edges", p. 20); no value of τ is given.
- **Self-organized criticality** (§IV.F, pp. 21–22): the forest-fire model
  gives α = 1.19 ± 0.01, cut off at the lattice size; "it is probably not
  the universal law that some have claimed it to be" (p. 22).
- **Others** (§IV.G, pp. 23–24): highly optimized tolerance (Carlson and
  Doyle), coherent noise (Sneppen and Newman), the lognormal from
  products of random numbers, and "random multiplication processes can
  also generate perfect power-law distributions with only a slight
  modification: if there is a lower bound on the value that the product
  of a set of numbers is allowed to take" (p. 24); record dynamics
  (Sibani and Littlewood), with waiting times of exponent 1.
- **Conclusion** (§V, p. 24): the Yule process and criticality with
  self-organized criticality are "perhaps the two most important" of the
  mechanisms.

## Assumptions

- A continuous power law above an x_min chosen by judgement; no method for
  choosing it. The estimator of Appendix B assumes a pure power law above
  x_min.
- The Yule process without extinction, in its stationary limit.
- A heuristic coarse-graining for percolation, flagged by the author.
- A symmetric ±1 walk for the return-time result.

## Concepts

Power law, exponent, x_min; cumulative distribution and rank/frequency
plot; Zipf's law; Pareto distribution; logarithmic binning;
maximum-likelihood exponent; divergent moments; Lorenz curve and the
80/20 rule; scale-free distribution; Yule and zeta distributions; the Yule
process, Simon's "Gibrat principle", cumulative advantage, preferential
attachment; gambler's ruin and first return time; percolation and the
critical point; finite-size cutoff; self-organized criticality and the
forest-fire model; highly optimized tolerance; coherent noise; lognormal
and multiplicative process with a lower bound; record dynamics.

## Connections

Newman cites Mitzenmacher (LIT-3003, read; THEORY-2150) as a
companion review. Both have random typing, Yule and Simon, and the
lognormal against the power law; Newman adds percolation,
self-organized criticality, highly optimized tolerance, coherent noise,
inverses and record dynamics, and Mitzenmacher adds Mandelbrot's
optimization and Reed's double Pareto. Newman restates Reed and Hughes
(LIT-3007) in two sentences, a neighbour description and no stand-in
for reading it. It is the predecessor of LIT-2987: the estimator of
Eq. 5 is the same, without x_min selection or tests. Works it names that
the record now relies on are registered: Simon (LIT-tmp7g7aj), Miller
(LIT-tmppzucs), Carlson and Doyle (LIT-tmp2octb), Sneppen and Newman
(LIT-tmp1db7e) and Sibani and Littlewood (LIT-tmpf9hct). Bak, Tang and
Wiesenfeld (LIT-2992) is cited for self-organized criticality, which
Newman illustrates with the forest-fire model instead.

## Bearing on the record

- **CLAIM-795** (supports items 2, 3, 6 and 7 in part; adds four
  mechanisms). Percolation (item 2, p_c = 0.5927462), the walk's 3/2
  (item 3, as first return rather than first passage), Reed and Hughes
  (item 6: α = 1 − a/b with a = −λ and b = g is a density exponent
  1 + λ/g, a survival exponent λ/g) and x = 1/y (item 7, without the
  d-ball geometry). Nothing on items 1 (critical branching), 4 (rate
  mixtures) and 5 (sample-space reduction). Random typing, highly
  optimized tolerance, coherent noise and record dynamics are further
  mechanisms with no rich-get-richer feedback. ARG-tmp3ppjy.
- **CLAIM-815** (leaves open; a parallel). The walk's 3/2 by
  generating functions (Eqs. 51–62, pp. 15–16); no branching process, no
  cycle lemma, no Dwass. It gives one half of the coincidence and nothing
  on the identity. ARG-tmp275n1.
- **CLAIM-803** (supports the first clause, and "fit first" in part;
  milder than the claim). Many mechanisms, several reaching similar
  exponents, and most power laws probably not from phase transitions;
  maximum likelihood over least squares, and a lognormal that can look
  straight. No model comparison and none of the dynamical tests. Newman
  assigns mechanisms by plausibility: the Yule process is "the most
  widely accepted theory" for citations, cities and income.
- **CLAIM-841** (supports the distributional half). "Most experimentally
  observed power laws are probably not the result of phase transitions"
  (p. 12), and tuning makes criticality "an unlikely explanation for
  generic power-law distributions" (p. 19). None of the claim's routes
  (symmetry, a line of fixed points, KPZ, flux, coarsening) is in the
  review; footnote 1 puts non-statistical power laws out of scope.
- **CLAIM-817** (supports the linear-plus-entry half). Every Yule
  variant founds a new unit each step and attaches in proportion to k or
  k + c. Nothing on nonlinear kernels.
- **CLAIM-830** (supports the entry point implicitly; a clash of
  names). Entry is built into every Yule variant. Simon's name for the
  rich-get-richer rule is "the Gibrat principle", the name the claim
  uses for proportional growth without entry; see TERM-tmpg1vx2.
- **CLAIM-824** (supports both halves qualitatively). Products give a
  lognormal; a lower bound gives "perfect power-law distributions"
  (p. 24). No exponent condition.
- **QUESTION-505** (bears on it). Each exponent is a ratio:
  1 − a/b, 1 + 1/γ, 2 + (k0 + c)/m, the walk's 3/2. Newman notes that the
  Yule process "can produce a wide range of exponents to match the
  observations by suitable adjustments of the parameters" (p. 19).
- **LEAD-211** (background). Finite-size cutoffs at criticality and
  the forest fire's cutoff at the lattice size, not used as a test.
- **LIT-3007**, **LIT-2962** and **LIT-2997**: the first restated
  briefly; the second and third (superstatistics, sample-space reduction)
  absent from the review.
- No bearing: CLAIM-769 and THEORY-2131 (rate mixtures, absent);
  Arthur's absorbing-barrier walk, a parallel only by name.

## Limitations

- Pedagogical, with heuristic arguments the author flags; x_min by eye;
  no goodness-of-fit test and no comparison with alternatives.
- Read as the 2006 v3, not the journal text.
- Its "combinations of exponentials" is an exponential of an
  exponentially distributed variable, not a mixture of exponential rates;
  the review has no rate-mixture or superstatistics mechanism, so it does
  not carry CLAIM-795's item 4.
