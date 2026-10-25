---
status: Read
paper: LIT-tmpcevhu
title: 'Wald — Sequential tests of statistical hypotheses'
version: 1
history:
- version: 1
  date: '2026-10-25'
  note: >-
    Read in full from the copy the owner supplied on 2026-10-25: a JSTOR
    scan of The Annals of Mathematical Statistics 16(2): 117–186, 70
    pages, with no text layer. The pages were rendered at 300 dpi with
    pdftoppm and run through tesseract, and the text was read in full:
    the table of contents, Introduction A, Historical Note B, Part I §§1–4
    (the current test, general definitions, the sequential probability
    ratio test with §§3.1–3.5, the number of observations with §§4.1–4.7)
    and Part II §§5–6 (one-sided alternatives, binomial, double
    dichotomies, normal mean, and the outline of a general theory with
    weight functions), Tables 1–3, Figures 1–7 from their captions and
    text, and the 11 references. Extraction garbled most displayed
    equations, so the ones the record relies on were read from page
    images: (3.1)–(3.10), (3.16)–(3.29), (3.34)–(3.40), (4.7)–(4.14),
    (4.26)–(4.34), Table 1, (4.47)–(4.52) and (4.75)–(4.82). The
    calculations of η, δ, ξ and ξ′ for the binomial and normal cases
    (§§3.5 and 4.2, with their Mills-ratio lemma), the truncation bounds of
    §4.6 and the examples of §6 were followed for their results from the
    extracted text, not checked line by line. The main results are
    re-derived and checked numerically in THEORY-tmpeglfj and
    THEORY-tmpda363.
date: '2026-10-25'
summary: >-
  Defines the sequential probability ratio test: sample until the
  likelihood ratio of two simple hypotheses leaves an interval (B, A).
  Exact inequalities tie A and B to the error rates, so A = (1 − β)/α and
  B = β/(1 − α) are set with no distribution theory, and the realized
  errors can rise above α or β only slightly. It derives the operating
  characteristic and the expected sample size. It proves that no test with
  the same errors needs fewer observations on average under either
  hypothesis, once the overshoot of the boundaries is neglected, and for a
  normal mean it saves about half the fixed-sample test. It never mentions
  diffusion or Brownian motion.
---
<!-- inactive-ok-file: CLAIM-262 — Proposed; the owner's earlier statement of the hypothesis, named, nothing here rests on it -->
# NOTE-tmpxtksz: Wald — Sequential tests of statistical hypotheses

## Contribution

It names the sequential probability ratio test and gives its theory: when
it stops, how its boundaries relate to the error probabilities, its
operating characteristic, and the distribution and mean of its sample
size. Against any other test of the same strength, it is optimal up to
the overshoot. Before it, sequential procedures were double or multiple
sampling schemes (Dodge and Romig, Bartky) with no optimality theory.
After it, a test of a simple hypothesis against a simple alternative
needs, on average, about half the observations of the Neyman–Pearson test
with the same α and β.

## Key insight

Accumulate the log likelihood ratio Z_m = Σ log f₁(xᵢ)/f₀(xᵢ) and stop when
it leaves (log B, log A). The boundaries are set by the error rates alone,
because on every sample path that accepts H₁ the ratio is at least A, so
P₁(accept H₁) ≥ A·P₀(accept H₁). No sampling distribution has to be
computed. "Another surprising feature of the sequential probability ratio
test is that the test can be carried out without determining any
probability distributions whatsoever" (p. 119). The motivation is
Bayesian (§3.1). With a prior, a rule that stops when either posterior
passes a level d > ½ is a pair of likelihood-ratio thresholds that do not
depend on m. Dropping the prior gives the SPRT.

## Assumptions

- Two simple hypotheses, densities (or probability functions) f₀ and f₁ of
  one random variable X (§1). Part II reduces one-sided and composite
  problems to this case, or to mixtures over a weight function.
- For the definition and the error inequalities (3.18)–(3.19): only that
  the test terminates with probability one (3.11). "The independence of
  the observations is, however, not necessary for the validity of (3.18)
  and (3.19)" (p. 130), with an autoregressive example.
