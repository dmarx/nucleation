---
status: Read
paper: 'LIT-tmpsrubd'
title: 'Meng, Sen Sharma, Andonian, Belinkov and Bau — Mass-editing memory in a transformer'
version: 1
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Read in full on 2026-10-27 from the arXiv PDF of 2210.07229v2 (1
    August 2023; headed "Published as a conference paper at ICLR 2023"),
    fetched from arxiv.org/pdf/2210.07229, text extracted with
    pdftotext. Read: §§1–9 and Appendices A (causal tracing on GPT-J), B
    (implementation and runtimes of each method), C (metric definitions),
    D (mixed relations), E (the election and astronomy demonstrations)
    and F (ablations of layers, module and λ), with Tables 1 and 2 read as
    tables. The scaling curves, the category plots and the ablation plots
    were read from captions and text; numbers that appear only in them
    were not used. Appendix B.4 was also read from a rendering of page 15,
    to settle a fraction the text extraction garbled. v1 (13 October
    2022) was not compared. The record
    checked the update rule, the scores and the runtimes (below).
date: '2026-10-27'
summary: >-
  MEMIT inserts thousands of facts into GPT-J and GPT-NeoX at once. It
  treats the MLP output matrix of each layer in a range that causal
  tracing implicates as a linear associative memory, computes for each
  fact a target change of the hidden state at the top of that range,
  and spreads it over the layers with a closed-form least-squares update
  for the whole batch. At 10,000 CounterFact edits on GPT-J it scores 85.8
  against 50.3 for ROME applied one at a time; ROME is better at a handful
  of edits.
---
<!-- inactive-ok-file: THEORY-1011 THEORY-tmpiz2n7 CLAIM-454 — Proposed; the storage hypothesis it inherits, the account of why tracing and editing part, and a claim it bears on, cited as open -->

# NOTE-tmpt77xq: Meng, Sen Sharma, Andonian, Belinkov and Bau — Mass-editing memory in a transformer

## Contribution

A method that scales direct weight editing from single facts, where ROME
([LIT-1536](../literature.d/LIT-1536.md)) works, to batches of ten thousand, where ROME applied
repeatedly and the hypernetwork editors fail. It does so by solving one
least-squares problem per layer for the whole batch, against a covariance
of previously stored keys, and by spreading each edit over several
layers. It also reruns ROME's causal tracing on GPT-J and uses it to
choose those layers.

## Key insight

If an MLP's output matrix is the least-squares solution for the
associations it already holds, then adding a batch of new associations
has a closed form that needs only the covariance of the old keys:
Δ = R K₁ᵀ (C₀ + K₁K₁ᵀ)⁻¹, where R is the new pairs' residual under the old
weights. And if several consecutive MLPs all add to the subject's hidden
state, the change each edit needs can be split among them, so that each
matrix moves less.

## Assumptions

- **Facts and requests.** Tuples (s, r, o); a batch E with no two requests
  giving the same (s, r) different objects.
- **The memory model.** W_out of each MLP is a linear associative memory
  with W₀ = argmin Σ‖Ŵkᵢ − mᵢ‖², so W₀K₀K₀ᵀ = M₀K₀ᵀ (Eq. 8). Pretraining
  is assumed to have left the weights at that optimum. The old keys are
  assumed to be a random sample of the layer's inputs, so C₀ = λ·E[kkᵀ],
  estimated from 100,000 Wikitext samples (50,000 for GPT-NeoX).
- **λ** weights old against new associations: 15,000 for GPT-J, 20,000
  for GPT-NeoX.
- **Layers.** R = {3, …, 8} for GPT-J, numbered from 0, chosen where the
  gap between restoring a state and restoring it with the MLPs severed is
  largest; R = {6, …, 10} for GPT-NeoX. L = max(R).
- **Targets.** For each fact, δᵢ added to the hidden state at layer L and
  the last subject token is optimized by gradient descent (20 or 25 steps)
  to make the object likely after random prefixes; its norm is clamped
  (to less than 3/4 of ‖h‖ on GPT-J).
- **Spreading.** Layer by layer in ascending order, with activations
  recomputed after each layer's update, layer l receives the fraction
  1/(L − l + 1) of the remaining residual.
- **Baselines.** FT-W (fine-tuning layer 21 with weight decay, tuned only
  at n = 10,000), MEND (the GPT-J hypernetwork trained for ROME), and ROME
  applied sequentially at layer 5. SERAC is not compared, having no public
  code.

## Key results

- **zsRE, 10,000 true facts, GPT-J (Table 1).** Score (harmonic mean of
  efficacy, paraphrase, specificity): MEMIT 50.7 (96.7, 89.7, 26.6);
  FT-W 42.1; MEND 20.0; ROME 2.6 (specificity 0.9); unedited GPT-J 26.4.
  Specificity barely moves for any method that does not break the model.
