---
number: 766
status: Read
formerly:
- NOTE-tmp75pvf
paper: LIT-983
title: 'Linson et al. — Impaired context disambiguation in post-traumatic psychopathology'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from bioRxiv version 2 (posted 2025-08-04, under the old
    title "Neurocomputational impairments in disambiguation of context as
    a key determinant of post-traumatic psychopathology"), as the Europe
    PMC open-access JATS full text (PPR1047206), converted to text:
    abstract, introduction, Overview, the neuromodulatory circuit,
    Results, Discussion, Online Methods, the Experts by Lived Experience
    feedback and every figure caption. The figures were not viewed and
    the Supplementary Information was not read. The current version 3
    (2026-05-13, the current title) could not be reached: bioRxiv returned
    HTTP 429 to every request for its PDF and its JATS XML over several
    minutes of retries with backoff. What is said below is about version
    2.
date: '2026-10-14'
summary: >-
  An active-inference model of PTSD as lost context disambiguation. An
  overly precise prior that one is in a harmful context makes the
  exploratory policy look uninformative. The agent attenuates its
  periphery, never gets the evidence that would correct the prior, and
  the belief sustains itself. Shown only in illustrative simulations,
  which also contrast exposure that restores context sensitivity with a
  precision-lowering drug that removes symptoms until it stops.
---
<!-- inactive-ok-file: THEORY-058 THEORY-285 — Proposed; the loop account QUESTION-045 names as a partial answer, and the account filed from this reading -->

# NOTE-766: Linson et al. — Impaired context disambiguation in post-traumatic psychopathology

## Contribution

The paper recasts post-traumatic stress disorder as a failure to tell
which context one is in, not a failure of fear extinction. It gives a
generative model (a partially observed Markov decision process under
active inference) in which a traumatic experience can leave an overly
precise prior for "harmful context". That prior stops the agent sampling
the evidence that would correct it. It attaches a putative neuromodulatory
circuit and a cognitive account of flashbacks, and it shows the loop and
two interventions in simulation.

## Key insight

The maintaining link is a choice of what to look at. Under active
inference, the agent picks policies by expected information gain. If the
prior is already confident that the context is harmful, looking at the
periphery is "falsely believed to be uninformative due to overly
informative prior beliefs". So the agent attenuates the periphery and
focuses on the foreground, whose observations are the same in both
contexts. "As long as the sensory attenuation policy is selected, no
amount of observations will render prior beliefs obsolete." The prior is
kept up not by what it says but by the policy it licenses.

## Assumptions

- **Two contexts, one shared cue.** The model has a harmful and a harmless
  context that share an ambiguous first observation (the "triangle") and
  differ only in peripheral observations.
- **Two actions per time step.** Exploratory sensing of the periphery, or
  sensory attenuation of the periphery. Three-step trials, four policies.
- **Context priors are learned Dirichlet counts** (the D vector), with
  learning and forgetting. Vulnerable and resilient agents differ in "the
  specific weights of learning and forgetting". The paper gives no values.
- **Drugs act on precision.** SSRIs, benzodiazepines and alcohol are
  modelled as lowered precision in the likelihood (A) and transition (B)
  tensors.
- **Harm, not fear.** The model is framed around harm expectation and
  defensive mobilisation, and is meant to stay compatible with fear
  conditioning and extinction "without relying on these constructs".
- **The circuit is putative.** The PPtg–LC acetylcholine–noradrenaline
  loop, the dorsal raphe serotonergic "brake" and the forebrain control
  are hypotheses assembled from the literature. They do not drive the
  simulations.

## Key results

- **Pathogenesis (Fig. 6).** Both agents start with balanced context
  priors, shown as two attractor basins. Then they get a short run of
  harmful trials, then a long run of random trials (50/50). The resilient
  agent gathers peripheral evidence and rebalances. The vulnerable agent
  enters "a 'vicious circle'": "the sensory attenuation policy prevents
  learning about the harmless context, which biases the system towards
  the sensory attenuation policy, and so on". The basins collapse into
  one. *Holds for:* one illustrative run per phenotype, with unstated
  parameters.
- **Trial schedule (Fig. 7a).** Trials 1–5 harmless, 6–16 harmful, 17–60
  random. By trials 50–60 the vulnerable agent selects sensory
  attenuation "under any condition".
- **Successful intervention (Figs. 7b–c, 7f blue).** Sixty trials of
  "controlled exposure to harmless condition" restore the exploratory
  policy near the end of the block. The priors begin to rebalance and stay
  balanced when random trials resume.
- **Illusory intervention (Figs. 7d–e, 7f orange).** Lowered A and B
  precision under random trials gives "more grayscale (low precision
  policy selection) and a wider range of selected policies", read as
  fewer symptoms. When precision is restored, the attenuation policy
  returns even on harmless trials, because "the contextual priors were not
  rebalanced". The authors say this contrast "closely matches randomised
  controlled trial (RCT) results", citing van der Kolk et al. (2007),
  EMDR against fluoxetine. It is asserted, not fitted.
