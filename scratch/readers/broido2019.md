# Reader notes: broido2019 (LIT-2963)

Broido, A. D. and Clauset, A. (2019), "Scale-free networks are rare",
Nature Communications 10, 1017; doi:10.1038/s41467-019-08746-5;
arXiv:1801.03400 (v1, 9 Jan 2018, the only arXiv version). Read 2026-11-22.

## Provenance and copies located

| Address | Kind (step 5) | Outcome |
|---|---|---|
| https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6399239/fullTextXML | Europe PMC's documented REST interface (ADR-101), open-access published version | **Read** 2026-11-22 (HTTP 200, JATS XML). The route was the interface. Licence in the XML: "Open Access This article is licensed under a Creative Commons Attribution 4.0 International License". |
| https://arxiv.org/pdf/1801.03400 | arXiv preprint (v1) | Fetched 2026-11-22 (HTTP 200, PDF). Only the abstract and first page read, to note how v1 differs. |
| https://www.nature.com/articles/s41467-019-08746-5 | publisher, open access | Not fetched (the same text was read through Europe PMC). |

PMCID found through the Europe PMC search API (query DOI:10.1038/s41467-019-08746-5); no email address sent anywhere.

**What was read**: the published version's abstract, Introduction, Results
(all subsections), Discussion, Methods, figure captions, the category
definitions and Table 1. **Skipped**: the Supplementary Information
(Supplementary Notes 1 to 6: graph simplification, estimation details,
the robustness tests and the synthetic-network tests are only summarized in
the main text), the references list, and the figures as images.

**Versions differ.** The arXiv v1 abstract says "only 4% exhibiting the
strongest-possible evidence of scale-free structure and 52% exhibiting the
weakest-possible evidence". The published version has a Super-Weak category
v1's abstract does not name, and gives Weakest as 29%. Quote the published
numbers; the arXiv id in the LIT points at the older text. The LIT could
add `doi: 10.1038/s41467-019-08746-5` (doi is not preferred over arxiv per
CLAUDE.md, so only as a note).

No supplement or neighbour was read or quoted.

## Summary

The paper tests how common scale-free degree distributions are, using 928
network data sets from the Index of Complex Networks (ICON). Each data set
is simplified into one or more simple graphs (18,448 in all). Graphs with
mean degree outside 2 < ⟨k⟩ < n are dropped, which leaves 3662. For each
degree sequence it fits a discrete power law above a k_min chosen by KS
minimization, with α by maximum likelihood; it tests plausibility by a
goodness-of-fit p-value (p ≥ 0.1 counts as plausible); and it compares the
fit with exponential, log-normal, Weibull and power-law-with-cutoff fits on
the same tail, using Vuong's normalized likelihood-ratio test. The results
are aggregated per data set into nested evidence categories (Super-Weak,
Weakest, Weak, Strong, Strongest, Not Scale Free). Strongly scale-free
networks are rare (4% Strongest), and a log-normal fits at least as well
as a power law in 88%. Domains differ: social networks are at best weakly
scale free, while a few technological networks (half the CAIDA AS graphs)
and biological networks (mainly metabolic) are strongly so.

## Contribution

1. A taxonomy that makes "scale-free network" testable at graded strengths
   (Results, "Definitions of a scale-free network"; Fig. 2).
2. A severe test of that taxonomy, run uniformly over a large corpus from
   many domains, with robustness checks and synthetic controls.
3. An interpretive conclusion: mechanisms that necessarily produce power
   laws have a limited role, and the degree distribution is a weak
   discriminator between mechanisms.

## Key results (section; verbatim)

- **Categories** (Results, Definitions): "Weakest: For at least 50% of
  graphs, a power-law distribution cannot be rejected (p ≥ 0.1)." "Strong:
  Requirements of Weak and Super-Weak, and 2<α^<3 for at least 50% of
  graphs." "Strongest: Requirements of Strong for at least 90% of graphs,
  and requirements of Super-Weak for at least 95% of graphs." "Super-Weak:
  For at least 50% of graphs, no alternative distribution is favored over
  the power law."
