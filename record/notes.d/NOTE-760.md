---
number: 760
status: Read
formerly:
- NOTE-tmp582tx
paper: LIT-238
title: 'Grünwald & Roos — Minimum Description Length Revisited'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv v2 PDF (arxiv.org/pdf/1908.08484v2,
    37 pp., 18 Dec 2019), text extracted with pdftotext: §§1–7 and
    Appendix A, every displayed equation and example. The reference list
    was used only to identify works cited. A review: almost every result
    is stated with a citation and no proof, and none of the cited proofs
    was checked here. The journal version (Int. J. Math. Industry 11(1),
    2019) was not read. The skim note filed with the paper is NOTE-198.
date: '2026-10-14'
summary: >-
  A review of MDL since 2007. Each model is replaced by one universal
  distribution, chosen for small worst-case log-loss regret against the
  model's best fit. NML is the minimax choice, with complexity
  (k/2) log(n/2π) + log ∫ v√|I| + o(1). Estimation is penalised ML with a
  luckiness function v. The switch distribution nearly resolves AIC–BIC,
  the RIPr gives tests safe under optional continuation, and MDL and Bayes
  can be inconsistent under misspecification. Results are cited, not proved.
---
<!-- inactive-ok-file: THEORY-087 THEORY-080 CLAIM-188 THEORY-035 — Proposed or Rejected; entries this review bears on, open or retired -->

# NOTE-760: Grünwald & Roos — Minimum Description Length Revisited

## Contribution

A self-contained introduction to MDL written without coding theory, and
an update of Grünwald's 2007 book (G07). It takes in the decade's results,
and it reports, by number, which of G07's open problems they settled. The
new results it collects are:

- a general NML with a luckiness function v, and the MDL estimator as
  penalised maximum likelihood;
- an exact expansion of NML complexity for exponential families with
  nonuniform v (Suzuki & Yamanishi 2018);
- the switch distribution (van Erven et al.) and the RIPr for composite-
  null testing (Grünwald et al. 2019);
- convergence of general MDL estimators under a generalised complexity
  bound (Grünwald & Mehta 2019);
- the misspecification failure (Grünwald & van Ommen 2017).

It contains no new theorem of its own.

## Key insight

MDL does not ask which distribution in a model fits best. It asks which
single distribution p̄ stands in for the whole model, so that
Σ_{zⁿ} p̄(zⁿ) ≤ 1 rules out a good fit to every sample. The right p̄ is the
one whose fit tracks the best in-model fit in the worst case over data,
maxₚ̄ min_{zⁿ} p̄(zⁿ)/max_θ p_θ(zⁿ)v(θ). That is the NML distribution, and
its log-normaliser is the model's complexity. Bayes marginals, two-part
codes and prequential plug-in predictors are other choices of p̄, judged
by how close they come.

## Assumptions

- **Model classes.** Countable collections of parametric models
  M_γ = {p_θ : θ ∈ Θ_γ}, with ML estimators assumed to exist and be unique
  "purely for simplicity".
- **"Sufficiently regular".** The asymptotics (14)–(16) need exponential
  or curved exponential families, and data whose ML estimates stay in an
  INECCSI set: interior non-empty, closure a compact subset of the
  interior. For the prequential plug-in, (14) holds only in expectation
  under a distribution in the model.
- **Finiteness of complexity.** With v ≡ 1, NML exists iff the Shtarkov
  integral ∫ p_{θ̂(zⁿ)}(zⁿ) dzⁿ is finite. It is infinite for most models
  on unbounded outcome spaces, including the normal location family.
  Nonuniform v, or v set by m start-up points, is the remedy.
- **Frequentist results (§6).** These assume i.i.d. data from a
  distribution in one of the models, except where misspecification is the
  subject.

## Key results

All are cited by the review. None is proved in it.