- **The bistable reading (Discussion).** Plasticity can create unstable
  basins that favour sampling, or "a collapse or canalisation into a
  single basin". The collapse is "self-maintaining because it precludes
  epistemic foraging", and "the saddle point between basins corresponds to
  a reinstatement of context-sensitivity".
- **Key hypothesis.** "The balance of plasticity-enhancement and
  plasticity-decay for aversive events is greater in the vulnerable."
- **Testable predictions stated.**
  - Cued traumatic recall attenuates peripheral sensing more than focal
    sensing (a target/distractor paradigm).
  - Differently valenced contexts change startle to the same probe less in
    PTSD than in controls.
  - Active inference predicts more weight on trauma-encoded context, and
    dual representation theory less.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | An overly precise harmful-context prior can make exploration look uninformative and so block the evidence that would correct it | moderate | follows from expected-information-gain policy selection; shown in simulation (Figs. 4, 6) |
| C2 | Whether the loop forms depends on the learning and forgetting rates for aversive evidence | weak | two illustrative phenotypes, parameters not reported |
| C3 | Controlled exposure that restores exploration rebalances priors durably; precision-lowering drugs suppress symptoms without rebalancing | weak | one simulated sequence each (Fig. 7); the two arms also differ in environment |
| C4 | The simulated contrast matches the EMDR–fluoxetine RCT | weak | asserted by citation, no fit |
| C5 | A PPtg–LC–DRN neuromodulatory circuit implements the elevated tonic arousal of PTSD | weak | literature synthesis, not modelled |
| C6 | Flashbacks are a blend of focal sensation and top-down recalled context in visual working memory under peripheral attenuation | weak | narrative account; the model "does not drive the simulation" on this |

## Method

1. A generative model over hidden context (harmful, harmless) and state,
   with a shared cue at the start and context-specific peripheral
   observations reachable only by the exploratory action (Fig. 4).
2. Policies scored by expected free energy, so exploration is chosen when
   it is expected to resolve uncertainty about context.
3. Context priors D learned across trials as Dirichlet counts with
   forgetting. Vulnerable and resilient agents differ in learning and
   forgetting weights.
4. Interventions: a block of harmless-only trials (exposure), or lowered
   precision of the A and B tensors under random trials (drug), followed
   by restoration.

## Concepts

- **Context.** "Elements of the sensory or cognitive periphery that
  provide evidence for the states of affairs prior to belief-updating."
- **Contextual prior (D).** The learned prior probability of being in each
  context at the start of a trial.
- **Sensory (peripheral) attenuation.** A policy that lowers precision on
  the periphery while keeping focus on foreground elements. The authors
  read it as hypervigilance: "rapid shifting of foreground focus without
  resolving contextual uncertainty".
- **Counterfactual blocking.** From their earlier work (Moutoussis et al.
  2018): an impaired ability to accumulate evidence that a context is
  benign, so that Bayesian learning "breaks".
- **Pathogenesis, not aetiology.** The process by which a response that
  was adaptive becomes persistent, as opposed to its causes.
