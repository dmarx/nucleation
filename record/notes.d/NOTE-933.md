---
number: 933
status: Read
formerly:
- NOTE-tmpw0lqu
paper: LIT-1160
title: 'Donoho & Tanner — observed universality of phase transitions'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv PDF, 0906.2530v1 of 14 June 2009 (48 pages,
    the only arXiv version; the title page carries "Date: 14 May 2009"),
    extracted with pdftotext -layout: §§1–4 and the whole appendix, §5 with
    §§5.1–5.9, including every R regression transcript and Tables 1–10. The
    reference list was scanned. The published Phil. Trans. R. Soc. A
    version (21 pages) was not read: royalsocietypublishing.org returned
    403, so page and section numbers here are the arXiv copy's, and the
    appendix may not be in the journal text. Figures 1–24 were read from
    their captions, the surrounding text and the panel titles that survive
    extraction (the ρ(δ; C) values and widths printed over Figures 18–20,
    23 and 24); their plotted content does not survive. The axis labels of
    Figures 16, 17 and 21 extract as garbage. Dropped symbols were restored
    from context: ε in "ε = k/n" (§1.3), ≪ in "k ≪ N" and "n ≪ N" (§1.4).
date: '2026-10-14'
summary: >-
  For Gaussian matrices, ℓ1 minimization (and its nonnegative LP form)
  recovers a k-sparse vector from n random measurements in dimension N
  with probability tending to 1 below a curve ρ(δ; Q) in the plane δ = n/N,
  ρ = k/n, and to 0 above it; this was proved earlier and is restated here
  as Theorem 2.1. In 2,948,000 linear programs over eight non-Gaussian
  ensembles at N = 200, 400 and 1600, the 50% success points fall on the
  same curves, but exact finite-N agreement is rejected: the differences
  from the Gaussian decay as N^(-1/2), so the paper supports only an
  asymptotic ("weak") universality, as an observation, not a theorem.
---

# NOTE-933: Donoho & Tanner — observed universality of phase transitions

## Contribution

The sharp thresholds for sparse recovery by linear programming had been
proved only for matrices with iid Gaussian entries, by counting the faces
of randomly projected polytopes. This paper tests, by a confirmatory Monte
Carlo study with formal inference, whether the thresholds sit at the same
place for non-Gaussian matrices. It finds that they do in the large-N
limit, for the ensembles tried, and that they do not at finite N. It
states the result as a hypothesis, "weak universality", and poses the open
problem of characterizing the class of ensembles it holds for.

## Key insight

Where an ℓ1 recovery fails is a property of how a random projection treats
the faces of a regular polytope, and the location of that failure is
rigid: change the matrix ensemble from Gaussian to random signs, sparse
ternary, partial DCT or Hadamard, and the 50% point moves only by a
finite-size term of order N^(-1/2) that vanishes as the problem grows. The
paper calls this "a rigidity of the phase transition" and says it is far
stronger than universality in the statistical-physics sense, which allows
the location to move (§3.2, Clarification 1).

## Assumptions

- **Proportional growth.** n = δN and k = ρn with δ, ρ fixed and N → ∞
  (Theorem 2.1). δ ∈ (0, 1), so the systems are underdetermined.
- **The decoder is fixed.** Recovery means the solution of (LP),
  min 1ᵀx subject to y₀ = Ax, x ≥ 0, for nonnegative x₀, or of (P1),
  min ‖x‖₁ subject to y₀ = Ax, for signed x₀. "Success" is agreement with
  x₀ to six digits. The curves belong to these two programs. The paper
  says other algorithms have other, algorithm-specific transitions
  (§3.7, citing Maleki & Donoho 2009).
- **General position.** Lemmas 2.1 and 2.2 need the columns of A in
  general position. For the Gaussian ensemble this holds with probability
  one; for the sparse ensembles at small n it fails (§5.7.3).
