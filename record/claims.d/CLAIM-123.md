---
number: 123
status: Proposed
formerly:
- CLAIM-tmpzkhdr
title: 'In conditional generation, adding scores composes two conditions exactly when the ratio p(y₁,y₂|x)/(p(y₁|x)p(y₂|x)) does not vary with the noisy state x, which conditional independence of the conditions at that state is sufficient for but does not require'
version: 3
history:
- version: 2
  date: '2026-10-16'
  note: >-
    Grounds add THEORY-405, the account of Composable Diffusion filed
    from LIT-770 in the THEORY backfill, which states the conditions under
    which summed scores are a product. The claim is unchanged.
- version: 3
  date: '2026-10-19'
  note: >-
    Corrected at the owner's direction, from the owner's promotion audit
    of 2026-10-19. The title said score addition composes conditions only
    under conditional independence. That is a sufficient condition stated
    as a necessary one, and the claim's own defeat condition (a proof that
    score addition composes without the assumption) is met: the derivation
    gives an exact criterion, and the body now gives dependent conditions
    that satisfy it. The derivation survives, so the claim is corrected,
    not rejected. Title, defeat condition and the first section are
    revised; the warrant stays demonstrated and the status Proposed.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the identity s₁₂ − s₁ − s₂ + s₀ = ∇ₓ log [p(y₁,y₂|x) /
  (p(y₁|x)p(y₂|x))], or in the example of conditions that are dependent
  given x and whose ratio does not vary with x.
tags:
- compositionality
- probabilistic-modeling
date: '2026-10-09'
line:
- pragmatic-transport
- formal-apparatus
works:
- what-survives-translation
grounds:
- LIT-770
- LIT-776
- LIT-783
- LIT-782
- THEORY-405
summary: >-
  The manuscript's §7, citing Composable Diffusion, T2I-CompBench and
  Schrödinger bridges. The readings support it, and the manuscript is
  more careful than the paper it cites.
illustrated_by:
- CASE-004
corroborated_by:
- CLAIM-321
---

# CLAIM-123: In conditional generation, adding scores composes two conditions exactly when the ratio p(y₁,y₂|x)/(p(y₁|x)p(y₂|x)) does not vary with the noisy state x, which conditional independence of the conditions at that state is sufficient for but does not require

## The claim

Under a product-of-experts factorization, s₁₂ = s₁ + s₂ − s₀, which is what
Composable Diffusion exploits ([LIT-770](../literature.d/LIT-770.md)). The manuscript adds that this needs
conditional independence at the relevant noisy state and does not guarantee
correct joint bindings. Schrödinger bridges give a path-space view of
conditional transport ([LIT-776](../literature.d/LIT-776.md)).

**The exact condition.** Write s₀ = ∇ₓ log p(x), sᵢ = ∇ₓ log p(x|yᵢ) and
s₁₂ = ∇ₓ log p(x|y₁,y₂), all at the same noisy state x. By Bayes,
∇ₓ log p(x|y) = ∇ₓ log p(x) + ∇ₓ log p(y|x), so

  s₁₂ − s₁ − s₂ + s₀ = ∇ₓ log [p(y₁,y₂|x) / (p(y₁|x)p(y₂|x))].

The scores add exactly when the right side vanishes, that is, when the
ratio does not vary with x on a connected region where the densities are
positive and differentiable. Conditional independence given x makes the
ratio 1 for every x, so it is sufficient. It is not necessary. Let y₁ and
y₂ each take values in {0, 1, 2}, with p(yᵢ|x) = (σ(x)/2, σ(x)/2, 1 − σ(x))
for any smooth σ into (0, 1), and let v = (1, −1, 0), so that
Σ_y v(y)p(y|x) = 0 for every x. Then

  p(y₁,y₂|x) = (1 + ε v(y₁)v(y₂)) p(y₁|x) p(y₂|x),  0 < ε < 1,

is a conditional distribution with the given marginals for every x. The
conditions are dependent given x (the factor is 1 + ε at y₁ = y₂ = 0), and
the ratio is 1 + ε v(y₁)v(y₂) for every x, so the scores add exactly. The
example is constructed; nothing here says prompts behave this way.

The manuscript's caution therefore stands with one correction. Conditional
independence is the condition under which addition is guaranteed for every
pair of condition values, not the only one under which it holds, and the
criterion is about one pair (y₁, y₂) at one noise level.

## What it does not say

It does not say a generative failure is evidence of sheaf contextuality, and
it does not identify denoising time with historical or telephone-game time.
The reading of Composable Diffusion ([NOTE-597](../notes.d/NOTE-597.md)) supports the manuscript's
caution: the paper derives the composition for clean data, applies it at every
noise level without discussion, and loses to an energy-based baseline when
composing relations.

## In C7's appendix

C7 Appendix D, omitted from the extracted manuscript, states the identity's
conditions: "The product-of-experts conditional score identity follows from the
conditional independence of c1 and c2 given x_t and a shared prior p_t(x_t),
subject to positivity and differentiability. It is not a generic identity for
arbitrary prompt embeddings or finite-step diffusion implementations. When scores
are approximate, compositional failures may reflect estimator error, model
misspecification, or sampling limitations." It adds controls: prompts paired by
entities, scene type and length, randomized order and seeds, and evaluation blind
to condition. The open question behind it is [QUESTION-018](../questions.d/QUESTION-018.md).

## A second caveat on adding scores

Ho and Salimans ([LIT-839](../literature.d/LIT-839.md)) show that learned scores are not
conservative, so a guided field is in general the score of no density. That
is a caveat on s₁₂ = s₁ + s₂ − s₀ beyond the condition on the ratio this
claim states. Attend-and-Excite ([LIT-806](../literature.d/LIT-806.md)) documents conjunctions failing
by omission ("catastrophic neglect"), and in T2I-CompBench++ ([LIT-798](../literature.d/LIT-798.md))
Composable Diffusion is again the weakest method.

## Note of 2026-10-13: a second line

Under [ADR-040](../decisions.d/ADR-040.md) (group C, decided by the owner) this claim also holds
`formal-apparatus`. It rests on no claim, and the conditions on the score identity are mathematics about conditional generation, not about translation.

## Note of 2026-10-15: split under [ADR-043](../decisions.d/ADR-043.md)

[ADR-043](../decisions.d/ADR-043.md)'s classification found this claim compound: that adding scores
composes conditions only under conditional independence at the noisy
state is a derivation (demonstrated), while that each condition can be
met while their conjunction or relational binding fails is documented by
benchmarks and method papers (empirical). The empirical part is now [CLAIM-321](CLAIM-321.md),
which corroborates this claim. This claim keeps the derivation and its
conditions, and stays demonstrated. Its title, which led with the
empirical part, was changed to state only the derivation; the first
disjunct of its defeat condition, a model whose per-condition
satisfaction predicts its joint binding accuracy, is [CLAIM-321](CLAIM-321.md)'s.
