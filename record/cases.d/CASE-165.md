---
number: 165
status: Proposed
formerly:
- CASE-tmplcm41
title: 'A dynamic beta–Bernoulli latent-feature model of an organization''s members: a finite Indian buffet prior over who holds which interpretive features, a sticky logistic transition for holding them, activations, and team, communication and authorization layers above; at the proposed size of sixteen features it falls well short of the Indian buffet process it quotes, its persistence term does not hold rare features, and the difference between having a capacity and using it is not identified from the outputs'
version: 2
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed from T22–T24 of the exchange "Experimental Infrastructure
    Review": the model as T23 stated it, with T24's port to transformer
    checkpoints. Its prior marginals, the sticky transition and the
    identifiability gaps were re-checked numerically when it was filed. No
    model was fitted, and no lab holds an implementation.
- version: 2
  date: '2026-10-27'
  note: >-
    A dated note added on item 2: the Markov IBP, which item 2 names
    as Van Gael et al. 2009 and not held, was registered and read on
    2026-10-27 (LIT-1577, NIPS 21 of December 2008); the note
    places the sticky term against it with its two THEORYs and their
    caveats, and confirms item 2's numbers. Title, standing and status
    unchanged.
standing: stipulated
kind: construction
tags:
- probabilistic-modeling
- mathematical-statistics
- individuation
date: '2026-10-26'
line: distributed-agency
summary: >-
  The owner's T22 ("maybe we could benefit from a restaurant process
  model, like an indian buffet model"), developed at T23 ("flesh out our
  proposed generating probability model further") into a full generative
  specification for the Northstar firm, and carried to transformer
  training at T24. It is the candidate method of [QUESTION-276](../questions.d/QUESTION-276.md) in its
  most worked-out form. Its facts are its definition, and four of them
  are not what T23 says: at K = 16 the prior expects 6.83 features, not
  αH₁₂ = 9.31; a held rare feature is kept with probability 0.16 a day;
  and having, using and splitting features are confounded in the
  reconstruction. It shows what such a model would have to get right
  before its features could count for anything.
supports:
- CLAIM-454
---
<!-- inactive-ok-file: CLAIM-263 — Proposed; the quotient test cited as one way to tell a birth from a split, nothing here rests on it -->
<!-- inactive-ok-file: CLAIM-454 — Proposed; filed with this case from the same exchange -->
<!-- inactive-ok-file: THEORY-1004 — Proposed; a reading of the same day, cited for its measure of presence against use -->

# CASE-165: A dynamic beta–Bernoulli latent-feature model of an organization's members: a finite Indian buffet prior over who holds which interpretive features, a sticky logistic transition for holding them, activations, and team, communication and authorization layers above; at the proposed size of sixteen features it falls well short of the Indian buffet process it quotes, its persistence term does not hold rare features, and the difference between having a capacity and using it is not identified from the outputs

## The construction (T23)

For employees e = 1 … N, latent features k = 1 … K and days t:

- **Prior** (T23 §3). π_k ~ Beta(α/K, 1), B_{ek,0} | π_k ~ Bernoulli(π_k),
  W_k ~ p(W). "As K grows, the induced distribution over the initial binary
  feature allocations approaches the familiar one-parameter IBP
  construction", with "E[K_N] = αH_N".
- **Holding a feature** (§4), "a sticky logistic transition":
  logit p_{ek,t+1} = logit(π_k) + ρB_{ek,t} + β_social Σ_f C_{ef,t}B_{fk,t}
  + β_team Σ_g M_{eg,t} B̄_{gk,t} + β_learn r_{ek,t}, and
  B_{ek,t+1} ~ Bernoulli(p_{ek,t+1}). T23 names it accurately: "an
  IBP-inspired initial allocation with a separately specified dynamic
  transition model. It is not automatically the exact dependent IBP of
  Williamson, Orbanz, and Ghahramani".
- **Using a feature** (§5). An activation a_{ek,t} ∈ [0, 1], Beta-distributed,
  and the interpretation u_{e,t} = Σ_k B_{ek,t} a_{ek,t} W_k o_{e,t} +
  W_e^private o_{e,t}, with optional pairwise terms. "Feature availability
  should not be confused with feature use."
- **Access, world and reports** (§5–6). A signal reaches an employee with
  a probability set by team, role, communication and attention; the world
  is X_{t+1} = f(X_t, A_t) + ε_t; reports are O_{j,t} ~ N(H_j X_t +
  b_j(ρ_{j,t}), σ_j²), with a reporting bias the organization can move.