- **The sparse vector.** Support uniform at random; nonzeros uniform on
  [0, 1] (+) or [−1, 1] (±). Footnote 6 says the values do not matter for
  (P1) and (LP).
- **The ensembles tried (Table 1).** Gaussian (suites 1–2, the baseline),
  Bernoulli, partial DCT ("Fourier"), Ternary (1/3), Ternary (2/5),
  Ternary (1/10), partial Hadamard, Expander and Rademacher, each with
  + and ± coefficients: 16 non-Gaussian suites over 8 non-Gaussian
  ensembles. The Fourier and Hadamard ensembles have dependent rows, the
  Expander dependent columns (§3.7).
- **Sizes.** N = 200, 400 and 1600 (Hadamard: N = 256 and 512); at N =
  1600, n from 160 to 1440 in 9 equal steps; k chosen to cover success
  rates from 5% to 95%; M = 200 trials per point, against a Gaussian
  baseline of M = 1000 at the same (k, n, N) (§5.1.2).

## Key results

- **Lemma 2.1 (simplex).** For A with columns in general position and
  x₀ ≥ 0 with k nonzeros, the fraction of systems (y₀, A) for which x₀ is
  the only solution of (LP) is f_k(AT^{N−1}) / f_k(T^{N−1}), where
  T^{N−1} = {x ∈ R^N : Σxᵢ = 1, xᵢ ≥ 0} (2.3) and f_k counts k-faces.
- **Lemma 2.2 (cross-polytope).** The same with (P1) and
  C^N = {x ∈ R^N : Σ|xᵢ| ≤ 1} (2.4): fraction = f_k(AC^N) / f_k(C^N).
- **Theorem 2.1** (credited to Donoho 2005a, b and Donoho & Tanner 2005a,
  b, 2009a; not proved here). For A n × N with iid N(0, 1) entries and
  n = δN, k = ρn, N → ∞, there are functions ρ(δ; Q), Q ∈ {T, C}, with
  lim f_k(AQ)/f_k(Q) = 1 for ρ < ρ(δ, Q) and 0 for ρ > ρ(δ, Q). And
  ρ(δ, T) > ρ(δ, C) for δ ∈ (0, 1). The paper gives no formula for either
  curve.
- **Values of ρ(δ; C).** Not tabulated; the panel titles of Figures 18–20
  and 24 print them: 0.189 at δ = 0.1, 0.2424 at 0.2, 0.2899 at 0.3,
  0.3364 at 0.4, 0.3848 at 0.5, 0.4375 at 0.6, 0.4979 at 0.7, 0.5724 at
  0.8, 0.6773 at 0.9.
- **The geometric reading (§1.5).** For n standard Gaussian points in R^d
  with δ = d/n and ρ = k/d below ρ(d/n; T), the typical (k+1)-tuple spans
  a k-face of their convex hull. With the points and their reflections,
  the same holds for ρ < ρ(d/n; C)(1 − ε).
- **Three appearances of ρ(δ; C) (§§1.2–1.4).** Forward stepwise
  regression with an FDR stopping rule at p = 200 (Donoho & Stodden 2006)
  "falls off a cliff" roughly at ρ(δ; C), with δ = n/p, ρ = k/n. The
  breakdown point of ℓ1 regression under a partial Hadamard design
  coincides with ε*(γ; C) = (1 − γ)ρ((n − p)/n; C), γ = p/n. Partial
  Fourier compressed sensing at N = 200 has its 50% success contour near
  ρ(δ; C), so recovery needs n ≳ k/ρ(n/N; C). The paper says "roughly" for
  the first and third.
- **Scale (§3.3).** 2,948,000 optimizations over 16,984 situations, 6.8
  CPU years, mostly with Mosek, checked against CVX.
