---
status: Read
paper: LIT-2987
title: 'Clauset, Shalizi and Newman, Power-law distributions in empirical data, read for how to test a power law and why the lognormal is seldom excluded'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Read on 2026-11-22 by a delegated reader from arXiv
    (arxiv.org/pdf/0706.1062, v2 of 2 February 2009, the authors' upload,
    43 pages), text extracted with pdftotext. Read: the abstract, §1, §2
    with Box 1, §3.1, §3.3, §3.5, §4 with §§4.1–4.2, §5 with §§5.1–5.3,
    §6 in full with Tables 6.1–6.3, §7, and the opening of Appendix A.
    Skimmed or skipped: §3.2 and §3.4 (the estimators' performance in
    simulation; Table 3.1 glanced at), the rest of Appendix A, Appendices
    B, C (only its heading and the Vuong citation checked) and D, the
    references, and the figures (text only). Page numbers are the arXiv
    v2's, not SIAM Review's (51(4), 661–703, 2009). Every quotation and the
    US-cities rows rechecked by the filer by script against the downloaded
    text. No email address sent.
date: '2026-11-22'
summary: >-
  A complete procedure for power-law data: the exponent by maximum
  likelihood above an x_min chosen to minimize the Kolmogorov–Smirnov
  distance, a bootstrap goodness-of-fit p-value, and Vuong likelihood-ratio
  tests against the lognormal and other alternatives. On 24 data sets it
  rejects 7, finds only word frequencies convincing and excludes the
  lognormal only for HTTP sizes. Its lesson is indistinguishability more
  than refutation, and where statistics cannot decide it defers to
  mechanism; it has no dynamical tests.
---
<!-- inactive-ok-file: CLAIM-803 CLAIM-841 CLAIM-806 CLAIM-824 CLAIM-830 CLAIM-821 SYNTHESIS-119 ARG-141 THEORY-tmpw4qgu ARG-tmps95tv — Proposed; the entries this reading bears on, its own reading and the argument filed with it -->

# NOTE-tmphbwdu: Clauset, Shalizi and Newman, Power-law distributions in empirical data, read for how to test a power law and why the lognormal is seldom excluded

## Contribution

A synthesis and a standard: "Many of the methods we describe have been
discussed previously; our goal here is to bring them together to create a
complete procedure" (§1, p. 2). Its own parts are three: x_min by minimum
Kolmogorov–Smirnov distance (§3.3), a bootstrap test that refits each
synthetic set (§4.1), and a uniform reanalysis of 24 data sets (§6). The
reading is [THEORY-tmpw4qgu](../theory.d/THEORY-tmpw4qgu.md).

## Key results

- **A straight line is not enough.** "being roughly straight on a log-log
  plot is a necessary but not sufficient condition for power-law
  behavior" (§4, p. 15); again in §7 (p. 26).
- **Regression fails.** Least squares gives errors such that "the results
  they give cannot not be trusted" [sic] (§3, p. 5), and "high values of
  r2 cannot be taken as evidence in favor of the power-law form"
  (Appendix A, p. 31).
- **x_min.** "Our estimate x̂min is then the value of xmin that minimizes
  D" (§3.3, p. 11).
- **A fit is always possible.** "Regardless of the true distribution from
  which our data were drawn, we can always fit a power law" (§4, p. 14),
  and "a large p-value does not necessarily mean the power law is the
  correct distribution for the data" (§4.1, p. 17).
- **Statistics rule out; they do not choose.** "Statistical tests can be
  used to rule out specific hypotheses, but it is up to the researcher to
  decide what a reasonable hypothesis is in the first place" (§5, p. 19).
  The likelihood ratio "can tell us not only which of two hypotheses is
  favored, but also when the data are insufficient to favor either of
  them" (§5.1, p. 19).
- **Extrapolation.** "conclusions based on different fitted forms can
  differ enormously even if the forms are indistinguishable in the domain
  covered by the actual data" (fn. 10, p. 20).
- **The 24 data sets** (§6). "17 of the 24 data sets are consistent with
  a power-law distribution" (p. 23); for seven (HTTP connections,
  earthquakes, web links, fires, wealth, web hits, metabolic) the power
  law is "firmly ruled out". Only word frequencies is "truly convincing"
  (p. 26). The cutoff form "is clearly favored" for almost a dozen,
  among them fires, flares, earthquakes and web hits (p. 26).
- **The lognormal** (p. 26): it "is not ruled out for any of our data sets
  except the HTTP connections. In general, we find that it is extremely
  difficult to tell the difference between log-normal and power-law
  behavior", and "it appears unlikely that any test would be able to tell
  them apart unless we have an extremely large data set".
- **Mechanism where statistics stop** (p. 26): for birds, books, cities,
  religions, wars, citations, papers, proteins and terrorism, "we must
  consider whether there is a mechanistic or other nonstatistical argument
  favoring one distribution or another". And (§7, p. 30) "it may matter
  greatly whether the observed quantity follows a power law or some other
  form"; "we also need methods to validate the models that have been
  proposed to explain those power laws".
