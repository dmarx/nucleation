---
status: Skimmed
paper: LIT-tmphckuv
title: 'van Rooyen — On Experiments'
version: 1
history:
- version: 1
  date: '2026-10-30'
  note: >-
    Read from arXiv's v2 (arxiv.org/pdf/2508.08288, 13 October 2025, 23
    pages), text extracted with pdftotext. Read in full: §§1–3 (the
    decision problem and probability as positive linear functionals),
    §5 (transitions, comparing experiments, Bayes and minimax risk), §6
    (divisibility, Blackwell–Sherman–Stein, the general data processing
    theorem and its examples), §7 (deficiency, Theorems 26 and 27, Lemma
    28, Theorem 29, Lemma 30) and §8, with the reference list. Theorem 26
    and its proof were checked line by line, and the factor-2 point below
    was checked on a two-state example. Not read: §4 (pp. 3–9), on
    representing loss functions, which the author says appeared before as
    Appendix C of van Rooyen and Williamson (2018); the proofs of
    Theorems 16 and 19, which the paper does not give. Section numbers
    are the paper's; page numbers are the PDF's. Hence Skimmed.
date: '2026-10-30'
summary: >-
  For finite sets and a fixed prior π, Theorem 26 proves Le Cam's
  randomization theorem: the least π-averaged total variation between a
  garbling of e and e′ is at most ε exactly when e's minimum Bayes risk
  exceeds e′'s by at most ε‖L‖∞ for every action set and loss. The proof
  is a minimax argument after Torgersen. It is right for losses in
  [0, 1] and loses a factor of 2 for signed ones, and it is not the
  uniform statement; the uniform one follows from it at every prior with
  one more minimax exchange.
---
<!-- inactive-ok-file: CLAIM-488 — Proposed; the claim this reading bears on, cited as open -->
<!-- inactive-ok-file: LIT-778 — Unavailable; Torgersen, unread, whose proof the paper says it streamlines -->

# NOTE-tmp9x3x4: van Rooyen — On Experiments

## Contribution

A compact account of the comparison of statistical experiments in the
language of Markov transitions between finite sets. Its own list of new
contributions: a general data processing inequality, a bias–variance
decomposition for canonical losses, streamlined proofs of the
Blackwell–Sherman–Stein and randomization theorems, and a linear
programme for deficiency (§1). For this record the contribution is
Theorem 26, a short proof of the randomization theorem with a prior fixed.

## Key insight

Whatever an experiment lets a decision maker do is the set of strategies
d∘e it can reach. Garbling shrinks that set, so every risk minimised over
it can only rise (Theorem 24). Le Cam's theorem is the quantitative
converse: if e's best risk is never more than ε worse than e′'s, a garbling
of e is within ε of e′.

## Assumptions

- **Finite sets.** "The Basic Sets of Study are Finite" (§3.1): unknowns
  Θ, observations Z (§5.2) and, in §7, actions. The minimax steps rely on
  this.
- **Experiments are Markov transitions** e ∈ M(Θ, Z), column-stochastic
  matrices (§5.1–5.2).
