---
number: 815
status: Read
formerly:
- NOTE-tmpw3u6o
paper: LIT-971
title: 'Gerstgrasser et al. — Is Model Collapse Inevitable?'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from arXiv (2404.01413v2, 29 April 2024), text extracted
    with pdftotext: §§1–4, Appendix A (related work), Appendix B (both
    proofs, checked step by step), Appendices C–F (language-model
    ablations with Table 2, VAE details, the Replace-Multiple setting,
    and the extra linear-regression plots). The published COLM 2024
    version was not compared.
date: '2026-10-14'
summary: >-
  In a fixed-design linear regression refit each round to labels drawn
  from the previous fit, keeping every earlier round's data gives test
  error σ²d/(T−d−1)·Σ1/i², bounded by π²/6 times the first fit's, where
  replacing the data gives σ²d/(T−d−1)·n. The error still rises every
  round. Small language models and a diffusion model on accumulated data
  hold their test loss over five to eight rounds; a VAE's still rises,
  more slowly.
---
<!-- inactive-ok-file: CLAIM-050 CLAIM-056 CLAIM-081 CLAIM-199 THEORY-155 THEORY-289 — Proposed; the claims and accounts this reading bears on, and the one it produces, open -->

# NOTE-815: Gerstgrasser et al. — Is Model Collapse Inevitable?

## Contribution

Earlier model-collapse studies mostly replaced each generation's training
data with the previous model's samples. This paper keeps the real data
and adds each generation's samples to it. In that setting the test loss
of language models, a molecular diffusion model and (more weakly) a VAE
stops growing with generations, and in the linear-regression framework of
Dohmatob et al. the test error has a closed form that is bounded in the
number of rounds.

## Key insight

When data accumulate, round i's fresh sampling noise is one share in i of
the training set, so its effect on the estimate is scaled by 1/i and its
effect on squared error by 1/i². The squares are summable, so the error
converges. Replacing data gives each round's noise full weight, and the
errors add.

## Assumptions

For the theorems (§3, App. B):

- **Linear-Gaussian data.** x ~ N(0, Σ), y = x·w* + ε, ε ~ N(0, σ²).
- **Fixed design.** The same T × d matrix X of real covariates is reused
  every round; only the labels are regenerated, Ŷ_{n+1} = X·ŵ_n + E_{n+1},
  with fresh noise E_{n+1} ~ N(0, σ²I_T) of the *same* variance as the
  real label noise.
- **Under-parameterised, ridgeless OLS.** T ≥ d (T ≥ d + 2 for
  Theorem 2), X full column rank.
- **Isotropic features for Theorem 2,** Σ = I_d.
- **"Model collapse" means test error diverging with rounds** (footnote
  3); bounded error counts as avoiding it.

For the experiments (§2): one run per configuration as far as reported,
five rounds for the language models (ten for replace), eight for the
diffusion model and VAE; each round trains a fresh model.

## Key results

- **Theorem 1.** Under accumulation, for all n ≥ 1,
  ŵ_n = w* + (XᵀX)⁻¹Xᵀ·Σ_{i=1}^{n} E_i / i. Proved by induction
  (App. B).
- **Theorem 2.** With Σ = I_d and T ≥ d + 2,
  E_test^Accum(ŵ_n) = σ²d/(T−d−1) · Σ_{i=1}^{n} 1/i²
  ≤ σ²d/(T−d−1) · π²/6. Uses E[(XᵀX)⁻¹] = I/(T−d−1) (Lemma 3, from
  Dohmatob et al.).
- **Replace (Dohmatob et al., eq. 4).** E_test^Replace(ŵ_n) =
  σ²d/(T−d−1) · n.
- **Replace-Multiple (App. E, eq. 11).** Fitting round i to T·i fresh
  samples from the previous model alone gives σ²d/(T−d−1) · Σ 1/k ≈
  σ²d/(T−d−1) · log n: slower, still unbounded.
- **Numerics (Fig. 7, Fig. 16).** Simulation matches the formulas for
  d = 10 and 32, T ∈ {100, 316, 1000}, σ² from 0.01 to 100, up to 200
  rounds.
- **Language models (§2.1, Table 2).** GPT-2 9M and Llama-2 12M/42M/126M
  on TinyStories, one epoch per round. Test cross-entropy at round 4,
  against round 1: accumulate −0.06 to −0.28; replace +0.53 to +0.66 at
  temperature 1.0 and +4.00 at temperature 0.3 (GPT-2); replace with
  data grown to the accumulated size, +0.35 to +0.36.
- **Diffusion (§2.2, Fig. 4).** GeoDiff on 40,000 GEOM-Drugs
  conformations: under replace, loss jumps at the first synthetic round
  and then stays roughly flat; under accumulate, roughly constant.
- **VAE (§2.3, Figs. 5–6, 15).** CelebA 64×64: under replace, samples
  collapse to one mode; under accumulate, test error "does increase with
  the number of iterations (albeit much more slowly)", samples lose
  minor features (glasses, hats) while reconstructions keep them.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | In the fixed-design linear model, accumulation gives test error σ²d/(T−d−1)·Σ1/i², bounded by π²/6 times the first round's | strong | Theorem 2, proved |
