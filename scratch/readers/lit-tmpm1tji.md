# Reader notes: LIT-tmpm1tji

Transtrum, Machta, Brown, Daniels, Myers, Sethna, "Sloppiness and Emergent
Theories in Physics, Biology, and Beyond", arXiv 1501.07668 (v1, 2015-01-30,
the only version). Published as "Perspective: Sloppiness and emergent theories
in physics, biology, and beyond", J. Chem. Phys. 143, 010901 (2015),
doi:10.1063/1.4923066 (Crossref API, 2026-11-21, no mailto sent).

## Step 1: copies located (2026-11-21)

- https://arxiv.org/e-print/1501.07668 : arXiv, author's manuscript (LaTeX
  source, JChemPhysReview.tex, revtex aip/jcp). HTTP 200. READ.
- https://arxiv.org/pdf/1501.07668 : arXiv PDF of the same, 15 pages.
  HTTP 200. Fetched; used only to confirm it exists; text read from source.
- doi:10.1063/1.4923066 (AIP): published version. Not sought, not read.
  Differences between arXiv v1 and the published Perspective are unchecked.

## Provenance

Read in full from the arXiv LaTeX source (all sections I-VI, all figure
captions, commented-out author notes skipped except where noted), plus the
image Eigenvalues.png (Fig. 1). Bibliography (.bbl) not read. Section numbers
below are the source's: I Parameter indeterminacy and sloppiness; II
Mathematical Framework; III Why Sloppiness? Information Geometry; IV Model
Reduction; V Emergence in Physics as sloppiness; VI Ramifications in
Biochemical Modeling; VII More general consequences. No page numbers (source).

## Summary

A Perspective reviewing the Sethna-group sloppy-models programme. Sloppiness
is introduced by the sum-of-exponentials fit and defined by the FIM spectrum;
the FIM is read as a Riemannian metric on the model manifold (data-space
image of parameter space); because eigenvalues are not reparametrization
invariant, the invariant counterpart is the global geometry: bounded model
manifolds whose widths (geodesic arc lengths) and extrinsic curvatures fall
exponentially, the hyperribbon, derived for one independent variable from
interpolation theorems. MBAM reduces a model by following a geodesic along the
thinnest direction to a manifold boundary (EGFR: 48 parameters to 12).
Continuum limits and the RG are read as parameter-space compression (Machta
et al. 2013): hopping model and Ising model become sloppy when observed at
long times/lengths. Then consequences: parameter estimation vs prediction in
systems biology, "wrong" effective models, PCA, Levenberg-Marquardt and
geodesic acceleration, robustness/evolvability, pattern recognition,
autoencoders, and "why the world is comprehensible".

## Contribution

A programmatic synthesis rather than new results: it ties local sloppiness
(FIM spectrum) to global geometry (hyperribbon), names interpolation as the
reason for the hierarchy, and RG/continuum limits as its physical instance,
and argues that emergent simple theories are "hidden inside" sloppy models.

## How it defines sloppiness (for the record's TERM)

1. **Informal, by symptom (§I):** "{\em Sloppy} is the term used to describe a
   class of complex models exhibiting large parameter uncertainty when fit to
   data."
2. **By the FIM spectrum (§I):** "Most of the FIM eigenvalues are very small,
   corresponding to combinations of parameters that have little effect on
   model behavior. These unimportant parameter combinations are designated
   \emph{sloppy}. A small number of eigenvalues are relatively large ...
   (known as \emph{stiff}). It is generally observed that the FIM eigenvalues
   decay roughly log-linearly, with each parameter combination being less
   important than the previous by a fixed factor ... Consequently there is not
   a well-defined boundary between the stiff and sloppy combinations".
   Fig. 1 caption: eigenvalues "are roughly evenly spaced in log-space,
   extending over many orders of magnitude." Fig. 1 itself shows five spectra
   (systems biology, neural network, radioactive decay, diffusion, Ising),
   normalized, spanning about 6-7 decades.
3. **No quantitative criterion.** The review gives no threshold on decades
   spanned, no spacing test, no count. "Roughly log-linearly" / "roughly
   evenly spaced" / "many orders of magnitude" is all. The only numeric cut
   is practical, in Fig. 6's caption: the reduced EGFR model "has removed the
   irrelevant parameters identified as eigenvalues less than $1$ (dotted
   line)" (eigenvalues in units set by the measurement error).