- **Organization** (§7–8). Poisson communication attempts with typed
  messages, team records L_{g,t}, proposals by softmax over local
  appraisals, and enactment by P(A_t | P_t, Γ_t, L_t, C_t) through a
  permission structure Γ_t. The established form of a team layer at
  t = 0 is the hierarchical beta process ([THEORY-1015](../theory.d/THEORY-1015.md)): each team's
  prevalence of a shared feature is drawn around a shared one. It puts
  each member in one group, fixed, so it cannot give the overlapping and
  changing membership M_{eg,t} or the β_team dynamics. "A frequently active employee may have little
  authority. An employee who rarely communicates may possess a critical
  veto."
- **No perspective variable** (§10). "It does not contain a primitive
  random variable whose value is the organization's current perspective."
  A perspective is "a derived hypothesis about a persistent regime" and a
  tuple of features, relations, governance and history, inferred
  afterwards. "The IBP prior supplies multiplicity; the relational dynamics
  will have to supply organization" (§3). That division is
  [CLAIM-454](../claims.d/CLAIM-454.md).
- **Proposed size** (§12, "Northstar generative study v0"). N = 12, 4
  formal teams, K = 16, α = 3, 5 world dimensions, 64 days: "proposed
  experimental settings, not measured results".
- **How to use it** (§16). "Option A — Mechanistic simulator + IBP
  inference" first: fit the feature model to a simulator that does not
  assume it, so that "feature discovery can be tested against a world that
  did not itself assume IBP-distributed employees".

## What checks out

- The IBP's sequential construction (T22) and E[K_N] = αH_N. For N = 12
  and α = 3, αH₁₂ = 9.310, and simulating the buffet gives 9.29 to 9.33.
  The beta process gives the same count a second way, as the IBP's de
  Finetti measure ([THEORY-985](../theory.d/THEORY-985.md)).
- The finite beta–Bernoulli limit. E[occupied features] is
  K(1 − (α/K)B(α/K, N + 1)), which is 8.38 at K = 50 and 9.26 at K = 1000
  and tends to αH_N, from below for every finite K ([THEORY-999](../theory.d/THEORY-999.md)).
- The joint factorization (§9) is a valid chain-rule factorization under
  its stated Markov assumptions. It does let decisions depend on the
  hidden world directly, p(D_t | O_t, S_t, Θ), so "access comes before
  interpretation" is intended and not enforced.
- The two non-identifiabilities §15 names: column permutation, and the
  scale trade of W_k against a_{ek} (exact while the rescaled activation
  stays in [0, 1]). §15 also says that "Closely related latent features may
  also split or merge without significantly changing the likelihood".

## What does not

1. **The truncation is not generous at the size chosen.** T22 recommends
   "a finite, generously truncated beta–Bernoulli approximation"; T23 fixes
   K = 16 and quotes αH_N. At K = 16 the expected number of occupied
   features is 6.83 (simulated 6.82), 27% short of 9.31, and the expected
   number per employee is Kα/(K + α) = 2.53, not α = 3. The buffet itself
   seldom needs more than 16 (P(K_N > 16) ≈ 0.015), so a stick-breaking
   truncation at 16 would be close to it (8.97, simulated). The finite
   model at 16 is not. The review T22 and T23 cite states αH_N for the
   limit only (§4.6); for finite K it gives no count of occupied features,
   so the quotation at K = 16 has no support there ([THEORY-999](../theory.d/THEORY-999.md),
   [NOTE-1172](../notes.d/NOTE-1172.md)).
