---
number: 277
status: Proposed
formerly:
- THEORY-tmppce05
promote_when: >-
  An independent derivation of Theorem IV.8 of LIT-239, or a published
  restatement with its own proof, such as the later algorithmic-statistics
  surveys by Vereshchagin and Shen, read here. The record has read the
  proof once and checked its counting, but not every constant. It is
  refuted by a string x and a bound α for which some set of complexity at
  most α + O(log n) minimises two-part length and yet has randomness
  deficiency more than c log n above β_x(α), for every constant c. What
  cannot settle it is a practical MDL procedure that works or fails on
  parametric families. Those are not the complexity-bounded classes the
  theorem is about, and the authors say the result does not transfer
  directly.
title: 'For individual data, at every bound on model complexity, the model with the shortest two-part code is, to within O(log n), the best-fitting model in randomness deficiency, although the fit itself cannot be computed or approximated'
version: 2
history:
- version: 2
  date: '2026-10-30'
  note: >-
    The twenty-fourth status review, as second checker under ADR-065 §5.
    The file's re-derivation covers only the easy direction of Theorem
    IV.8. The converse rests on Lemma C.4, which the file and NOTE-787
    record only as "the counting checks out", and the promotion audit of
    2026-10-19 found that its covering construction did not close. A
    re-derivation of Lemma C.4 by a different covering argument is
    written out in the note of 2026-10-30. It has had one checker, so it
    does not yet meet §5, and the computability clause (Theorems D.2 and
    D.6) is not re-derived at all. The title, status and promote_when are
    unchanged.
tags:
- learning-theory
- information-theory
- mathematics
date: '2026-10-14'
source:
- LIT-239
- LIT-224
summary: >-
  Vereshchagin & Vitányi (2002/2004), [LIT-239](../literature.d/LIT-239.md), read in [NOTE-787](../notes.d/NOTE-787.md),
  Theorem IV.8: β_x(α) + K(x) and λ_x(α) agree to within O(log n) for a
  string of length n. Every set minimising K(S) + log |S| at complexity α
  is within O(log n) of the best fit there. h_x and λ_x are upper
  semicomputable, while β_x is not semicomputable. Restated by Grünwald &
  Vitányi, [LIT-224](../literature.d/LIT-224.md), §6.2. Finite-set models; computable distributions at
  O(log n) cost. It says nothing at the (k/2) log n scale of parametric
  model selection, and nothing about K(A) + K(x | A).
---
<!-- inactive-ok-file: THEORY-036 THEORY-087 — Proposed; the companion theories filed today and the entries named under Connections -->

# THEORY-277: For individual data, at every bound on model complexity, the model with the shortest two-part code is, to within O(log n), the best-fitting model in randomness deficiency, although the fit itself cannot be computed or approximated

## Source

Vereshchagin & Vitányi (arXiv 2002; IEEE Trans. Inf. Theory 2004),
[LIT-239](../literature.d/LIT-239.md), read in [NOTE-787](../notes.d/NOTE-787.md). The pointers are §§II–V, Lemma IV.2,
Theorems IV.4, IV.8 and IV.11, Remark IV.10, Lemma C.4, Claim C.5,
Appendix B and Theorems D.1–D.6. Restated without proof by Grünwald &
Vitányi, [LIT-224](../literature.d/LIT-224.md) §6.2, read in [NOTE-776](../notes.d/NOTE-776.md).

## What was actually shown

**Setting.** One finite string x, of length n and complexity K(x) = k.
Models are finite sets S ∋ x. Three functions of a complexity bound α:

- h_x(α) = min{log |S| : K(S) ≤ α}, Kolmogorov's structure function, or
  constrained maximum likelihood;
- λ_x(α) = min{K(S) + log |S| : K(S) ≤ α}, the constrained two-part MDL
  length;
- β_x(α) = min{log |S| − K(x | S) : K(S) ≤ α}, the best achievable
  randomness deficiency, or best fit.

Small deficiency means x has every simple property that most members of S
have (Lemma II.3).

**The theorem (IV.8).** β_x(α) + k and λ_x(α) are within O(log n) of each
other in argument and value, and so is h_x(α) + α by Lemma IV.2. One
direction is immediate from δ(x | A) = Λ(A) − K(A | x*) − k + O(1). The
other rests on Lemma C.4. For every A ∋ x there is an S ∋ x of the same
size with K(S) ≤ K(A) − K(A | x) + O(log Λ(A)). Its proof is a counting
argument over enumerated sets, and [NOTE-787](../notes.d/NOTE-787.md) checked the counting.
Remark IV.10 states the practical form. Every set of complexity at most
α + O(log n) that minimises two-part length has deficiency at most
β_x(α) + O(log n).

