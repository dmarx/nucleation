---
status: Active
status_note: >-
  read 2026-11-15 (NOTE-tmpruuy9) from the arXiv PDF, v1: the abstract,
  §1 with Table 1, §2.5, the §3.2 discussion, §3.3 with Lemma 3.2, §4 and
  App. A; the proofs, the detailed statements of Thms. 2.1–2.3 and
  3.1–3.3, §1.2 and App. B–E not checked or skipped. Worth reading here as
  the formal counterpart of the sharpening reading of RL post-training: an
  exponential tilt of a frozen reference can reweight modes but not create
  or recover them, and forward-KL fine-tuning on new data alone collapses
  an old mode's weight. The only work in this batch that states the
  KL-regularized optimum in closed form.
title: 'A Quantitative Characterization of Forgetting in Post-Training'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Registered and read on 2026-11-15 from the owner's pasted continuation
    of the ChatGPT exchange "Explain String Theory", in A's turn on loss of
    mass on old modes against drift within modes in post-training. A gave
    authors, year and topic only; an arXiv author search for both surnames
    returned eight 2026 papers, of which this alone matches (its abstract
    names "mass forgetting, where the old mixture weight collapses to zero"
    and "old-component drift"). Checked on the arXiv API: Krishnakumar
    Balasubramanian (UC Davis and Amazon) and Shiva Prasad Kasiviswanathan
    (Amazon); v1 submitted 2026-03-12, the only version, which is
    `published:` and the copy read. No journal-ref, so filed as a
    preprint. OpenAlex and Semantic Scholar both refused with HTTP 429 and
    were not retried. No email address was sent to any service. The record
    held no LIT for this work.
tags:
- learning-theory
- probabilistic-modeling
- anthology-candidate
date: '2026-11-15'
published: '2026-03-12'
arxiv: '2603.12163'
first_author: 'Balasubramanian'
keywords:
- 'catastrophic forgetting'
- 'post-training'
- 'mass forgetting'
- 'old-component drift'
- 'forward KL'
- 'reverse KL'
- 'replay'
- 'exponential tilt'
implementations: []
summary: >-
  Balasubramanian & Kasiviswanathan (2026), arXiv:2603.12163. In a two-mode
  Gaussian mixture, forward-KL SFT on new data alone drives the old mode's
  weight to zero even with the components exactly right, while
  KL-regularized RL toward a target that keeps the old mode converges to
  it and moves the old mean only through overlap terms that decay
  exponentially with separation. An exponential tilt of a frozen reference
  "cannot create or destroy modes" (Lemma 3.2). Here as the idealized
  counterpart of Yue et al.'s sharpening (LIT-tmpfmva5), bearing on
  QUESTION-392. Its account is THEORY-tmppt44k.
---
<!-- inactive-ok-file: THEORY-tmppt44k — Proposed; new entries filed in the same contribution -->

# LIT-tmpdyhv5: A Quantitative Characterization of Forgetting in Post-Training

Balasubramanian, K. & Kasiviswanathan, S. P. (2026). A Quantitative
Characterization of Forgetting in Post-Training. arXiv preprint
arXiv:2603.12163.

## Key takeaways

*From the reading, NOTE-tmpruuy9.*

- **Forward KL forgets mass** (§1, Thm. 2.1): the new-data SFT objective "is
  strictly increasing in β (even when the component shapes are already
  correct), so β⋆ = 0 is the unique population minimizer".
- **Reverse KL does not** (§1, Thms. 2.2–2.3): KL-regularized RL toward the
  mixture target converges "to the true target (thereby avoiding mass
  forgetting)", with drift "gated by misassignment probabilities that decay
  exponentially with mode separation".
- **A tilt cannot create modes** (Lemma 3.2): "OAPL cannot create or
  destroy modes; it can only reweight the mass already present in the
  reference"; if the reference has lost the old mode, "then OAPL cannot
  recover it in this idealization."
- **The closed form** (App. A): for max E_π[r] − τ·KL(π‖πref), "The unique
  optimizer is the exponential tilt" π*(y) ∝ πref(y)·e^{r(y)/τ}.

## Standing in the record

A's characterization holds: the paper separates loss of mass on old modes
from drift within a mode, in a setting the authors call "intentionally
minimal". On A's math, the reader's verdict: this paper does state
π* ∝ π0 exp(r/β), as the unique optimizer of the KL-regularized objective,
with temperature τ (β is the mixture weight here) and with no conditioning
on a prompt. Lemma 3.2 supports A's sharpening framing within the
idealization, which assumes disjoint support. Its advice on replay and
anchors is ML practice and belongs to the anthology (ADR-048); hence the
flag.
