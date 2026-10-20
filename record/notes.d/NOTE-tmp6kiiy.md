---
status: Read
paper: 'LIT-tmpf5lvd'
title: 'Wiskott and Sejnowski — Slow feature analysis'
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Read in full from Wiskott's own PostScript preprint (49 pp., the
    `url:` on the LIT), whose first page says the version "does not differ
    significantly from the final version" in Neural Computation 14(4). It
    was converted with Ghostscript and the text extracted with pdftotext.
    The typeset article was not compared. Read: the abstract, §1, §2 (the
    learning problem, Eqs. 1–4), §3 (the algorithm, Eqs. 5–34, footnote 1
    and the neural implementation), §4.1–4.4 (Examples 1–5 with Tables 1–6
    and the figure captions), §5 with §5.1–5.2, and the references. The
    extraction dropped the ligature letters ("c", "fi", "ff") and set
    subscripts and Greek symbols on separate lines, so the displayed
    equations were reconstructed from their layout and the prose. Every
    reconstructed equation used here is consistent with the text around
    it, and the closed form is re-derived in THEORY-tmp45pcv. The figures
    were read from captions and text only, so the plotted functions,
    trajectories and η-curves were not judged. Tables 4 and 6 lost their
    column alignment and their icons, and only the numbers the prose
    repeats are cited from them.
date: '2026-10-20'
summary: >-
  Finds instantaneous functions y = g(x(t)) whose outputs vary as slowly as
  possible, minimizing ⟨ẏ²⟩ under zero mean, unit variance and
  decorrelation. Over a fixed nonlinear expansion (all monomials of degree
  one and two), the problem is solved in closed form by sphering and then
  taking the smallest eigenvectors of the derivative covariance, a
  generalized eigenproblem. Stacked modules learn translation, size,
  rotation, contrast and, less well, illumination invariance for 1-D
  patterns, depending only on the training stimulus. The closed form is
  proved; everything about invariance, generalization and hierarchy is
  demonstrated on synthetic signals. The premise that slower means more
  abstract is assumed, not shown, and no generative model is used.
---
<!-- inactive-ok-file: CLAIM-331 CLAIM-327 THEORY-186 — Proposed; claims and accounts this reading bears on, nothing here rests on their being settled -->

# NOTE-tmp6kiiy: Wiskott and Sejnowski — Slow feature analysis

## Contribution

