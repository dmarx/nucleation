---
status: Read
paper: 'LIT-tmp7q0hf'
title: 'Eichler and Didelez — Causal reasoning in graphical time series models'
version: 1
history:
- version: 1
  date: '2026-10-16'
  note: >-
    Read in full from arXiv 1206.5246v1, the UAI 2007 paper as printed
    (pp. 109–116): §§1–5, Examples 3.2, 4.2, 4.5, 4.7, 4.9, 4.12 and 4.14,
    Figures 1–4 from captions and prose, references. Nothing skipped.
    Extracted with pdftotext; the edge glyphs in the graph definitions
    were lost, and I reconstructed them from the prose. I checked the
    causal effects in Examples 4.2 and 4.14 against the defining
    equations. The front-door theorem's proof is deferred to "Eichler and
    Didelez (2007), in preparation", which I did not read.
date: '2026-10-16'
summary: >-
  Defines the causal effect of intervening on one component of a stationary
  multivariate time series on another at a later time, and relates it to
  strong Granger noncausality through mixed graphs. Under Assumption 2.3
  (an intervention independent of the system's past and of the other
  contemporaneous variables, and acting on the future only through the
  present), a missing Granger edge a → b means no effect on b at the next
  step, a ∉ an(b) means no effect at any horizon, and time-series back-door
  and front-door criteria identify effects from observational data. A
  present edge is only "potentially causal".
---

# NOTE-tmpm48uq: Eichler and Didelez — Causal reasoning in graphical time series models

## Contribution

Granger noncausality had been read informally as "not causal", and Granger
causality as "potentially causal". This paper states when the first reading
is a theorem. It defines causation for time series by intervention, links
interventions to the Granger-causal Markov property of a mixed graph, and
gives graphical identification criteria for time series, analogues of
Pearl's back-door and front-door criteria.

## Key insight

An intervention indicator can be treated as one more node, with a single
edge into the intervened component. If the indicator is Granger-noncausal
for b given S at all horizons, the observational predictor of b from S's
past is also the post-intervention predictor. The graph's paths say when
that holds.

## Assumptions

- **X is stationary and mixing**, with regular, a.s. absolutely continuous
  conditional distributions (§2).
- **Assumption 2.3 (intervention).** (i) (X_V(t−1) history,
  X_{V∖a}(t)) ⊥⊥ σ_a(t). Whether one intervenes is neither informed by the
  past nor informative about the other variables at t, which "excludes
  instantaneous causality". (ii) {X_V(t + j), j ∈ ℕ} ⊥⊥ σ_a(t) | X_V(t)
  history. The future is tied to the intervention only through the
  present and past. Together they make an intervention "an isolated
  exogenous change of the system". They must be checked in each
  application.
- **V is rich enough.** The system V includes every relevant process,
  observable or not, so that Assumption 2.3 can be believed. The observed
  processes S ⊆ V may be fewer (§2.1).
- **σ is a decision variable**, not a random one (Remark 2.2).
- **The global Granger-causal Markov property** for a mixed graph G
  (Def. 4.6) for the graphical results.
- **Effects are defined for h > 0.** Contemporaneous effects are outside the
  framework.

## Key results

- **Theorem 3.1, back-door.** If Assumption 2.3 holds, a, b ∈ S, and
  X_b(t + h) ⊥⊥ σ_a(t) | X_S(t) history for all h, then S identifies the
  effect: E_s X_b(t + h) = E_∅ E_s[E_∅(X_b(t + h) | X_S(t) history)]. "Under
  Assumptions 2.3, V always has to identify the causal effect due to
  condition (ii)."
- **Example 3.2, Gaussian.** For a purely nondeterministic stationary
  Gaussian process with a well-conditioned spectrum, the effect of setting
  X_a(t) = x* is Φ_ba^{(h)}(1)x*, the coefficient of the best linear h-step
  predictor from S's autoregression, computed recursively.
- **Def. 4.1, strong Granger noncausality.** X_A ↛ X_B [X_V] if
  X_B(t + 1) ⊥⊥ X_A history at t | X_{V∖A} history at t: conditional
  independence, not just absence of correlation.
- **Theorem 4.8.** If every an(B)-pointing path between A and an(B) is
  m-blocked given B ∪ C, X_A is Granger-noncausal for X_B at all horizons.
- **Lemma 4.10, Theorem 4.11.** If every an(b)-pointing back-door path
  between a and an(b) is m-blocked given S, X_b(t + h) ⊥⊥ σ_a(t) |
  X_S(t) history, so Theorem 3.1 applies.
- **Theorem 4.13, front-door.** Three m-blocking conditions through a
  mediating set C identify the effect. Proof deferred.
- **Conclusion.** No edge a → b implies no effect of X_a(t) on X_b(t + 1);
  a ∉ an(b) implies no effect at any horizon. Granger-causal edges are
  "potentially causal", given Assumption 2.3.
- **Example 4.2, ctd.** With Z latent, the effect of X3(t) on X1(t + 2) is
  β₁₂β₂₃x₃*. Back-door with S = {1, 2, 3}, from the observed
  autoregression, gives φ₁₂(1)φ₂₃(1) + φ₁₃(2) = β₁₂β₂₃. *Checked:*
  projecting Z(t − 2) on the observed past gives coefficient
  c = α₁α₂/(1 + α₂²) on X2(t − 1) and −cβ₂₃ on X3(t − 2), so
  (β₁₂ + c)β₂₃ − cβ₂₃ = β₁₂β₂₃. The latent confounder biases the one-step
  coefficients but cancels in the two-step one.
