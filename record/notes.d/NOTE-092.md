---
number: 92
status: Read
formerly:
- NOTE-tmp1cbty
paper: LIT-132
title: 'Quillien — Luck and intentional action'
version: 2
history:
- version: 2
  date: '2026-09-26'
  note: >-
    Read in full (Full text of the article, read in full: abstract;
    Introduction (Our Proposal; Causation and Counterfactuals; Explaining
    Intuitions About Luck and Intentional Action; Other Recent Accounts;
    Overview of Empirical Tests); Studies 1–3 (Methods, Participants,
    Results, Discussion); the item-level correlations; General Discussion;
    Conclusion; notes 1–20; the reference list. Source: the open-access (CC
    BY) PMC HTML (PMC13327788), fetched with curl into
    scratchpad/rawA/quillien_pmc.html and converted to rawA/quillien.txt.
    The PMC PDF and the direct.mit.edu PDF both returned an HTML challenge
    page, not a PDF, so I read the PMC HTML text; the figures (Figs 1–6)
    were available only as captions. I could NOT get the Supplementary
    Information (opmi-10-857-s001.pdf; the PMC and Europe PMC links returned
    HTML challenge pages). The SI holds the mediation details, the
    between-subjects first-trial analyses, the morally-bad Study 2 question
    wordings and pilots S2a–S2c, so none of those are verified here. I did
    not open the OSF data.). Upgraded from `Skimmed` to `Read`: the claims
    table, assumptions and results are new, and the skim is corrected where
    the full text disagreed.
date: '2026-09-26'
summary: >-
  Across three Prolific studies (N = 198, 673, 142; Likert 1–7), judgments
  that "X happened because the agent wanted X" track intentionality
  judgments under manipulations of luck. Causation is the strongest
  predictor of intentionality: standardized β = .46, .56, .53, against
  know-how β = .33, .20, .27 and probability-raising β = .14, .16, .10.
  Across the 12 condition means, r = .98. Causation only partly mediates
  the effect of luck (64%, 45% and 49%; exploratory analyses). As the
  causal account predicted, Study 3 found that the effect of Process
  (normal vs mix-up) on intentionality is larger when the agent knows how
  the buttons work (interaction F(1, 423) = 32). In the morally neutral
  Kraemer vignette, intentionality and causation came apart.
---
<!-- inactive-ok-file: LIT-144 — Deferred: a related work named by a 2026-09-26 close reading on the agency tag; lapses when the cited work is read -->

# NOTE-092: Quillien — Luck and intentional action

## Contribution

The paper extends Quillien & German's (2021) causal definition of "intentionally" to the luck effect, the finding that successes due to chance are judged less intentional. It derives from counterfactual theories of causal judgment a set of qualitative predictions: skill-independent luck effects, objective over subjective probability, alternative-option effects, the Kraemer means/ends asymmetry, and moral override. It then tests whether causal judgments of the form "E because the agent wanted E" move with intentionality judgments. The new empirical contributions are: (i) the Knobe (2003) marksman pattern holds for causal judgments; (ii) the Kraemer effect appears in causal judgments only in the morally bad vignette; (iii) a predicted Knowledge × Process interaction, which the know-how and probability-raising theses do not predict (note 18: they are "agnostic").

## Key insight

Calling an outcome intentional is, on this account, a causal judgment about the agent's desire. That judgment is graded, and luck weakens it by making the desire–outcome link non-robust: it is easy to imagine the agent wanting E and E failing. The folk concept of intentional action is therefore "externalist": it depends on how mental states connect to the world, not on the mental states alone. The paper compares it to the folk concept of knowledge in Gettier cases (Conclusion).

## Assumptions

