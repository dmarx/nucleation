# Reader notes: LIT-tmp0z602 (Amari, Park & Ozeki 2006)

## Copies located (2026-11-21)

- https://bsi-ni.brain.riken.jp/database/file/274/280.pdf — RIKEN Brain
  Science Institute publication database (the first and third authors'
  institute): the published MIT Press version, 59 pp., Neural Computation
  18, 1007–1065. Kind: research-institution page (ADR-074). First fetch
  reset mid-transfer (agent proxy: tunnel closed); second fetch 200,
  application/pdf, 608,606 bytes. Read.
- https://doi.org/10.1162/neco.2006.18.5.1007 — publisher, closed (OpenAlex
  oa_status closed). Not fetched.
- https://pure.teikyo.jp/en/publications/e86d54aa-0d92-466b-83b3-9e7eb6e9165a
  — Teikyo Pure record (OpenAlex), no pdf_url listed. Not fetched.
- https://research.knu.ac.kr/en/publications/singularities-affect-dynamics-of-learning-in-neuromanifolds/
  — Kyungpook (Park) record page. Not fetched.
- Semantic Scholar: openAccessPdf CLOSED. No arXiv copy.

## Provenance

Read from the RIKEN BSI copy above (PDF, published version, pp. 1007–1065),
converted with pdftotext -layout. Read in full: abstract, §§1–7 (pp.
1007–1052), including all theorems. Skimmed: appendix proofs (pp.
1052–1061). Skipped: references. Figures are not in the text extraction;
their captions were read. The extraction drops some symbols, notably ≠
(e.g. p. 1040 prints "u∗ = 0 (singularity) and u∗ = 0 (regular)" for
u* = 0 and u* ≠ 0); quotes below are corrected only where the sense is
unambiguous, and marked.

## Summary

A review of the authors' results (Amari & Ozeki 2001; Amari, Park & Ozeki
2001–2003) on singular statistical models — multilayer perceptrons,
gaussian mixtures, a toy "cone model" — plus a new analysis of learning
dynamics in a gaussian mixture (§5.3). Parameters that give the same
distribution form a critical set C on which the Fisher matrix degenerates;
identifying them gives a reduced space M̃ with a cone-type singularity
(§3, after Dacunha-Castelle & Gassiat 1997). Consequences surveyed: the MLE
is not asymptotically gaussian, the likelihood-ratio statistic grows like
log n (MLP) or log log n (mixtures), AIC/BIC/MDL lose their justification,
a smooth prior on M is "infinitely large" at singular points of M̃ (§4).
§5: near C, gradient descent has fast and slow manifolds — the state is
quickly attracted to a slow manifold near the singularity and then moves
slowly along it, the plateau; natural gradient removes it. §6:
generalization and training errors for MLE and Bayes (uniform and Jeffreys
priors) in the cone model and the one-hidden-unit MLP, when the truth is
at the singularity.

## Contribution

A unified picture of where singularities come from in hierarchical models
and what they break, with toy models solved explicitly; the first
fast/slow-manifold analysis of gradient learning near a gaussian-mixture
singularity; explicit errors showing that in singular models
generalization depends on the prior and E_gen = −E_train can fail.

## Key results

1. **Fisher degeneracy on a continuum.** p. 1009: "Riemannian metric
   degenerates at such singular points, which are not isolated but form a
   continuum." For one hidden unit, ∂l/∂v = 0 at v = 0 (or ∂l/∂w = 0 at
   w = 0), Eqs. 2.8–2.9, p. 1013: "the Fisher information matrix, equation
   2.6, degenerates, and its inverse G⁻¹(θ) does not exist in the set
   C : vw = 0. The Cramér-Rao theorem is no longer valid at the critical
   set C." For k hidden units the critical set is vᵢwᵢ = 0 or wᵢ = ±wⱼ
   (Eq. 2.25, p. 1019): "Since the Fisher information is 0 along this
   direction, the Fisher information matrix degenerates, and its inverse
   diverges to infinity … the distance becomes 0 along a certain
   direction." Cone model, Eq. 5.4: G(ξ, θ) = diag(1 + c², c²ξ²), rank 1
   at ξ = 0.