- **NML (3)–(4), (13), (25).** p̄_nml,v(zⁿ) = max_θ p_θ(zⁿ)v(θ) / ∫ max_θ
  p_θ(zⁿ)v(θ) dzⁿ, defined iff comp(M; v) = log ∫ max_θ p_θ(zⁿ)v(θ) dzⁿ is
  finite. It uniquely solves max_p̄ min_{zⁿ} FR(p̄, zⁿ) (13). Equivalently,
  with v ≡ 1, it is the minimax-regret predictor (25), and comp(M; 1) is
  the minimax regret.
- **MDL estimator (5).** θ̂_v = argmax_θ p_θ(zⁿ)v(θ), a penalised ML
  estimator. It is MAP when v is a density.
- **BIC/MDL asymptotics (14).** −log p̄(zⁿ) ≤ −log p_{θ̂_ml}(zⁿ) +
  (k/2) log n + C for sufficiently regular data. It holds with equality up
  to a constant for NML, Bayes and two-part codes, and only in expectation
  for prequential plug-in.
- **Complexity expansion (15).** comp(M; v) = (k/2) log(n/2π) +
  log ∫ v(θ)√|I(θ)| dθ + o(1) for k-dimensional exponential families.
  This is Rissanen (1996) for v ≡ 1 on INECCSI sets, and Suzuki &
  Yamanishi (2018) in general.
- **Laplace for Bayes (16).** −log p̄_bayes = −log p_{θ̂_ml} +
  (k/2) log(n/2π) + ½ log |I(θ̂)| − log w(θ̂) + o(1). With the generalised
  Jeffreys prior w ∝ v√|I|, NML and Bayes become asymptotically
  indistinguishable.
- **Selection and estimation unified (17)–(18).** With v_full(γ, θ) =
  π′(γ)v_γ(θ) and π(γ) := π′(γ)/exp(comp(M_γ, v_γ)), the meta-NML over
  models selects the same γ as joint penalised ML over (γ, θ).
- **Two-part codes need no special status (§2.3).** By Grünwald & Mehta
  (2019), every consistency and rate result for two-part estimators holds
  for general θ̂_v. That refutes G07's Open Problem 13.
- **Switch distribution (§3.1).** −log p̄_switch(zⁿ) ≤ min_i
  {−log p̄₁(z_i…z_n | z^{i−1}) − log p̄₀(z^{i−1})} + 2 log n. With a clever
  π the overhead is O(log log n). The result is strongly consistent and
  prediction-optimal within an O(log log n) factor (van Erven et al. 2007,
  2012). Yang (2005) shows the dilemma cannot be solved exactly.
- **No hypercompression (27) and RIPr (28).** P₀(p₀(Zⁿ)/p̄₁(Zⁿ) ≤ α) ≤ α
  for any p̄₁. For composite nulls, the reverse information projection of
  p̄₁ onto the Bayes marginals of M₀ makes this hold for all θ ∈ Θ₀
  (Grünwald et al. 2019). The Bayesian t-test with right-Haar priors is an
  instance.
- **Horizon dependence (§3.2).** NML depends on n: for Bernoulli, the
  probability of 00 is 0.4 at n = 2 and about 0.397 at n = 3. It is
  horizon-free only in rare cases (Bartlett et al. 2013). In-model
  plug-in estimators need the correction (var_p Z / var_{p̃} Z)·½ log n
  under misspecification (26). No in-model estimator escapes it
  (Grünwald & Kotłowski 2010).
- **Multinomial NML regret (30).** The Szpankowski–Weinberger formula
  n log α + (α + 2) log C_α − 1/C_α − ½ log(C_α + 2/α), with α = n/r, for
  r = Θ(n).
- **WBIC (31).** −log p_{θ₀}(zⁿ) + λ log n + O_p(√log n) for singular
  models, with λ the real log canonical threshold (Watanabe 2013).
- **Consistency (§6.1).** θ̂_v is consistent if v(θ*) < ∞ and, for some
  η < 1, comp_η(M, v) of (32) is o(n). This is weaker than Barron–Cover.
  "Ironically", for η = 1 it does not suffice.