- For the operating characteristic, the sample size and the optimality
  theorem: independent, identically distributed observations, so that
  zᵢ = log f₁(xᵢ)/f₀(xᵢ) are i.i.d. with nonzero variance, and A > 1 > B
  (α + β < 1).
- The practical formulas neglect the excess of Z_n over the boundary at
  stopping: "If both | Ez | and the standard deviation of z are small",
  which "will be the case when f₁(x) is near f₀(x)" (pp. 135, 143).

## Key results

- **Definition (3.8)–(3.10).** Accept H₁ if p₁ₘ/p₀ₘ ≥ A, accept H₀ if
  p₁ₘ/p₀ₘ ≤ B, take another observation if B < p₁ₘ/p₀ₘ < A, with
  0 < B < A. The test "has been justified here merely on an intuitive
  basis" (p. 127), from the posterior thresholds (3.1)–(3.7).
- **Termination (3.11).** It stops with probability one under either
  hypothesis, by Lemma 1 of Wald's "On cumulative sums of random variables"
  (1944), cited and not reproved.
- **The fundamental inequalities (3.16)–(3.19).** 1 − β ≥ Aα and
  β ≤ B(1 − α), that is α/(1 − β) ≤ 1/A and β/(1 − α) ≤ B. Hence α ≤ 1/A,
  β ≤ B (3.20)–(3.21).
- **Setting the boundaries (3.24)–(3.30).** The exact boundaries satisfy
  A(α, β) ≤ (1 − β)/α and B(α, β) ≥ β/(1 − α). With A = (1 − β)/α and
  B = β/(1 − α), the realized errors satisfy α′ ≤ α/(1 − β),
  β′ ≤ β/(1 − α) and α′ + β′ ≤ α + β, so "at most one of the probabilities
  α and β may be increased" (p. 132). The gap is "merely on account of the
  fact that the number m of observations is discontinuous". "If fractional
  observations were possible … A(α, β) and B(α, β) would be exactly equal
  to (1 − β)/α and β/(1 − α) respectively" (p. 132).
- **Operating characteristic (3.32)–(3.35).** Let h ≠ 0 solve
  E e^{hz} = 1. Then E e^{hZ_n} = 1 (3.32), the probability γ of accepting
  H₁ is (1 − E*)/(E** − E*) exactly (3.34), and
  γ ≈ (1 − B^h)/(A^h − B^h) (3.35). "It is easy to verify that h = 1 if
  H = H₀, and h = −1 if H = H₁." The paper gives bounds (3.42), (3.44), and
  an exact solution when z is a lattice variable (3.45)–(3.48).
- **Expected sample size (4.4)–(4.14).** EZ_n = En·Ez (4.4), so
  En = [(1 − γ)E*Z_n + γE**Z_n]/Ez (4.7) and
  En ≈ [(1 − γ) log B + γ log A]/Ez (4.8), with bounds through the maximal
  expected overshoot ξ, ξ′ (4.9)–(4.14).
- **Savings for a normal mean (§4.3, Table 1).** With E₁(z) = E₀(−z) =
  ½(θ₀ − θ₁)², the ratios E_i(n)/n(α, β) do not depend on θ₀, θ₁, and for
  α, β from .01 to .05 the saving is 47–63%: "at least 47 per cent" (p. 148).
- **Distribution of n (§4.4).** The fundamental identity
  E{e^{Z_n t}[φ(t)]^{−n}} = 1 (4.35) gives the characteristic function of n.
  For normal z with one boundary, m = (Ez)²n/2σ_z² has the density
  c/(2Γ(½)m^{3/2}) e^{−c²/4m − m + c} with c = (Ez) log A/σ_z² (4.51). The
  paper notes that a density for a discrete n is an artefact of neglecting
  the excess.
- **Termination and truncation (§§4.5–4.6, Tables 2–3).** Lower bounds on
  the probability of stopping by n₀. Upper bounds on the errors when the
  test is cut off at n₀ and decided by the sign of Z_{n₀}.
