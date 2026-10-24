---
status: Read
paper: 'LIT-tmp9li67'
title: 'Brown, Price & Dombrovski — Anxiety as a disorder of uncertainty'
version: 1
history:
- version: 1
  date: '2026-10-24'
  note: >-
    Read in full on 2026-10-24 from the NIH author manuscript in PubMed
    Central (PMC10475148, NIHMS 1901333), the accepted manuscript of the
    Cognitive, Affective, & Behavioral Neuroscience paper, fetched as JATS
    XML through NCBI E-utilities (efetch, db=pmc) and converted to text by
    script. PMC's licence line: "This file is available for text mining. It
    may also be used consistent with the principles of fair use under the
    copyright law." Read: the abstract, every section from the
    introduction to the conclusions, Figures 1–4 (captions; the images were
    not available in the XML) and Tables 1–2. The reference list was not
    read. The version of record is free to read at Springer (bronze open
    access, per Unpaywall), but link.springer.com answered every request
    with a client challenge page, and PMC's PDF route with a reCAPTCHA. The
    PsyArXiv preprint (doi:10.31234/osf.io/4zykv, version 1 of 30 August
    2022, CC BY 4.0) was downloaded and compared at the abstract, the
    section structure and Table 2: they match apart from wording. The
    manuscript has no page numbers, so places are given by section.
date: '2026-10-24'
summary: >-
  A narrative review and theoretical proposal, with no new data and no
  simulation. Computational learning studies of anxiety (seven, not a
  systematic search) find altered adjustment of learning rate to kinds of
  uncertainty, mostly with aversive outcomes, rather than inflated threat
  learning or valuation. The authors propose that in aversive environments
  avoidance of uncertain states keeps their uncertainty high and so
  perpetuates itself, that anxiety amplifies this by misreading noise as
  change, and that exposure works by reducing the uncertainty, not the
  threat. It covers fear-based disorders and says it does not explain GAD.
---
<!-- inactive-ok-file: CLAIM-tmp8z857 CLAIM-283 CLAIM-349 THEORY-285 — Proposed; the claims and reading this bears on, named, nothing here rests on them -->
<!-- inactive-ok-file: LIT-tmppvxx9 LIT-tmp4sdbb LIT-tmpciuti — Deferred or read in this batch; works named for comparison -->

# NOTE-tmp1dwn4: Brown, Price & Dombrovski — Anxiety as a disorder of uncertainty

## Contribution

Cognitive-behavioural accounts put excessive learned threat behind
maladaptive anxiety, and exposure therapy was built on that view. The
authors argue that the laboratory record does not show enhanced aversive
conditioning or overvaluation of aversive outcomes in anxiety, but does show
disrupted learning under uncertainty. They then join that finding to
temporal-difference models of avoidance (Markov decision processes) and to
the explore/exploit trade-off, which no earlier account had done: "To our
knowledge, no work has yet connected the maladaptive uncertainty learning
seen experimentally in anxiety to these models of avoidance" (Temporal
difference MDP models of avoidance). The result is a framework, stated in
words and diagrams. Nothing is fitted or simulated.

## Key insight

In an aversive environment, choosing the known safe option over an
uncertain one is the normal policy, and it has a side effect: the uncertain
option is never sampled, so its uncertainty never falls. "This avoidance
maintains high uncertainty and perpetuates avoidance by preventing
exploration of more uncertain states" (Uncertainty-sensitive Markov
decision-process models and anxious avoidance). If anxiety inflates the
kinds of uncertainty that discourage exploration, the same loop runs
harder: "Continued avoidance of uncertain states will maintain
inappropriately elevated uncertainty estimates, ensuring continued
avoidance." Exposure, on this view, is forced exploration that lowers the
uncertainty estimate, and the lower estimate in turn favours more
exploration.

## Assumptions

- **Three kinds of uncertainty (Table 1; Precisely defining uncertainty).**
  Irreducible uncertainty (noise, risk), and two reducible kinds:
  estimation uncertainty (what is not yet known about stable contingencies)
  and unexpected uncertainty (volatility, the chance that contingencies
  have changed). High volatility should raise the learning rate; high noise
  should lower it.
- **In aversive settings the sign of exploration flips (Fig. 3).** In
  rewarding environments irreducible uncertainty decreases exploration and
  estimation uncertainty increases it; "effects are opposite in aversive
  environments". The effect of unexpected uncertainty is marked "?" and
  guessed to decrease exploration under threat.
- **Avoidance as temporal-difference learning.** They adopt the MDP models
  of Moutoussis et al. (2008) and Maia (2010), in which avoidance is
  reinforced by an advantage or a drop in negative value, and add an
  uncertainty term that drives exploration.
- **Values update between episodes.** Each exposure exercise is one
  episode of an MDP, and "values and uncertainties are generally only
  updated once the episode is over" (Exposure as remediating maladaptive
  uncertainty learning). This is what lets them explain why between-session
  but not within-session fear reduction predicts outcome.
