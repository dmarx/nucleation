---
status: Read
paper: LIT-2963
title: 'Broido and Clauset, Scale-free networks are rare, read for how often network degree distributions pass a severe power-law test'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Read on 2026-11-22 by a delegated reader from Europe PMC's documented
    REST interface (ebi.ac.uk/europepmc/webservices/rest/PMC6399239/fullTextXML,
    JATS XML), the open-access published version (Nature Communications 10,
    1017, CC BY 4.0 as the XML states); the interface was the route
    (ADR-101). The PMCID came from the Europe PMC search API, queried by
    DOI. Read: the abstract, Introduction, Results (all subsections),
    Discussion, Methods, figure captions, the category definitions and
    Table 1. Skipped: the Supplementary Information (graph simplification,
    estimation details, the robustness and synthetic-network tests, known
    here only from the main text's summaries), the references and the
    figures as images. The arXiv v1 (1801.03400) was fetched for its
    abstract and first page only: it reports 52% in Super-Weak where the
    published text has 46%, and the published numbers are the ones quoted.
    Every quotation rechecked by the filer by script against the XML. No
    reply to the paper was read. No email address sent.
date: '2026-11-22'
summary: >-
  Fitting a discrete power law above a KS-chosen k_min to the degree
  sequences of 928 network data sets and testing it against alternatives,
  Broido and Clauset find 49% Not Scale Free, 29% Weakest and 4%
  Strongest, and a lognormal at least as good as the power law for 88%;
  social networks are at best weakly scale free. They conclude that a
  mechanism which necessarily yields power-law degrees has a limited role
  and that the degree distribution weakly discriminates between
  mechanisms. Their test is of a pure power law; Voitalov and others,
  defining power laws as regularly varying tails, dispute the verdict.
---
<!-- inactive-ok-file: CLAIM-803 CLAIM-841 CLAIM-817 CLAIM-806 CLAIM-824 CLAIM-830 SYNTHESIS-119 THEORY-2150 THEORY-188 THEORY-803 TERM-142 THEORY-tmphcnj3 ARG-tmpmt4gj ARG-tmp38kft — Proposed; the entries this reading bears on, its own reading and the arguments filed with it -->
<!-- inactive-ok-file: LIT-3004 LIT-2968 LIT-2987 LIT-tmpvmrkv — Deferred; works this reading bears on or names, registered and unread -->

# NOTE-tmpleyjh: Broido and Clauset, Scale-free networks are rare, read for how often network degree distributions pass a severe power-law test

## Contribution

A taxonomy that makes "scale-free network" testable at graded strengths,
a severe test of it run uniformly over a large corpus from many domains,
and the conclusion that "the finding that scale-free networks are
empirically uncommon does imply a generally limited role for any
mechanism that necessarily produces power-law degree distributions"
(Discussion). The reading is THEORY-tmphcnj3.

## Key results

- **Corpus.** 928 network data sets from the Index of Complex Networks,
  simplified into 18,448 simple graphs, of which those with mean degree
  outside 2 < ⟨k⟩ < n are dropped, leaving 3662 (Methods).
- **Method.** A discrete power law above a k_min chosen by
  Kolmogorov–Smirnov minimization, α by maximum likelihood, plausibility
  at p ≥ 0.1, and Vuong likelihood ratios against exponential,
  lognormal, Weibull and cutoff fits on the same tail: the procedure of
  LIT-2987, which it cites as standard.
- **Categories** (Results, Definitions). "Weakest: For at least 50% of
  graphs, a power-law distribution cannot be rejected (p ≥ 0.1)." Weak
  adds n_tail ≥ 50; Strong adds 2 < α̂ < 3 and Super-Weak; Strongest
  requires Strong for at least 90% of graphs and Super-Weak for 95%.
  "Super-Weak: For at least 50% of graphs, no alternative distribution is
  favored over the power law."
- **Proportions.** "fully 49% of networks fall into the Not Scale Free
  category"; 46% are Super-Weak; Weakest and Weak "account for only 29 and
  19% of networks"; "only 10 and 4% of network data sets can be
  classified as belonging to the Strong or Strongest categories".
- **The lognormal.** "the log-normal is favored more than three times as
  often (48%) over the power law, as vice versa (12%)", inconclusive in
  40%; "the log-normal is at least as good a fit as the power law for the
  vast majority of degree distributions (88%), suggesting that many
  previously identified scale-free networks may in fact be log-normal
  networks."
- **Exponents.** α̂ is "concentrated around a value of α̂ = 2", with 32% at
  α̂ ≥ 3, 39% in (2, 3) and 34% below 2, mostly fungal networks.
- **Domains.** Social: "not a single network falls into the Strong or
  Strongest categories. Hence social networks are at best only weakly
  scale free". Technological: 28% Strong, including half the CAIDA
  autonomous-system graphs, 1% Strongest. Biological: 6% Strongest,
  mainly metabolic. All three airport networks and 46 of 49 road networks
  are Not Scale Free.
- **Robustness.** Under the "most permissive" scheme Strong and Strongest
  merge at 18%; synthetic preferential-attachment networks "should and do
  fall into the Strongest category"; "little evidence of a general
  pattern of diverging moment ratios"; removing the fungal networks
  raises Strongest from 4% to 5%.
- **Mechanism.** The degree distribution "represents relatively weak
  evidence when trying to distinguish generating mechanisms ... even when
  the distribution's functional form is clear" (Introduction); "some
  variations of preferential attachment do not produce power-law degree
  distributions" (Introduction); "For some networks, there is strong
  evidence that mechanisms like preferential attachment apply, e.g.,
  scientific citation networks" (Discussion); a scale-free claim needs "a
  severe statistical test ... that goes beyond static degree
  distributions" (Discussion).

## Assumptions

- Scale-free means a pure discrete power law, Pr(k) ∝ k^(−α) for
  k ≥ k_min, with the body below discarded. No slowly varying correction
  is allowed.
- p ≥ 0.1 as plausible, p < 0.1 for the likelihood ratios, no correction
  for multiple tests.
- Every simple graph of a data set weighted equally, so a directed network
  with power-law in-degrees and other out-degrees can miss Strongest; the
  permissive scheme checks this.
- The sparsity filter drops about 80% of derived graphs; fungal networks
  are 28% of the corpus.

## Concepts

The severe test (after Mayo); the nested evidence categories; k_min by
Kolmogorov–Smirnov minimization; the discrete power-law likelihood;
goodness-of-fit p-value; Vuong's normalized likelihood ratio; the moment
ratio ⟨k²⟩/⟨k⟩²; graph simplification; the lognormal as heavy-tailed but
not scale free.

## The verdict is disputed

Voitalov, van der Hoorn, van der Hofstad and Krioukov, "Scale-free networks
well done" (LIT-tmpvmrkv, registered, unread), contest it. Their abstract
gives the hinge: they define a power-law distribution as a regularly
varying one, which "allows the distribution to deviate from a pure power
law arbitrarily but without affecting the power-law tail exponent", and
conclude that real-world scale-free networks "are definitely not as rare
as one would conclude based on the popular but unrealistic assumption that
real-world data comes from power laws of pristine purity". Broido and
Clauset test a pure power law above k_min; the reply's definition is
TERM-142's sense 1, P(X > x) = x^(−α)L(x). Which definition is right for a
given use is the question; nothing beyond the reply's abstract is relied
on here.

## Bearing on the record

- **CLAIM-803** (supports, both halves it touches; qualifies in the
  direction the claim allows). The degree distribution is "relatively weak
  evidence when trying to distinguish generating mechanisms"; the method
  fits against the lognormal first. The absence of a power law does
  constrain mechanisms ("a generally limited role"), so shape informs
  negatively. The three dynamical tests are left open: it asks for a test
  "that goes beyond static degree distributions" and names none. It adds
  the converse, that some preferential attachment does not give a power
  law. ARG-tmpmt4gj.
- **CLAIM-841** (does not bear on the thesis; qualifies one folded-in
  bullet). The paper never mentions criticality. It shows a lack of
  evidence for power-law degrees, not that the networks "are not" scale
  free. ARG-tmp38kft.
- **CLAIM-817** (a parallel). "Limited role" and "some variations of
  preferential attachment do not produce power-law degree distributions"
  are the empirical side of the claim's sublinear and superlinear cases.
- **CLAIM-806** (background). The Weibull is favoured over the power law
  in 47% of data sets; the paper does not tie it to sublinear attachment.
- **CLAIM-824**, **CLAIM-830** (parallels). Lognormal-like degree tails
  are common; the paper calls for "mechanisms that produce non-scale-free
  structural patterns" and does not name Gibrat or multiplicative growth.
- **QUESTION-505** (background data). α̂ is concentrated near 2, against
  the Barabási–Albert 3.
- **TERM-142** (a contrast). "Scale-free network" here is the narrow sense,
  an exact power law above k_min, not the regularly varying sense 1.
- **LIT-3004**, **LIT-2968** (qualifies their premise that real networks
  are generally scale free); directed preferential attachment is kept as a
  synthetic control that is correctly classed Strongest.
- **THEORY-188**, **THEORY-803** (background). The CAIDA Internet graphs
  are among the few Strong networks.
- **THEORY-2150** (a parallel). The corpus-scale side of Mitzenmacher's
  lognormal-against-power-law confusion.
- **SYNTHESIS-119** (supports its organizing thesis for network degrees).

## Limitations

- Main text only; the supplementary tests are known from summaries.
- The tested model is a pure power law above k_min; a regularly varying
  tail that is not exactly a power law could be classed Not Scale Free.
  The paper does not test a regularly varying definition, which is the
  ground of the dispute above.
- The categories depend on thresholds (50%, 90%, 95%, n_tail ≥ 50,
  p ≥ 0.1).
- By its own account it "considers only the degree distributions of
  networks, and hence says relatively little about" the underlying
  processes.