It turns the slowness principle for learning invariances, which earlier
work pursued with online rules (Földiák's trace rule, Mitchison's
anti-Hebbian synapse, Becker and Hinton's mutual-information modules), into
a closed-form algorithm. A nonlinear expansion makes the problem linear in
the expanded signal, so sphering and an eigendecomposition give the global
optimum within the chosen function space in one shot, with many ordered,
decorrelated outputs at once. The paper shows that hierarchical stacks of
such modules learn a range of invariances for one-dimensional patterns from
the training stimulus alone.

## Key insight

Ask for functions of the present input whose outputs change slowly, and
forbid the trivial answers by fixing their variance and making them
decorrelated. "Slow variation of the output signal can therefore not be
achieved by temporal low-pass filtering, but must be based on extracting
aspects of the input signal that are inherently slow" (§1). Within the span
of a fixed basis this is a Rayleigh-quotient problem, so the slowest outputs
are eigenvectors and their slowness values are eigenvalues.

## Assumptions

- **A training signal of fixed length, processed as one batch.** Averages
  ⟨f⟩ are temporal averages over [t₀, t₁] (§2). No stationarity, ergodicity
  or generative model is stated. The paper does not say how ż is computed
  from the sampled signal; a difference quotient is implied.
- **An instantaneous input–output function.** g acts on x(t) alone. Where
  temporal context is needed, it is supplied by appending delayed copies to
  the input (Example 2, x₆…x₁₀ = x₁…x₅ delayed one sample).
- **A fixed function space.** g_j(x) = Σ_k w_jk h_k(x) with fixed h_k: all
  monomials of degree one (SFA¹) or of degrees one and two (SFA²),
  K = I + I(I + 1)/2. Optimality is claimed only within this span.
- **The premise.** "Primary sensory signals, which in general code for
  local properties, vary quickly while the perceived environment changes
  slowly" (§1), and "a slowly varying representation can be considered to
  be of higher abstraction level than a quickly varying one". Both are
  stated as motivation and are not tested.
- **For Examples 4–5:** a one-dimensional retina of 65 sensors; patterns
  of low-pass filtered Gaussian noise (size 15–30, filter width 2–5) or
  Lambertian-shaded random depth profiles, moved one at a time with
  pauses, never two in view; and, by the symmetry of architecture and
  stimulus, one module trained per layer and copied, which the authors say
  amounts to "an implicit weight sharing constraint".

## Key results

- **The learning problem (§2, Eqs. 1–4).** For each j, minimize
  Δ(y_j) = ⟨ẏ_j²⟩ subject to ⟨y_j⟩ = 0, ⟨y_j²⟩ = 1 and
  ⟨y_j′y_j⟩ = 0 for all j′ < j. "Strict invariances are not the goal, but
  rather approximate ones that change slowly." The ordering
  Δ(y_j′) ≤ Δ(y_j) for j′ < j follows because y_j carries more
  constraints. Folding the constraints into the objective, as
  Δ/⟨(y − ⟨y⟩)²⟩ (Becker and Hinton 1992), leaves an arbitrary offset and
  scale.
- **The closed form (§3, Eqs. 5–8, 19–26).** After sphering the expanded
  signal (⟨z⟩ = 0, ⟨zzᵀ⟩ = I), the constraints hold "if and only if" the
  weight vectors are orthonormal, and Δ(y_j) = w_jᵀ⟨żżᵀ⟩w_j. So the w_j are
  the eigenvectors of ⟨żżᵀ⟩ with the smallest eigenvalues λ_j, and
  Δ(y_j) = λ_j. In the raw expanded coordinates this is the generalized
  eigenproblem ⟨ż̃ż̃ᵀ⟩w = λ cov(z̃)w. The paper does not use that phrase.
  SVD replaces PCA, and near-zero singular values are discarded. The
  record's step-by-step derivation, with the singular case, the joint
  form and the basis-independence, is [THEORY-tmp45pcv](../theory.d/THEORY-tmp45pcv.md).
- **The η-index (Eq. 34).** η(y) = (T/2π)√Δ(y) over a window of length
  T. For y = √2 sin(2πnt/T), η = n (footnote 1; checked here).
- **Example 1 (§4.1).** From three simple-cell signals, one a distractor,
  quadratic SFA's first output extracts the shared amplitude (in fact its
  square), the complex-cell response: r = 0.99. On longer signals,
  r = 0.981 ± 0.004 on training and 0.93 ± 0.04 on test data. Phase is not
  extracted, "because it is a cyclic variable".
- **Example 2 (§4.1, Table 1, Fig. 6).** Ten inputs (five binocular simple
  cells plus delayed copies) give 63 usable quadratic outputs, whose
  η-values "grow almost linearly" with index. Ten to sixteen are slower
  than the input: disparity, amplitude, phase change (velocity), squared
  disparity, products such as disparity times amplitude change. The
  features are spread over outputs: velocity correlates 0.66, 0.34 and
  0.33 with three of them, 0.94 with the best combination of the first
  14. "The decorrelation constraint is not sufficient to isolate the slow
  features into separate components." Linear SFA extracts none of them.
- **Example 3 (§4.2, Table 2, Figs. 7–8).** A slow signal x_s hidden as
  x̃ = [x_f, sin(2x_f) + 0.5x_s] needs more than a quadratic function.
  Repeating quadratic SFA, three outputs passed each time, gives
  correlations 0.59, 0.61 and 0.97 at stages one to three. "Only the
  third SFA extracts a slow feature. The first and second SFA did not
  yield an η-value lower than that of the input signal." A rarely
  switching binary signal behaves the same (0.43, 0.69, 0.97): rare and
  slow are not distinguished at matched η.