2. **The sticky transition does not hold rare features.** Without social,
   team or learning input, a held feature is kept with probability
   σ(logit π_k + ρ). Under the prior at K = 16, E[ln π_k] = −K/α = −5.33 and
   the median π_k is 0.025, where the probability of keeping a held feature
   is 0.16 at ρ = 2, 0.58 at ρ = 4 and 0.91 at ρ = 6. "A feature persists
   because an employee retains it" holds only where ρ is near −logit π_k,
   and one ρ cannot do that for features of different prevalence. The
   stationary prevalence also departs from π_k (0.36 against 0.2 at ρ = 2,
   0.75 at ρ = 4), so the buffet's prior properties hold at t = 0 only.
   The established relatives fix what this term does not. The dependent
   IBP T23 names thresholds a Gaussian process at the quantile of a stick
   that does not change with time, so each feature's prevalence stays
   fixed and its persistence is set separately ([THEORY-1006](../theory.d/THEORY-1006.md)); but for
   one correlation a rarer feature is still kept less often (0.59 at a
   prevalence of 0.025 against 0.75 at 0.2, for correlation 0.9), and only
   per-feature length scales make it a per-feature parameter. The Markov
   IBP (Van Gael et al. 2009, described in the review's §7.4, not held)
   gives each feature its own probabilities of turning on and staying on.
   And with team-specific prevalences, as in a hierarchical beta process
   ([THEORY-1015](../theory.d/THEORY-1015.md)), one ρ fails across teams as well as across
   features.
3. **Having and using are not identified from the outputs.** §2 calls
   the separation of B and a "important" ("An engineer may possess the
   capacity to interpret customer harm but not activate that interpretive
   mode"). In u = Σ B a W o + W^private o:
   - B = 1 with a near 0 and B = 0 give nearly the same output, so
     availability is told from activation only by the prior and the
     transition, not by the data.
   - A feature one employee holds at constant activation c is absorbed into
     that employee's private map, W^private + cW_k, exactly.
   - Features whose B and a columns coincide across employees are
     identified only through W_k + W_l, exactly.
   These are instances of [CLAIM-148](../claims.d/CLAIM-148.md)'s gauge, which says a factorization is
   identified only up to an invertible change of latent coordinates. A
   correlated prior over features does not remove the third: it separates
   co-occurring features only where they sometimes occur apart
   ([THEORY-1012](../theory.d/THEORY-1012.md), [NOTE-1184](../notes.d/NOTE-1184.md)). The author–topic model has the
   absorption of the second in published form. Its per-document
   "fictitious author" plays W^private, a topic used by one document can
   sit there or in a real author's distribution as the priors choose, and
   adding it improves prediction throughout ([THEORY-1003](../theory.d/THEORY-1003.md)).
4. **Splits and zero contributions are free.** In the per-component form
   T24 ports to transformers, r_c(x) ≈ Σ_k B_ck a_k(x) v_ck, rescaling a
   feature is exact, splitting a_k into two columns with copied B and v
   raises K by one at no cost, and B_ck = 1 with v_ck = 0 equals B_ck = 0.
   A generic invertible mix of features destroys all 15 zeros of B∘V in a
   6 × 4 check, so sparsity is what identifies features, up to permutation,
   scale and splits. A "birth" in B can therefore be an artefact of the
   prior or of a split, and needs a test beyond reconstruction, such as a
   causal effect or [CLAIM-263](../claims.d/CLAIM-263.md)'s quotient by the full symmetry group. The
   review's own worked example shows both freedoms: in its photograph
   demonstration three of the four main features code an object's
   absence, and three extra ones code "slight differences in the
   locations" ([NOTE-1172](../notes.d/NOTE-1172.md)), so a 1 in a column need not mean "has" and
   a feature can be a split of another.

All of these were re-computed when this case was filed (exact formulas,
and Monte Carlo over 20,000 draws or more).

## The port to transformer checkpoints (T24)

T24 carried the model to components c of a transformer across checkpoints
s, with a temporal prior p(B_s | B_{s−1}, θ_s, 𝒟_s), "where 𝒟_s summarizes
training exposure". Two further gaps:

- **The prior conditions on what it should predict.** B_s is inferred from
  activations fixed by θ_s, so conditioning on θ_s leaves the prior
  nothing to forecast. The prospective test T24 itself asks for, fitting
  early checkpoints and predicting later ones, needs B_{s+1} predicted
  from B_{≤s}, exposure and intervention without θ_{s+1}. Since the true
  dynamics are known ((θ, m) updated by the optimizer), a dynamic model of
  B is a coarse-graining, and whether it is adequate is a closure question
  ([TERM-068](../terms.d/TERM-068.md), [QUESTION-252](../questions.d/QUESTION-252.md)).
- **Components are not exchangeable.** The buffet treats its customers as
  exchangeable. Heads and MLP channels are distinguished by layer and by
  what they read and write, so a layer-indexed or hierarchical prior would
  be needed.

In a transformer the third gap above, having against using, is measured
by intervention rather than left to the prior. Cross-checkpoint
crosscoders separate a feature's presence at a checkpoint (its decoder
norm) from its causal use on a task (its indirect effect), and a feature
can be present and idle ([NOTE-1186](../notes.d/NOTE-1186.md), [THEORY-1004](../theory.d/THEORY-1004.md)). The refined-LLC
study compares a head's weight sensitivity with output ablation, which
mostly agree and sometimes do not ([NOTE-1188](../notes.d/NOTE-1188.md)). A crosscoder's jointly
trained dictionary is the deterministic analogue of this model's
allocation without a temporal prior, and the split caution of item 4
applies to it too. Where a task's symmetries fix the components'
features, as in Musat, Pimentel, Zucchet and Hofmann's idealized
attention-only model ([THEORY-981](../theory.d/THEORY-981.md)), both identifiability worries are
removed by construction: the coordinates are given, not inferred.

## What it can show

What a latent-feature model of members must get right before its features
can be read as anything: a truncation that matches the prior quoted, a
persistence term scaled to prevalence, and a test that separates having
from using and a birth from a split. It is the form in which
[QUESTION-276](../questions.d/QUESTION-276.md)'s candidate method would be judged, and its
§10 division is [CLAIM-454](../claims.d/CLAIM-454.md)'s.

## What it cannot show

That any firm's or network's members hold such features, or that the
model fitted to anything recovers a perspective. Nothing has been fitted.
"An IBP prior by itself cannot produce organizational capture,
self-maintaining coalitions, or effective institutional learning" (T23
§13).

