---
number: 796
status: Read
formerly:
- NOTE-tmplnu3m
paper: LIT-984
title: 'Gu et al. — Data Mixing Can Induce Phase Transitions in Knowledge Acquisition'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from arXiv (2505.18091v3, 10 May 2026, the NeurIPS 2025
    version), text extracted with pdftotext: §§1–7, Appendices A–D, the
    dataset, fitting and threshold-estimation details of Appendix E
    (E.1–E.6; the CKM and downstream tables of E.7 and D.7 only for their
    headline numbers), and every proof in Appendix F. The orientation of
    the fraction r/(1−r) in Theorem 4.3 was checked against the
    non-layout extraction, since the layout text renders it ambiguously.
date: '2026-10-14'
summary: >-
  An optimal capacity-bounded learner, given a mixture of equally frequent
  random facts and a second domain, learns none of the facts until the
  second domain's marginal loss reduction per unit of capacity falls below
  r·p/(1−r), then all of them within Htot more capacity. Pythia models
  trained on synthetic biographies mixed into web text show near-zero
  recall below a threshold model size and mixing ratio, and 4–16 times
  more training barely moves it.
---
<!-- inactive-ok-file: THEORY-187 THEORY-204 THEORY-039 THEORY-229 THEORY-293 — Proposed; the accounts this reading is compared with, and the one it produces, not leaned on -->

# NOTE-796: Gu et al. — Data Mixing Can Induce Phase Transitions in Knowledge Acquisition

## Contribution

Before this paper, controlled studies (Allen-Zhu and Li) had found that
the facts a language model stores grow linearly with its size when it is
trained on knowledge-dense data alone. This paper shows that when the same
data are a fraction r of a web-text mixture, recall is near zero below a
critical model size and below a critical mixing ratio, and rises steeply
past them. It gives a capacity-allocation account: for an idealised
optimal learner with a capacity budget measured in bits, the allocation to
the facts jumps from none to all as capacity or r crosses a threshold.

## Key insight

A learner with a fixed budget spends it where it buys the most loss
reduction. Every fact has the same small marginal value, r·p per bit,
while the web domain's marginal value starts high and declines. So the
facts are worth nothing to the learner until the web's marginal value has
fallen below theirs, and then they are all worth taking. The threshold is
an onset set by a comparison of marginal values, not by how often or how
long the facts are seen.

## Assumptions

- **The learner is optimal under a capacity bound** (Definition 4.1). Its
  capacity is the mutual information I(A(D_θ); D_θ) ≤ M between the
  trained model and the data distribution. A trained network is *modelled*
  as such a learner; nothing in the paper shows that SGD finds the optimum.
- **Facts are uniform and independent.** K facts, disjoint input sets,
  targets drawn independently, all with the same exposure frequency p
  (Definition F.2).
- **The two domains are orthogonal** (Definition F.5): no input shared
  across domains has its next-token distribution depend on θ₁ or θ₂, and
  the two latents are independent. Real knowledge overlaps with web text;
  the theory assumes it does not.
- **For the closed forms only:** the web domain's best loss is a power law
  in capacity, F_P2(M) = C + A·M^(−α), with α ∈ (0, 1).
- **Experiments:** Pythia architecture, 14M–6.9B parameters, WSD schedule,
  peak learning rate 10⁻³, batch 512 × 2048 tokens; most runs single-seed
  (Appendix A gives cost as the reason). SynBio repeats many times per run
  (about 100 passes at r = 0.1 over 32B tokens), the web data less than
  once.

## Key results

- **Theorem 4.2 (facts alone).** With all K facts at exposure frequency p,
  F_P(M) = C + p·max{Htot − M, 0}, where Htot = Σᵢ H(Yᵢ). Loss falls
  linearly in capacity: no transition. *Holds when:* the factual universe
  of Definition F.2.
- **Theorem 4.3 / F.9 (mixture).** With M₀⁻(t) = sup{M : −F′_P2(M) > t}
  and M₀⁺(t) = inf{M : −F′_P2(M) < t}, any optimal M-bounded learner
  learns nothing of the facts (L̄₁ = F_P1(0)) if M ≤ M₀⁻(r·p/(1−r)), and
  learns them all (L̄₁ = F_P1(∞)) if M ≥ M₀⁺(r·p/(1−r)) + Htot. *Holds
  when:* orthogonal mixture, uniform facts; F_P2 convex (Lemma F.1, by the
  rate–distortion argument).
