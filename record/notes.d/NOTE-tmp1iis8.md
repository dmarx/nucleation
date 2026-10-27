---
status: Read
paper: LIT-tmpj9tel
title: 'Wang, Variengien, Conmy, Shlegeris and Steinhardt — A circuit for indirect object identification in GPT-2 small'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Read in full on 2026-10-26 from the arXiv PDF of 2211.00593 (v1 of 1
    November 2022, the only version, fetched from arxiv.org/pdf/2211.00593),
    text extracted with pdftotext. Read: §§1–6 and Appendices A
    (disentangling token and position signals), B (path patching, with
    Algorithm 1), C (S-inhibition keys), D (previous-token heads), E
    (templates), F (backup name movers), G (GPT-2 architecture), H and I
    (induction and duplicate-token heads on random tokens), J (MLPs), K
    (minimality sets), L (adversarial templates) and M (the greedy
    completeness search). The figures (path-patching heat maps, scatter
    plots, the completeness and minimality plots) were read from their
    captions and the text; their values were not read off the plots. The
    head tally, the template count and the linear fit of Appendix A were
    checked by the record.
date: '2026-10-26'
summary: >-
  A circuit of 26 attention heads in seven classes that carries GPT-2
  small's indirect-object predictions on fifteen templates, found by
  tracing back from the logits with path patching and checked against
  three criteria. Mean-ablating everything else keeps 87% of the logit
  difference; knocking out the three main name movers costs 5%, because
  other heads take over; and a greedy search finds knockouts under which
  circuit and model differ by up to 87%. Its by-products: heads that
  communicate positions rather than tokens, induction heads doing a
  different job from their original one, and heads that write against the
  answer.
---
<!-- inactive-ok-file: THEORY-tmpmd4za CLAIM-tmpwr001 CLAIM-367 THEORY-tmpoirdq THEORY-tmpgz1nk — Proposed; the hypothesis this reading files and the claims and accounts it bears on, cited as open -->

# NOTE-tmp1iis8: Wang, Variengien, Conmy, Shlegeris and Steinhardt — A circuit for indirect object identification in GPT-2 small

## Contribution

It is the first attempt to reverse-engineer a natural behaviour of a
pretrained language model end to end. The behaviour is indirect object
identification (IOI): in "When Mary and John went to the store, John gave
a drink to", predict "Mary". The paper names the heads that do it and what
each class does, introduces path patching to find them, and states three
criteria a circuit explanation should meet. Its own circuit meets the
first, meets the other two under easy tests, and fails the second under a
search for the hardest case. The paper reports that failure.

## Key insight

The model runs an interpretable algorithm, "identify all previous names,
remove all names that are duplicated, output the remaining name", and runs
it redundantly. Because components stand in for one another, an
explanation can reproduce the model's output (faithfulness) and still
leave out parts the model uses. So a circuit has to be tested under
knockouts, by comparing circuit and model with the same parts removed.

## Assumptions

- **The model.** GPT-2 small: 12 layers of 12 heads, with layer norms and
  MLPs. Only attention heads are circuit nodes. MLPs, layer norms and
  embeddings are not intervened on in the main analyses.
- **The task.** p_IOI: fifteen templates (Figure 14, in BABA and ABBA
  orders) with single-token names from a list of 100 English first names,
  and places and objects from a hand-made list of 20 words. Metrics: the
  logit difference between IO and S, and the IO probability. GPT-2 small
  has mean logit difference 3.56 over 100,000 samples, prefers IO over S
  99.3% of the time, and gives IO a mean probability of 49%.
- **Knockouts are mean ablations** over p_ABC, the same templates with
  three unrelated names, with the mean taken per template so that
  grammatical information stays constant. A circuit C is evaluated as the
  model with every node outside C knocked out. Zero ablation was "noisy".
