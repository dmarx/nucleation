---
number: 508
status: Read
formerly:
- NOTE-tmpso23o
paper: 'LIT-610'
title: 'The Weighted Likelihood Ratio, Linear Hypotheses on Normal Location Parameters'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full from a JSTOR scan the owner supplied (20 pages, printed
    pp. 204–223; the first image is p. 204 with JSTOR's footer, not a
    separate cover sheet). The text came from OCR, and every equation
    quoted here was checked against the 300 dpi page images: (2.3)–(2.6),
    (3.1)–(3.9), (3.9*), (4.6)–(4.9), (4.19), (4.22), (5.24)–(5.28),
    (5.42) and (5.45), and the two sentences applying (3.8) in §4.1.2 and
    §5.1.2. Section 2's decision theory, §4.2 and §5.1.3–5.2 (the
    Behrens–Fisher cases) were read for what they claim, not re-derived.
    The references were checked for the Dickey & Lientz entry.
date: '2026-10-03'
summary: >-
  States the Savage–Dickey ratio in general, not only for normal models:
  for a sharp hypothesis η(θ) = η_H with positive prior mass, the Bayes
  factor L_D(H) equals the alternative's posterior density of η at η_H
  over its prior density there (3.9), provided the null's nuisance prior
  is the alternative's conditional prior at η_H (3.8). Dickey calls it
  Savage's density ratio and credits the proof to Dickey & Lientz. He
  then applies it to normal means, the Model-I F test and the univariate
  and multivariate Behrens–Fisher problems with conjugate priors.
---

# NOTE-508: The Weighted Likelihood Ratio, Linear Hypotheses on Normal Location Parameters

## Contribution

The paper states, as a theorem in a general setting (§3), that the Bayes
factor for a sharp hypothesis equals a ratio of posterior to prior density
at the hypothesised value, and says exactly which prior condition makes
that hold without approximation. It then uses Raiffa and Schlaifer's
conjugate families to give the Bayes factor in closed form for a normal
mean (§4.1), for a linear hypothesis in the linear normal model, as a
Bayesian replacement for the F test (§5.1), and for the univariate and
multivariate Behrens–Fisher problems (§4.2, §5.2). It also adds a new
conjugate family for normal sampling in which the mean and variance can be
independent a priori (4.23), and restates the whole theory for a general
utility, as a "weighted utility-likelihood ratio" (§2, (3.9*)).

## Key insight

If the prior under the null is what the alternative's prior says once the
tested parameter is set to its null value, then the null model needs no
separate integral. Its marginal likelihood is a slice of the alternative's,
and dividing the two leaves only how the data moved the density of the
tested parameter at the null value. Then a conjugate prior makes the Bayes
factor a ratio of two ordinates of the same family, prior and posterior.

## Assumptions

- **Setting (§2).** Data D ∈ Rⁿ with density φ(D | θ) "depending
  continuously" on θ ∈ R^r. H is a Borel set with 0 < P(H) < 1, and
  0 < P(H | D) < 1 too. The same likelihood φ serves both hypotheses in
  (2.5) and (2.6).
- **Sharp hypothesis (§3, (3.1)).** A smooth reparameterisation ξ(θ) =
  (η′, ζ′)′ with nonzero Jacobian, η ∈ R^q, ζ ∈ R^(r−q), and H: η(θ) = η_H
  against H̄: η(θ) ≠ η_H. So η may be a vector, and H is any analytic
  surface segment, not only a linear one. Linear manifolds are the
  normal-theory cases of §§4–5.
- **Mixture prior (3.2).** P(S) = P(H̄)∫∫ f(η, ζ) dζ dη + P(H)∫ g(ζ) dζ,
  over S∩Ξ and S∩H∩Ξ. Against a dominating measure with an extra unit mass
  at η = η_H, the prior density is (3.5): P′(ξ) = P(H̄) f(ξ)[1 − δ(η − η_H)]
  + P(H) g(ζ) δ(η − η_H), with δ(0) = 1 and δ = 0 elsewhere. That is a point
  mass on the null inside a continuous prior.