- **CounterFact, 10,000 counterfactuals (Table 2).** GPT-J: MEMIT S 85.8
  (ES 98.9, PS 88.6, NS 73.7; GE 619.9; RS 40.1); FT-W 67.6 with
  generation entropy collapsed to 293.9; ROME 50.3 with RS 3.3; MEND 23.1;
  unedited 22.4. GPT-NeoX: MEMIT 82.0 (97.2, 82.2, 70.8) against 23.7
  unedited.
- **Scaling (Figure 5).** Over n from 1 to 10,000 on a log grid, ROME
  holds to about n = 10 and degrades from n = 32; MEND declines from
  n = 6 and has almost no effect by n = 10,000; MEMIT is best at large n,
  while at small n ROME generalizes slightly better at slightly lower
  specificity, which the authors put down to ROME's hard equality
  constraint against MEMIT's soft least squares.
- **Relations (Figures 6–7, 10).** On 27 CounterFact relations with at
  least 300 cases, MEMIT's score beats FT and MEND in every one; "plays
  sport" (P641) and "owned by" (P127) are hardest. Mixing two relations
  in one batch gives about the average of the two alone, up to 700 edits.
- **Ablations (Appendix F).** More layers in R raise efficacy,
  generalization and specificity; a range of late MLPs with low causal
  effect is "considerably worse"; editing attention instead of MLPs is
  considerably worse; λ trades specificity and fluency against efficacy
  and generalization, with the score highest near 10⁴.
- **Runtime (Appendix B).** For 10,000 edits on GPT-J: MEND 98 s, FT-W
  0.48 h, MEMIT 7.44 h (6.54 h computing the targets, serial and
  parallelizable, plus 0.90 h for the updates), ROME 12.29 h.
- **Demonstrations (Appendix E).** The November 2022 US election results
  inserted with ES 100% and PS 94%; 289 (star, constellation) facts raise
  GPT-J's accuracy from 53% to 86%.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | At 10,000 edits on GPT-J and GPT-NeoX, MEMIT keeps efficacy, generalization and fluency high and specificity moderate, far above the baselines tested | strong for these baselines and data | Tables 1–2, Figure 5; scores recomputed ([THEORY-tmpukwxl](../theory.d/THEORY-tmpukwxl.md)) |
| C2 | Eq. 14 is the least-squares update for adding a batch of associations to a matrix already at its least-squares optimum | demonstrated | the derivation, checked numerically |
| C3 | Spreading the edit over the causally implicated MLPs, rather than one layer or late layers or attention, is what makes it work | moderate | Appendix F ablations, from plots |
| C4 | Edit performance does not depend on how diverse the batch is | weak to moderate | four relation pairs, up to 700 edits, ten runs each |
| C5 | The edited layers are where facts are stored and recalled | inherited, not tested | from ROME's causal tracing and Geva et al.; see Bearing |

## Method

1. For each fact, optimize δᵢ so that replacing the hidden state h_L at
   the last subject token by zᵢ = h_L + δᵢ makes oᵢ likely after random
   prefixes (Eq. 16).
