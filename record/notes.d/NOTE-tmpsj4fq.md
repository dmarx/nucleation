---
status: Read
paper: LIT-tmpvgq87
title: 'Hesp et al. — Deeply felt affect: the emergence of valence in deep active inference'
version: 1
history:
- version: 1
  date: '2026-10-23'
  note: >-
    Read in full from the publisher's CC BY PDF as deposited by Aarhus
    University (pure.au.dk), text extracted with pdftotext. The abstract
    and §§1–6, with figure and table legends, were read closely, and the
    primer steps M1–M3 (§§3.1.1–3.1.3) were skimmed. The supplementary
    appendixes A1–A4 are not in the PDF and were not read. Page numbers
    are the journal's. Every quotation was checked by script against the
    extracted text. The simulation code on GitHub was not run.
date: '2026-10-23'
summary: >-
  A computational proof of principle with no data. Valence is a state of
  self, inferred at a slower, deeper level from affective charge, the
  update to the expected precision γ that sets how far the preference-
  driven action model, rather than habit, governs policy selection.
  Positive charge is rising confidence in the action model and negative
  charge falling confidence. The valence level sends priors on γ back
  down. "Felt" means explicitly represented, which the authors take as
  necessary, not sufficient, for self-reportable valence. For the record,
  this is the closest existing model of that felt valence is the system modelling its own
  dominance. But its sign and intensity run against the record's
  dominance account for negative valence, and it inherits the
  wanting/liking problem.
---
<!-- inactive-ok-file: CLAIM-tmpz8lli TERM-tmp8gbrt THEORY-055 THEORY-101 THEORY-662 CLAIM-tmp85p0g — Proposed; the account and candidate this reading tests and its neighbours, cited as open -->
<!-- inactive-ok-file: QUESTION-059 — Deferred; whether a functional characterization of affect must be felt, which this reading bears on -->
<!-- inactive-ok-file: LIT-tmp63om1 LIT-tmpb4r95 — Unavailable or Deferred, unread; Carver and Scheier 1990 and Carver 2003, compared here -->
<!-- inactive-ok-file: LIT-tmpmp2nw LIT-tmpd3ww1 — drafts filed in the same tranche -->

# NOTE-tmpsj4fq: Hesp et al. — Deeply felt affect: the emergence of valence in deep active inference

## Contribution

A formal model of emotional valence in discrete-state active inference,
with a simulation. Its own addition is "parametric depth". A higher level
infers its states from a lower level's *parameter* (the precision γ)
rather than from its states, and in return sets that parameter's prior.

## Key insight

Valence is the agent's inference about how well its own action model is
doing. The paper's hypothesis is "emotional valence can be formalized as a
state of self that is inferred on the basis of fluctuations in the
estimated confidence (or precision) an agent has in her generative model
of the world that informs her decisions", implemented "as a hierarchically
superordinate state representation that takes the aforementioned
confidence estimates at the lower level as data for further self-related
inference" (p. 401).

## Assumptions

- **Active inference.** Organisms minimize free energy, and "subjective
  fitness" is estimated model evidence, which natural selection keeps close
  to biological fitness (pp. 402–403).
- **Precision as confidence.** γ is "an internal estimate of model fitness
  (subjective fitness)" (p. 408). It is "a minimal form of (implicit,
  non-reportable) metacognition" (p. 408).
- **Explicit representation is necessary for report.** On assumed
  knowledge of conscious and unconscious processing, "higher-level valence
  representation (as in our model) will be necessary for conscious
  experience of valence" (p. 435).
- **Valence is one-dimensional and binary** in the simulation, with
  continuous intensity discussed informally (§5.4, §5.5).

## Key results

- **The mechanism.** Policy selection mixes a habitual prior with
  γ-weighted expected free energy, and "higher γ values afford a greater
  influence of the expected free energies of each policy entailed by one’s
  current action model" (p. 408). The update of γ is affective charge:
  "positive and negative AC corresponds, respectively, to increased and
  decreased confidence in one’s action model" (p. 410). AC "lends a sign
  to otherwise unsigned divergences between predictions and outcomes"
  (p. 399). Read back, the Conclusion calls AC "the corresponding
  belief-updating term that tracks its progress and regress: affective
  charge (AC)" (p. 438).
- **Precise action is not positive valence.** For prey suddenly chased,
  "while they have precise beliefs about action, AC would be highly
  negative (i.e., a case of negative valence but confident action
  selection)" (p. 410).
