---
status: Read
paper: LIT-341
title: 'Grokking: Generalization Beyond Overfitting on Small Algorithmic Datasets'
version: 1
history:
- version: 1
  date: '2026-09-29'
  note: >-
    Read in full (Full text of arXiv 2201.02177 v1 (6 Jan 2022; the only
    version), 10 pp.: abstract, §§1–4, Appendices A.1–A.5 and references.
    Text was extracted with PyMuPDF. The figures are images and were read
    from their captions and the text. I did not read the 2021 ICLR MATH-AI
    workshop version, and nothing in this PDF mentions it.). The first NOTE
    on this paper, which was seeded from its abstract alone.
date: '2026-09-29'
summary: >-
  Small decoder-only transformers (2 layers, width 128, 4 heads, ~4·10⁵
  non-embedding parameters) trained on binary-operation tables over
  abstract symbols can reach 100% validation accuracy long after fitting
  the training set. In the headline run (division mod 97, 50% data, Adam
  with no weight decay, a budget of 10⁶ steps), training accuracy is
  near-perfect before 10³ steps, validation accuracy only near 10⁶, with
  little progress before 10⁵. The optimisation time to generalise rises
  steeply as the training fraction falls (on S₅ near 25–30% data, −1% data
  costs +40–50% median steps), and weight decay is the most data-efficient
  intervention tried.
---

# NOTE-tmpdix4e: Grokking: Generalization Beyond Overfitting on Small Algorithmic Datasets

## Contribution

The paper proposes small algorithmic datasets as a cheap, single-GPU testbed for generalisation: binary-operation tables a∘b = c with each element an unstructured token. In that testbed it:

- **Names the phenomenon.** Grokking is validation accuracy rising from chance to perfect far past the point of overfitting.
- **Gives data-efficiency curves** for 12 operations.
- **Shows the cost of less data.** Optimisation time to generalise grows fast as data shrinks, while time to fit does not.
- **Ranks interventions.** Weight decay is best.
- **Shows structure in the output weights.** Learned output-layer weights sometimes show the algebraic structure of the operands.

## Key insight

With little enough data from a structured table, generalisation stops accompanying fitting and becomes something that can happen much later, if at all. How much later is a steep function of how much data was withheld and how the optimiser is regularised.

## Assumptions

- **The data.** Equations ⟨x⟩⟨op⟩⟨y⟩⟨=⟩⟨x∘y⟩ with p = 97 for the modular operations and S₅ for the permutation ones (12 operations, App. A.1.1). The training set is a random fraction of all equations, and the rest is validation.
- **The model.** A decoder-only transformer with causal masking, 2 layers, width 128, 4 heads, ~4·10⁵ non-embedding parameters. Loss and accuracy are computed on the answer token only (App. A.1.2).
- **Default optimisation.**
  - AdamW, learning rate 10⁻³, weight decay 1, β₁ = 0.9, β₂ = 0.98, 10 warm-up steps.
  - Minibatch min(512, half the training set), a budget of 10⁵ updates.
  - The §3.1.1 learning-time curves use 5·10⁵ updates.
  - The §3.1 headline run uses 10⁶ updates and Adam with no weight decay.
- **Abstract symbols.** The network never sees numeric or permutation notation.

## Key results

- **Grokking (§3.1, Figs. 1 and 4).**
  - Division mod 97 at 50% data: training accuracy near 100% before 10³ steps, validation near 100% at about 10⁶, with little generalisation before 10⁵.
  - Validation loss rises from about 10² to 10⁵ steps before a second descent.
  - This is "typical" near the minimal generalising data size.
- **Learning time (§3.1.1, Fig. 1 centre).**
  - For the product in S₅, median steps to 99% validation grow steeply as data shrinks; near 25–30% data, −1% data gives +40–50% steps.
  - Steps to 99% training accuracy trend down and stay at 10³–10⁴.
  - A similar "exponential increase" is seen on every task that generalised.
- **Across operations (§3.2, Fig. 2 right).**
  - x−y (mod p−1) and x/y (mod p) need about the same data. They are the same group up to relabelling via a primitive root, and the paper checks this.
  - Symmetric operations need less data than asymmetric ones (possibly an architecture effect).
  - x³ + xy² + y (mod 97) never generalised up to 95% data.
  - A mixed rule (x/y for odd y, x−y otherwise) did generalise.