- The folk "A did X intentionally" is roughly equivalent to "X happened because A wanted X" (statements (1)–(2)). This is a simplification of Quillien & German (2021), which speaks of "attitude" and adds constraints against deviant causal chains (note 1).
- Causal judgment is graded and counterfactual. People simulate alternatives and weigh necessity and robustness (Causation and Counterfactuals). Counterfactual simulation is "anchored" in the actual world: in a mix-up, people imagine other mix-ups (note 17).
- The probability-raising thesis is read non-teleologically, as whether the action *in fact* raised the odds (note 7).
- The mediation analyses assume Condition → Causation → Intentionality is the right causal model. They are "confirmatory", not discovery (Study 1 Results).
- "Morality" is a label for a vignette contrast confounded with difficulty (note 8; Study 2 Methods), and the paper does not rely on it as a clean manipulation.
- Samples: US Prolific workers with 50–1000 prior studies and ≥90% approval, excluded for failing comprehension or a white-text bot check.

## Key results

- **Study 1** (Knobe 2003 marksman; 2 skill × 2 morality, within-subjects; N = 198 of 200).
  - Intentionality: high skill M = 6.65 (SD 0.98) vs low M = 5.19 (2.14), F(1, 591) = 240; bad 6.51 vs neutral 5.34, F = 154; skill × morality interaction F = 94 (skill effect larger when morally neutral); all p < .001.
  - Causation: 6.56 vs 5.35, F = 194; bad 6.39 vs neutral 5.52, F = 100; interaction F = 79.
  - Know-how: skill F = 643, morality F = 46, interaction F = 54. Probability-raising: 127 / 66 / 18.
  - Mediation by causation: 64% of the skill effect [0.56, 0.73].
  - Mixed model standardized β: causation .46, know-how .33, probability-raising .14. Bootstrap CIs on differences: causation − know-how [.01, .25]; causation − probability-raising [.20, .43]; know-how − probability-raising [.10, .28].
- **Study 2** (Kraemer; 2 Means/Ends × 2 morality, between-subjects; N = 673 of 695).
  - Intentionality: ends M = 4.26 (2.40) vs means 2.40 (1.87), F(1, 669) = 176; bad 4.22 vs neutral 2.44, F = 164; interaction F = 105.5.
  - Causation: ends 3.71 vs means 2.43, F = 78; morality F = 145; interaction F = 86.
  - Know-how: condition F = 178, morality F = 0.27 (p = .60), interaction F = 19. Probability-raising: 44 / 38 / 7.36 (p = .007).
  - Within the neutral vignette: intentionality ends 2.70 vs means 2.20, t(333.2) = 2.62, p = .009; know-how t = 6.26; probability-raising t = 2.75; **causation 2.22 vs 2.20, t(350.3) = .12, p = .91 (no effect)**.
  - Within the bad vignette: intentionality 6.01 vs 2.62, t = 16.9; causation 5.39 vs 2.68, t(315) = 11.6; know-how t = 13.3; probability-raising t = 7.46.
  - Mediation: 45% [0.36, 0.55].
  - β: causation .56, know-how .20, probability-raising .16. Difference CIs: causation − know-how [.24, .47]; causation − probability-raising [.30, .49]; know-how − probability-raising [−.05, .14] (not reliable).
- **Study 3** (gumball machine; Knowledge × Process, within-subjects; N = 142 of 198).
  - Intentionality: know 4.88 (2.22) vs don't 2.91 (1.98), F(1, 423) = 202; normal 4.65 vs mix-up 3.14, F = 118; **Knowledge × Process F = 32, p < .001** (Process matters more with knowledge).
  - Causation: 4.50 vs 2.96, F = 165; 4.25 vs 3.21, F = 75; interaction F = 36.
  - Know-how: Knowledge F = 800; Process p = .19; interaction p = .12. Probability-raising: Knowledge F = 8.5 (p = .004); Process F = 91; interaction p = .79.
  - Mediation of the Process effect: 49% [0.38, 0.61].
  - β: causation .53 [.46, .60], know-how .27 [.20, .33], probability-raising .10 [.04, .16].
  - Conditional Nakagawa R²: causation-only model .57 vs know-how × probability-raising model .44; difference CI [.07, .19].