- **Path patching.** For a sender head h and receivers R, run x_orig with
  every head frozen at its x_orig value except h, patched from x_new (the
  p_ABC counterpart); MLPs and layer norms are recomputed; record the
  receivers' inputs; then run x_orig with the receivers patched to those
  values. This measures the effect of h on R through paths that avoid
  other heads, averaged over more than 200 pairs.
- **Dot products with unembeddings** ignore the final layer norm's scale,
  which the authors note and say did not change the correlations.

## Key results

- **The circuit (Figure 2).** 26 heads in seven classes. Name Mover Heads
  9.9, 9.6, 10.0. Negative Name Mover Heads 10.7, 11.10. S-Inhibition Heads
  7.3, 7.9, 8.6, 8.10. Induction Heads 5.5, 6.9 (fuzzy: 5.8, 5.9).
  Duplicate Token Heads 0.1, 3.0 (fuzzy: 0.10). Previous Token Heads 2.2,
  4.11. Backup Name Mover Heads 9.0, 9.7, 10.1, 10.2, 10.6, 10.10, 11.2,
  11.9. The record's tally: 3 + 2 + 4 + 4 + 3 + 2 + 8 = 26.
- **Name movers.** They attend to IO at END (mean attention 0.59), and the
  logit they write for a name correlates with their attention to it
  (ρ > 0.81, N = 500). Copy score, the share of name tokens that land in
  the top five logits through the head's OV circuit: above 95% for all
  three, under 20% for an average head. Negative name movers write the
  opposite direction (negative copy score 98%, against 12% for an average
  head); the authors speculate they hedge against confident mistakes.
- **S-inhibition.** Patching the four S-inhibition heads moves the name
  movers' attention from IO to S1. They attend to S2 (mean 0.51) and carry
  two signals, the token S and the position of S1. Over six counterfactual
  datasets, the logit difference after patching is fitted by
  2.31·S_pos + 0.99·S_tok with a mean error of 7% of baseline: position
  matters more than token. The position signal is relative: lengthening
  the prefix with S1–S2 distance fixed leaves the logit difference at 3.57
  against 3.56.
- **Where the position signal comes from.** Duplicate token heads (S2 →
  S1) and induction heads (S2 → S1+1, through previous-token heads 2.2 and
  4.11 by K-composition) write it. Patching their outputs from altered
  position signals drops the logit difference by at least 88% of the
  S-inhibition drop; changing only the token, by less than 8%. So
  "Induction Heads perform a different function compared to what was
  described in their original discovery": here their output is a pointer
  to S1. On repeated random tokens, 4.11 and 2.2 have the highest
  previous-token scores, 5.5 and 6.9 are among the five highest induction
  scores, and 3.0 and 0.1 among the three highest duplicate-token scores.
- **Backup name movers.** Knocking out the three name movers costs only 5%
  of the logit difference: other heads change behaviour and take over,
  and negative name mover 10.7 even turns positive. The authors
  "hypothesize that this compensation phenomenon is caused by the use of
  dropout during training". Before the knockout, the eight backups behave
  diversely: four like name movers, two copy IO and S equally, one prefers
  S1, one copies S2 negatively.
- **Faithfulness.** |F(M) − F(C)| = 0.46, 13% of F(M) = 3.56: the circuit
  keeps 87% of the logit difference.
- **Completeness.** For K ⊆ C, the incompleteness score
  |F(C \ K) − F(M \ K)|. Small for random K and for whole classes; for K
  found greedily, "up to 3.09 (87% of the original logit difference)". The
  greedy sets mix classes and are hard to interpret.
- **Minimality.** For each head v, a K is found such that removing v from
  C \ K changes F by at least 1% of F(M); some heads contribute little.
- **A naive circuit** (no backup or negative name movers) has faithfulness
  0.1 and is easier to show incomplete with random or class knockouts;
  under the greedy search both circuits are similarly incomplete.
