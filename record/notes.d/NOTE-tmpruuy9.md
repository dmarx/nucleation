---
status: Read
paper: LIT-tmpdyhv5
title: 'Balasubramanian and Kasiviswanathan — Forgetting in post-training'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Read on 2026-11-15 from arXiv:2603.12163v1, https://arxiv.org/pdf/2603.12163,
    text by pdftotext. Read: the abstract, §1 (setting, the two kinds of
    forgetting, the main results, Table 1), §2.5, the §3.2 discussion after
    Thm. 3.2, §3.3 with the OAPL set-up and Lemma 3.2, §4 and App. A.
    Skipped: the proofs, and the statements of Thms. 2.1–2.3 and 3.1–3.3 in
    detail; §1.2; App. B–E, including the finite-mixture extension. The
    proofs were not checked. The filer rechecked every quote below against
    the downloaded text, and added from it that Lemma 3.2 assumes the
    disjoint-support setting and step-wise constant rewards; the quoted
    sentences on OAPL are the discussion after the lemma, not its
    statement.
date: '2026-11-15'
summary: >-
  In a two-mode mixture, forward-KL SFT on new data collapses the old
  mode's weight; KL-regularized (reverse-KL) RL toward a target that keeps
  the old mode converges to it, with drift exponentially small in mode
  separation; an exponential tilt of a frozen reference only reweights
  modes it already has. States the KL-regularized optimum in closed form.
---
<!-- inactive-ok-file: THEORY-tmp9rnyv THEORY-tmpxu3kz — Proposed; new entries filed in the same contribution -->
<!-- inactive-ok-file: CLAIM-576 — Proposed; the claim this reading bears on -->

# NOTE-tmpruuy9: Balasubramanian and Kasiviswanathan — Forgetting in post-training

## Contribution

A population-level theory of forgetting in a two-component mixture,
target pα = α·po + (1 − α)·pn and learner qβ = β·qo + (1 − β)·qn, with po
and pn equal-covariance Gaussians at Mahalanobis separation δ, following
the two-mode model of Chen et al. (2025). It separates mass forgetting
(β⋆ = 0) from old-component drift (the old mean moves), and analyses SFT,
KL-regularized RL, replay and three near-on-policy methods (SDFT,
TTT-Discover, OAPL).

## Key insight

Which way the KL points decides what is lost. Forward KL on new data has no
reason to keep mass where it sees no data; reverse KL toward a target that
keeps the old mode only lets it drift through the overlap; and a tilt of a
reference can only reweight what the reference already holds.

## Assumptions

- Two modes (App. D: finite mixtures, not read); mostly equal-covariance
  Gaussians; in the main results the old component starts correct.
- The RL target explicitly keeps the old mode. Results are at the
  population level, under gradient flow.
- Lemma 3.2: the disjoint-support setting (Definition 1.1) and step-wise
  constant rewards.
- §1: "This setting is intentionally minimal".

## Key results

- **Thm. 2.1** (§1): forward-KL SFT on new data "is strictly increasing in
  β (even when the component shapes are already correct), so β⋆ = 0 is the
  unique population minimizer."
- **Thms. 2.2–2.3** (§1): reverse-KL RL can "converge to the true target
  (thereby avoiding mass forgetting)", and drift is "gated by misassignment
  probabilities that decay exponentially with mode separation".
- **§2.5**: "reverse-KL updates can adapt the new mode while perturbing an
  already-correct old mode only through exponentially small overlap
  regions." Purely on-policy optimisation can suffer "finite-batch
  starvation".
- **Replay** (§1, Table 1): for reverse KL, replay "does not alter the
  population objective" but prevents "old-mode starvation".
- **Near-on-policy methods** (§1): "TTT-Discover's entropic objective is
  intrinsically mode-seeking: without a sufficiently strong KL anchor it
  can still collapse mass onto the higher-reward mode"; OAPL's "target is an
  exponential tilt of a frozen reference policy: it can only preserve or
  reweight modes already present in that reference".
- **Lemma 3.2 and after** (§3.3): the OAPL target is again a two-component
  mixture with unchanged components, β⋆ = β0·e^{ro/τ}/(β0·e^{ro/τ} + (1 −
  β0)·e^{rn/τ}) (Eq. 3.18). "In the disjoint-support idealization, OAPL
  cannot create or destroy modes; it can only reweight the mass already
  present in the reference"; if the reference has already collapsed the
  old mode, "then OAPL cannot recover it in this idealization."
- **App. A**: for max_π E_π[r] − τ·KL(π‖πref), "The unique optimizer is the
  exponential tilt" π*(y) = πref(y)·e^{r(y)/τ}/Z; maximising the objective
  is minimising KL(π‖π*).

## Concepts

Mass forgetting; old-component drift; forward against reverse KL;
misassignment probability; Bhattacharyya overlap; numerator and
denominator replay; old-mode starvation; exponential tilt; mode-seeking.

## Bearing on the record

- **Yue et al. ([THEORY-tmp9rnyv](../theory.d/THEORY-tmp9rnyv.md))**: Lemma 3.2 is the formal counterpart of
  the sharpening reading. Under a fixed KL anchor the optimum is a tilt of
  the reference, which reweights and cannot add a mode the reference gives
  no mass. It holds in an idealization, and Yue et al. mostly train
  without KL; ProRL ([THEORY-tmpxu3kz](../theory.d/THEORY-tmpxu3kz.md)) resets its reference, so no fixed
  tilt applies there.
- **[QUESTION-392](../questions.d/QUESTION-392.md) and [CLAIM-576](../claims.d/CLAIM-576.md)**: a formal case of a process that can only
  reweight existing possibilities, which is the claim's line between
  selecting within a repertoire and altering it. Proposed for a dated note
  rather than a relation, since it is an idealization.
- **[CLAIM-567](../claims.d/CLAIM-567.md)**: weak. Mass collapse makes a feasible old mode unreachable
  by sampling.
- **On A's math**: the paper states A's π* ∝ π0 exp(r/β), with τ for the
  temperature and no prompt conditioning.

## Limitations

- Proofs not checked; a theory paper with toy models.
- Whether modes correspond to behaviours in language models is left to
  future work (§4).
