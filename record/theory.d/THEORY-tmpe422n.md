---
status: Proposed
promote_when: >-
  A step-by-step derivation, recorded in a promotion-audit decision file or
  found in a source the record has read, of the two steps not re-derived
  below. The first is the achievability half: superposition random coding
  with a first-stage codebook of rate above I(X; X̂₁) and conditional
  second-stage codebooks of rate above I(X; X̂₂ | X̂₁) reaches both
  distortions, by the covering lemma and its conditional form. The second
  is that the Hamming channel (49) is a stochastic matrix that degrades
  the fine optimum into the coarse one for every finite source. Numerical
  confirmation, which the record already has, cannot settle either. A
  proof covering continuous alphabets is not needed, since the title
  claims only finite ones.
title: 'For a memoryless source with finite alphabets and a per-letter distortion, a description at rate R(D₁) can be refined to distortion D₂ < D₁ at total rate R(D₂) iff some pair of rate–distortion-optimal test channels forms a Markov chain X → X̂₂ → X̂₁; the condition holds for every discrete source under Hamming distortion and fails for some three-letter sources under absolute error'
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Filed Proposed from NOTE-tmpyi9oi. The characterization is the paper's
    Theorem 2, the examples its §IV and §V-B. The converse is re-derived
    below directly from the coding definitions, without the paper's
    appeal to Ahlswede's no-excess-rate theorem, and the counterexample is
    re-derived with its printing slips corrected. The achievability half
    rests on El Gamal and Cover's cited theorem, and the Hamming channel
    was checked numerically, not derived, so the entry is not Active under
    ADR-047 v2.
tags:
- information-theory
- mathematics
date: '2026-10-20'
source:
- LIT-tmp25otd
answers:
- QUESTION-tmpproc1
summary: >-
  Equitz and Cover (1991), [LIT-tmp25otd](../literature.d/LIT-tmp25otd.md), read in [NOTE-tmpyi9oi](../notes.d/NOTE-tmpyi9oi.md). Lossless
  two-stage description is possible exactly when the coarse optimum is a
  stochastic degradation of the fine optimum. That is a Markov chain on
  test channels, not nesting of partitions, and it is an asymptotic
  block-coding statement. It does not say that optimal single-shot
  quantizers or deterministic encoders nest, and the paper's own Gaussian
  example shows they need not. It says nothing yet about the information
  bottleneck beyond a formal transfer through the KL distortion.
---
<!-- inactive-ok-file: THEORY-163 — Proposed; an open reading this bears on, nothing here rests on it -->
# THEORY-tmpe422n: For a memoryless source with finite alphabets and a per-letter distortion, a description at rate R(D₁) can be refined to distortion D₂ < D₁ at total rate R(D₂) iff some pair of rate–distortion-optimal test channels forms a Markov chain X → X̂₂ → X̂₁; the condition holds for every discrete source under Hamming distortion and fails for some three-letter sources under absolute error

## Source