- **Headline proportions** (Results, Assessing): "fully 49% of networks fall
  into the Not Scale Free category"; Weakest and Weak "account for only 29
  and 19% of networks"; "only 10 and 4% of network data sets can be
  classified as belonging to the Strong or Strongest categories".
- **Log-normal** (Results, Alternative distributions): "the log-normal is
  favored more than three times as often (48%) over the power law, as vice
  versa (12%) ... the log-normal is at least as good a fit as the power law
  for the vast majority of degree distributions (88%), suggesting that many
  previously identified scale-free networks may in fact be log-normal
  networks." Table 1: exponential favoured 41% against power law 33%;
  Weibull 47% against 33%; cutoff 56% (it nests the power law, so the power
  law can never win).
- **Exponents** (Results, Scaling parameters): α̂ "is concentrated around a
  value of α^=2, but with a long right-tail such that 32% of data sets
  exhibit α^≥3"; 39% in (2, 3); 34% below 2, mostly fungal and slime-mould
  spatial networks.
- **Domains** (Results, Assessing): social: "not a single network falls
  into the Strong or Strongest categories. Hence social networks are at
  best only weakly scale free"; technological: "28% Strong", including
  "the other half of the CAIDA graphs", but "1% Strongest"; biological:
  "6% Strongest ... primarily metabolic networks"; transportation: "all
  three airport networks and 46 of 49 road networks fall into the Not Scale
  Free category".
- **Robustness** (Results, Robustness): under the "most permissive"
  scheme, Strong and Strongest merge at 18%; synthetic directed
  preferential-attachment networks "should and do fall into the Strongest
  category". Moment ratios: "little evidence of a general pattern of
  diverging moment ratios" ⟨k²⟩/⟨k⟩² (Fig. 7). Removing the fungal 28%
  raises Strongest only from 4% to 5%.
- **Mechanism** (Introduction): "Because the shape of a degree distribution
  imposes only modest constraints on overall network structure, it
  represents relatively weak evidence when trying to distinguish generating
  mechanisms, even when the distribution's functional form is clear." And
  "some variations of preferential attachment do not produce power-law
  degree distributions".
- **Mechanism** (Discussion): "the finding that scale-free networks are
  empirically uncommon does imply a generally limited role for any
  mechanism that necessarily produces power-law degree distributions";
  "For some networks, there is strong evidence that mechanisms like
  preferential attachment apply, e.g., scientific citation networks";
  "A claim that some network is scale free should thus be established
  using a severe statistical test that goes beyond static degree
  distributions."
- **Use in theory** (Discussion): "for some types of calculations, e.g.,
  the location of the epidemic threshold, scale-free networks can be useful
  models, even when real-world degree distributions are simply heavy
  tailed, rather than scale free".

## Assumptions

- Scale-free means a pure discrete power law, Pr(k) = C k^(−α) for
  k ≥ k_min (Methods, eq. 1), and the body below k_min is discarded. The
  paper defines scale invariance as f(ck) = g(c)f(k), whose only
  normalizable solution is a power law (Introduction). No slowly varying
  correction is allowed.
- p ≥ 0.1 counts as plausible; the LRT threshold is p < 0.1; there is no
  multiple-test correction (Methods).
- Each simple graph derived from a data set is weighted equally (a uniform
  prior), so a directed network whose in-degrees are power-law but whose
  out-degrees are not can fail the Strongest threshold. The permissive
  scheme is the check on this.
- The sparsity filter (⟨k⟩ > 2) drops about 80% of the derived graphs, most
  of them from three data sets (Methods).
- The corpus is ICON's holdings. Fungal networks are 28% of it, and
  transportation and information networks are too few to analyse alone.

## Concepts

The severe test (cited to Mayo); the evidence categories; k_min selection
by KS minimization; the discrete power-law MLE; the goodness-of-fit
p-value; Vuong's normalized likelihood ratio; the moment ratio
⟨k²⟩/⟨k⟩² and its divergence for 2 < α < 3; graph simplification of
directed, weighted, multiplex, temporal and bipartite data; the
log-normal as a heavy-tailed but not scale-free alternative.