- **Power-law case (eqs. 4–6).** With F_P2 = C + A·M^(−α):
  M_thres ~ (1/(r·p))^(1/(α+1)), r_thres ~ 1/(p·M^(α+1)), and a single
  fact's threshold frequency f_thres ~ M^(−(α+1)). *Holds when:* the power
  law holds for the web domain.
- **Threshold in model size (§3.1, Fig. 1).** For r ∈ {0.1, 0.2, 0.3, 0.4},
  SynBio-320k plus FineWeb-Edu, 32B tokens, 14M–410M models: accuracy
  near zero, then above 60% past a size that falls as r rises.
- **Threshold in mixing ratio (§3.2, Fig. 2, Table 1).** 70M models: mean
  accuracy 0.4% at r = 0.1–0.2, 0.8% at 0.25, 7.3% at 0.3, 27.5% at 0.35,
  58.1% at 0.45 (three seeds, s.d. ≤ 3.1). 410M models: near zero for
  r ≤ 0.3, about 80% at r = 0.4. Pythia-2.8B and 6.9B show the same shape
  at r of a few percent with smaller SynBio sets (Fig. 9). Validation loss
  shows it too (Fig. 10).
- **Training longer barely helps (§3.2, Figs. 3–4).** At r = 0.2, 512B
  tokens (about 3000 exposures per biography for 70M, 200 for 410M) leave
  accuracy near zero. Steps T to 40% accuracy grow linearly in 1/r for
  r > 0.4. Below that they exceed a power-law fit (T ≈ 0.098·r^(−3.84),
  R² = 0.985) by more than 2.9× at r = 0.25 and 1.9× at r = 0.2, and
  exceed an exponential fit (log T = −0.255 + 1.514/r, R² = 0.998) by more
  than 2× at r = 0.25 (App. E.5).
- **The threshold frequency is a power law in size (§5, Fig. 7).** On
  SynBio-10k with power-law subset frequencies at r = 0.01, log f_thres
  against log M has slope −1.152; the fitted web exponent α ≈ 0.283
  predicts −1.283. Across Llama-2, Qwen-2.5 and Gemma-2 base models, the
  PopQA popularity threshold falls linearly in log size, with family-specific
  slopes.
- **Reasoning subtasks (§3.3, App. D.3).** Slope calculation inside
  OpenWebMath and a max-of-30-integers task show the same thresholds in
  size and r. The max task reaches 60% from fewer than 3,500 unique
  examples out of 10⁶⁰ inputs.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | An optimal capacity-bounded learner on an orthogonal mixture learns none of a set of equally frequent facts below a capacity threshold, and all of them within Htot above it | strong | Theorem 4.3, proved (App. F.3) |
| C2 | With a power-law loss on the other domain, the threshold size scales as (1/rp)^(1/(α+1)) | strong (given the power law) | eqs. 4–6 |
| C3 | Pythia models on SynBio + web text show near-zero recall below a threshold model size and mixing ratio, then a steep rise | moderate | Figs. 1–2, 9; one seed except Table 1 |
| C4 | Below the threshold ratio, much longer training barely helps: steps to a target accuracy grow faster than exponentially in 1/r | moderate | Figs. 3–4; extrapolation of fits over r ∈ [0.2, 0.55] |
| C5 | The trained networks' thresholds are the optimal learner's thresholds | weak | consistency of shape and of one exponent (1.152 against 1.283) |
| C6 | The threshold frequency for a fact falls as a power law in model size in open model families | weak | PopQA, page views as a frequency proxy, an LLM judge, family-specific slopes |

## Concepts

- **Mixing ratio r.** Fraction of training tokens from the knowledge-dense
  set.
- **Exposure frequency p.** Probability that an input belonging to a given
  fact occurs in the knowledge-dense distribution; r·p is its frequency in
  the mixture.
- **Capacity.** I(A(D_θ); D_θ), the bits a trained model carries about
  the data distribution; Allen-Zhu and Li's estimate is about 2 bits per
  parameter.