- **Item level** (12 condition means across studies): intentionality correlates with causation r(10) = .98, with know-how r(10) = .82, and with probability-raising r(10) = .88.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Luck manipulations (skill, means/ends, process) move causal judgments of "E because the agent wanted E" in the same direction as intentionality judgments | strong (for the association) | experiments S1–S3, ANOVAs above |
| C2 | Causal judgment predicts intentionality better than know-how or probability-raising | moderate | mixed-model β in all three studies with bootstrap CIs on differences; S1's causation − know-how CI [.01, .25] barely excludes 0 |
| C3 | The Knowledge × Process interaction in intentionality, a novel prediction of the causal account, holds and is mirrored in causation but not in know-how or probability-raising | moderate–strong | S3, pre-registered; single vignette family |
| C4 | Luck affects intentionality *via* causal judgment | weak–moderate | exploratory, non-pre-registered mediation covering only 45–64% of effects; the authors say the evidence is "mostly correlational" |
| C5 | The causal account explains the Kraemer effect | weak (partial) | S2: holds in the morally bad vignette only; in the neutral vignette, intentionality shows the effect and causation does not |
| C6 | The account also explains the objective-vs-subjective probability, alternative-option and moral-override patterns in prior literature | informal argument | Intro, re-reading of Ericson et al. 2023, Mele & Cushman 2007, Knobe 2003; not tested here |
| C7 | The folk concept of intentional action is externalist, like that of knowledge | informal argument | Conclusion; analogy only |
| C8 | Control-based accounts cannot explain S3, since the manipulation occurs after the agent's action | informal argument | General Discussion |

## Method

Vignette experiments on Prolific with Likert (1–7) agreement ratings of four statements per scenario: intentionality, causation ("because [she] wanted"), know-how and probability-raising. Question order was partly fixed (S1, S3: intentionality first; S2: intentionality last). Analyses: (repeated-measures) ANOVA; Welch t-tests within vignettes; linear mixed-effects models with participant random intercepts and standardized β; participant-level bootstrap (1,000); exploratory mediation; item-level Pearson correlations over condition means. Data and code are on OSF.

## Concepts

- **Causal account of intentional action**: "A did X intentionally" ≈ "X happened because A wanted X" (after Quillien & German 2021; Davidson 1980).
- **Necessity**: whether E would still have happened without C.
- **Robustness / sufficiency**: whether C would still have produced E under slightly different background conditions. The paper's key lever for luck.
- **Luck effect**: lower intentionality for outcomes achieved by chance.
- **Kraemer effect**: the ends judged intentional, but the chancy means to them not.
- **Know-how thesis** (Pavese; Pavese & Henne 2023) and **probability-raising thesis** (Ericson et al. 2023; Doan et al. 2025), read non-teleologically: the rival accounts.
- **Process** (S3): whether the machine works normally or mixes up containers after the choice. It varies probability-raising while holding the agent's mental states fixed.

## Connections

It builds on Quillien & German (2021) and on counterfactual models of causal selection (Icard, Kominsky & Knobe 2017; Quillien & Lucas 2024). It replicates Knobe (2003) and Pavese & Henne (2023), and re-reads Ericson et al. (2023) and Doan et al. (2025). Among held works, [LIT-206](../literature.d/LIT-206.md) (Goldstein et al., interpretationist desires for LLM "instance agents", Deferred) is the closest neighbour on the question of attributing desires and agency. Quillien measures how people turn a desire attribution into an *intentional-action* attribution, and the answer is that the desire–outcome link must be robust. The record's counterfactual-causation papers ([LIT-144](../literature.d/LIT-144.md), Pernu on exclusion and downward counterfactuals) share the necessity/sufficiency vocabulary but are metaphysics, not folk psychology.

**Agency.** The work holds a causal-externalist account of *attributed* agency. What makes an outcome someone's intentional doing, in the folk concept, is that their desire was a robust (not merely necessary) cause of it. It is a theory of the concept of intentional action, not of what agents are. **The `agency` tag is justified**: intentional action and control are in the tag's blurb, and a reader browsing agency would expect this. It should stay first, with `cognition` second.

## Bearing on the record