- **Example 4 (§4.3, Figs. 9–19).** Four layers, each a linear SFA module
  with convergent input (three neighbours, or nine retinal sensors) and a
  quadratic one with direct input, over 65 sensors. Nine outputs per
  module, signals clipped at ±3.7 between modules. Trained on 20 patterns,
  tested on 50.
  - The top outputs respond to a passing pattern with a half or full sine
    wave, "a better compromise between signal constancy in the center and
    smooth onsets and offsets" than a constant. Outputs 1 and 3 carry
    location ("where"), outputs 2 and 4 pattern identity ("what"),
    unprompted, although "for some parameter regimes … no explicit
    where-components emerge".
  - Response-vector angles across locations average 12.6° on test and
    11.3° on training patterns, against 90° by chance. Normalized average
    rank is 0.05 on training and 0.12 on test patterns, against chance
    near 0.5. Twenty training patterns suffice, and five give "reasonable
    performance". Performance holds down to four propagated components
    per module and falls to chance with one. It degrades gracefully with
    added noise, reaching chance near noise level 2.
  - The layer-1b function weights monomials of the same degree and spread
    in a bell or half-sine profile across location, a "fade-in/fade-out
    mechanism" related to hand-built higher-order networks with weight
    sharing.
  - η falls across layers (Fig. 19), with the linear a-sublayers
    contributing slightly more beyond 1b. The test curves "are not
    monotonic and cross each other".
  - No implicit similarity measure was found: the correlation between the
    best shifted pattern correlation and the response angle was only
    −0.47.
- **Example 5 (§4.4, Tables 4–6, Figs. 20–23).** The same network, trained
  on patterns that vary in one of location, size, cyclic shift
  ("rotation"), contrast or illumination angle, learns that invariance.
  Extrapolated test ranks for many training patterns: 0.050 location,
  0.015 size, 0.055 rotation, 0.000 contrast, 0.160 illumination.
  Illumination does not generalize across a change in the sign of the
  light angle. Training for translation also gives some size invariance,
  not the reverse, and illumination gives some contrast invariance, not
  the reverse. Training on two or three invariances at once degrades
  performance, for two named reasons: the space of patterns grows, and the
  mechanisms for different invariances "may not be compatible".
- **Relation to Becker and Hinton (§5.1, Eq. 42).** With a = y(t) and
  b = y(t − 1), I = ½ log(V(a + b)/V(a − b)) is "almost identical" to Eqs.
  1–4, so "the information theoretic approach provides a systematic
  motivation but not a different optimization problem". Checked: with
  equal unit variances, I = ½ log((4 − Δ₁)/Δ₁), strictly decreasing in
  Δ₁ = ⟨(y(t) − y(t − 1))²⟩.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Within a fixed function space, the slowest decorrelated unit-variance outputs are the bottom eigenvectors of the sphered derivative covariance, found in one shot and globally | strong | §3, Eqs. 5–8, with Mitchison (1991); re-derived in [THEORY-tmp45pcv](../theory.d/THEORY-tmp45pcv.md) |
| C2 | Repeated SFA approximates input–output functions of higher degree at lower cost than a direct high-degree expansion | moderate | Example 3, one construction, means over 10 runs |
| C3 | A hierarchical network of SFA modules learns translation, size, rotation, contrast and, to a lesser degree, illumination invariance for 1-D patterns, depending only on the training stimulus | moderate | Examples 4–5, synthetic 1-D patterns, 3–5 runs per condition |
| C4 | A few training patterns generalize to new patterns | moderate | Fig. 15; for translation; with clipping, which the authors call "crucial" |
| C5 | Where- and what-information emerge in separate components without being built in | weak | Fig. 11 and the authors' own statement that it fails in some regimes and is "unclear" why |
| C6 | Learning several invariances at once degrades performance | moderate | Tables 4 and 6 |
| C7 | SFA is not particularly sensitive to noise | weak | an informal argument (§5) and Fig. 17 |
| C8 | A slowly varying representation is of a higher abstraction level | assumed | stated as the premise (§1), not tested |

## Method

1. Normalize each input component to zero mean and unit variance.
2. Expand nonlinearly: z̃ = h̃(x), all monomials of degree one, or of
   degrees one and two.
3. Sphere: z = S(z̃ − ⟨z̃⟩) with ⟨zzᵀ⟩ = I, by SVD, discarding directions
   of near-zero variance.
4. Diagonalize ⟨żżᵀ⟩. The J eigenvectors with the smallest eigenvalues
   give g_j(x) = w_jᵀh(x) and y_j with Δ(y_j) = λ_j.
5. Optionally feed the first few outputs, or a combination of several
   modules' outputs, to a new module, and repeat from step 2.
6. Apply the stored offsets, scalings, S and w_j to test data, which are
   then only approximately normalized.

## Concepts

