# Reader notes: LIT-tmp3njir (Hoogland et al., arXiv 2402.02364)

## Located copies (2026-11-21)

- https://arxiv.org/pdf/2402.02364 : arXiv preprint (author's manuscript,
  v3 of 1 Aug 2025, 49 pp., header "To appear in Transactions on Machine
  Learning Research (07/2025)"). Fetched 2026-11-21, HTTP 200,
  application/pdf. Lawful (arXiv). Read.
- arXiv API record (export.arxiv.org, id_list=2402.02364), fetched
  2026-11-21, no email sent: v3 updated 2025-08-01, published 2024-02-04;
  comment "To appear, TMLR. Material on essential dynamics from v1 of this
  preprint has been removed and developed in arXiv:2501.17745".

No other copy sought: the arXiv copy is the authors' own and was read.
The TMLR version was not fetched or compared; v3's header says "To appear".

## Provenance

arXiv PDF v3 (1 Aug 2025), 49 pp., text by pdftotext -layout; page 2
(Fig. 1) rendered and looked at to read the LLC curves. Read in full: main
text §§1–8 (pp. 1–11), App. A (LLC definition, SGLD, hyperparameters,
calibration guide, non-likelihood loss, estimates away from minima), App. B
(stage identification, seeds, Hessian comparison), App. D.2.3–D.2.6, App. E
(one-layer model), App. F (training details). Skimmed: App. C and
D.1–D.2.2 (metric definitions and figures behind §§6–7), reference list for
the entries cited here. Figures other than Fig. 1 read from captions only.
Codebase named in the paper (github.com/timaeus-research/icl) not opened.
No email address sent anywhere.

## Summary

Two small transformers are trained once each (plus four extra seeds): a
two-layer attention-only language model on a DSIR-filtered Pile subset
(3,355,016 parameters, 8 heads/layer, AdamW, weight decay 0.05, 50k steps)
and a two-layer in-context linear regression transformer with MLPs
(51,717 parameters, D = 4, K = 8, Adam, no regularization, 500k steps).
At checkpoints the local learning coefficient (LLC) is estimated with
Lau et al.'s SGLD estimator. The estimated LLC curve is lightly smoothed
with a Gaussian process, differentiated in log t, and its plateaus (zeros
or near-zero local minima of the slope) are taken as stage boundaries.
Each run gets five stages. Setting-specific metrics then show that most
stages coincide with interpretable changes: LM1 bigrams, LM2 n-grams and
use of positional embedding, LM3 previous-token heads, LM4 induction heads
and in-context learning, LM5 nothing found; LR1 context-free prediction,
LR2 in-context learning, LR3–LR4 loss of OOD robustness with embedding,
attention and layer-norm "collapse", LR5 nothing found. The LLC rises in
most stages and falls in LM3, LR3 and LR4.

## Contribution

1. A stage-division method: stage boundaries at plateaus of the estimated
   LLC over log training time, automatic once smoothing, tolerance and
   checkpoint spacing are fixed.
2. Two case studies in which those stages line up with independently
   measured behavioural and structural changes, and the stage boundaries
   recur across five seeds.
3. Stages of LLC decrease (simplification) documented, with candidate
   mechanisms (layer-norm, unembedding, embedding, attention collapse)
   argued to create degeneracy.
4. A practical guide to calibrating SGLD LLC estimation (App. A.5),
   including a departure from Lau et al.'s β*.

## Key results (section, short quote)

- R1 Stages from LLC plateaus. §5: "We use critical points (that is,
  plateaus, where the first derivative vanishes) in the LLC curve to define
  stage boundaries that divide training into developmental stages."
  Stages are periods of change, boundaries are pauses; §2: "We emphasize
  changes in degeneracy over a stage whereas in bifurcation theory the
  focus is more on the degeneracy at stage boundaries".
- R2 Stages match development. Abstract: "these changes in degeneracy
  coincide with significant changes in the internal computational
  structure and the input/output behavior of the transformers." §6: "Note
  that we did not discover significant changes in LM5"; same for LR5 (§7).
