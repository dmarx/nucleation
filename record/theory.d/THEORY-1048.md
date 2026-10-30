---
number: 1048
status: Active
formerly:
- THEORY-tmp20e6b
title: 'On the Black Queen Hypothesis of Morris, Lenski and Zinser, losing a costly function whose product leaks to neighbours is favoured by ordinary individual selection in large free-living microbial populations, and the loss proceeds until the remaining producers just supply the community, so that most cells come to depend on a rare few with no relatedness, cooperation or collective required'
version: 2
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed Proposed from NOTE-1212, the reading in full of Morris,
    Lenski & Zinser (2012). The formal argument (equations 1–3) is
    sound given its assumptions; the one worked case, katG in
    Prochlorococcus, rests on phylogeny and cited physiology, and the
    other cases are suggestions. Hence Proposed.
- version: 2
  date: '2026-10-30'
  note: >-
    Promoted by the twenty-fourth status review, at the status review's
    ruling (the owner delegated these rulings; ADR-065). The title
    reports what Morris, Lenski and Zinser's hypothesis says, read in
    full in NOTE-1212, and nothing in the record contradicts the report.
    What the condition asked beyond the title, that the authors be
    right, moves to THEORY-1235, Proposed, which extends this entry
    and keeps the condition word for word (ADR-065 §3). The answers edge
    on QUESTION-277 is moved to bears_on (ADR-060): the reading is
    evidence on the question, not an answer to it as posed. The old
    promote_when: "An experimental evolution study in which a
    loss-of-function mutant of a costly, leaky function invades a
    population or community, with its selection coefficient measured,
    and the invasion stops at a helper frequency matching what the
    measured cost and leakiness predict. Coexistence of helpers and
    beneficiaries must be shown to be maintained by the frequency
    dependence, not by niche differences. Alternatively, a field system
    in which beneficiary loss of a function is shown, by dN/dS or
    population-genetic evidence, to be selected rather than drifted,
    with helper density measured. More genomes that lack a leaky
    function do not meet it, since drift and other ecological causes
    predict that too. It is refuted if such losses in large free-living
    populations prove effectively neutral, or if beneficiaries spread
    until the function is lost from the community."
tags:
- endosymbiosis
- ecology
date: '2026-10-27'
source:
- LIT-1568
bears_on:
- QUESTION-277
summary: >-
  Morris, Lenski & Zinser (2012), [LIT-1568](../literature.d/LIT-1568.md), read in [NOTE-1212](../notes.d/NOTE-1212.md). A
  loss-of-function mutant invades when its resource saving
  B = (Q_A − Q_M)/Q_A exceeds its cost C, which falls as other cells'
  leaky activity protects it. Because protection falls as producers become
  rare, the loss is frequency dependent and stops short of community-wide
  loss. The evidence is Prochlorococcus's loss of katG and its dependence
  on a peroxide-removing community. The dependence it produces is one-way,
  from beneficiaries to helpers, and involves no collective.
---
<!-- inactive-ok-file: THEORY-1235 — Proposed; filed beside this reading by the twenty-fourth status review: the hypothesis itself, whether it is true -->
<!-- inactive-ok-file: QUESTION-277 LIT-1570 LIT-1225 THEORY-141 — Open, Deferred or Proposed; the question this bears on and the accounts set beside it, nothing here rests on them -->
# THEORY-1048: On the Black Queen Hypothesis of Morris, Lenski and Zinser, losing a costly function whose product leaks to neighbours is favoured by ordinary individual selection in large free-living microbial populations, and the loss proceeds until the remaining producers just supply the community, so that most cells come to depend on a rare few with no relatedness, cooperation or collective required

## Source

Morris, Lenski & Zinser (2012), *mBio* 3(2): e00036-12, [LIT-1568](../literature.d/LIT-1568.md), read
in full in [NOTE-1212](../notes.d/NOTE-1212.md) from the PubMed Central copy. The sections "The
Black Queen Hypothesis" (equations 1–3), "Are beneficiaries 'cheaters'?",
and the katG case with Figure 1.

## What was actually shown

- **A cost–benefit condition.**
  - The benefit of loss is the fractional saving in a limiting resource,
    B = (Q_A − Q_M)/Q_A.
  - The cost is the shortfall in a function's effective rate,
    k = k₀ + Σ NᵢLᵢkᵢ, which includes the leaky contribution of every
    other cell. With growth linear in k,
    C = (k_M − k)(μ_M − μ₀)/(μ_M k_M).
  - A mutant invades when B > C. As it spreads, the producers thin out,
    k falls and C rises, so the spread stops where B = C.

  This follows from the definitions, and was re-derived in the reading.
- **Outcomes.**
  - Against its ancestor alone, the mutant and the ancestor coexist on one
    limiting resource.
  - Where unrelated species supply the good, the ancestor goes extinct.
  - In a mixed community, loss proceeds "in every species ... until B is
    less than or equal to C for all individuals".
- **The case.**
  - No Prochlorococcus genome has katG. The Synechococcus KatG proteins
    are monophyletic, so the gene was lost.
  - Axenic Prochlorococcus dies in sunlit seawater, and co-occurring cells
    remove peroxide. These are cited results, not shown in the paper.
  - The benefit is an iron-quota saving of about 0.2%, computed, not
    measured as fitness.
- **Distinct from kin selection.** It needs no relatedness between
  producer and user: leakiness and density dependence do the work.

What could have failed: the formal condition cannot, given its
premises. The case could have failed if katG absence were ancestral, or
Prochlorococcus were peroxide-tolerant.

## What this does not say

- **Not that endosymbiont reduction is Black Queen.** The paper credits
  drift for endosymbionts and states the hypothesis for free-living
  organisms. Others extend it to symbionts ([LIT-1570](../literature.d/LIT-1570.md)'s
  "environment-induced redundancy").
- **Not that the outcome benefits all.** The conclusion says the division
  of labour "is often to the advantage of all". The paper's own analysis
  allows beneficiaries to harm helpers when they share a limiting
  resource.
- **Not a collective or a transition.** Nothing is co-transmitted or
  reproduces as a unit. The dependence is a community pattern, not a
  higher-level individual.
- **Not tested beyond one function.** Nitrogen fixation, siderophores,
  sulfur assimilation and biofilm matrix are matched to criteria, not
  analysed. The "shooting the moon" acceleration is speculation.
- **Not shown for nonlinear responses.** The linearity of equation 3 is
  assumed, and robustness to nonlinearity is asserted.

## Connections

- **[QUESTION-277](../questions.d/QUESTION-277.md).** This bears on the question's first route. Dependence
  arises by individual selection. It is directional (D, one way), and
  function is distributed across genomes (G). Cohesion, host control and
  collective-level selection are all absent. It is the record's clearest
  case of interdependence that is not individuality.
- **[THEORY-141](THEORY-141.md).** That account's stability condition presupposes a
  collective. This one produces dependence without any, so the two do not
  compete. They describe different outcomes.
- **[LIT-1225](../literature.d/LIT-1225.md).** Cooper & West (unread) model extreme specialization
  favoured within a group, where helpers are selected as helpers. Here
  helpers are what remains after others defect.
