# Reader notes: clauset2009 (LIT-2987)

Clauset, Shalizi & Newman (2009), "Power-law distributions in empirical data", arXiv:0706.1062 (published SIAM Review 51(4), 661-703).

## Provenance

- **Read:** https://arxiv.org/pdf/0706.1062, arXiv preprint v2 (stamp "arXiv:0706.1062v2 [physics.data-an] 2 Feb 2009"), PDF, 43 pp. Fetched 2026-11-22, HTTP 200, 2,285,458 bytes; converted with pdftotext (layout and plain). Kind: arXiv, the authors' own upload (lawful, step 5).
- **What was read:** abstract; §1 Introduction; §2 Definitions and Box 1; §3.1, §3.3 (x_min by KS), §3.5; §4 and §4.1-4.2 (goodness of fit); §5, §5.1-5.3 (likelihood ratio); §6 in full, Tables 6.1-6.3; §7 Conclusions; opening of Appendix A.
- **Skimmed or skipped:** §3.2 and §3.4 (simulation performance of the estimators; figures and Table 3.1 only glanced at); Appendix A.1 onwards beyond its opening; Appendices B (MLE derivations), C (likelihood-ratio details; only its heading and the Vuong citation checked), D (random-number generation); references. Figures were not rendered (text only).
- Page numbers below are the arXiv v2 PDF's printed page numbers, not SIAM Review's.
- No email address was sent anywhere. No other copy was sought, as arXiv sufficed.

## Copies located

| Address | Kind | Outcome (2026-11-22) |
|---|---|---|
| https://arxiv.org/pdf/0706.1062 | arXiv preprint v2, authors' upload | Fetched and read |

## Summary

The paper puts together a full procedure for deciding whether data follow a power law, and it says how to fit one when they do. Box 1 (p. 3) gives the recipe in three steps. First, estimate the exponent α by maximum likelihood, choosing the lower bound x_min so that the Kolmogorov-Smirnov distance between the data above it and the fitted model is as small as possible. Second, test the fit with a Monte Carlo (semiparametric bootstrap) p-value, and reject the power law when p ≤ 0.1. Third, compare the power law with alternatives (lognormal, exponential, stretched exponential, power law with exponential cutoff, and Poisson for discrete data) by Vuong's normalized log-likelihood ratio, which comes with its own p-value. The authors show that least-squares fits on log-log histograms give biased exponents and no test of fit at all (§3, Appendix A). They then apply the procedure to 24 data sets that had been claimed to be power laws (§6).

## Contribution

The paper is a synthesis and a standard rather than a new estimator. "Many of the methods we describe have been discussed previously; our goal here is to bring them together to create a complete procedure" (§1, p. 2). The new parts are three: choosing x_min by minimum KS distance (§3.3), the bootstrap test whose synthetic sets are refitted each time (§4.1), and the 24 data sets reanalysed in one consistent way (§6).

## Key results

