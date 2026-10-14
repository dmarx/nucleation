---
status: Read
paper: LIT-969
title: 'Abel et al. — Agency Is Frame-Dependent'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv PDF (arXiv:2502.04403v1, the only
    version, 6 Feb 2025), text extracted with pdftotext -layout: the
    abstract, §1 (Introduction), §2 (the four claims and the conclusion),
    §3 (Discussion), Figure 1's caption and the reference list. The paper
    is four pages of text with no appendix, no theorem and no formal
    definition. The works its four claims are adapted from (Jiang 2019,
    Harutyunyan 2020, Kenton et al. 2023, Zadeh 1963, Abel et al. 2023)
    were not re-read; Kenton et al. is held here as LIT-909.
date: '2026-10-14'
summary: >-
  A four-page position paper. It argues, informally, that each of four
  conditions of agency (a boundary, being the source of action,
  goal-directedness and adaptivity) can be settled only after a choice
  of commitments it calls a reference frame, so agency attributions are
  frame-relative. Each step is adapted from a cited result. It gives no
  definition of a frame, no proof and no principle for choosing one.
---
<!-- inactive-ok-file: THEORY-tmp8ntgq CLAIM-170 CLAIM-174 CLAIM-194 THEORY-071 THEORY-232 THEORY-208 — Proposed; the theory filed from this reading and the claims and accounts it bears on, open -->
<!-- inactive-ok-file: LIT-430 — Unavailable; Dennett's book, which the paper cites for the puzzle, named and not leaned on -->

# NOTE-tmpk2s59: Abel et al. — Agency Is Frame-Dependent

## Contribution

The paper states, as a thesis for reinforcement learning, that whether a
system has agency depends on a reference frame: a set of commitments an
observer makes before the question can be answered. It supports this by
taking four conditions of agency in turn and citing, for each, a result
or remark showing that the condition can come out either way under two
plausible choices. Nothing is proved. The paper's own words: "At present,
our definitions, claims, and arguments are purely philosophical".

## Key insight

Each condition of agency hides a choice. Where is the boundary? Which
causal variables are in the model? What makes a goal "meaningful" rather
than an as-if description that fits every input-output system? Which
changes in behaviour count as adaptation? Fix these and agency can be
decided; leave them open and it cannot. The frame is not a defect to be
removed but part of what a statement about agency says.

## Assumptions

- **A four-part account of agency, "due largely to Barandiaran et al.
  (2009)"** (§1, Figure 1a): (1) individuality, a boundary separating the
  system from its surroundings; (2) source of action; (3) goals or norms
  that regulate interaction; (4) adaptivity, steering experience in light
  of the goals. The paper notes that Barandiaran et al. "combine
  normativity and adaptivity into one property". It is a reconstruction,
  not Barandiaran's three conditions (see Connections).
- **Agency is binary on this account**: a system has it if all four
  conditions hold. "Naturally there is room for developing a non-binary
  account."
- **Robustness to the definition is asserted, not shown**: "regardless of
  how the semantics of 'agent' or 'agency' are worked out, the need for
  frame dependence will remain."
- **The setting is input-output systems as RL models them.** The goal
  argument (Claim 3) is about inferring reward from behaviour.

## Key results

There are no theorems. The four claims, as stated (§2):

- **Claim 1 (individuality; adapted from Jiang 2019 and Harutyunyan
  2020).** "Nearly all agents admit many plausible boundaries one could
  draw that separates them from their environment. Moreover, key
  quantities of an agent can change depending on which boundary is
  chosen." Support: Bohr's stick, the extended mind, and Jiang's
  Proposition 10, that the optimal policy and Bellman error of an RL agent
  depend on where the agent-environment boundary is drawn.
- **Claim 2 (source of action; adapted from Kenton et al. 2023).** "There
  exist cases with at least two plausible choices of causal variables
  where the former choice identifies an agent in the causal model, and
  the latter choice refutes the presence of an agent in the causal
  model." Support: Kenton et al.'s own remark that discovering an agent
  "is relative to a frame – a choice of variables that appear in our
  causal model".
- **Claim 3 (normativity).** "For nearly all cases of input-output
  systems, whether that system is meaningfully goal-directed depends on a
  reference point whose choice is arbitrary." Support: every system can be
  described as if goal-directed (a broken thermostat that always sets
  20° "has the goal" of 20°); in inverse RL the zero reward is consistent
  with every behaviour (Russell 1998; Ng and Russell 2000), and reward is
  underdetermined by behaviour without intervention. Occam priors and
  maximum entropy rule some goals out, but they are themselves extra
  principles.