- **Losses are real-valued and may be negative** ("a negative loss
  represents a gain", §2), measured by ‖L‖∞ = max_{θ,a} |L(θ, a)|.
- **Variational distance** V(P, Q) = max_A (P(A) − Q(A)) (§6.5), equal to
  ½ Σ_z |P(z) − Q(z)| (§7.1).
- **A prior π is fixed** in Definition 25 and Theorem 26.

## Key results

- **Theorem 16 (§5.2).** Minimax risk equals the largest Bayes risk over
  priors, "a simple application of the minimax theorem"; not proved.
- **Theorem 21 and 22 (§6).** e divides e′ (e′ = f∘e for some Markov f)
  if and only if, for every action set, every strategy e′ allows e also
  allows; and (Blackwell–Sherman–Stein) if and only if e's Bayes risk is
  no larger for every action set, loss and prior. The forward half is
  proved; the converse is Theorem 26 with ε = 0.
- **Theorem 24 (§6.3).** For any Risk : M(Θ, A) → ℝ, the minimum over the
  strategies e can reach cannot rise under garbling. Mutual information
  and total variation are the examples (§6.5–6.6).
- **Definition 25 (§7).** ξ^π(e, e′) := min_{f∈M(Z,Z′)} E_{θ∼π}
  V(f∘e(θ), e′(θ)), the directed deficiency, and Ξ^π its symmetrisation.
- **Theorem 26 (Randomization Theorem, pp. 18–19).** "Fix ϵ > 0 and a
  prior π. Let e and e′ be experiments. Then, Risk^π_L(e) ≤ Risk^π_L(e′) +
  ϵ‖L‖∞ for all action sets and loss functions, if and only if
  ξ^π(e, e′) ≤ ϵ." Credited to Le Cam (1964), with "the proof from [17]",
  Torgersen's 1991 book, "with some streamlining".
  - *Reverse implication.* Take f attaining ξ^π, any rule d′ for e′, and
    d = d′∘f. Then Risk^π_L(e, d) − Risk^π_L(e′, d′) ≤ E_π V(d∘e(θ),
    d′∘e′(θ)) ‖L‖∞ ≤ E_π V(f∘e(θ), e′(θ)) ‖L‖∞ ≤ ε‖L‖∞, the middle step
    by the data processing inequality for V.
  - *Forward implication.* Fix A and d′, and let ϕ(L, d) =
    Risk^π_L(e, d) − Risk^π_L(e′, d′) − ε‖L‖∞, "affine in d and concave in
    L". The hypothesis gives sup_L min_d ϕ ≤ 0 (because d′ is at least as
    risky as e′'s best rule). By the minimax theorem "there exists a
    saddle point (L*, d*)" with min_d sup_L ϕ = sup_L min_d ϕ ≤ 0, so
    Risk^π_L(e, d*) ≤ Risk^π_L(e′, d′) + ε‖L‖∞ for all L, hence E_π
    V(d*∘e(θ), d′∘e′(θ)) ≤ ε. Taking A = Z′ and d′ the identity makes d*
    the garbling f.
- **Theorem 27 (p. 19).** Ξ^π(e, e′) = sup_L |Risk^π_L(e) −
  Risk^π_L(e′)| / ‖L‖∞, from Theorem 26 and Lemma 28.
- **Theorem 29 (pp. 19–20).** For π of full support, Ξ^π is a metric on
  experiments up to equivalence.
- **Lemma 30 (p. 20).** ξ^π as a linear programme in a stochastic matrix F
  and slacks M.

## Claims

Only a Read note may fill this in; §4 was not read, so this reading is
Skimmed. Theorem 26 is graded in prose: the forward implication is
proved, with the caveat on the saddle point below; the reverse
implication is proved for losses in [0, 1] and is wrong by a factor of 2
for signed losses.

## Concepts

- **Transition, Markov transition** — a linear map between spaces of
  measures; Markov if it sends distributions to distributions (Def. 15).
- **e divides e′** — e′ = f∘e for a Markov f (Def. 20); garbling.
- **Directed deficiency ξ^π** — the π-average, not the maximum over θ, of
  the variational distance after the best garbling (Def. 25).

## Connections

Le Cam's 1964 paper and Torgersen's 1991 book are the sources; neither is
read here, and the record holds Torgersen as [LIT-778](../literature.d/LIT-778.md), Unavailable. The ε = 0
case is Blackwell's order, read in [LIT-781](../literature.d/LIT-781.md) ([NOTE-595](NOTE-595.md)). Han's lecture
([LIT-tmp44f5w](../literature.d/LIT-tmp44f5w.md), [NOTE-tmp30fln](NOTE-tmp30fln.md)) states the uniform version and sketches its
converse. [CLAIM-381](../claims.d/CLAIM-381.md) computes the uniform directed deficiency between finite
tables as a linear programme; its programme carries the ½ that Lemma 30's
lacks.

## Bearing on the record

- **[CLAIM-488](../claims.d/CLAIM-488.md): partly.** The claim's first step lacks the converse of the
  randomization criterion for finite experiments, uniform in the unknown:
  that if, for every [0, 1]-loss problem and every rule for e′, some rule
  for e is within ε at every θ, then a single garbling f has
  max_θ V(f∘e(θ), e′(θ)) ≤ ε. Theorem 26 proves the converse for one fixed
  prior, with the deficiency averaged over θ, and its hypothesis is about
  minimum Bayes risks. That is the core of the argument, proved in full
  for finite sets. What the uniform version needs beyond it:
  1. **Apply it at every prior.** The uniform, rule-by-rule hypothesis
     implies Theorem 26's hypothesis for every π: average the per-θ
     inequality over π, then minimise. So ξ^π(e, e′) ≤ ε for every π.
  2. **Exchange the garbling and the prior.** max_π min_f E_π V(f∘e(θ),
     e′(θ)) = min_f max_θ V(f∘e(θ), e′(θ)). This is a second minimax step:
     f ranges over the compact convex set of stochastic matrices (Z, Z′
     finite), the objective is convex in f (V is convex and f∘e is linear
     in f) and linear in π, and the priors form a compact simplex (Θ
     finite). Sion's theorem gives the equality. Neither the paper nor
     the record states this step.
  3. **Restrict to [0, 1] losses**, or measure the loss by its range
     max L − min L rather than ‖L‖∞, because of the factor-2 point below.
  With those, the converse holds in [CLAIM-381](../claims.d/CLAIM-381.md)'s finite setting, and the
  easy direction closes the circle. The reading therefore supplies the
  hard step; the uniform statement is a short re-derivation away, not in
  the paper.
- No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **Fixed prior.** Every quantitative result in §7 is for a fixed π. The
  uniform deficiency of Le Cam, the one the comparison of experiments
  usually means, is not defined in the paper.
- **The factor of 2.** In the reverse implication, the step
  Risk^π_L(e, d) − Risk^π_L(e′, d′) ≤ E_π V(·, ·)‖L‖∞ holds when L takes
  values in [0, ‖L‖∞], not for signed losses, since |E_P L − E_Q L| can
  reach 2V(P, Q)‖L‖∞. A check: Θ = {0, 1}, π uniform, e′ the identity, e
  constant. Then ξ^π(e, e′) = ½. With L(θ, a) = −1 if a = θ and +1
  otherwise, ‖L‖∞ = 1, Risk^π_L(e′) = −1 and Risk^π_L(e) = 0, so the
  inequality Risk^π_L(e) ≤ Risk^π_L(e′) + ½ fails. With the 0–1 loss it
  holds with equality. Theorem 27 inherits the slip. The forward
  implication is unaffected: its proof goes through with the losses
  restricted to [0, 1] and the bound ε, and the loss it finally uses is
  an indicator. Restricted to [0, 1] losses, the theorem holds in both
  directions.
- **The saddle point.** Sion's theorem, which the paper cites through
  Komiya, gives min_d sup_L ϕ = sup_L min_d ϕ with the minimum attained,
  because the rules form a compact set; it does not give a maximising L*
  over the unbounded set of losses. The proof uses only d*, so the
  conclusion stands.
- **Lemma 30.** The printed constraints make the objective Σ |π_j E′_ij −
  π_j [FE]_ij| = 2 E_π V, and the proof's displayed step drops the
  absolute values (without them the column sums are zero). The programme
  computes 2ξ^π.

## Open questions

- Whether the record wants the uniform converse written out as its own
  CLAIM, with steps 1–3 above, which is what [CLAIM-488](../claims.d/CLAIM-488.md)'s note of
  2026-10-29 calls "a checked re-derivation".
