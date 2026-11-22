<!-- scratch/studies/lead-146/preregistration-draft.md: the draft preregistration LEAD-146 asks for -->
# Draft preregistration of the discriminating fidelity study (CASE-055)

Drafted on 2026-11-22 for LEAD-146 by the assistant (Claude, in this
session). **Nothing here is fixed.** CASE-055 says every margin, power and
rate "is to be fixed in its preregistration, by the owner". Each choice that
is the owner's is marked **[OWNER n]** with its alternatives and the draft's
lean; §11 lists them. Numbers marked *assumed* are guesses to be replaced by
a pilot; numbers marked *computed* come from `power.py` (`results.json`).

## 1. What the study tests

One study, CASE-055, with an intralingual arm (English source, English
retellings) and an interlingual arm (English source, renderings in one
target language). Each hypothesis is stated as the defeat condition of the
claim it tests, on one effect: the **held-out increment in R²** (Δ) that one
predictor set adds over another in predicting receivers' recovery per
rendering, cross-validated with folds grouped by source item.

- **H1, CLAIM-220.** Pragmatic observables (P) against the propositional
  rivals: Δ = R²(P) − max(R²(Q1), R²(Q2)), where Q1 is human-rated
  propositional sameness and Q2 sameness of proposition and illocutionary
  type. Defeated if Δ is shown smaller than the margin, in either arm
  ("or this holds in the study's interlingual arm").
- **H2, CLAIM-202 as worded.** On arm (c) renderings, the transport
  measures (T: CLAIM-228, CLAIM-231, CLAIM-259) over the static profile
  (S): Δ = R²(S+T) − R²(S).
