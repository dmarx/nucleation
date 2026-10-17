---
status: Active
title: "Directed information from an input sequence to an output sequence, the sum over time of the information the inputs up to now carry about the current output given the past outputs, is at most their mutual information and equal to it when the channel is used without feedback; in a causal system it bounds what the output reveals about the source, so feedback cannot raise a memoryless channel's capacity; and the usual definition of a memoryless channel holds only without feedback"
version: 1
tags:
- information-theory
- causality
date: '2026-10-17'
source:
- LIT-tmpcmyem
summary: >-
  Massey (1990), [LIT-tmpcmyem](../literature.d/LIT-tmpcmyem.md), read in full in [NOTE-tmpik4nc](../notes.d/NOTE-tmpik4nc.md) from the
  author's preprint. Three short theorems, all checked; the feedback
  inequality also checked numerically. "Causal" is Massey's factorization
  condition, not intervention. That directed information is full-history
  transfer entropy plus instantaneous terms is the record's derivation.
---

# THEORY-tmppkvwa: Directed information from an input sequence to an output sequence, the sum over time of the information the inputs up to now carry about the current output given the past outputs, is at most their mutual information and equal to it when the channel is used without feedback; in a causal system it bounds what the output reveals about the source, so feedback cannot raise a memoryless channel's capacity; and the usual definition of a memoryless channel holds only without feedback

## Source

Massey (1990), "Causality, Feedback and Directed Information", Proc.
ISITA-90, [LIT-tmpcmyem](../literature.d/LIT-tmpcmyem.md), read in full in [NOTE-tmpik4nc](../notes.d/NOTE-tmpik4nc.md) from the author's
preprint. The proceedings version was not compared.

## What was actually shown

**Definitions.** A discrete channel is memoryless if P(y_n | x^n y^{n−1})
= P(y_n | x_n), and used without feedback if P(x_n | x^{n−1} y^{n−1}) =
P(x_n | x^{n−1}). Together they give the textbook
P(y^N | x^N) = Π P(y_n | x_n), which noiseless feedback violates. Directed
information is I(X^N → Y^N) = Σ_n I(X^n; Y_n | Y^{n−1}).

**Theorem 1.** I(X^N → Y^N) ≤ I(X^N; Y^N), with equality without
feedback. With noiseless feedback over a binary symmetric channel
(crossover 0.1), N = 3, the reading found I(X;Y) = 1.469 bits against
I(X → Y) = 0.531: mutual information counts the fed-back copies.

**Theorem 2.** For a DMC, I(X^N → Y^N) ≤ Σ I(X_n; Y_n), with equality iff
the outputs are independent.

**Theorem 3.** In a causal system, where a channel sees a source only
through its own inputs and outputs, I(U^K; Y^N) ≤ I(X^N → Y^N). With
Theorem 2, feedback cannot raise a DMC's capacity.

What could have come out otherwise: directed information could have
coincided with mutual information under feedback. The numerical case
shows it does not.

## What this does not say

- **That directed information is causal in the interventional sense.**
  Massey's causal system is a factorization condition about how
  information may enter a channel. Nothing is set or perturbed.
- **That directed information is transfer entropy.** It conditions on the
  current input X_n. By the chain rule it is the sum of full-history
  transfer entropies plus the sum of instantaneous terms
  I(X_n; Y_n | X^{n−1}, Y^{n−1}); the record checked this on a random
  binary process ([NOTE-tmpik4nc](../notes.d/NOTE-tmpik4nc.md)). The decomposition is the record's.
- **Anything for continuous alphabets or time.**
- **That it suffices for a theory of feedback systems.** Massey leaves that
  open.

## Connections

- [TERM-tmpj9z04](../terms.d/TERM-tmpj9z04.md) and [TERM-tmpq0ms2](../terms.d/TERM-tmpq0ms2.md): directed information contains
  full-history transfer entropy, and so Granger causality in the Gaussian
  case ([THEORY-tmp0xaeq](THEORY-tmp0xaeq.md)), as its lagged part. Its instantaneous part is
  Geweke's instantaneous feedback ([LIT-tmpj9yuo](../literature.d/LIT-tmpj9yuo.md)).
- [CLAIM-tmp6nu4a](../claims.d/CLAIM-tmp6nu4a.md)'s counterexample has zero lagged part and positive
  instantaneous part.
- [THEORY-tmpkovi2](THEORY-tmpkovi2.md) (Ay and Polani) is an interventional measure; this one is
  not.
