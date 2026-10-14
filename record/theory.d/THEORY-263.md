---
number: 263
status: Proposed
formerly:
- THEORY-tmpgdeej
promote_when: >-
  A check of Theorem 1's proof and of the claim that the rate log
  dP_{W|S}/dP(W) satisfies Theorem 2's condition at zero distortion,
  together with a second source deriving a PAC-Bayes bound from a
  variable-rate covering argument outside finite alphabets. The account
  is refuted by an algorithm and prior for which the variable-rate bound
  with that rate fails where the disintegrated PAC-Bayes bound holds, or
  the reverse. What cannot settle it: whether either bound is tight or
  non-vacuous for networks, which is a different question.
title: "A coding rate that varies with the realised sample and output makes rate-distortion generalisation bounds data-dependent, and with the rate set to the pointwise information density log dP_{W|S}/dP(W) against a fixed prior the bound is the disintegrated PAC-Bayes bound"
version: 1
tags:
- learning-theory
- information-theory
date: '2026-10-14'
source:
- LIT-233
summary: >-
  Sefidgaran & Zaidi (2023; IEEE Trans. Inf. Theory 2024), [LIT-233](../literature.d/LIT-233.md), read
  in [NOTE-806](../notes.d/NOTE-806.md). Theorem 1: with a sample-dependent rate R_{S,W},
  gen ≤ √(4σ²(R_{S,W} + log(√(2n)/δ))/(2n−1) + ε). With R_{S,W} =
  log dP_{W|S}/dP(W) the coding condition holds at ε = 0 and the bound is
  the disintegrated PAC-Bayes bound. The general Theorems 3–5 recover
  Rivasplata et al.'s PAC-Bayes bound and Xu–Raginsky's. The coding
  construction is proved for finite alphabets only. The general proofs
  are change of measure. The rate is a Shannon code-length difference
  against a prior, not Kolmogorov complexity.
---
<!-- inactive-ok-file: THEORY-238 THEORY-248 THEORY-266 — Proposed; the account of a related bound for representations, and the two accounts filed beside this one today, cited for context -->

# THEORY-263: A coding rate that varies with the realised sample and output makes rate-distortion generalisation bounds data-dependent, and with the rate set to the pointwise information density log dP_{W|S}/dP(W) against a fixed prior the bound is the disintegrated PAC-Bayes bound

## Source

Sefidgaran & Zaidi (2023), [LIT-233](../literature.d/LIT-233.md), read in full in [NOTE-806](../notes.d/NOTE-806.md):
Definition 2, Theorems 1–5, §IV-A and §IV-B, Proposition 1, and proofs
E-A to E-F, E-J and E-K.

## What was actually shown

**Variable-size compressibility.** Take m independent experiments
(S_i, W_i). A fixed-rate scheme ([LIT-236](../literature.d/LIT-236.md)) may use a book of e^{mR}
candidate output blocks for every block. Here only the first
e^{Σ_i R_{S_i,W_i}} entries may be used for a given block, so the number
of codewords spent depends on the realised samples and outputs
(Def. 2). The distortion is on squared generalisation error (eq. 10).

**The bound.** If A is compressible in this sense and the loss is
σ-subgaussian, then with probability ≥ 1 − δ,

gen(S, W) ≤ √(4σ²(R_{S,W} + log(√(2n)/δ))/(2n − 1) + ε)

(Theorem 1). The proof weights the j-th book entry by 1/j, so the union
bound costs a harmonic sum, about mR_max. Variable size therefore costs
only a vanishing term.

**PAC-Bayes as the lossless case.** For finite S × W, Theorem 2 gives a
sufficient condition on R_{S,W} for compressibility. The rate R_{S,W} :=
log (dP_{W|S}/dP)(W), for a fixed prior P, satisfies it at ε = 0, and the
resulting bound "recovers the PAC-Bayes bound of [Catoni],
[Blanchard–Fleuret]", the disintegrated form of McAllester's (§II). In
general spaces, Theorem 4 with λ = 1 and a fixed, possibly
data-dependent prior gives Rivasplata et al.'s Theorem 1.ii (eq. 29).
Clerico et al. observe that this contains most PAC-Bayes bounds. Theorem
5 gives Xu–Raginsky ([LIT-347](../literature.d/LIT-347.md)). §IV-A gives [LIT-236](../literature.d/LIT-236.md)'s Theorem 10.

**What the rate is.** log dP_{W|S}/dP(W) is the number of nats by which
coding the output with the prior costs more than coding it with the
algorithm's posterior. It is a Shannon code-length difference against a
chosen prior, as in Blum and Langford's PAC-MDL.

What could have failed: a variable-size book could have cost a union
bound over its maximal size, which would give back the data-independent
rate. The 1/j weighting is what keeps the cost at the realised rate.

## What this does not say

- **Not that compression is the mechanism outside finite alphabets.**
  The coding construction (Theorem 2) is proved only for finite S × W.
  The general Theorems 3–5 are change-of-measure inequalities, Lemma 1
  plus Donsker–Varadhan, to which the paper gives a compression reading.
- **Not that every bound in the family is data-dependent.** The
  conditions range over a KL ball around the unknown P_{S,W}. A bound is
  computable from one sample only when the chosen rate or prior is, as in
  the PAC-Bayes case. The fast-rate constant of §IV-A and Theorem 6
  depend on μ.
- **Not Kolmogorov complexity or MDL in the algorithmic sense.** The rate
  is relative to a prior the analyst picks. No bound is stated in terms
  of program length, and no link to minimal sufficient statistics is
  made.
- **Not that the unified bounds are tighter than their originals.** They
  are recovered, "possibly" improved. The only new bound shown finite
  where its predecessor is infinite is the lossy PAC-Bayes bound of
  Proposition 1, on a Gaussian-mean example.
- **Not a numerical bound for any network.** None is computed.

## Connections

- **[THEORY-248](THEORY-248.md) ([LIT-236](../literature.d/LIT-236.md))** holds the fixed-rate, data-independent
  bound this generalises.
- **[THEORY-028](THEORY-028.md).** Its Xu–Raginsky half is the lossless, in-expectation
  case of Theorem 5 here.
- **[THEORY-266](THEORY-266.md)** holds this paper's trajectory bound, which is
  data-dependent except for a coupling term.
- **[THEORY-238](THEORY-238.md) ([LIT-245](../literature.d/LIT-245.md)).** The same group applies a block-coding
  argument to an encoder's latents, and this paper names that work as an
  extension.