- **H2′, CLAIM-202 restated against the strong contextual baseline.**
  CLAIM-205 (Active) holds that the rival accounts need not fix one
  context, so a win over S would not tell the line from them; CLAIM-205
  asks for "the incremental thesis restated against a strong contextual
  baseline, specified in advance". Δ = R²(C+T) − R²(C), where C is the
  baseline of §3. H2′ is the test that answers CLAIM-205; H2 is kept
  because CLAIM-202's defeat condition names it. **[OWNER 1]** whether H2′
  replaces H2 as the confirmatory test of CLAIM-202 (lean: both
  confirmatory, H2′ decisive for what the line adds; restating CLAIM-202's
  `defeated_if` is the owner's, and this draft does not do it).
- **H4, QUESTION-074 (optional).** Prediction under an unobserved
  composition: T and C fitted on renderings under transformations A and B
  separately, scored on renderings under A then B. **[OWNER 2]**
  confirmatory, exploratory, or left out (lean: exploratory in this study;
  no power is computed for it, and it needs transformations shown to meet
  CLAIM-260's conditions, which no entry yet does).

CLAIM-204's three findings use "an equivalence margin and a power fixed
before its data" in the same design; the margin fixed here would serve them
too, but their tests (relational profiles, transfer across languages) are
not drafted here.

## 2. Gate: Stage 0 (LEAD-162)

No fidelity test is run until Stage 0 passes: the definition given to judges,
reliability between judges and between passes against a target fixed in
advance, and known-groups validity on reattributed sentences. Choosing the
coefficient and target is LEAD-162's, which needs a reading the record does
not hold (QUESTION-076). This draft's power calculation assumes each
human-rated predictor has reliability 0.80 and shows what 0.60 costs (§9).
If Stage 0 fails, the outcome is a negative answer to QUESTION-076, and the
theses are left untested, not defeated (CASE-055's note of 2026-10-10).

## 3. Predictor sets, the baseline among them

All human-rated predictors are rated by raters other than those who supply
the criterion (CASE-055). Every set is fitted inside the training folds
only.

| Set | What it is |
|---|---|
| Q0 text | embedding similarity (one fixed multilingual encoder, named before data) and surface similarity (chrF against the source or a back-translation in the interlingual arm) |
| Q1 proposition | human-rated propositional sameness |
| Q2 proposition and force | Q1 plus human-rated sameness of illocutionary type |
| P pragmatic observables | ratings of stance, footing, alignment and expected uptake, each as distance from the source's, combined with weights fixed before data |
| S static profile | P's stance and footing ratings in one stated default context |
| C **strong contextual baseline** | see below |
| T transport | CLAIM-228's observational distortion over the item's class, CLAIM-231's order effects of sequence contexts, CLAIM-259's directed decision term |

**The strong contextual baseline C.** CLAIM-504 (Proposed) names its kind,
"rich context-response profiles and supervised prediction", and its note of
2026-10-30 says it "is not specified beyond the reading's table". This
draft specifies it, so that the increment measures what the transport
**structure** adds, not what extra **data** add:

1. **Same inputs as T.** The context-response profile: for each rendering
   and its source, the raters' stance, footing and act-probability ratings
   in each of the K stated contexts that T is computed from (K = 6
   *assumed*: three preceding framings of the relationship, three later
   framings), and the differences between rendering and source. T is a set
   of fixed functionals of this same matrix; C sees the whole matrix
   unstructured.
2. **A flexible learner on it.** Ridge regression on the full profile, its
   penalty tuned by nested cross-validation within training folds; and a
   gradient-boosted tree model on the same features; C's prediction is
   the better of the two in the inner folds.
3. **A supervised text model.** A classifier fine-tuned, inside training
   folds only, to predict the receivers' act choices from the text of
   source and rendering (and the context text), its predicted recovery
   entered as a feature.

**[OWNER 3]** the baseline's extent. (a) items 1–3, as above (lean: the
strongest rival the draft can specify, which is what CLAIM-205 asks for);
(b) items 1–2 only, so that C and T see exactly the same information and the
increment is purely structural; (c) items 1 and 3 with a linear learner
only, cheaper and less prone to overfitting at this n. Whatever is chosen,
CLAIM-504's open part, whether this is the *strongest* operationalization
the rivals license, stays open: a pass over C shows that T adds over this
baseline, not over every one.

**[OWNER 4]** P's weights: unit weights on the four standardized distances
(lean: no estimation, nothing to overfit), or weights fitted in a pilot and
frozen.

## 4. Criterion: recovery

Receivers read a rendering (target receivers) or a source (source
receivers) and make two choices under stated tasks: which of a stated set of
acts it performs (teasing, reproach, reprimand, a neutral remark, other),
and which of four offered continuations fits. The source receivers' answers
on each source item give its act distribution and its modal act.

Per rendering, recovery y = the share of its J receivers whose chosen act is
the source's modal act, averaged with equal weights (fixed now) with the
share whose continuation is the source receivers' modal continuation.

**[OWNER 5]** the scoring rule: (a) modal match, as above (lean: simple, and
what the power calculation simulates); (b) proper-score credit, each choice
scored by the source distribution's probability of it, which uses the
source's split instead of discarding it (CLAIM-226's point that
disagreement is signal); (c) act and continuation as two co-primary
outcomes with Holm's correction, in place of the average.

Items whose source modal act has less than half the source receivers' votes
are dropped from the primary analysis and kept for (b) as a secondary.

Holistic fidelity ratings are collected as a secondary outcome, for
CLAIM-240 (CASE-055).

## 5. Populations and sampling frames (CLAIM-226)

Every inference is scoped to the frame named, not to "readers of English" or
"readers of German".

- **Source receivers.** Adults (18+) who report English as their first
  language and who live in one named country, recruited through one named
  online research panel, with quotas on age band (18–34, 35–54, 55+) and
  gender matching the country's census margins; education recorded. The
  frame is the panel's eligible registrants in that country.
  **[OWNER 6]** country: (a) United Kingdom (lean: one national variety of
  address norms, and T/V-like distinctions are not at issue on the English
  side); (b) United States; (c) both, as two populations with a population
  term.
- **Target receivers.** Adults who report the target language as their
  first language, living in the target language's main country (Germany,
  France or Japan by §6), same panel or an equivalent named one, same quotas;
  people who report fluent English are kept and the self-report recorded
  as a covariate, since excluding them would bias the frame toward older
  receivers.
- **Predictor raters.** A separate pool, trained on Stage 0's definition:
  students or graduates in linguistics or translation, named by
  institution or panel, native in the language they rate; none supplies
  the criterion.
- **Bilingual check.** **[OWNER 7]** whether to add a third population of
  English–target bilinguals who judge both source and renderings, the
  design CLAIM-226 offers for separating population from transport (lean:
  yes, as a secondary arm of about 200 receivers; it is a different
  receiver, CLAIM-226 says, so it does not replace the target population).