- **Finding 1 (§3.5.1).** The Z-scores for success rates, non-Gaussian
  against Gaussian (Eq. 3.5), lie mostly in [−2, 2]. For Rademacher
  (Table 2) the counts with |Z| < 2 are 142, 199 and 380 against 139.4,
  196.6 and 374.2 expected at N = 200, 400, 1600.
- **Finding 2.** Strict (finite-N) universality is rejected. The mean
  Z-score has a nonzero trend in δ within each ensemble.
- **Finding 3.** Weak universality is not rejected: p₁(A) − p₀(A₀) =
  O_p(N^(-1/2)). For suites 3–10 the model µ(δ; N, E) = α(N, E) + β(N, E)
  (δ − 1/2), with α = α₀ + α₁/N^(1/2) and β = β₀ + β₁/N^(1/2) (5.7–5.8),
  has residual standard error 1.042 with α₀ = β₀ = 0 imposed and 1.043
  without; the added non-decaying terms give F = 0.7467, p = 0.7475, and
  none is significant at 0.10 (§5.5).
- **The exponent (Table 8).** Fitting α and β to N^(−γ), R² is highest at
  γ = 1/2 (0.9760 intercepts, 0.9822 slopes) among γ ∈ {1.5, 1.25, 1,
  0.75, 0.5, 0.33, 0.25}. Joint models with constant terms: F = 1.53 on
  12 and 23 df, p = 0.2394 (intercepts); F = 1.35, p = 0.30 (slopes)
  (§5.6). The authors say γ was chosen on the same data it is tested on.
- **Gaussian transition width (Table 5).** √N · w(δ, N) lies between
  0.6240 and 0.7277 for suite 2 over δ ∈ {0.2, …, 0.8} and N ∈ {200, 400,
  1600}, so w ∝ N^(-1/2). The figure panels use nominal widths of
  0.65/√N (my reconstruction from the printed ±0.04596 at N = 200 and
  ±0.01625 at N = 1600). The success rate is fitted by
  Φ̄((ρ − ρ(δ; Q))/w(δ, N; Q)); the probit link has the best likelihood,
  the logit gives more balanced residuals (§5.2.1).
- **Gaussian LD50 (Tables 3–4).** The empirical 50% point exceeds
  ρ(δ; C) at every δ and N tabulated, by 0.00076 to 0.0018 at N = 1600.
  Median N^(1/2)(LD50 − ρ) is 0.094, 0.079, 0.047 and median N(LD50 − ρ)
  is 1.324, 1.581, 1.881 at N = 200, 400, 1600. The paper reads this as
  convergence "at roughly the rate 1/N".
- **Method check (§5.3).** Gaussian against Gaussian: 170 of 180 (94.4%)
  and 175 of 181 (96.7%) Z-scores have |Z| < 2 (Table 6). Simplex against
  cross-polytope (suite 1 against suite 2): Z-scores down to about −30
  (Figure 12).
- **Exceptional ensembles (§5.7).** Ternary (1/10) and Expander (suites
  11, 12, 15, 16) fit badly at small N and small δ: some Z-scores reach
  20, the linear model's residual standard error is 1.854, a hinged model
  with knot at δ = 1/2 brings it to 1.706 (adjusted R² 0.5358 → 0.6071,
  F = 113.42). The residual SD falls with N and is below 1.10 at N = 1600
  in every suite (Table 9). The misfit is modelled as the LD50 displaced
  one transition width down, ρ† = ρ(δ; Q) − w, giving mean Z
  µ ∝ φ((ρ − ρ†)/w)/w (Figure 20).
- **Why they are exceptional (§5.7.3, Table 10).** Sparse matrices at
  small n have sparse null vectors, so columns are not in general
  position. Ternary (1/10) at N = 200, n ≤ 60 often draws an all-zero
  column (spark 1). Expander at N = 200, n ≤ 40 has null vectors with 6
  nonzeros. At N = 1600, n = 160 no null vector with fewer than 161
  nonzeros was found. The authors read the effect as transient: "for
  sufficiently large N, it becomes likely that spark(A) ≈ n".