4. **Stiff/sloppy are directions, not parameters (§I, §IV):** "the data
   places constraints on \textit{combinations} of the parameters"; Fig. 4:
   "The components of the smallest eigenvector of the FIM is often a
   complicated combination of bare parameters".
5. **Versus mere ill-conditioning.** The review does not draw this line
   explicitly; it says "The FIM ($J^TJ$) for a typical sloppy model is
   extremely ill-conditioned" (§VII, Levenberg-Marquardt). What it adds to
   ill-conditioning is (a) the shape, log-even spacing with no gap, and (b)
   its move to invariant geometry, because the spectrum alone cannot carry
   the claim (§III): "the eigenvalues of the FIM are not sufficient to make
   this conclusion"; "the FIM can be transformed into any positive definite
   matrix by a simple linear transformation of parameters while model
   predictions are always invariant to such a reparameterization." The
   invariant notion is the manifold: "the widths of sloppy model manifolds are
   exponentially distributed ... when we use dimensionless model parameters
   (e.~g.~log-parameters), the square roots of the FIM eigenvalues are a
   reliable approximation to the widths". So in this review sloppiness proper
   is a global property of the model manifold (bounded, hierarchy of widths
   and of extrinsic curvatures), of which the eigenvalue spread in log
   parameters is the local symptom.
