---
status: Read
paper: 'LIT-tmp2w545'
title: 'Semantic Rate-Distortion Theory with Applications'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from arXiv v1 (12 September 2025, 34 pages, text
    extracted with pdftotext): Sections 1–6, Appendices A–D and the
    reference list. Every proof was followed; Theorem 3's closed
    form was checked numerically against a grid search over p(Y|X) at
    q = 0.9 for five (D_p, D_o) pairs (agreement to grid resolution). The identities stated under Bearing
    on the record (the KL case as the information bottleneck, the TV case
    as a bound on Bayes risk) are my derivations, not the paper's.
    Figures 1–9 were not seen; their captions and the tables were.
date: '2026-10-09'
summary: >-
  Defines semantic distortion between the posterior of a latent meaning
  given the original and given the reconstructed observation, and proves
  that the resulting information rate–distortion function, with a second
  symbolic constraint, is the operational limit under lower
  semicontinuity; solves the binary symmetric case. Its sequence
  distortion is defined as an expected maximum but the proofs use maxima
  of expectations; with KL divergence the function is the information
  bottleneck, which the paper does not note.
---

<!-- inactive-ok-file: THEORY-156 — Proposed; cited for the comparison of experiments the TV bound relates to -->
<!-- inactive-ok-file: THEORY-tmp3ijnj — Proposed; filed from this reading, under test -->
<!-- inactive-ok-file: CLAIM-tmpek80j — Proposed; named as a manuscript claim this reading bears on -->

# NOTE-tmpsmtp6: Semantic Rate-Distortion Theory with Applications

## Contribution

Earlier semantic rate–distortion work (Liu, Zhang and Poor; Chai et al.,
[LIT-tmpfnpwq](../literature.d/LIT-tmpfnpwq.md)) asks the decoder to estimate the hidden meaning S, or to
match its marginal law. This paper instead asks that the reconstruction
leave the receiver with the same posterior over meanings as the original
would have: d_p(p(S|x), p(S|y)). It proves the corresponding coding
theorem, with an ordinary distortion on the symbols as a second
constraint, and computes the function for a binary source.

## Key insight

When an observation supports several readings, the thing to transmit is
the distribution over readings that it supports, and fidelity is how close
the receiver's distribution, given what it receives, comes to that. The
reconstruction need not look like the original, only be equally
informative about S.

## Assumptions

- (S, X) i.i.d. with a known joint law p(S, X); S is task-relative,
  fixed by a task known to both ends. Coding acts on X; the decoder
  outputs Y; S–X–Y is a Markov chain (Definition 8).
- Perfect channel: the paper studies compression only.
- Stochastic encoders and decoders with access to randomness (common,
  local or both).
- d_p is any non-negative function on pairs of distributions over S; the
  converse needs R^I lower semicontinuous, guaranteed (Proposition 2) for
  finite alphabets when d_p is continuous in its second argument and a
  regularity condition (16) holds.
- **Sequence distortion** (Definition 3): d(xⁿ, yⁿ) = max over i of
  d(x_i, y_i), for both distortions, with the constraints on its
  expectation (Eqs. 8–9). See Bearing on the record: the proofs do not use
  this definition.

## Key results

- **Theorem 1 (achievability).** R^I(D_p, D_o) ≥ R^O(D_p, D_o): the Poisson
  functional representation (Li and El Gamal) gives codes of rate
  I(X;Y) + O(log n / n) whose output is exactly distributed as the
  single-letter optimiser's n-fold product.
- **Theorem 2 (converse).** If R^I is lower semicontinuous then
  R^O ≥ R^I, so the two are equal. The proof is the standard chain
  I(Xⁿ; Yⁿ) ≥ Σ I(X_i; Y_i) and convexity-free monotonicity.
- **Proposition 2 (lower semicontinuity).** For finite S, X, Y, d_p
  continuous in its second argument and condition (16); the remark says
  bounded d_p (TV, Wasserstein) and every f-divergence satisfy it.
