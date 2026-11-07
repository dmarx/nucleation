---
number: 354
status: Active
formerly:
- CLAIM-tmpilfhr
title: 'Freedom of will and autonomy come in degrees along several dimensions, among them viable reachability, control cost, robustness to disturbance, governance reconfigurability, revisability and motivational integration, and agents compare by inclusion of what they can viably reach under matched conditions: a partial order with incomparable pairs, not a scalar, and a gradient only of a declared measure'
version: 4
history:
- version: 2
  date: '2026-10-21'
  note: >-
    Note of 2026-10-21 added, from the exchange of 2026-10-20 on effective
    description, agency and legibility: A18's prisoner's dilemma gives a
    two-agent route to this claim's non-monotonicity, in which the shrinking
    of the set is imposed and not chosen. The claim is unchanged.
- version: 3
  date: '2026-11-04'
  note: >-
    Vocabulary only, under ADR-070: "endorse" in TERM-053's sense now
    reads conferral (TERM-103) or grant (TERM-101). The
    content is unchanged.
- version: 4
  date: '2026-11-06'
  note: >-
    At the status review's ruling (the owner delegated these rulings), at
    the twenty-seventh status review: THEORY-054 and THEORY-411 move from
    grounds to corroborated_by (ADR-058). The body cites self-determination
    theory as prior art for graded autonomy and as the source of the
    integration dimension, which the claim lists among others and whose
    content CLAIM-534 gives, and cites Sen's partial ordering as the same
    shape in another line; the argument is the reachable-set order on
    CLAIM-079, CLAIM-345 and CLAIM-025. Promoted (ADR-057): every premise is
    Active, no objection is filed, and nothing in the record meets the
    defeated_if, since empowerment (note of 2026-11-03, later) does not
    collapse the profile to a scalar and the robotics readings (note of
    2026-11-05) leave the order untested rather than refuted.
role: thesis
warrant: interpretive
defeated_if: >-
  A showing, in the model class the claim is applied to, that the
  dimensions are not separable: that one of them (say viable
  reachability) fixes the others, so that a single scalar defined from
  the dynamics alone, with no task or value fixing weights, agrees with
  every matched comparison the profile makes and leaves no pair
  incomparable. Or a showing that, under matched state, horizon, budget,
  disturbance class and viability set, the viable reachable sets of any
  two candidate agents are always nested. Not defeated by intuitions that
  one of two agents is plainly freer, nor by a scalar built for a
  declared task, which the claim allows.
tags:
- free-will
- self-governance
- agency
date: '2026-10-18'
line:
- will-organization
rests_on:
- CLAIM-079
- CLAIM-025
- CLAIM-345
grounds:
- THEORY-134
- THEORY-654
complements:
- CLAIM-128
- CLAIM-122
- CLAIM-027
- CLAIM-352
- CLAIM-410
summary: >-
  The owner's, U9 of the exchange of 2026-10-17: "controllability of a
  system isn't binary, and neither is sensitivity to perturbation", so
  can the account speak of "gradations (perhaps even gradients/spectra?)
  of freedom of will/autonomy". Worked out by A9 §3 and §7, A10 §7 and
  A15's central thesis. The dimensions vary separately, and comparison
  is by inclusion of viably reachable sets under matched conditions, a
  partial order, the shape [CLAIM-128](CLAIM-128.md) has in the transport line. The
  sharp edge: it does not measure metaphysical free will or
  responsibility, and reachable-set size is not monotone with autonomy,
  since a precommitment can shrink the set while making an endorsed
  project realizable.
---
<!-- inactive-ok-file: TERM-053 — Superseded by ADR-070 (conferral, TERM-103; grant, TERM-101); cited as the term of its time -->
<!-- inactive-ok-file: CLAIM-465 TERM-006 — Proposed, Deferred, Unavailable or new; cited from the exchange "Organizational Nucleation and SLT" of 2026-11-04 as open -->
<!-- inactive-ok-file: CLAIM-545 LIT-1614 — Proposed, Open, Deferred or Unavailable; cited from the exchange "Assess SDT Coverage" of 2026-11-02 as open, works registered unread among them -->
<!-- inactive-ok-file: THEORY-1280 CLAIM-527 — Proposed; the parent paper's agency, and the claim that separates its quantity -->

# CLAIM-354: Freedom of will and autonomy come in degrees along several dimensions, among them viable reachability, control cost, robustness to disturbance, governance reconfigurability, revisability and motivational integration, and agents compare by inclusion of what they can viably reach under matched conditions: a partial order with incomparable pairs, not a scalar, and a gradient only of a declared measure

## The claim

The owner, U9 of the exchange of 2026-10-17: "controllability of a system
isn't binary, and neither is sensitivity to perturbation. I'm wondering if
our account equips us to make concrete statements about gradations
(perhaps even gradients/spectra?) of freedom of will/autonomy".