6. **Versus singular / non-identifiable.** Not addressed. No mention of rank
   loss, singular models, Watanabe or structural identifiability. Its
   prototype is described as practically unidentifiable: "each parameter is
   \emph{almost completely undetermined}. Any parameter can be varied by an
   infinite amount and the model could still fit the data" (§I), the
   infinity coming from manifold boundaries ("Many parameters and parameter
   combinations can be taken to extreme values (zero or infinity) without
   leading to infinite predictions", §III; "evaporated parameters", §IV). It
   says compensation means parameters "cannot be individually identified"
   (§I). It does not remark that the sum of exponentials is singular where
   two rates coincide (the record's CASE-tmpb2gly). The FIM is called
   "positive semi-definite", nothing more.
7. **Relative to the experiment:** implicit, not stated as a definition
   condition: the hopping model is a "hyper-blob" after one step and a
   hyperribbon after many (Fig. 2); §VI: constrain parameters "with
   system-level measurements that are similar to the types of measurements we
   wish to predict".

## Why sloppiness is ubiquitous (its claims)

- **Collective observation / compensation (§I):** "In each case, observations
  measure a system's collective behavior, and this means that when parameters
  have compensatory effects they cannot be individually identified."
- **Interpolation (§III), the main theoretical argument:** "presuming
  smoothness or analyticity of the predictions as a function of time, one can
  demonstrate an exponential hierarchy of widths consistent with the
  hyperribbon structure observed empirically" (for "the case of a single
  independent variable"); "the model essentially functions as an
  interpolation scheme among observed data points. Models are predictive with
  unconstrained parameters when the predictions interpolate among observed
  data." Interpolation also predicts an exponential hierarchy of extrinsic
  curvatures, small relative to widths, explaining Bates and Watts' "mystery"
  of small extrinsic curvature.
- **Coarse-graining / RG (§V):** "many different multi-parameter microscopic
  theories typically collapse onto one coarse-grained model ... This
  parameter space compression underlies the success of renormalizable and
  continuum limit models." Hopping model: stiff directions are "the total
  number of particles, net mean velocity, and diffusion constant. As time
  evolves, all other microscopic parameter combinations become increasingly
  sloppy"; Ising: "develops stiff directions along precisely those parameter
  combinations deemed `relevant' under the renormalization group." A
  commented-out passage (not in the published text) says "RG arguments thus
  \textit{derive} the presence of sloppiness"; not attributable.
- **Speculative (§VII):** selection effect of what we choose to study, or
  evolution/modularity producing comprehensible circuits.

## Key results and claims (quoted)

- Prediction without parameters (§I): "As long as the model predictions
  depend on the same stiff parameter combinations as the data, the
  predictions of the model will be constrained in spite of large numbers of
  poorly determined parameters."
- Hyperribbon (§III): "The exponential distribution of manifold widths has
  been described as a \emph{hyperribbon}".
- MBAM (§IV): "approximate a high-dimensional, but thin model manifold by its
  boundary"; EGFR "29 differential equations and 48 parameters" reduced to "6
  differential equations and 12 parameters and is notably \emph{not sloppy}".
- Caution (Fig. 5, §VI): measuring parameters one by one "can fail if even one
  relevant parameter remains unknown".
- "Wrong" models (§VI): "an effective model that is microscopically
  inaccurate may still be insightful and predictive".
- PCA (§VII): singular values of data on a hyperribbon are "bounded by the
  hierarchy of widths" (argued, a bound left unproved in an author comment).
- Neural networks (§VII "Big data is reducible"): an autoencoder treated as a
  fitting problem "with parameters $\theta_\alpha$ giving the outputs of the
  digital neurons" (the code, not the weights); unpublished work by Hayden et
  al. shows "a clear hyperribbon structure". Fig. 1 includes a "Neural
  Network" spectrum, source not identified in the caption.
- Thesis (§VII): "adding more complexity to a model produces diminishing
  returns in fidelity, {\em because the model predictions have an underlying
  hyperribbon structure.}"

## Assumptions

Least squares with independent Gaussian errors, σ=1 (§II); FIM as metric,
local; interpolation argument assumes one independent variable and
smoothness/analyticity; width-eigenvalue correspondence needs log/dimensionless
parameters; generality of sloppiness is empirical (17 systems-biology models,
Gutenkunst et al. 2007, and the Fig. 1 cases).

## Concepts

sloppy/stiff directions; FIM as Riemannian metric; model manifold; manifold
boundaries; geodesic widths; hyperribbon; extrinsic vs parameter-effects
curvature; evaporated parameters; MBAM; information topology; parameter
space compression; model graph; geodesic acceleration; sloppy subspace.

## Errors noticed

- §II: "$\DKL(\theta||\theta+\delta \theta) = g_{\mu\nu} \delta \theta^\mu
  \delta \theta^\nu + \ldots$" omits the factor 1/2 (standard: ½ g δθ δθ).
- §V: hopping model's stiff directions listed as three (number, velocity,
  diffusion constant); Fig. 2 speaks of "two remaining extended directions"
  (normalized distributions; the count depends on whether particle number is
  a parameter). Minor.

## Verdict on the exchange's characterization

Accurate on sloppiness as the reason emergent simple theories exist (the
abstract: "simple theories of macroscopic behavior are hidden inside
complicated microscopic processes") and on the hyperribbon. On effective
dimension depending on resolution: the review supports only the
coarse-graining half (manifold contracts from hyper-blob to hyperribbon as
time is coarsened); it does not state that resolved dimension grows with data
or precision, nor give d_eff(n). A19 §5's caution that stiffness and RG
relevance should not always be equated is A's, not the review's: the review
says "precisely those". The neural-network analogy A presses has a source
here, but in a different sense (autoencoder code as parameters).

## Bearing on named codes

- **TERM-tmp5z2du (hyperribbon): supports, with one qualification.** Source
  of the term: "The exponential distribution of manifold widths has been
  described as a hyperribbon". Qualify the local-global tie: the review says
  √λ approximates widths only "when we use dimensionless model parameters
  (e.~g.~log-parameters)", and grounds the hierarchy in interpolation for "a
  single independent variable". Condition 1 (relative to experiment): consistent
  (Fig. 2 hyper-blob vs hyperribbon). Condition 2 (regular): the review is
  silent. "Not RG relevance": the review is less cautious than the TERM
  ("precisely those"); the caution rests on THEORY-777/742, not this work.
  The TERM's "no sharp line" matches "not a well-defined boundary between the
  stiff and sloppy combinations".
- **CLAIM-tmpficzj: supports** consequence 1 (quote above, §I) and the
  "simplicity of response" reading (abstract; §VI "wrong" models; §VII
  "Different models can describe the same behavior"). Bears on its
  defeated_if second clause: the review concedes that FIM eigenvalues are
  parametrization dependent and answers with manifold widths, so the claim is
  safer stated over widths than over eigenvalues. Qualifies its NN paragraph
  and ARG-tmpmvc5e: the review does press an NN analogy and shows an NN
  spectrum (Fig. 1), but its §VII parameters are the autoencoder's neural
  outputs, not weights; the regular/singular objection is not addressed.
- **CLAIM-tmpj0k4q: supports in part, leaves open the rest.** Compression
  half: §V/Fig. 2, "as time proceeds, the model manifold contracts onto a
  hyper-ribbon, in which just two parameter combinations distinguish
  behavior". The growth-with-n half and the counts: absent; nearest are
  §VI "it is hard to know $m$ ahead of time" and Fig. 6's cutoff "eigenvalues
  less than $1$", a fixed-data resolvability threshold of the nλ≳1 kind.
- **THEORY-774, THEORY-777: parallel/background** (qualitative restatement of
  Machta et al. 2013, LIT-1299). **THEORY-742: background**, not addressed.

## Recheck (record/ grepped for sloppy, hyperribbon, model manifold, MBAM,
evaporat, parameter space compression, extrinsic curvature, Levenberg,
information topology, neutral space, ill-conditioned, Transtrum/Machta/...)

Held entries the first search missed:
- **CLAIM-tmpcgvcp** (sloppiness vs singularity are different properties):
  the review neither supports nor contradicts; it offers no singular case and
  calls the FIM only "positive semi-definite". Leaves open; the record's
  distinction is its own, not this review's.
- **CASE-tmpb2gly** (sum of exponentials with rates u±v, singular at v=0):
  the review's own prototype; it does not note the singular stratum.
  Background, and worth noting in the NOTE.
- **TERM-tmpnxjq4** (weak direction, six senses; sense 4 "sloppy: vᵀIv, I
  invertible ... identified given enough data"): qualifies. The review's
  sloppiness mixes local (FIM) and global (boundaries, parameters running to
  infinity: "Any parameter can be varied by an infinite amount"), so its
  sloppy directions are not all "identified given enough data" at fixed
  design.
- **ARG-tmpmvc5e** (Rejected NN analogy): qualifies, as above.
- **CLAIM-tmpnu4ar** (reduction moves toward manifold boundaries): supports
  the reduction half (§IV MBAM).
- **CLAIM-tmpa8hb2, ARG-tmpj0r42, CLAIM-tmpcg4uu** (stratification and the
  hyperribbon): background; the review has nothing on strata.
- **CLAIM-tmppkdjz, ARG-tmpjx3ww** (width vs importance): the review equates
  sloppy with "unimportant ... little effect on model behavior" but relative
  to the fitted data, and Fig. 5 warns one unmeasured parameter can carry
  large predictive uncertainty: bears on ARG-tmpjx3ww's question whether the
  account mistook width for importance; it states importance relative to
  observed behaviour.
- **LIT-1299** (Machta et al. 2013), **LIT-1254** (Raju et al.,
  information loss under coarse graining), **LIT-1882** (LaMont and Wiggins):
  same programme, held; the review restates LIT-1299.
- **SYNTHESIS-tmp69tyj** (power laws): parallel; the review makes no
  power-law or criticality claim from sloppiness.

## Limitations

A review/perspective: results are cited, not derived (interpolation proof,
MBAM, Machta). Read from arXiv v1, not the published version. No
quantitative definition of sloppiness. Neural-network and PCA passages are
speculative; Hayden et al. is unpublished at the time.

## Candidate THEORY

Transtrum, Machta, Brown, Daniels, Myers and Sethna (2015) characterize a
sloppy model by Fisher eigenvalues roughly evenly spaced in log over many
decades with no gap between stiff and sloppy directions, and, since the
eigenvalues change under reparametrization, locate the invariant content in
a bounded model manifold whose widths fall exponentially (the hyperribbon),
which they derive from interpolation for smooth predictions in one
independent variable and read, through parameter-space compression, as why
coarse-grained physical theories and other emergent simple models predict
well.

promote_when: a reading of Transtrum, Machta and Sethna 2010/2011
(LIT-tmpd3swn, LIT-tmpzkxka) confirms that the interpolation argument gives
an exponential hierarchy of widths for smooth single-variable models and
that √λ in log parameters approximates those widths.