- **Scope.** Fear-based disorders (panic, social and specific phobia, OCD,
  PTSD), distinguished from distress disorders such as GAD.

## Key results

There are no new results. The paper reports and organises others'.

- **What the learning literature shows (Current ideas about the role of
  uncertainty; Choice models).** Anxiety disorders show elevated responding
  to safety signals during conditioning, more responding to the extinguished
  threat cue, and broader generalization, not stronger conditioning. In
  decisions from description, anxiety goes with more risk and ambiguity
  aversion but not more loss aversion: people with high anxiety "avoid
  choices where such outcomes are less predictable".
- **Computational studies (Table 2; Reinforcement learning studies).**
  Seven studies (Browning et al. 2015; Brown et al. 2018; Homan et al.
  2019; Gagne et al. 2020; Norbury et al. 2021; Abend et al. 2022; Zika et
  al., preprint), from 20 to 147 participants per group. The common thread
  is in how the learning rate adjusts to uncertainty (associability,
  volatility adjustment, latent-state formation): "Other parameters
  measuring overall learning rate, choice consistency, and outcome valuation
  show little relationship with anxiety." Differences appear mostly with
  losses or aversive outcomes. The selection was by the authors' knowledge
  and searches and does "not represent a comprehensive, structured
  literature review following PRISMA guidelines".
- **The synthesis (Anxiety as maladaptive aversive uncertainty learning).**
  Under high volatility anxious people learn slightly slower overall but
  speed up after very surprising outcomes; under high noise they learn
  faster, especially after surprising losses, an effect called "less
  consistent". The authors read this as an inability to tell noise from
  change.
- **Habit is not the source (Current theories of avoidance).** Large
  transdiagnostic samples tie reduced model-based planning to compulsivity,
  not anxiety: "Regardless, maladaptive avoidance in anxiety does not seem
  to stem from an increased tendency to form habits."
- **Clinical observations they lean on (What is missing from our
  understanding of exposure?).** Higher pretreatment avoidance predicts
  worse response beyond severity; reductions in avoidance come before other
  symptom change; "In practice, initial exposure sessions focus more on
  reducing avoidance than on changing expectations of feared outcomes."
  Augmenting normative extinction (D-cycloserine, TMS or tDCS,
  novelty-facilitated extinction) has not improved exposure. These are
  cited, not tested here.
- **The proposal (Uncertainty-sensitive MDP models; Fig. 4).** Normative
  behaviour in uncertain aversive MDPs already avoids uncertain states. In
  anxiety, noise is misread as estimation or unexpected uncertainty, both
  of which reduce exploration under threat, so avoidance grows. Avoiding
  raises the learned value of the avoidant option and reduces its
  uncertainty while the uncertainty of the unchosen option stays put. High
  uncertainty is also distressing and raises perceived threat imminence,
  pushing behaviour toward passive avoidance and cached "options".
- **Relapse (Exposure as remediating …).** "Corrections in uncertainty
  estimates, but not vulnerabilities in uncertainty learning itself, may
  explain relapse after response to exposure therapy".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Anxiety is not well characterised by enhanced aversive conditioning or by overvaluation of aversive outcomes | moderate | cited meta-analysis (Duits et al. 2015) and decision studies; not re-analysed |
| C2 | In computational learning studies anxiety goes with altered adjustment of learning rate to uncertainty, mostly for aversive outcomes, not with altered overall learning rate or valuation | moderate to weak | seven studies chosen without a systematic search, with mixed directions; Table 2 |
| C3 | In aversive MDPs avoiding uncertain states keeps their uncertainty high and perpetuates avoidance | argued, not modelled | verbal and diagrammatic argument; Figs 3–4 |
| C4 | Anxious avoidance arises because anxiety misreads noise as change and so inflates the uncertainty that suppresses exploration under threat | weak: a hypothesis | no simulation, no data |
| C5 | Exposure works by reducing miscalculated uncertainty, not by extinguishing excess threat | weak: a hypothesis | consistency with between-session findings, cited |
| C6 | Maladaptive avoidance in anxiety does not come from increased habit formation | moderate | cited transdiagnostic studies (Gillan et al.) |

## Concepts

- **Irreducible uncertainty**: "Uncertainty from probabilistic
  relationships between stimuli and outcomes" (Table 1); noise or risk.
- **Estimation uncertainty**: reducible uncertainty from "lack of knowledge
  about current relationships between stimuli and outcomes" (Table 1).
- **Unexpected uncertainty**: reducible uncertainty "related to
  possibility of changes in contingencies" (Table 1); volatility.
- **Options**: "Decision policy specifying a set sequence of actions
  between several linked states in an MDP" (Table 1). Unlike habits they
  are goal-directed and interruptible; the authors suggest anxious people
  fall back on them under threat.