- **Ablations on S₅ (§3.3, Fig. 2 left).**
  - Weight decay "more than halving" the data needed is the strongest intervention. Decay toward the initialisation helps, but less than decay toward the origin.
  - Minibatch, gradient or weight noise helps.
  - The learning rate must be within about one order of magnitude.
  - "Some generalization happens even with full batch optimizers and models without weight or activation noise at high percentages of training data."
- **Output-layer structure (§3.4, Fig. 3).** t-SNE of the output layer shows cosets of a subgroup for S₅ and a circular "number line" (+8 steps) for modular addition. The structure is clearer with weight decay.
- **Outliers (A.4, Fig. 6).** Up to about 1,000 randomly relabelled training examples barely affect generalisation, and more hurts it. Training always reaches 100%, so the network memorises the outliers rather than denoising them.
- **Sharpness (A.5, Fig. 7).** On S₅ composition, a Keskar-style sharpness φ correlates with validation accuracy at Spearman −0.79548 (p < 0.000014). The paper calls this "suggestive" that grokking happens in flatter regions.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Networks can generalise from chance to perfect far past overfitting on small algorithmic tables | strong (experiment) | Fig. 1 and its loss curves (Fig. 4); typical near the minimal data size |
| C2 | Optimisation needed to generalise rises steeply as the training fraction falls | moderate–strong (experiment) | S₅, 7 seeds (Fig. 1 centre); "similar pattern" asserted for the other tasks |
| C3 | Weight decay is the most effective intervention for data efficiency | moderate (experiment) | one task (S₅), 3 seeds, 10⁵ steps (Fig. 2 left) |
| C4 | Noise helps via flatter minima | weak (conjecture) | consistent with Fig. 2; flatness link offered as a hypothesis (§3.3, A.3), plus one correlation (A.5) |
| C5 | Learned output layers reflect the operands' algebraic structure | weak–moderate (qualitative) | t-SNE pictures "for some networks" (Fig. 3) |
| C6 | The phenomena are architecture-agnostic | assertion | A.3 says the emphasis is on phenomena "we believe to be architecture-agnostic"; one architecture tested |
| C7 | Grokking is distinct from double descent | weak (argument) | A.3: the second descent comes far past interpolation and accuracy is not non-monotone |

## Method

1. Enumerate all equations for an operation and hold out a random fraction.
2. Train a fixed small transformer with fixed hyperparameters, sweeping the data fraction and the optimiser/regularisation variant.
3. Record steps to 99% train and validation accuracy, and best validation accuracy within a budget.
4. Visualise the output-layer weights with t-SNE.
5. Measure sharpness per Keskar et al.

## Concepts

- **Grokking.** Generalisation far beyond the point of overfitting.
- **Algorithmic-dataset testbed.**
- **Data-efficiency curve.**
- **Optimisation-time-versus-data trade.**
- **Outlier memorisation.**
- **Sharpness/flatness as a predictor of grokking.**

## Connections

- **[LIT-345](../literature.d/LIT-345.md) (Nanda et al. 2023).** It supplies the mechanism for modular addition: a Fourier-multiplication circuit, then memorisation, circuit formation and cleanup. It also claims grokking needs weight decay or dropout. That sits awkwardly with this paper's Fig. 1 run, which grokked with plain Adam and no weight decay over a 10⁶-step budget. Nanda's budget was 40k epochs and its setting differed (1 layer, p = 113, full batch, 30% data). Nanda cites Thilak et al.'s "slingshot" as the likely implicit regulariser in such runs.
- **Double descent** (Nakkiran et al.; Belkin et al.): distinguished in A.3.
- **Zhang et al. 2016 ("rethinking generalization"):** the converse phenomenon (A.3).
- **Keskar et al. / Hochreiter & Schmidhuber:** flat minima (A.5).

## Bearing on the record

**Row 15 ("grokking as a concept-resolvability phenomenon"; must-cite with Watanabe).**
- *What the paper supplies.* The phenomenon, and two measured dependences a resolvability reading would have to explain: time-to-generalise against data fraction, and the effect of weight decay.
- *What it does not supply.* It has no notion of resolvability, identifiability, Fisher degeneracy or singular learning theory. Its explanatory gesture is flatness: noise drives the optimiser to "flatter/simpler solutions", with a Spearman −0.80 correlation between sharpness and validation accuracy on S₅.
- *The honest link to [LIT-354](../literature.d/LIT-354.md) (Watanabe).* Flat, degenerate minima are where SLT's local learning coefficient is small, so "grokking happens in flatter regions" is the kind of observation SLT would recast. The paper does not make that link, and one correlation on one task is thin support.
- *So:* the map's verdict (`KNOWN` for SLT, `SYNTHESIS` for the framing) stands. Power et al. are cited correctly as the owner of the phenomenon and should not be cited as support for the resolvability reading.