- **Valence is the deeper state, not AC.** "Note that we are not associating
  the affective charge term to emotional valence directly" (p. 417).
  "Parametric depth means that higher-order affective processes generate
  priors that parameterize lower-order (context-specific) inferences, which
  in turn provide evidence for those higher-order affective states"
  (p. 417). In anthropomorphic terms the agent can "explicitly represent
  whether her model is doing “good” or “bad” at a timescale that spans many
  decisions and observed outcomes" (p. 416). "Notice that when the
  affective charge is zero, the affective expectations on the current
  trial are determined completely by the expectations at the previous
  trial" (p. 420).
- **Simulation.** Over 64 T-maze trials with reversal at trial 33 the rat
  infers negative valence in the first and third quarters and positive in
  the second and fourth. It takes the cue-skipping shortcut only after
  positive valence is established, which the authors read as "a
  dissociation between positive valence and confident risky behaviors"
  (p. 423). Removing the higher level leaves behaviour unchanged before
  reversal ("Before context reversal, their behaviors were
  indistinguishable", p. 425). After reversal the agent without that level
  persists, then avoids. It also does not habituate: "the simpler agent
  cannot habituate to its own successes and failures" (p. 424).
- **Felt.** "Presumably this type of explicit valence representation is
  also a necessary condition for self-reportable experience of valence"
  (p. 429). "we have shown that a higher level is necessary to represent
  estimates about oneself", and so "only more complex organisms equipped
  with hierarchical models that can integrate internal evidence for
  different internal states will be capable of experiencing valence"
  (pp. 435–436). Which level matters is left open (p. 433).
- **The wanting/liking challenge, conceded.** "Arguably, the strongest and
  most important challenge for claiming a relation of dopamine, AC, and
  valence arises from previous studies linking dopamine more closely to
  “wanting” than pleasure" (p. 430). "A limitation of our model is that it
  does not currently have the resources to account for these other
  valence-related signals" (p. 430). The fallback is that "AC provides one
  source of evidence for higher-level valence representations and that
  pleasure is only one source of positive valence" (p. 431).
- **Counterexamples addressed (§5.5).** Falling without a parachute has
  certain outcomes but every policy fails preferences, so negative. In fear,
  intensity tracks how negative AC is. In anger, "confidently acting on
  anger can be associated with positive valence" (p. 434).
- **Prediction.** "trial-by-trial changes in AC would be predicted to
  correlate with those same valence measures" (p. 437), meaning self-report
  and startle, and with imaging correlates.
- **A sign inconsistency.** The text says γ rises "when (π − π̄) · Gπ > 0"
  (p. 409). The Figure 3 legend on the same page says it rises when "AC =
  (π − π̄) · Gπ < 0", and §3.3.3 writes "AC = (π̄ − π) · Gπ" (p. 420). The
  qualitative reading (positive AC is rising confidence) is consistent
  throughout. The formula's sign is not.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Valence can be formalized as a higher-level state inferred from changes in expected precision of the action model | demonstrated in simulation (face validity only) | T-maze model |
| C2 | A valence level improves adaptation to contingency change | moderate (in silico) | lesion comparison, Fig. 9 |
| C3 | AC is formally a generalized reward prediction error | strong (formal) | equivalence when ambiguity is negligible (p. 429) |
| C4 | Explicit higher-level valence representation is necessary for conscious valence | assumed | appeal to conscious-access literature |
| C5 | AC is dopaminergic | weak | one study (Schwartenbeck et al. 2015), as the authors say |

## Concepts

- **expected precision γ** — confidence in the action model, which weights
  expected free energy against the habitual prior in policy selection.
- **affective charge (AC)** — the Bayes-optimal update to γ. Its sign is
  rising or falling confidence.
- **subjective fitness** — estimated model evidence, an internal proxy for
  biological fitness.
- **parametric depth** — a higher level that takes a lower level's
  parameter as data and sets that parameter's prior.
- **affective inference** — inference about one's own valence state.

## Connections

Brouillet and Friston ([LIT-957](../literature.d/LIT-957.md), [NOTE-785](NOTE-785.md), [THEORY-662](../theory.d/THEORY-662.md)) cite it for valence,
and their felt fluency is the same shape: a hierarchically deeper
inference about precision. Sandved-Smith et al. ([LIT-1191](../literature.d/LIT-1191.md), [NOTE-958](NOTE-958.md)) extend
its parametric depth to attention and meta-awareness. Berridge and
Kringelbach ([LIT-tmpmp2nw](../literature.d/LIT-tmpmp2nw.md)) supply the wanting/liking evidence it
concedes it cannot yet meet. The sign of AC is close to Carver and
Scheier's progress against a reference rate ([LIT-tmpdmzgc](../literature.d/LIT-tmpdmzgc.md), [LIT-tmp63om1](../literature.d/LIT-tmp63om1.md)),
which the paper does not cite.

## Bearing on the record

**It is the nearest existing model of the felt-as-self-model candidate,
and the match is closer than its vocabulary suggests.** Policy selection
here is a negotiation between two rankings of the options. One is the
preference-driven expected free energy Gπ, the other the habitual prior
Eπ, and γ sets how far Gπ wins. On the record's terms ([TERM-tmp8gbrt](../terms.d/TERM-tmp8gbrt.md)), γ
*is* a dominance strength: the weight of one perspective's ordering in a
compensatory negotiation, the first regime of [CLAIM-tmp85p0g](../claims.d/CLAIM-tmp85p0g.md). The deep
level infers its valence state from changes in that weight and sets it
top-down. That is what the candidate proposes, almost exactly.
The deep level's purpose also fits the record's resumption mark: it lets
the agent re-weight after reversal without being surprised afresh.

**But it identifies valence with the self-model, not with the dominance,
and it reverses the record's intensity clause for negative valence.** Two
divergences matter:

- *Where valence is.* Hesp et al. put valence at the deeper level, and AC
  is only evidence for it. The record's account ([CLAIM-tmpz8lli](../claims.d/CLAIM-tmpz8lli.md)) puts
  valence in the dominance regime and makes feeling a further question. If
  the record adopts the felt-as-self-model candidate, Hesp is precedent
  for felt valence at the deeper level. Hesp gives no reason to call the
  lower regime valence at all.
- *Negative valence lowers dominance.* In Hesp, negative valence is low γ.
  The preference ordering's grip weakens and the agent "fall[s] back on
  her baseline prior over policies" (p. 420). On [TERM-tmp8gbrt](../terms.d/TERM-tmp8gbrt.md), negative
  valence is the maintenance ordering dominating while the system runs
  behind, and intensity is the strength of that dominance. These are
  opposed unless the habit prior in a negative state counts as the
  dominant maintenance ordering, and the paper gives no reason to read it
  so. The record held its intensity clause "for negative valence only"
  because of Carver 2003 ([LIT-tmpb4r95](../literature.d/LIT-tmpb4r95.md)). Hesp is a formal model in which
  the clause also fails for negative valence, if γ is the dominance. The
  paper's §5.5 fear case cuts the other way. There, confident flight is
  strong dominance with negative valence, which fits the record better
  than Hesp's binary scheme does.

**The sign clause is supported.** AC is zero when things go as expected
and signed by whether outcomes beat or fall short of the expectation.
That is "progress and regress" against a reference (p. 438), the same
shape as Carver and Scheier's reference-rate neutral point, which the
record adopted. This is independent convergence from a different
formalism.

**On wanting and liking, Hesp and the record are in the same boat.** The
paper concedes that if AC is dopaminergic it sits on Berridge's 'wanting'
side. Dominance, as the record defines it, sits there too
([NOTE-tmprub8s](NOTE-tmprub8s.md)). So neither account, as it stands, is an account
of 'liking'. The paper's fallback, that pleasure is "only one source of
positive valence", is available to the record as well. Taking it means
conceding that "hedonic valence" in [TERM-tmp8gbrt](../terms.d/TERM-tmp8gbrt.md) names something other
than pleasure.

**For the three layers.** The paper supplies an operational handle for
layer (3) that does not depend on report. Compare a system with the
self-modelling level against one without it. Behaviour is identical while
contingencies are stable and diverges after a reversal: faster
re-weighting, attenuated surprise, no habituation in the lesioned agent.
So the self-model shows itself in *how dominance is re-set after a
perturbation*, not in which ordering wins at steady state. That gives
the felt-as-self-model candidate a test that layers (1) and (2) cannot
supply. "Felt" here still means explicitly represented and so reportable,
as in Brouillet and Friston ([THEORY-662](../theory.d/THEORY-662.md)). Hesp et al. assume that
representation is necessary and do not claim it is sufficient, so
[QUESTION-059](../questions.d/QUESTION-059.md) is not answered.

## Limitations

A face-validity simulation. Its parameters are hand-set, there is no
fitting to data and no model comparison, and valence is binary. The claim
that explicit representation is necessary for conscious valence is
assumed. The dopamine link rests on one study. The AC sign convention is
inconsistent across pp. 409–420. The supplementary appendixes, which hold
the free-energy derivations and the neuroanatomy (A4), were not read.

## Open questions

- If γ is read as dominance strength, does the model admit a regime where
  negative valence goes with *strong* dominance of a maintenance ordering
  (Hesp's fear case), or only with weakened dominance of the preference
  ordering?
- Could the lesion comparison be run on an organization, with a
  self-monitoring function removed and re-weighting after a shock
  compared?