2. **Where the singularity sits in the model's image.** One hidden unit,
   p. 1012: identifying equivalent points, "the critical set C is reduced
   to a single point. … It consists of two components connected by a
   single point (see Figure 1, right). In other words, M̃ has
   singularity." Mixture, p. 1015: "the space where singularities are
   accumulated on a line C̃ and the dimensionality is reduced on the
   line"; embedded in an exponential family, a line v = const "is not
   smooth but is a cusp in S" (pp. 1017–1018), and as v(1 − v) → 0 "the
   points in M̃ shrink toward the origin as u → 0 but expand into infinite
   dimensions" (p. 1018). Two-unit example, p. 1020: "is a cone depicted in
   Figure 4, and the apex is the singular point." Cone model, p. 1022: "two
   cones, one for ξ ≥ 0 and the other for ξ ≤ 0, of d + 1 dimensions …
   connected at the apex ξ = 0. The apex ξ = 0 is the singularity."
   General, p. 1025: "the image of M forms a cone in the space of
   functions of x, whose apex is log p0(x) … This is called the tangent
   cone." The word "boundary" does not occur in the paper.
3. **Plateaus: attraction to the critical set even from a regular truth.**
   p. 1018: "In gradient descent learning algorithms, the critical set C
   works as a pseudo-attractor (the Milnor attractor) even when the true
   distribution is at a regular point far from it. The singular point
   resembles a black hole in the dynamics of learning". p. 1009: "once
   parameters are attracted to singular points, … [they] are very slow to
   move away from them. This is the plateau phenomenon". §4.5 (pp.
   1032–1033), reporting Fukumizu & Amari (2000): the line Q of
   two-unit perceptrons equivalent to the best one-unit approximation
   "forms critical points of the cost function"; part of it "can be truly
   attractive, although it is not a usual asymptotically stable
   equilibrium but has directions of escape … the perceptron is truly
   attracted to the line and stays inside the line … until it finds a
   place from which it can escape. This explains the plateau phenomenon."
   And: "The problem of plateau cannot be resolved by simply increasing
   η".
4. **Fast and slow manifolds.** p. 1035: "a slow manifold emerges around
   the critical set to which the state is quickly attracted by fast
   dynamics, and then the state escapes toward the optimal point slowly in
   the slow manifold. This is a universal feature of the plateau
   phenomenon." Cone model, p. 1036: "ξ̇ is of order O(1), whereas θ̇ is of
   order O(ξ) … The dynamics becomes especially slow when ξ is small".
   Figs. 8, 10, 13: clear plateaus in the standard-gradient loss curves,
   none under natural gradient.
5. **Truth at the singularity: algebraic approach in the gaussian
   mixture.** Case I (u* = 0), Eq. 5.13, p. 1040: u̇ = −ηc₂(v)²u³,
   v̇ = −η(c₂c₂′/2)u⁴; "When u is small, v̇ is of O(u⁴) and is much smaller
   than u̇, which is of order u³ … u converges to 0 without significantly
   changing v." (The reader's derivation, not the paper's: u̇ ∝ −u³ gives
   u ∝ t^(−1/2). The paper states no rate.) Case II (u* ≠ 0, extraction
   reads "= 0"): the same trajectories, reversed, "escaping from u = 0
   toward u*" (p. 1041); then quickly to M_S, slowly along it (p. 1042).
   Reported from Park, Inoue & Okada (2003), p. 1034: with the truth on the
   singularity, the trajectory "does not stop at any point in the line …
   and … approaches the point where either v1 or v2 is zero."
6. **Natural gradient near C.** p. 1034: "Since the metric degenerates in
   C, its inverse diverges to infinity. … if we evaluate G⁻¹∇L near C, we
   can see that the infinitely strong repulsive force works in the
   direction of escape from C (Fukumizu & Amari, 2000)." Cone model,
   p. 1036: under natural gradient "θ̇ is of order ξ⁻¹, so no slow
   manifolds appear." Mixture: update terms O(u⁻²), O(u⁻³) (p. 1043).
7. **Priors.** p. 1029: "a smooth prior on M is singular in the
   equivalence class M̃ … the Bayesian smooth prior is in favor of
   singular points (perceptrons with a smaller number of hidden units)
   with an infinitely large factor." Theorems 4, 6, 8, 10: Bayes E_gen =
   1/(2n) under a uniform prior on ξ, (d+1)/(2n) under Jeffreys (which is
   0 at ξ = 0).
