---
status: Read
paper: LIT-tmp3u0k8
title: 'Griffiths and Ghahramani — Infinite latent feature models and the Indian buffet process'
version: 1
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Read in full on 2026-10-27 from the NeurIPS proceedings' own PDF
    (https://papers.nips.cc/paper_files/paper/2005/file/2ef35a8b78b572a47f56846acbeef5d3-Paper.pdf,
    8 pages), text extracted with pdftotext. Read: the abstract, §§1–4,
    the captions of Figures 1–3 and the 15 references. Figure 3's trace
    plots were read from the caption and the text only; no number was
    taken from a chart. Equations (2)–(7) were checked against the text
    where extraction garbled them. The limit (4) and the buffet's
    distribution were checked numerically on lof-classes (record script,
    2026-10-27). The Gatsby technical report the paper defers to was not
    read.
date: '2026-10-27'
summary: >-
  Introduces the Indian buffet process: the finite beta–Bernoulli feature
  model with π_k ~ Beta(α/K, 1) has a limit as K → ∞ on left-ordered
  equivalence classes, eq. (4), and a sequential buffet produces the same
  distribution, so objects are exchangeable and K+ ~ Poisson(αH_N). Used
  as the prior of an infinite binary linear-Gaussian model, its Gibbs
  sampler settles on about seven features for 100 photographs of four
  objects. The paper is the original of the authors' 2011 review.
---
<!-- inactive-ok-file: CASE-165 CLAIM-454 — Proposed; the construction and claim this reading bears on, cited as open -->

# NOTE-tmpit34t: Griffiths and Ghahramani — Infinite latent feature models and the Indian buffet process

## Contribution

It does for latent features what the Chinese restaurant process did for
latent classes. A finite model with K features is written down, its
feature probabilities are integrated out, and the limit K → ∞ is taken on
equivalence classes that ignore the order of columns. The limit is an
exchangeable distribution over binary matrices with N rows and an
unbounded number of columns, of which finitely many are non-zero. A
sequential "buffet" generates it. It is the first paper on the IBP; the
review of 2011 (LIT-1556) expands it.

## Key insight

Feature labels are not identifiable, so the limit has to be taken on what
survives relabelling. The left-ordered form (columns sorted by the binary
number they spell, first row most significant) plays the role a partition
plays for class assignments. On these classes the K → ∞ limit is finite
and simple, and a process with the rich-get-richer form of the Chinese
restaurant process produces it.

## Assumptions

- **Finite model (§2.1).** z_ik | π_k ~ Bernoulli(π_k), π_k | α ~
  Beta(α/K, 1), all independent. Integrating π out gives (2), P(Z) =
  ∏_k (α/K)Γ(m_k + α/K)Γ(N − m_k + 1)/Γ(N + 1 + α/K), exchangeable in the
  objects.
- **Equivalence classes (§2.2).** Two matrices are equivalent if lof(·)
  maps them to the same left-ordered matrix. A class has
  K!/∏_{h=0}^{2^N − 1} K_h! members, K_h the number of columns with full
  history h. Inference on classes is appropriate when p(X | F) does not
  depend on the order of the columns, as in PCA or CVQ.
- **The likelihood (§3).** x_i ~ N(z_i A, σ_X² I), A ~ N(0, σ_A² I);
  integrating A out gives (8), which depends only on Z's non-zero
  columns and so stays defined as K → ∞.

## Key results

- **The limit (4).** P([Z]) → α^{K+}/∏_{h ≥ 1} K_h! · exp{−αH_N} ·
  ∏_{k ≤ K+} (N − m_k)!(m_k − 1)!/N!, with H_N the N-th harmonic number.
  It is infinitely exchangeable. "Technical details of this limit are
  provided in [13]", the technical report.
- **The buffet (§2.4).** The first customer takes Poisson(α) dishes;
  customer i takes each earlier dish with probability m_k/i, then
  Poisson(α/i) new ones. The buffet's matrices (5) are not left-ordered
  and their customers are not exchangeable, but ∏_i K₁⁽ⁱ⁾!/∏_h K_h! of
  them map to each left-ordered form, and summing gives (4).
- **Conditionals (§2.5).** Finite: P(z_ik = 1 | z_−i,k) = (m_−i,k +
  α/K)/(N + α/K), (6). Infinite: m_−i,k/N for features others hold, (7),
  and Poisson(α/N) new features for object i.
