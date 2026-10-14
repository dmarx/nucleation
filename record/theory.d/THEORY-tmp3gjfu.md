---
status: Proposed
promote_when: >-
  An empirical study of a real community that measures members' private
  opinions independently of what they express publicly, for example by
  an anonymous survey set beside platform posts. It must find that a
  small, persistently vocal minority goes with a large silent share of
  the majority, and that this silence, not conversion or network
  geometry alone, accounts for most of the gap between expressed and
  private opinion. Another simulation, with a different decision rule,
  cannot settle it: it would show robustness, not that the mechanism
  operates. Nor can observational data on expressed opinion alone, which
  cannot separate silence from absence.
title: "A spiral of silence can make a small, fixed minority opinion look far more widespread than it is without any member changing belief, and in the model that shows it the network's direct distortion of what members see is small"
version: 1
tags:
- social-science
- network-science
- epistemology
date: '2026-10-14'
source:
- LIT-939
summary: >-
  Vilone and Polizzi (2024), [LIT-939](../literature.d/LIT-939.md), read in full in [NOTE-tmpttt5h](../notes.d/NOTE-tmpttt5h.md). In
  agent-based models on scale-free networks with fixed private beliefs,
  a hard-core minority drives 55–60% of agents, nearly all of them in
  the majority, into silence, so that expressed and perceived opinion
  lean far toward the minority. The friendship-paradox distortion is
  small and of no fixed sign. This is simulation only. Beliefs never
  change, so nothing here shows a community coming to believe the
  minority view, and the majority is overturned only when the minority
  exceeds about 30%.
---
<!-- inactive-ok-file: THEORY-146 THEORY-143 — Proposed; accounts of community-level epistemic mechanisms this one sits beside -->

# THEORY-tmp3gjfu: A spiral of silence can make a small, fixed minority opinion look far more widespread than it is without any member changing belief, and in the model that shows it the network's direct distortion of what members see is small

## Source

Vilone and Polizzi (2024), *PLOS ONE* 19(1): e0296075, [LIT-939](../literature.d/LIT-939.md), read in
full in [NOTE-tmpttt5h](../notes.d/NOTE-tmpttt5h.md).

## What was actually shown

Two agent-based models on scale-free networks (N = 5000, λ = 2.2, and
λ = 1.5 as a check). Private beliefs b_i = ±1 are fixed. A hard-core
minority (b = −1, always expressed) sits on every node of degree K_c,
and the majority's belief strengths σ_i are drawn uniformly from [0, 1].

- **Model 1: no voluntary silence.** An agent expresses its belief with
  probability σ_i and otherwise its neighbours' majority.
  - Expressed opinion falls below belief for every K_c.
  - The local climate r, what agents see around them, differs from the
    global expressed average by "at most around 15%" (K_c = 10).
  - At K_c = 3, agents see slightly under 0.2 against a mean belief of
    about 0.67.
- **Model 2: silence allowed.** Agents choose ω_i ∈ {−1, 0, +1} to
  maximise
  G(ω_i) = −| (σ_i b_i + Σ_j A_i^j ω_j)/(|Γ_i| + 1) − ω_i |,
  with A_i^j = deg(j)/deg(i).
  - About 55–60% of agents end silent, "regardless of K_c" (Fig 3).
  - Expressed opinion plateaus well below belief even as the minority
    falls under 0.1% (K_c = 20), where each hard-core agent silences
    about 150 others, far beyond its own neighbours (Fig 4).
  - Here the locally perceived opinion is *closer* to the true beliefs
    than the global average is: the topological effect is "besides
    small, also non-universal".

What could have come out otherwise: the silent fraction could have
scaled with the minority's size or centrality, and the topological term
r − ⟨ω⟩ could have dominated, as the "majority illusion" account
expects. Neither happened.

## What this does not say

- **Not that the community comes to believe the minority view.**
  Beliefs are fixed by construction. The result is about what is
  *expressed and perceived*. Whether silence would in time change beliefs
  is outside the model, and the authors warn that fixed beliefs may
  exaggerate the dynamics.
- **Not that structure, rather than members' choices, sets the outcome.**
  The paper's point is close to the opposite. The direct effect of
  network geometry is small, and the bias is "mainly due to agents'
  behavior". Structure matters through degree-weighted influence and the
  cascade, and those are effects of the decision rule as much as of the
  graph.
- **Not that a few charismatic agents are needed.** A large, poorly
  connected minority produces the same silent fraction. Number and
  centrality trade off.
- **Not a reversal.** Expressed majority and minority swap places only
  when the minority exceeds about 30%. Below that the minority looks
  bigger, but does not look like the majority.
- **Not shown in any real community.** No empirical validation. The
  55–60% figure agrees with one other model (Ross et al.'s social-bot
  model), which is agreement between simulations, not evidence.
- **"Charisma" is degree,** by stipulation.

## Connections

- **[QUESTION-047](../questions.d/QUESTION-047.md).** A community-level mechanism by which what a
  community *appears* to hold, which is all any member can observe,
  comes apart from what every member believes. It answers only the
  question's second clause (which mechanisms), and only for appearance.
  No `answers:` relation is declared, because the model has no belief
  that the community settles on.
- **[THEORY-146](THEORY-146.md).** That account biases a community without corrupting any
  individual, through funding and recruitment. This one distorts a
  community's public face without changing any individual's belief,
  through expression. Both locate the effect above the members.
- **[THEORY-143](THEORY-143.md).** That account finds communication structure decisive for
  where an inquiring group settles. This one finds the network's direct
  effect on perception small. The settings differ (learning against
  fixed belief), so there is no conflict, but the two should not be
  cited together as "structure matters".