- **Densities as elementary derivatives (3.3)–(3.4).** f(ξ) is the limit,
  as the radius ρ → 0, of the ball probability P[S_ρ(ξ) | H̄] over the ball's
  Lebesgue measure, and it is "assumed uniquely defined throughout Ξ".
  Hence f is defined on H, where H̄ has no mass, and "not necessarily zero"
  there. This is what lets f(η_H, ζ) appear in the theorem.
- **The theorem's condition (3.8).** g(ζ) = f(η_H, ζ) / ∫ f(η_H, ζ) dζ:
  the null's prior on the nuisance parameters is the alternative's prior
  conditioned at η_H. In the applications Dickey states it as a limit:
  "assume that σ² | H is distributed identically to the limiting
  distribution of σ² | μ, H̄" (§4.1.2), and "β, σ² | H is distributed as
  the limiting distribution of β, σ² | H̄, from (5.29) given C_Hβ = η_H"
  (§5.1.2).
- **Positive mass on a sharp hypothesis** is "proposed as a good
  approximation to many prior opinions" (§3), not argued further.

## Key results

- **Odds (2.3)–(2.6).** O(H | D) = L_D(H)·O(H), with the weighted
  likelihood ratio L_D(H) = Φ(D | H)/Φ(D | H̄) and Φ(D | H) = ∫ φ(D | θ)
  dP(θ | H), likewise for H̄. L_D(H) is the Bayes factor for the null
  (BF01 in later notation).