- **Slowness Δ(y)** — ⟨ẏ²⟩ of a zero-mean, unit-variance output.
- **η-index** — (T/2π)√Δ: the number of oscillations a pure sine of the
  same Δ would make in the window.
- **Invariance** — slow variation of the output, not constancy: "Strict
  invariances are not the goal."
- **Where- and what-information** — location and identity of a pattern.
  The paper argues both are slow relative to the sensory signal and both
  can be extracted by the slowness objective.
- **SFA module** — one application of the algorithm, read as a neuron
  with fixed nonlinear dendritic clusters (sigma-pi units) or as an RBF
  network with fixed hidden units, with lateral anti-Hebbian connections
  for decorrelation (Fig. 3). Not an online rule.

## Connections

It positions itself against two families of online rules (§5.1): trace
rules after Földiák (1991), Wallis and Rolls (1997) and Eisele (1997), whose
winner-take-all decorrelation yields a one-of-n code rather than distinct
slow features, and information-theoretic rules after Becker and Hinton
(1992), Zemel and Hinton (1992), Stone and Bray (1995) and Stone (1996),
whose objective it shows to be nearly its own. Mitchison (1991) had the
eigenvector solution for linear units, normalized by Σw² rather than output
variance, which the paper shows to be wrong-footed: a zero input component
would win. Its claimed novelty is the closed form, made possible by the
expansion. Pfau et al. ([LIT-252](../literature.d/LIT-252.md), [NOTE-824](NOTE-824.md)) later treat SFA, through
Sprekeler (2011), as the graph-Laplacian case of a spectral inference
network.

## Bearing on the record

- **THEORY filed: [THEORY-tmp45pcv](../theory.d/THEORY-tmp45pcv.md) (Active).** The closed form as a
  generalized eigenproblem, with the record's derivation. It adds one
  consequence the paper does not draw: in a stack whose stages contain
  their inputs' linear span, each of the first m slowness values can only
  stay or fall from stage to stage, on the training signal.
- **[CLAIM-331](../claims.d/CLAIM-331.md).** The paper takes "slower = more abstract" as its
  premise (C8), not as a finding. So its hierarchy is not independent
  evidence that higher levels are slower: [THEORY-tmp45pcv](../theory.d/THEORY-tmp45pcv.md) shows that in an
  unclipped stack the higher stage cannot be faster on the training data,
  because the objective forbids it. Three points cut finer than the claim
  does. (1) The inequality is weak and stalls: two stages in Example 3
  gain no slowness before a third does. (2) On test data the η-curves
  across layers cross and are not monotonic (Fig. 19). (3) The slowest
  outputs include location, which is not an invariant. The paper's own
  framing is that "what" and "where" are slow together relative to the
  sensors. Slowness picks out what the claim calls a level only together
  with another criterion, which is the claim's "a mark of a level and not
  its definition". Recommended: a note on the claim recording that a
  hierarchy optimized for slowness is slower by construction and only
  weakly, so it should not be cited as a case for the temporal facet.
- **[CLAIM-327](../claims.d/CLAIM-327.md), [CASE-116](../cases.d/CASE-116.md).** An SFA output is an observer's
  statistic in the strictest sense: a function of the present input that
  nothing reads back. The network is feedforward, and "processing is
  instantaneous". It is [CASE-116](../cases.d/CASE-116.md)'s arm A at the level of features, a slow
  variable nobody reads, and so by [CLAIM-327](../claims.d/CLAIM-327.md) not a level of the system it
  describes, whatever its slowness. Nothing in the paper bears on
  endogeneity.
- **[QUESTION-tmp8qovh](../questions.d/QUESTION-tmp8qovh.md).** The brief question was under which
  generative assumptions slow features are coarse, predictively
  sufficient or quickly learned.
  - **Generative assumptions.** The paper has none. Its only premise is
    the informal one in Assumptions. When the slowest features recover
    the latent variables of a generative process is not addressed. §5.2
    names "the optimal responses of an SFA-module" as future work.
  - **Coarse.** In the refinement sense, a stack is a chain: each stage's
    outputs are functions of the stage below. Within a stage, the spans of
    the first k outputs nest in eigenvalue order ([THEORY-tmp45pcv](../theory.d/THEORY-tmp45pcv.md)). But a
    slow feature is not coarse in any other sense. Example 2's slow
    features include squares and products of the generating signals, and
    the slowest top-level output is location.
  - **Predictively sufficient.** Not addressed. The lag-one identity in
    [THEORY-tmp45pcv](../theory.d/THEORY-tmp45pcv.md) shows that each output maximizes its own lag-one
    autocorrelation, so each is maximally self-predictable from its
    previous value. That is not sufficiency for predicting the input.
  - **Quickly learned.** Not addressed. The solution is closed form, and
    the paper says nothing about the order in which an online rule would
    acquire the features.
  The question gains a third exactly-commuting case beside
  [THEORY-tmp3xg7a](../theory.d/THEORY-tmp3xg7a.md): refinement and the slowness order agree because both
  come from the objective. The answer the question wants, conditions
  under which an independently given hierarchy matches the slowness
  order, is not here.