- **Validation (§5.8).** Rademacher and Hadamard were analysed after the
  model was fixed. Rademacher fits the prespecified scaling model
  (residual SE 1.037); the authors call this inferentially rigorous.
  Hadamard behaves like the exceptional ensembles at N = 256, is fitted
  by the displaced-LD50 model with no refitting, and shows overdispersion
  at N = 512 for + coefficients. With only N = 256 and 512, its scaling is
  not tested.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | For iid Gaussian A, the fraction of k-sparse vectors recovered by (LP) or (P1) tends to 1 below ρ(δ; Q) and to 0 above it | strong | Theorem 2.1 with Lemmas 2.1–2.2, proved in the cited earlier papers, not here |
| C2 | For the eight non-Gaussian ensembles tried, the 50% success points match the Gaussian curves asymptotically ("weak universality") | moderate | Findings 1 and 3; §§5.5–5.6 regressions; three sizes only; out-of-sample check on Rademacher |
| C3 | Exact finite-N agreement with the Gaussian fails | strong | Finding 2; significant 1/√N terms in every non-Gaussian suite (§5.5) |
| C4 | Differences from the Gaussian decay as N^(-1/2) | moderate | Table 8, R² over three N; exponent chosen on the same data; untestable for Hadamard |
| C5 | Sparse ensembles are exceptional at small N because their columns are not in general position, and the effect is transient | moderate | Table 10, the displaced-LD50 fit, one size (N = 1600) where it is gone |
| C6 | The same curve governs stepwise regression's breakdown | weak | one cited simulation (Donoho & Stodden 2006), "roughly"; stepwise regression has no formal tie to polytopes (§1.6) |
| C7 | Universality here is a new kind of high-dimensional limit theorem | weak | conjecture, by analogy with the CLT (§3.2, §4) |

## Method

1. For each suite and each (N, n, k), draw M = 200 pairs (x₀, A), form
   y = Ax₀, and solve (LP) or (P1) without x₀.
2. Score ExactRecon = 1 when the solution matches x₀ to six digits.
3. Compare each suite's success fraction with the Gaussian baseline
   (M = 1000) at the same (N, n, k) by a two-sample binomial Z-score
   (3.5).
4. Test the strong null (Z ~ N(0, 1) everywhere) and the weak null
   (the mean and SD discrepancies decay with N) by linear models of Z on
   1/√N, δ − 1/2, ensemble and, for exceptional suites, a hinge
   (1/2 − δ)₊.
5. Hold out two ensembles (Rademacher, Hadamard) and fit the same models
   to them afterwards.

## Concepts

- **Phase transition** — here, a curve ρ(δ; Q) in the (δ, ρ) plane across
  which the limiting success probability jumps from 1 to 0; at finite N, a
  transition zone of width w ∝ N^(-1/2).
- **δ = n/N** — undersampling, measurements over unknowns. **ρ = k/n** —
  sparsity, nonzeros over measurements. Not k/N.
- **ρ(δ; T), ρ(δ; C)** — the transitions for the simplex (nonnegative
  x₀, (LP)) and cross-polytope (signed x₀, (P1)). T lies above C.
- **Strong (strict) universality** — equal success probabilities for every
  ensemble at every finite (k, n, N). Rejected.
- **Weak (asymptotic) universality** — differences that vanish as N grows.
  Not rejected.
- **Rigidity** — the authors' word for their universality: the transition's
  location is invariant across ensembles, not only its form.
- **LD50** — the ρ at which success is 50%, from bioassay usage.
- **spark(A)** — the number of nonzeros in the sparsest nonzero null
  vector of A. The paper writes spark(A) = n for Gaussian A; for a
  generic n × N matrix it is n + 1, which matches its own "no null vector
  with fewer than 161 nonzeros" at n = 160 (my observation; the off-by-one
  does not affect the argument).