Equitz and Cover (1991), *IEEE Transactions on Information Theory*
37(2):269–275, [LIT-tmp25otd](../literature.d/LIT-tmp25otd.md), read in full in [NOTE-tmpyi9oi](../notes.d/NOTE-tmpyi9oi.md) from the scan on
Cover's Stanford page. The characterization is Theorem 2, the counterexample
§IV (Gerrish's problem) and the Hamming case §V-B. The converse below is the
record's re-derivation, and is more direct than the paper's.

## What was actually shown

**Setting.** X₁, X₂, … i.i.d. ~ p(x) on a finite 𝒳. A reproduction alphabet
X̂ is finite, the distortion is d: 𝒳 × X̂ → ℝ and per-letter additive, and
R(D) = min I(X; X̂) over p(x̂|x) with E d(X, X̂) ≤ D. Refinement from D₁ to D₂
(D₁ ≥ D₂) is achievable when there are first-stage indices I ∈ [2^{nR₁}] and
addenda J ∈ [2^{n(R₂−R₁)}], with R₁ = R(D₁) and R₂ = R(D₂), that meet the two
distortions asymptotically (Definition 2).

**Converse (re-derived here).** Take codes that meet E d(Xⁿ, X̂ᵢⁿ) ≤ Dᵢ + ε.
Let X̂₁ₖ be a function of I and X̂₂ₖ a function of (I, J).

1. nR₁ ≥ H(I) ≥ I(Xⁿ; I) = Σₖ I(Xₖ; I | X^{k−1}) = Σₖ I(Xₖ; I, X^{k−1})
   ≥ Σₖ I(Xₖ; X̂₁ₖ). The equality uses Xₖ ⊥ X^{k−1}, and the last step
   is data processing. In the same way, nR₂ ≥ H(I, J) ≥ Σₖ I(Xₖ; X̂₁ₖ, X̂₂ₖ).
2. Let Q be uniform on {1, …, n} and independent of Xⁿ, and put X = X_Q,
   X̂ᵢ = X̂ᵢ_Q. Then X ~ p(x) and X ⊥ Q, so R₁ ≥ I(X; X̂₁, Q) and
   R₂ ≥ I(X; X̂₁, X̂₂, Q), with E d(X, X̂ᵢ) ≤ Dᵢ + ε.
3. By the chain rule, R(D₂) = R₂ ≥ I(X; X̂₂) + I(X; Q | X̂₂)
   + I(X; X̂₁ | X̂₂, Q). Also I(X; X̂₂) ≥ R(D₂ + ε). So
   I(X; X̂₁ | X̂₂) ≤ I(X; X̂₁, Q | X̂₂) ≤ R(D₂) − R(D₂ + ε) =: δ(ε).
   Likewise I(X; X̂ᵢ) ≤ Rᵢ = R(Dᵢ).
4. This gives a joint p_ε(x̂₁, x̂₂ | x) on finite alphabets with
   E d(X, X̂ᵢ) ≤ Dᵢ + ε, I(X; X̂ᵢ) ≤ R(Dᵢ) and I(X; X̂₁ | X̂₂) ≤ δ(ε). R(D)
   is convex and non-increasing, hence continuous for D above its minimum
   (and continuous from the right at the minimum for finite alphabets), so
   δ(ε) → 0. The conditionals form a compact set, and mutual information
   and expected distortion are continuous in them on finite alphabets. So
   a limit point p has E d ≤ Dᵢ, I(X; X̂ᵢ) ≤ R(Dᵢ), and hence
   I(X; X̂ᵢ) = R(Dᵢ) by the definition of R. It also has
   I(X; X̂₁ | X̂₂) = 0, which is the Markov chain X → X̂₂ → X̂₁.

The paper reaches the same end by citing Ahlswede's theorem that El Gamal
and Cover's multiple-descriptions region is tight without excess rate. The
argument above does not need that theorem.

**Achievability (the paper's, resting on a cited theorem).** Given optimal
channels with X → X̂₂ → X̂₁, I(X; X̂₁, X̂₂) = I(X; X̂₂) = R(D₂), so the
second stage needs only R(D₂) − R(D₁) = I(X; X̂₂ | X̂₁). The paper's
construction (§III-B) draws 2^{nR₁} first-stage codewords i.i.d. from
p(x̂₁), and under each one 2^{n(R₂−R₁)} codewords from Π p(x̂₂ | x̂₁ₖ). It
encodes by minimum distortion at each stage, and appeals to El Gamal and
Cover's theorem (with X̂₀ constant) for the rates and distortions. That
appeal is not re-derived here.

**The condition is not automatic (§IV, re-derived).** Let 𝒳 = X̂ = {1, 2, 3},
P_X = ((1−p)/2, p, (1−p)/2), d = |x − x̂|, and z = e^{R′(D)}. The middle
letter's optimal output mass, (p − z + pz + z²)/(1 − z)², is negative
between the roots of z² − (1−p)z + p. These are real iff p² − 6p + 1 > 0,
i.e. p < 3 − 2√2. In that range the optimum uses only the outer letters,
with backward channel rows ((1−p)/(1+z²), p, (1−p)z²/(1+z²)) and its mirror.
Above it, all three letters are used, with backward channel
(1/(1+z))[[1, z(1−z), z²], [z, 1−z, z], [z², z(1−z), 1]]. Take D₂ in the
two-letter range and D₁ in the upper three-letter range. If X̂₁ → X̂₂ → X,
then P_{X|X̂₁} = P_{X̂₂|X̂₁} P_{X|X̂₂}, and every row of the right side has
middle entry p. On the left, rows 1 and 2 have middle entries
z₁(1−z₁)/(1+z₁) and (1−z₁)/(1+z₁), which are equal only at z₁ = 1. But
z₁ ≤ (1−p)/(1+p) < 1. The optimal channels are unique at both points: at D₁
because [z^{|x−x̂|}] has determinant (1 − z²)² ≠ 0, and at D₂ because the
two used columns are independent. So no optimal pair is Markov, and by the
converse refinement fails. The regions were confirmed by Blahut–Arimoto
for p = 0.1 (two-letter range z ∈ (0.130, 0.770)). The paper prints the
region conditions in (34)/(36) reversed, and the lower bound in (37)
without its full factor ½; [NOTE-tmpyi9oi](../notes.d/NOTE-tmpyi9oi.md) gives the details.

**Hamming distortion (§V-B, checked, not derived).** For any finite source
and d = 1 − δ(x, x̂), the paper gives a closed-form degrading channel (49)
between the "upside-down waterfilling" optima. Here, for four random
five-letter sources and six slope pairs each, the least-squares solution
of P_{X|X̂₁} = T P_{X|X̂₂} was row-stochastic and nonnegative, with
residual below 10⁻¹⁵.

What could have failed: the converse could have needed the excess-rate
freedom of general multiple descriptions. It does not, because with both
stages at the bound every slack in step 3 is forced to zero. And the
three-letter source could have admitted a degrading channel. The constant
middle column of the two-letter backward channel rules one out.

## What this does not say

- **Not that optimal partitions nest.** The chain is between test
  channels, and X̂₁ may be a *noisy* function of X̂₂. For deterministic
  encoders the chain does reduce to refinement of partitions, since
  I(X; T₁|T₂) = H(T₁|T₂). But optimal rate–distortion test channels are
  generally stochastic.
- **Not anything single-shot.** It is a statement about long blocks. The
  paper's Fig. 1 shows that the optimal 4- and 8-level scalar quantizers
  of a Gaussian are not nested, with thresholds {0, ±0.98} against
  {0, ±0.50, ±1.05, ±1.75}, although the Gaussian is successively
  refinable.
- **Not continuous sources.** The paper also shows the Markov chains for
  the Gaussian under squared error and the Laplacian under absolute error,
  and both constructions are correct. But Theorem 2 is proved for finite
  alphabets, so those cases go beyond what this entry claims.
- **Not the information bottleneck, yet.** The IB is rate–distortion with
  reproduction alphabet Δ(Y) and distortion KL(p(y|x) ‖ q), which is
  infinite. The transfer is formal and plausible, and [NOTE-tmpyi9oi](../notes.d/NOTE-tmpyi9oi.md) sets
  out what it would need. A brute force over deterministic encoders found
  IB optima at two budgets that are incomparable partitions. That is the
  record's, and is not filed as a claim.
- **Not how much is lost.** When refinement fails, the rate penalty is not
  bounded here.

## Connections

- **[QUESTION-tmpproc1](../questions.d/QUESTION-tmpproc1.md): answers in part.** It gives the rate–distortion
  answer to the question's Markov formulation: nesting in the stochastic
  sense is exactly lossless progressive coding, and it can fail. The
  question's title asks for the stronger "a function of the finer".
- **[NOTE-676](../notes.d/NOTE-676.md).** Its nesting across the compression weight is imposed by
  the fixed tree, and is single-shot and deterministic. This entry neither
  supplies nor contradicts it.
- **[THEORY-163](THEORY-163.md).** Annealed IB category hierarchies can now be tested for
  the Markov condition between successive β, rather than read as nested
  from their bifurcations.
