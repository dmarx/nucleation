# Reader notes: quinn2023 (LIT-2958)

Quinn, Abbott, Transtrum, Machta & Sethna, "Information geometry for
multiparameter models: New perspectives on the origin of simplicity",
arXiv 2111.07176 (v of 2022-09-22), Rep. Prog. Phys. (2023).

## Step 1: copies located (2026-11-22)

- arXiv API metadata, https://export.arxiv.org/api/query?id_list=2111.07176 :
  200. Title on arXiv is "...origin of simplicity" (as LIT-2958 has it);
  the reader message's "origin of simple behavior" is not the title.
- arXiv source, https://arxiv.org/e-print/2111.07176 : 200, gzip tarball of
  the LaTeX source (author's manuscript, arXiv; lawful, step 5 first
  place). Fetched, no obstacle. This is the copy read.
- Not sought further (the arXiv copy suffices): the PMC copy A17 cites.

## Step 2: read (2026-11-22)

**Provenance.** arXiv e-print 2111.07176, LaTeX source of the version
dated 2022-09-22 (author's manuscript; tarball built 2022-09-26), from
https://arxiv.org/e-print/2111.07176. Read in full as LaTeX with comment
lines stripped: abstract, §1, §2 (ModelManifolds.tex, SloppyExamples.tex),
§3 Hyperribbon bounds, §4 Effective theories and MBAM (4.1-4.3), §5 Priors
(5.1-5.2), §6 RG (6.1-6.2), §7 Minkowski embeddings (7.1-7.4), §8 Future
directions and Conclusions. Figures not viewed as images; every caption
read. Reference list consulted only for cited keys. The published Rep.
Prog. Phys. text was not compared. Section numbers are the manuscript's
(its .toc); no page numbers are given, as the source has none.

**Title.** arXiv and LIT-2958 agree: "...New perspectives on the origin of
simplicity". The reader message's "origin of simple behavior" is wrong.

### Summary
A review for physicists of the Sethna-group programme. A model's
predictions form a model manifold, with the Fisher metric as distance; in
many models across the sciences the FIM spectrum spreads evenly in log
over many decades (Fig. 2, 17 models) and the geodesic widths fall roughly
geometrically (Fig. 3): a hyperribbon. §3 restates Quinn, Wilber, Townsend
& Sethna 2019 (PRL 122, 158302; not held): for least-squares models smooth
in their control variable, the manifold lies within ε_N of a
Vandermonde-skewed parallelepiped, or inside a hyperellipsoid whose j-th
axis is bounded by ρ^(−j). §4 puts effective theories on manifold
boundaries (cGh; Hasse diagram of the boundary cell complex), reviews MBAM
and its equivalence to balanced truncation and to singular perturbation.
§5 argues that Jeffreys prior fails on hyperribbons, reviews the
mutual-information-maximizing prior (discrete, weight on edges) and
introduces an "adaptive slab-and-spike" prior (the abstract's "projected
maximum likelihood"), which projects NML weight onto the maximum-likelihood
point. §6 restates Machta et al. 2013 and Raju et al. 2018 on
coarse-graining contracting the irrelevant directions of the metric. §7
reviews InPCA (Bhattacharyya divergence, zero-replica limit) and isKL (a
finite, 2N-dimensional Minkowski embedding of exponential families).

### Contribution
Mainly synthesis. New by the paper's own account: the projected / adaptive
slab-and-spike prior ("not published elsewhere", §1), and the statement
that physical emergence and least-squares sloppiness, both hyperribbons,
have explanations that "seem completely different" (§8.2).

### Key results (section; verbatim)
1. Joint definition (§2): "We call a model sloppy, and the model manifold
   a hyperribbon, if the parameter-space eigenvalues and prediction-space
   widths are hierarchical: roughly equally spaced in log, spanning
   several decades."
2. Sloppy is not low-dimensional (§2): "A sloppy model will have an
   effective low-dimensional description if many of its widths are small
   compared to the precision of the predictions demanded. This need not be
   the case -- the ΛCDM model ... is sloppy ... because the experiments
   are so precise that all parameters are well determined from the data."
3. Spectrum not intrinsic (§2): "If we re-scale some parameters ... the
   FIM and hence the spectrum of eigenvalues will change"; geodesic length
   "is independent of the way we define the coordinate system".
4. Ubiquity is empirical (§1): "it is an empirical fact that, for a great
   many models from various branches of science, this manifold has a
   characteristic shape we term a hyperribbon."
5. Bound (§3.2): "the model manifold Y is constrained by a hyper-ellipsoid
   whose j-th largest principal axis length is bounded by a power law
   ρ^{-j}" [sic: ρ^(−j) is geometric in j, not a power law]. Scope (§3
   title): "for nonlinear least-squares models"; it rests on "the
   smoothness of the predictions as the experimental controls ... are
   varied".
6. Neither separation of scales nor structural non-identifiability (§3):
   "the observed hierarchies are not primarily due to a separation of
   scales"; with all rate constants set to one, "The cost Hessian remains
   sloppy"; sloppiness is "practical identifiability", whereas structural
   non-identifiability "would give eigenvalues of the metric exactly equal
   to zero".
7. Boundaries and singularities (§2 footnote; §4.3): the model manifold
   "is not strictly a manifold ... the important simpler models at the
   boundary introduce fold lines, corners, and other singularites"; "model
   manifolds may have singular models that are not strictly boundaries,
   such as a the tip of a cone. These singularities often correspond to
   useful reduced models."
8. MBAM (§4.1): a geodesic along a sloppy eigenvector to a boundary, then
   the analytic limit, one parameter fewer; "We do not necessarily require
   the true value of the perturbation parameter to be small. Rather, the
   true parameter value may be large provided the data to be explained do
   not constrain its value." Equivalent to balanced truncation for LTI
   systems (§4.2).
9. Priors (§5): for Jeffreys, "Scaling the metric g → M g has no effect at
   all on p_J(θ)"; in a D = 26 sum of exponentials "its posterior is
   centered 20 standard deviations away from the data"; the smallest FIM
   eigenvalue "is about 10^{-50}". The optimal prior: "Along a short
   dimension (say ≲1 standard deviations) the atoms will lie only at the
   boundaries."
10. RG (§6.1): for irrelevant directions d log(ds²)/db = −D + 2y_i; along
   relevant ones "the microscopic metric does not contract". §6.2: the
   hopping model after one step "is not a hyper-ribbon, but is extended
   roughly equally in all directions".
11. Relative to the question (§8.2): "The Ising model is not sloppy, and
   has no beautiful emergent theory, unless one only cares about long
   length and time scales. And a systems biology model is not sloppy if
   one designs experiments to measure one parameter at a time ... Perhaps
   it is caring about the answers to the right questions that makes
   science possible?"
12. Two explanations, not one (§8.2): "Emergence in physics and emergence
   in least-squares models are both characterized by sloppiness ... and
   both form hyperribbons, but our explanations for the two seem
   completely different"; for general probabilistic models "we do not yet
   have an explanation for this in general, except for ... exponential
   families".
13. Neural networks (§8.3, §8.4): work in progress on InPCA views of
   training, and "We have speculated about the relationship between
   sloppiness and large machine learning models." Fig. 3 shows a "Neural
   Network" width spectrum from Quinn et al. 2019 (InPCA paper); §1 cites
   Kaplan et al. 2020 for generalization "even with millions of
   parameters".
14. Overfitting (§1): "new parameters are typically unable to drastically
   improve model fits, and can therefore be added without harming model
   predictions ... A reduced model description may still be preferred as
   being more comprehensible, reliable, or likely, but not because the
   fuller model will overfit."

### Assumptions
Gaussian-noise least squares for §3's rigour; analytic or bounded-
derivative dependence on one control variable (several only in a
supplement); widths from a central point along FIM eigendirections;
reduced models where parameters run to limits; priors shown on sums of
exponentials only.

### Concepts
model manifold; Fisher metric; stiff / sloppy; hyperribbon; geodesic
width; practical vs structural identifiability; boundary cell complex and
Hasse diagram; MBAM; balanced truncation; nested models; mutual-
information (optimal) prior; NML; adaptive slab-and-spike prior; metric
flow under RG; InPCA; isKL; Minkowski (pseudo-Riemannian) embedding;
orthogonality catastrophe; zero-replica limit.

### Verdict on the exchange's characterization
LIT-2958's summary ("model manifolds ... are hyperribbons with a few stiff
and many sloppy directions, which is why simple effective models work") is
fair, with two qualifications the paper makes itself: the ubiquity is "an
empirical fact", proved only for smooth least-squares models (results 4,
5), and a hyperribbon gives a low-dimensional description only where many
widths fall below the precision demanded (result 2). A17's link between
coarse-graining, sloppiness and emergent simplicity is in §6, but the
review says the coarse-graining and least-squares explanations "seem
completely different" (result 12): it offers no single account of why
simple effective theories exist. It does not claim sloppiness for large
networks; it speculates (result 13).