- **Misspecification (§6.3).** If no model contains the truth, MDL and
  Bayes can be inconsistent (Grünwald & Langford 2007). Even with finitely
  many models they can select arbitrarily bad ones for fairly large n
  (Grünwald & van Ommen 2017). The cause is that no-hypercompression (33)
  fails with p̃, the KL-closest model, in place of p₀. Tempering the
  likelihood, p^η with η < 1 (Safe Bayes), restores it.
- **PAC-MDL and deep learning (§6.4).** Flat minima need fewer bits
  (Hochreiter & Schmidhuber 1997; Hinton & van Camp 1993). PAC-Bayes bounds
  contain −log π(θ), or a KL term read as bits-back code length, and give
  nontrivial bounds for some networks (Dziugaite & Roy 2017; Zhou et al.
  2018).
- **Rademacher link (§7).** NML complexity is bounded by Rademacher
  complexity for p_θ ∝ exp(−η·loss_θ) with bounded loss (Grünwald & Mehta
  2019).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | NML is the unique worst-case-optimal universal distribution, and its complexity is the minimax regret | strong | eqs. (13), (25), standard results cited |
| C2 | For regular parametric models every standard universal code pays (k/2) log n + O(1) over the ML fit | strong | eqs. (14)–(16), cited (Rissanen; Suzuki & Yamanishi) |
| C3 | General penalised-ML (luckiness) estimators have a code-length reading and the same convergence guarantees as two-part estimators | moderate | Grünwald & Mehta (2019), cited |
| C4 | The switch distribution is consistent and prediction-optimal up to O(log log n) | moderate | van Erven et al., cited; the 2 log n bound derived in text |
| C5 | MDL and Bayes can be inconsistent when every model is wrong | moderate | Grünwald & Langford; Grünwald & van Ommen, cited |
| C6 | MDL "unifies" AIC vs BIC and CV vs Bayes | weak | "to a large extent" (abstract), "to some extent" (§1); the switch result is "almost", and Yang (2005) shows no exact resolution |
| C7 | PAC-Bayes bounds give an MDL-style account of why flat minima generalise | weak | a review paragraph (§6.4) citing others |

## Concepts

- **Universal distribution p̄_γ.** A single distribution standing for the
  model M_γ, whose code length tracks the best in-model fit. The six kinds
  are Bayes, NML, two-part, prequential plug-in, switch and RIPr.
- **Luckiness function v.** A nonnegative function on Θ, not necessarily
  integrable. It says for which data one will be "lucky" and get small
  regret early. Unlike a prior, it carries no belief that the model is true
  (§2.5).
- **comp(M; v).** The log-normaliser of luckiness-NML: model complexity
  and minimax luckiness regret.
- **Fitness ratio.** FR(p̄, zⁿ) = p̄(zⁿ)/max_θ p_θ(zⁿ)v(θ).
- **INECCSI.** Interior non-empty, closure a compact subset of the
  interior of Θ.
- **Improper (out-of-model) estimation.** Predicting with p̄(Z_i | z^{i−1}),
  which need not lie in M.

## Connections

The review puts "ideal", Kolmogorov-complexity MDL (Vitányi & Li,
[LIT-225](../literature.d/LIT-225.md)) out of scope and defers it to G07. Its only pointer to the
structure-function line of Vereshchagin & Vitányi ([LIT-239](../literature.d/LIT-239.md)) and
Grünwald & Vitányi ([LIT-224](../literature.d/LIT-224.md)) is §7's remark that Rissanen's later
programme "expands MDL and NML ideas in the direction of the Kolmogorov
structure function". It cites neither paper. The WBIC of (31) is Watanabe's
([LIT-616](../literature.d/LIT-616.md)). The Laplace expansion (16) is the one MacKay's Occam factor
([LIT-623](../literature.d/LIT-623.md)) and [THEORY-087](../theory.d/THEORY-087.md) use. The §6.4 PAC-Bayes link is the one Sefidgaran
et al. ([LIT-245](../literature.d/LIT-245.md)) make into a theorem for encoders.

## Bearing on the record

- **No THEORY, QUESTION or CLAIM cited this paper before today.** [LIT-623](../literature.d/LIT-623.md)
  named it as "the record's MDL holding" while it was unread.