**Row 7 (predicate harmonics = characters).** The only hint is Fig. 3: a circular embedding for modular addition, and coset clusters for S₅. These are qualitative t-SNE pictures. The quantitative Fourier/character result is in [LIT-345](../literature.d/LIT-345.md).

**ML practice.** It is held in the anthology ([ANTH-LIT-538](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-538.md), `Active`; NOTE-281). Disagreements with the anthology's reading, reported per [ADR-013](../decisions.d/ADR-013.md) and not fixed here:
- **Weight decay, and the headline run's optimiser.** NOTE-281 calls weight decay "the thread" and the strongest intervention. That is true of the §3.3 comparison. But neither NOTE-281 nor [ANTH-LIT-538](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-538.md) records that the headline grokking run (Fig. 1; §3.1) used Adam with no weight decay and a 10⁶-step budget (App. A.1.2). This matters for the anthology's own chain of claims:
  - [ANTH-LIT-085](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-085.md)/[NOTE-052](NOTE-052.md) lean on Nanda's "no grokking without regularisation".
  - The founding example is a grokking run without explicit regularisation.
  - So "weight decay drives grokking" is too strong as a reading of the founding paper. Weight decay speeds grokking and cuts the data needed, but the founding example did not use it.
- **Symbol embeddings.** [ANTH-LIT-538](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-538.md)'s takeaway "learned symbol embeddings sometimes show the structure" follows the paper's contribution list. The paper's figure is of the *output layer* (unembedding) weights; NOTE-281 has this right.
- **Seeds.** NOTE-281 says "results averaged over three seeds where reported". The learning-time curves that carry the "−1% data ⇒ +40–50% steps" number used 7 seeds (A.1.2).
- **Otherwise the anthology's reading matches the text.** That includes the "sometimes" caveat, the x³ + xy² + y failure and the data-fraction headline. NOTE-281's "the founding paper already measured the regime dependence" is correct.

## Limitations

- **One architecture and small tasks.** One tiny architecture, 3–7 seeds, algorithmic tables only. Architecture-independence is believed, not tested.
- **A testbed paper.** It has ablations and no mechanism, and says so (§4).
- **Qualitative visualisations.** The t-SNE pictures are qualitative and shown "for some networks".
- **Different budgets and optimisers across experiments.** The headline run (no weight decay, 10⁶ steps) is not comparable to the ablation setting (AdamW with weight decay 1, 10⁵ steps). Readers routinely merge them.
- **The sharpness result is preliminary.** One task, one correlation.

## Open questions

- Why do some operations (x³ + xy² + y) never grok? The paper offers only "to such a model, the data is effectively random".
- Does "time to generalise" as a function of data fraction have a form that a resolvability or learning-coefficient account ([LIT-354](../literature.d/LIT-354.md)) would predict? An exponential-looking rise is reported but not fitted.
- The no-weight-decay grokking of Fig. 1: is it the slingshot mechanism (as [LIT-345](../literature.d/LIT-345.md) suggests via Thilak et al.), and does it survive with SGD instead of Adam?

## Corrections to the seeded skim

- Seeded from metadata. The text confirms the title, authors (Power, Burda, Edwards, Babuschkin of OpenAI; Misra of Google, "at OpenAI at the time of this work"), the arXiv id and date. The seed's "(earlier ICLR 2021 MATH-AI workshop version)" is not attested in this PDF and is unverified here.
- The seed summary is accurate. It should add two things.
  - *Conditions.* The dramatic grokking is reported for dataset sizes "close to the minimal dataset size for which the network generalized within the allotted optimization budget"; at larger sizes train and validation curves track each other (§3.1).
  - *No weight decay in the headline run.* Figure 1's run used Adam with no weight decay (App. A.1.2), yet the paper's comparison experiments find weight decay the strongest aid.
- Minor.
  - *Output layer, not input embeddings.* The contribution list says "symbol embeddings", but §3.4 and Fig. 3 visualise the output-layer (unembedding) weight matrix.
  - *Seeds.* Results use 3 seeds, but the learning-time curves (§3.1.1) use 7.
- Map role (row 15, "grokking as a concept-resolvability phenomenon") is the owner's framing, not the paper's. See Bearing on the record.