### Bearing on the named codes
- **TERM-135 (hyperribbon): supports, and adds two points.** Supports the
  definition (result 1; "a ribbon is much longer than it is wide, and much
  wider than it is thick", §2), widths from an initial point (§2), and
  condition 1 (results 2, 11; the hopping model, result 10). Adds: (a) for
  least-squares models smooth in the controls there is a rigorous bound
  (result 5), beyond the 2011 argument TERM-135 calls "a ratio-test
  heuristic"; (b) the authors loosen condition 2 themselves: "singular
  models that are not strictly boundaries, such as a the tip of a cone"
  (result 7), the point TERM-135 credits to LIT-2960. On "Not RG
  relevance": the abstract again "connect[s] stiff and sloppy directions
  ... with relevant and irrelevant eigendirections"; −D + 2y_i (result 10)
  matches the record's b^(2y−d) (THEORY-777). Also its Sources line
  ("the 2023 review is Deferred and unread") becomes stale.
- **CLAIM-820: supports, with one qualification.** Consequence 1: §8
  "predictions are independent of all but a few parameter combinations,
  which is unfortunate if you want to deduce the parameters from
  collective behavior, but fortunate if you want to test the predictions
  of the model before the parameters are fully measured". Consequence 3
  and relativity to the observables: result 11, nearly in the claim's
  words. Qualification: result 2, sloppiness alone does not give
  behavioural simplicity; widths must be small against the precision
  demanded (ΛCDM). defeated_if clause 2 is answered by widths (result 3)
  and by the rates-set-to-one test (result 6). "Not, yet, for neural
  networks": left open by the review (result 13), consistent. Result 14
  adds an interpretive point the claim does not make.
- **TERM-140 (sloppy): supports; qualifies one point; leaves one open.**
  Supports "relative to a design" (result 11; §2 on optimal experimental
  design), "relative to a chart" (result 3), "graded" ("several decades",
  no threshold); separates sloppiness from structural non-identifiability
  (zero eigenvalues, result 6) as TERM-140 separates it from singularity.
  Qualifies: the review's "sloppy" needs eigenvalues *and* widths
  hierarchical (result 1), while TERM-140 keeps the local half only, as its
  "A hyperribbon" bullet says; the skew criterion appears only as "The
  most important eigendirections need not align with our parameter
  directions" (§1). Leaves open: "roughly evenly spaced on a log scale"
  (§2) again reads as fixed spacing, against TERM-140's density reading.
  Parallel: separation of scales "certainly will generate a large range of
  eigenvalues, but do[es] not explain why eigenvalues span many decades
  uniformly" (§3), close to TERM-140's separation from ill-conditioning.

### Limitations
A review: §3's theorem is restated, not proved; the multi-control case is
in a supplement of the 2019 paper; the widths and spectra figures come
from earlier papers. The new prior is shown only on sums of exponentials;
the mutual-information comparison (Fig. 11) is an estimate. "Power law
ρ^{-j}" misnames geometric decay. Network content is speculation and work
in progress. Interior singular sets get one sentence (result 7).

### Candidate THEORY
"Quinn, Abbott, Transtrum, Machta and Sethna (2023) call a model sloppy,
and its model manifold a hyperribbon, when its Fisher eigenvalues and
geodesic widths are both hierarchical, roughly evenly spaced in log over
several decades; they present the ubiquity of this shape as empirical,
bound it rigorously only for least-squares models smooth in their control
variables, hold that it gives a low-dimensional description only where
many widths fall below the precision demanded, and say that its
explanations in renormalizable physics and in least-squares fitting seem
completely different."

promote_when: Quinn, Wilber, Townsend and Sethna 2019 (Phys. Rev. Lett.
122, 158302, doi:10.1103/PhysRevLett.122.158302) is read and confirms that
the manifold of a least-squares model meeting the review's smoothness
condition lies within a hyperellipsoid whose j-th axis is bounded by
ρ^(−j).