- R3 LLC changes per stage (Fig. 1 table): LM Δλ̂ = +26.4, +22.5, −1.57,
  +8.62, +1.77; LR Δλ̂ = +21.4, +149, −12.3, −44.1, +3.56. From the
  figure: LM λ̂ runs from about 80 to about 145; LR from near 0 to about
  165, then down to about 120.
- R4 Seeds. B.4: "In each seed, LLC estimation reveals stage LM1–LM4. In
  three of the five seeds, stage LM5 is subdivided into two additional
  stages." For LR: "In each seed, LLC estimation reveals stages LR1–LR5."
- R5 Hessian misses them. B.5 (LR only): "The Hessian fails to detect
  three of the four stage boundaries identified by our LLC-based
  methodology." Trace and max eigenvalue via PyHessian.
- R6 Groundwork before the event. §6.2: heads that later form the
  induction circuit begin to compose in LM2; "the foundations for the
  induction circuit are laid in advance of any measurable change in model
  outputs or attention patterns."
- R7 Decreases. §6.3: "The LLC decreases during LM3, suggesting an
  increase in degeneracy (a decrease in model complexity). This may be
  related to interaction between heads." §7.3 on LR3–4 layer-norm
  collapse: "we conjecture that this explains part of the striking
  decrease in estimated LLC over these stages". One-layer LM (App. E): the
  LLC drops between steps 400 and 900, "We did not closely investigate
  why".

## Assumptions and what the authors do and do not claim about singularities

- The Bayesian singular learning process is motivation by analogy, not a
  model of training. §2: "While there are many differences between
  Bayesian inference and modern neural network training, an analogy to the
  singular learning process informs our methodology for stage division."
  §5: "While the general connection between the singular learning process
  in Bayesian inference and stagewise development in deep learning remains
  to be understood". Fig. 3 shows posterior switching between
  neighbourhoods as n grows; the paper's stages are in training time t.
- §5 on the free-energy crossover: "We note that this is not the only
  possible dynamic—lower-order terms may also play a role in the evolving
  competition." Its expectation for larger models: changes "may be more
  gradual, while still being delineated by brief moments in which the
  posterior is stably concentrated around a given local minimum."
- The LLC decreases are not explained by the singular learning process.
  §8: "the example transitions in the singular learning process outlined
  in Section 5 and Figure 3 describe LLC increases. Though we note that
  decreasing the LLC while holding the loss constant would be another way
  to decrease the free energy according to equation (4), providing a full
  theoretical account of these stages is an open problem." D.2.6: "in
  idealized Bayesian inference, we do not expect the posterior to
  concentrated around the neighborhood of an equal-loss-but-higher-
  degeneracy local minimum to begin with" (sic).
- No causal claim. §8: future work should be "seeking to establish a
  causal connection between changes in degeneracy and changes in
  structure and behavior." D.2.6: "Actually establishing a causal link
  between increasing degeneracy and structure development is beyond the
  scope of this paper."
- Estimates away from minima. A.7: checkpoints "will not be local minima
  of the population loss, violating the theoretical conditions under which
  the LLC is defined"; they speculate the estimator gives "the LLC of a
  different potential to the population loss—a potential for which the
  current parameter actually is at a critical point."
- The loss is not a negative log likelihood (overlapping prefixes); App.
  A.6 reports orderings unchanged for LR with a likelihood-based variant.
- Not universal. §8: "We do not claim that the structural and behavioral
  developments we observed in each setting are universal phenomena." Only
  "macroscopic" changes are expected to show as LLC plateaus.
- Nowhere do the authors say a stage is a passage between singular
  regions, a change of dominant singularity, or a resolution of a
  singularity. The word "singularity" is not used for stages; "degeneracy"
  and "local minimum" are.

## Estimator settings (bear on CLAIM-tmpcg4uu, NOTE-tmp92pjh)