| C2 | In the linear model, under accumulation the error still rises with every round and never falls below the first round's | strong | Theorem 2's sum is increasing in n (not stated by the authors as such); the language models' loss instead fell slightly (Table 2) |
| C3 | Matching the amount of data does not remove collapse: what bounds it is keeping the earlier (real) data | moderate | Replace-Multiple, eq. 11 and Table 2's (*) column |
| C4 | Small language models trained on accumulated data keep their test loss over five rounds | moderate | Table 2, Fig. 2; single runs |
| C5 | Accumulation avoids collapse across model families | weak | holds for the language and diffusion models; the VAE's error still rises |

## Concepts

- **Replace / accumulate / replace-multiple.** Train round n on only the
  newest synthetic set; on the real data plus every synthetic set so
  far; on a synthetic set from the newest model as large as the
  accumulated one.
- **Model collapse (as used here).** Test error growing without bound in
  the number of rounds. The authors list three other uses in the
  literature: collapse to a few modes, to uniformity, and amplification
  of artifacts (§4).

## Connections

It extends Dohmatob, Feng and Kempe (2024a), "Model collapse demystified",
from replace to accumulate, and reuses their Lemma 3. Marchi et al.
(2024) obtained the same square-summable variance independently.
Alemohammad et al. (2023) ran one accumulating experiment and concluded
that real data "only delays" degradation; this paper reads their plot as
a plateau. Martínez et al. (2023a) found fast deterioration even with
accumulation on a small dataset; the paper leaves the discrepancy open.
Mobahi et al. (2020) study the noiseless case (self-distillation), where
predictions shrink to zero.

## Bearing on the record

- **[QUESTION-016](../questions.d/QUESTION-016.md)** (when does iterated
  reconstruction preserve or destroy task-relative sufficiency). The LIT
  registered the paper as "a case of retained side information stopping
  the loss of sufficiency". The paper supports something narrower.
  - *The loss is bounded, not stopped.* Σ_{i≤n} 1/i² increases with n,
    so every round adds error; the limit is π²/6 ≈ 1.64 times the first
    model's.
  - *What is retained is the source, not side information.* The real
    sample stays in every round's training pool. That is not an
    interpreter's side information in [QUESTION-016](../questions.d/QUESTION-016.md)'s sense (A86 §3).
  - *It is still a pure chain from the real sample.* By Theorem 1 every
    ŵ_n is the first-round estimate plus independent noise. So each
    model is a garbling of the real data, and nothing in the paper
    contradicts the question's point that sufficiency can only decline
    along such a chain. The paper shows how slowly it can decline, for
    one task.
  - *The task is a single one.* Squared-error prediction under the
    original distribution, not a family Q of decision problems
    ([CLAIM-050](../claims.d/CLAIM-050.md)).
- **[CLAIM-267](../claims.d/CLAIM-267.md)** (and
  [CLAIM-056](../claims.d/CLAIM-056.md)): with e_(i+1) ≤ L_i·e_i + ε_i,
  end-to-end error is bounded by the discrepancies weighted by the later
  Lipschitz constants. Accumulation is an exact instance in which the
  per-round discrepancy is scaled by 1/i, so the weighted sum converges;
  replacement is the case in which it is not, and the errors add
  linearly. It is the record's first closed-form example of the
  "accumulated but bounded" regime.
- **[CLAIM-081](../claims.d/CLAIM-081.md)** (retaining the ancestor and
  drifting are different profiles). The VAE under accumulation is a
  measured case: reconstructions keep the minor features while samples
  drift away from them (App. D, Fig. 15). Shown in pictures only.
- **[THEORY-155](../theory.d/THEORY-155.md)** (Bayesian iterated learning
  converges to the prior). A contrasting chain. There the data are
  replaced and the chain forgets its start; here the start is kept in the
  pool and the chain stays near it.
- **[CLAIM-199](../claims.d/CLAIM-199.md)** (a garbling can raise a
  receiver's usable information but never above the source). Consistent:
  no round here beats the first.
- **A new THEORY is filed** for C1–C3: [THEORY-289](../theory.d/THEORY-289.md).
- **ML practice.** The paper's message for training on web data that
  contains model outputs (accumulate, do not replace) is advice for
  practice and is not filed here.

## Limitations

- The theory reuses the real covariates X every round and regenerates
  only the labels, with noise of exactly the real variance. It is silent
  on covariate drift, on mode loss, and on any mechanism other than
  added label noise.
- The experiments are short (five rounds for language models), appear to
  be single runs, and report no error bars.
- For the VAE, accumulation slowed collapse but did not stop it, which
  the abstract does not say.
- "Avoids model collapse" is defined as bounded test error. Under other
  definitions the authors themselves list (mode collapse, artifact
  amplification), the theorem says nothing.

## Open questions

- Does the bound survive covariate regeneration (sampling x from the
  model as well), or a model class whose per-round error is not
  additive? A nonlinear or over-parameterised version of Theorem 2 would
  settle it.
- Do the VAE's rising error and the language models' flat error reflect
  the model class or the task? The same accumulation protocol over more
  rounds and seeds, across classes, would tell.
