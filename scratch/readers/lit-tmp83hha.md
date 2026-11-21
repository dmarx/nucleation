# Reader notes: LIT-tmp83hha, "Does SGD really happen in tiny subspaces?"

Song, Ahn & Yun, ICLR 2025, arXiv 2405.16002. Read 2026-11-21.

## Provenance

- **Read**: the arXiv e-print (LaTeX source), https://arxiv.org/e-print/2405.16002,
  fetched 2026-11-21; gzip tarball, last modified 2025-03-12, with
  `\iclrfinalcopy` set (the ICLR 2025 camera-ready text). Kind: arXiv, the
  authors' own deposit. Read `main.tex` in full: abstract, §§1–6, the
  appendix (related work, experimental details, CE loss and standard
  architectures, GD-vs-SGD, noise scale, distance from switching step,
  toy model, EoS/SAM, SGDM/Adam, effective learning rates, sharpness
  plots, test accuracy).
- **Skipped**: the figures themselves (PDF plots in the tarball were not
  rendered); results are taken from the text and captions.
- **Also located**: https://arxiv.org/pdf/2405.16002 (arXiv PDF, lawful),
  downloaded 2026-11-21 without obstacle, not needed beyond the source.
- No obstacle, bot check or refusal met. No email address sent anywhere.
  Downloads in scratchpad/downloads/lit-tmp83hha/, not in the repository.

## Summary

Gur-Ari et al. (2018) observed that SGD gradients lie mostly in the span of
the top-k eigenvectors of the training-loss Hessian (k = number of classes).
The paper asks whether networks can therefore be trained inside that span
(Q1). They cannot: projecting each update onto the top-k span (Dom-SGD)
stops the training loss falling; projecting it onto the orthogonal
complement (Bulk-SGD) trains as well as SGD. The alignment is "spurious":
in the small-learning-rate (GF) regime it is caused by SGD noise kicking
iterates up the walls of a steep, ill-conditioned valley, and it vanishes
under full-batch GD; at the Edge of Stability it comes from
self-stabilizing oscillation. The same holds for SAM, momentum and Adam,
and momentum and Adam raise the effective step in the bulk.

## Definitions (exact)

- Hessian: of the training loss L: R^p → R, ∇²L(θ), eigenvalues
  λ₁ ≥ … ≥ λ_p, eigenvectors u_i (§2, Notations). Parameter space.
- **Dominant subspace** (Definition 1): "S_k(θ) := Span{u_i(θ): i∈[k]}, and
  its orthogonal complement by S_k^⊥(θ), referred to as the bulk subspace.
  Unless specified otherwise, the default choice for k is the number of
  classes" (k = 10 for MNIST/CIFAR, 2 for SST2).
- So "bulk" is the whole (p − k)-dimensional complement, every eigenvalue
  below the top k, including any negative ones; it is not a small set of
  smallest-eigenvalue directions.
- χ_k(v) = ‖P_k v‖/‖v‖, the fraction of a vector in the dominant subspace.
- Dom-SGD: θ ← θ − η P_k(θ) g_t; Bulk-SGD: θ ← θ − η P_k^⊥(θ) g_t; the
  subspace is "recompute[d] … at every step".

## Experiments

- Models: 3-layer tanh MLP (width 200), 3-layer ReLU CNN (width 32), 2-layer
  Transformer (dim 64, 8 heads); also VGG11 and ResNet8 (App.). Data: first
  5000 MNIST, first 5000 CIFAR10, first 1000 SST2. Loss: categorical MSE
  mainly; cross-entropy in the appendix. Batch 50; constant learning rate
  (0.01, 0.001, 0.001 in the GF runs).
- Switch from SGD to Dom-/Bulk-SGD when the EMA of χ_k exceeds 0.95.
  Switching happens at ~53% training accuracy (CNN/CIFAR10-5k) and ~69%
  (Transformer/SST2-1k), so "not the end-of-training phenomenon" (Remark 1).
- SGD↔GD switches; noisy GD with Gaussian noise; batch sizes 50–5000.
- 2-D toy: L = ½(1000x² + y²), split as ℓ₁,₂ = L ± 100xy.
- EoS (GD, η = 0.1 on MLP), SAM (η = 0.01, ρ = 0.1), SGDM and Adam.
- Preliminary test accuracy on full MNIST (App., last section).

## Key results

1. **Dom-SGD stalls** (§3.2): "we observe that Dom-SGD fails to further
   decrease the training loss, unlike standard SGD. Actually, we observe
   that Dom-SGD even slowly increases the loss in long run."
