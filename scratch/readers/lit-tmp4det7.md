# Reader notes: LIT-tmp4det7 (Xu, arXiv 2605.17084)

## Provenance
- Read: https://arxiv.org/pdf/2605.17084, PDF, version v2 (arXiv stamp "3 Nov 2026"; "Preprint. November 4, 2026"), 23 pp. Fetched 2026-11-21 over the arXiv site, converted with pdftotext. Author: Weilun Xu (EPFL), sole author.
- Read in full: main text pp. 1-10, Appendices A-G pp. 13-23. Skimmed: references (pp. 10-12). Figures read from captions and text only (plot values not extractable from the PDF text); every number below comes from the prose.
- v1 (2026-05-16) not read; differences between versions not checked.

## Copies located (2026-11-21)
- https://arxiv.org/abs/2605.17084, arXiv abstract page. HTTP 200.
- https://arxiv.org/pdf/2605.17084, arXiv PDF (v2). HTTP 200. Read.
- https://arxiv.org/html/2605.17084, arXiv HTML. HTTP 200. Fetched, not read (PDF used).
No obstacle anywhere. Status: read.

## Summary
At a language model's final hidden state, Xu folds the final-norm weight into the unembedding, centres over the vocabulary, removes the LayerNorm mean direction, and takes the SVD of the resulting W = C_V W_out diag(γ) R (Eq. 1). The right singular directions are split into 20 equal bands. A document's component in a band is replaced by the calibration mean (a mean-ablation of the state, not a zeroing of weights; norm scale held fixed), and compared with the same replacement in 8 random subspaces of equal rank, rescaled per document to equal length ‖δu‖². Each change is measured by logit distance D = ‖δℓ‖² (every token pair weighted equally) and by prediction change K = KL(p‖p′), with Fisher term F = ½Var_p(δℓ) (pairs weighted by p_t p_t′). The bottom band (5% smallest singular values) moves logits less than equal-length random changes but changes K and the loss several times more; the per-unit ratio F/D (the "consequence spectrum") is near random across most bands and rises steeply only over the last few. The mechanism offered: the two leading candidate tokens' contrast w1 − w2 lies disproportionately in the bottom band. Truncating the unembedding by singular value raises loss more than random truncation; ranking by expected Fisher term avoids this.

## Contribution
An operational, equal-length test, with prespecified comparisons and bootstrap intervals, that the logit (Aitchison/WᵀW) metric and the predictive Fisher metric pulled back to the final state disagree most along the unembedding's smallest singular directions, in 10 trained models, with a mechanism traced to the leading-pair contrast.