- **Optimality (§4.7).** Theorem: for any sequential test S of strength
  (α, β) that terminates with probability one,
  E₀(n|S) ≥ [(1 − α) log(β/(1 − α)) + α log((1 − β)/α)]/E₀(z) (4.80) and
  E₁(n|S) ≥ [β log(β/(1 − α)) + (1 − β) log((1 − β)/α)]/E₁(z) (4.81). The
  SPRT attains both when the excess is zero, so it is then "exactly an
  optimum test", and otherwise "very nearly" one (p. 157). Footnote 12:
  "The author conjectures that the sequential probability ratio test is
  exactly an optimum test even if the excess of Z_n over the boundaries is
  not zero. However, he did not succeed in proving this."
- **Part II.** For one-sided alternatives, test θ₀ against a chosen θ₁ and
  rely on a monotone operating characteristic (§5.1). The binomial plan
  has acceptance and rejection numbers linear in m (5.9)–(5.10). Double
  dichotomies are tested exactly through the unlike pairs (0, 1) and
  (1, 0), whose conditional law depends only on the odds ratio u (5.17)–
  (5.24), and the test stays valid when success rates drift from trial to
  trial alike in both series. The normal mean with known σ has
  h = (θ₁ + θ₀ − 2θ)/(θ₁ − θ₀) (5.37). §6 replaces the alternative by a
  weight-function mixture (6.1), so the SPRT bounds a weighted average of
  the second-kind errors (6.5). With spherical weights it gives a test on
  Σx̄ⱼ² (6.10)–(6.14), and for a normal mean with unknown variance a ratio that is
  homogeneous of degree zero in the observations, so free of scale
  (6.22)–(6.26). "There are several unsolved problems in this case"
  (p. 119).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The SPRT stops with probability one | strong | cited from Wald 1944, Lemma 1 |
| C2 | α/(1 − β) ≤ 1/A and β/(1 − α) ≤ B for any terminating SPRT, independence not required | strong | (3.12)–(3.19), a two-line proof; re-derived in THEORY-tmpeglfj |
| C3 | Boundaries (1 − β)/α and β/(1 − α) give α′ + β′ ≤ α + β, and neither error can rise much | strong for the sum and for α′ ≤ α/(1 − β); "for all practical purposes" for the rest | (3.26)–(3.30); re-derived and simulated |
| C4 | Neglecting the excess, P(accept H₀) = (A^h − 1)/(A^h − B^h) and En = [(1 − γ) log B + γ log A]/Ez | strong as approximations; exact without excess | (3.32)–(3.35), (4.4)–(4.8), from Wald 1944; re-derived in THEORY-tmpda363 |
| C5 | No sequential test of the same strength has smaller E₀(n) or E₁(n) than (4.80)–(4.81), and the SPRT attains them without excess | strong | §4.7 theorem, proved here; re-derived |
| C6 | The SPRT is exactly optimal even with excess | weak (conjecture) | footnote 12 |
| C7 | For a normal mean it saves 47–63% of observations for α, β in .01–.05 | strong within the approximation | Table 1, from (4.30)–(4.34); reproduced |
| C8 | The procedure extends to one-sided and composite hypotheses through monotone OC curves and weight functions | moderate | Part II; the minimax choice of weights is left as a calculus-of-variations problem |

## Concepts

- **Sequential test**: a partition of each m-dimensional sample space into
  accept-H₀, accept-H₁ and continue regions R⁰ₘ, R¹ₘ, Rₘ (§2.1).
- **Strength (α, β)**: the two error probabilities. Tests of equal
  strength are compared by E₀(n) and E₁(n).
- **Optimum test**: admissible, and minimizing max[E₀(n), E₁(n)] among
  tests of equal strength (§2.2). Efficiency is the ratio to that minimum.
- **Cylindric point of type i**: a finite sample path on which the test
  first accepts Hᵢ (§3.2).
- **Operating characteristic** L: the probability of accepting H₀ as a
  function of the true distribution (§§3.4, 5.2.4).
- **Current test procedure**: the fixed-sample most powerful test.

