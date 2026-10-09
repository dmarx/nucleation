---
number: 648
status: Read
formerly:
- NOTE-tmphi66p
paper: 'LIT-844'
title: 'Quantum-Like Contextuality in Large Language Models'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the arXiv PDF (2412.16806v1, the only version, 23
    pages in the journal's preprint template, text layer extracted):
    abstract, §§1–9, every table and figure caption, and the reference
    list. Propositions 3.3, 3.4 and 7.1 were checked by hand; the CbD
    quantities of §4 were recomputed for the PR-like parametrisation
    (s_odd = 3, so CNT1 = 2 − Δ, and Δ ≥ 2·SF); the sheaf criterion was
    reduced to SF < 1/6 from (3.4) with CF = 1 and |M| = 3. The
    experiments, the regression and the code repository were not rerun
    or inspected. The Royal Society version (Proc. R. Soc. A 481:20240399,
    2025) could not be reached (Cloudflare challenge) and was not read.
    Cited works not read: Vallée et al. 2024 (the corrected inequality),
    Lo et al. 2022, 2023 and 2024.
date: '2026-10-09'
summary: >-
  Builds a three-sentence anaphora schema with the support of the PR
  prism, instantiates it 51,966,480 times from Simple English Wikipedia,
  and takes one referent probability per sentence from BERT: 0.148% of
  the models pass a signalling-corrected sheaf test and 71.1% the CbD
  test. Because the schema fixes the support, both verdicts depend only
  on how uncertain BERT is in the three sentences; the tie to embedding
  distance is a softmax identity with weak correlations.
---

<!-- inactive-ok-file: THEORY-013 — Proposed; cited for what this reading bears on, not as settled -->
<!-- inactive-ok-file: CLAIM-009 CLAIM-037 CLAIM-044 — Proposed; open, and cited as open: the claims this reading bears on -->

# NOTE-648: Quantum-Like Contextuality in Large Language Models

## Contribution

Earlier language tests of contextuality used a few dozen hand-chosen
phrases ([LIT-842](../literature.d/LIT-842.md)) or eleven noun pairs. This paper automates the
construction: a fixed linguistic schema shaped like the minimal
contextual scenario is filled from a corpus, and a masked language model
supplies the probabilities, giving about 52 million models. It reports
many contextual ones under both a signalling-corrected sheaf criterion
and Contextuality-by-Default, and relates the parameter that decides
contextuality to the geometry of BERT's output layer.

## Key insight

What the paper establishes is a property of its schema more than of
language. The sentences "the same one" and "the other one" make the
support of every instance that of the PR prism, which no global
assignment fits. Contextuality is then decided by signalling alone: an
instance counts as contextual when BERT's three referent choices are
close enough to even that the signalling cannot explain away the built-in
parity contradiction.

## Assumptions

- **Scenario**: the 3-cycle, X = {X1, X2, X3} (adjectives as pronoun
  modifiers), contexts {X1,X2}, {X2,X3}, {X3,X1}, outcomes the two nouns
  (§5).
- **Stipulated joints.** In context (i) the probability P1(O1) goes to
  (O1, O1) and P1(O2) to (O2, O2); in (iii) to (O1, O2) and (O2, O1). Only
  one marginal per context is measured, by masking the first referent.
- **Normalisation** over the two candidate nouns (footnote 2).
- **Sheaf criterion** CF > 2|M|·SF, taken from Vallée et al. (2024); the
  paper uses it as the test for signalling models, and does not say
  whether it is necessary as well as sufficient.
- **CbD criterion** for cyclic systems, CNT1 = s_odd(…) − Δ − n + 2 > 0
  (Kujala and Dzhafarov; [LIT-831](../literature.d/LIT-831.md)).
- **Isotropy** of BERT's prediction vectors, for the step from the logit
  difference to the embedding distance (§7a).

## Key results

- **Proposition 3.1–3.2.** The binary 3-cycle is minimally contextual;
  its only strongly contextual model up to relabelling is the PR prism
  (two correlated contexts, one anti-correlated).
- **Proposition 3.3.** Every PR-like model (PR support, any weights) has
  CF = 1. Checked: the only no-signalling model on that support is the PR
  prism itself, which is strongly contextual.
- **Proposition 3.4.** SF = max_i |ε_i|. Checked.
- **Criteria for the schema.** Sheaf-contextual iff SF < 1/6, i.e. every
  P_i(O1) ∈ (5/12, 7/12). CbD-contextual iff Δ < 2 with
  Δ = |ε1 − ε2| + |ε2 − ε3| + |ε3 + ε1|; the paper gives
  2·SF ≤ Δ ≤ 2n·SF (n odd). Reader's check: s_odd = 3 for any PR-like
  model, so CNT1 = 2 − Δ.
- **§6b.** 51,966,480 instances; 77,118 (0.148%) sheaf-contextual and
  36,938,948 (71.1%) CbD-contextual; the sheaf region lies inside the CbD
  region (Fig. 6). The mass concentrates at SF = 1, Δ = 2.
- **§6c.** Top 1% most similar noun pairs (519,660 models): 0.50%
  sheaf-contextual and 81.83% CbD-contextual. Fig. 11: both rates rise
  with the similarity threshold.
- **Proposition 7.1.** ε = tanh((p·Δx + Δb)/2): the softmax over two
  logits. Checked.
- **§7b.** Of nouns' entropy, adjectives' entropy, Euclidean distance and
  bias difference, Euclidean distance correlates best (Kendall,
  Spearman, Pearson 0.06–0.09 on the full data, 0.12–0.20 on similar
  pairs); cubic R² 0.009 and 0.080 at best.
- **§8.** The earlier, hand-chosen 11 pairs gave 350 (3.1%)
  sheaf-contextual and 9,321 (84%) CbD-contextual of 11,052 models.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | BERT's referent probabilities on the PR-anaphora schema yield 77,118 sheaf-contextual and 36,938,948 CbD-contextual models | strong as a count, given the stipulated support and the criteria | §6b, Fig. 5 |
| C2 | These are "experimental evidence" of contextuality in natural language | weak | the joints are stipulated by the schema; only one probability per context comes from BERT; no human data |
| C3 | Contextual instances come from semantically similar nouns, "proved" by an equation | weak | Prop. 7.1 is a softmax identity; the distance link needs isotropy; correlations ≤ 0.2 |
| C4 | Euclidean distance is the best predictor of contextuality among the features tried | moderate (for those four features) | Tables 3–6 |
| C5 | The sheaf and CbD criteria capture "different aspects" of contextuality, their bounds being orthogonal | weak (interpretive) | §8, Fig. 6 |
| C6 | Quantum methods may be advantageous in language tasks | not supported here | abstract and §8; speculation |

## Method

Corpus pipeline (NLTK tokenisation, Penn Treebank tagging, adjacent JJ–NN
pairs) → noun pairs sharing five frequent adjectives → three masked
sentences per instance → bert-base-uncased probabilities for the two
nouns, normalised → PR-like empirical table → SF and Δ in closed form →
correlations and polynomial regressions against four features.

## Concepts

- **PR prism**: the strongly contextual model on the binary 3-cycle with
  perfect correlation on two contexts and anti-correlation on the third.
- **PR-like model**: any model with the PR (prism) support.
- **signalling fraction (SF)**: the least μ with e = (1 − μ)e^NS + μe^S,
  e^NS no-signalling.
- **direct influence (Δ)**: the CbD sum of differences of a content's
  expectation across its two contexts.
- **PR-anaphora schema**: Definition 5.1.

## Connections

It follows [LIT-842](../literature.d/LIT-842.md) (Wang, Sadrzadeh, Abramsky and Cervantes) in testing
language for contextuality, and moves from lexical ambiguity to anaphora.
It uses Abramsky and Brandenburger ([LIT-016](../literature.d/LIT-016.md)), the contextual fraction
([LIT-265](../literature.d/LIT-265.md)) and the signalling-corrected inequality of Vallée et al., and
the CbD cyclic criterion ([LIT-831](../literature.d/LIT-831.md), [LIT-777](../literature.d/LIT-777.md)). Its schema is Specker's
triangle (the "pint/wine/grub" model of [LIT-845](../literature.d/LIT-845.md), Example 8) with
pronouns in place of questions. It treats the Winograd schema as the
nearest benchmark and BERT as the measuring instrument.

## Bearing on the record

- **[THEORY-013](../theory.d/THEORY-013.md)** (behavioural, social and word-meaning data published as
  contextual show none once signalling is separated). [NOTE-645](NOTE-645.md) named
  this paper as the candidate counterexample. It does not meet
  [THEORY-013](../theory.d/THEORY-013.md)'s `promote_when` in either direction. It is not a
  behavioural data set: the probabilities are BERT's, and the authors
  say human judgements remain to be collected (§8). And its CbD verdicts
  are not a finding about context effects in the data. Because the
  schema fixes the support, Δ < 2 holds whenever BERT's three choices are
  uncertain and roughly consistent: if P1 = P2 = P3 = p, then Δ = 2|2p − 1|,
  below 2 for every p strictly between 0 and 1. Seventy-one per cent
  CbD-contextual measures how often BERT is not certain. The sheaf
  verdicts (0.148%) are more demanding but rest on the same stipulated
  support. [THEORY-013](../theory.d/THEORY-013.md) should not be cited as refuted by this paper, and
  its "does not say" list could name it as a non-behavioural case whose
  contextuality is built into the schema. That inference is mine.
- **[CLAIM-009](../claims.d/CLAIM-009.md)** (pragmatic judgements may be formally contextual).
  Anaphora resolution is pragmatic by the paper's own classification
  (§2), so this is nearer to [CLAIM-009](../claims.d/CLAIM-009.md) than [LIT-842](../literature.d/LIT-842.md) was. But the
  judgements are a model's, and the contextuality comes from the
  sentences' "same/other" constraints. It shows that pragmatic
  materials can be built so that any uncertain resolver yields formally
  contextual data. It is not evidence that people's pragmatic judgements
  are contextual.
- **[CLAIM-037](../claims.d/CLAIM-037.md)** (formal contextuality needs CbD when marginals shift).
  Supported: no instance is no-signalling unless all P_i = ½ (§5). It also
  shows how far apart two signalling-aware criteria can be on the same
  data: 0.148% against 71.1%. The defeater [CLAIM-037](../claims.d/CLAIM-037.md) names concerns
  consistently connected systems; these are not, so it is not met.
- **[CLAIM-044](../claims.d/CLAIM-044.md)** (ambiguity admits several global readings, contextuality
  none). This paper is the clean case of "incompatible constraints". Each
  pronoun is ambiguous between two nouns, and that ambiguity alone is
  not contextual. The contextuality comes from the odd number of
  "other" constraints around the cycle, as in the parity case [CASE-035](../cases.d/CASE-035.md).
  Here "a contextual one admits none" holds, since the PR prism is strongly
  contextual.
- **Not the transport problem.** Nothing here maps one scenario to
  another; [CLAIM-100](../claims.d/CLAIM-100.md) is untouched.
- **For the anthology.** §7 relates the contextuality parameter to BERT's
  output geometry (logit difference, embedding distance), which the
  anthology's concept-geometry topic could hold; hence the flag. No
  instruction for machine-learning practice.

## Limitations

- Joint distributions are stipulated by the schema, not observed; only
  one marginal per context comes from BERT.
- The probabilities come from one masked language model, normalised over
  two candidates; no human judgements.
- The sheaf criterion is taken from Vallée et al. without discussion of
  whether it is a sufficient test only; the paper calls it "the"
  criterion.
- Instances are often unnatural (noun pairs that never co-occur; the
  authors call the schema "grammatical but unnatural").
- The geometric account assumes isotropic prediction vectors; the
  correlations are weak.
- Numerical and labelling inconsistencies: 0.0148% (§6c) against 0.148%
  (§6b, Fig. 5); "Table 2" for Table 1; correlation targets unclear.
- The journal version was not read and may differ from the preprint.

## Open questions

- The same schema with human judgements, where the joint distribution
  could be elicited rather than stipulated.
- A schema whose support is measured, not fixed by "same/other", so that
  contextuality would be a finding about the resolver.
- Whether the sheaf test of Vallée et al. is necessary as well as
  sufficient for signalling models, which decides whether 0.148% is a
  lower bound.