- **[THEORY-087](../theory.d/THEORY-087.md) is supported on its regular half by a second source.**
  Eqs. (15)–(16) give the (k/2) log n penalty, with the Fisher-volume
  constant, for NML as well as Bayes. They also show that NML and Bayes
  under the generalised Jeffreys prior become asymptotically
  indistinguishable. So the penalty [THEORY-087](../theory.d/THEORY-087.md) derives from MacKay is the
  description-length penalty too. On the singular half, eq. (31) quotes
  WBIC's form, −log p_{θ₀} + λ log n + O_p(√log n). That is the same λ
  log n leading term, cited, not derived, and it adds nothing [THEORY-087](../theory.d/THEORY-087.md)
  lacks.
- **[CLAIM-154](../claims.d/CLAIM-154.md) and [CLAIM-188](../claims.d/CLAIM-188.md).** §6.3 bears on any Bayes-factor threshold
  used to name structure. When every candidate model is misspecified,
  which a block or coupling model of a real system is, Bayes and MDL can
  prefer the wrong model for large n. The remedy (Safe Bayes, η < 1)
  changes the effective Occam cost. [CLAIM-188](../claims.d/CLAIM-188.md) objects to [CLAIM-154](../claims.d/CLAIM-154.md) on
  singularity. Misspecification is a second, independent ground for the
  same caution, and the record does not yet hold it. This is recorded here
  rather than filed: the review cites the result and does not prove it.
- **[QUESTION-040](../questions.d/QUESTION-040.md) (what an Occam term should count).** comp(M; v) is
  a candidate answer: the log of the number of distinguishable
  distributions, (k/2) log(n/2π) + log ∫ √|I|. Like [THEORY-080](../theory.d/THEORY-080.md)'s spectral
  count, it weights directions by Fisher information rather than counting
  parameters. The review notes (Roos 2008; Zou & Roos 2017) that models
  with equal parameter counts differ in this term. It does not address the
  selection-bias half of [QUESTION-040](../questions.d/QUESTION-040.md).
- **[THEORY-035](../theory.d/THEORY-035.md) (Rejected).** §6.4's flat-minima-as-short-codes is a
  different compression from [THEORY-035](../theory.d/THEORY-035.md)'s I(X;T). The review neither
  supports nor bears on the rejected account.
- **The LIT's summary says a little too much.** "Unifies methods usually
  seen as rival … within one worst-case framework" drops the paper's own
  hedges, "to a large extent" and "to some extent". The switch distribution
  only "almost" solves the AIC–BIC dilemma, and Yang (2005), whom the
  review cites, shows no consistent method is always prediction-optimal.
  The LIT is corrected.
- **Machine-learning practice.** The variable-selection example
  (Example 4) and the remark that Lasso is luckiness-MDL are statistical
  method, not training advice. §6.4 reports a generalisation account, not
  an instruction. Nothing here for the anthology.

## Limitations

- **A review.** Each result's conditions are those of the cited paper,
  which this reading did not check. Where the review states a condition
  ("sufficiently regular", "under very mild conditions"), it often defers
  the precise form to G07.
- **Regular parametric models dominate.** Irregular and latent-variable
  models get one section (§5), and WBIC is quoted, not related to NML.
- **Little on Kolmogorov-complexity MDL.** It is set aside deliberately,
  so the review says nothing about the individual-data guarantees of
  [LIT-239](../literature.d/LIT-239.md).
- **Deep learning (§6.4)** is one page and calls itself one of "several
  explanations (which presumably all form a piece of the puzzle)".

## Open questions

- Does the NML complexity of a singular model have an expansion with λ in
  place of k/2, as WBIC has for the Bayes marginal? The review gives (15)
  for exponential families only.
- Under misspecification, is there a principled η for NML, as Safe Bayes
  gives for Bayes? §6.3 says Grünwald & Mehta "suggests" so.
- The review says it remains open to bound the prediction error at an
  individual t, as opposed to cumulatively (§6).