**What could have come out otherwise.** Before the paper, only
β_x(α) ≤ h_x(α) + α − K(x) + O(1) was known. Theorem IV.4 shows that
λ_x(α) ≫ K(x) happens for some (x, α). At those points nothing forces a
small set to be a typical one, and the theorem says it is anyway.

**The asymmetry.** The converse fails. A best-fitting set need not
minimise code length. In the counterexample, S₁ = {0,1}ⁿ ∪ {y} has
optimal fit for random x but two-part length 3n/2 against λ_x = n
(Remark IV.10). The two coincide only at "critical" α, where λ_x is still
falling (Theorem IV.11).

**Computability.** h_x and λ_x, and their witnesses, can be approximated
from above by dovetailing (§VIII). β_x cannot be approximated from below
within |x|/3 or from above within |x|/log⁴ |x| (Theorem D.6). Given x and
K(x), no algorithm approximates λ_x within |x|/(10 log |x|) or finds the
minimal sufficient statistic (Theorem D.2, Corollary D.3). So the fit is
reached by minimising code length, a quantity that can be searched,
although the fit itself cannot be measured.

## What this does not say

- **Not that practical MDL selects best-fitting models.** The models are
  complexity-bounded classes of finite sets, or computable distributions
  with K(P) ≤ n + O(log n) at O(log n) extra cost (Appendix B). The
  authors call parametric families "partially poorer and partially richer"
  and say the results "cannot be directly transplanted to the traditional
  setting" (§IV-D).
- **Not anything at the scale of parametric model selection.** The
  precision is O(log n). The (k/2) log n penalty that separates
  k-parameter models in BIC or NML ([THEORY-087](THEORY-087.md), [LIT-238](../literature.d/LIT-238.md)) lies inside the
  error term.
- **Not that minimising K(A) + K(x | A) works.** Only the worst-case data
  code log |S| (or −log P(x)) carries the guarantee. §V-B(iii) gives
  examples where the "ultimate compression" form picks a model of
  deficiency n/2 against a best of n/4. This bears on the ideal MDL of
  Vitányi & Li ([LIT-225](../literature.d/LIT-225.md)), filed as [THEORY-259](THEORY-259.md).
- **Not that best-fitting models are found in finite time.** The
  dovetailed MDL search converges at an unknown time. Before that it
  carries only the bound δ(x | L_t) + K(x) ≤ |p_t| + log |S_t| + O(1).
- **Not that the minimal sufficient statistic is unique or a canonical
  boundary.** At non-critical α, independent sets witness the same λ_x.
  The minimal sufficient statistic is defined to logarithmic precision and
  cannot be computed.
- **Not that most data have simple models.** Non-stochastic strings,
  whose structure function stays above the sufficiency line until α ≈ K(x),
  exist for every length and complexity (Corollary IV.9). The paper gives
  existence, not frequency.

## Connections

- **[THEORY-244](THEORY-244.md)** relates the expected structure function to Shannon's
  distortion-rate function ([LIT-224](../literature.d/LIT-224.md), Theorem 6.27). This theory is the
  individual-data statement that one averages.
- **[THEORY-259](THEORY-259.md)** is the Bayesian route to the same two-part code, and
  holds only for data random for the hypothesis. This theory needs no
  such condition: it holds for every x, and the deficiency it controls is
  the amount by which x fails that condition.
- **[CLAIM-152](../claims.d/CLAIM-152.md).** The algorithmic sufficient statistic has no target
  variable. It is sufficient for x itself, relative to the reference
  machine. That is a qualification of "any individuation built on
  sufficiency", and it does not give a unique boundary either (above).
- **[THEORY-036](THEORY-036.md).** The split of a shortest description into model bits and
  noise bits is a formal version of Dennett's "description more efficient
  than the bit map" that separates pattern from noise. Neither [LIT-239](../literature.d/LIT-239.md)
  nor [LIT-224](../literature.d/LIT-224.md) cites Dennett, and the link is the record's.

## Note of 2026-10-30: a re-derivation of Lemma C.4, awaiting a second checker

