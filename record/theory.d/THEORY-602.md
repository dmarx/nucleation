---
number: 602
status: Active
formerly:
- THEORY-tmpotoox
title: "An ergodic source's entropy is the least average rate at which it can be encoded, a noisy channel has a capacity below which any rate can be sent with arbitrarily small error and above which the equivocation cannot fall below the excess, and a source can be reproduced at a given fidelity over a channel exactly when its rate for that fidelity does not exceed the capacity; Shannon rests the justification of entropy on these theorems, not on the axioms that single out −Σ p log p"
version: 1
tags:
- information-theory
date: '2026-10-16'
source:
- LIT-764
summary: >-
  Shannon (1948), [LIT-764](../literature.d/LIT-764.md), read in [NOTE-591](../notes.d/NOTE-591.md): Parts I–II closely, Parts
  III–V and the later appendices skimmed for their theorem statements.
  The noisy-channel achievability proof is a random-coding sketch at the
  typical-set level, not a full ε–δ argument, and the strong converse is
  not proved; the theorems themselves were later made rigorous. Shannon
  says the uniqueness theorem for H is "in no way necessary" to the
  theory. The theorems assume ergodic, finite-state sources and channels
  and say nothing about meaning.
supports:
- CLAIM-050
---

<!-- inactive-ok-file: LIT-317 — Unavailable; named for what it adds to this paper, not leaned on -->

# THEORY-602: An ergodic source's entropy is the least average rate at which it can be encoded, a noisy channel has a capacity below which any rate can be sent with arbitrarily small error and above which the equivocation cannot fall below the excess, and a source can be reproduced at a given fidelity over a channel exactly when its rate for that fidelity does not exceed the capacity; Shannon rests the justification of entropy on these theorems, not on the axioms that single out −Σ p log p

## Source

Shannon (1948), "A Mathematical Theory of Communication", *Bell System
Technical Journal* 27, [LIT-764](../literature.d/LIT-764.md), read in [NOTE-591](../notes.d/NOTE-591.md) from the reprint "with
corrections". Section and theorem numbers are the reprint's. The
continuous parts (§§18–29) were skimmed for their statements.

## What was actually shown

**Typical sequences (Theorems 3–4).** For an ergodic finite-state source
of entropy H, long sequences split into a set of total probability below
ε and a set whose members have log(1/p)/N within δ of H; the number of
most probable sequences needed to reach probability q grows as 2^{HN}.

**Noiseless coding (Theorem 9).** A source of H bits per symbol can be
sent over a channel of capacity C at C/H − ε symbols per second, and not
faster than C/H.

**Noisy coding (Theorem 11).** With R = H(x) − H_y(x) and C = max R, if
H ≤ C there is a code with arbitrarily small error frequency; if H > C
the equivocation can be brought to H − C + ε and no lower. The proof
averages the error over random codes and notes that some code does at
least as well. Worked example: 1000 binary symbols per second with 1%
errors carry about 919 bits per second, not 990.

**Equivocation is exact (Theorem 10).** H_y(x) is exactly the capacity a
correction channel needs.

**Fidelity (Theorem 21, skimmed).** A source with rate R₁ at fidelity v₁,
R₁ the minimum rate over joint distributions meeting the fidelity, can be
sent at that fidelity iff R₁ ≤ C. For white noise with power P against N
in band W, C = W log((P + N)/N) (Theorem 17).

**The axioms (Theorem 2, §6).** The only H continuous in the p_i,
increasing in n for equal probabilities and additive over successive
choices is −K Σ p_i log p_i. Shannon says the theorem "and the assumptions
required for its proof, are in no way necessary for the present theory",
and that the definitions' justification "will reside in their
implications".

What could have come out otherwise: reliable transmission could have
required the rate to fall to zero as the error requirement tightened.
The redundancy needed is a fixed fraction, paid once.

## What this does not say

- **That the proofs are complete by modern standards.** Theorem 11's
  achievability is stated in terms of "about" and "small", and the strong
  converse is not proved ([NOTE-591](../notes.d/NOTE-591.md), Limitations).
- **How to build good codes.** Apart from Hamming's (§17), no
  construction approaching capacity is given, and long block delays are
  generally needed.
- **Anything about meaning.** Semantic aspects are set aside in the
  Introduction as "irrelevant to the engineering problem".
- **That "relative entropy" is the KL divergence.** Here it is the ratio
  of a source's entropy to the maximum on its alphabet.
- **That the axioms show no other quantity can measure information.**
  Shannon offers them as plausibility only. An argument that leans on
  them alone leans on what he disclaimed.
- **That continuous entropy is coordinate-free.** It is not (§20); rates
  and capacities, as differences, are.

## Connections

- Baudot & Bennequin's cohomological characterisation ([LIT-053](../literature.d/LIT-053.md),
  [THEORY-479](THEORY-479.md)) is a second uniqueness result for entropy, needing only
  measurability. Like Theorem 2, it does not replace the coding theorems
  as the justification.
- The I–MMSE identity ([THEORY-617](THEORY-617.md)) reads Gaussian-channel mutual
  information as accumulated estimation error.
- [CLAIM-050](../claims.d/CLAIM-050.md) takes rate–distortion from this paper. The information
  bottleneck ([LIT-338](../literature.d/LIT-338.md)) inherits Part V's form, a minimum rate over joint
  distributions meeting a fidelity constraint, and [THEORY-161](THEORY-161.md) holds the
  semantic rate–distortion frameworks' limits.
- Shannon 1949 ([LIT-317](../literature.d/LIT-317.md)), which the record credits with the sampling
  theorem and the capacity formula, adds their proofs; both statements
  first appear here ([NOTE-591](../notes.d/NOTE-591.md)).