8. **Testing.** E[λ] = c(n)k with c(n) = log n for MLPs (Fukumizu 2003)
   and log log n for mixtures (Hartigan; Liu & Shao), Eqs. 4.3–4.5.

## Assumptions

Averaged (deterministic) learning equations, small learning rate, online
gradient (Eq. 4.17). Gaussian output noise, squared error = −log
likelihood. Toy models of one hidden unit, two-unit committee, a cone in
R^(d+2), a two-component 1-D mixture with known mean; the mixture analysis
is a small-u Taylor expansion with v(1 − v) > c, so it does not cover the
v → 0, 1 branches of C. Bias-induced nonidentifiability ignored (p. 1020).
§6 assumes the truth at the singularity, and some results large d or the
Donsker condition (p. 1047 notes non-Donsker failure as β → 0).

## Concepts

Neuromanifold; critical set C; reduced space M̃ (residue class); locally
conic structure and tangent cone (Dacunha-Castelle & Gassiat); gaussian
random field Y(ω); Milnor (pseudo-)attractor; slow and fast manifolds;
plateau; natural (Riemannian) gradient and its adaptive form (Eq. 4.15);
cone model.

## Verdict on the exchange's characterization

As registered: "singular regions where parameters are unidentifiable;
gradient learning is attracted to them and slows, which produces
plateaus". Accurate, with one sharpening: the paper's plateau is chiefly
the regular-truth case — attraction to a Milnor-attractor critical line
and slow escape along a slow manifold — not relaxation into a singular
optimum. Natural-gradient behaviour near singularities: accurate — the
paper says natural gradient sees an "infinitely strong repulsive force"
from C and shows no plateau, while warning (p. 1018) that "the effect of
the singularity is not negligible when the true distribution is at, or
near, the singularity C." Transtrum 2011's equating of network metric
singularities with manifold *boundaries*, citing this paper (as
NOTE-tmpzxtnv reports): the paper does not say "boundary". It places the
singularities in the interior of parameter space (vw = 0, w₁ = w₂ at
finite values) and in the image at a cone apex, a pinch point joining two
components, or a cusp line — places where the model has a tangent cone
instead of a tangent space. Whether a cone apex counts as a "boundary" in
Transtrum's sense (any point where the metric is singular) is
definitional there; in the ordinary sense of an edge where the manifold
ends, the paper's pictures (Figs. 1, 4, 5) do not show one, except that
the reduced cone in ξ ≥ 0 ends at its apex. The citation stretches the
paper.

## Bearing on the named codes

- **CLAIM-tmpcbfdj** — supports the first part, parallel to the
  qualification. Eq. 5.13 is the claim's quartic case in a real model:
  with the truth at the singularity the gradient along u is cubic, so the
  approach is algebraic (t^(−1/2), reader's derivation). And, as in the
  claim's off-balance qualification, the flow reaches the critical set at a
  generic point: "u converges to 0 without significantly changing v". The
  paper does not discuss learning coefficients, so it is silent on the
  second part. It does hold the distinction CLAIM-tmpcbfdj says the record
  lacks: three cases, truth at, near, and away from the singularity (§4,
  p. 1027), with plateaus in the regular case coming from slow escape and,
  at the singularity, slow entry (p. 1034: "the component of the flow
  entering C is extremely slow near C").
- **CLAIM-tmpv5asv** — qualifies. It supports that slow phases in
  gradient training can be singular in origin, and attributes the
  backpropagation plateau to singularity (§4.5). But its plateaus are
  transients that end in escape, shown on two-parameter toys; it reports
  no power-law relaxation, no distribution of timescales, and no
  comparison with criticality. Nothing bears on the second part
  (dependency trees).
- **CLAIM-tmpp83vc** — background; supports the exchange's "dynamics are
  separate" point (A37 §4). The paper's dynamics use the Fisher metric and
  fast/slow manifolds, never resolution of singularities; algebraic
  geometry is "Another general framework … which we do not summarize
  here" (p. 1024). Its Bayesian remark (smooth prior favours singular
  points "with an infinitely large factor", p. 1029) is consonant with
  reading (b) but gives no transition account.
- **ARG-tmpmvc5e** — supports the "relevant difference": the Fisher matrix
  of an MLP degenerates on continua at finite parameters (p. 1009,
  Eq. 2.25), and the paper's whole point is that regular-model theory
  (Cramér–Rao, AIC, BIC) does not hold there. Qualifies the dated note's
  report that Transtrum "equates network metric singularities with
  boundaries, citing Amari, Park and Ozeki": the cited source calls them
  cone apices and critical sets, not boundaries.
- **NOTE-tmpzxtnv** — qualifies its line 116 in the same way; the
  citation is Transtrum's reading, not the paper's term.
- **THEORY-082** (held) — supports. Eqs. 2.8–2.9 and 2.25 give the same
  degeneracy THEORY-082 derives from Amari 1998's Eq. 6.12 (the factor
  vᵢ), and add the w = 0 and wᵢ = ±wⱼ components; p. 1013 states the
  Cramér–Rao failure on C directly. Its natural-gradient escape result
  ("infinitely strong repulsive force") is a dynamical complement to
  THEORY-082's point that Fisher efficiency is undefined there.

