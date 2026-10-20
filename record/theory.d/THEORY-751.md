---
number: 751
status: Active
formerly:
- THEORY-tmpe422n
title: 'For a memoryless source with finite alphabets and a per-letter distortion, a description at rate R(D₁) can be refined to distortion D₂ < D₁ at total rate R(D₂) iff some pair of rate–distortion-optimal test channels forms a Markov chain X → X̂₂ → X̂₁; the condition holds for every discrete source under Hamming distortion and fails for some three-letter sources under absolute error'
version: 2
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Filed Proposed from NOTE-988. The characterization is the paper's
    Theorem 2, the examples its §IV and §V-B. The converse is re-derived
    below directly from the coding definitions, without the paper's
    appeal to Ahlswede's no-excess-rate theorem, and the counterexample is
    re-derived with its printing slips corrected. The achievability half
    rests on El Gamal and Cover's cited theorem, and the Hamming channel
    was checked numerically, not derived, so the entry is not Active under
    ADR-047 v2.
- version: 2
  date: '2026-10-20'
  note: >-
    Promoted with its title unchanged, carrying out the promotion audit's
    decision for THEORY-751 (batch 060, ADR-047 v2). The two steps the
    entry lacked are re-derived in the note below: achievability by
    superposition coding, from the covering lemma and its conditional
    form, and a degrading channel for the Hamming optima of every finite
    source, in closed form from the optimality conditions.
tags:
- information-theory
- mathematics
date: '2026-10-20'
source:
- LIT-1238
answers:
- QUESTION-220
summary: >-
  Equitz and Cover (1991), [LIT-1238](../literature.d/LIT-1238.md), read in [NOTE-988](../notes.d/NOTE-988.md), with every step
  re-derived by 2026-10-20. Lossless
  two-stage description is possible exactly when the coarse optimum is a
  stochastic degradation of the fine optimum. That is a Markov chain on
  test channels, not nesting of partitions, and it is an asymptotic
  block-coding statement. It does not say that optimal single-shot
  quantizers or deterministic encoders nest, and the paper's own Gaussian
  example shows they need not. It says nothing yet about the information
  bottleneck beyond a formal transfer through the KL distortion.
---
<!-- inactive-ok-file: THEORY-163 — Proposed; an open reading this bears on, nothing here rests on it -->
# THEORY-751: For a memoryless source with finite alphabets and a per-letter distortion, a description at rate R(D₁) can be refined to distortion D₂ < D₁ at total rate R(D₂) iff some pair of rate–distortion-optimal test channels forms a Markov chain X → X̂₂ → X̂₁; the condition holds for every discrete source under Hamming distortion and fails for some three-letter sources under absolute error

## Source

Equitz and Cover (1991), *IEEE Transactions on Information Theory*
37(2):269–275, [LIT-1238](../literature.d/LIT-1238.md), read in full in [NOTE-988](../notes.d/NOTE-988.md) from the scan on
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