- **Population against transport.** Anchor items whose act is fixed by
  convention (a formal apology, a greeting to a superior, a thanks, a
  refusal), about 20, each in a conventional translation, judged by both
  populations. A multi-group model tests invariance on them; the
  population offset estimated on anchors enters the interlingual model as a
  fixed term, so that a population difference is not read as distortion by
  transport. If fewer than three quarters of anchors are invariant at the
  preregistered tolerance, the interlingual arm reports population
  differences only and its defeat tests are not run.
- **Historical sources** (Villon, Henley, Marot) are not in this draft's
  primary analysis; CASE-055's separate arm, scoped to a stated modern
  reading, keeps its own preregistration.

**Exclusions**, fixed now: failing either of two attention checks; finishing
in less than a third of the median time; failing a first-language check
item; more than 10% missing answers. *Assumed* exclusion rate 10%, so
recruitment is 1.11 × the analysed number.

## 6. The language pair (CLAIM-222)

CLAIM-222 asks for "at least one language pair in which footing or
politeness is grammatically marked on one side only, with judges on both
sides". CASE-055 names French or German (T/V obligatory) and Japanese
(honorific marking obligatory), and the lead asks for one pair.
**[OWNER 8]**:

- **(a) English → German** (du/Sie, marked in the pronoun, the verb's
  agreement and the imperative). Large panels and translator pools;
  address norms close enough to English that anchor invariance is likely to
  hold, so the result is likely to be interpretable. Forced only in
  utterances with second-person address, so every interlingual item must
  address its hearer; teasing, reproach and reprimand mostly do.
- **(b) English → French** (tu/vous). The same profile as (a); the choice
  between (a) and (b) is one of panels and translators, not of theory.
- **(c) English → Japanese** (plain and polite predicate forms and
  honorifics). Marking is forced on every finite predicate, not only in
  address, so the forced choice is stronger and needs no item filter. The
  communities differ more, so anchor invariance is more likely to fail, and
  a failure leaves the interlingual defeat tests unrun (§5); recruitment
  and translation cost more.

Lean: (a) as the principal pair, because the study's value depends on the
invariance test passing; (c) as a second pair if budget allows, since
CLAIM-222's question is sharper there.

Renderings in the interlingual arm are by professional translators, each
under one stated brief **[OWNER 9]**: (a) one brief for all, "an
instrumental translation for adult readers of the target language" (lean:
Nord's instrumental type, LIT-1863, so the brief is held constant); (b)
two briefs, instrumental and documentary, crossed with items, which tests
Nord's distinction at twice the cost.

## 7. Materials and the rates assumed

Per source item, the renderings of CASE-055's arms: (a) proposition kept,
footing changed; (b) proposition changed, footing kept; (c) static profile
matched, response to later framings different; (d) a professional
translation; and, in the intralingual arm, English retellings.

| Rate | Value | Status | Consequence |
|---|---|---|---|
| mean recovery across renderings | 0.65 | *assumed* | near 0.5 maximizes criterion variance; near ceiling (0.9) loses power |
| SD of recovery on the logit scale | 1.2 | *assumed* | sets how much renderings differ |
| item share of latent variance | 0.10 | *assumed* | items are the resampling unit |
| variance the baseline explains | 0.30 | *assumed* | higher leaves less for any increment |
| source items whose modal act has a majority | 0.75 | *assumed* | build 1.33 × the analysed items |
| arm (c) renderings that pass the static-match check | 0.50 | *assumed* | write two for each one kept |
| target acts among screened natural utterances | 0.05–0.10 | *assumed*; pilot | screen 10–20 utterances per one kept |
| natural target-act utterances with second-person address | 0.8 | *assumed*; pilot | only addressed ones enter the German or French arm |
| receivers excluded | 0.10 | *assumed* | recruit 1.11 × |
| anchors invariant | ≥ 0.75 required | rule | below it, §5 |

The source mix **[OWNER 10]**: (a) half CASE-040's written topic × act cells,
half natural utterances drawn by a stated rule (lean: CASE-055 names both,
and the natural half guards against items written to suit the theory); (b)
written cells only, cheaper, with the natural utterances as a later study.

The pilot (about 20 items, 200 receivers) fixes the *assumed* rows before
the main study's sample size is frozen; the decision rules and margins in
§8–9 are fixed before the pilot and do not change after it.

