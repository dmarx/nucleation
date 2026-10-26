---
status: Read
paper: LIT-tmpajpeb
title: 'Meng, Bau, Andonian and Belinkov — Locating and editing factual associations in GPT'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Read in full on 2026-10-26 from the arXiv PDF of 2202.05262v5 (13
    January 2023; footer "36th Conference on Neural Information Processing
    Systems (NeurIPS 2022)"), fetched from arxiv.org/pdf/2202.05262, text
    extracted with pdftotext. Read: §§1–6 and Appendices A (the derivation
    of the rank-one update), B (causal tracing details, other models,
    other corruptions, integrated gradients), C (zsRE), D (CounterFact
    construction), E (baselines and ROME's implementation), the extended
    results on smaller models, the generation samples for GPT-2 XL and
    GPT-J, the dataset samples, the attention-editing experiment and the
    human evaluation with its instructions. The heat maps, line plots and
    hyperparameter sweeps were read from captions and text; Tables 1, 2
    and 4 were read as tables. v1 (10 February 2022, "Locating and Editing
    Factual Knowledge in GPT") was fetched and compared only on its title,
    its causal-trace numbers, its dataset count and its choice of edit
    layer. The record checked Table 4's scores and the closed-form update
    (below).
date: '2026-10-26'
summary: >-
  Causal tracing restores one clean hidden state into a run whose subject
  tokens were noised, and measures how much of the correct object's
  probability comes back. In GPT-2 XL, over 1000 known facts, the effect
  concentrates at two sites: middle layers at the last subject token,
  where MLP outputs dominate, and late layers at the last token, where
  attention does. A rank-one update of one middle MLP's output matrix,
  keyed on the subject's last token, then inserts counterfactual facts
  that generalize to paraphrases while sparing neighbouring subjects, which
  no other editor tested does on the new CounterFact dataset. The authors
  read this as showing where and how facts are stored.
---
<!-- inactive-ok-file: THEORY-tmpvugrm CLAIM-tmpwr001 THEORY-802 CLAIM-130 — Proposed; the hypothesis this reading files and the claims and accounts it bears on, cited as open -->

# NOTE-tmp0p8a7: Meng, Bau, Andonian and Belinkov — Locating and editing factual associations in GPT

## Contribution

Two methods and a benchmark. Causal tracing applies causal mediation
analysis to hidden states: corrupt the subject, restore one state, and
read off how much of the fact returns. ROME edits one MLP layer by a
closed-form rank-one update that makes a chosen key map to a chosen value
while disturbing the layer's other key–value pairs as little as possible
in a least-squares sense. CounterFact tests edits for efficacy,
generalization to paraphrases, specificity to related subjects, fluency
and consistency. The paper uses the edit as a test of the localization:
editing where tracing points works best.

## Key insight

Two interventions point to one place. Restoring states shows that in
GPT-2 XL a fact's recall depends on middle-layer MLP outputs at the
subject's last token. Editing weights shows that a rank-one change to one
of those MLPs, at that token, changes the fact in a way that generalizes
and stays specific, and that editing elsewhere does worse. The authors
infer that middle MLPs are key–value stores keyed by the subject. The
inference from "editing here works" to "the fact is stored here" is the
step the record holds to be unproven (LIT-968).

## Assumptions

- **Facts as tuples** (s, r, o), elicited by a prompt naming s and r.
- **Corruption.** Gaussian noise of scale ν = 3σ_t (three times the
  empirical standard deviation of token embeddings) added to the subject
  tokens' embeddings, ten samples per prompt. Clean probability of the
  correct object averages 27.0% on the 1000 known facts; corrupted, 8.47%.
- **Effects.** TE = P[o] − P*[o]; IE of a state = P*_{clean h}[o] − P*[o],
  averaged over prompts (ATE, AIE). The direct effect was "noisy and
  uninformative" and not reported. MLP and attention effects were
  computed for runs of ten consecutive layers, since single-layer
  restorations had "generally negligible effects".
- **The MLP as associative memory.** W_proj is treated as solving
  W K ≈ V for keys K and values V. Inserting (k*, v*) minimizes ‖Ŵ K − V‖
  subject to Ŵ k* = v*, solved by Ŵ = W + Λ(C⁻¹k*)ᵀ with C = KKᵀ estimated
  from 100,000 Wikipedia token activations and
  Λ = (v* − W k*)/((C⁻¹k*)ᵀ k*).
- **Choosing k* and v*.** k* is the MLP's post-nonlinearity activation at
  the last subject token, averaged over 20 random prefixes. v* is
  optimized (Adam, at most 20 steps) to make the edited output predict o*,
  with a KL term (weight 10²) keeping "{subject} is a" predictions close
  to the original.
- **Models.** GPT-2 XL (1.5B, 48 layers) throughout; GPT-J (6B) for
  editing; GPT-NeoX (20B), GPT-2 Medium and Large for traces; layers
  numbered from 0.

## Key results

- **Causal traces (GPT-2 XL, 1000 facts).** ATE 18.6%. "A large portion
  of the effect is mediated by strongly causal individual states
  (AIE=8.7% at layer 15) at the last subject token", the "early site";
  the "late site" at the last token is expected. MLP contributions peak at
  AIE 6.6% at the early site, attention there at 1.6%; attention dominates
  at the late site.
- **Severing.** Freezing the MLPs at their corrupted values while restoring
  a state removes the causal effect of low-layer states at the last
  subject token but not of higher-layer ones; freezing attention shows no
  such transition. The authors conclude MLP computation at middle layers
  is essential.
- **Robustness.** Similar traces in GPT-J, GPT-NeoX and smaller GPT-2s
  (with more early attention in the Eleuther models), with an extra token
  corrupted, and with noise matched to the embeddings' covariance or
  uniform. Smaller noise (ν = σ_t) gives effects too small to read.
  Integrated gradients do not show the pattern. Some facts depend on an
  earlier subject token ("Mitsubishi" in "Mitsubishi Electric").
- **zsRE (Table 1, GPT-2 XL, 10,000 records).** ROME: efficacy 99.8,
  paraphrase 88.1, specificity 24.2; MEND-zsRE, trained on zsRE, has the
  best paraphrase score, 99.3. Specificity barely moves for any method,
  which the authors take to show the measure is insensitive.
- **Edits by layer and token (Figure 5).** ROME at each layer–token pair:
  best at the last subject token in middle layers, generalization peaking
  at the 18th layer; earlier or later tokens generalize or specialize
  poorly. Editing late-layer attention instead (AttnEdit, layer 33)
  reproduces the rewriting prompt but fails on paraphrases.
- **CounterFact (Table 4).** 21,919 records; 7,500 tested on GPT-2 XL and
  2,000 on GPT-J. Score S, the harmonic mean of efficacy (ES),
  paraphrase (PS) and neighborhood (NS) scores: ROME 89.2 on GPT-2 XL
  (ES 100.0, PS 96.4, NS 75.4) and 91.5 on GPT-J; next best FT+L, 66.9 and
  68.7. Fine-tuning generalizes but damages neighbours (GPT-2 XL NS 40.4;
  GPT-J 10.3); FT+L is specific but generalizes poorly (PS 48.7); KE and
  MEND trained on CounterFact damage neighbours badly (NS 6.9, 5.5).
  Knowledge Neurons barely edit (ES 28.7).
- **Human evaluation.** Fifteen volunteers, 50 facts, 150 judgements
  each of consistency and fluency: ROME rated more consistent with the
  inserted fact than FT+L 1.8 times as often, and somewhat less fluent.
- **Limits the authors state.** One fact per edit; edits are directional
  ("The Space Needle is in Seattle" and "the iconic landmark in Seattle is
  the Space Needle" are separate); only factual associations studied; the
  edited model "will guess plausible new facts that have no basis in
  evidence".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | In GPT-2 XL, restoring states at middle layers of the last subject token recovers much of a corrupted fact's probability, mostly through MLP outputs | strong for this measure | 1000 facts, confidence intervals in Figure 7, robust to corruption choices (THEORY-tmpom5gw) |
| C2 | The same pattern holds in GPT-J, GPT-NeoX and smaller GPT-2s | moderate | traces in Appendix B, with the noted differences |
| C3 | ROME edits generalize and stay specific better than the other editors tested | strong for these baselines and metrics | Table 4; the record recomputed S |
| C4 | Edits work best where tracing points (last subject token, middle layers) | moderate | Figure 5, one model |
| C5 | Mid-layer MLPs store factual associations as linear key–value memories keyed by the subject | weak to moderate | inferred from C1 and C4; LIT-968 shows C4 does not imply it (THEORY-tmpvugrm) |
| C6 | Any middle MLP layer could store any fact equivalently | conjecture | stated from Zhao et al.'s layer-swap result, not tested |
| C7 | Late attention reads the recalled attribute and moves it to the prediction | moderate | traces and AttnEdit's regurgitation |

## Concepts

- **Causal tracing**: clean, corrupted, and corrupted-with-one-restored-
  state runs; the indirect effect of a state is the probability it
  restores.
- **Early and late sites**: middle layers at the last subject token; late
  layers at the last token.
- **Linear associative memory**: a matrix W storing pairs by W K ≈ V
  (Kohonen, Anderson).
- **ROME**: Rank-One Model Editing, the constrained least-squares rank-one
  insertion of (k*, v*) into an MLP's output matrix.
- **CounterFact metrics**: ES/EM (efficacy score and magnitude), PS/PM
  (paraphrase), NS/NM (neighbourhood), S (harmonic mean of ES, PS, NS),
  GE (n-gram entropy of generations), RS (TF-IDF similarity to reference
  texts).
- **Essence drift**: an edit changing what kind of thing the subject is.

## Connections

It applies causal mediation analysis (Pearl 2001; Vig et al. 2020) to
hidden states, takes MLPs as key–value memories from Geva et al. (2021) and
the rank-one insertion from Bau et al.'s rewriting of generative models
(2020), and compares with fine-tuning, constrained fine-tuning (Zhu et
al.), Knowledge Neurons (Dai et al.), KE (De Cao et al.) and MEND (Mitchell
et al.). It cites Elhage et al. (LIT-tmp9dono) for attention as copying.
MEMIT (Meng et al. 2022) extends it to many edits. The record holds the
principal critique: Makelov et al. (LIT-968). The record does not hold
Hase et al.'s test of whether tracing predicts which layer edits best.

## Bearing on the record

- **LIT-968, THEORY-282.** Makelov et al. prove (their Lemma D.2) that any
  one-dimensional fact patch in an MLP has a rank-one weight edit with the
  same output at that token, and find ROME edits approximated by subspace
  interventions across layers 20–35 of GPT2-XL, whose fact patches depend
  on the null space of W_out. So a successful rank-one edit at a layer is
  available whether or not the fact is "stored" there. That undercuts C5
  and the reading of C4 as confirmation, not C1 or C3. THEORY-tmpvugrm is
  filed Proposed for that reason.
- **CLAIM-tmpwr001.** Causal tracing locates where restoring a state helps
  a corrupted run; ROME shows where writing a state changes the output.
  Neither locates the variable that does the work in the uncorrupted
  model, which is the distinction the claim draws between a recovered
  feature and what organizes the behaviour. The analogy is the record's.
- **QUESTION-030 and CLAIM-130.** Causal tracing is an intervention that
  sets states to values from another run, as in CLAIM-130's do(S)
  caution. Restoring a clean state into a noised run tests sufficiency
  within that run, not what constitutes recall.
- **THEORY-802.** The key k* is a direction in MLP activation space chosen
  by averaging; the value v* is found by optimization. Many (k, v) pairs
  could produce the same edit, and the paper does not ask whether its pair
  is the one the model uses.
- **LIT-tmpj9tel.** IOI finds a circuit of heads with MLPs left out; this
  paper finds MLPs decisive for facts and attention for moving them. The
  two are complementary pictures of GPT-2-family models, each treating the
  other's components as given.
- **Accounts filed.** THEORY-tmpom5gw (Active): the traces and the edits
  as measured. THEORY-tmpvugrm (Proposed): the localized factual
  association hypothesis.

No instruction for machine-learning practice is drawn; model editing and
its evaluation are practice, the anthology's (`anthology-candidate`).

## Limitations

- **Corruption defines the effect.** IE is measured against a noised run;
  smaller noise makes effects unreadable, and the noise is off the data
  distribution.
- **Single states matter little alone** for MLPs and attention, so their
  effects are reported for windows of ten layers, which blurs which layer
  matters.
- **zsRE specificity** is insensitive, as the authors note; CounterFact's
  neighbourhood prompts fix that for related subjects only.
- **Editing success is not localization** (LIT-968).
- **One fact per edit, directional, factual associations only.**

### Errors and inconsistencies found

- **The hidden-state peak.** §2.1 gives "AIE=8.7% at layer 15". Appendix
  B.1 says restoring the best state, bucketed by layer, peaks "around the
  15th layer of the last subject token, where the score is raised on
  average to 15.0%", from a corrupted 8.47%: an AIE of 6.5%. The MLP peak
  in the same appendix is also "15.0%" (AIE 6.5%, matching §2.1's 6.6%), so
  one of the two 15.0% figures, or the 8.7%, is wrong. v1 has the same
  appendix sentences.
- **Figure references from v1.** v5's Appendix B and E.5 refer to "Figure
  1j", "Figure 1k", "Figure 1l" and "Figure 1m"; v5's Figure 1 has panels
  a–g. E.5 also says "as Figure 3 shows, layer 18 is approximately when MLP
  outputs begin to switch from acting as keys to values"; v5's Figure 3 is
  the severed-MLP trace and shows no such analysis.
- **The edit layer.** v5 edits GPT-2 XL at layer 18, "the center of causal
  effect in MLP layers"; Appendix B.1 centres the MLP effect at "the 17th
  layer", and v1 edited at layer 15. With layers numbered from 0, the 18th
  layer of §3.4 is layer 17. The choice is defensible from Figure 5, but
  the stated reasons do not agree.
- **zsRE fields.** Appendix C: "t∗ and P N were included in the original
  version of zsRE, whereas P N was added by Mitchell et al." One of the two
  should be the paraphrase set P P.
- **Checked and consistent.** The ATE of 18.6% matches 27.0% − 8.47%. Every
  S in Table 4 is the harmonic mean of its row's ES, PS and NS to within
  0.1. The closed-form update satisfies the constraint and equals the
  Lagrangian solution of the constrained least-squares problem (checked
  numerically on random keys and values, to 10⁻¹⁵). The dataset's 21,919
  records and 21,595 counterfactual statements (Table 2) count different
  things.

## Open questions

- Does the layer where causal tracing peaks predict where edits work best,
  across facts? (Hase et al. 2023, not held, asks this.)
- What would a test that separates storage from editability look like,
  given Makelov et al.'s equivalence of rank-one edits and fact patches?
- Why are edits directional, and what does that say about the key?
