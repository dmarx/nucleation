---
status: Active
title: 'The persistence a Dirichlet–categorical hierarchy gives a run of selections is an observer''s learning about a fixed mixture, not a change in what selects: under a uniform prior an observed first choice raises the predicted chance of repeating it from 1/2 to 2/3, while the same choice forced leaves it at 1/2, so the hierarchy''s reinforcement is not evidence of self-formation or of a maintained will-organization, which need the mixture itself to change under the choice'
version: 1
role: disclaimed
warrant: demonstrated
defeated_if: >-
  An error in the computation; or a model in which observational
  reinforcement in such a hierarchy entails a causal change in the
  mixture, under conditions met by the systems the record applies it to.
tags:
- probabilistic-modeling
- free-will
date: '2026-11-02'
line:
- will-organization
- formal-apparatus
rests_on:
- CLAIM-414
complements:
- CLAIM-025
- CLAIM-tmphbnqm
uses:
- TERM-tmp8cp5q
- TERM-023
summary: >-
  A13 of the exchange "Assess SDT Coverage" (2026-11-02), answering the
  owner's U13, what the Dirichlet–categorical reading implies for
  Jennings's attention as the source of a free will. A13: "Self-formation
  requires a causal update, not merely a posterior update in the
  observer." Correct, short and not held. It limits the record's own
  H1/H2 reading ([CLAIM-tmphbnqm](CLAIM-tmphbnqm.md)) and A11's suggestion that LDA already has
  "a primitive analogue of a will-organization". Rechecked here by
  simulation.
---
<!-- inactive-ok-file: TERM-tmp8cp5q — Proposed; terms added at the owner's review of 2026-11-03 -->

# CLAIM-tmplz9zf: The persistence a Dirichlet–categorical hierarchy gives a run of selections is an observer's learning about a fixed mixture, not a change in what selects: under a uniform prior an observed first choice raises the predicted chance of repeating it from 1/2 to 2/3, while the same choice forced leaves it at 1/2, so the hierarchy's reinforcement is not evidence of self-formation or of a maintained will-organization, which need the mixture itself to change under the choice

## The claim

Take θ ~ Beta(1, 1) and choices Z₁, Z₂ ~ Bernoulli(θ), independent given θ.
Then P(Z₂ = 1 | Z₁ = 1) = E[θ²]/E[θ] = (1/3)/(1/2) = 2/3. If Z₁ is set by
intervention, do(Z₁ = 1), the arrow θ → Z₁ is cut, θ keeps its prior, and
P(Z₂ = 1 | do(Z₁ = 1)) = E[θ] = 1/2. A simulation of 400,000 runs gives
0.667 and 0.500.

The rise from 1/2 to 2/3 is information about θ, gained by whoever watches
the first choice. Nothing in the chooser changed. So the tendency of a
Dirichlet–categorical hierarchy to "reinforce" a run of selections is the
observer's learning about a fixed mixture. Self-formation, in the sense the
record holds ([TERM-023](../terms.d/TERM-023.md)'s transformation; [CLAIM-025](CLAIM-025.md)'s capacity to transform
the governing organization), needs the mixture itself to change because of
the choice. That is a further structure, for example θ_{t+1} = F(θ_t, Z_t),
and it is told apart from the observer's learning only by intervening
([CLAIM-414](CLAIM-414.md)).

## What it does not say

- **That self-formation does not happen.** It says this hierarchy's
  reinforcement is not evidence of it.
- **Anything about Jennings's paper** ([LIT-tmpasemk](../literature.d/LIT-tmpasemk.md)) beyond this. The claim
  is the formal limit on reading its fluid-to-formed transition off
  observed choice sequences. The paper's own mechanism, from Voigt 2022, is
  a causal update of the chosen option's stored value (p. 25), which is the
  structure this claim says self-formation needs ([NOTE-tmpby7i2](../notes.d/NOTE-tmpby7i2.md)).

## Note of 2026-11-03: Voigt, read

The causal update Jennings takes from Voigt is a correlational finding with a
causal role imported for gaze, not an intervention (NOTE-tmpic1x7). So the
structure this claim says self-formation needs is proposed there, not shown.
CASE-tmph9iwi builds it.