- **Core fear**: read as "a specific terminal state in a specific MDP"
  (Practical advantages), which is why exposures must target it.

## Connections

It builds on the uncertainty-and-anticipation model of Grupe & Nitschke
(2013), intolerance of uncertainty (Carleton 2016), Piray & Daw (2021) on
telling noise from volatility, and the temporal-difference avoidance models
of Moutoussis et al. (2008) and Maia (2010). It sets itself against
Mowrer's two-factor theory, Lovibond's expectancy model (which it recasts
in temporal-difference terms rather than rejecting), LeDoux et al.'s
Pavlovian and habit routes, and emotional processing theory. It cites
Zorowitz et al. (LIT-tmppvxx9) and Gagne & Dayan (2022) as pessimistic
policies that produce avoidance, and doubts they capture anxiety: "This form
of choice process, where avoiding negative outcomes is favored over
maximizing reward, may better represent normative, negative
outcome-avoiding behavior in aversive environments than anxiety, however."

## Bearing on the record

- **CLAIM-tmp8z857 (governance-maintained anxiety).** The exchange cited this
  review as adjacent evidence. The reading gives the claim one step and a
  rival.
  - **The step it supports.** The claim says avoidance keeps the
    hypotheses of danger and safety unseparated and that "the defense keeps
    the uncertainty unresolved". This paper says the same in
    reinforcement-learning terms: avoidance of uncertain states "maintains
    high uncertainty and perpetuates avoidance". It also says the policy
    that starts the loop is normative in aversive settings, which fits the
    claim's caution that defence is not by itself pathology.
  - **The rival it supplies.** Its loop runs entirely through a belief
    variable, the uncertainty estimate, and a fixed exploration policy.
    There is no authority variable and no process that is granted or
    denied influence. In the claim's own terms this is a belief-maintained
    account with an information cost, the first defeater the claim names.
    For the claim to be distinct, its test has to hold the uncertainty
    estimate fixed, not only the represented threat probability, since
    here a correct threat estimate with an inflated uncertainty estimate is
    enough to keep avoidance going.
  - **Habit.** The paper's reading of the literature, that anxious
    avoidance is not habit, removes one of the claim's alternatives at the
    level of the literature, not of a test.
  - **Belief correction is not behavioural correction.** The clinical
    point that early exposure targets avoidance before expectations, and
    that avoidance reduction precedes symptom change, fits the claim's
    separation of the two. The sources are cited, not read.
- **QUESTION-045 (a disorder kept by behaviour that blocks its own
  disconfirmation).** A candidate mechanism of the question's kind, at the
  level of verbal theory: the maintaining link is avoidance of uncertain
  states, and exposure cuts it. It offers no test that holds exposure fixed
  while cutting the link, and no individual data.
- **THEORY-285.** The same shape in another formalism: an agent that
  will not sample where it is uncertain keeps the uncertainty. The active
  inference model makes the uncertainty a precise prior; here it is a
  miscalculated uncertainty estimate.
- **Correction to the exchange.** Its description ("better understood
  through disrupted uncertainty learning and explore–exploit decisions
  than through threat expectancy alone") is accurate. It should add that
  this is a proposal without a model run or data, that the evidence base is
  seven studies chosen without a systematic search, and that the framework
  is for fear-based disorders and, by its authors' statement, does not
  explain GAD.
- Filed: THEORY-tmp0vr2q (the empirical synthesis) and THEORY-tmpf8za8 (the
  avoidance–uncertainty loop, as a proposal).
- No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **No model is run.** The MDP figures are schematics with illustrative
  numbers. Whether an uncertainty-sensitive agent with misattributed noise
  actually produces persistent avoidance, and how much, is not shown.
- **The evidence base is small and selected.** Seven studies, chosen
  without a structured search, with inconsistent directions that the
  authors acknowledge, and with samples from 20 to 147 per group.
- **The direction of exploration under threat is partly guessed.** The
  effect of unexpected uncertainty on exploration in aversive settings "has
  yet to be investigated" (The explore-exploit dilemma and avoidance).
- **Scope stated by the authors.** They write that "many components
  require further testing before this framework can influence clinical
  practice"; it does not cover distress tolerance; and "the function of exposure therapy in
  non-fear based disorders, like generalized anxiety disorder or in eating
  disorders, is not explained by this framework" (Next steps).
- **Read from the accepted manuscript**, not the typeset version of record.

## Open questions

- Does an uncertainty-sensitive MDP agent with noise misread as volatility
  reproduce persistent avoidance in simulation, and in an instrumental task
  with people?
- Do measured uncertainty-learning deficits predict avoidance, and does
  their change with exposure predict relapse, as the authors propose?
- Can the uncertainty estimate be changed while avoidance is held fixed,
  or the reverse? That contrast would separate this account from one in
  which the avoidance policy is maintained for other reasons.