2. **Bulk-SGD matches SGD** (§3.3): "Bulk-SGD is as effective as SGD in
   decreasing the training loss … it is indeed a small fraction of gradient
   that aligns with the bulk subspace that contributes to training loss
   decrease." Phenomenon 2: "the training loss does not decrease within the
   dominant subspace".
3. **Noise causes the alignment** (§4.1, Phenomenon 3): switching SGD to GD,
   "the alignment disappears as soon as we switch to GD"; under GD "χ_k(∇L)
   quickly reaches and remains near 0", yet "GD and SGD trajectories
   closely track each other" (App. track_GF). Smaller batches and larger
   injected noise raise χ_k (App. ngd).
4. **Mechanism, a valley** (§4.3): the landscape is "steep along the dominant
   subspace and flat along the bulk subspace", and "there is a direction
   within the bulk subspace along which the bottom of the valley descends."
   Dom-SGD "fails to follow the true progress direction along the bulk
   subspace." Dom-SGD weights barely move from the switch point (App.
   distance). Toy: at θ = (0.01, 0.5), χ₁ ≈ 0.999.
5. **EoS and SAM** (§5): Dom-GD and Dom-SAM also fail; Bulk-GD and Bulk-SAM
   match; at EoS the alignment "arises from a self-stabilization mechanism".
   In the GF regime with full-batch GD, Dom-GD also fails (App. GD_alignment).
6. **Momentum and Adam amplify the bulk** (§6, Table 1, SST2-1k, first 1000
   steps): mean Bulk-LR 0.0100 (GD), 0.0828 (GD+m), 0.4672 (Adam−m),
   2.6639 (Adam+m); "Bulk-LR positively correlates with the training speed."
7. **Sharpness** (App. sharpness): "Dom-SGD decreases the sharpness, unlike
   SGD and Bulk-SGD. Moreover, Bulk-SGD increases sharpness more rapidly
   than SGD." The authors hypothesise "the dominant component in SGD is
   primarily an effect of stochastic noise, while the bulk component behaves
   more similarly to continuous-time gradient flow."
8. **Test accuracy** (App., preliminary, full MNIST): "Bulk-SGD generalizes
   as well as SGD, while Dom-SGD fails to generalize well."
9. Not in conflict with low-dimensional training (Li et al. 2023's PCA
   subspace of the trajectory): "the low-dimensional subspaces they chose
   are not the dominant subspace" (App. related work); in the toy, PCA of
   the iterates aligns "much closer to the y-axis", the bulk.

## Assumptions and scope

- "Learning" means training-loss decrease (optimization); generalization
  is a preliminary appendix check. No representation, feature or
  decodability is measured.
- Small subsampled datasets, small models, MSE loss mainly, constant
  learning rates. The dominant subspace is fixed at k = #classes.
- The explanation (valley) is "one plausible explanation", supported by the
  toy and distance measurements, not proved. "providing a theory on our
  empirical findings beyond the toy model" is left open (§7).

## Concepts

dominant subspace, bulk subspace, spurious alignment, Dom-/Bulk-SGD (and
-GD, -SAM, -OPT), GF regime vs EoS regime, maximum stable sharpness,
self-stabilization, ill-conditioned valley, effective learning rate
(Dom-LR, Bulk-LR), progressive sharpening.

## Verdict on the exchange's characterization

The exchange (A41, as recorded in CLAIM-tmppkdjz, ARG-tmpjx3ww,
QUESTION-tmp82zpm and the LIT summary): "SGD progresses in the Hessian's
bulk, not its top subspace"; "projecting gradient steps onto the top
Hessian eigenspace does not reduce loss, while the bulk carries the useful
progress". **Accurate**, with three qualifications:
- The spectrum is the training-loss Hessian in parameter space; "top" is
  top-k with k = number of classes; "bulk" is its whole complement, not a
  set of smallest-eigenvalue directions.
- "Learning" is training-loss descent. The paper says nothing about
  directions becoming informative or decodable.
- The paper's own reading is that the top-subspace component is noise
  (oscillation across a valley), not that the small directions are
  surprisingly "important". The result is close to what a steep valley
  predicts once its stiff directions are equilibrated; it is surprising
  only against the first-order expectation that gradient alignment means
  progress (§3.1).
The LIT summary's "Gradients align with the dominant Hessian subspace, yet
projecting updates onto it stalls learning; progress happens in the bulk
subspace" is correct; add that the alignment is SGD-noise (GF) or
EoS-oscillation driven and absent under small-step GD.

## Bearing on the named codes