- **Theorem 3 (binary).** ρ = ½, q₁ = q₂ = q, d_p = TV, d_o = Hamming,
  C = |1 − 2q|: R = 1 − h₂((1 − √(1 − 2D_p/C))/2) for D_p ≤ a(D_o), and
  R = 1 − h₂(min(D_o, ½)) for D_p > a(D_o), where a(D_o) = 2C·D_o(1 − D_o)
  for D_o ≤ ½ and C/2 above. The expected TV distortion is
  Λ(w, z) = C(wz/(w + z) + (1 − w)(1 − z)/(2 − w − z)) ≤ C/2, so for
  D_p ≥ C/2 the semantic constraint is idle, and for q = ½ (X carries no
  information about S) it is idle everywhere.
- **Experiment** (Tables 1–2). MNIST, MLP autoencoder, rate d·log L;
  loss MSE + γ·KL(one-hot true label ‖ classifier output on the
  reconstruction). Digit accuracy of a fixed classifier on reconstructions:
  at 4 bits 14.6% (γ = 0), 78.0% (0.01), 95.0% (0.1); at 12 bits 62.4%,
  94.2%, 98.2%; γ = 0 needs 36 bits for 85%. At 8 bits with γ = 100, 97.9%
  accuracy from images "barely recognizable to human observers".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The information semantic rate–distortion function is achievable | strong for per-letter expected distortions; not shown for the expected-maximum distortion of Definition 3 | Theorem 1, Appendix A |
| C2 | It is the operational limit under lower semicontinuity | strong, same proviso | Theorem 2, Appendix B |
| C3 | Lower semicontinuity holds for finite alphabets and bounded distortions | strong | Proposition 2, Appendix C |
| C4 | Lower semicontinuity holds for every f-divergence | weak: asserted as "easily verified"; KL is unbounded and the condition is not checked | remark after Proposition 2 |
| C5 | Closed form for the doubly symmetric binary case | strong | Theorem 3, Appendix D, checked numerically |
| C6 | Constraining posterior distortion improves semantic accuracy and saves rate | moderate for the experiment run, which is task-aware training against a classifier; it does not test the theory's quantity | Tables 1–2 |

## Method

Achievability: pick the single-letter p(Y|X) meeting both constraints at
rate near R^I; encode Xⁿ by the index K of the first point of a Poisson
process, marked by i.i.d. draws Ỹ_i from p_Yⁿ, that minimises
T_i · dp_Yⁿ/dp_Yⁿ|Xⁿ(Ỹ_i | xⁿ); the decoder outputs Ỹ_K. Then (Xⁿ, Ỹ_K)
has exactly the product law and H(K) ≤ nI(X;Y) + log(nI + 1) + 4.

## Concepts

- **intrinsic meaning / extrinsic observation**: s, the task-relevant
  content, and x, the string that carries it; "semantic kernel" and
  "medium".
- **semantic probability distortion (based on the observation)**:
  d_p(p_S|x, p_S|y), a divergence between posteriors over meanings.
- **observation distortion**: an ordinary distortion d_o(x, y).
- **ambiguity / polysemy**, as the paper uses them: "orange" (colour or
  fruit) is called ambiguity, "several days" (three to seven, equally
  likely) polysemy. In linguistic usage the first is polysemy or
  homonymy and the second vagueness; the paper's point needs only that
  one string supports a distribution over readings.

## Connections

It builds on rate–distortion–perception theory (Blau and Michaeli; Theis
and Wagner; Chen et al.) for its proof techniques, and on the
latent-state semantic sources of Liu, Zhang and Poor. It cites Chai et al.
([LIT-tmpfnpwq](../literature.d/LIT-tmpfnpwq.md)) as a semantic RDP framework, describing it as using
"adaptive divergence metrics", where that paper fixes total variation on
the marginal law. It does not cite the information bottleneck ([LIT-338](../literature.d/LIT-338.md))
or the indirect rate–distortion problem with logarithmic loss, to which
its KL case reduces (below). Reference [6] (Gholipour et al. 2025) is cited
for the claim that semantic communication can exceed Shannon capacity, the
same claim the survey reports ([LIT-tmpmigxa](../literature.d/LIT-tmpmigxa.md)).

## Bearing on the record

- **The KL case is the information bottleneck.** Under S–X–Y,
  E[D_KL(p(S|X) ‖ p(S|Y))] = E log p(S|X)/p(S|Y) = H(S|Y) − H(S|X) =
  I(S;X) − I(S;Y). So with d_p = KL and no symbolic constraint,
  R(D_p) = min{I(X;Y) : I(S;Y) ≥ I(S;X) − D_p}, which is Tishby, Pereira
  and Bialek's bottleneck ([LIT-338](../literature.d/LIT-338.md)) with the reconstruction as the
  bottleneck variable. The paper names KL as a valid d_p but does not
  make this connection, and so does not see that its central constraint,
  for that choice, is twenty-five years old. My derivation.