- **Exceptional ensemble** — one whose Z-scores need a displaced-LD50 or
  hinge term at small N: Ternary (1/10), Expander, Hadamard.

## Connections

It rests on the face-counting results of Donoho (2005a, b) and Donoho &
Tanner (2005a, b, 2009a) for the Gaussian case, and on Donoho & Tanner
(2008b) for finite-N exponential bounds and the O(1/√n) width. It cites
Adamczak et al. (2009), who proved for ensembles with independent columns
that a success region exists, and says there is "no suggestion that this
region matches the region for the Gaussian". It cites Berinde et al.
(2008) for the expander evidence and Maleki & Donoho (2009) for other
algorithms. It does not discuss the restricted isometry property, the
Johnson–Lindenstrauss lemma or any union-bound argument.

## Bearing on the record

- **[QUESTION-120](../questions.d/QUESTION-120.md), the shape of the thresholds.**
  The question guesses each threshold is the log of a family's size over a
  squared tolerance. This paper's threshold is not of that kind. ρ(δ; Q)
  is an exact limiting location in the proportional regime k = ρδN,
  obtained by counting faces, not a sufficient condition from a union
  bound. The paper gives no k log(N/k) form and no small-δ asymptotics of
  ρ(δ; C). Its one remark on mechanism is a guess that the √N width is
  "typical when describing the frequency of success of an event among
  O(N) weakly dependent indicator variables" (§5.6), which is a CLT
  picture, not a concentration-plus-union-bound one. It also reports that
  the concentration-style result it knows (Adamczak et al.) proves a
  success region without matching the Gaussian one. My observation: so
  the question's general shape fits the sufficient bounds (JL, RIP), and
  not the sharp Donoho–Tanner curve, which needs a second kind of fact.
- **The superposition thread.** The question asks for the toy model's
  phase change to be compared with "the Donoho–Tanner curve at the same
  (δ, ρ)". The reading sets three conditions on that comparison. The
  curve belongs to (P1) or (LP), and the paper says other decoders have
  other transitions; the toy model decodes with a ReLU and a bias
  ([NOTE-278](NOTE-278.md)). Its coordinates are δ = m/n and ρ = k/m in the toy model's
  letters, with k the number of active features, not a sparsity fraction
  1 − S of all features. And it is a large-N limit, while the toy model's
  "phase change" is a discontinuity at small n and m ([NOTE-278](NOTE-278.md)).
  The values of ρ(δ; C) printed in the figures make a numerical
  comparison possible.
- **The expand-and-threshold thread.** The ensembles nearest to the fly's
  and SDM's sparse binary maps are Ternary (1/10) and Expander, and they
  are the ones that broke at small N, because their columns fail general
  position (an all-zero column, null vectors with 6 nonzeros). They
  conform by N = 1600. My observation: this paper is about compression
  (n < N) and recovery by LP, so it says nothing directly about expansion
  followed by a top-k threshold. It does show that sparse ensembles join
  the Gaussian class only past a size that depends on their sparsity.
- **The random-features thread.** Nothing. The paper has no kernels and no
  regression on random features.
