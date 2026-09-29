---
number: 283
status: Read
formerly:
- NOTE-tmp9pv0t
paper: LIT-345
title: 'Progress measures for grokking via mechanistic interpretability'
version: 1
history:
- version: 1
  date: '2026-09-29'
  note: >-
    Read in full (Full text of arXiv 2301.05217 v3 (19 Oct 2023; carries
    "Published as a conference paper at ICLR 2023"), 35 pp.: abstract,
    §§1–6, the reproducibility statement, author contributions, references,
    and Appendices A–F including all tables. Text was extracted with
    PyMuPDF. The figures are images and were read from their captions and
    the text. I checked the trigonometric identities (the first one is
    mistyped; see corrections) and the Appendix B values of cos(2π·14·x/113)
    at x = 8 and 16.). The first NOTE on this paper, which was seeded from
    its abstract alone.
date: '2026-09-29'
summary: >-
  A one-layer ReLU transformer (P = 113, 30% of pairs, full-batch AdamW
  with λ = 1, 40k epochs) that groks modular addition implements a
  "Fourier multiplication" algorithm. The embedding maps a and b to
  cos/sin(w_k·a), cos/sin(w_k·b) at five key frequencies k ∈ {14, 35, 41,
  42, 52}, with w_k = 2πk/113. Attention and MLP form cos/sin(w_k(a+b)),
  and the neuron-logit map W_L (≈ rank 10) reads out Σ_k
  α_k·cos(w_k(a+b−c)). Progress measures built from this (restricted and
  excluded loss) show training splits into memorisation (0–1.4k epochs),
  circuit formation (1.4k–9.4k) and cleanup (9.4k–14k), with the
  test-accuracy jump inside cleanup.
---

# NOTE-283: Progress measures for grokking via mechanistic interpretability

## Contribution

The paper fully reverse-engineers the algorithm a small grokking transformer learns for addition mod 113, and uses that to define continuous progress measures underneath the apparently sudden generalisation.

- **The algorithm.** Addition is done as composition of rotations. Inputs are embedded as points on circles at a few frequencies and combined by angle-addition identities, and the output is read off by constructive interference of cosines.
- **The measures.** Restricted loss and excluded loss split training into three phases, and show that the generalising circuit forms well before test accuracy jumps.
- **The removal.** Memorising components are then removed under weight decay.

## Key insight

Grokking is not a sudden discovery. A structured circuit is gradually amplified alongside a memorising solution. Test performance jumps only when regularisation strips the memorisation away, because the generalising circuit reaches the same training loss with smaller weights.

Once the algorithm is known, "hidden progress" is directly measurable: project the logits onto, or away from, the algorithm's frequencies.

## Assumptions

- **The model.** One-layer ReLU transformer with d_model = 128, 4 heads of dimension 32, d_mlp = 512, learned positional embeddings, no LayerNorm and untied embed/unembed (§3; App. A).
- **The data.** Input "a b =" with one-hot a, b ∈ {0,…,112}, 30% of the 113² pairs for training, and test on all the rest.
- **Training.** Full-batch AdamW, learning rate 10⁻³, λ = 1, 40k epochs.
- **Simplifications made to read the circuit, checked by ablation.** Attention from "=" to itself is negligible (0.1–0.4%), and the MLP skip connection can be ignored, so Logits ≈ W_U·W_out·MLP, which defines W_L (App. A.1).
- **Robustness (App. C.2, D).** Checked on four more seeds, data fractions 10–90%, P ∈ {53, 109, 401}, 2-layer models, dropout, L1, and three other tasks.

## Key results

- **Periodicity (§4.1).**
  - W_E is sparse in the Fourier basis, with 6 non-negligible frequencies, of which 5 are used later: k ∈ {14, 35, 41, 42, 52}.
  - Attention scores and neuron activations are periodic in (a, b).
  - The logits' 2D Fourier spectrum has 20 significant components: 5 frequencies × 2 × 2.
- **Composing weights (§4.2, eq. 2, Table 1).**
  - W_L ≈ Σ_k cos(w_k)·u_kᵀ + sin(w_k)·v_kᵀ, with a residual under 0.55% of the Frobenius norm, so rank ≈ 10.
  - u_kᵀ·MLP and v_kᵀ·MLP are about 44–68 × cos/sin(w_k(a+b)), with FVE 93.2–98.2%.
  - The logits are fitted by Σ_k α_k·cos(w_k(a+b−c)) with 95% of variance explained. Using that approximation *lowers* test loss from 2.4·10⁻⁷ to 4.7·10⁻⁸.