## Limitations

A review, mostly of the authors' earlier papers; several key dynamical
claims (Milnor attractor, repulsion under natural gradient, Park et al.'s
entry point) are reported, not derived here. Toy models with two
effective parameters; the mixture analysis is local in u. No rates of
plateau escape are given; plateau lengths are shown only in figures. The
natural-gradient analysis does not address what happens exactly on C,
where G⁻¹∇L is "0 × ∞". Text extraction lost ≠ signs and figure content.

## Candidate THEORY sentence

In a multilayer perceptron the Fisher matrix degenerates on a continuum
of finite parameters (vᵢwᵢ = 0, wᵢ = ±wⱼ), which collapses in the space of
distributions to a cone-type singular point; near it ordinary gradient
learning has fast and slow manifolds, so the state is quickly drawn
toward the singularity and then moves slowly along a slow manifold — the
plateau — even when the truth is regular, while natural gradient is
repelled from it and shows no plateau.

promote_when: the record rederives the cone model's fast/slow split
(ξ̇ = O(1), θ̇ = O(ξ) under gradient; θ̇ = O(1/ξ) under natural gradient,
from G = diag(1 + c², c²ξ²)) and the Fisher rank loss on vw = 0, and
reproduces the plateau in the standard but not the natural-gradient loss
curve of the cone model or one-unit MLP from (ξ, θ) = (1.5, 5π/6).

## Recheck (grep of record/ after reading)

Terms: Milnor, slow manifold, cone model, Fukumizu, Saad, Rattray,
Dacunha, tangent cone, Hartigan, critical set, neuromanifold, committee
machine, Jeffreys, log log n, plateau, Amari. Held entries the first
search missed:
- **THEORY-2009** (Proposed; Chen, Kunin, Yamamura & Ganguli, LIT-2793):
  the sets where a neuron vanishes or two neurons are identical — exactly
  this paper's critical set (Eq. 2.25) — are invariant under SGD and can
  attract. Parallel and supporting: a modern restatement of the critical
  set as attractor (this paper's Milnor attractor), with SGD noise in
  place of averaged flow.
- **THEORY-740**, **THEORY-186**, **THEORY-187** (Saxe et al.; LIT-864,
  NOTE-667, which mentions Fukumizu): stagewise plateaus in deep linear
  networks from small balanced starts. Parallel: plateaus at the origin
  saddle of a product parameterization, a singular point of the same kind
  (w = 0, v = 0).
- **QUESTION-363**, **QUESTION-039**: the order of acquisition in
  training; this paper bears as background (plateaus as dwelling near
  smaller-model critical sets: "the smaller one forms a critical set
  within the larger neuromanifold", p. 1030).
- **NOTE-472** (Amari 1998, natural gradient) mentions plateaus; consistent.
- **LIT-tmpv9upr** (Wei et al., Deferred) is the paired work; mentions
  Milnor.
No hit for Dacunha-Castelle, tangent cone, Hartigan, or critical set. The
"cone model" hits (THEORY-825, NOTE-1764, LEAD-tmpp88ld) concern
hyperbolic entailment cones, not this model.

## Neighbours

Not needed; the work itself was read. No other work was read or quoted.