1. **A straight log-log line is not enough.** "being roughly straight on a log-log plot is a necessary but not sufficient condition for power-law behavior" (§4, p. 15). The conclusions repeat it: such behaviour "is a necessary but by no means sufficient condition for true power-law behavior" (§7, p. 26).
2. **Regression fits fail.** Least-squares methods "generate significant systematic errors under relatively common conditions ... the results they give cannot not be trusted" [sic] (§3, p. 5). Also, "high values of r2 cannot be taken as evidence in favor of the power-law form" (App. A, p. 31).
3. **x_min by KS.** "we choose the value of x̂min that makes the probability distributions of the measured data and the best-fit power-law model as similar as possible above x̂min" ... "Our estimate x̂min is then the value of xmin that minimizes D" (§3.3, p. 11). An x_min set too low biases α badly; one set too high only costs data (p. 9-10, Fig. 3.3).
4. **A fit is always possible.** "Regardless of the true distribution from which our data were drawn, we can always fit a power law. We need some way to tell whether the fit is a good match" (§4, p. 14).
5. **A high p does not confirm the power law.** "a large p-value does not necessarily mean the power law is the correct distribution for the data" (§4.1, p. 17), because other distributions may fit as well, and with small n a power law is hard to rule out at all.
6. **Statistics cannot settle the alternatives.** "Statistical tests can be used to rule out specific hypotheses, but it is up to the researcher to decide what a reasonable hypothesis is in the first place" (§5, p. 19).
7. **The likelihood-ratio test can say "undecided".** It is valuable because "it can tell us not only which of two hypotheses is favored, but also when the data are insufficient to favor either of them" (§5.1, p. 19). With the p-value taken into account, misclassification between power law and lognormal falls "to a few parts per thousand" (§5.3, p. 22).
8. **Extrapolation is where the forms part.** Indistinguishable fits can diverge in the tail: "conclusions based on different fitted forms can differ enormously even if the forms are indistinguishable in the domain covered by the actual data" (fn. 10, p. 20).
9. **What the 24 data sets showed.** "17 of the 24 data sets are consistent with a power-law distribution", and seven are "firmly ruled out": HTTP, earthquakes, web links, fires, wealth, web hits, metabolic (§6, p. 23). Only word frequencies is "truly convincing" (p. 26). The power law with cutoff is "clearly favored" for about a dozen sets (p. 26).
10. **Lognormal and power law look alike.** "The log-normal ... is not ruled out for any of our data sets except the HTTP connections. In general, we find that it is extremely difficult to tell the difference between log-normal and power-law behavior. Indeed over realistic ranges of x the two distributions are very closely equal, so it appears unlikely that any test would be able to tell them apart unless we have an extremely large data set" (§6, p. 26).
11. **Where statistics stop, mechanism comes in.** For birds, books, cities, religions, wars, citations, papers, proteins and terrorism, which are plausible power laws and also plausible lognormals and stretched exponentials, "we must consider whether there is a mechanistic or other nonstatistical argument favoring one distribution or another" (§6, p. 26).
12. **Cities, specifically.** Data set (m) is "The human populations of US cities in the 2000 US Census" (p. 23). Table 6.1 (p. 27): n = 19,447, x̂_min = 52.46 ± 11.88 (thousands), α̂ = 2.37(8), n_tail = 580 ± 177, p = 0.76. Table 6.2 (p. 28): LR against the lognormal −0.090 (p = 0.93), against the exponential 3.65 (p = 0.00), against the stretched exponential 0.204 (p = 0.84), against the cutoff −0.123 (p = 0.62). The verdict is "moderate", meaning the power law fits and the lognormal and stretched exponential are equally plausible.
13. **On mechanism.** "If ... the goal is, say, to infer plausible mechanisms ... then it may matter greatly whether the observed quantity follows a power law or some other form". The authors also echo Ijiri and Simon and Mitzenmacher that "the characterization of empirical distributions is only a part of the challenge ... we also need methods to validate the models that have been proposed to explain those power laws" (§7, p. 30).

## Assumptions

- The data are i.i.d. draws, and the power law holds exactly above x_min (§3.1, p. 5).
- Below x_min the data are discarded and not modelled. The bootstrap resamples the body nonparametrically and the tail parametrically (§4.1, p. 17).
- The alternatives are fitted only to the same tail x ≥ x_min, so the comparisons are about the tail and say nothing about the body.
- p ≤ 0.1 is a conventional threshold, "conservative" by the authors' choice (p. 17). KS is the chosen distance, but "another goodness-of-fit measure could be used" (p. 15).
- Sampling biases in the data sets were not corrected (p. 23).
- α > 1, and there is no upper cutoff in the pure model (p. 5).

## Concepts

Hill estimator / MLE for α, which is continuous (eq. 3.1) or discrete via the Hurwitz zeta (eq. 3.5); x_min; tail size n_tail; KS distance; semiparametric bootstrap p-value; Vuong's normalized log-likelihood ratio n^(-1/2) R/σ for non-nested models, and the nested-model LR for the power law against the power law with cutoff (§5.2); BIC / marginal likelihood for x_min (Handcock and Jones, §3.3); Hill plot; slowly varying functions L(x) (§3.5); the "moderate / good / none / with cut-off" support ratings.

## Verdict on how the record characterizes the work