**Achievability (the paper's, resting on a cited theorem; re-derived in the note of 2026-10-20).** Given optimal
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
without its full factor ½; [NOTE-988](../notes.d/NOTE-988.md) gives the details.

**Hamming distortion (§V-B, checked here; derived in the note of 2026-10-20).** For any finite source
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
  infinite. The transfer is formal and plausible, and [NOTE-988](../notes.d/NOTE-988.md) sets
  out what it would need. A brute force over deterministic encoders found
  IB optima at two budgets that are incomparable partitions. That is the
  record's, and is not filed as a claim.
- **Not how much is lost.** When refinement fails, the rate penalty is not
  bounded here.

## Connections

- **[QUESTION-220](../questions.d/QUESTION-220.md): answers in part.** It gives the rate–distortion
  answer to the question's Markov formulation: nesting in the stochastic
  sense is exactly lossless progressive coding, and it can fail. The
  question's title asks for the stronger "a function of the finer".
- **[NOTE-676](../notes.d/NOTE-676.md).** Its nesting across the compression weight is imposed by
  the fixed tree, and is single-shot and deterministic. This entry neither
  supplies nor contradicts it.
- **[THEORY-163](THEORY-163.md).** Annealed IB category hierarchies can now be tested for
  the Markov condition between successive β, rather than read as nested
  from their bifurcations.

## Note of 2026-10-20: achievability and the Hamming channel, re-derived

The promotion audit (batch 060) re-derived the two steps above that rested
on a citation or a numerical check.

**Achievability.** Fix optimal test channels with X → X̂₂ → X̂₁, so that
I(X; X̂₁, X̂₂) = I(X; X̂₂) = R(D₂), and let δ > 0.

1. Draw 2^{nR₁} first-stage words X̂₁ⁿ(i) i.i.d. from Π p(x̂₁), with
   R₁ = R(D₁) + δ. Under each, draw 2^{n(R₂−R₁)} words X̂₂ⁿ(i, j) from
   Π_k p(x̂₂ | x̂₁ₖ(i)), with R₂ − R₁ = I(X; X̂₂ | X̂₁) + δ.
2. For typical xⁿ, each X̂₁ⁿ(i) is jointly typical with xⁿ with probability
   at least 2^{−n(I(X;X̂₁)+δ′)}. So the chance that none is typical is at
   most exp(−2^{n(δ−δ′)}), which tends to 0 (the covering lemma).
3. Given a jointly typical (xⁿ, x̂₁ⁿ), each X̂₂ⁿ(i, j) is jointly typical with
   both with probability at least 2^{−n(I(X;X̂₂|X̂₁)+δ′)}. The same bound
   applies at rate R₂ − R₁ (the conditional covering lemma).
4. On joint typicality the distortions are within ε·d_max of E d(X, X̂ᵢ) ≤ Dᵢ.
   The total rate is I(X; X̂₁) + I(X; X̂₂ | X̂₁) + 2δ = R(D₂) + 2δ. Letting δ
   and ε go to 0 puts (R(D₁), R(D₂)) in the closure of the achievable set,
   which is the paper's Definition 2. With the converse above, the iff
   holds.

**Hamming distortion, for every finite source.** Take d = 1 − [x = x̂] and
D strictly between 0 and D_max = 1 − max p.

1. For a level θ ∈ (0, max p), put a(x) = min(p(x), θ),
   κ = 1 − Σ a > 0 and U = {x : p(x) > θ}. Then set
   q(x̂) = (p(x̂) − θ)/κ on U and 0 off it, and take the backward channel
   P(x | x̂) = a(x) + κ[x = x̂]. Each row sums to 1, Σ q = 1, and
   Σ q(x̂)P(x | x̂) = a(x) + κq(x) = p(x).
2. Its distortion is D = 1 − θ − κ = (|U| − 1)θ + P(Uᶜ). That is continuous
   and increasing in θ, so every D in range has a θ.
3. The candidate is optimal. With z = θ/(θ + κ) and λ(x)p(x) = a(x)/z, the
   sufficient condition for a minimum of I (Csiszár; Gallager's Theorem
   9.4.1) is c(x̂) = Σ_x λ(x)p(x)z^{d(x,x̂)} ≤ 1, with equality where q > 0.
   Here c(x̂) = 1 − κ + (κ/θ)a(x̂). That equals 1 on U, where a = θ, and is
   at most 1 off U, where a = p ≤ θ. This is upside-down waterfilling.
4. For D₂ < D₁, the levels satisfy θ₂ < θ₁ and U₁ ⊆ U₂. Put
   T(x̂₂ | x̂₁) = t[x̂₂ = x̂₁] + w(x̂₂), with t = κ₁/κ₂ and w = (a₁ − a₂)/κ₂.
   Here w ≥ 0, w vanishes off U₂, t ∈ (0, 1] and Σw = 1 − t. So T is a
   stochastic matrix.
5. Σ_{x̂₂} T(x̂₂ | x̂₁)P₂(x | x̂₂) = a₂ + κ₁[x = x̂₁] + (a₁ − a₂) = P₁(x | x̂₁),
   and q₁T = q₂. So q₁(x̂₁)T(x̂₂ | x̂₁)P₂(x | x̂₂) is a joint distribution with
   the two optima as its marginals and X → X̂₂ → X̂₁. At D₁ = D_max the
   coarse stage is constant, and at D₂ = 0 the fine stage is X. Both are
   trivially Markov.

**Numerical check of the derivation.** For 38 random sources on three to six
letters, Blahut–Arimoto at a random slope matched the θ construction at the
same distortion, with |ΔR| ≤ 2.2 × 10⁻¹⁵. For 30 random sources and level
pairs, T was nonnegative and stochastic, with ‖TP₂ − P₁‖ and ‖q₁T − q₂‖ at
most 9 × 10⁻¹⁵. This T was derived here and not compared symbol by symbol
with the paper's (49).