The record held graded autonomy in one sense only: integration
([THEORY-054](../theory.d/THEORY-054.md), Ryan and Deci), and its own graded-ownership thesis, [CLAIM-016](CLAIM-016.md),
is Deferred with the `authenticity` line. Nothing in it graded control
authority by reach, cost or robustness. The owner's idea is new to the
record.

A9 §3 built the object. Given a set K of conditions the organization must
keep satisfying, R_T^K(s₀; E) is the set of states it can reach within
horizon T, staying in K, with control expenditure at most E. That is
[CLAIM-079](CLAIM-079.md) put to work: what counts is the viable alternatives, not the
stable ones. Then: "We can compare systems by **set inclusion** ... Under
matched states, costs, controls, and environmental conditions, that means
A has at least all of B's viable alternatives. But when reachable sets
overlap without containing one another, the systems are **incomparable**,
rather than one being objectively freer." And: "This gives us a partial
order of freedom, which seems much more defensible than a universal
ranking."

The dimensions vary separately, each for its own reason:

- **Viable reachability against control cost.** Equal controllability rank
  leaves the cost of a transition free ([CLAIM-345](CLAIM-345.md)). A9: a person
  "might genuinely be able to reorganize a habit, but the cognitive,
  social, emotional, or material effort needed could be prohibitively
  large."
- **Robustness to disturbance.** A9 §4: "an option available only when the
  environment cooperates is different from one the organization can
  reliably realize under resistance." The robust set asks for a policy
  that works against every admissible disturbance (∃π ∀w). [THEORY-654](../theory.d/THEORY-654.md) is a
  case on file: the LQR margins hold with the full state and are lost with
  an observer, so a plant can be controllable and observable and still
  fragile.
- **Governance.** A9 §4: "A remotely operated robot can have an enormous
  reachable state space while its actions are determined entirely by
  someone else." What is reachable is not what the organization's own
  governance can select ([CLAIM-027](CLAIM-027.md), [CLAIM-122](CLAIM-122.md)).
- **Revisability against reliable execution.** A9 §7: "strong habits can
  improve control economy while reducing revisability." That is [CLAIM-025](CLAIM-025.md)
  and [CLAIM-099](CLAIM-099.md): the operative regime, its governance and the capacity to
  transform it persist or fail separately.
- **Motivational integration.** Added by A15 §8.1, F = (R, C, V, G, I, E_f,
  R_v), from [THEORY-054](../theory.d/THEORY-054.md). A15 conceded what SDT already holds: "The novelty
  is **not** that autonomy comes in degrees."