## Note of 2026-10-27: item 2 and the Markov IBP, now held

Item 2 names "The Markov IBP (Van Gael et al. 2009, described in the
review's §7.4, not held)". It was registered and read on 2026-10-27, at
the owner's request ("get started on the seven works and markov IBP"), as
[LIT-1577](../literature.d/LIT-1577.md): Van Gael, Teh and Ghahramani, *The Infinite Factorial Hidden
Markov Model* ([NOTE-1199](../notes.d/NOTE-1199.md)), the paper that introduces the Markov Indian
buffet process. It appeared at NIPS 21, the conference of December 2008;
the review ([LIT-1556](../literature.d/LIT-1556.md)) cites it as 2009, the year of the printed volume. It
is the same work, and the record dates it 2008-12-01.

- **What it gives each feature ([THEORY-1034](../theory.d/THEORY-1034.md)).** Each feature's
  probability of staying on, b ~ Beta(γ, δ), is drawn independently of its
  probability of switching on, a ~ Beta(α/M, 1), so persistence does not
  depend on rarity. T23's sticky term, with its other inputs at zero, is
  the same two-state chain per feature, with on-rate π_k and the stay-rate
  tied to it as σ(logit π_k + ρ). At the paper's prior means every
  feature, however rare, is kept with E[b] = 10/11 = 0.91; T23 needs
  ρ = 5.97 to reach that for the median feature (π = 0.0248), and then
  mis-scales common ones. So the Markov IBP fixes the coupling of
  persistence to rarity that item 2 finds.
- **What it does not fix ([THEORY-1019](../theory.d/THEORY-1019.md)).** Its expected number of
  features on is α at the first step but rises toward
  α·E[ln((2 − b)/(1 − b))], 9.04 at the paper's prior means (γ = 10,
  δ = 1, α = 3), three times α; after the first step the rows are not
  IBP-distributed. Prevalence is not held either: the stationary
  on-fraction is a/(1 − b + a), 0.22 at a = 0.025 with b = 10/11. So the
  "t = 0 only" problem item 2 names remains under the Markov IBP; of the
  relatives the record holds, only the dependent IBP keeps prevalence fixed
  over time ([THEORY-1006](../theory.d/THEORY-1006.md)).
- **The members' axis.** "Gives each feature its own probabilities"
  holds for one sequence of time steps. The model has no axis of members,
  and sharing (a, b) across N members is not derived in the paper.
- **Item 2's numbers re-check.** The keep probabilities 0.16, 0.58 and
  0.91 at ρ = 2, 4 and 6 for the median π, and the stationary prevalences
  0.36 and 0.75, which are the same formula a/(1 − b + a) with b = 0.649
  and 0.932 ([NOTE-1199](../notes.d/NOTE-1199.md)).

The paper's printed predictive rules for its sequential buffet are both
misprinted; the record's reading uses the rules derived from its eq. (6)
([NOTE-1199](../notes.d/NOTE-1199.md)). The case is unchanged.