- **Neurons (§4.3, Fig. 5).**
  - 433 of 512 neurons (84.6%) are over 85% explained by a degree-2 polynomial in one key frequency.
  - Their W_L columns carry only that frequency: 44 neurons for k = 14.
- **Ablations (§4.4).**
  - Replacing the 433 neurons by their polynomials raises loss by about 3% (2.41 → 2.48·10⁻⁷).
  - Keeping only the cos/sin(w_k(a+b)) terms improves loss by 77% (to 5.54·10⁻⁸).
  - Ablating any key frequency hurts. Ablating all 113² − 40 other logit Fourier components improves loss by 70% (to 7.24·10⁻⁸).
  - Projecting the MLP onto the 10 W_L directions lowers loss by 50%. Projecting onto their null space gives loss 5.27, worse than uniform.
- **Attention (App. C.1.2–3).**
  - The pattern is ≈ 0.5 + α(cos w_k·a − cos w_k·b) + β(sin w_k·a − sin w_k·b), with FVE 97.9–99.1% (Table 2).
  - The softmax over two tokens is a sigmoid in a nearly linear regime. Replacing it by a linear map improves loss (2.41 → 2.12·10⁻⁷).
  - Heads 0 and 2 compute single-frequency degree-2 terms. Heads 1 and 3 have opposite patterns and amplify all key frequencies.
- **Why several frequencies (App. B).** A single cosine has near-maxima away from 0 (cos(2π·14·8/113) ≈ 0.998). Summing frequencies interferes constructively only at a + b ≡ c.
- **Phases (§5.2, Fig. 7).**
  - Memorisation, 0–1.4k epochs: train and excluded loss fall.
  - Circuit formation, 1.4k–9.4k: excluded loss rises, restricted loss falls, and the sum of squared weights falls, while train and test loss stay flat.
  - Cleanup, 9.4k–14k: test loss drops suddenly, weight norm drops sharply, and the Fourier Gini coefficient jumps.
  - Across seeds, memorisation always ends at about 1,400 epochs, while the later phase boundaries vary (App. C.2.1).
- **Other seeds (App. C.2.1, Tables 3–4).** They use 3–4 key frequencies, different per seed. Ablating the key frequencies gives loss 6.5–11, and keeping only them gives about 6·10⁻⁸.
- **Regularisation and data (§5.3; App. C.2.2, D.1).**
  - No grokking with λ = 0: excluded loss never rises.
  - λ = 0.3 groks in about 3k epochs, λ = 1 in 5–10k, λ = 3 in 20k (App. D.1). This conflicts with the sentence before it, which says larger weight decay groks faster.
  - Dropout (p = 0.2, 0.5) also groks, and L1 does not.
  - At ≥60% data (P = 113) generalisation is immediate. At 10–20%, no generalisation within 40k epochs.
  - P = 53 needs λ = 5. P = 401 generalises immediately at 20%.
- **Other tasks (App. D.3).** 5-digit addition, repeated subsequences and skip-trigrams grok only with limited data (700 or 512 points), not with fresh data per step.
- **Every generalising weight-decay model uses a Fourier-multiplication variant** (Table 5). Dropout models are not sparse in the Fourier basis.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The mainline network computes a + b mod 113 by Fourier multiplication | strong (experiment: weights, activations, ablations) | §4, Tables 1–2, Figs. 3–6 |
| C2 | Generalising weight-decay models across seeds, data fractions, primes and depth use variants of it | strong–moderate (experiment) | App. C.2, Table 5 (key frequencies differ per run) |
| C3 | Training splits into memorisation, circuit formation and cleanup, with the circuit formed before the test-accuracy jump | moderate–strong (experiment) | Fig. 7, 5 seeds (Figs. 18–19); phase boundaries chosen by eye from inflection points |
| C4 | Grokking needs regularisation (weight decay or dropout) and limited data | moderate (experiment) | App. D.1, D.3, within these budgets; cf. Power et al.'s no-weight-decay run ([LIT-341](../literature.d/LIT-341.md)) |
| C5 | Weight decay drives circuit formation and cleanup | moderate (correlation plus argument) | weight-norm inflections (Fig. 7); the App. E.1 argument is speculative |
| C6 | Mechanistic interpretability can supply progress measures for emergence generally | weak (proof of concept) | §6 and App. F say so |
| C7 | Phase transitions are inherent to circuit composition (the lottery-ticket-style explanation) | weak (speculation) | App. E.2, labelled a hypothesis |