## Models, ablation, metric, effect sizes (as the brief asks)
- **Models.** Ten base models: Pythia 70M, 160M, 410M, 1B, 1.4B, 2.8B, 6.9B (final checkpoints), Llama-3.1-8B, Qwen3-1.7B-Base, Qwen3-8B-Base; plus Llama-3.1-8B-Instruct and post-trained Qwen3-8B (§3, App. C). 1,536 OpenWebText documents of 128 tokens (512 calibration), state at the 128th token; also 8th/32nd token and DeepMind Code Contests code (56 model–condition–position combinations, §3.3, Table 2). Float32.
- **Ablation.** "We change the final hidden state within one band b by replacing its component in that band with the calibration mean µ" (§2.3, Eq. 6: δu = −P_b(u − µ)). Not a weight ablation. Norm scale fixed ("We hold the scale at its value on the unchanged input", §2.1); natural path (scale recomputed) as a check. Truncation experiment (§5.1) is equivalent to truncating the unembedding with a corrected bias, no retraining.
- **Metric in which directions are small.** Singular values of the centred, γ-folded unembedding acting on the normalized state u, i.e. eigenvalues of G = WᵀW, "the Aitchison metric" pulled back (App. B): "σ_i² ... also measures how widely the tokens' unembedding vectors spread along v_i, with every token counted equally" (§2.1). The comparison metric is F̄ = E_x[Wᵀ Σ_p W], Σ_p = diag p − ppᵀ; "the quotient of the two metrics ρ(v) = vᵀF̄v / vᵀGv ... is the per-direction form of the consequence spectrum" (App. B). Not small in representation variance: the bottom band "holds on average 1.5 to 6.6 times its share of the directions in variance" of the late states (App. D).
- **Effect sizes.**
  - Equal length, main comparison: K and loss "several times as large" as random (§3.1; Fig. 2a gives the values graphically). Prose numbers: Qwen3-8B and Qwen3-1.7B K ratios 3.5 and 4.1 (7.7 and 8.5 with near-zero directions removed, loss excess 0.69 and 0.64 nats; App. E.1); unrescaled references K 3.3 to 21 times random (App. E.1); uncentred basis D 0.10–0.29, K 3.9–11.2 times random; bottom-band F/D 12 to 38 times random vs. 0.4 to 2.5 for a top-variance subspace (App. E.1).
  - Per document: bottom band exceeds references per unit logit distance in 83–93% of documents; total K larger in only 47–68% (§3.1). Median per-document loss excess −0.13 to 0.02 nats; top decile carries 63–115% of the summed excess (App. E.2).
  - Top token replaced in 25–48% of documents vs 10–29% for references; top-1 accuracy falls 0.03–0.20 vs ≤0.04 (App. E.2).
  - Total effect: removing the top band "increases the loss as much as removing the bottom band's, or more, in nine of the ten models, by 0.96 to 1.75 nats against 0.17 to 1.23 nats" (App. E.2). Top band C_b 0.4 to 2.4.
  - Mean square of bottom-band singular values is 0.31–0.41 of the average; values "decline smoothly into the bottom band" (within 0.3% across the edge) (App. D, Fig. 5).
  - Truncation at 20% rank: by singular value +0.11 to 1.24 nats over random; consequence-ranked 0.07 to 0.28 nats below random (App. E.4).
  - Temperature: K ratio falls from 3.6–10.4 at T = 0.5 to 0.09–0.30 at T = 8 (App. E.3).

## Key results, with quotes
1. §3.1: "The bottom band's changes move the logits less than their references, as their small singular values imply. Nevertheless, in every model, their prediction change and their loss change are several times as large (Figure 2a)."
2. §3.2: "Across most of the spectrum, the prediction change per unit of logit distance stays within about a factor of two of that of random changes. The large excess appears only over the last few bands, and the bottom band has the largest C_b in every model."
3. §2.3, Eq. 8: for a single singular direction "the singular value drops out of the ratio F/D", F/D = ½Var_p(a_i): "A direction can therefore have a small singular value and still a large prediction change per unit of logit distance."
4. §4.1: the leading pair's contrast share and the consequence spectrum's logarithms "correlate at 0.95 to 0.98 across the ten models"; leading pair exceeds a frequency-matched pair by 1.29–1.59 (App. E.3), but "Most of it is common to probable tokens".
5. §4.2: the pair-vs-rest and within-pair parts of K "together account for 85 to 99% of the band's excess prediction change".
6. §5.1: "truncating the unembedding by singular value changes the logits less than random truncation but increases the loss more" (§1); whitened (SVD-LLM) truncation does even better, so "The cost therefore lies in ranking by the singular values alone, not in truncation as such."
7. App. E.1: robust to reference scaling, donor replacement, natural path, raw and uncentred bases, removing 16 extreme coordinates; one exception (Pythia-70M in the raw basis, K ratio 0.71).
8. §7, training origin, untested: "Testing this origin would require tracking the organization during training and comparing controlled training objectives."

## Assumptions
- The Euclidean inner product on the normalized state u (in the γ-folded, Helmert/identity basis) defines both the SVD and "equal length". The paper checks the raw and uncentred bases but not arbitrary invertible reparametrizations.
- Scale of the final norm held fixed (checked on the natural path, K ratio 1.00–1.21 times the fixed-scale value).
- Equal-length random changes as the null; "changes of equal length need not produce states that occur naturally" (Limitations).
- One site (final hidden state), ≤8B params, ≤128 tokens, no chat template.