- **Checks of what the record says about this paper.**
  - QUESTION: Donoho and Tanner "observe that the sparse-recovery
    transition does not depend on the ensemble". Imprecise. They observe
    it for eight non-Gaussian ensembles and only asymptotically. At finite
    N it does depend on the ensemble (Finding 2), by O(N^(-1/2)), and by a
    full transition width for sparse and Hadamard matrices at small N. The
    all-ones matrix is a stated counterexample, cyclic polytopes another
    (§3.7), and the class it holds for is an open problem.
  - LIT summary: "Simulations over many random matrix ensembles find that
    the sharp transition at which ℓ1 minimization stops recovering
    k-sparse vectors ... falls on the same curve as for Gaussian
    matrices." Imprecise on three points. It also covers nonnegative
    recovery by (LP), with its own curve ρ(δ; T). "Many" is eight
    non-Gaussian ensembles. The agreement is with the asymptotic Gaussian
    theory and holds only in the limit; finite-N universality is rejected.
  - LIT takeaway "For Gaussian matrices the curve is computed exactly by
    counting faces of randomly projected polytopes." Correct, but it is
    proved in the authors' earlier papers; this one restates it
    (Theorem 2.1) and gives no formula for the curve. "Succeeds with
    probability near 1 below a curve" holds in the limit; at finite N
    there is a zone of width about 0.65/√N.
  - LIT takeaway "Many non-Gaussian ensembles (random signs, partial
    Fourier, sparse matrices and others) put the transition on the same
    curve. It is an empirical finding ... not proved." Correct in
    substance. "Partial Fourier" in the study is partial DCT; random
    Fourier sampling appears only in the illustrative Figure 3 (N = 200).
    It omits that strict universality was rejected and that three
    ensembles were exceptional at small N.
  - LIT Standing: the `mathematical-statistics` tag "for its reading of
    the transition as a limit on what can be inferred from undersampled
    data". Supported: the abstract says the thresholds "place hard
    limits" on high-throughput linear modelling, and the arXiv class is
    math.ST.
  - Bibliography: the journal volume, issue and pages (367(1906):
    4273–4293) and the DOI cannot be checked against this copy, which
    carries neither. The arXiv date 14 June 2009 matches `published:`;
    the copy's own date line is 14 May 2009.
- **For the anthology.** The paper's applied claims, how many measurements
  an MRI scanner needs and when stepwise regression breaks, are practice
  in statistics and signal processing, not machine learning. Nothing here
  is an instruction for machine-learning practice.

## Limitations

- An observational study. Nothing about non-Gaussian ensembles is proved,
  and the authors say the result "goes far beyond current theory".
- Three problem sizes, the largest N = 1600; two for Hadamard. A decay
  rate fitted on three points, with the exponent chosen on the same data
  (the authors say so; only Rademacher validates it out of sample).
- Eight non-Gaussian ensembles, all with "a certain air of 'orthogonality'
  or 'weak independence'" (§3.7). The universality class is not
  delineated.
- Two decoders only. The curves are not claimed for other algorithms.
- The paper is inconsistent in places. Table 1 describes Rademacher, like
  Bernoulli, as "equally likely to be 0 or 1". The caption's rule
  "Ternary(p) has P(0) = 1 − p and P(±1) = (1 − p)/2" cannot both hold
  (P(±1) should be p/2), and Ternary (1/3) is described as uniform on
  {−1, 0, 1}, P(0) = 1/3, while Figure 4 labels it "p = 2/3". The Expander
  is P(0) = 14/15 in Table 1, "p = 1/5" in Figure 4 and "(1/15)" in §5.7.3.
  §3.3 counts "8 different matrix ensembles", §5.1.1 "9" (with the
  Gaussian). §5.9 says all "but two" ensembles behave like the Gaussian,
  while §5.8 adds Hadamard as a third exception. The Figure 2 caption
  gives the vertical axis of panel (b) as k/p; the text and axis say
  k/(n − p). None of these changes a finding.
- The stepwise-regression surprise rests on another paper's simulation
  and the word "roughly".

## Open questions

- The authors' open problem: characterize the class of matrix ensembles
  whose transitions match the Gaussian's. A theorem for any non-Gaussian
  ensemble would close part of it.
- Whether the 1/√N discrepancy has the CLT-like source the authors guess
  at (§5.6).
- For the record: where the toy model of superposition's boundary lies
  relative to ρ(δ; C) when its coordinates are mapped as above, and
  whether a ReLU-with-bias decoder has a transition of its own at all in
  the large-n limit.
- Whether expanding sparse binary maps of the fly's kind have an analogue
  of the general-position failure seen here at small n.