- **LIT-2987 summary** ("A maximum-likelihood and goodness-of-fit method ... comparing them with alternatives; many claimed power laws do not survive it") is accurate. But "many do not survive" undersells the sharper finding. Seven of 24 were rejected outright, 17 survive as plausible, only one is convincing, and the lognormal is rejected for just one. The paper's main empirical lesson is indistinguishability more than refutation.
- **CLAIM-803**: the paper is cited correctly for "a straight line on a log-log plot is not sufficient evidence" (p. 15, p. 26) and for fitting by maximum likelihood and comparing with the lognormal and other alternatives (Box 1, §5). The claim's "fit first" ordering matches Box 1. The paper does **not** state CLAIM-803's thesis that a power law does not identify its mechanism, nor any of its three dynamical tests (gain proportional to size, floors and resets, a cutoff that moves with system size). It comes nearest at p. 26: when tests are inconclusive one must look for "a mechanistic or other nonstatistical argument". At p. 30 it holds that distributional form "may matter greatly" for inferring mechanisms. That matches CLAIM-803's "What it does not say" (that shape is not uninformative).
- **ARG-141** says the claim's positive half "rest[s] on Clauset, Shalizi and Newman ... and on A". This is right for "fit first" and wrong for "read the dynamics". The dynamical tests rest on A alone. The reader should correct that sentence when the reading is filed.

## Bearing on the named codes