2. For each layer l in R in ascending order: compute each fact's key
   kᵢˡ (the MLP's hidden activation, averaged over prefixes) and residual
   rᵢˡ = (zᵢ − h_L)/(L − l + 1); set the target mᵢˡ = W_out kᵢˡ + rᵢˡ;
   apply Δˡ = Rˡ Kˡᵀ (Cˡ + Kˡ Kˡᵀ)⁻¹; recompute activations.

## Concepts

- **Critical path of MLP layers**: the range of MLPs at the last subject
  token whose severing most reduces a restored state's effect in causal
  tracing.
- **Linear associative memory**: a matrix W chosen to minimize
  Σ‖Wkᵢ − mᵢ‖² over stored pairs (Kohonen; Anderson).
- **CounterFact metrics**: ES, PS, NS as the share of cases where the new
  (or, for neighbours, the true) object outranks the other; S their
  harmonic mean; GE the weighted bi- and tri-gram entropy of generations;
  RS the TF-IDF similarity to a reference text about the new object.

## Connections

It extends ROME ([LIT-1536](../literature.d/LIT-1536.md)): with one fact and one layer, MEMIT's problem
is ROME's with the hard constraint relaxed to least squares. It cites
Geva et al. ([LIT-tmpe8ypo](../literature.d/LIT-tmpe8ypo.md), and their 2022 follow-up) for MLPs as
key–value memories, Elhage et al. ([LIT-1534](../literature.d/LIT-1534.md)) for the residual stream that
lets each MLP add to the hidden state, and Pearl and Vig et al. for causal
mediation. It compares against fine-tuning (Zhu et al.), MEND (Mitchell et
al.) and sequential ROME. Hase et al. ([LIT-tmpg22tp](../literature.d/LIT-tmpg22tp.md)) test its use of
causal tracing to choose layers and include it as an editing method.

## Bearing on the record

- **[THEORY-1011](../theory.d/THEORY-1011.md).** MEMIT is built on the storage hypothesis, and its
  success at scale is offered as more of the same kind of support: edits
  at the traced MLPs work, at late MLPs or in attention they work less
  well. Makelov et al.'s point ([LIT-968](../literature.d/LIT-968.md)) applies unchanged: an edit at a
  layer can produce the output whether or not the layer holds the fact.
  And Hase et al. ([THEORY-tmpg87ki](../theory.d/THEORY-tmpg87ki.md)) show that MEMIT's success, fact by
  fact, does not follow where tracing places the fact. MEMIT's ablations
  compare ranges of layers averaged over facts, which Hase et al. agree
  matter; they do not test storage. So it adds nothing toward promoting
  [THEORY-1011](../theory.d/THEORY-1011.md).
- **[THEORY-998](../theory.d/THEORY-998.md).** MEMIT's traces on GPT-J (501 facts) reproduce ROME's
  pattern on GPT-2 XL: MLPs at the last subject token in early-to-middle
  layers, attention at the last token late, and severing the MLPs removes
  the early states' effect. GPT-J also shows strong early attention at the
  last subject token, which the severing experiment suggests is not a
  mediator. This extends [THEORY-998](../theory.d/THEORY-998.md)'s measurements to a second model; it
  does not change their scope.
- **[THEORY-tmpiz2n7](../theory.d/THEORY-tmpiz2n7.md).** That spreading an edit over five or six layers
  works better than one is consistent with Hase et al.'s account that
  edits override accumulated information, and with the opposite, that the
  fact is held across those layers. MEMIT does not distinguish them.
- **[CLAIM-454](../claims.d/CLAIM-454.md).** The method's target is a change to the hidden state at
  one layer and token that produces the new object; it then finds weight
  changes that write it. That is an intervention chosen for its output,
  which says nothing about which variable organizes recall in the
  unedited model.
- **Account filed.** [THEORY-tmpukwxl](../theory.d/THEORY-tmpukwxl.md) (Active): the measured scaling
  result.

No instruction for machine-learning practice is drawn. Mass editing is
practice, the anthology's (`anthology-candidate`).

## Limitations

- **The storage reading is assumed**, not tested; the layer range comes
  from causal traces averaged over facts.
- **The memory model's assumptions** (pretraining left W at the
  least-squares optimum; old keys are a random sample of inputs) are not
  checked; λ absorbs the mismatch and is tuned.
- **Baselines.** FT-W is tuned only at n = 10,000 and on one layer; MEND
  uses a hypernetwork trained for single edits; SERAC is missing.
- **zsRE specificity** sits near the unedited model's 26–27 for every
  method except ROME, so it barely discriminates.
- **Directional, (s, r, o) facts only**, as the authors say: an edit of
  "Tim Cook is CEO of Apple" does not edit "the CEO of Apple is Tim Cook".
- **Two models, one run per configuration** for the main tables; the
  relation-mixing plots average ten.

### Errors and inconsistencies found

- **Token label.** §4.3 says δᵢ is added "at layer L and token T", where
  the rest of the section and Eq. 16 use the last subject token S.
- **Model name.** Appendix A writes "Unlike with GPT-XL" for GPT-2 XL.
- **Figure reference.** Appendix D says "Figure D depicts"; the figure is
  Figure 10 (and Figure 7 in the main text).
- **Counting CounterFact.** §5.2.2 calls CounterFact "a collection of
  21,919 factual statements"; they are records of counterfactual edit
  requests ([NOTE-1166](NOTE-1166.md) counts 21,919 records and 21,595 counterfactual
  statements).
- **The GPT-NeoX clamp.** Appendix B.4 clamps "‖h_i^L‖ to 3/10 ‖h_i^L‖",
  the hidden state's norm to a fraction of itself; from the GPT-J
  sentence before it, the norm clamped is δᵢ's.
- **"Speficity"** in Figure 10's axis labels.
- **Checked and consistent.** Eq. 14 equals the joint least-squares
  solution over old and new pairs exactly when W₀ is the old pairs'
  least-squares solution (checked numerically on random keys and values,
  to 10⁻¹⁶); with one new pair it does not satisfy the pair exactly, as
  ROME's constrained update does, which is the soft-versus-hard difference
  §5.2.2 names. Every S in Tables 1 and 2 is the harmonic mean of its row
  to within rounding (ROME's zsRE 2.6 needs a specificity near 0.95, inside
  the printed 0.9). The n grid is round(10,000^(i/16)) for i = 0…16. The
  runtimes agree: 1,716.21 s = 0.48 h, 3,226.35 + 23,546.65 s = 7.44 h,
  44,248.26 s = 12.29 h, about 4.4 s per ROME edit. 10,000 edits against
  SERAC's 75 is the "100x" of the conclusion.

## Open questions

- If edits at layers where tracing does not place a fact work for single
  edits (Hase et al.), does the advantage of the traced range at 10,000
  edits come from the range or from spreading over many layers?
- How far does a batch of edits disturb facts not in the batch, beyond
  the neighbourhood prompts of the edited subjects?
- Do the edited associations compose with the model's other knowledge
  (reverse relations, multi-hop questions), or only reproduce the
  inserted prompt and its paraphrases?