The second check at the status review (ADR-065 §5) followed what the file
records and found one direction written out and the other only cited.
Throughout, K is prefix complexity, A ⊆ {0,1}ⁿ (restricting a model to
strings of x's length costs O(log n)), Λ(A) = K(A) + log |A| and
δ(x | A) = log |A| − K(x | A).

1. **The easy direction holds.** Symmetry of information gives K(A) +
K(x | A*) = K(x) + K(A | x*) + O(1), and K(x | A) ≥ K(x | A*) − O(1). So
δ(x | A) ≤ Λ(A) − K(x) − K(A | x*) + O(1) ≤ Λ(A) − K(x) + O(1). Applied to
a set witnessing λ_x(α), β_x(α) + K(x) ≤ λ_x(α) + O(1).

2. **The converse needs Lemma C.4.** For every A ∋ x there should be an
S ∋ x, with ⌈log |S|⌉ = ⌈log |A|⌉, such that K(S) ≤ K(A) − K(A | x) +
O(log Λ(A)). Chopping the enumerated strings into blocks in the order
they qualify does not prove it, because the block that x lands in need not
ever fill. That is the step the audit of 2026-10-19 could not close.

3. **The lemma, by an online cover.** Put k = K(A), m = ⌈log |A|⌉ and
l = K(A | x). Let L list, in enumeration order, the sets B ⊆ {0,1}ⁿ with
K(B) ≤ k and ⌈log |B|⌉ = m; there are fewer than 2^(k+1) of them. Given x
together with k, m and n, A is fixed by its place among the members of L
that contain x. So x lies in at least 2^(l − c log Λ(A)) of them. Put
2t = 2^(l − c log Λ(A)). If 2t < n + 2, then l = O(log Λ(A) + log n) and
S = A already meets the bound, so assume 2t ≥ n + 2.

4. **A finite game.** An adversary presents up to 2^(k+1) subsets of
{0,1}ⁿ of size at most 2^m. After each, the chooser may add that set to
its cover. The chooser wins if, at every moment, every string already in
2t presented sets is covered, and the cover never exceeds
Q = 2^(k+2) p sets, where p = (n + 2)/(2t). Choosing each presented set
with probability p wins with positive probability. A string in 2t
presented sets is uncovered with probability at most (1 − p)^(2t) <
e^−(n+2), so by a union bound over the 2ⁿ strings the probability that any
is uncovered is below 1/2. By Markov's inequality the probability that
the cover exceeds Q is at most 1/2. The game is finite, so it is
determined (Zermelo). An adversary with a winning strategy would win
against every deterministic chooser, and so with probability 1 against
the random one. That contradicts the above, so the chooser has a winning
strategy, and an exhaustive search finds it from (n, m, k, t).

5. **The covering set.** Run that strategy against the enumeration of L.
Once x has appeared in 2t sets, which happens at a finite stage, some chosen
set S covers it, and S was fixed when it was chosen. S is a member of L,
so ⌈log |S|⌉ = m. It is named by (n, m, k, t) and its place among the
chosen sets. Hence K(S) ≤ log Q + O(log Λ(A) + log n) = k − l + O(log
Λ(A) + log n).

6. **The converse.** Take A witnessing β_x(α), and S from step 5. Then
K(S) ≤ α + O(log n), and Λ(S) ≤ K(A) − K(A | x) + log |A| + O(log n). By
step 1's identity, K(A) − K(A | x) ≤ K(x) − K(x | A) + O(log n). So Λ(S) ≤
K(x) + β_x(α) + O(log n), that is, λ_x(α + O(log n)) ≤ β_x(α) + K(x) +
O(log n). Together with step 1 this is Theorem IV.8, and Remark IV.10
follows: a set of complexity at most α + O(log n) that minimises Λ has
δ ≤ λ_x(α + O(log n)) − K(x) + O(1) ≤ β_x(α) + O(log n).

A script (numpy, in the session's scratchpad, s277_cover.py) simulated
the game of step 4, with n = 10, m = 4, 2^(k+1) = 512 sets and 2t = 64,
against randomized adversaries with a heavy core and a planted string.
The random chooser won all 300 plays, with covers of 40 to 108 sets
against the bound of 192. As a control, the chooser at p/8 lost 83 of
300 plays. A second control showed the naive chopping's block containing
the planted string still unfilled when the adversary stopped, in all 300
plays. The script checks only the combinatorics; complexity is not
computable.

## Note of 2026-10-30: what holds it back

Lemma C.4's re-derivation above has had one checker, and ADR-065 §5 needs
a second. The title's last clause, that the fit cannot be computed or
approximated, rests on Theorems D.2 and D.6, which no one has
re-derived. Once a second checker confirms steps 3 to 6, the entry can be
narrowed to Theorem IV.8 and Remark IV.10 and promoted. The computability
clause would then go to a Proposed THEORY that extends it (ADR-047 kind 1).

If a second checker confirms steps 3 to 6, the narrowed title would be: "For a string x of length n and every complexity bound α, a finite set of complexity at most α + O(log n) that minimises two-part code length has randomness deficiency within O(log n) of the best achievable at complexity α; the minimal two-part code length and the best fit plus K(x) agree to within O(log n) in argument and value". Until then the title above stands.