- **The TV case is decision-relative.** For any loss L(a, s) with range
  at most 1, the receiver who acts on p(S|y) incurs at most E d_TV(p(S|X),
  p(S|Y)) more Bayes risk than one who could act on p(S|x): for each pair,
  min_a E_{p(S|y)}L − min_a E_{p(S|x)}L ≤ sup_a |E_{p(S|y)}L −
  E_{p(S|x)}L| ≤ d_TV. So a bound D_p bounds the loss of informativeness
  uniformly over every bounded decision problem about S, for the given
  prior; D_p = 0 means Y is as informative about S as X. This is the
  quantitative, prior-fixed counterpart of the Blackwell comparison the
  record states in [THEORY-156](../theory.d/THEORY-156.md). My derivation.
- **[CLAIM-tmpek80j](../claims.d/CLAIM-tmpek80j.md)** (fidelity relative to the receiver's decisions,
  made precise by Blackwell's order). The TV case above is a working
  example of that claim's standard, and the paper is prior art for it in
  communication: a rate–distortion function whose fidelity criterion
  controls every bounded decision about the meaning. It differs from the
  claim in fixing the prior on S and in using one divergence rather than
  a family Q of decision problems.
- **[CLAIM-tmpp8j04](../claims.d/CLAIM-tmpp8j04.md).** The exchange's description is accurate:
  "ambiguity, polysemy, and distortion of conditional semantic probability
  distributions" is what the paper formalises, and preserving a
  distribution over interpretations is its stated aim. The concession is
  therefore well founded, and stronger than the exchange knew, because the
  KL version reaches back to the information bottleneck. What the paper
  does not have is any structure on S (no overlapping contexts, no
  compatibility between local readings) or any sequential composition of
  reconstructions; S is one finite variable per symbol.
- **The definitions and the proofs disagree.** Definition 3 sets the
  sequence distortion to max over i of d(x_i, y_i), and Eqs. 8–9 bound its
  expectation. Appendix A, Eqs. 32–33, writes E[max_i d] = max_i E[d], which
  is false in general (the expectation of a maximum is at least the
  maximum of expectations; for Hamming distortion and i.i.d. errors it
  tends to 1). Appendix B's converse works with max_i E[d] (Eqs. 35–36).
  So Theorems 1–2 are proved for constraints on per-letter expected
  distortion, max_i E[d(X_i, Y_i)] ≤ D, not for the definition as written.
  Under that reading the results stand; under the written one,
  achievability is not shown.
- **The experiment is not the theory.** The theory's p(S|x) is the
  posterior under the source law and p(S|y) the posterior under the code.
  The experiment replaces the first by a one-hot true label and the second
  by a pretrained classifier's output, so the trained objective is MSE
  plus the classifier's cross-entropy: task-aware compression, a known
  technique. Its results show that training for the task helps the task,
  not that the posterior-distortion function is achieved.
- Source of [THEORY-tmp3ijnj](../theory.d/THEORY-tmp3ijnj.md). Not machine-learning practice, though the
  experiment is a training recipe; no anthology flag.

## Limitations

- Finite alphabets for lower semicontinuity; the binary case is
  doubly symmetric with a uniform prior.
- No channel: compression only, on a perfect channel.
- The joint law p(S, X) is assumed known to both ends; where it comes
  from, for natural language, is not discussed.
- The remark that every f-divergence satisfies condition (16) is not
  proved, and KL, the divergence the experiment uses, is unbounded.
- "Weierstrass distance" in the remarks after Theorem 2 is presumably
  the Wasserstein distance.

## Open questions

- Restate Definition 3 and Eqs. 8–9 with per-letter expectations (or an
  average), or prove achievability for the expected maximum; one or the
  other closes the gap.
- With d_p = KL and a symbolic constraint, the function is a bottleneck
  with an extra distortion constraint; is its binary closed form known
  from the bottleneck literature?
- For several tasks at once (several S), does a single code with small
  posterior distortion for each exist at the rate of the hardest one, or
  is there a penalty? The paper's model has one task.