No THEORY in the record rests on it that I know of. It could support a theory note on the folk attribution of intentional action, if one is written. For ML practice it carries nothing: there is no instruction for training or evaluating models. One tangential relevance, which is not a practice: the finding that people withhold intentionality when the desire–outcome link is non-robust bears on how people will attribute intent to automated agents whose success is chancy. The paper does not study machines.

## Limitations

- The evidence is correlational. Mediation is exploratory and partial (≈ half).
- The author raises two worries himself: asking causation and intentionality about the same vignette invites task-demand and consistency effects, and the argument against this (differential tracking) is indirect.
- The causal-judgment item ("because [she] wanted") is close in wording to the intentionality item, and is not a measure of causal strength per se.
- Few vignettes: one scenario family per study. The morality contrast is confounded with difficulty and wording.
- The item-level r = .98 rests on 12 condition means.
- The neutral Kraemer case dissociates intentionality from causation (also Varghese & Henne 2025), which the account does not explain.
- No computational counterfactual model is fitted, so "robustness" is never measured, only inferred from the manipulations.
- The SI was not read (see `read:`).

## Open questions

- Fit an explicit counterfactual causal-strength model (e.g. Quillien & Lucas 2024) to the vignettes and test whether its predicted desire–outcome strengths predict intentionality quantitatively, beyond the rated causation item.
- What drives the residual half of the luck effect, and the neutral Kraemer divergence?
- Do the same patterns hold for attributions to artificial agents, and across cultures beyond US Prolific?

## Corrections to the seeded skim

- **There is no formal or computational model.** The dossier and skim describe a "causal theory" as if it had a model, and the request asked for "the model's exact form". The account is verbal: "people judge that an agent did X intentionally if the agent's desire toward X caused X to happen" (Our Proposal), where causal strength is graded. The two ingredients, *necessity* ("would E still have happened if C had not happened?") and *robustness/sufficiency* ("would C still have led to E even if background circumstances had been slightly different?"), are taken informally from counterfactual theories (Icard et al. 2017; Quillien & Lucas 2024). Note 2 says the mind need not compute them explicitly. No equation is fitted and no model predictions are computed. The only quantitative models in the paper are statistical: repeated-measures and 2×2 ANOVAs; linear mixed-effects regressions of intentionality on causation, know-how and probability-raising with participant random intercepts (standardized β via `effectsize::standardize_parameters`, "refit"); participant-level bootstrap (1,000 resamples) CIs on β differences; and exploratory mediation of the form Condition → Causation → Intentionality.
- **"Subsumed by" overstates the paper.** The skim says know-how and probability-raising are "presented as consistent with, and subsumed by" the causal account. The paper says they are "consistent with" it (Other Recent Accounts). The General Discussion concedes that know-how and probability-raising stay "weakly or moderately associated with intentionality even when controlling for causal judgments", and that the findings "do not foreclose" independent effects.
- **Causal judgment explains only about half of the luck effect.** The dossier and abstract do not say this. The mediated shares are 64% [.56, .73] in S1, 45% [.36, .55] in S2 and 49% [.38, .61] in S3. All the mediation analyses are exploratory and were not pre-registered (note 11).
- **Study 2 was not pre-registered**, although it follows the pre-registrations of pilots S2a and S2b. Studies 1 and 3 were pre-registered.
- **The Study 2 vignette is not the intro's.** The intro's Kraemer example (a lever opens one of ten boxes, box eight holds poison) is not the Study 2 stimulus. Study 2 used Pavese & Henne's arrow-down-path-eight "moral" vignette and a game-show green-ball vignette.
- **Study 3 lost 28% of its sample to comprehension checks** (56 of 198 excluded; final N = 142). The dossier does not mention this.
- **Typo in the published text.** The Study 3 causation mix-up mean is printed as "(SD = 3.21, SD = 1.98)". It is presumably M = 3.21.
- Otherwise the dossier's bibliographic data (Open Mind vol. 10, 857–883; 2026-06-17; DOI 10.1162/OPMI.a.361) and its reading of the Study 2 divergence (the neutral Kraemer case) agree with the text.