- **Adversarial examples.** Adding a sentence that repeats IO ("Mary had a
  good day.") makes the model prefer S 23% of the time; repeating S
  instead, 0.4%. The authors say such examples could have been found
  without the circuit.
- **MLPs.** Knocking out MLP0 reverses the sign of the logit difference;
  other single MLPs matter little; knocking out all MLPs after the first
  gives −1.1.
- **GPT-2 medium (preliminary).** A sparse set of heads affects the logits
  directly, but not all attend to IO and S.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | In GPT-2 small on p_IOI, 26 heads in seven classes carry most of the logit difference by the algorithm described | strong for these templates and this model | path patching at each step, attention analyses, faithfulness 87% ([THEORY-tmpccb5u](../theory.d/THEORY-tmpccb5u.md)) |
| C2 | The circuit is complete | refuted by the paper itself | greedy knockouts give incompleteness up to 87% |
| C3 | S-inhibition heads carry position and token signals, position the larger | strong | Appendix A, six counterfactual datasets, linear fit with 7% error |
| C4 | Induction and duplicate-token heads supply the position signal | moderate | patching from altered-position datasets (≥ 88% vs < 8%); the authors list missing weight-level checks |
| C5 | Backup heads compensate when name movers are knocked out | strong as an observation | Figure 15 |
| C6 | Dropout in training causes the compensation | hypothesis | none offered beyond its plausibility ([THEORY-tmpmd4za](../theory.d/THEORY-tmpmd4za.md)) |
| C7 | Negative name movers hedge to avoid high loss on mistakes | speculation | stated as such |
| C8 | Mechanistic understanding of large models is feasible | weak | one task in one 117M-parameter model; preliminary look at GPT-2 medium |

## Concepts

- **IO, S1, S2, END**: the indirect object; the first and second mentions
  of the subject; the final position.
- **Logit difference**: logit(IO) − logit(S).
- **p_ABC**: the reference distribution with three unrelated names, for
  mean ablation and as x_new.
- **Path patching**: patching a sender's effect on chosen receivers along
  paths that avoid other heads.
- **Faithfulness**: |F(M) − F(C)| small.
- **Completeness**: |F(C \ K) − F(M \ K)| small for every K ⊆ C.
- **Minimality**: every v ∈ C has some K ⊆ C \ {v} with
  |F(C \ (K ∪ {v})) − F(C \ K)| large.
- **Copy score**: share of names whose token is in the top five logits
  when passed through the head's OV circuit.

## Connections

It builds on Elhage et al.'s framework ([LIT-tmp9dono](../literature.d/LIT-tmp9dono.md)) for its notation and
its induction and previous-token heads, on Olsson et al. ([LIT-tmpe7b5o](../literature.d/LIT-tmpe7b5o.md)) for
the induction-head tests, on causal mediation analysis (Vig et al. 2020),
on Geiger et al.'s causal abstraction, and on Nanda and Lieberum's mean
ablation. Meng et al.'s ROME ([LIT-tmpajpeb](../literature.d/LIT-tmpajpeb.md)) is cited as kindred work. Its
circuit is the basis of later benchmarks, among them MIB's IOI tasks
([LIT-tmprlq7z](../literature.d/LIT-tmprlq7z.md)) and the InterpBench model MIB uses, and of Makelov et al.'s
illusion ([LIT-968](../literature.d/LIT-968.md)).

## Bearing on the record

- **[LIT-968](../literature.d/LIT-968.md) and [THEORY-282](../theory.d/THEORY-282.md).** Makelov et al. show the subspace-patching
  illusion on MLP8 of GPT-2 small for this task, and a faithful
  residual-stream direction after layer 8 that is "written only by the
  S-inhibition heads" and read by the name movers. That is this circuit's
  S-inhibition → name mover link, found again by a different method, and
  a check on it that the record now holds.
- **[LIT-tmprlq7z](../literature.d/LIT-tmprlq7z.md), [THEORY-tmp4lqc8](../theory.d/THEORY-tmp4lqc8.md).** MIB's IOI causal variables are on the
  four S-inhibition heads named here, and its finding that token and
  position signals can be disentangled at head level is this paper's
  Appendix A, re-run.
- **[CLAIM-tmpwr001](../claims.d/CLAIM-tmpwr001.md).** Induction heads here do something other than what
  defines them: their output serves as a pointer to a position. What a
  component contributes depends on the circuit it is in, and is not read
  off its own response profile. The analogy to the claim (a mode is not a
  perspective apart from the relations among its carriers) is the
  record's.
- **[THEORY-tmpgz1nk](../theory.d/THEORY-tmpgz1nk.md).** Within one model the paper finds reuse of a known
  component type, but it gives no evidence across models; the GPT-2 medium
  look found a different pattern at the name-mover stage.
- **[CLAIM-367](../claims.d/CLAIM-367.md) and [CASE-113](../cases.d/CASE-113.md).** The dropout hypothesis attributes a property
  of the trained network, redundancy that hides components from
  knockouts, to a condition of training. It is a candidate case of a
  network property whose source lies with the training regime, not the
  network. It is untested here ([THEORY-tmpmd4za](../theory.d/THEORY-tmpmd4za.md)).
- **[QUESTION-tmpivbso](../questions.d/QUESTION-tmpivbso.md) and [THEORY-tmpoirdq](../theory.d/THEORY-tmpoirdq.md).** The paper reads one trained
  model. Its circuit, its backups and its completeness test are the
  measurements a developmental study would track over checkpoints, and the
  backups are a warning for any circuit-only description fitted to one
  checkpoint: knockouts at one time reveal heads that ordinary operation
  hides. [THEORY-tmpoirdq](../theory.d/THEORY-tmpoirdq.md)'s circuits before and after fine-tuning use the
  same kind of circuit discovery.
- **Accounts filed.** [THEORY-tmpccb5u](../theory.d/THEORY-tmpccb5u.md) (Active): the circuit and its three
  tests, as measured. [THEORY-tmpmd4za](../theory.d/THEORY-tmpmd4za.md) (Proposed): the dropout hypothesis.

No instruction for machine-learning practice is drawn; the methods are
interpretability practice, the anthology's (`anthology-candidate`).

## Limitations

- **Narrow behaviour.** Fifteen templates, single-token names, one model.
  Backup heads were selected by an arbitrary 2% threshold.
- **MLPs and layer norm left out**, though knocking out all MLPs after the
  first breaks the task, so the circuit is of heads given the MLPs.
- **Missing validations**, as the authors list them: weight-level checks of
  the duplicate-token and induction heads, and how the S-inhibition heads'
  attention arises.
- **Mean ablation over p_ABC** defines what "knocked out" means; another
  reference distribution would define a different circuit function.

### Errors and inconsistencies found

- **"Comparable" faithfulness.** §4.4 says the naive circuit "has a
  faithfulness score of 0.1, comparable to the full circuit C". The full
  circuit's score (§4) is 0.46. Lower is better on this measure, so by it
  the naive circuit is the more faithful of the two.
- **The greedy completeness search.** Algorithm 3 adds at each step the
  node maximizing |F(C \ (K ∪ {v})) − F(C \ K)|, a quantity in the circuit
  alone, which is the minimality score's form. The text says K is "greedily
  optimized … to maximize the incompleteness score", |F(C \ K) − F(M \ K)|,
  which involves the model. As printed, the algorithm does not compute what
  §4.2 says it optimizes.
- **Keys or values.** Appendix C, on the S-inhibition heads' keys, says the
  duplicate token heads "appear to also influence S-Inhibition Heads'
  values". The section's subject suggests keys.
- **Checked and consistent.** The head tally is 26. The template list has
  15 entries. The linear fit gives 2.31 + 0.99 = 3.30 for both signals
  original, 7.3% below the 3.56 baseline, matching the stated 7% mean
  error.

## Open questions

- Would a model trained without dropout show backup name movers?
- What are the token and position signals, as vectors?
- Do the hard-to-interpret greedy sets point to a component class the
  circuit misses, or to interactions of the knockout method?
