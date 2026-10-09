---
status: Read
paper: LIT-tmpcsywp
title: 'That''s what she (could have) said'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the eScholarship copy of the proceedings paper
    (repositories.cdlib.org/content/qt5f03m09d/qt5f03m09d.pdf, a cover
    page and pages 120–125): abstract, introduction, "Specificity
    Implicatures" with Eqs. 1–5, Experiment 1 with Fig. 2, "Horn's
    Principle" with Eqs. 6–8, Experiment 2 with Fig. 3 and Table 1,
    Discussion and references. The two-column extraction interleaved the
    columns; the text was put back in order by hand. The three-meaning
    model predictions were known from Fig. 3's legend, not recomputed.
    The two-lexicon argument for Horn's principle was followed step by
    step.
date: '2026-10-09'
summary: >-
  Recursive Bayesian speaker–listener reasoning yields specificity
  implicatures but cannot derive Horn's principle from utterance costs
  alone; letting the agents be uncertain about the lexicon breaks the
  symmetry, so costlier signals go to less likely meanings in one-shot
  games without equilibrium refinements, and two online games with novel
  symbols show people drawing both implicatures without prior conventions.
---
<!-- inactive-ok-file: THEORY-tmprknoj — Proposed; open, and cited as open: the claim, argument or reading is under test, not settled -->
<!-- inactive-ok-file: LIT-473 — Deferred; filed, not read, and cited only as the source of the signalling-game framing -->

# NOTE-tmp9okql: That's what she (could have) said

## Contribution

Horn's division of pragmatic labour, that marked or costlier forms carry
less probable meanings, had resisted derivation: in a signalling game
where two signals differ only in cost, the efficient and the inefficient
assignment are both equilibria, and game-theoretic pragmatics needed a
selection rule or an evolutionary story to pick one. This paper derives
it in one shot from recursive cooperative reasoning, by adding
uncertainty about what the signals literally mean. It also shows, with
novel symbols and no conventions, that people draw both specificity and
Horn implicatures.

## Key insight

A costly signal is worth paying for only to a speaker whose meaning would
otherwise be misread. If the listener allows that the signal might mean
anything, the only speaker with a reason to pay is one who means the
unlikely thing, and that asymmetry, once in the listener's model, is
amplified by each level of reasoning.

## Assumptions

- **Common knowledge of communicative goals** (Lewis 1969; Clark 1996);
  the speaker wants to convey a specific meaning, the listener to recover
  it.
- **Literal listener** L₀(m|u, L) ∝ L_u(m)P(m), with L_u a truth function;
  a signal with no conventional or iconic meaning is all-true in the base
  model.
- **Softmax speaker** with gain λ > 0 and utility log L_{n−1}(m|u) − c(u).
- **Lexical uncertainty model**: the prior over lexicons is uniform over
  all lexicons in which every utterance is true of at least one meaning
  and every meaning has at least one true utterance (seven in the 2 × 2
  case).
- **The set of alternative utterances is fixed and known** to both.

## Key results

- **Eqs. 2–5 (base model).** S_n(u|m) ∝ exp(λU_n(u|m)), U_n(u|m) =
  log L_{n−1}(m|u) − c(u), L_n(m|u) ∝ P(m)S_{n−1}(u|m). Eq. 4 is printed as
  S_n ∝ (L_{n−1}(m|u) e^{c(u)})^λ; from Eq. 3 the exponent should be
  e^{−c(u)}, a sign slip in the printed paper.
- **Specificity implicature.** Meanings pyramid and cube, utterances
  "pyramid" and "shape", equal costs: S₁ prefers "pyramid" for pyramid
  and must say "shape" for cube, so L₂ reads "shape" as cube; with depth
  both tend to probability 1, for λ > 1 and P(m) > 0 (Fig. 2).
- **Failure on costs.** With two all-true signals of different cost, L₀
  reads both as the prior and no level breaks the symmetry.
- **Eqs. 6–8 (lexical uncertainty).** S_n(u|m, L) ∝ exp(λU_n(u|m, L));
  L_n(m|u) ∝ Σ_L P(m)P(L)S_{n−1}(u|m, L); U₁ uses L₀(m|u, L), U_n for n > 1
  uses the marginal L_{n−1}(m|u). The model reduces to the base model when
  one lexicon is fixed, so specificity implicature survives; and it
  derives the efficient Horn mapping, for two meanings and for three
  (Fig. 3, averaged over a parameter grid).
- **Experiment 1.** 40 participants, five rounds each, random partners,
  $0.06 per success. Listeners read the alien symbol as the unnamed
  object on every trial; speakers chose it for the unnamed object on every
  trial and chose the name for the named object on all but two.