- **Claim 4 (adaptivity; adapted from Zadeh 1963 and Theorem 3.1 of Abel
  et al. 2023).** "For many input-output systems, there will exist at
  least two reference frames (and in most cases, many more) such that
  according to the first reference frame the system is adaptive, while
  according to the second, the system is not." Zadeh: "what matters is
  not whether [the system] is adaptive or not, but what ... it is
  adaptive [to]". A fixed policy is non-adaptive under one reference
  class of behaviour change and adaptive under another.
- **The conclusion.** "Since agency is simply the logical conjunction of
  these latter three properties conditioned on the choice of a boundary,
  then reaching a conclusion about agency itself must be made in
  reference to these commitments. In other words: agency is
  frame-dependent."
- **The reference frame** is "a collection of these four commitments":
  a boundary; "a reference object such as a set of causal variables"; "a
  principle for isolating whether the system is meaningfully pursuing a
  goal"; "a choice of what changes in behavior count as meaningful
  adaptation". A boundary "could be a cut in a graph (Jiang, 2019) or a
  Markov blanket (Friston et al., 2009)". A formal construction is left
  to future work.
- **Choosing a frame (§3).** "It is unclear which frame-selection
  principles are defensible". Dennett's intentional stance "could be
  formalised as a principle for selecting frames in terms of predictive or
  explanatory power". Frames are likened to Marr's levels and Dennett's
  stances.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Where the agent–environment boundary is drawn changes quantities such as the optimal policy and Bellman error | moderate | cited: Jiang (2019) Prop. 10, not reproduced |
| C2 | Whether a causal model contains an agent depends on the chosen variables | moderate | cited: Kenton et al. (2023), [LIT-909](../literature.d/LIT-909.md) |
| C3 | Goal-directedness inferred from behaviour needs an extra principle to rule out trivial goals | moderate | the inverse-RL underdetermination results, cited |
| C4 | Whether a policy is adaptive depends on a chosen class of meaningful behaviour change | moderate | cited: Zadeh (1963); Abel et al. (2023) Thm 3.1 |
| C5 | Attributions of agency on the four-part account are relative to a frame | weak | the conjunction of C1–C4, informal |
| C6 | The choices that make up a frame are arbitrary | weak | asserted; no argument that no choice is privileged |
| C7 | Any basic science of agency requires frame-dependence | weak | asserted in the abstract and §3; not argued beyond C5 |

## Concepts

- **Agency.** "A system's capacity to steer outcomes toward a goal."
- **Reference frame (agent reference frame).** The four commitments
  listed above, jointly sufficient to decide the four conditions.
- **Frame-dependent.** A property is frame-dependent when "reaching a
  conclusion about whether a given system possesses [it] requires an
  independent commitment whose choice is arbitrary".
- **Meaningful goal.** Not defined. The paper's point is that a
  definition requires a principle outside the system.

## Connections

It is a short gathering of earlier results under one name. Claim 2
rests on Kenton et al. ([LIT-909](../literature.d/LIT-909.md)), whose frame-relativity the record already
records in [CLAIM-174](../claims.d/CLAIM-174.md). The principle it floats for choosing frames,
predictive or explanatory power after Dennett (*The Intentional Stance*,
[LIT-430](../literature.d/LIT-430.md), held here unavailable; "True Believers", [LIT-398](../literature.d/LIT-398.md)), is what
Orseau et al. ([LIT-911](../literature.d/LIT-911.md)) formalise as an agent-versus-device comparison
under a prior.

**Its account of Barandiaran et al. is a reconstruction.** Barandiaran,
Di Paolo and Rohde ([LIT-566](../literature.d/LIT-566.md), read in [NOTE-458](NOTE-458.md)) give three
conditions (individuality, interactional asymmetry, normativity), not
four. Two of them are stated precisely so that no observer supplies
them. The system must distinguish itself from its environment "without
an observer", or explanation regresses through observers. Its norms are
set by its own organisation, and failure must be possible. Abel et al.
argue that *an observer's* boundary and *an observer's* goal attribution
are frame-relative. They do not engage the claim that an autonomous
system draws its own boundary and sets its own norms. So against
[THEORY-071](../theory.d/THEORY-071.md) the paper changes the subject rather than refuting it: it shows
that behavioural or observer-side tests of these conditions are
frame-relative, which Barandiaran et al. would grant.

## Bearing on the record