## Concepts
Consequence spectrum C_b; logit distance D (squared Aitchison distance; up to V the squared length under Park et al.'s causal inner product, App. B); Fisher term F; ρ(v) as quotient of two metrics and its generalized eigenvectors (likelihood-informed subspaces, Cui et al. 2014, Spantini et al. 2017); contrast share; band enrichment × state alignment (Eq. 11); consequence-ranked truncation (OBD saliency applied to directions).

## Verdict on the exchange's characterization
- CLAIM-tmppkdjz: "A credits the distinction [G_pred vs G_logit] to Xu" — accurate. App. B defines G = WᵀW and F̄ = E[WᵀΣ_pW] and their quotient. But the claim's phrase "That trained unembeddings show the reversal systematically is Xu's empirical claim" overstates it. Xu does not show the Fisher ranks the smallest singular direction above the largest. Xu shows the *ratio* F/D peaks at the bottom. Per unit state length, the Fisher term is "lowest over the middle bands and rises above random at both ends" (App. D, Fig. 5d), and the top band's total loss effect equals or exceeds the bottom band's in 9/10 models. So it's a U-shaped, partial non-monotonicity, not a reversal.
- ARG-tmpjx3ww: "perturbing the unembedding's least-amplified directions moves next-token distributions more than matched random perturbations": correct if "perturbing" means the final hidden state along those directions (it is not a perturbation of the unembedding weights). "G_pred is a predictive Fisher, but pulled back to a hidden state rather than to parameters": confirmed (App. B).
- LIT-tmp4det7 summary, "carry a disproportionate share of next-token prediction": too loose. They matter disproportionately *per unit of logit distance and at equal state length relative to random directions*. In total the top band matters as much or more (App. E.2).
- QUESTION-tmp82zpm and A41's "spectrally quiet subspace": Xu's directions are quiet in the logit metric only. In representation variance they are loud (1.5–6.6× their share). Reading Xu as evidence about low-*variance* directions would be wrong.

## Bearing on the named codes
- **CLAIM-tmppkdjz: supports, and qualifies.** Supports the thesis that metrics disagree, empirically, in trained models: "the two geometries disagree most along the directions that the unembedding amplifies least" (§7). It answers the claim's own question (its random-Gaussian check found Spearman 0.85) with trained-model evidence that the WᵀW and pulled-back-Fisher orders come apart at the bottom. Qualifies: the disagreement is in the quotient ρ, and is partial (U-shaped F per unit E, top band still important in total), not a full reversal of the largest and smallest. Not evidence for the variance-vs-label half: Xu's bottom band has *excess* state variance, and a top-variance subspace has small F/D (0.4–2.5).
- **ARG-tmpjx3ww: supports its premise.** The paper's metric is the state-space pullback (App. B), not a parameter Fisher, so it does not bear on the hyperribbon's parameter-space hierarchy. Its framing ("Distance and variance give a representation one geometry ... the geometry of the prediction ... changes with the context", §7) is the "other spectra are poor proxies for the predictive one" reading the argument gives. Adds that the predictive metric is context-dependent (Σ_p(x)), so its ranking is averaged over documents.
- **QUESTION-tmp82zpm: leaves open (background).** Final checkpoints only; no tracking through training. §7 offers a possible training origin (from Thrampoulidis 2024 and Zhao et al. 2024): the part of the output weights that sets odds among plausible tokens stays finite while exclusion grows. If that maps onto singular directions, it "places the distinctions among plausible candidates at the bottom of the spectrum". Only the bottom half is consistent with the data, and the top half is "not established" (App. E.3). It is a testable developmental hypothesis for the question, using Pythia's checkpoints, which the paper did not use.
- **THEORY-420 (Staats et al.): parallel/contrast.** Xu cites Staats (§6, App. G) as showing the same divergence "inside the network". Differences: Xu ablates a *state* component at the output, not weight singular values inside blocks; Xu's unembedding is rectangular (V × q), but its bottom singular values "decline smoothly", with no gap at the band edge, and the paper makes no random-matrix (below-bulk) analysis. So Xu's effect doesn't rest on the outlier mechanism THEORY-420 leaves untested. Both measure damage under no-refit removal against a magnitude ranking.

## Limitations
- Author-stated (p. 10): one site, ≤8B, ≤128 tokens, no chat formatting; equal-length changes may be off-distribution; truncation without retraining; implications for interpretation/editing not tested.
- Reader's: effect sizes for the main comparison are given mostly in figures; prose gives ranges from robustness runs. The per-document effect is heavy-tailed (median loss excess ≈ 0). "Smallest" is relative to a Euclidean metric on u fixed by the architecture's normalization. Under an invertible reparametrization of u, the singular directions and "equal length" change, though the generalized eigenproblem of (F̄, G) does not (the paper names it, App. B, but ranks by singular value). Single author; AI assistance acknowledged for code and revision.

## Candidate THEORY
Sentence: "In ten trained language models (Pythia 70M–6.9B, Llama-3.1-8B, Qwen3 1.7B and 8B), replacing the final hidden state's component along the 5% of directions the centred, norm-folded unembedding amplifies least moves the logits less than equal-length random changes but changes the next-token distribution and loss several times more. The prediction change per unit of logit distance stays near random over most of the spectrum and peaks at that bottom band, because the two leading candidate tokens differ disproportionately there. In total, the top band's removal costs as much loss or more."
promote_when: "An independent replication on at least one of these models finds the bottom band's equal-length K ratio above one and its consequence spectrum peaking at the bottom band, or the paper passes peer review with these results intact."

## Recheck (grep of record/ after reading, 2026-11-21)
Searched: 2605.17084, consequence spectrum, Aitchison, Cancedda, entropy neuron, attention sink, causal inner product, likelihood-informed, Spantini, Thrampoulidis, SVD-LLM, Fisher-weighted, optimal brain damage, Gauss-Newton, softmax bottleneck, tuned lens, LEACE, Stolfo, unembedding, logit lens, Jolliffe, Eckart, Hsu et al, Zhao et al. 2024.
- **THEORY-018** (missed by the first search): "Softmax training identifies a language model's final-layer representation only up to an invertible linear map, so no inner product on it is intrinsic, and Park, Choe and Veitch's causal inner product is fixed by a stipulation." Bears directly as a *qualification*: Xu's singular directions and equal-length comparisons depend on the Euclidean inner product on u. Xu's D is (up to V) the causal-inner-product length (App. B), the stipulated inner product THEORY-018 names. The quotient ρ(v) and its generalized eigenvectors are invariant under such maps; the singular-value ranking is not. This sharpens QUESTION-tmp82zpm's "harmless representation reparameterizations" caution.
- **LIT-304** (Park, Choe & Veitch, linear representation hypothesis; NOTE-302): background. Xu relates D to its causal inner product (App. B).
- **THEORY-738, THEORY-286** (unconstrained-features / simplex-encoded-label geometry under imbalance, Thrampoulidis line): parallel to Xu's §7 training-origin hypothesis, which cites Thrampoulidis (2024) and Zhao et al. (2024), neither held as LIT (no hit).
- **NOTE-803** mentions Stolfo et al. (2024) in passing; Stolfo (entropy neurons writing into the unembedding's null space) is not held as a LIT. Cancedda (2024), the closest prior observation per Xu, is not held.
- tuned lens (THEORY-2145, CLAIM-771) and LEACE hits: background only (Xu names them as distance- or KL-based methods, §5.2, §6); not read further.
- No other hit on the consequence spectrum, likelihood-informed subspaces or SVD-LLM.

## Neighbours
Not needed: the work itself was read. No other work read or quoted.