## 8. Analysis and decision rules

- **Model.** For each predictor set, an outcome model of y on the set's
  features, fitted in training folds; five folds grouped by source item, so
  every scored rendering belongs to an item no fit has seen. **[OWNER 11]**
  the held-out unit: (a) source items (lean: the stricter test, and the
  one a generalization claim needs); (b) renderings, with an item's other
  renderings in training, which the wording "held-out renderings" also
  allows and which is easier to pass. Judge and group random effects enter
  the confirmatory refit of the receiver-level model (CASE-055); the
  held-out Δ is computed from rendering-level predictions.
- **Interval.** A 90% percentile interval for Δ from a cluster bootstrap
  over items (2,000 resamples), so each one-sided test is at α = 0.05.
- **Decision.** With margin δ:
  - **defeated** if the interval's upper bound is below δ ("adds less than
    a margin fixed in advance", CLAIM-202; "within an equivalence margin",
    CLAIM-220);
  - **supported** if its lower bound is above δ;
  - **inconclusive** otherwise, reported as such, with the interval.

  **[OWNER 12]** the support rule: (a) lower bound above δ, as above (lean:
  symmetric with the defeat rule, so neither verdict is easier to reach by
  the rule's choice); (b) lower bound above 0, which declares support for
  increments the margin calls negligible; under (b) an interval wholly
  between 0 and δ meets both rules, and the draft would rank defeat first.
- **Multiplicity.** Each hypothesis tests a different claim, with its own
  defeat condition; no correction across them. Within CLAIM-220 the two
  arms are a disjunction of defeat, so each is tested at α = 0.05 and either
  suffices.
- **Order.** Stage 0, then the anchor invariance test, then H1, H2 and H2′
  in each arm, then the secondary outcomes.

## 9. The margin, and the power behind it

**Scale.** δ is stated on the observed held-out R² of y with J = 30
receivers per rendering (computed criterion reliability 0.88; 0.79 at
J = 15). **[OWNER 13]** the scale: (a) observed, with J fixed now (lean:
nothing estimated enters the test); (b) disattenuated by the criterion's
split-half reliability, which makes δ independent of J but adds an
estimated quantity to the test.

**Computed power** (`power.py`, 400 runs a cell; R = 6 renderings an item in
the analysis set; six baseline and three transport features; reliabilities
0.80). "Defeat" is the probability of the defeat verdict when the true
increment is 0; "support" the probability of the support verdict when the
true observed increment is about 2δ.

| δ | items (renderings) | defeat at Δ = 0 | support at Δ ≈ 2δ |
|---|---|---|---|
| 0.05 | 80 (480) | 1.00 | 0.68 |
| 0.05 | 120 (720) | 1.00 | 0.86 |
| 0.05 | 160 (960) | 1.00 | 0.95 |
| 0.05 | 240 (1,440) | 1.00 | 0.99 |
| 0.02 | 160 (960) | 1.00 | 0.49 |
| 0.02 | 240 (1,440) | 1.00 | 0.72 |
| 0.02 | 320 (1,920) | 1.00 | 0.87 |
| 0.02 | 400 (2,400) | 1.00 | 0.93 |
| 0.02 | 480 (2,880) | 1.00 | 0.97 |
| 0.01 | 320 (1,920) | 1.00 | 0.50 |

**Size check** (*computed*): the probability of the defeat verdict when the
true increment equals the margin, nominally 0.05.

| δ | 80 items | 160 items | 240 items | 320 items |
|---|---|---|---|---|
| 0.05 | 0.12 | 0.09 | 0.065 | 0.06 |
| 0.02 | 0.18 | 0.135 | 0.11 | 0.09 |
| 0.01 | 0.22 | 0.16 | 0.13 | 0.11 |

Two things the tables show. First, the binding constraint is power to
**support**, not to defeat: the held-out increment of added features is
biased downward at small n, since the extra features cost fitted
parameters, so a null increment is easily shown smaller than δ. Second,
the same bias makes the defeat rule too liberal at the margin: a thesis
whose true increment is exactly δ is defeated 9% of the time at the lean
(δ = 0.05, 160 items), not 5%, and more often at smaller margins.
**[OWNER 17]** (a) accept it and report it (the error is on the side of
defeating the record's own thesis, which is the cautious side for a
thesis); (b) test defeat with a 95% interval, which the simulation has not
yet checked; (c) 240 items at δ = 0.05, where the size is 0.065; (d)
correct the estimate for its bias, by the simulated bias at the realized
n, which puts a modelled quantity into the test. Lean: (a) with (c) if
budget allows.

Sensitivity at δ = 0.02 and 240 items: J = 15 receivers drops support power
from 0.72 to 0.52; predictor reliability 0.60 drops it to 0.50; three
renderings an item (720 renderings) drops it to 0.39. Receivers, Stage 0
reliability and renderings per item each matter about as much as items.

**[OWNER 14] the margin.**

- **(a) δ = 0.05** (lean). 160 analysed items an arm gives power 0.95 to
  support an increment of about 0.10 and certainty to defeat a null one.
  Justification: feasibility, said plainly. It is the smallest of the
  three margins the study resolves at a size one lab could run (§10). Under
  it, an increment below 5% of the criterion's variance on held-out items
  counts as no increment, and the thesis as worded, "adds", would be
  defeated for this frame and pair. Whether 5% is small enough to matter is
  a substantive judgement the record has no reading for, and is the
  owner's.
- **(b) δ = 0.02.** Close to the conventional "small" increment in
  regression (Cohen's f² of 0.02, cited from convention, not from a
  reading the record holds); 400 analysed items an arm give support power
  0.93, so 2.5 times (a)'s cost. Choose it if the claim is meant to survive
  small real increments.
- **(c) δ = 0.01.** Not reachable at these assumptions: 320 items give
  support power 0.50. Not recommended.
- One margin for all hypotheses (lean), or a wider one for H1, whose rivals
  are weaker and whose increment should be larger: **[OWNER 15]**.

The calculation does not cover H4, the receiver-level mixed model, or a
baseline C that overfits more than a six-feature linear model; a C with
many features (option 3a) will lose more to overfitting in the training
folds, which makes T's increment over it easier to support, not harder, so
the table is conservative for H2′ only if C is no weaker than modelled.

## 10. Size and cost at the lean

At δ = 0.05, per language arm: 160 analysed items → 214 built (majority
rule) → for the German or French arm, natural items screened for address.
Renderings: arms (a), (b), (d) one each, arm (c) two kept (four written),
retelling one: six analysed an item, 960 an arm. H2 uses arm (c) only, so it
has 320 renderings at this size; **[OWNER 16]** (a) raise arm (c) to six kept
an item (twelve written), so H2 has the power of the table (lean: H2's
analysis set is the one CLAIM-202's wording names); (b) run H2 on all
renderings with S as covariate, which departs from that wording; (c) accept
H2 underpowered and let H2′ carry the decision.

Receivers: 960 renderings × 30 receivers ÷ 40 renderings a receiver = 720
analysed target receivers an arm (800 recruited), and about 160 source
receivers for 214 items. Raters for predictors: K = 6 contexts × renderings
× stance, footing and act ratings, by at least three raters each; the
largest cost after receivers.

## 11. The owner's decisions

1. H2′ beside H2, and whether to restate CLAIM-202's defeat condition.
2. H4 confirmatory, exploratory or out.
3. The baseline C's extent: (a) profile, learner and text model; (b) profile
   and learner; (c) linear only.
4. P's weights: unit, or pilot-fitted and frozen.
5. The scoring rule: modal match, proper-score credit, or co-primary.
6. The source country: UK, US, or both.
7. A bilingual population, as a secondary arm.
8. The language pair: English → German, → French, or → Japanese.
9. The translators' brief: one instrumental brief, or two briefs crossed.
10. The source mix: half natural, or written only.
11. The held-out unit: items or renderings.
12. The support rule: lower bound above δ, or above 0.
13. The margin's scale: observed with J fixed, or disattenuated.
14. The margin: 0.05, 0.02 or 0.01.
15. One margin for all hypotheses, or a wider one for H1.
16. Arm (c)'s size for H2.
17. The defeat rule's excess size at the margin: accept, a 95% interval,
    more items, or a bias correction.

The leans, together, give a study of 214 built items an arm, about 960
analysed renderings and 800 recruited target receivers an arm, at
δ = 0.05.

The wording is the assistant's (Claude, in this session); adopting it is
the owner's call.