- **CLAIM-803: supports the "fit first" half, and supports the first clause in part.** The fitting half is in Box 1 (p. 3) and §5 (pp. 18-19). On the first clause the support is indirect: a lognormal and a power law are "extremely difficult to tell ... apart" (p. 26), so the distribution cannot discriminate even between distributional families, let alone mechanisms, and the authors themselves defer to "mechanistic or other nonstatistical argument" (p. 26). The claim's dynamical tests are **left open**: none appear. **It qualifies** the claim mildly. Where the forms can be told apart, as with the cutoff "clearly favored" for fires, quakes and web hits (p. 26), the shape narrows the field, as the claim's "What it does not say" concedes. The paper stresses this too (p. 30). As a source the work belongs in CLAIM-803's `grounds` for the fitting clause.
- **ARG-141: qualifies.** ARG-141 is about Mitzenmacher, and the two readings are complementary. Mitzenmacher supplies the negative clause, Clauset et al. the fitting method that ARG-141 notes Mitzenmacher lacks (Mitzenmacher's "simple empirical test" is exactly what Clauset et al. reject at p. 15). Clauset et al. do not supply the dynamical tests, so ARG-141's sentence attributing them partly to LIT-2987 should be narrowed (see the verdict above). A parallel source argument for LIT-2987 → CLAIM-803 (fitting clause) would be the natural filing.
- **QUESTION-506 (city-size tail): leaves open; it supports the question's framing and gives a datum.** This is the record's first fitted city tail. US cities in 2000 have a plausible power-law tail above about 52,000 (α̂ = 2.37 ± 0.08, p = 0.76, 580 cities). The lognormal is not distinguishable (LR −0.090, p = 0.93), nor is the stretched exponential (p = 0.84) (Tables 6.1-6.2, pp. 27-28). So the question's "Yes" branch requirement that the tail first be "fitted against a lognormal" is already unmet for this data set: the fit cannot separate a Gibrat lognormal (CLAIM-824 without a floor) from a power law (with a floor or with attachment and entry). That is the question's own point that a cross-section cannot decide it. The data are a single US census cross-section with no time dimension or shock, and they do not bear on Japan or on the return to prior paths.

## Recheck (search of record/ after reading)

Entries the first search (LIT-2987, CLAIM-803, ARG-141, QUESTION-506 and grep for likelihood ratio, lognormal and x_min) did not surface as bearing:

- **NOTE-317** (HTSR, grokking): it applies this paper's method. "The PL tail ρ(λ) ~ λ^(−α) is fitted by Clauset–Shalizi–Newman MLE, with λ_min chosen to minimise the KS distance." **Background / method source.** NOTE-317 could cite LIT-2987. The paper's warnings bear on that use. A high KS p does not confirm a power law (p. 17), and lognormal tails are rarely excluded (p. 26). An ESD α is fitted on an n_tail that is often small (§4.2: small n cannot reject).
- **CLAIM-806** (linear attachment at a boundary between the stretched-exponential tails of sublinear attachment and condensation): **qualifies its empirical use.** The stretched exponential is "plausible" alongside the power law for nine data sets, and "the indistinguishability of power laws and stretched exponentials" is noted (p. 26). The sublinear/linear distinction CLAIM-806 draws is a model distinction that finite cross-sections often cannot make.
- **CLAIM-824** (Gibrat gives a lognormal; a floor gives a power law): **qualifies its empirical reach, and supports CLAIM-803's demand for dynamics.** At realistic n the two cross-sections are "very closely equal" (p. 26), so a floor must be read from the dynamics, not from the fitted tail.
- **CLAIM-830** (attachment versus Gibrat is told apart by entry): the same bearing as CLAIM-824. **Background.**
- **LEAD-211 and LEAD-209** (track the cutoff and how it scales): **background / method.** The nested LR test of a power law against a power law with exponential cutoff (§5.2, Tables 6.2-6.3) is a ready tool for detecting a cutoff in one sample. The paper has nothing on how a cutoff scales with system size.
- **CLAIM-841** (a power law does not indicate criticality): **parallel.** The paper favours the cutoff form for fires, quakes and flares, the classic SOC examples (p. 26), and it rejects the pure power law for earthquakes (p. 23). CLAIM-841 already cites Broido and Clauset (LIT-2963), a later application of this method to networks.
- **SYNTHESIS-119** (the line's account): the fitting step it relies on through CLAIM-803 is this paper's. It should cite the reading once filed.
- **CLAIM-821** (a measure read without its null cannot certify) cites CLAIM-803. It is a **parallel**: the bootstrap p-value is scoring against a null fitted to the same data (§4.1, p. 17, "the same calculation that we performed for the real data set").
- **LIT-2963** (Broido & Clauset, "Scale-free networks are rare", Deferred): this is the natural successor and the paper that applies this method. Not read here.
- Not relevant: **LIT-2809 / NOTE-2095 / THEORY-2054** (Larremore, Clauset & Jacobs, block models), which share an author only. The other HTSR notes (NOTE-633, NOTE-679, NOTE-1475 and others) do not name the fitting method.

## Limitations

- The paper is about the tail only. It says nothing about the body below x_min, and x_min selection can cut away most data (cities: 580 of 19,447).
- It assumes i.i.d. data. Dependent data (time series, networks with sampling bias) are not treated, and the biases were "not corrected" (p. 23).
- The LR test is inconclusive in most real cases, which the authors themselves report (p. 26).
- KS is insensitive in the extreme tail, a point the paper does not stress and which is not quoted here.
- The set of alternatives is fixed. A mixture or a double Pareto-lognormal is not tested.
- The page numbers are the arXiv v2 numbers. I did not compare with the SIAM Review version.
- I read the text, not the figures.

## Candidate THEORY

**Sentence:** Clauset, Shalizi and Newman show that a straight line on a log-log plot is necessary but not sufficient for a power law. They replace least-squares fits with a maximum-likelihood estimate of the exponent above a lower bound chosen to minimise the Kolmogorov-Smirnov distance, a bootstrap goodness-of-fit test, and Vuong likelihood-ratio tests against alternatives. Applied to 24 data sets conjectured to be power laws, the procedure rejects 7, finds only word frequencies convincing, and fails to rule out the lognormal for any set but one (US city sizes among them). So power-law and lognormal tails are seldom distinguishable at realistic sample sizes, and the choice must then rest on mechanism.

**promote_when:** A second reading, or a check against the published SIAM Review version, confirms four things: the three-step procedure as stated (MLE with the KS-chosen x_min, the bootstrap p-value with rejection at p ≤ 0.1, and Vuong's test); the tallies of Tables 6.1-6.3 (7 of 24 rejected, only word frequencies rated "good", the lognormal rejected only for HTTP sizes); the US-cities row (p = 0.76, lognormal LR −0.090 with p = 0.93); and the p. 26 sentence deferring inconclusive cases to "a mechanistic or other nonstatistical argument".

## Neighbours

None needed. The work itself was read. No other work was read or quoted.