## Verdict on how the exchange characterized it

- LIT-2963's status note and Standing ("strongly scale-free real networks
  are uncommon"): **accurate**; it matches the abstract ("strongly
  scale-free structure is empirically rare").
- LIT-2963's summary ("preferential attachment's pure power law is seldom
  what real networks show"): **fair**. The paper speaks of power-law degree
  distributions in general, not of preferential attachment's in
  particular. It keeps preferential attachment for citation networks and
  limits "any mechanism that necessarily produces power-law degree
  distributions".
- CLAIM-841, "Many reported scale-free networks are not (A10 §6)" from
  "rigorous studies": **slightly overstated**. The paper shows a lack of
  evidence and says many "may in fact be log-normal networks". It does not
  show that they are not scale free: 46% are Super-Weak, and in 40% the
  log-normal test is inconclusive. "Many networks reported as scale free
  show little statistical evidence of it" is the paper's claim. The
  attribution to Broido and Clauset is right.
- CLAIM-803, "Broido and Clauset ... carry the same caution over to
  networks": **accurate**, and the paper says so directly (the Introduction
  and Discussion quotes above).

## Bearing on the named codes

- **CLAIM-803: supports**, on both halves the paper touches. (a) The
  description is not the mechanism: "relatively weak evidence when trying
  to distinguish generating mechanisms, even when the distribution's
  functional form is clear" (Introduction), and "a weak discriminator
  between mechanisms" (Discussion). (b) Fit against alternatives such as
  the log-normal first: the method is exactly this (Methods; Table 1), and
  the log-normal does at least as well in 88%. It also **qualifies** in the
  direction CLAIM-803's "What it does not say" already allows: the absence
  of a power law does constrain mechanisms ("a generally limited role for
  any mechanism that necessarily produces power-law degree
  distributions"), so the shape is informative negatively. It **leaves
  open** CLAIM-803's three dynamical tests: the paper asks for a test
  "that goes beyond static degree distributions" but names none. It adds a
  converse the claim lacks: "some variations of preferential attachment do
  not produce power-law degree distributions" (Introduction), so the
  mechanism does not fix the law either (compare CLAIM-817 and CLAIM-806).
  Candidate `grounds` once a THEORY is filed.
- **CLAIM-841: background or contrast.** The paper never mentions
  criticality, symmetry or the claim's routes, so it does not bear on the
  thesis. It bears only on the folded-in bullet "Many reported scale-free
  networks are not", which it **qualifies** as above. In contrast with the
  claim's direction, it doubts that the power law is there at all, before
  any question of what it indicates. It should not enter CLAIM-841's
  `grounds` for the thesis. It could be cited for that bullet, reworded.

## Limitations

- Main text only. The robustness and synthetic-network details are in the
  Supplementary Notes, which were not read, so the claims about those tests
  are the paper's summaries.
- The tested model is a pure power law above k_min. A tail that is
  regularly varying, P(X > x) = x^(−α)L(x) (TERM-142 sense 1), but not
  exactly power-law could be classed as not scale free. The paper does not
  test a regularly varying definition, and whether one would change the
  proportions is not addressed in the main text.
- The categories depend on thresholds (50%, 90%, 95%, ntail ≥ 50, p ≥ 0.1)
  that the paper justifies by error rates; the permissive variant moves
  Strong plus Strongest from 10% and 4% to 18% together.
- The paper says itself that it "considers only the degree distributions
  of networks, and hence says relatively little about ... the underlying
  processes" (Discussion).
- No reply to the paper or re-analysis of it was sought or read.

## Candidate THEORY

**Sentence.** Fitting a discrete power law to the upper tail of each degree
sequence from 928 network data sets (the Index of Complex Networks), testing
its plausibility, and comparing it with exponential, log-normal, Weibull and
cutoff alternatives by likelihood ratio, Broido and Clauset find a power law
plausible for 29% of data sets, and plausible, with 2 < α < 3 and not beaten
by an alternative, in nearly all of a data set's graphs for 4%. A
log-normal fits at least as well as the power law for 88% of degree
distributions. Social networks are at best weakly scale free, while some
technological and biological networks are strongly so. From this they
conclude that a mechanism which necessarily yields power-law degrees has a
limited role, and that a degree distribution weakly discriminates between
mechanisms.

**promote_when.** A rerun of the paper's published pipeline and data
(github.com/adbroido/SFAnalysis on the ICON corpus), or an independent
reimplementation of the same fitting, goodness-of-fit and likelihood-ratio
procedure and category thresholds, reproduces the category proportions
(29% Weakest, 4% Strongest, 88% log-normal at least as good) within a few
percentage points.

## Recheck (search after reading)

Searched record/ for scale-free, preferential attachment, degree
distribution, log-normal/lognormal, Weibull, stretched exponential, Vuong,
k_min/xmin, regularly varying, Index of Complex Networks, Barabási, CAIDA
and Internet. Entries the first search did not name:

- **SYNTHESIS-119** (a power law does not identify its mechanism): **supports**
  its organizing thesis for network degrees; it does not cite LIT-2963
  now. A candidate for its network or cumulative-advantage line.
- **CLAIM-817** (cumulative advantage gives a power law only with linear
  attachment and entry): **parallel**. Its "Not that any real system's heavy
  tail comes from cumulative advantage" is consistent with the paper's
  "limited role". The paper's "some variations of preferential attachment
  do not produce power-law degree distributions" is the empirical side of
  the claim's sublinear and superlinear cases.
- **CLAIM-806** (linear attachment balanced between stretched-exponential
  and condensation): **background**. The Weibull or stretched exponential is
  favoured over the power law in 47% of the paper's degree sequences, though
  the paper does not tie this to sublinear attachment.
- **CLAIM-824 and CLAIM-830** (Gibrat's lognormal, and what entry adds):
  **parallel**. The paper finds log-normal-like degree tails common and
  calls for "mechanisms that produce non-scale-free structural patterns,
  e.g., those with degree distributions better fitted by a log-normal". It
  does not name Gibrat or multiplicative growth.
- **QUESTION-505** (what fixes the exponent): **background data**. Empirical
  α̂ is concentrated near 2, with 32% ≥ 3 and 34% < 2, against the
  Barabási–Albert prediction of 3.
- **TERM-142** (scale-free, sense 1, heavy-tailed marginal, regularly
  varying): **contrast**. The paper's operational definition is narrower,
  an exact power law above k_min. The term should note that "scale-free
  network" in this paper means the narrower sense.
- **LIT-3004** (Barabási and Albert 1999) and **LIT-2968** (Network
  Science ch. 5): **qualifies** their empirical premise that real networks
  are generally scale free. The paper keeps directed preferential attachment
  as a synthetic control that is correctly classed Strongest.
- **LIT-2987** (Clauset, Shalizi and Newman, unread): the paper applies
  "standard statistical methods" from its ref. 49 (CSN, by the method
  described: KS-minimized k_min, discrete MLE, p ≥ 0.1, Vuong LRT). This
  is indirect evidence of what LIT-2987 contains; it does not read it.
- **THEORY-188 and THEORY-803** (hyperbolic network models; the Internet
  fit): **background**. The CAIDA autonomous-system graphs, the Internet case,
  are among the few Strong networks (half Strong, half Weakest), so the
  Internet's power-law degree, which THEORY-188's source fits, is one of
  the better-supported cases.
- **THEORY-2150** (Mitzenmacher, a lognormal looks straight on log-log
  axes): **parallel**. Broido and Clauset give the corpus-scale empirical
  side of the same lognormal-against-power-law confusion.

No held entry contradicts the paper. The record holds no reply to it or
re-analysis of it that the search found.

## Neighbours

Not needed: the work itself was read in full text (main paper).