- **US cities** (data set (m), "The human populations of US cities in the
  2000 US Census", p. 23). Table 6.1 (p. 27): n = 19,447, x̂_min =
  52.46 ± 11.88 thousand, α̂ = 2.37(8), n_tail = 580 ± 177, p = 0.76.
  Table 6.2 (p. 28): normalized log-likelihood ratio against the
  lognormal −0.090 (p = 0.93), the exponential 3.65 (p = 0.00), the
  stretched exponential 0.204 (p = 0.84), the power law with cutoff
  −0.123 (p = 0.62); support "moderate", meaning a good fit with other
  plausible alternatives. The tail is 580 of 19,447 cities, 3.0%.

## Assumptions

- Independent, identically distributed data; an exact power law above
  x_min, with no upper cutoff in the pure model (§3.1).
- Below x_min the data are discarded, and the alternatives are fitted to
  the same tail, so every comparison is about the tail.
- p ≤ 0.1 rejects, a conventional and "conservative" choice; KS is the
  distance chosen.
- Sampling biases in the data sets were not corrected (p. 23).

## Concepts

Maximum-likelihood exponent (continuous, and discrete by the Hurwitz zeta);
x_min and n_tail; Kolmogorov–Smirnov distance; semiparametric bootstrap
p-value; Vuong's normalized log-likelihood ratio for non-nested models
and the nested ratio for the cutoff; the ratings none, moderate, good,
with cut-off.

## Bearing on the record

- **[CLAIM-803](../claims.d/CLAIM-803.md)** (supports "fit first"; supports the first clause in part;
  leaves the dynamical tests open). Box 1 and §5 are the fitting clause.
  The first clause it reaches only indirectly: if a lognormal and a power
  law are "extremely difficult to tell ... apart", the tail cannot pick a
  mechanism, and the authors defer to "a mechanistic or other
  nonstatistical argument". None of the three dynamical tests is here.
  Where forms do separate (the cutoff for fires, quakes, web hits) shape
  narrows the field, as the claim's "What it does not say" allows.
  [ARG-tmps95tv](../arguments.d/ARG-tmps95tv.md).
- **[ARG-141](../arguments.d/ARG-141.md)** (qualifies it). Its sentence that the claim's positive half
  rests on this paper and on A is right for "fit first" and wrong for
  "read the dynamics", which rests on A alone (corrected there).
- **[QUESTION-506](../questions.d/QUESTION-506.md)** (leaves it open; a datum). The record's first fitted
  city tail: plausible power law above about 52,000, and the lognormal not
  distinguishable (p = 0.93). See its note of this date.
- **[CLAIM-824](../claims.d/CLAIM-824.md)** and **[CLAIM-830](../claims.d/CLAIM-830.md)** (qualify their empirical reach). At
  realistic n a lognormal and a power-law tail are "very closely equal",
  so a floor, or attachment with entry, has to be read from the dynamics,
  not from the fitted cross-section.
- **[CLAIM-806](../claims.d/CLAIM-806.md)** (qualifies its empirical use). The stretched exponential is
  plausible beside the power law for nine data sets; the sublinear-against-
  linear distinction is one finite cross-sections often cannot make.
- **[CLAIM-841](../claims.d/CLAIM-841.md)** (a parallel). The cutoff form is favoured for fires,
  quakes and flares, the classic self-organized-criticality cases, and the
  pure power law is rejected for earthquakes.
- **[CLAIM-821](../claims.d/CLAIM-821.md)** (a parallel). The bootstrap scores the data against a null
  fitted to the same data by "the same calculation".
- **[LEAD-209](../leads.d/LEAD-209.md)** and **[LEAD-211](../leads.d/LEAD-211.md)** (method). The nested likelihood ratio of a
  power law against one with an exponential cutoff (§5.2) detects a cutoff
  in one sample; nothing here on how a cutoff scales with system size.
- **[NOTE-317](NOTE-317.md)** (method source). Its fit of the spectral tail is this
  paper's method; the paper's warnings apply to it.
- **[SYNTHESIS-119](../syntheses.d/SYNTHESIS-119.md)**: the fitting step it relies on through [CLAIM-803](../claims.d/CLAIM-803.md).
- **[LIT-2963](../literature.d/LIT-2963.md)**: the successor that applies the method to networks.

## Limitations

- The tail only: nothing about the body below x_min, which for cities
  discards 97% of the data.
- Independent data assumed; time series and sampled networks are not
  treated.
- The likelihood-ratio test is inconclusive in most real cases, as the
  authors report.
- A fixed set of alternatives: no mixtures and no double Pareto-lognormal.
- Kolmogorov–Smirnov is insensitive in the extreme tail; the paper does not
  stress it.