- **Experiment 2.** 140 participants; objects at 60/30/10%; messages free,
  $0.01, $0.02; frequencies and costs randomized between subjects. All six
  efficient-mapping comparisons hold in mixed logit regressions (t from
  5.31 to 8.27, p < .001). By-subject ANOVAs find no first-round main
  effect or interaction for five of six response types; the
  intermediate-cost message shows a small first-round interaction
  (p < .05).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Basic recursive reasoning yields specificity implicatures, converging with depth | strong (derivation) | the two-meaning argument and Fig. 2 |
| C2 | Basic recursive reasoning cannot derive Horn's principle from costs | strong (derivation) | the symmetry argument |
| C3 | Lexical uncertainty derives the efficient Horn mapping in one-shot games without equilibrium refinements | moderate | two-lexicon argument; three-meaning case by simulation over a parameter grid |
| C4 | It is the first such derivation | weak | the authors' survey of van Rooij and Franke |
| C5 | People draw specificity implicatures among novel signals without conventions | moderate | Experiment 1, ceiling behaviour, 40 participants |
| C6 | People coordinate on Horn's mapping in one shot, by reasoning rather than learning | moderate | Experiment 2 regressions; first-round analysis, one exception; five rounds per participant, with feedback after each |

## Method

Model predictions are computed by recursion to a chosen depth; for three
meanings they are averaged over a fine grid of λ and depth. The games are
web interfaces in which a speaker sees an object and clicks one of the
messages; the listener clicks an object; both learn whether they
succeeded. Ten practice rounds without partner or feedback precede five
scored rounds with re-randomized partners.

## Concepts

- **specificity implicature**: strengthening a less specific utterance to
  the negation of a more specific available one, with or without a
  canonical scale (the authors' term, for scalar implicature generalized).
- **Horn implicature / Horn's principle**: costlier forms are associated
  with less probable meanings (Horn's Q- and R-principles).
- **lexicon**: a map from utterances to truth functions on meanings.
- **lexical uncertainty**: the listener and speaker reason over a
  distribution of lexicons rather than one.

## Connections

The base model is "very similar" to Jäger and Ebert's iterated best
response; the informativeness utility is credited to Frank, Goodman, Lai
and Tenenbaum (2009, CogSci), not to the Psychological Science paper of
the same year ([LIT-tmpgto9c](../literature.d/LIT-tmpgto9c.md)). The equilibrium-selection problem is Cho
and Kreps's and Chen, Kartik and Sobel's; evolutionary or hybrid
derivations of Horn's principle are van Rooij's and Franke's. Goodman and
Frank ([LIT-tmphavsf](../literature.d/LIT-tmphavsf.md)) cite this paper for cost sensitivity, and its
lexical-uncertainty model is the ancestor of the uRSA lexical-uncertainty
treatment of embedded implicature they describe.

## Bearing on the record

- **Produces, with [LIT-tmpkwn2g](../literature.d/LIT-tmpkwn2g.md) and [LIT-tmphavsf](../literature.d/LIT-tmphavsf.md), [THEORY-tmprknoj](../theory.d/THEORY-tmprknoj.md).** Its
  specific contribution there is that interpretation depends on the
  alternatives and their costs, not only on the uttered form, and that
  this holds for signals with no prior meaning.
- **On meaning by contrast.** In Experiment 1 the alien symbol acquires a
  meaning only through its contrast with the iconic alternative. That is
  an experimental case of a sign's interpretation being fixed by what
  else could have been said; it is not a case of meaning without
  reference, since the contrast works only because one alternative is
  iconically tied to an object.
- **On [LIT-473](../literature.d/LIT-473.md).** The paper assumes Lewis's common knowledge but argues
  that its two conventions need no precedent; [LIT-473](../literature.d/LIT-473.md) is unread, so the
  record cannot yet say whether that departs from Lewis's account.
- No instruction for machine-learning practice; nothing for the
  anthology.

## Limitations

- Proceedings paper, six pages; the three-meaning predictions are shown
  but not analysed.
- Experiment 1 is at ceiling with 40 participants and one design; it
  cannot distinguish models that all predict the same mapping, and the
  displayed predictions are said to be insensitive to parameters.
- Experiment 2's players get feedback after every round, so learning
  within five rounds is possible; the first-round analysis tests for it
  with null results in five of six cases, not a direct one-shot test.
- Costs are money, made explicit; whether the same reasoning governs
  costs that are length, effort or frequency is not tested.
- The lexicon prior is uniform over a hand-specified set.

## Open questions

- Does lexical uncertainty predict Horn mappings when costs are implicit
  and graded, as in natural language?
- How sensitive is the derived mapping to the lexicon prior, beyond the
  uniform one used?
- A strictly single-trial version of Experiment 2 would separate
  reasoning from fast learning.