- **Example 4.14.** With Z correlated with X3's noise, back-door fails,
  and the front-door criterion gives φ₁₂(1)φ₂₃(1)x₃* = β₁₂β₂₃x₃*.
  *Checked:* Z(t) is untouched by the intervention, and the naive
  two-step coefficient carries an extra αρ.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Under Assumption 2.3, if S's observed past makes b's future independent of σ_a, the effect is identified from observational quantities | strong | Theorem 3.1, proved |
| C2 | Under Assumption 2.3, the whole system V always identifies the effect | strong | by condition (ii); remark after Theorem 3.1 |
| C3 | Graphical back-door blocking in the mixed graph is sufficient for C1 | strong | Lemma 4.10 via Theorem 4.8; proof sketched by augmenting the graph |
| C4 | A missing Granger edge means no effect at the next step; non-ancestry means none at any horizon | moderate | Conclusion, "by a similar reasoning as for Lemma 4.10"; not written out |
| C5 | A front-door criterion identifies effects under a latent confounder of the cause | moderate | Theorem 4.13 stated; proof deferred to work in preparation; Example 4.14 checks |
| C6 | In a Gaussian VAR the effect is a multi-step linear-predictor coefficient | strong | Example 3.2 with Box et al.'s recursion; Examples 4.2, 4.14 checked |
| C7 | Granger (1969) required the series to contain all relevant processes but did not ask whether an intervention is possible | assertion | Conclusion; about Granger's paper, not shown from it |

## Concepts

- **Intervention indicator σ_a(t)** — idle (∅), atomic (set to x*),
  conditional (a function of the observed past) or random (a known
  distribution) (Def. 2.1).
- **ACE** — E_{σ_a(t)=s} X_b(t + h) (Def. 2.5).
- **Mixed graph** — directed edges a → b for Granger causality, dashed
  undirected edges for contemporaneous dependence, up to three edges per
  pair (§4.2). Contemporaneous dependence may come from hidden processes.
- **m-separation** — path blocking where a node is an m-collider if both
  adjacent edges have an arrowhead or a dashed end at it (Def. 4.4).

## Connections

- **Builds on** Granger (1969, [LIT-tmppqyor](../literature.d/LIT-tmppqyor.md)), Florens and Mouchart's strong
  noncausality, Eichler's graphical time-series models, Pearl's back-door
  and front-door criteria, and Dawid's decision-theoretic intervention
  indicators. White (2006) is named as the nearest work on interventions in
  time series.
- **[NOTE-010](NOTE-010.md) C5**, "if all relevant variables are measured, Granger- and
  Pearl-type analyses coincide". This paper is a statement of conditions
  for it. Measuring everything gives C2, but C2 also needs Assumption
  2.3(i), which excludes instantaneous causation. My counterexample, filed
  in [CLAIM-tmp6nu4a](../claims.d/CLAIM-tmp6nu4a.md), has every variable measured and a Granger-noncausal
  for b, yet a lagged intervention effect of a on b. It works because a
  acts on b within one sampling step, which the graph shows only as a
  dashed edge.
- **[NOTE-010](NOTE-010.md) C4 and [THEORY-497](../theory.d/THEORY-497.md)** say ΦID's quantities are
  interventional if p(X_t′ | X_t) is a do()-distribution, with faithfulness
  and the causal Markov condition. Assumption 2.3 is the time-series form
  of the first condition. Theorem 3.1 needs neither faithfulness nor a
  Markov condition. The graphical criteria need the global Granger-causal
  Markov property, an analogue of the causal Markov condition. No result
  here needs faithfulness.
- **[NOTE-tmp5fslk](NOTE-tmp5fslk.md) (Seth 2010).** A macro variable that is a function of the
  micro variables at the same time cannot be intervened on as Assumption
  2.3(i) requires. So Granger causation from it to its micro variables is
  not an effect in this paper's sense. My inference; filed as
  [CLAIM-tmpa4kr6](../claims.d/CLAIM-tmpa4kr6.md).

## Bearing on the record

- Filed as [THEORY-tmp4g68i](../theory.d/THEORY-tmp4g68i.md). It answers [NOTE-010](NOTE-010.md)'s C5, which is
  annotated, and grounds [CLAIM-tmp6nu4a](../claims.d/CLAIM-tmp6nu4a.md).
- [NOTE-tmp2veo7](NOTE-tmp2veo7.md)'s C4 says only perturbation identifies physical causation
  "unambiguously". By this paper observational data identify it too, but
  only under Assumption 2.3, which the data cannot test. So "unambiguously"
  is the word that keeps C4 true.
- **For the Anthology of the SOTA:** no instruction for ML practice.

## Limitations

- Every result is a sufficient condition. Nothing says when an effect is
  not identifiable.
- Assumption 2.3 is untestable from observational data. The paper says it
  must be believed "based on substantive background knowledge".
- C4 is stated in the conclusion as easily seen, and C5's proof is not in
  the paper.
- The examples are linear Gaussian. The definitions are general, but the
  computation of effects is shown only for the Gaussian case.
- Excluding instantaneous causality makes the results depend on the
  sampling interval, which the paper notes is "often chosen arbitrarily"
  (§4.1) while declining a per-time-point graph for that reason.

## Open questions

- Sequential interventions at several times (the authors', §5).
- Necessary conditions for identification, the analogue of completeness
  results for DAGs.
- What survives when the sampling interval is coarser than the causal one,
  so that Assumption 2.3(i) fails by aggregation.