- **Return slope.** The decay of arousal after harm becomes unlikely.
  Vulnerability is "an inappropriately sluggish decay".

## Connections

The paper extends Linson, Parr and Friston (2020) and Linson and Friston
(2019) on PTSD under active inference, and Moutoussis et al. (2018) on
computational psychotherapy. It cites Kaye et al. (2023) and Seriès
(2019) as kindred computational accounts. It names Carhart-Harris's
"canalisation" for the collapsed basin. It sets itself against dual
representation theory on how much weight trauma-encoded context gets.

## Bearing on the record

- **[QUESTION-045](../questions.d/QUESTION-045.md).** The paper is an individual-scale model of exactly the
  structure the question names, and it answers part of it in simulation.
  - *Behaviour that blocks its own disconfirmation.* The sensory
    attenuation policy is selected because the prior is precise, and it
    withholds the only observations that could lower that precision.
  - *Capacity to leave degrades.* The basins collapse to one, so the
    exploratory policy, the way out, stops being selected.
  - *The maintaining link, not the content.* The two interventions both
    leave the prior's content (harmful) in place at the start. The drug
    lowers the symptoms; exposure restores the exploratory policy.
    Only restoring the policy rebalances the prior. That is the
    question's contrast in model form.
  - **Limit.** The two arms are not matched. Exposure runs in a
    controlled harmless-only environment and the drug in a random one, so
    the simulation does not hold exposure fixed while cutting the link,
    as the question asks. And it is a model, with no individual data and
    no measured hysteresis.
- **[THEORY-058](../theory.d/THEORY-058.md)** holds that disorders are kept up by self-reinforcing
  loops and outlast their triggers. This model is a worked mechanism of
  one such loop, with a stated tipping point. It is consistent with
  [THEORY-058](../theory.d/THEORY-058.md) and adds no data.
- **[THEORY-053](../theory.d/THEORY-053.md)** says only specific change in the theorised process,
  ahead of the outcome, bears on a theory of change. The paper's drug arm
  is an instance: the outcome (symptoms) moves without the process
  (context priors), and the symptoms come back. The paper reads it the
  same way.
- **[LIT-983](../literature.d/LIT-983.md)'s filing description holds.** The status note said it "models
  a maintained disorder as impaired belief-updating with an explicit
  adaptive/maladaptive boundary". It does, but the "boundary" is a
  qualitative tipping point in a simulation, not an estimated threshold.
- **Filed from this reading:** [THEORY-285](../theory.d/THEORY-285.md), the self-sustaining
  prior and the drug–exposure contrast, at simulation strength.
- **Anthology.** The paper carries treatment suggestions (psychotherapy
  that restores context sensitivity, drugs as adjuncts, caution about
  immediate debriefing). They are clinical, not machine-learning practice,
  so nothing goes to the anthology.

## Limitations

- **Simulation only.** No data are fitted. The phenotypes, schedules and
  precision changes are chosen to illustrate, and the parameter values
  are not given in the main text.
- **Version 2 only.** The current version 3 was not reached and may
  differ.
- **The circuit is not modelled.** The neuromodulatory account and the
  flashback account are narrative, assembled from cited findings.
- **The RCT match is by citation**, against one trial, with no
  quantitative comparison.
- **Unmatched intervention arms**, as above.
- **Two contexts.** Generalisation to many contexts, or to a graded harm
  probability, is not shown.
- The Experts by Lived Experience feedback is endorsement of the account's
  fit to experience, not evidence about mechanism, and the paper does not
  present it as such.

## Open questions

- The paper's own tests: peripheral against focal attenuation under cued
  recall, context-modulated startle, and the opposite predictions from
  dual representation theory.
- Can learning and forgetting rates for aversive context be estimated in
  people after trauma, and do they predict who develops PTSD? That would
  turn C2 from illustration into a finding.
- In the model, does exposure under a random environment, matched to the
  drug arm, still rebalance the priors? That is the comparison
  [QUESTION-045](../questions.d/QUESTION-045.md) needs, and the model could run it.