- **[LIT-252](../literature.d/LIT-252.md), [NOTE-824](NOTE-824.md).** [NOTE-824](NOTE-824.md)'s description of SFA ("Minimizing
  the expected squared change of features between adjacent frames under
  unit second moment") matches §2 with the zero-mean constraint folded
  in. Correct as written.
- **[LIT-tmpzunec](../literature.d/LIT-tmpzunec.md) and [THEORY-186](../theory.d/THEORY-186.md).** These concern orders of
  acquisition by spectrum. SFA orders converged features by a different
  spectrum, that of the pencil (⟨ż̃ż̃ᵀ⟩, cov z̃), and has no learning
  dynamics to compare.
- **Anthology.** The flag `anthology-candidate` stays: the paper is a
  representation-learning method. It carries no instruction for
  machine-learning practice in general. Its practical advice is internal
  to its own algorithm: use SVD rather than PCA on degenerate expansions,
  clip transferred signals, and propagate a few components between
  modules.
- **Not cited by any entry for something it does not say.** [CLAIM-331](../claims.d/CLAIM-331.md) and
  [QUESTION-tmp8qovh](../questions.d/QUESTION-tmp8qovh.md) cite it only as unread.

## Limitations

- **"Guaranteed to find the optimal solution" holds per module, for the
  training signal and the chosen function space.** The hierarchy is
  greedy, without backpropagation, and is not optimal over the composite
  function class. Example 3's stalls show that the greedy stack can pass
  through stages that gain nothing.
- **Slowness is not invariance.** The title says "Learning of
  Invariances". What is learned is slow functions, which include
  location, an equivariant variable (Example 4). The authors say so in
  §1, and the title still overstates.
- **The half-sine response is explained heuristically.** No optimal
  response is derived, and the authors list that analysis as future work.
- **The what–where separation is unexplained** in the authors' words
  ("It is unclear why the second where-component … emerges so
  reliably").
- **Generalization depends on clipping**, which is "crucial" and was not
  tuned. Test outputs are only approximately normalized.
- **One inconsistency.** The text gives an average test rank of 6.9 for
  Fig. 14, and the caption gives 6.2. The text's normalized 0.12 matches
  6.9, since (6.9 − 1)/49 = 0.120 and (6.2 − 1)/49 = 0.106. The training
  values agree: (1.9 − 1)/19 = 0.047, reported as 0.05.
- **Synthetic one-dimensional stimuli only**, presented one at a time.
  Learning from natural image sequences is named as open (§5.2). Only one
  module per layer was trained, so the absence of weight sharing that
  Fig. 9 stresses is not tested.
- **The curse of dimensionality.** A quadratic expansion of I inputs has
  I + I(I + 1)/2 dimensions, which limits each module to small inputs
  ("up to 12 dimensions").
- **The derivative estimate is not stated.**

## Open questions

- Under what generative model of x(t) do the slowest functions recover
  its latent variables, and in what form (the half-sine responses suggest
  harmonics of the latent variables rather than the variables
  themselves)? An analytic solution for the unconstrained (free-response)
  problem would answer it. Later work by Wiskott and colleagues is
  standardly cited for this and is not in the record.
- Is the degradation under several invariances fundamental, or does it
  disappear with more patterns and more propagated components (§5.2)?
- Can SFA be combined with independent component analysis to separate the
  slow features that decorrelation leaves mixed (§5.2)?
- For [QUESTION-tmp8qovh](../questions.d/QUESTION-tmp8qovh.md): in what order does an online slowness rule (a
  trace rule, or SFA by gradient) acquire the eigen-features, and is it
  the slowness order?