## Connections

Its predecessors, by the Historical Note, are Dodge and Romig's double
sampling (1929), Bartky's multiple sampling for a binomial mean (1943) and
Hotelling's chain experiments. Friedman and Wallis posed the problem in
March 1943, and Wald devised the test in April 1943. Barnard found a
sequential test of double dichotomies independently, and it "differs from
the one obtained by applying the sequential probability ratio test"
(p. 121). The test was first issued in a restricted report (September
1943), and the OC and sample-size theory rest on Wald's "On cumulative
sums of random variables" (1944). In the record, Bogacz et al. (LIT-569,
NOTE-461) restate it as the test "of Barnard and Wald" that is fastest
for a given error rate, with the drift-diffusion model as its continuum
limit, and THEORY-068 reads that limit.

## Bearing on the record

- **THEORY-tmpeglfj** (the boundaries and error inequalities) and
  **THEORY-tmpda363** (OC, sample size and optimality, and their
  coincidence with Brownian motion with drift) are filed from this
  reading.
- **THEORY-068 and LIT-569.** "Fastest for a given error rate" is, in this
  paper, a theorem only up to the overshoot (§4.7), with exact optimality a
  conjecture (footnote 12). The record's statement through LIT-569 should
  be read that way. The continuum limit is not in Wald. What is in Wald is
  that the error bounds become equalities "if fractional observations were
  possible" (p. 132), and that the overshoot-free OC, sample size and
  sample-size density, (3.35), (4.8) and (4.51), are exactly those of
  Brownian motion with drift (re-derived in THEORY-tmpda363). That is the
  sense in which the drift-diffusion model is the SPRT's continuum limit.
- **CASE-155**, note of 2026-10-25, and **CLAIM-tmpfd9lk.** "Wald's
  sequential probability ratio walk" holds as Wald defines it, with two
  provisos. (1) The walk Z_m = Σ log f₁/f₀ is the SPRT's statistic. The SPRT
  is the walk with fixed boundaries, so the identification needs
  commitment as a bound on the log odds, which CLAIM-tmpfd9lk already
  states as a condition. (2) The case's log odds start at the prior odds,
  not at zero. Wald's §3.1 covers that exactly: the posterior log odds are
  log(g₁/g₀) + Z_m, and posterior thresholds are likelihood-ratio
  thresholds shifted by the prior. The case's "drift is half the variance"
  for Gaussian evidence is Wald's h = −1 under H₁ (p. 135). For normal z,
  h = −2Ez/σ_z² (4.39), so Ez = σ_z²/2.
- **CLAIM-262** (the owner's continuous statement) and CASE-tmpvmjgd
  need nothing from Wald beyond the DDM limit, which they take from
  THEORY-068.

The proposed edits to those entries are written for the consolidator,
not made here. No instruction for machine-learning practice, so nothing
for the anthology.

## Limitations

- **Optimality is proved only without overshoot.** It holds exactly when
  z takes only the values ±d and log A, log B are multiples of d, and
  approximately when f₁ is near f₀. The general case is conjectured
  (footnote 12).
- **The working formulas are approximations.** The OC and the sample size
  are exact only through the conditional expectations E*, E** and
  E*Z_n, E**Z_n, which need the overshoot distribution. Bounds are given,
  and for the normal case the paper's own bounds may be loose.
- **The truncation bounds are loose** by the author's own account: "It
  would be desirable to find closer limits" (p. 154).
- **Simple hypotheses.** Composite problems are reduced to simple ones
  with a choice of θ₁ or of weight functions. The minimax choice of
  weights is left open except in symmetric cases.
- **Key lemmas are elsewhere.** Termination, the fundamental identity and
  the bounds on E*, E** are cited from the 1944 cumulative-sums paper.

## Open questions

- Is the SPRT exactly optimal with overshoot? Footnote 12 conjectures so.
  It was later proved by Wald and Wolfowitz (1948), a work the record does
  not hold.
- How should weight functions be chosen for composite alternatives in
  general (§6)?
- Tighter bounds on the errors of the truncated test (§4.6).