- **CLAIM-tmppkdjz** (metrics can rank directions in opposite orders):
  **qualifies, weak support**. It is an instance of "large under curvature,
  little contribution to loss descent", i.e. Hessian curvature against
  descent per step. But it is a dynamical result within one metric (the
  stiff directions are already at their valley floor), not two static
  metrics reversing order. Passage: §4.3, "steep along the dominant
  subspace and flat along the bulk subspace … there is a direction within
  the bulk subspace along which the bottom of the valley descends."
- **ARG-tmpjx3ww**: **supports its verdict, qualifies one premise.** The
  verdict that the findings do not correct the hyperribbon account stands:
  the paper's picture (stiff directions fitted first, progress then along
  the flat floor) is the sloppy-model picture, not a refutation of it. The
  premise "None of the four findings measures that spectrum for
  parameters" is qualified for this work: the paper's main loss is MSE,
  whose Hessian is the Gauss–Newton JᵀJ on the training set plus a residual
  term, i.e. close to the hyperribbon's parameter-space metric (my
  reasoning; the paper does not decompose its Hessian). So this finding does
  touch the predictive spectrum, and is consistent with it.
- **QUESTION-tmp82zpm**: **leaves open; parallel at most.** Nothing tracks a
  direction becoming informative, a degeneracy changing or a distinction
  becoming decodable. The subspace is recomputed each step; no direction is
  followed. Parallel: the sharpness observations (Bulk-SGD sharpens faster,
  Dom-SGD flattens; App. sharpness) are a local-geometry change driven by
  which component is kept, a possible handle on "event 2" but not studied
  as such.

## Limitations

Small subsets (5k/1k), small models, MSE mainly; constant learning rates;
k fixed at #classes (no sweep over k reported in the main text); top-k
eigenvectors recomputed each step (costly, so only small models); the
mechanism is plausible, not proved; generalization only preliminary.

## Candidate THEORY

"In small-learning-rate SGD on MLP, CNN and Transformer classifiers trained
on 5k-MNIST, 5k-CIFAR10 and 1k-SST2, the stochastic gradient lies mostly in
the span of the training-loss Hessian's top-k eigenvectors (k the number of
classes), yet projecting each update onto that span stops the training loss
falling while projecting it onto the orthogonal complement trains as fast
as SGD; the alignment comes from gradient noise across a steep valley, and
vanishes under full-batch gradient descent, so the loss falls along the
valley's low-curvature floor."

promote_when: an independent study, on at least one architecture or
dataset not in the paper, finds that top-k-projected SGD stalls while
complement-projected SGD matches SGD, and that the top-k alignment
disappears under full-batch gradient descent at the same learning rate.

## Recheck (search of record/ after reading)

Searched for Gur-Ari, tiny subspace, dominant/bulk subspace, Edge of
Stability, self-stabilization, sharpness, SAM, Papyan, Sagun, outlier,
valley, Hessian. Held entries the first search missed:
- **LIT-619 / NOTE-479** (Papyan 2020, three-level hierarchy of Hessian
  outliers): background, supports the definition. Its Connections already
  cites Gur-Ari: the top-C span "from class means". Explains why the
  dominant subspace has k = #classes.
- **THEORY-731** (Active; Gauss–Newton splits into four terms, class-centre
  term rank ≤ C) and **THEORY-078** (Proposed; top C Fisher eigenvalues
  carried by class-mean logit derivatives): background; they say what the
  dominant subspace is, which Song et al. do not.
- **LIT-617** (Papyan 2018, full spectrum of deepnet Hessians): background,
  outliers vs bulk.
- **THEORY-209 / LIT-1011** (limiting dynamics of SGD: anomalous diffusion,
  noise isotropic in the Hessian's column space): parallel; SGD noise
  shaping motion across curvature directions.
- **THEORY-781, THEORY-213, QUESTION-206** (gradient noise and symmetric
  subspaces): parallel, noise steering SGD geometry.
- **THEORY-082** (steepest descent defined only relative to a metric):
  bears on CLAIM-tmppkdjz; Adam/momentum raising Bulk-LR is a change of
  metric for descent.
- **TERM-tmpnxjq4** sense 3, "low curvature, vᵀHv": this paper is the
  instance of that sense; its "bulk" is the complement of the top-k, not
  the low tail.
- No held entry on Edge of Stability (Cohen et al.) or self-stabilization
  (Damian et al.) as works; NOTE-318, NOTE-663, NOTE-714 mention EoS in
  passing. LIT-861 is unrelated.

## Neighbours

None needed; the work itself was read.