- **[QUESTION-032](../questions.d/QUESTION-032.md).** It supports the question's framing: agency asked
  "relative to a level of description and a target". It widens what the
  relativization must include. Beyond a level and a target, a frame
  fixes the causal variables, a principle for meaningful goals and a
  class of meaningful adaptations. It does not supply the test the
  question asks for, and gives no verdict on the thermostat ([CASE-044](../cases.d/CASE-044.md)):
  it uses the thermostat only to say that the verdict depends on the
  frame. It should carry no `answers` edge.
- **[CLAIM-174](../claims.d/CLAIM-174.md).** Its "What it does not say" already concedes that test 2
  inherits an observer-relative prior and test 3 Kenton et al.'s
  frame-dependence. This paper adds that test 3's verdict also depends on
  which changes count as adaptation (Claim 4). Kenton et al.'s
  intervention on "how its actions affect the world" is one such choice,
  not the only one. It also predicts that test 1's boundary, taken from
  coupling, is one more frame commitment, which is [CLAIM-152](../claims.d/CLAIM-152.md)'s caution
  in other words.
- **[CLAIM-194](../claims.d/CLAIM-194.md).** It agrees that coupling criteria cannot by themselves
  supply individuality. It goes further, holding that no boundary is
  observer-free, which [CLAIM-194](../claims.d/CLAIM-194.md) does not hold. [CLAIM-194](../claims.d/CLAIM-194.md) instead
  locates the line at self-production, the move Abel et al. do not
  address.
- **[THEORY-232](../theory.d/THEORY-232.md) (Watson, [LIT-990](../literature.d/LIT-990.md)).** The two are close. Watson's
  comparison of a whole's agency with its parts' is relative to a chosen
  decomposition and stipulated goals for the parts. Those are Abel et
  al.'s frame components (1) and (3). Watson concedes that relativity for
  one measure; Abel et al. argue that every account has it. Two
  differences:
  - Watson's measure is comparative and stays meaningful *within* a frame.
    Abel et al. say nothing against comparison within a frame.
  - [THEORY-232](../theory.d/THEORY-232.md)'s `promote_when` asks for an agency ranking stable across
    reasonable decompositions. Abel et al. predict no such stability *in
    general*, but they show no instance for Watson's measure, so the
    paper cannot settle that theory either way.
- **[THEORY-071](../theory.d/THEORY-071.md) and [THEORY-208](../theory.d/THEORY-208.md).** Against Barandiaran's absolute
  conditions, see Connections: the argument targets observer-side tests,
  not organisational closure. Against Floridi's level-of-abstraction-free
  permissiveness, it supplies the relativity Floridi leaves unstated.
- **[LIT-969](../literature.d/LIT-969.md)'s own filing text overstates it.** It says the paper addresses
  "every essential property of agency in Barandiaran's and Moreno's
  accounts". Moreno (2018) is cited as background and not analysed. And
  the paper takes no "direct position" on the thermostat, beyond saying
  that the verdict on it is frame-relative.
- **No new THEORY in the record holds the thesis.** It is filed from this
  reading as [THEORY-tmp8ntgq](../theory.d/THEORY-tmp8ntgq.md).
- No instruction for machine-learning practice; nothing for the
  anthology.

## Limitations

- **No definitions, no proof.** The authors say so and list both as future
  work.
- **Quantifiers drift.** Claim 2 is existential ("there exist cases"),
  Claim 4 says "many", Claim 3 "nearly all". The conclusion is
  universal ("any measurement of a system's agency must be made relative
  to a reference frame"). From existential premises it follows only
  that *some* attributions depend on the frame, not that all do. A system
  on which every plausible frame agrees is not ruled out.
- **"Arbitrary" is asserted.** That a choice is needed does not show that
  no choice is better. The paper itself floats predictive power as a
  principle of selection, which would make the choice principled.
- **The goal argument is about inference from behaviour.** It shows that
  behaviour underdetermines reward. It does not touch accounts on which
  goals are fixed by the system's organisation (Barandiaran) or by
  intervention (Kenton et al. use interventions, and Amin et al. 2017,
  which the paper cites, recover reward with them).
- **Each step is borrowed.** The four supporting results are cited, not
  reproduced, and this reading did not check them.

## Open questions

- A formal definition of a reference frame, and a proof that the four
  conditions are frame-dependent under it. The authors name this as
  the next step.
- Whether some systems are agents under every reasonable frame. A
  "frame-robust" core would make frame-dependence a matter of degree.
- Which frame-selection principle is defensible. Predictive power, as
  in Orseau et al., would turn the relativity into a model-comparison
  problem the record already has machinery for ([CLAIM-174](../claims.d/CLAIM-174.md) test 2).
