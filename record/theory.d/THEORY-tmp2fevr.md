---
status: Active
title: 'For discrete X and Y, with an intervention on a variable abstraction T of X defined as the mixture of interventions on X weighted by Bayes inversion of the encoder under a protocol prior, no abstraction gains causal information about Y over X itself, and at full weight on causal control the causal information bottleneck is optimised by the partition of X by p(y | do(x)), mapped one class to one value of T, uniquely up to relabelling when T has exactly as many values as there are classes; these are Chalupka et al.''s causal macrovariables'
version: 1
tags:
- causality
- information-theory
date: '2026-10-29'
source:
- LIT-tmpagj3g
summary: >-
  Simoes, Dastani and van Ommen (UAI 2025), [LIT-tmpagj3g](../literature.d/LIT-tmpagj3g.md), Proposition 20
  with its proof (pp. 14–15), read in [NOTE-tmpuxoku](../notes.d/NOTE-tmpuxoku.md) from the arXiv
  preprint v5. Active: the proof is a strict-concavity argument, checked
  here on the paper's Genetic Mutations SCM. It is the interventional
  counterpart of [THEORY-743](THEORY-743.md), and unlike the bottleneck there it reaches
  the partition exactly, because γ = 1 drops the compression term. It
  holds for the paper's stipulated intervention on T and a fixed
  protocol; it says nothing about intermediate γ.
---

# THEORY-tmp2fevr: For discrete X and Y, with an intervention on a variable abstraction T of X defined as the mixture of interventions on X weighted by Bayes inversion of the encoder under a protocol prior, no abstraction gains causal information about Y over X itself, and at full weight on causal control the causal information bottleneck is optimised by the partition of X by p(y | do(x)), mapped one class to one value of T, uniquely up to relabelling when T has exactly as many values as there are classes; these are Chalupka et al.'s causal macrovariables

## Source

Simoes, Dastani and van Ommen (2025), [LIT-tmpagj3g](../literature.d/LIT-tmpagj3g.md), Definitions 4, 5, 13
and 19 and Proposition 20 (pp. 4, 12, 14–15) of arXiv 2410.00535v5; read in
[NOTE-tmpuxoku](../notes.d/NOTE-tmpuxoku.md).

## What was actually shown

**The setting.** T is given by an encoder q(t | x). With a protocol prior
p*(x) (uniform in the paper), the decoder is p*(x | t) ∝ q(t | x)p*(x),
p*(t) = Σ_x q(t | x)p*(x), and p(y | do(T = t)) = Σ_x p*(x | t)
p(y | do(X = x)) (Definitions 4–5, p. 4). Causal information gain is
Ic(Y | do(T)) = H(Y) − Σ_t p*(t) H[p(y | do(T = t))] (Definition 13,
p. 12). At γ = 1 the Lagrangian is −Ic(Y | do(T)), so minimising it is
minimising the causal entropy Σ_t p*(t) H[p(y | do(T = t))].

**The argument (pp. 14–15).** By strict concavity of entropy,
H[Σ_x p*(x | t) p_do(x)] ≥ Σ_x p*(x | t) H[p_do(x)], strictly when the
cell of t mixes two x with different p(y | do(x)). Summing with weights
p*(t) gives Hc(Y | do(T)) ≥ Σ_x p*(x) H[p_do(x)] = Hc(Y | do(X)) for every
encoder, so Ic(Y | do(T)) ≤ Ic(Y | do(X)). The deterministic encoder of
the causal partition mixes only x with equal p(y | do(x)), so it attains
equality (eq. 15). With exactly as many values of T as classes, any other
encoder must mix two classes in some value of T, and the inequality is
strict.

**The check.** On the Genetic Mutations SCM of Fig. 2b (noise as in Fig.
1c), the 16 values of X fall into four causal classes, the values of
θ(x) = x₁ + x₂ + (2 − x₃)x₁x₂, against ten classes of the observational
p(y | x). The θ-encoder keeps Ic(Y | do(X)) = 0.798 bits; 20,000 random
stochastic four-valued encoders reached at most 0.340; merging two classes
gave 0.697.

**What could have failed.** A stochastic encoder could have done better
than any partition; concavity rules it out.

## What this does not say

- **Anything about γ < 1.** The compression trade-off has no ground truth
  in the paper, and nothing says the optima for different γ nest
  ([THEORY-743](THEORY-743.md) leaves the same open for the IB).
- **That the intervention on T is a physical one.** It is defined from the
  encoder and the protocol; the authors defend it as a consistent
  stipulation for "an artificial, conceptual abstraction of X" (p. 15).
- **That the partition is protocol-free.** The partition itself is fixed
  by p(y | do(x)), but which encoders are optimal at γ < 1, and how much
  Ic a coarsening loses, depend on p*.
- **That the optimiser finds it.** That is [THEORY-tmppip5e](THEORY-tmppip5e.md)'s empirical
  question.
- **Anything for continuous variables**; the argument uses exact discrete
  entropies.