- **Demonstration (§3).** 100 webcam images, 240 × 320, reduced to the
  mean and the first 99 principal components; each holds each of four
  objects (a $20 bill, a Klein bottle, a prehistoric handaxe, a cellphone)
  with probability 0.5. The sampler starts at K+ = 1 with σ_A, σ_X and α
  at 0.5, 1.7 and 1, sampled by Metropolis steps; all stabilize after
  about 100 iterations, "with the algorithm finding solutions with
  approximately seven latent features". The four commonest "perfectly
  indicated the presence and absence of the four objects", and three less
  common ones "coded for slight differences in the locations of those
  objects". By the caption, the first indicates the bill's presence and
  the other three the absence of the Klein bottle, the handaxe and the
  cellphone.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The finite model's lof-class probability converges to (4) as K → ∞ | strong, details deferred | §2.3; checked numerically (THEORY-tmpo1cju) |
| C2 | The Indian buffet process generates the same distribution on lof-classes | strong | §2.4; checked by simulation (THEORY-tmpo1cju) |
| C3 | The infinite conditional is m_−i,k/N with Poisson(α/N) new features | strong | (7), from exchangeability and the limit of (6) |
| C4 | The linear-Gaussian likelihood depends only on the non-zero columns of Z | strong | (8) |
| C5 | Gibbs sampling with an IBP prior recovers the four objects from staged photographs | weak | one run, one dataset built to suit the model, no comparison |

## Concepts

- **lof(Z)**: the left-ordered form; columns sorted by the binary number
  they spell, first row most significant.
- **History of feature k at object i**: (z_1k, …, z_(i−1)k), indexed by
  its decimal value.
- **K+**: the number of features held by at least one object.
- **Indian buffet process**: the sequential process above, named for
  London's Indian buffets, "with an apparently infinite number of
  dishes".

## Connections

The review of 2011 (LIT-1556, NOTE-1172) is this paper's long version:
the same derivation, the same demonstration, the two-parameter and
stick-breaking variants added. The stick-breaking construction is Teh,
Görür and Ghahramani's (LIT-tmpfhqac). The beta process as the IBP's de
Finetti measure is Thibaux and Jordan's (LIT-1537, THEORY-985). The
Markov IBP (LIT-1577) repeats this paper's finite-model-and-limit
argument for rows that are time steps. Knowles and Ghahramani (LIT-tmpezspt)
use the IBP as the mask of an infinite ICA, the model the infinite
factorial HMM's experiments compare against. The paper's reference [4],
Ghahramani's factorial learning, and the factorial models it calls CVQ are
the static ancestors of factorial HMMs (LIT-tmpkxifq).

## Bearing on the record

- **CASE-165, item 1.** The αH_N the case says T23 quotes is this
  paper's, and as here it belongs to the limit only. The paper gives
  K+ ~ Poisson(αH_N) only implicitly, through the buffet's Poisson(α/i)
  new dishes; it gives no count of occupied features for the finite
  model, as the review does not (THEORY-999). So the case's correction,
  6.83 at K = 16 against 9.31, has no counterpart in the original either.
- **CASE-165, item 4.** The case cites "the review's own worked example"
  for absence-coding features and split features. The example is this
  paper's, in the same words ("three less common features coded for
  slight differences in the locations of those objects"); the caption
  says three of the four main features code absence. The review repeats
  it. The case's point stands on the original, which explains neither
  the absence coding nor the split features.

No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **The limit is stated, not derived**, in the paper: the rearrangement
  displayed above (4) is a sketch, and the details are in the technical
  report.
- **No count for finite K.** The paper's finite model is used only to
  take the limit.
- **One demonstration**, one run, data built to match the model (four
  objects, each present with probability 0.5), no held-out evaluation and
  no comparison with a finite model.
- **Errors and slips.** None of substance found. "A feature possessed by
  both previous objects were assigned" (§2.2) is a garbled sentence; the
  text gives the images as 240 × 320 pixels and the caption as 320 × 240;
  the NeurIPS site and its BibTeX reverse the authors' order.

## Open questions

- What does the finite model at the K a practitioner would use (CASE-165's
  16) do to the posterior, rather than to the prior's count?
