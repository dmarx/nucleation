---
status: Active
title: "Mutual-information measures of individuality that read a system's next state off its present one measure association, not propagation: I(S_{t+1}; S_t) can be positive when the environment alone drives the system, and conditioning on the environment does not recover the interventional quantity, which can be zero where the conditional measure is one bit"
version: 1
tags:
- complex-systems
- individuation
- information-theory
- causality
date: '2026-10-16'
source:
- LIT-005
answers:
- QUESTION-115
summary: >-
  Bourrat (2024), [LIT-005](../literature.d/LIT-005.md), read in [NOTE-027](../notes.d/NOTE-027.md), against Krakauer et al.'s
  (2020) measures. A* = I(S_{t+1}; S_t) is confounded when the environment
  is a common cause (his Fig. 2), and his interventional Â = I(S_{t+1};
  Ŝ_t) is zero there. His claim that Â equals Krakauer's conditional A =
  I(S_{t+1}; S_t | E_t) is false in general: [NOTE-027](../notes.d/NOTE-027.md)'s XOR system has A =
  1 bit and Â = 0. Â itself depends on an intervention distribution the
  paper leaves open, and neither it nor the paper's two ETI criteria is
  computed on any system.
---
<!-- inactive-ok-file: LIT-005 LIT-049 — Proposed; LIT-005 is the source this account was read from, and its NOTE places it; LIT-049 is named as its ancestor -->
<!-- inactive-ok-file: LIT-1137 — Deferred; Krakauer et al., registered unread, named as the measures the source argues against -->
<!-- inactive-ok-file: THEORY-222 THEORY-tmpcxkrx THEORY-tmppkom6 — Proposed; neighbouring accounts named for comparison, nothing here rests on their being settled -->

# THEORY-tmp343c3: Mutual-information measures of individuality that read a system's next state off its present one measure association, not propagation: I(S_{t+1}; S_t) can be positive when the environment alone drives the system, and conditioning on the environment does not recover the interventional quantity, which can be zero where the conditional measure is one bit

## Source

Bourrat (2024), [LIT-005](../literature.d/LIT-005.md), *European Journal for Philosophy of Science*
14:9, read in full in [NOTE-027](../notes.d/NOTE-027.md). The paper argues against Krakauer et al.
(2020), which the record holds as [LIT-1137](../literature.d/LIT-1137.md), unread. The counterexample to
the paper's equivalence is [NOTE-027](../notes.d/NOTE-027.md)'s own.

## What was actually shown

**The measures.** Krakauer et al. coarse-grain a Markov process into a
system S and an environment E and decompose I(S_t, E_t; S_{t+1}) two ways
(Eq. 5): as A* + nC, with A* = I(S_{t+1}; S_t), and as Ei + A, with A =
I(S_{t+1}; S_t | E_t). High A* they call organismal individuality, high A
colonial individuality, high nC environmentally determined individuality.

**The confound (§4, Fig. 2).** If E fully determines S at every step, S_t
and S_{t+1} are correlated through E and A* can be positive with no
causal link from S_t to S_{t+1}. Bourrat's replacement, Â = I(S_{t+1};
Ŝ_t), the mutual information under an intervention on S_t (Eq. 6), is
zero in that world. [NOTE-027](../notes.d/NOTE-027.md) rates this argument correct.

**The equivalence that fails (§5, p. 9).** The paper says that adjusting
for E_t in Krakauer's model gives Â ≡ I(S_{t+1}; S_t | E_t) = A.
[NOTE-027](../notes.d/NOTE-027.md)'s counterexample: S_{t+1} = S_t ⊕ E_t, with S_t and E_t
independent and uniform. Then A = 1 bit, but p(s_{t+1} | do(s_t)) =
Σ_e p(s_{t+1} | s_t, e) p(e) = ½ for every s_t, so Â = 0 under any
intervention distribution. Adjustment licenses the averaged channel
Σ_z p(s′ | s, z) p(z); its mutual information is a different quantity from
the conditional mutual information, which averages within-stratum
dependence.

**What could have come out otherwise.** Conditioning on E could have been
enough to remove the confound and give the causal quantity. In the XOR
system it gives the most dependence the system has, where intervention
finds none.

## What this does not say

- **That Â is the right measure of individuality.** It is a definition.
  Its value depends on the distribution chosen for Ŝ_t (fn. 4: uniform,
  population, or a "normal" range), which the paper leaves open, so
  comparisons across coarse-grainings are not yet defined.
- **That Bourrat's ETI criteria work.** C1 (normalised Â across
  coarse-grainings) and C2 (low variance of Â under interventions on E)
  are never computed on any model, and "low" has no threshold.
- **That [LIT-005](../literature.d/LIT-005.md) shows how to estimate causal individuality from
  observational data.** Its one implementation-level step is the false
  equivalence, and its Fig. 3 adjustment set leaves a backdoor through
  E_b,T−1 open ([NOTE-027](../notes.d/NOTE-027.md), C6).
- **That Â separates an individual from a part of one.** The paper says it
  does not (§7), and offers "the coarsest grain at which Â is maximal" as
  future work.
- **That Krakauer's measures are useless.** They measure predictive
  retention. The point is that retention and causal propagation are
  different things, and a high score on the first is not evidence of the
  second.

## Connections

- **[QUESTION-115](../questions.d/QUESTION-115.md)** asks which of persistence, integration and causal level
  each information criterion tracks. This constrains the answer for
  temporal retention: A* and A track predictive dependence, which the
  environment can supply, and neither is the interventional quantity. It
  does not say which criterion finds a collective's boundary.
- **The ΦID review ([LIT-025](../literature.d/LIT-025.md); [THEORY-tmpcxkrx](THEORY-tmpcxkrx.md))** makes the same point for
  its own measures: they are interventional only if p(X′ | X) is a
  do()-distribution, and predictive otherwise. Neither paper cites the
  other.
- **Effective information ([THEORY-222](THEORY-222.md))** is mutual information under a
  maximum-entropy intervention. Â with a uniform intervention distribution
  has the same structure ([NOTE-027](../notes.d/NOTE-027.md)'s observation), which is one way to
  fill the choice fn. 4 leaves open.
- **Bourrat's earlier account ([LIT-049](../literature.d/LIT-049.md); [THEORY-tmppkom6](THEORY-tmppkom6.md))** first stratifies
  on the environment, as δC|E, to exclude ecologically driven coherence.
  This is where that stratification and its gap show up formally.
