---
status: Read
paper: 'LIT-tmpcwed2'
title: 'No, Ingber and Weissman — Strong successive refinability'
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Read in full from arXiv:1506.03407v2 (33 pages), text extracted with
    pdftotext. Read: the abstract, §I, §II (source dispersion, Theorems 1–2;
    successive refinement, Theorems 3–4 and Definition 2), §III
    (Definitions 3–4), §IV (Theorem 5, Corollary 6, Remark 1, Theorem 7),
    §V (method of types, Lemma 8, Corollary 9, the four-case scheme and
    Lemma 10, the Gaussian proof with Theorem 11 and Corollary 12), §VI
    (layered codes: Definition 6, Theorem 13, Lemmas 14–15, Algorithms 1–2,
    Remarks 2–3, the discussion), §VII and Appendices A–H. Displayed
    equations were partly garbled by extraction and were reconstructed
    from the surrounding text; Figures 1–2 are block diagrams, read from
    their captions. Not read: the cited results the proofs rest on
    (Kostina–Verdú and Ingber–Kochman dispersion, the Wang–Ingber–Kochman
    Lemma 3 behind Lemma 10, Rogers' sphere covering, Csiszár–Körner). The
    published IEEE version was not compared. The paper contains nothing on
    logarithmic loss; the registration's premise is corrected below. The
    direct-versus-remote log-loss argument in "Bearing on the record" is
    the record's, checked with
    /tmp/claude-0/-home-user-nucleation/409f735e-c44b-5ba1-82f0-18d34af58efc/scratchpad/niw-scripts/logloss_check.py.
date: '2026-10-20'
summary: >-
  Extends successive refinement to second order. For finite alphabets, a
  two-stage code can reach both decoders' rates with their dispersion terms
  if the source is successively refinable throughout a neighbourhood of its
  law (Corollary 6), which holds for any discrete source under Hamming
  distortion; the Gaussian under squared error is shown directly. Layered
  codes then use L_n refinement stages to cut encoding complexity, at a rate
  penalty of order L_n log n / n, for binary and Gaussian sources. It does not
  treat logarithmic loss, which the reading that named it had recalled; the
  log-loss refinability result is No and Weissman's, concerns direct log-loss
  with soft reconstructions of the source itself, and does not reach the
  information bottleneck, whose loss is remote.
---
<!-- inactive-ok-file: THEORY-tmpe422n THEORY-163 CLAIM-157 — Proposed; the first-order characterization and an open reading this bears on, nothing here rests on their being settled -->
# NOTE-tmpmscti: No, Ingber and Weissman — Strong successive refinability

## Contribution

Equitz and Cover asked whether a two-stage description loses rate at first
order, n → ∞. This paper asks whether it loses anything at second order, in
the √n correction that fixes the rate at finite block length n and excess
distortion probability ε. It gives a second-order achievability result for
successive refinement of finite-alphabet sources, a sufficient condition
for "strong" refinability, and a direct proof for the Gaussian. It then
turns refinement into a complexity tool: a point-to-point code built as many
refinement layers is searched layer by layer, and the number of layers can
grow with n.

## Key insight

When a source is refinable not only at its own law but at every law near
it, the minimum two-stage total rate R(P̃, D₁, D₂) equals the one-stage
R₂(P̃, D₂) on a neighbourhood. The two functions then have the same
derivative in P, and the dispersion is the variance of that derivative
under P. So the second-order terms coincide too. Refinement at all
neighbouring laws is what lets a type-by-type code, which pays for the
empirical type of each block, lose nothing at √n.

## Assumptions

- **A memoryless source.** X₁, X₂, … i.i.d. with law P.
- **Finite alphabets for Theorem 5 and Corollary 6.** 𝒳, X̂₁ and X̂₂ are
  finite, distortions are bounded by d_M, P(x) > 0 for every x, and each
  decoder may have its own distortion d₁, d₂.
- **Smoothness.** R₁(P, D₁) and R(P, D₁, D₂) are continuously twice
  differentiable in D₁, D₂ and in P near (P, D₁, D₂), with derivatives in
  P defined through an extension off the simplex (Appendix A).
- **Excess-distortion criterion.** Success at decoder i means
  dᵢ(Xⁿ, X̂ᵢⁿ) ≤ Dᵢ, with failure probabilities ε₁ and ε₂ counted
  separately (Definition 3), unlike the joint error event of §II-B.
- **The layered-code results are narrower.** Theorem 13 is for a binary
  source under Hamming distortion and the Gaussian under squared error
  only. Remark 3 says why: the scheme needs a difference operation (XOR,
  subtraction) matched to the distortion.

## Key results

- **Theorem 1 (cited, [16]).** For a discrete source,
  R_{P,D,ε}(n) = R(P, D) + √(V(P, D)/n) Q⁻¹(ε) + O(log n / n), with
  V(P, D) = Var[R′(X, D)] and R′(x, D) = ∂R(Q, D)/∂Q(x) at Q = P.
  Theorem 2 (cited, [8]): for N(0, σ²) under squared error, V = ½ nat².
- **Theorem 4 (cited, Koshelev; Equitz and Cover).** Refinable at
  (D₁, D₂) iff some P_{X̂₁X̂₂|X} has X − X̂₂ − X̂₁, Rᵢ(P, Dᵢ) = I(X; X̂ᵢ) and
  E dᵢ ≤ Dᵢ. Stated here with separate distortions d₁, d₂.
- **(16).** R(P, D₁, D₂) = inf I(X; X̂₁, X̂₂) subject to both distortion
  constraints and I(X; X̂₁) ≤ R₁(P, D₁), from Rimoldi's region (Theorem 3).
  Refinable at (D₁, D₂) iff R(P, D₁, D₂) = R₂(P, D₂).
- **Definition 4 (strong successive refinability).** There is a code with
  (1/n) log M₁ = R₁(P, D₁) + √(V₁/n) Q⁻¹(ε₁) + o(1/√n) and
  (1/n) log M₁M₂ = R₂(P, D₂) + √(V₂/n) Q⁻¹(ε₂) + o(1/√n). The converse
  is free, from point-to-point coding.
- **Theorem 5 (finite alphabets).** There is a code with
  (1/n) log M₁ = R₁(P, D₁) + √(V₁(P, D₁)/n) Q⁻¹(ε₁) + O(log n / n) and
  (1/n) log M₁M₂ = R(P, D₁, D₂) + √(V(P, D₁, D₂)/n) Q⁻¹(ε₂) + O(log n / n),
  where V(P, D₁, D₂) = Var[R′(X, D₁, D₂)].
- **Corollary 6.** If every P̃ in a neighbourhood of P is successively
  refinable at (D₁, D₂), then V(P, D₁, D₂) = V₂(P, D₂) and P is strongly
  successively refinable there. *Holds when:* the smoothness above.
- **Remark 1.** Every discrete source under Hamming distortion is
  refinable, so (where R is suitably differentiable) every discrete source
  under Hamming distortion is strongly refinable.
- **Theorem 7.** N(0, σ²) under squared error is strongly refinable for
  σ² > D₁ > D₂, with dispersion ½ at both decoders. The proof covers
  balls with balls (Rogers: fewer than k_s n^{5/2} Rⁿ unit balls cover a
  radius-R ball) and refines additively, x̂₂ = x̂₁ + x̃.
- **Lemma 8 (refined covering lemma).** A type class T_P is successively
  (D₁, D₂)-covered by B₁ and sets B₂(x̂₁) with (1/n) log |B₁| ≤
  R₁(P, D₁) + k₁ log n / n and (1/n) log |B₁||B₂(x̂₁)| ≤ R(P, D₁, D₂) +
  k₂ log n / n, with k₁ = 4|𝒳||X̂₁| + 9 and
  k₂ = 6|𝒳||X̂₁||X̂₂| + 2|𝒳||X̂₁| + 17 independent of P and n.
- **Theorem 13 and Lemmas 14–15 (layered codes).** For L stages with
  D₁ > … > D_L = D, total rate
  Σ (1/n) log Mᵢ ≤ R(D) + √(V(D)/n) Q⁻¹(ε) + L k̃ log n / n + O(log n / n),
  the last term independent of L and the Dᵢ. Encoding searches L
  sub-codebooks of size M = exp(nR/L) each.
  - L_n = n/log²n + 1 gives R = R(D) + O(1/log n) at search cost
    L_n · n^{R log n}.
  - L_n = √n/log²n + 1 keeps the dispersion term, R = R(D) +
    √(V/n) Q⁻¹(ε) + O(1/√(n log n)), at cost L_n exp(R √n log² n).
  - In the limit, binary and Gaussian sources are "infinitesimally"
    (and, at the second rate, "strongly infinitesimally") successively
    refinable, and rateless.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Successive refinement of a finite-alphabet source achieves (R₁ + dispersion, R(P, D₁, D₂) + dispersion) | strong, resting on a cited dispersion lemma | Theorem 5; Lemma 8 proved in Appendices B, F–H; Lemma 10 cited |
| C2 | A source refinable at every law in a neighbourhood of P is strongly refinable at P | strong | Corollary 6, from C1 and equal derivatives |
| C3 | Every discrete source under Hamming distortion is strongly successively refinable | moderate: it inherits C2's smoothness hypothesis, which Remark 1 states loosely | Remark 1 |
| C4 | The Gaussian under squared error is strongly successively refinable | strong | Theorem 7, by sphere covering |
| C5 | Layered codes with L_n stages trade encoding complexity against rate, with penalty of order L_n log n / n, for binary-Hamming and Gaussian sources | strong as an existence result | Theorem 13, Lemmas 14–15 |
| C6 | "An O(n^{log n}) algorithm that asymptotically achieves the rate-distortion bound" (abstract) | weak as worded | see Limitations: an encoding search over codebooks shown to exist, and the bound needs R below one nat |

## Method

Achievability by type covering. The encoder first sends the empirical type
of the block (|𝒳| log(n + 1) bits). Types are split into four classes by
whether the first decoder's rate and the two-stage rate for that type fall
within the second-order budgets ΔR₁ and ΔR₂. Each class gets its own code:
both stages, the first stage only, a point-to-point code for decoder 2 cut
into two messages, or nothing. Lemma 8 builds the two-stage covering of a
single type class by random selection from conditional type classes, with
every slack in log n / n tracked so that the constants do not depend on P.
The Gaussian case replaces types with sphere covering, and refines
additively: the residual x − x̂₁ lies in a ball of radius √(nD₁), which a
fixed second codebook covers. Layered codes iterate that residual step L
times (Algorithms 1 and 2).

## Concepts

- **Source dispersion V(P, D)**: the variance under P of the derivative of
  R(·, D) with respect to the source law. It sets the √n term of the
  minimum rate at excess-distortion probability ε.
- **R(P, D₁, D₂)**: the least total rate of a two-stage code whose first
  stage is at the rate–distortion bound, (16).
- **Strongly successively refinable**: refinable with both dispersion terms
  (Definition 4), with separate error probabilities at the two decoders.
- **Layered code**: a point-to-point code whose codebook is L
  sub-codebooks searched in sequence, each stage a virtual decoder
  (Definition 6).
- **Infinitesimal successive refinability**: refinability with a number of
  stages growing with n and vanishing rate increments (from No and
  Weissman's "Rateless lossy compression via the extremes", cited as [13]).

## Connections

It extends the first-order characterization of Koshelev and of Equitz and
Cover ([LIT-tmp25otd](../literature.d/LIT-tmp25otd.md), [THEORY-tmpe422n](../theory.d/THEORY-tmpe422n.md)) and Rimoldi's rate region to the
second-order (dispersion) regime of Ingber and Kochman and of Kostina and
Verdú. On the error-exponent side it cites Kanlis and Narayan and Tuncel
and Rose, whose four-way split of error events it borrows. Chow and Berger
(1997) are cited for symmetric Gaussian mixtures failing to be refinable
under squared error. The layered codes belong with low-complexity
rate–distortion codes (Gupta–Verdú–Weissman, polar codes for lossy
compression, SPARC) and with tree-structured vector quantization (Effros,
Chou, Riskin and Gray), which it notes cannot reach R(D) in general.

## Bearing on the record

**The registration's premise is wrong.** [NOTE-tmpyi9oi](NOTE-tmpyi9oi.md) recalled this paper
as showing that every discrete memoryless source is successively refinable
under logarithmic loss. The paper never mentions logarithmic loss. The
result recalled is in two other papers, identified on 2026-10-20 from their
abstracts and not read: No and Weissman, "Universality of logarithmic loss
in lossy compression" (ISIT 2015, doi:10.1109/ISIT.2015.7282839,
arXiv:1709.00134), and No, "Universality of Logarithmic Loss in Successive
Refinement" (Entropy 21(2):158, 2019, doi:10.3390/e21020158). The
abstracts say: "if the first decoder operates under logarithmic loss, we
show that any discrete memoryless source is successively refinable under
an arbitrary distortion criterion for the second decoder."

**What "successively refinable under log-loss" means, and why it does not
reach the information bottleneck.** The rest of this section is the
record's argument, not the paper's.

1. *Operationally.* Direct logarithmic loss takes the reconstruction of a
   source letter to be a distribution q over the source alphabet 𝒳, with
   loss d(x, q) = log 1/q(x). A block code sends nR bits about Xⁿ, and the
   decoder outputs one soft reconstruction qₖ per letter. Distortion is the
   per-letter average expected loss, and refinability is the usual
   asymptotic statement, n → ∞, about two such decoders.
2. *Why it is easy.* For any test channel U and any reconstruction rule,
   E[−log q_U(X)] ≥ H(X|U) = H(X) − I(X; U), with equality when q_u is the
   posterior p(x|u). So R(D) = H(X) − D on [0, H(X)], and **every** channel
   with I(X; U) = H(X) − D is optimal. Given an optimal U₂ at D₂, let U₁
   equal U₂ with probability a and an erasure symbol otherwise. Then
   I(X; U₁) = a·I(X; U₂), which reaches H(X) − D₁ for a suitable a, and
   X − U₂ − U₁ is a Markov chain by construction. So the Equitz–Cover
   condition holds at every pair (D₁, D₂). (Checked on five random
   five-letter sources: expected log-loss equals H(X) − I to four places at
   both stages.) The construction uses a finite U with posterior
   reconstructions, so Equitz and Cover's finite-alphabet theorem applies
   to the finite reconstruction set it uses, although Δ(𝒳) is infinite. To
   keep the loss bounded, the posteriors must be bounded away from zero.
   Choosing U₂ with full support does that; the erasure's posterior is
   p(x) itself.
3. *The information bottleneck is remote log-loss.* The encoder sees X,
   and the decoder's q ∈ Δ(Y) is scored on a variable Y that the encoder
   does not see: E[−log q_U(Y)] = H(Y|X) + E KL(p(·|X) ‖ q_U). This is the
   KL distortion [NOTE-tmpyi9oi](NOTE-tmpyi9oi.md) used for the transfer. Here optimal test
   channels are the IB optima, not every channel at the given rate, and
   step 2's degradation fails. In [CLAIM-tmphan8l](../claims.d/CLAIM-tmphan8l.md)'s four-state source, the
   best stochastic encoders found at β = 8 and β = 12 have
   (I(X;T), I(T;Y)) = (0.546, 0.097) and (0.952, 0.139) bits. Erasing the
   β = 12 optimum down to 0.546 bits keeps only 0.079 bits about Y. That
   shows one degradation is suboptimal; [NOTE-tmpyi9oi](NOTE-tmpyi9oi.md)'s linear programme
   had already found no exact degrading channel, without certifying the
   optima.
4. *The two coincide only when Y carries no more than a function of X.*
   If Y = X, KL(δ_x ‖ q) = −log q(x) and the IB is direct log-loss on X.
   If Y = f(X), every optimum factors through f(X) (the averaging step of
   [THEORY-tmp35hmc](../theory.d/THEORY-tmp35hmc.md), which holds in the constrained form too), and the IB
   is direct log-loss on f(X), so it is refinable. In that case
   [THEORY-tmp35hmc](../theory.d/THEORY-tmp35hmc.md) step 4 already showed that the Lagrangian path is
   trivial.

**[QUESTION-tmpproc1](../questions.d/QUESTION-tmpproc1.md): what this does and does not settle.**

- *It does not settle the stochastic half.* The log-loss theorem covers
  direct log-loss, which is the IB only in the degenerate case of point 4.
  It neither shows the IB refinable for stochastic p(y|x) nor shows it not.
- *It sharpens what an answer must be.* For finite alphabets, refinability
  is a statement about single-letter optimal test channels (Equitz and
  Cover's Theorem 2), and single-letter IB optima are exactly those test
  channels for the remote problem. So "successive refinability of the IB
  between two rates" and "some pair of stochastic IB optima at those rates
  satisfies X → Z₂ → Z₁" are the same condition, once the remote coding
  theorem is in hand. The asymptotic and the single-shot readings part only
  for deterministic encoders ([CLAIM-tmphan8l](../claims.d/CLAIM-tmphan8l.md)) and for quantizers of a single
  sample (Equitz and Cover's Fig. 1).
- *"Refinable" asks for some pair of optima, not the ones a solver finds.*
  Under direct log-loss the optima at each rate form a huge family, and two
  arbitrary members at different rates generally do not nest, although the
  source is refinable. An annealing path ([THEORY-163](../theory.d/THEORY-163.md)) that passes no
  degradation test does not by itself refute refinability where optima are
  not unique.
- *In block codes, the messages always nest.* In any two-stage code the
  coarse message is a prefix of the fine one, so the coarse cells of 𝒳ⁿ are
  unions of fine cells: a function, not a noisy function. The Markov chain
  between single-letter channels is the shadow that nesting leaves after
  single-letterization. This bears on the question's "function versus noisy
  function" wording: operationally the function version always holds, and
  what can fail is that both stages be optimal.
- *The leads for the stochastic half,* identified from abstracts and not
  read or registered: Tian and Chen, "Successive refinement for hypothesis
  testing and lossless one-helper problem" (IEEE TIT 54(10), 2008,
  doi:10.1109/TIT.2008.928951), which gives the IB an operational meaning
  through successive refinement; and Charvin, Catenacci Volpi and Polani,
  "Exact and soft successive refinement of the information bottleneck"
  (Entropy 25(9):1355, 2023, doi:10.3390/e25091355, open in PMC
  10528077), which proves refinability for binary, jointly Gaussian and
  deterministic-relevance cases, gives a linear-programming test for the
  discrete case, and measures the loss when refinement fails ("typically
  low, though not entirely negligible"). The second is the most direct
  reading for the question.

**What this paper itself adds.** Refinement, where it holds, survives at
second order if it holds near the source's law as well. Its layered codes
are the operational form of [QUESTION-tmp8qovh](../questions.d/QUESTION-tmp8qovh.md)'s refinement order with
many levels: for binary-Hamming and Gaussian sources, a chain of L_n
nested descriptions, each at the rate–distortion bound, costs only
O(L_n log n / n) in rate. That is a coarse-to-fine hierarchy with
arbitrarily many levels that loses nothing in the limit, but only for
sources already refinable, and only for long blocks. Nothing in it bears on
the dynamical entries named for this batch ([THEORY-733](../theory.d/THEORY-733.md), [THEORY-661](../theory.d/THEORY-661.md),
[CLAIM-157](../claims.d/CLAIM-157.md) and the rest).

No THEORY is filed. The paper's own results are second-order coding
theorems that the record's questions do not turn on. The direct-log-loss
argument above is the record's and is short enough to stand here; it could
be filed as a demonstrated CLAIM.

No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **No log-loss content.** See above.
- **A sufficient condition only.** Corollary 6 needs refinability at every
  law near P. Whether refinability at P alone implies strong refinability,
  for instance at a P on the boundary of a refinable region such as
  Gerrish's three-letter source at p = 3 − 2√2, is not addressed.
- **Remark 1 is loose.** It asks that R(P, D) be "appropriately
  differentiable", while Corollary 6 needs twice continuous
  differentiability of Rᵢ in both Dᵢ and P.
- **The abstract's complexity claim.** With L_n = n/log²n, each stage's
  codebook has M = exp(nR/L_n) = n^{R ln n} words, so the search costs
  about (n/log²n)·n^{R ln n}. That is O(n^{ln n}) only when R < 1 nat. It
  holds for binary sources (R ≤ ln 2) and fails for a Gaussian at
  R = ½ ln(σ²/D) > 1. And the codebooks are shown to exist by covering
  arguments, not constructed, so "design an O(n^{log n}) algorithm"
  describes the search given a codebook.
- **Layered codes cover two sources.** Remark 3 concedes that the residual
  trick needs a group operation matched to the distortion, and does not
  extend it beyond binary sources.
- **Printing slips, none affecting the results.** In the Gaussian proof,
  case 2 of ε₁ < ε₂ writes B(0, r₂) for the ball that C₁^{(0,1)} must
  cover, which is B(0, r₁). Appendix E speaks of "√(nD₁)-balls" for
  Hamming balls of radius nD₁. Appendix F's (190)–(193) write d₂(x, x̂₁)
  for d₂(x, x̂₂).
- **Cited, not proved here.** The point-to-point dispersion theorems and
  the lemma behind Lemma 10.

## Open questions

- Is refinability at P alone enough for strong refinability, or can the
  dispersion term be lost at a law where refinement holds but fails
  nearby?
- Is the information bottleneck, as remote log-loss, refinable for every
  stochastic p(y|x)? The record's evidence ([NOTE-tmpyi9oi](NOTE-tmpyi9oi.md)'s heuristic, step 3
  above) suggests not, and Charvin, Catenacci Volpi and Polani's
  linear-programming test would settle a given instance.
- Do layered codes extend to any discrete source refinable under its
  distortion, without a group structure on the alphabet?