- **Theorem (Savage's Density Ratio), (3.8)–(3.9).** If (3.8) holds, then
  L_D(H) = P′(η_H | H̄, D)/P′(η_H | H̄), where P′(η | H̄) = ∫ f(η, ζ) dζ and
  P′(η | H̄, D) = ∫ φ(D | η, ζ) f(η, ζ) dζ / Φ(D | H̄). The proof is one
  line: substitute (3.8) for g in (3.6). Dickey credits the proof to
  Dickey and Lientz, and the unpublished discovery of the exact general
  formula to Savage (1963). Approximate special forms are credited to
  Jeffreys (1948), Lindley (1961) and Savage (1959, 1961).
- **Stable estimation (§3, p. 209).** With a locally uniform prior f ≡ c
  the numerator becomes the normalised likelihood integrated at η_H, so
  L_D(H) ≐ ∫ ψ_D(η_H, ζ) dζ / P′(η_H | H̄): data in the numerator, one
  subjective number in the denominator. A better approximation evaluates
  the prior at the maximum-likelihood values instead.
- **Utility version (3.9*).** If U(d*(θ), θ)·φ(D | θ) is continuous in η
  at η_H, the weighted utility-likelihood ratio has the same
  posterior-over-prior form, and a removable discontinuity of U at η_H is
  handled by the rescaling (3.10)–(3.12).
- **Normal mean, σ² known (4.6)–(4.7).** With μ | σ², H̄ ~ N(x̄0, σ²/n0),
  L_D(H) = (n1/n0)^½ exp(½σ⁻²Q), Q = n0(x̄0 − μ_H)² − n1(x̄1 − μ_H)² =
  n0 n1⁻¹ n(x̄0 − x̄)² − n(x̄ − μ_H)². As n0 → 0, prior "ignorance" under
  the alternative, L_D(H) → ∞ (citing Cornfield 1966). The stable
  estimation form (4.9) divides the normal density of x̄ at μ_H by the
  prior density P′(μ | H̄) at μ = x̄.
- **Normal mean, σ² unknown (4.19).** Under the Normal-gamma prior,
  L_D(H) = P1′(μ_H)/P0′(μ_H), a ratio of posterior to prior Student-t
  ordinates at μ_H.
- **Linear hypothesis in the linear normal model (5.24)–(5.25), σ²
  known.** For H: C_Hβ = η_H, L_D(H) = (|C_H N0⁻¹ C_H′| / |C_H N1⁻¹
  C_H′|)^½ exp(½σ⁻²Q) with Q = SSB0 − SSB1, the analysis-of-variance
  "sum of squares between" computed with prior and posterior means and
  information matrices. Dickey says this corrects and generalises
  Edwards, Lindman & Savage (1963), Eq. [22], p. 233.
- **σ² unknown (5.42), (5.45).** The ordinates are multivariate t, and in
  the stable-estimation limit the Bayes factor is an F-density ordinate at
  the observed (SSB/q)/(SSW/ν) over a prior density. Dickey adds: "The
  author has vague memories of verbal statements by Leonard J. Savage, at
  least as early as 1965, that ordinates of F densities are more important
  than tail areas."
- **Independence prior (4.23), (5.46)–(5.51).** A product of a normal
  density in μ and a Normal-gamma, which with n0 = 0 makes μ and σ²
  independent a priori. Its Bayes factor involves Behrens–Fisher densities
  (4.30)–(4.31). In the multivariate case it needs numerical integration,
  four of them by Dickey's count.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | For a sharp hypothesis with positive prior mass, under (3.8), the Bayes factor is the alternative's posterior-to-prior density ratio of η at η_H | strong (derivation, any likelihood) | §3, Theorem, (3.8)–(3.9) |
| C2 | The condition is that the null's nuisance prior equal the alternative's conditional prior at η_H, with densities fixed as elementary derivatives | strong (it is the theorem's hypothesis) | (3.3), (3.4), (3.8) |
| C3 | Conjugate priors under the alternative give closed-form Bayes factors for normal means and linear hypotheses | strong (derivation) | (4.6), (4.19), (5.24), (5.42) |
| C4 | A vague alternative prior drives the Bayes factor towards the null without bound | strong for the known-variance normal case | §4.1.1, n0 → 0 |
| C5 | Stable estimation gives a one-ordinate approximation that should not be used for a formal decision without checking it | the approximation is derived; the caution is the author's judgement | §1, §3, (4.9), (4.22), (5.27), (5.45) |
| C6 | Tail-area and likelihood-ratio tests for composite hypotheses are "an irresponsible escape" from prior opinion | polemic, not argued in the paper | §1 |
| C7 | L_D(H) is invariant to the choice of η and ζ if the new parameters carry the induced distribution | cited, not shown here | §3, citing Dickey & Lientz (1969) |

## Concepts

- **weighted likelihood ratio**: L_D(H) of (2.4), the likelihood averaged
  over the prior under H divided by the same under H̄. Now called the
  Bayes factor.
- **sharp hypothesis**: a set of prior positive probability that is a
  lower-dimensional analytic surface in parameter space (§3).
- **Savage's density ratio**: Dickey's name for (3.9). The name
  "Savage–Dickey" is not used in the paper.
- **elementary derivative**: a density defined as the limiting ratio of
  probability to Lebesgue measure on shrinking balls (3.3), which makes
  its value on a null set meaningful.
- **stable estimation / precise measurement**: Savage's approximation that
  treats a prior that is roughly flat where the likelihood is concentrated
  as exactly flat.
- **weighted utility-likelihood ratio**: L_{U*,D}(H) of (2.14), the
  utility treated as the likelihood of a hypothetical second experiment.

## Connections

- **Wagenmakers et al. ([LIT-609](../literature.d/LIT-609.md), read in [NOTE-484](NOTE-484.md))** take the ratio from
  Dickey & Lientz and this paper. Their condition, that the nuisance prior
  under the alternative tends to the nuisance prior under the null as
  φ → φ0, is Dickey's (3.8) in the limit form he himself uses in §4.1.2
  and §5.1.2. Their Appendix A derivation is Dickey's one-line proof
  written out with Bayes' rule.
- **Friston & Penny ([LIT-620](../literature.d/LIT-620.md), read in [NOTE-487](NOTE-487.md))** recover the ratio as the
  point-mass case of their reduced-prior identity (their Eq. 6) and cite
  this paper for it. Dickey's mixture prior (3.5), a point mass at η_H
  inside a continuous f, is exactly the reduced prior of that case, and
  his g is the reduced model's prior on the remaining parameters.
- **Bayesian model reduction ([LIT-614](../literature.d/LIT-614.md))** calls itself a generalisation of
  the Savage–Dickey ratio "to any new prior". Dickey's theorem is already
  general in the likelihood and in the dimension of η. What BMR
  generalises is the reduced prior, from a point mass to any narrower
  prior.
- **Dickey & Lientz** is the paper the proof is credited to, and the
  record does not hold it.

## Bearing on the record

- **[THEORY-081](../theory.d/THEORY-081.md).** Its point-mass clause is Dickey's theorem. The reduced
  prior δ(φ − φ0) p_F(ψ | φ0) is (3.5) with g given by (3.8), and the
  conclusion is (3.9). Dickey states it for any likelihood continuous in
  θ and any smooth sharp hypothesis, so the clause now has its original
  source, not only the restatements in [LIT-609](../literature.d/LIT-609.md) and [LIT-620](../literature.d/LIT-620.md).
- **[LIT-609](../literature.d/LIT-609.md) and [LIT-620](../literature.d/LIT-620.md)** describe what Dickey shows accurately in
  substance, and Wagenmakers et al.'s source chain (Savage, then Dickey &
  Lientz) is Dickey's own. [LIT-620](../literature.d/LIT-620.md) read the two papers' conditions as
  alternatives, Wagenmakers's continuity against its own shared
  likelihood and nested priors. Dickey's theorem uses both, a shared φ in
  (2.5)–(2.6) and the conditional-prior requirement (3.8), and [LIT-620](../literature.d/LIT-620.md) now
  says so.
- **No ML instruction.** Nothing here belongs in the anthology.

## Limitations

- **No data.** Every result is analytic. There is no worked numerical
  example, and the Behrens–Fisher densities the independence prior needs
  are only referred to other papers for computation.
- **Coordinates.** The elementary derivatives in (3.3)–(3.4) are taken
  with respect to Lebesgue measure in the chosen coordinates ξ = (η, ζ),
  so the conditional at η_H, and with it (3.8), depends on how H is
  parameterised. Dickey cites an invariance result for the induced
  distribution and does not discuss the case where (3.8) is imposed anew
  in another parameterisation, the Borel–Kolmogorov issue that [LIT-609](../literature.d/LIT-609.md)
  raises.
- **Priors.** Dickey calls the Normal-gamma's prior dependence of μ and σ²
  "usually ridiculous" (§4.1.3), but §4.2 uses it anyway and hopes "future
  work will exploit the more realistic prior distributions of Section
  4.1.3".
- **Stable estimation** "should not form the basis of a formal decision
  procedure without an evaluation of the quality of the approximation"
  (§1), and "is unlikely to yield a realistic approximate posterior
  distribution for a large number of unknown parameters" (§3).

## Open questions

- What does (3.8) become when the conditioning is done in a different
  parameterisation of the same H, and how far apart are the two Bayes
  factors in practice? Dickey & Lientz's invariance result is cited for
  the induced case and not reproduced.
- How should the bounds on the conjugate parameters be assessed for the
  "robust inference throughout the bounded region" that §1 calls the
  unavoidable task? The paper names the task and does not do it.

## Corrections

- **The record's earlier description ([LIT-610](../literature.d/LIT-610.md), version 1)** left open
  whether Dickey stated the result for general nested models or only for
  normal linear hypotheses. It is general: §3 states it for any
  likelihood φ(D | θ) continuous in θ and any sharp hypothesis η(θ) = η_H
  under a smooth reparameterisation. Normal linear hypotheses are the
  applications, as the title says.
- **The record's earlier description** called this "the paper the
  Savage–Dickey density ratio is named after". It is one of the papers the
  name comes from, but Dickey calls the result "Savage's Density Ratio",
  credits its discovery to Savage's unpublished 1963 notes and its proof
  to Dickey and Lientz, and does not claim it as his own.
- **The paper's own citation of Dickey & Lientz.** The text dates it 1968,
  in §1 and in the proof of the theorem, and the reference list gives
  "(1968)" but places it in *Ann. Math. Statist.* 41, 214–226. This paper
  is volume 42 of 1971, so volume 41 is the 1970 volume, the year
  Wagenmakers et al. give ([LIT-609](../literature.d/LIT-609.md)). The 1968 is presumably a preprint
  date; the paper does not say. A second citation, "Dickey and Lientz
  (1969)" for the invariance result (§3, p. 209), has no entry in the
  reference list.
