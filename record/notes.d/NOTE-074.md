---
number: 74
status: Read
formerly:
- NOTE-tmpskbvw
paper: LIT-044
title: 'The epic story of maximum likelihood'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (full text of arXiv 0804.2996v1 (18 Apr 2008), the IMS
    electronic reprint of Statistical Science 22(4), 598–620 (2007), 24 pp.
    Covered §§1–14, Figs. 1–2 (Fig. 1 is a text box; for Fig. 2 I read the
    caption and Hotelling's description), Appendices 1–3 (Fisher's 1928
    draft contents, Fisher's Enclosure A of 28 Nov 1930, and Hotelling's
    "Spaces of statistical parameters"), acknowledgements and the full
    reference list. Nothing skipped. PDF from arxiv.org/pdf/0804.2996,
    extracted with PyMuPDF to raw4/0804.2996.txt. The reprint notes that it
    "differs from the original in pagination and typographic detail", so
    section references below are safer than page numbers. I checked the
    Appendix 2 Lagrangian argument and the Hodges variances in Fig. 1 by
    hand. I did not consult the archival letters or Fisher's papers
    directly; everything about them is Stigler's account.). Upgraded from
    `Skimmed` to `Read`: the claims table, assumptions and results are new,
    and the skim is corrected where the full text disagreed.
date: '2026-09-25'
summary: >-
  Stigler gives a history of maximum likelihood from Lagrange (1769) to Le
  Cam (1953). Fisher gave three optimality arguments. The 1922 one rests
  on the false belief that ML estimates are always sufficient. The 1925
  "ANOVA" one derives the information inequality V ≥ 1/I(θ) from Var X = E
  Var(X|T) + Var E(X|T), treating approximate normality as exact. The
  third, sent privately to Hotelling in 1930, holds for multinomial models
  and smooth degree-0-homogeneous estimators, and was published only in
  disguise in 1935. Stigler's verdict is that the Neyman–Scott
  growing-parameter example (Wald 1938, published 1948) is the practically
  important failure. He calls Hodges's 1951 superefficiency example "an
  ingenious but minor technical achievement", because the superefficiency
  set has Lebesgue measure zero (Le Cam 1953).
---

# NOTE-074: The epic story of maximum likelihood

## Contribution

Using Fisher's and Hotelling's correspondence and Neyman's papers, Stigler reconstructs the logical content of each historical justification of maximum likelihood, and what each silently assumed. The article adds three things not previously in print:

- Fisher's third, geometric proof (Enclosure A, 1930), with its restriction to degree-0-homogeneous, smooth estimators of multinomial parameters.
- The analysis of the 1925 information-inequality proof as a probabilistic analysis-of-variance decomposition.
- Hotelling's 1930 letters hinting at superefficiency two decades before Hodges, and Wald's 1938 letter to Neyman giving the first explicit inconsistent-ML example.

It also judges the Edgeworth priority dispute: Edgeworth was "an independent partial anticipation — a hint, not an instance".

## Key insight

"ML is optimal" was never one theorem. It was a sequence of arguments, each true under conditions its author either knew and left implicit or did not see:

- sufficiency (1922);
- a score linearly approximable by the MLE, plus exact normality (1925);
- multinomial data and smooth homogeneous estimators (1930).

The later counterexamples each break one of these: superefficiency on null sets, parameter counts growing with n, unbounded likelihoods. The ones that matter in practice are those where information per parameter does not grow.

## Assumptions

Premises and sources for the historical claims:

- **Archives:** the Fisher Papers (Adelaide), the Hotelling Papers (Columbia; Boxes 3, 44, 45) and the Neyman Papers (Bancroft; Box 14, Folder 28).
- **Published secondary accounts relied on:** Hald (1998, 2007), Savage (1976), Pratt (1976), Hinkley (1980), Aldrich (1997), Edwards (1974, 1997a), and Stigler's own earlier work (1986, 1999, 2005, 2007).
- **The mathematical reconstructions are Stigler's**, stated as such:
  - the §5 argument is "by my reconstruction";
  - the Cauchy-location origin of Fisher's recognition that sufficient statistics need not exist is "I speculate" (§6);
  - the route to the ANOVA proof is "what I believe to be the logical development Fisher had in mind" (§7).

For the proofs as reconstructed:

- **1922:** S and T are treated as exactly bivariate normal with mean θ; T is sufficient.
- **1925:** T ~ N(θ, V) exactly; V does not depend on θ; the likelihood is regular enough to differentiate under the integral; X = −nA(θ − θ̂) to order n^{−1/2}.
- **1930:** a multinomial model; T = φ(x₁, …, x_s) homogeneous of degree 0 and smoothly differentiable; no bias of order n^{−1/2}.

## Key results

What the article establishes:

- **Pre-Fisher (§2):**
  - Lagrange (1769/1776) maximised a multinomial likelihood before imposing the error curve, and so always arrived at method-of-moments estimates.
  - Daniel Bernoulli moved from iterative reweighting (1769, M-estimator-like) to product-of-densities maximisation (1778).
  - Gauss (1809) took the posterior mode under a uniform prior, which gives least squares.
- **Pearson & Filon (1898) (§3):** a Taylor expansion of a log-likelihood ratio, valid at most for ML estimates, applied "heedlessly" to moment estimates. It gave wrong standard errors, which Fisher (1922) publicly corrected.
- **First proof (1922, §5):** if T is sufficient and (S, T) are bivariate normal with common mean θ, then E(S|T) = θ + ρ(σ_S/σ_T)(t − θ) cannot depend on θ. So ρσ_S = σ_T ≤ σ_S. Hence "sufficiency implies optimality", given consistency and asymptotic normality. The 1921 abstract's claim that ML statistics "are always sufficient statistics" was dropped from the published paper. Fisher (1922, p. 323) says he was "not satisfied as to the mathematical rigour of any proof".
- **Second proof (1925 ANOVA, §7):** Var X = E[Var(X|T)] + Var[E(X|T)], with E[Var(X|T)] = Var X − 1/V ≥ 0. This gives V ≥ 1/I(θ), the information inequality. The residual E[Var(X|T)] is the information lost by T. Ancillary statistics enter as covariates, and the loss for efficient non-ML estimates tends to a finite limit, which Rao later called second-order efficiency.
- **Third proof (1930, §10, Appendix 2):** for a degree-0-homogeneous φ, Euler's relation gives Σ x ∂φ/∂x = 0. Minimising the multinomial asymptotic variance subject to consistency (Σ ∂φ/∂x · ∂f/∂θ = 1) by Lagrange multipliers gives ∂φ/∂x ∝ (1/f)(∂f/∂θ), the ML estimating equation. Fisher's summary: consistent, efficient statistics have equistatistical surfaces tangent along the expectation line, and ML's surface is the plane one. Stigler judges it "elegant, geometric, and I believe also correct, or at least completable", and "immune" to the Hotelling/Hodges facts, at a cost in generality (§11).
- **Hotelling (1930, §8–9):** his consistency and asymptotic-normality proof fails outside discrete, bounded-parameter cases. His 15 Nov and 12 Dec 1930 letters argue that consistency alone cannot secure minimum variance: stretching the projection along the curve beats ML near "regions of condensation". This anticipates superefficiency, though it is "vague".
- **Rigour (§11):** Doob (1934, 1936) and Dugué (1937) erred. Wald (1943, 1949) and Cramér (1946) gave the first satisfactory treatments, at the cost of unwieldy conditions. Wald (1943) excluded even the normal standard deviation.
- **Counterexamples (§12):**
  - Wald's 1938 letter: an errors-in-variables line, where ML is inconsistent. This became the Neyman–Scott example X_ij ~ N(µ_j, σ²), i = 1, 2, whose MLE of σ² converges to σ²/2.
  - Hodges: T_n = X̄_n if |X̄_n| ≥ n^{−1/4}, else αX̄_n. Its asymptotic variance is α² at θ = 0 and 1 elsewhere (Fig. 1). Le Cam (1953) showed the superefficiency set has Lebesgue measure zero.
  - The normal-mixture likelihood is unbounded.
  - Bahadur (1964) gave a clean one-dimensional theorem, restricted to asymptotically normal estimators with variance continuous in θ.
- **Priority (§11):** Edgeworth (1908–09) proved, via Schwarz's inequality, that ML is minimum-variance within location M-estimators. This had no influence on Fisher, and Neyman's 1951 charge of "an unjustified claim of priority" has "no merit".
- **Hotelling's parameter spaces (Appendix 3):** the Fisher-information metric g_αβ as a Riemannian metric (1929). The normal and gamma location-scale families are pseudospheres of constant negative curvature. This predates Jeffreys (1946) and Rao's information geometry.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Fisher's 1922 proof depended on the false belief that ML estimates are always sufficient | strong | the 1921 Nature abstract quoted against the 1922 text; Fisher's 1935 retrospective quoted |
| C2 | The 1925 information-inequality proof is an ANOVA decomposition of the score's variance | moderate | Stigler's reconstruction of Fisher (1925, 1935) and Hinkley (1980); the algebra is correct |
| C3 | Fisher gave a third, correct-or-completable proof privately to Hotelling in 1930 | strong | Enclosure A reproduced in full (Appendix 2); the argument checks by Lagrange multipliers |
| C4 | Hotelling's 1930 consistency proof is wrong in the generality claimed | moderate | Stigler's diagnosis (§8) plus Hotelling's own 1931 problem [#16](https://github.com/dmarx/nucleation/issues/16) |
| C5 | Hotelling foresaw superefficiency in 1930 correspondence | moderate | the letters are quoted; Stigler himself calls the proposals "vague" and says they "fall short" of Hodges or Stein |
| C6 | The first explicit inconsistent-ML example is Wald's, in a 1938 letter to Neyman | moderate | letter quoted; "perhaps" hedged ("The earliest explicit example is perhaps due to Abraham Wald") |
| C7 | Neyman's 1951 priority charge for Edgeworth has no merit | moderate | Stigler's reading, agreeing with Savage (1976) and Pratt (1976); Fisher's own letters quoted |
| C8 | Hodges's example is today a minor technical point, and the growing-parameter problem is the practical one | moderate | expert judgement, supported by Le Cam's (1953) measure-zero theorem |
| C9 | Fisher's proofs are all defensible given their implicit conditions | weak | explicitly "flirts with tautology" (§14); rests on the assertion that Fisher knew his conditions |
| C10 | The Fisher–Neyman feud brought ML's limitations into public view | weak | interpretive argument (§14) |
| C11 | ML's useful scope may exceed any achievable proof | weak | hedged ("Perhaps"), an assertion (§14) |

## Concepts

- **Superefficiency** — an estimator whose asymptotic variance is below 1/I(θ) at some θ. Hodges's T_n does this at θ = 0.
- **Consistency (Fisher versus Hotelling)** — for Fisher, a statistic is inconsistent only if it tends to the *wrong* limit. For Hotelling, one with no limit, such as the Cauchy sample mean, is also inconsistent (Fisher's letter of 7 Jan 1930, §8).
- **Efficiency (Fisher 1925)** — the limit of n·Var(T) is as small as possible, among consistent, asymptotically normal T.
- **Equistatistical surface / expectation line** — in Fisher's 1930 geometry, the level sets of T in the simplex of relative frequencies, and the curve f(θ) of cell probabilities.
- **Ancillary statistic** — Fisher's 1925 term, used as a covariate to reduce the "residual" E[Var(X|T)].

## Connections

- **Sources Stigler builds on:** his own "Fisher in 1921" (2005) and his history of Pearson's errors (2007); Hald's histories; Savage (1976); Pratt (1976); Efron (1975, 1982) on curvature and the geometry of ML; Kass & Vos (1997) on geometrical asymptotics.
- **[LIT-048](../literature.d/LIT-048.md) (Barnett & Bossomaier, read in reads/c50.md).** That letter's χ² result for transfer entropy is imported from Wald (1943), which Stigler (§11) presents as the rigorous completion of Fisher's 1922 argument, with conditions so restrictive they excluded basic examples. [LIT-048](../literature.d/LIT-048.md) does not check those conditions for its model. Stigler's growing-parameter warning also applies to [LIT-048](../literature.d/LIT-048.md)'s finite-state estimator, whose parameter count grows as a^k b^k. This link is mine; neither text makes it.
- **[LIT-018](../literature.d/LIT-018.md) (Fuchs, "Distinguishability and Accessible Information in Quantum Theory").** No textual link. Hotelling's Appendix 3 metric is the Fisher information metric, which Fuchs's quantum distinguishability measures generalise. I note this only as context.

## Bearing on the record

- In this record it is [LIT-044](../literature.d/LIT-044.md). Its summary should be revised on three points: Hodges is minor by Stigler's account and growing parameters are the practical failure; the third proof was published in disguise in 1935; and the closing claim is hedged ("perhaps"). Status: Deferred → Active.
- No THEORY document here depends on it.
- **For the Anthology of the SOTA:** no instruction for ML practice. Stigler's §12 remark that the Neyman–Scott example "still serves as a warning of what might occur in modern highly parameterized problems, where the information in the data may be spread too thinly to achieve asymptotic consistency" is the one sentence an anthology THEORY on why maximum-likelihood training (e.g. cross-entropy) need not inherit classical ML guarantees at scale might quote. It is a historian's remark, not a result about neural networks. The anthology documents that treat cross-entropy as maximum likelihood (e.g. [ANTH-THEORY-043](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-043.md), [ANTH-THEORY-107](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-107.md)) do not need it as a source.

## Limitations

- It is a history. Its theorem statements are reconstructions and sketches, not proofs. Readers needing the conditions for consistency and efficiency should go to Wald (1949), Cramér (1946), Le Cam (1953) or van der Vaart (1998), as Stigler himself indicates.
- Several key interpretive steps are explicitly speculative: why Fisher dropped the sufficiency claim (§6), the logical route to the ANOVA proof (§7), and the role of temperament and the feud (§14).
- Coverage stops at Le Cam's 1953 dissertation. Stein's 1955 shrinkage is mentioned in one sentence. Later asymptotic theory (local asymptotic normality, the Hájek–Le Cam convolution and minimax theorems) is not covered.
- The archival letters are quoted selectively; the full correspondence is not reproduced, except Enclosure A and Hotelling's summary.

## Open questions

- A modern, clear identification in print of exactly where Doob's and Dugué's proofs fail. Stigler says none exists (§14); he supplies one only for Hotelling.
- Whether Fisher's 1930 geometric proof extends cleanly to continuous regular families, which its geometry "superficially" promised (§11). Modern information geometry (Efron 1975; Kass & Vos 1997) is where this would be settled.

## Corrections to the seeded skim

- The dossier summary lists "the 1950s counterexamples (Hodges's superefficiency, growing parameter counts, unbounded likelihoods)" as marking "real limits". Stigler dates and weighs them differently.
  - Growing parameter counts come from Wald's 1938 letter to Neyman, published as Neyman & Scott (1948). Stigler calls this one "of more practical import", a warning "in modern highly parameterized problems" (§12).
  - Hodges's example (1951, published in Le Cam 1953) he calls "an ingenious but minor technical achievement", since Le Cam proved superefficiency possible only on a Lebesgue-null set.
  - He treats the normal-mixture unbounded likelihood (Kiefer–Wolfowitz folklore, 1950s) as "at least computational" in importance, and cites Cox as calling it somewhat pathological.
  - So the limits are not equally "real" in Stigler's account.
- The dossier and [LIT-044](../literature.d/LIT-044.md) call the third item "an unpublished 1930 characterization". It was a *proof*, Fisher's Enclosure A to Hotelling, 28 Nov 1930 (Appendix 2). It was published in disguised form: as an estimating-equation argument in Fisher (1935, pp. 45–46) and Fisher (1938, pp. 30–32), and in simplified form in Fisher (1956, pp. 145–148) (§10). It is "unpublished" only in its original geometric form. The abstract's "unpublished 1930 characterization of conditions" refers to this enclosure.
- The dossier's closing line, "ML's useful scope still exceeds anything that can reasonably be proved", is Stigler hedging, not asserting: "*Perhaps* as Fisher's powerful geometric intuition may have foreseen, the scope of useful application … exceeds that of any reasonably achievable proof" (§14).
- The dossier says the Hotelling, Doob and Dugué errors were "never … clearly identified in print". Stigler says that of the literature *before* him (§14). He himself identifies Hotelling's error in §8: an arctan reparametrisation to a finite interval combined with discretisation of the observations does not give the uniformity needed beyond discrete, bounded-parameter cases. Hotelling listed the gap as problem [#16](https://github.com/dmarx/nucleation/issues/16) of his 1931 "Outstanding Problems". Doob was "gently corrected by Wald", and Dugué's slip was found by Edith Mourier in the mid-1940s (§11).
- A precision the dossier omits: Stigler's §14 defence of Fisher is explicitly qualified. He says it "flirts with tautology", because any statement is true if all the conditions required for its truth are assumed. What distinguishes Fisher from Pearson–Filon is that Fisher's implicit conditions were clear to him and he misapplied none that Stigler knows of.