- β departs from Lau et al. A.5.1: "In practice, we find that it can be
  advantageous to sample at a higher temperature." "Instead of
  nβ = n/ log n, we perform LLC estimation at nβ = m/ log m, where m is
  the SGLD batch size." LM: m = 100, nβ = 21.7, γ = 100, ε = 0.001,
  20 chains × 200 steps (Table 1); training n = 5,000,000. LR: nβ = 66.7,
  γ = 13.3, ε = 0.0003, 10 chains × 5,000 steps with 1,000 burn-in
  (Table 2). The LR nβ is not m/log m (1024/ln 1024 ≈ 148); it equals
  β̃ = εnβ/2 = 0.01 from the sweep (reader's arithmetic).
- Fixed across checkpoints, and SGLD noise and batches seeded identically
  at every checkpoint (A.5.2), which smooths the curve.
- Tuned at final checkpoints and checked "for a subset of earlier
  checkpoints" (A.5.3); "γ should be as small as possible ... and β should
  be as large as possible (but no greater than 1/ log n)."
- Not reported: stage boundaries recomputed under different β or γ.
- B.1: boundaries "sensitive to the following choices: the intervals
  between checkpoints, the amount of smoothing, whether to differentiate
  with respect to t or log t, and the choice of tolerance."

## Concepts

LLC (volume-scaling exponent, A.1, with multiplicity m); SGLD LLC
estimator with localization γ and inverse temperature β (eq. 3); local
free energy and Watanabe's expansion (eq. 4); singular learning process
(Watanabe 2009 §7.6); LLC plateau as stage boundary; developmental stage;
degeneracy vs. curvature (A.2: "the LLC λ does not measure curvature");
layer-norm / unembedding / embedding / attention collapse as sources of
degeneracy (D.2); developmental interpretability (§8).

## Verdict on the exchange's characterization

The exchange (A37 region, line 10628 of exchange.txt): "They observed
changes in local learning coefficients associated with developmental
stages in transformer training." Accurate. Its follow-on nuance, that
"movement toward a more degenerate configuration can lower the coefficient
even while the model develops useful organization", matches LM3 and
LR3–LR4. The LIT's summary ("stages marked by changes in loss-landscape
degeneracy, measured by the local learning coefficient") is accurate. What
goes beyond the paper is the record's framing of it as "stagewise
development as passage between singularities" (LIT standing, CLAIM-
tmpgzb8v's context): the authors use the singular learning process only as
motivation, keep its link to training open, and do not identify stages
with changes of dominant singular region. Two precisions: (1) boundaries
are LLC plateaus, and the stages are the intervals of change between
them, not jumps; (2) the models are two specific small transformers.

## Bearing on the named codes

- CLAIM-tmpgzb8v (reading b): supports its weak half, "or at least leave
  their mark in local learning coefficients", for two small transformers
  (R1–R4); leaves open its strong half, that stages are switches of the
  dominant singular region: the paper does not test it and says the
  connection "remains to be understood" (§5); qualifies it in that three
  stages are LLC decreases, which the crossover to a richer, higher-λ
  region does not produce and the authors call unaccounted for (§8, D.2.6).
  Its sentence "Hoogland and colleagues ... report stagewise changes in the
  coefficient in transformers" is correct as written.
- CLAIM-tmpp83vc (U23): background and qualifies, as for (b). Nothing in
  the paper bears on reading (a): no blow-up or resolution is said to be
  carried out by training. The LLC decreases (R7) are a datum both readings
  must place.
- CLAIM-tmpcg4uu: leaves open, and sharpens the alternative it names. The
  paper does not vary β or γ across stages, so the separating test is not
  done. Reader's derivation, using the claim's own quadratic formula
  Σ ½·te_i/(te_i + γ) with t = nβ: a direction counts fully in the LM
  estimate only when e_i ≫ γ/(nβ) ≈ 100/21.7 ≈ 4.6, in the LR estimate
  ≈ 13.3/66.7 ≈ 0.2. The estimates (about 80–150 LM, up to about 165 LR)
  are far below d/2 (≈ 1.68M and ≈ 25.9k), consistent with most directions
  unresolved at those settings. So a rise in λ̂ could be directions
  stiffening past the cut-off as much as a change of stratum. Against a
  pure-curvature reading, weakly: B.5 finds Hessian trace and max
  eigenvalue not tracking λ̂, but those are dominated by the largest
  eigenvalues, not by those near the cut-off. The paper's β is not Lau's
  β* = 1/log n; any entry saying this paper's estimates are at β* is wrong.
- THEORY-975 (Wang et al., held): parallel. Same LM run (NOTE-1188), whose
  per-head refinement this paper cites as extension (§8, "Wang et al.,
  2025"). NOTE-1188's C6, that LLC decreases are a kind of stage, is
  confirmed in this paper's own words (§6.3, §8).
- THEORY-967 (heads change function): parallel, weak support. R6: the
  heads that become the induction circuit compose in LM2 before their
  attention patterns change; this neither tests nor contradicts
  repurposing.
- NOTE-tmp92pjh (Lau et al.): this paper departs from Lau's β* on
  practical grounds, applies the estimator away from minima (A.7), and
  reports estimates "stable" only "given sufficiently strong localization
  γ" (§4). Lau's cautions (unsettled sampler underestimates; consistency
  conjectured) apply here unaddressed except by traces and sweeps.

## Limitations

One run per setting analysed in depth; five seeds for stage boundaries
only. Two small models; one LM without MLPs. Stage boundaries depend on
smoothing, tolerance, checkpoint spacing and log t (B.1). Estimator
settings fixed across training and tuned largely at the end; no
sensitivity of the stage division to β or γ is reported. Estimates are
taken away from minima, on a non-likelihood loss, at an effective sample
size (nβ ≈ 22 or 67) far below n. LM5 and LR5 have no interpretation;
late-LM noise is high (B.2). Hessian comparison only for LR. Correlation,
not causation, as the authors say. The v1 material on "essential
dynamics" was removed (arXiv comment) and not read.

## Candidate THEORY

Title: In a two-layer attention-only language transformer (about 3.4M
parameters) and a two-layer in-context linear regression transformer
(about 52k parameters), plateaus in SGLD estimates of the local learning
coefficient over log training time divide training into five stages,
four (LM) or five (LR) of which recur in each of five seeds, and most
stages coincide with independently measured changes in behaviour or
structure (bigrams, n-grams, previous-token heads, induction heads;
context-free prediction, in-context learning, loss of out-of-distribution
robustness with layer-norm collapse); the estimate rises in most stages
and falls in three.

promote_when: An independent run of either setting (the authors' code or
a reimplementation) that recovers the LLC-plateau boundaries of LM1–LM4
or LR1–LR4, and the same behavioural or structural markers inside each
stage, with the estimator's nβ and γ each varied over at least a factor of
three; refuted if the boundaries move with nβ or γ, or the markers do not
line up with them.

## Recheck (grep after reading)

First search found only THEORY-975/967 (LIT-1535) and NOTE-1188. Missed:
- THEORY-1275 / NOTE-1462 / LIT-1894 (Chen et al. 2023, TMS, Bayesian vs
  dynamical transitions): the paper's only empirical precedent, cited as
  showing SGD and Bayesian transitions "reflected as sudden changes in the
  estimated LLC" (§5). Background; already a ground of CLAIM-tmpgzb8v.
- QUESTION-363 (SGD order vs Bayesian order): leaves open; §5 says the
  connection "remains to be understood".
- QUESTION-039 (order and moment of acquisition; one kind of event or
  several): bears; stages include simplifications (LLC decreases) and
  groundwork stages (R6), so "acquisition" here is several kinds.
- QUESTION-275 (circuit development as regimes): background; LM2's
  composition before the circuit's visible formation.
- QUESTION-tmpsy8qn (incidence order of strata vs refinement order):
  leaves open; the paper measures no strata, and the non-monotone λ̂
  (LM3) shows the estimate does not climb a chain monotonically.
- QUESTION-217 (coarse-to-fine orders): supports a single-run
  coarse-to-fine progression in the LM (bigrams → n-grams → induction),
  which §8 likens to Olsson et al.'s across-depth progression
  (NOTE-1173, LIT-1538).
- LEAD-tmpfrw11 (date onsets, vary β and γ): the paper does what the lead
  dates (behavioural markers vs LLC) but without the β/γ variation the
  lead asks for.
Nothing found for "essential dynamics" (arXiv 2501.17745), "layer-norm
collapse" or "singular learning process".