## Method

1. Take Fourier transforms of weights and activations over the input axes.
2. Do a low-rank decomposition of W_L onto cos/sin directions.
3. Regress activations on degree-2 trigonometric polynomials and report fraction of variance explained.
4. Replace components by their approximations or ablate them.
5. Track 2D-DFT logit ablations (restricted and excluded loss), Fourier Gini coefficients and weight norm through training.

## Concepts

- **Fourier multiplication algorithm.**
- **Key frequencies.**
- **Neuron-logit map W_L.**
- **Progress measure.** Restricted loss and excluded loss (after Barak et al.).
- **Memorisation, circuit formation and cleanup phases.**
- **Constructive interference.**
- **Slingshot mechanism.** Unnecessary for grokking here (App. D.2).

## Connections

- **[LIT-341](../literature.d/LIT-341.md) (Power et al.).** The source phenomenon. The claim that regularisation is needed (C4) should be read against [LIT-341](../literature.d/LIT-341.md)'s Fig. 1 run, which grokked with Adam and no weight decay over 10⁶ steps. The paper's own App. D.2 points to Thilak et al.'s slingshot as an implicit regulariser in such runs.
- **Barak et al. 2022** (progress measures, parities) and **Liu et al. 2022** (effective theory).
- **Olsson et al. 2022** (induction heads) for phase changes.
- **[LIT-323](../literature.d/LIT-323.md) (Toy Models of Superposition).** The same circuits line of work. Here, by contrast, the computation is "mostly aligned with the neuron basis" per frequency.

## Bearing on the record

**Row 7 ("predicate harmonics = characters; irrep multiplets = spectral degeneracies").** This is the strongest connection in the batch, and the paper never states it.

- **The structure in representation-theory terms.**
  - The real Fourier modes cos(2πk·x/113), sin(2πk·x/113) for k and 113 − k span the real 2-dimensional irreducible representations of ℤ/113 (the pair of complex characters χ_k, χ̄_k).
  - W_L ≈ Σ over five k of the (cos w_k, sin w_k) pairs is a sum of five such irrep "doublets" (rank 10).
  - The cos and sin parts enter with nearly equal coefficients in Table 1 (e.g. 44.6 against 43.6, and 44.1 against 44.1, for k = 14). That is what the rotation structure requires.
  - Whether the corresponding singular values of W_L are themselves degenerate in pairs, the spectral signature row 7 has in mind, is plotted as component norms (Fig. 3 right) but not reported numerically. It is unverified here.
  - The group operation is realised as rotation, the representation itself.
- **So the paper is empirical evidence** that a trained network can organise its weights into a small set of irreps of the task's symmetry group, with the logits a character sum. Row 7 predicts exactly that kind of structure.
- **But it does not pre-empt the row's `NOVEL-NARROW` part.**
  - Nanda et al. *chose* the DFT basis because they knew the group. The map's claim is to *detect an unknown* symmetry via degeneracy in a spectrum.
  - The map's §5 warns that equivariance and feature-geometry groups could get there first. This paper and its follow-ups are the closest such work in the record.
  - The owner should cite it as the known-group precedent and position the degeneracy-as-diagnostic as the step it does not take.
- **The non-abelian case.** Its irreps are not 1- or 2-dimensional. That falls under [LIT-305](../literature.d/LIT-305.md) (Kondor & Trivedi, harmonic analysis on compact groups), seeded and not read. Power et al.'s S₅ coset pictures ([LIT-341](../literature.d/LIT-341.md)) are only qualitative.

**Row 15 ("grokking; concept resolvability; SLT").** The paper supplies a mechanism, not a singular-learning-theory account.
- *What it offers.* Its explanatory story (App. E.1) is complexity under weight decay: the generalising circuit reaches the same training loss with smaller weights, so weight decay eventually prefers it.
- *What it does not use.* No Fisher information, degeneracy or learning coefficient appears.
- *The link to [LIT-354](../literature.d/LIT-354.md) (Watanabe) is by analogy.* Cleanup reduces the effective number of parameters in use: the Gini coefficient rises and W_L is rank 10 out of 113 × 512. That is the direction in which an SLT learning coefficient would fall. The paper measures none of it.
- *So:* the map's `KNOWN (SLT)` / `SYNTHESIS (framing)` verdict stands, and this paper is correctly cited for the mechanism of grokking, not for resolvability.

