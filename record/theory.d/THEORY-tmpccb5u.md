---
status: Active
title: 'In GPT-2 small on fifteen templates of indirect object identification, a circuit of 26 attention heads in seven classes, found by path patching, keeps 87% of the model''s mean logit difference when every other head is mean-ablated; knocking out its three main name mover heads costs only 5%, because other heads take over, and knockout sets found by greedy search make the circuit and the full model differ by up to 87% of the logit difference, so the circuit is faithful on average and incomplete under knockouts'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Active from NOTE-tmp1iis8, the reading of Wang et al. (2022) in
    full. One study, but the title claims no more than it measured, its
    design is interventional throughout, and nothing in the record
    contradicts it (ADR-047 v3); Makelov et al.'s finding of a faithful
    S-inhibition → name mover direction (LIT-968) agrees with one link of
    it. The dropout explanation of the backups is the Proposed
    THEORY-tmpmd4za.
tags:
- representation-learning
- causality
date: '2026-10-26'
source:
- LIT-tmpj9tel
summary: >-
  Wang et al. (2022), [LIT-tmpj9tel](../literature.d/LIT-tmpj9tel.md), read in [NOTE-tmp1iis8](../notes.d/NOTE-tmp1iis8.md): §§3–4 and the
  appendices. The circuit implements "identify the names, remove the
  duplicated one, output the rest" through duplicate-token, induction and
  previous-token heads, S-inhibition heads and name movers, with negative
  and backup name movers. The faithfulness, completeness and minimality
  tests are the paper's own. It says nothing beyond these templates and
  this model, it treats MLPs as given, and its greedy search is printed in
  a form that does not match its description.
---
<!-- inactive-ok-file: THEORY-tmpmd4za — Proposed; the hypothesis for the backups, cited as open -->

# THEORY-tmpccb5u: In GPT-2 small on fifteen templates of indirect object identification, a circuit of 26 attention heads in seven classes, found by path patching, keeps 87% of the model's mean logit difference when every other head is mean-ablated; knocking out its three main name mover heads costs only 5%, because other heads take over, and knockout sets found by greedy search make the circuit and the full model differ by up to 87% of the logit difference, so the circuit is faithful on average and incomplete under knockouts

## Source

Wang, Variengien, Conmy, Shlegeris and Steinhardt (2022), arXiv:2211.00593,
[LIT-tmpj9tel](../literature.d/LIT-tmpj9tel.md), read in full in [NOTE-tmp1iis8](../notes.d/NOTE-tmp1iis8.md).

## What was actually shown

**The task and model.** GPT-2 small (12 × 12 heads). Sentences from fifteen
templates with random single-token names; the model's mean logit
difference between IO and S is 3.56 over 100,000 samples.

**Finding the circuit.** Starting from the logits and working back, path
patching from p_ABC (three unrelated names) identifies at each step the
heads whose direct paths to the previously found heads' queries, keys or
values carry the logit difference. Each class is then characterized by
attention patterns, OV copy scores and counterfactual datasets. The
result: name movers (3), negative name movers (2), S-inhibition heads (4),
induction heads (4, two fuzzy), duplicate-token heads (3, one fuzzy),
previous-token heads (2) and backup name movers (8).

**Faithfulness.** F(C), the mean logit difference with every head outside
C mean-ablated (over p_ABC, per template), is within 0.46 of F(M) = 3.56:
87%.

**Redundancy.** With the three name movers knocked out, the logit
difference falls by only 5%; path patching after the knockout finds heads
that now write the answer, from which the eight backups were taken.

**Completeness.** |F(C \ K) − F(M \ K)| stays small when K is random or a
whole class, but reaches 3.09, 87% of F(M), for sets found greedily.

**Minimality.** Every head has a K for which removing it changes F by at
least 1% of F(M).

**What could have come out otherwise.** Path patching could have found the
effect spread thinly over many heads; the circuit could have kept far less
than 87%; the name movers' knockout could have destroyed the behaviour;
and every completeness test could have passed. The last would have been a
weaker paper.

## What this does not say

- **Not beyond the templates or the model.** A preliminary look at GPT-2
  medium finds a different name-mover stage.
- **Not a circuit of the whole computation.** MLPs, layer norms and
  embeddings are not nodes; knocking out all MLPs after the first breaks
  the task (logit difference −1.1).
- **Not complete.** The paper's own search finds knockouts it does not
  explain.
- **Not independent of the ablation.** "Knocked out" means replaced by the
  per-template mean over p_ABC; another reference distribution defines
  another circuit function.
- **Not why the backups exist.** That is [THEORY-tmpmd4za](THEORY-tmpmd4za.md).

## Connections

- **[THEORY-282](THEORY-282.md), [LIT-968](../literature.d/LIT-968.md).** Makelov et al. find a faithful residual-stream
  direction after layer 8 written only by the S-inhibition heads, and an
  illusory one in MLP8, in this task and model.
- **[THEORY-tmp4lqc8](THEORY-tmp4lqc8.md).** MIB's IOI variables sit on the S-inhibition heads
  named here.
- **[THEORY-tmpb4xka](THEORY-tmpb4xka.md).** The previous-token → induction K-composition first
  read in a two-layer toy reappears here, with the induction heads'
  output used as a position pointer.