A9 and A10 also list the efficacy of a higher-order attitude on
governance (A9's "endorsement efficacy", E_d). It is a candidate
dimension, an influence: A9, "It measures influence, not the normative
validity of endorsement."

On the owner's "gradients", A9 §8: a declared measure J(θ) of the viable
options has a gradient ∇_θ J, "But it wouldn't be an objective gradient of
free will. It would be the gradient of **a declared operational measure**,
under a declared model." A10 §7 the same: "It would not be an objective,
context-free gradient of metaphysical free will." So there is a gradient
once a task or value fixes the measure, and a profile, compared by
dominance, before one does.

The shape is on file in another line. [CLAIM-128](CLAIM-128.md) and [TERM-043](../terms.d/TERM-043.md): transport
profiles that trade off "are incomparable until a task fixes weights".
[THEORY-411](../theory.d/THEORY-411.md): Sen's approach "is deliberately incomplete and yields a partial
ordering". [QUESTION-115](../questions.d/QUESTION-115.md) has A12 of 2026-10-16 on individuation: "There
isn't yet a justified single scalar objective". This claim is the same
shape for freedom of will.

## What it does not say

- **Not metaphysical free will, and not responsibility.** A9's three senses:
  "Degrees of effective agency", "Degrees of autonomous governance", and
  "Freedom of will in the metaphysical sense". "The first two look amenable
  to quantitative characterization. They may help clarify the third, but
  they don't settle questions about determinism, moral responsibility, or
  ultimate sourcehood." The claim is about the first two. On Fischer and
  Ravizza ([THEORY-121](../theory.d/THEORY-121.md)), responsibility needs guidance control and not
  regulative control over alternatives, so a larger reachable set does not
  make a more responsible agent.
- **Not that more reachable is freer.** Inclusion orders one dimension.
  A11 §4: "A person who restricts access to a distraction might reduce
  immediate behavioral flexibility while increasing their ability to
  pursue an endorsed project." That is the reluctant writer ([CASE-013](../cases.d/CASE-013.md)).
  The precommitment shrinks the reachable set and lowers the cost and
  raises the robustness of the endorsed project. So the writer before and
  after are compared dimension by dimension, and may be incomparable.
  Reachable-set size is not monotone with autonomy.
- **Not conferral.** What the record called endorsement ([TERM-053](../terms.d/TERM-053.md)),
  now conferral ([TERM-103](../terms.d/TERM-103.md)), is any effect one process has on another's
  share of future influence, and it is not Frankfurt's. A9's "endorsement" is the
  reflective attitude. Here it is called higher-order volition.
- **Not that the dimensions are measured.** A9: "a Gramian is not
  automatically a meaningful psychological measure", and the profile's
  symbols "denote dimensions, not yet fully specified measurements."
- **Not that reachable states are valuable.** A11: "a control system's
  reachable states are not automatically valuable human opportunities."
  That is [CLAIM-352](CLAIM-352.md)'s point and [CLAIM-075](CLAIM-075.md)'s.
- **Not that K is the agent's own.** The comparison is relative to a
  viability set given from outside the dynamics ([THEORY-134](../theory.d/THEORY-134.md), [CLAIM-195](CLAIM-195.md)).
  Who fixes K is still open.
- **Not ownership.** Integration enters as one dimension. Whether a will is
  its own to a degree is [CLAIM-016](CLAIM-016.md)'s question, which stays Deferred.

## Note of 2026-10-21: a strategic route to non-monotonicity

A18 of the exchange of 2026-10-20 gave a strategic route to this claim's
non-monotonicity. In a prisoner's dilemma, with a rule enforcing
cooperation at (3, 3), removing the rule enlarges each player's action
set, and the unique equilibrium becomes (1, 1): "Expanded individual
action sets ⇏ Pareto-improved equilibrium outcomes". Checked. The sharp
edge already says precommitment can shrink the set and make an endorsed
project realizable. The PD is the two-agent form, in which the shrinking
is imposed and not chosen. That bears on autonomy, which this claim does
not settle. [CLAIM-410](CLAIM-410.md) uses the example.

## Note of 2026-10-31: "augmented ability to act" assumes a comparison this claim makes partial

The parent paper filed on this date defines agency by a transition "from
a lesser to an augmented ability to act" ([LIT-1902](../literature.d/LIT-1902.md), p. 1354;
[THEORY-1280](../theory.d/THEORY-1280.md)). That verdict assumes two abilities can be ranked. On
this claim they compare by inclusion, and pairs that overlap without
containment are incomparable. The paper's own case is one. In the MSF
meeting (pp. 1359–1363), MSF takes on an "ad hoc training program" it
first resisted ("[they] are not here as educators"), while declining
formal teaching (p. 1363). It gains a joint activity with the health
department. And by the paper's own account it may be "becoming a 'university'" (p. 1363), the direction
Robert had tried "to protect the organization from" (p. 1362). The paper
counts the outcome as transindividuation, "augmented ability to act" (p.
1362). Without a declared measure, this claim would class it as a
change, not an augmentation. [NOTE-1484](../notes.d/NOTE-1484.md) found the same gap
("Building augmentation into 'agency' makes a verdict depend on a
judgment of whose capacity counts"). This claim gives the reason in
general. [CLAIM-527](CLAIM-527.md) separates the quantity from valence and emotion.

No status, title or warrant changes.

## Note of 2026-11-02: what the profile lacks, and a corrected reachable set

In the exchange "Assess SDT Coverage" (2026-11-02) the replies rebuilt this claim three times without saying so: A16's
reachable set and Gramian, A21's "robust reachability" and A22's three
levels. Three points add to it.

- **Non-domination** (Pettit, [LIT-1614](../literature.d/LIT-1614.md)). An agent can be unfree because
  another holds an effective, unaccountable channel it never uses. The
  "governance" dimension, the remote-operated robot, covers actual external
  determination, not that counterfactual capacity. Formally it is the robust
  reachable set taken against an adversary class that includes the unused
  channel.
- **The allocation of control across channels, and its history** (A21 §8,
  A22 §3). A slow state that changes the agent's own gain, an outsider's and
  the noise gain makes susceptibility itself governable. That extends
  governance reconfigurability from what the agent can do to what can be
  done to it. The demonstrated part is [CLAIM-542](CLAIM-542.md).
- **A25 §7's reachable set of governance and legibility configurations**,
  ∃π_s ∀π_e. It ranges over every feedback policy. Against A25's own model
  it should range over the policies the current organization can carry out
  that read only what its legibility regime makes usable. Otherwise
  legibility drops out of the set.

A26 identified freedom with the whole profile under reflexive revision.
That is filed as [CLAIM-545](CLAIM-545.md), Proposed, resting on this claim. The claim
is unchanged.

## Note of 2026-11-03: legibility-limited policies, stated

This claim's note of 2026-11-02 said a reachable set should range over the
policies an organization can carry out on what it can read. Two
demonstrated claims from U30 to U33 of the exchange "Assess SDT Coverage" (2026-11-02) state it: [CLAIM-535](CLAIM-535.md) in
general (a policy acceptable everywhere exists exactly when the
circumstances an observation cannot separate share an acceptable action),
and [CLAIM-537](CLAIM-537.md) for tolerance-bounded compatibility. The motivational
integration this claim names is given a positive account in [CLAIM-534](CLAIM-534.md).

The claim is unchanged.

## Note of 2026-11-03 (later): empowerment and information, read

Empowerment (Klyubin et al. 2005, 2008; [NOTE-1511](../notes.d/NOTE-1511.md), [NOTE-1514](../notes.d/NOTE-1514.md)) is a
task-free number for perceivable reach, but it is open-loop, depends on the
horizon and ignores cost and viability, so it does not collapse this claim's
profile to a scalar. Its maxima in the cart-pole cannot be reached and held,
against what the agent can sustain ([CLAIM-079](CLAIM-079.md)). Ben-Tal et al.'s Table 2
([NOTE-1503](../notes.d/NOTE-1503.md)) is a quantitative case of legibility-limited policies: cost
34,583 with on-line information, 35,121 with past demands, infeasible with a
four-period delay or none.

The claim is unchanged.

## Note of 2026-11-04: restated without citation, from "Organizational Nucleation and SLT"

**What A26 restated.** The owner's U26 asked A to "synthesize the discussion". A26 gave four properties as distinct:
- compatibility;
- reachability, "the organization can attain it from its current state under the applicable constraints";
- viability, "the arrangement can be maintained over a relevant horizon without violating specified requirements";
- reconfigurability, "the organization can subsequently move to another appropriate arrangement when circumstances change".

It added that "acquiring authority and relinquishing authority are independently relevant capacities", citing [CLAIM-465](CLAIM-465.md). This claim already names viable reachability, governance reconfigurability and motivational integration as dimensions. [CLAIM-534](CLAIM-534.md) holds realizability, realization and maintenance, and [CLAIM-079](CLAIM-079.md) holds stability against viability. A26 cites none of them. A23 had drawn the same four properties, and [CLAIM-099](CLAIM-099.md) and [CLAIM-025](CLAIM-025.md) hold reconfigurability apart from viability. The exchange adds no new dimension.

**Endorsement, misread.**
- (a) A26 keeps only "Frankfurtian endorsement". It uses the record's sense unnamed, as "practical authority", and as E_t, "the relations through which processes affect one another's future authority".
- (b) Read as conferral ([TERM-103](../terms.d/TERM-103.md), formerly [TERM-053](../terms.d/TERM-053.md)), E_t is the conferral matrix E_ij, and a perspective's tolerance is its criterion for conferring influence ([CLAIM-552](CLAIM-552.md)). Frankfurt's sense is [TERM-102](../terms.d/TERM-102.md).
- (c) At U14 the owner asked whether the record's endorsement, now conferral, "satisfies the Frankfurtian sense". A14 itself answered that it does not.

A26's gloss of authenticity, "Non-dominating, answerable governance", leans on [TERM-006](../terms.d/TERM-006.md), which is Deferred. Its domination clause is this claim's non-domination profile and [CLAIM-545](CLAIM-545.md)'s. The claim is unchanged.

## Note of 2026-11-05: the constraint-architecture readings

The pasted synthesis on constraint architectures glosses the claim's dimensions as "several independently variable dimensions"; the claim does not say independent, and what it asserts is a partial order by inclusion of what is viably reached. Three robotics readings support it in kind. Murray and Sastry ([NOTE-1622](../notes.d/NOTE-1622.md)) separate what is admissible instantaneously from what is reachable, though with no state constraints they are silent on viability. Dollar and Howe ([NOTE-1575](../notes.d/NOTE-1575.md)) show robustness to disturbance and actuated reach coming apart, for power grasps only: an underactuated hand commands fewer shapes yet grasps more reliably under positioning error. Liu, Zhang and Fang ([NOTE-1558](../notes.d/NOTE-1558.md)) show actuated reach trading against the number of actuators, with diminishing returns. None compares agents by inclusion, so the order itself is left untested. No status changes.

## Note of 2026-11-05: A's resource models and further distinctions

A lists four spaces, the instantaneously admissible directions, the states reachable over a horizon, the viable directions and policies, and the transformations accessible at acceptable cost, and says "These are not interchangeable." The claim already joins the last three in its viable reach under a cost bound; the instantaneous space is not one of its dimensions, and [CLAIM-589](CLAIM-589.md) shows it is no bound over a horizon. [CLAIM-582](CLAIM-582.md) explains why a precommitment can help under the claim: the set a constraint shrinks is one of existence, while what it can improve must hold whatever a distraction does. No status changes.
