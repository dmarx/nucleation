---
status: Active
title: 'In relational quantum mechanics as Di Biagio and Rovelli define it, a fact relative to one system is stable for another, so that the other may sum over it classically, only approximately and only relative to that other system: decoherence of the first system by an environment the second cannot reach gives the classical rule to order of the environment states'' overlap, a differently coupled system may still see interference, and a fact can be stable for a system for which it is not yet a fact'
version: 1
tags:
- quantum-foundations
date: '2026-10-27'
source:
- LIT-tmpqu50n
summary: >-
  Di Biagio and Rovelli (2021), LIT-tmpqu50n, read in NOTE-tmppgt2i, §1
  (pp. 2–6). Active: the definitions are the paper's, and the result
  follows in a few lines from a partial trace (eqs. 5–8) under two stated
  conditions, ε small and the third system not interacting with the
  environment. It does not say that stable facts are absolute, that
  decoherence settles which outcome occurred, or what fixes the division
  into systems.
---
<!-- inactive-ok-file: THEORY-621 THEORY-tmpo4ob4 — Proposed; the RQM rule this rests on and the interpretive neighbour, cited as open -->

# THEORY-tmphf61a: In relational quantum mechanics as Di Biagio and Rovelli define it, a fact relative to one system is stable for another, so that the other may sum over it classically, only approximately and only relative to that other system: decoherence of the first system by an environment the second cannot reach gives the classical rule to order of the environment states' overlap, a differently coupled system may still see interference, and a fact can be stable for a system for which it is not yet a fact

## Source

Di Biagio and Rovelli (2021), LIT-tmpqu50n, §§1.1–1.3, pp. 2–6 of the
journal text; read in NOTE-tmppgt2i.

## What was actually shown

**The definitions (pp. 2–3).** A value of L_S is a fact relative to F when
an interaction makes a variable of F depend on it. Facts relative to one
system obey the classical sum rule, P(b^(F)) = Σᵢ P(b^(F)|aᵢ^(F))P(aᵢ^(F))
(eq. 2), which RQM takes to hold always. Across systems the rule
P(b^(W)) = Σᵢ P(b^(W)|aᵢ^(F))P(aᵢ^(F)) (eq. 3) "in general" fails, and its
failure is interference. "If (3) holds, we say that the facts aᵢ^(F) are
stable for W."

**The result (p. 4).** For F entangled with an environment E,
|ψ⟩ = Σᵢ cᵢ|F_ai⟩⊗|ψᵢ⟩, with 𝜖 = max_{i≠j}|⟨ψᵢ|ψⱼ⟩|², if (a) 𝜖 is small and
(b) W does not interact with E, then W's probabilities follow from the
reduced state Σᵢ|cᵢ|²|F_ai⟩⟨F_ai| + O(𝜖), and eq. (3) holds up to O(𝜖)
(eq. 8). "In the limit 𝜖 → 0, the variable L_F of the system F is exactly
stable for W." If L_S is entangled with a stable L_F, L_S is stable for W
too (p. 5).

**Relational (p. 5).** "decoherence is not an absolute phenomenon, but a
relational one: it depends on how the third system W interacts with the
combined system F − E … Another system W′ that interacts differently with
F − E might be able to detect interference effects." This could have come
out otherwise only if condition (b) were idle; it is not, since a W that
measures F–E jointly sees the coherences the partial trace discards.

**Stable without being a fact (pp. 5–6).** "a fact stable for W is not
necessarily a fact relative to W." In a laboratory measurement, after the
apparatus has decohered and before the experimenter reads it, L_S is stable
for the experimenter and not a fact for her; after she reads the pointer it
is "merely a stable fact for W" (p. 6).

**Approximate (p. 6).** "Stability is only approximate and relational.
Approximate, because no fact is exactly stable for any finite 𝜖."

**A limit case without decoherence (footnote 2, p. 5).** A fact relative
to E with amplitude |c₁| near 1 is stable for a W that does not interact
with E, to order η = 1 − |c₁|.

## What this does not say

- **That stable facts are absolute.** The paper says the opposite: "one
  does not avoid relationalism by restricting to stable facts" (p. 7).
- **That decoherence picks the outcome.** The reduced state is nearly
  diagonal; which aᵢ occurred is not given by it, and the authors agree
  that "decoherence alone is not a solution of the measurement problem"
  (p. 10).
- **A bound on the error.** O(𝜖) is stated, not bounded. With 𝜖 defined as a
  squared overlap, the off-diagonal elements of the reduced state are
  bounded by |cᵢcⱼ|√𝜖; the paper does not discuss this. Partial access of W
  to E is not treated.
- **That the same-context rule (eq. 2) is derived.** It is RQM's postulate
  (THEORY-621).
- **What the systems are.** S, F, E and W are given; how the world divides
  into them is not discussed.
- **Anything about persistence in time.** Stability here is a probability
  rule holding for a third system, not a record's lasting or staying
  accessible.