- **Marginal value.** Reduction in total test loss bought by one more unit
  of capacity assigned to a domain; r·p for the facts, (1−r)·(−F′_P2(M))
  for the web.
- **Threshold frequency f_thres.** Lowest per-fact frequency at which a
  model of size M learns the fact.

## Connections

It extends Allen-Zhu and Li's knowledge-capacity scaling (2024) from pure
to mixed data, and reads the frequency effects of Kandpal et al. and
Mallen et al. (long-tail facts are poorly recalled) as a threshold. The
learner is defined information-theoretically, by a rate–distortion
argument, as in the record's capacity-based accounts. Zucchet et al. (2025)
report a plateau before fact acquisition in training dynamics; this paper
does not model dynamics.

## Bearing on the record

- **[QUESTION-039](../questions.d/QUESTION-039.md)**, which asks what sets
  the moment a network acquires a structure and whether acquisition is
  one kind of event. The paper adds a threshold mechanism of a new kind:
  competition for capacity between domains. The threshold depends on the
  frequency of the structure *relative to the marginal value of everything
  else*, not on its own statistics alone. Two cautions for the question.
  - The theory is static: it says which allocation the optimum takes at
    each M and r, and nothing about *when in training* it is reached. The
    training-time result (superexponential T in 1/r) is empirical and
    unexplained by the theory.
  - In the theory the "transition" is an onset, not a jump. Above
    M₀ the web domain's share stays fixed and every further bit goes to
    the facts until Htot is spent, so recall rises linearly in M over a
    width of Htot. It looks abrupt only when Htot is small beside M₀.
- **Against the mechanisms the question holds.**
  [THEORY-086](../theory.d/THEORY-086.md),
  [THEORY-187](../theory.d/THEORY-187.md) and
  [THEORY-229](../theory.d/THEORY-229.md) time acquisition by
  eigenvalue and initial scale within one task.
  [THEORY-204](../theory.d/THEORY-204.md) sets a horizon by data size.
  This paper sets a threshold by a ratio of marginal values between
  tasks, measured in bits of capacity. The quantities are different, and
  no setting in the paper puts two of them side by side, which is what
  the question says would answer it.
- **[THEORY-039](../theory.d/THEORY-039.md)** cautions that later phases
  "differ in kind". This is a further kind: a transition in what is
  learned at the end of training as a function of mixture and size, not
  a phase within one run.
- **A new THEORY is filed** for C1–C4, at the strength the paper
  establishes: [THEORY-293](../theory.d/THEORY-293.md).
- **The LIT's seed summary** said that below the critical ratio the
  model "memorizes almost nothing however long it trains". The paper
  tested up to 16 times longer and fit step counts; "however long" is an
  extrapolation.
- **ML practice.** The two strategies of §6 (subsample the knowledge set;
  add compact rephrasings) and the takeaways on setting mixing ratios are
  instructions for practice. They belong to the Anthology's reading,
  [ANTH-LIT-451](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-451.md), not here.

## Limitations

- Most runs are single-seed; Table 1 gives three seeds for one sweep only.
- The link from the optimal learner to SGD-trained networks is asserted,
  and tested only by the shape of the curves and one exponent (1.152
  against the predicted 1.283, a 10% gap, without an interval).
- The orthogonality and uniform-frequency assumptions do not hold for
  real data; the authors say heterogeneous datasets may not show the
  transition, and that it should still hold per fact (§7).
- The PopQA test relies on page views as a frequency proxy and a
  Llama-3.1-8B judge. The judge prompt printed in Table 15 is a
  synonym-testing prompt, which does not match the description of a
  semantic-similarity judgement.
- The proof of Theorem F.8 states D⁺F_P1(0) = p; by Theorem 4.2 it is −p.
  The result is unaffected.

## Open questions

- Does SGD reach the capacity-optimal allocation, or is the training-time
  wall below r_thres a dynamical effect the static theory does not see?
  Tracking the loss on SynBio through training at r just below the
  threshold, for longer than 512B tokens, would separate the two.
- Is the threshold sharp for non-uniform facts? The theory with
  heterogeneous p would predict a graded onset fact by fact; the
  SynBio-10k power-law set is the place to test it.