**ML practice.** It is held in the anthology ([ANTH-LIT-085](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-085.md), `Active`; [NOTE-052](NOTE-052.md)). Disagreements with the anthology's reading, reported per [ADR-013](../decisions.d/ADR-013.md) and not fixed here:
- **"Grokking disappears above about 60% data" ([ANTH-LIT-085](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-085.md) takeaway; [NOTE-052](NOTE-052.md) C4, "strong").** Measured for P = 113, one-layer, λ = 1, in the appendix (C.2.2, Fig. 20), not the main text. The paper's own P = 401 runs show it is the amount of data, not the fraction, that matters: 20% of 401² pairs generalises immediately. The threshold as a fraction is setting-specific. The anthology's broader reading ("a data-starved-regime phenomenon") is supported.
- **"Weight decay … is load-bearing" and C5 "weight decay drives the cleanup phase".** App. D.1 shows dropout (p = 0.2, 0.5) also produces grokking without weight decay; L1 does not. And the founding paper's headline run ([LIT-341](../literature.d/LIT-341.md), Fig. 1) grokked with no weight decay. "Regularisation, in these budgets" is what the evidence supports.
- **[NOTE-052](NOTE-052.md)'s Key results list "Gini coefficients of W_U and W_L".** This reproduces the paper's §5.2 slip. §5.1 and Fig. 7 define them for W_E and W_L.
- **Otherwise [NOTE-052](NOTE-052.md) matches the text.** That includes the numbers, the phases, the five seeds and the "proof of concept" disclaimer. Two small additions:
  - The phase boundaries are read from inflection points by eye.
  - App. D.1's weight-decay/speed numbers contradict the sentence they illustrate (λ = 0.3 at about 3k epochs is faster than λ = 3 at about 20k, but the text says less weight decay is slower).

## Limitations

- **Small setting.** One task in the main text, a tiny one-layer model, and full batch. The progress measures are specific to the task by construction.
- **Phases by eye.** Phase boundaries are drawn from inflection points, not a defined criterion.
- **Regularisation claims are budget-relative.** "No grokking without regularisation" holds within 40k epochs, against Power et al.'s 10⁶-step no-weight-decay run.
- **Speculative appendices.** E.1 and E.2, the intuitive explanation and the composition hypothesis, are speculation and labelled as such.
- **Internal inconsistencies.** The W_U/W_E Gini naming, the weight-decay speed direction in D.1, and figure-label slips (see corrections).

## Open questions

- If the DFT basis is *not* supplied, does the degeneracy structure of W_L's singular spectrum (pairs of nearly equal singular values) recover the key frequencies and the group? That is the row-7 experiment on a solved case. It is cheap here, because the answer is known.
- For a non-abelian task (Power et al.'s S₅, [LIT-341](../literature.d/LIT-341.md)), do generalising networks use higher-dimensional irreps, with d²-fold degenerate blocks? That would be the first non-trivial test of "irrep multiplets = spectral degeneracies".
- Does a learning-coefficient estimate ([LIT-354](../literature.d/LIT-354.md)) track the cleanup phase in this setting? That would turn row 15's analogy into a measurement.

## Corrections to the seeded skim

- Seeded from metadata. The text confirms the title, authors (Nanda, Chan, Lieberum, Smith, Steinhardt), the arXiv id and ICLR 2023. I read v3 (19 Oct 2023). The seed's `published: 2023-01-12` is the v1 date and stays correct.
- The seed summary is accurate. It should add three things.
  - *The setting* is one-layer, P = 113 and full batch, with weight decay λ = 1.
  - *Regularisation.* The paper claims grokking needs weight decay or another regulariser (dropout works, L1 does not; App. D.1).
  - *Data.* Grokking disappears at ≥60% data for P = 113 (App. C.2.2, Fig. 20). That is a statement about the amount of data, not a universal fraction: at P = 401, 20% of pairs generalises immediately.
- Slips in the text.
  - The first identity in §3.1 is typed cos(w_k·a)·cos(w_k·a) − …; it should read cos(w_k·a)·cos(w_k·b).
  - §5.2 names the Gini matrices "W_U and W_L", but §5.1 and Fig. 7 say W_E and W_L.
  - App. C.1.2 refers to "Table 1" for the attention coefficients, which are in Table 2.
  - App. D.1 cites a nonexistent "Section 7".
  - Fig. 24's caption writes the weight decay as γ = 5 (γ is the learning rate elsewhere).
  - Fig. 34 is titled "50 Data Points" but captioned 512.
- Map roles (row 15 grokking mechanism; row 7 Fourier/character structure) hold, with the qualifications in Bearing on the record.
