---
number: 404
status: Active
formerly:
- THEORY-tmp0bflx
title: "With a common prior, a sender who commits to a signal the receiver observes can induce any distribution of posteriors whose mean is the prior, so an openly designed experiment moves a fully informed Bayesian receiver whenever the concave closure of the sender's value lies above its value at the prior; at the optimum, under the paper's tie-breaking, the receiver is certain when she takes the sender's worst action and indifferent when she takes another"
version: 2
history:
- version: 2
  date: '2026-10-21'
  note: >-
    Note of 2026-10-21 added, from the reading of Bergemann and Morris
    (NOTE-1034): THEORY-844 is this result's many-player
    generalization with information of the receivers' own. The account is
    unchanged.
tags:
- game-theory
- epistemology
- information-theory
date: '2026-10-16'
source:
- LIT-1021
summary: >-
  Kamenica & Gentzkow (2011), [LIT-1021](../literature.d/LIT-1021.md), read in [NOTE-717](../notes.d/NOTE-717.md) with the proofs.
  Proved results (Proposition 1, Corollary 2, Propositions 4 and 5) for a
  single ideal Bayesian receiver, a finite state space, commitment and
  sender-preferred tie-breaking. A judge who knows the investigation was
  designed to convict convicts 60 percent of defendants when 70 percent
  are innocent. The paper does not analyse manipulation, does not compute
  the receiver's welfare and does not cite Blackwell.
supports:
- CLAIM-404
---
<!-- inactive-ok-file: THEORY-414 — Proposed; a sibling account filed in the same batch, named in Connections and not leaned on -->
<!-- inactive-ok-file: THEORY-235 THEORY-040 — Proposed; accounts of manipulation and present structure named as neighbours, not leaned on -->

# THEORY-404: With a common prior, a sender who commits to a signal the receiver observes can induce any distribution of posteriors whose mean is the prior, so an openly designed experiment moves a fully informed Bayesian receiver whenever the concave closure of the sender's value lies above its value at the prior; at the optimum, under the paper's tie-breaking, the receiver is certain when she takes the sender's worst action and indifferent when she takes another

## Source

Emir Kamenica and Matthew Gentzkow (2011), "Bayesian Persuasion",
*American Economic Review* 101(6):2590–2615, [LIT-1021](../literature.d/LIT-1021.md), read in full in
[NOTE-717](../notes.d/NOTE-717.md), with Appendix A's proofs. The online Appendix was not read.

## What was actually shown

**Setting.** A common prior μ₀ in the interior of Δ(Ω), Ω finite; a compact
action set with at least two actions; continuous payoffs. Sender chooses a
signal π; Receiver observes π and its realization, which is reported
truthfully. "This makes our environment effectively nonstrategic." No
transfers. When Receiver is indifferent she takes the action Sender
prefers.

**Proposition 1.** For a value v*, these are equivalent: some signal has
value v*; some straightforward signal (realizations are recommended
actions, which Receiver follows) has it; some distribution of posteriors τ
with mean μ₀ has E_τ v̂(μ) = v*. Bayes plausibility is "the only
restriction on the equilibrium distribution of posteriors". The proof
constructs the signal: π(s | ω) = μ_s(ω) τ(μ_s) / μ₀(ω).

**Corollary 2.** With V the concave closure of v̂, the optimal value is
V(μ₀), and Sender gains iff V(μ₀) > v̂(μ₀). An optimum exists because the
tie-breaking makes v̂ upper semicontinuous. If v̂ is concave, no disclosure
is optimal at every prior; if convex and not concave, full disclosure is
(Remark 1).

**The judge.** Prior Pr(guilty) = 0.3; the judge convicts iff her posterior
is at least 0.5. The unique optimum gives posteriors 0 (weight 0.4) and 0.5
(weight 0.6): conviction with probability 0.6, against 0 with no
information and 0.3 with full information. The judge "is fully aware that
the investigation was designed to maximize the probability of
conviction". [NOTE-717](../notes.d/NOTE-717.md) redid these numbers.

**Propositions 4 and 5.** If an optimal signal induces a belief leading to
Sender's worst action, Receiver is certain there. Under Assumption 1 and a
strict gain, at an interior induced belief Receiver's preference is not
discrete: with finite actions she is indifferent between two.

**Alignment (Section IV).** More aligned preferences weakly raise Sender's
optimal value but can lower the gain, and can make the optimal signal less
informative.

**What could have come out otherwise.** The receiver's knowledge of
the design could have undone its effect. It does not, because each
posterior is correct given the signal. The NBER version adds that if Sender chose covertly, the only
equilibrium would be full disclosure.

## What this does not say

- **That this is manipulation.** The word appears once, for Sender's aim.
  The paper's taxonomy has incentives and persuasion, "anything which
  changes beliefs", and no third kind. Definitions that require
  covertness ([LIT-1002](../literature.d/LIT-1002.md), as [QUESTION-070](../questions.d/QUESTION-070.md) summarises it) would exclude this
  case, since the design is overt.
- **That the receiver is harmed.** The paper computes no welfare. On the
  record's arithmetic ([NOTE-717](../notes.d/NOTE-717.md)), the judge reaches a just verdict with
  probability 0.7 under the optimum, exactly as with no information and
  below the 1.0 of full information; in the product example the consumer
  gets her outside option either way and the firm takes "all the consumer
  surplus". So whether she is harmed depends on the baseline.
- **That it holds for real receivers.** Every result needs an ideal
  Bayesian with a common prior. The paper reads systematic harm to
  receivers as a sign that "limited rationality may be at play"; that is
  one sentence of its Conclusion, not a theorem.
- **That it holds without commitment or with several receivers.** The
  sender must commit and the receiver must observe the signal. Receivers
  who care about each other's actions and get private signals are outside
  the method.
- **Anything about Blackwell's order.** Blackwell is not cited. The paper
  redefines the state as "the realization of the most informative signal
  Sender can generate", so every signal is a garbling of full information,
  the optimum included. What the result does show is that the party who
  chooses the experiment can strictly prefer a less informative one, which
  Blackwell's ranking for the decider does not forbid ([NOTE-717](../notes.d/NOTE-717.md)).
- **That the indifference signature is general.** It is proved for finite
  actions under Assumption 1. Whether a third party could test for it more
  widely is open.

## Connections

- **[QUESTION-071](../questions.d/QUESTION-071.md)** asks whether a will can be manipulated with nothing in
  its present structure showing it. This is a different case, which the
  question does not yet name: influence that is fully visible and still
  effective, because each step of the receiver's inference is sound. It
  also leaves a present trace, a posterior exactly on a decision boundary.
  It concerns beliefs and actions, not will, so no `answers` edge is filed.
- **[QUESTION-070](../questions.d/QUESTION-070.md).** The sender is any optimiser of a payoff, and several of
  the paper's examples are institutional procedures (grading, ratings,
  performance reviews). That a selected procedure would act the same is
  the record's inference ([LIT-1021](../literature.d/LIT-1021.md), Standing). The paper does not say
  whether this is a wrong.
- **[THEORY-235](THEORY-235.md)** says covert influence exploiting decision-making
  vulnerabilities harms autonomy by making the person opaque to herself.
  Here the influence is overt and exploits no vulnerability; the receiver
  is ideal.
- **[CLAIM-050](../claims.d/CLAIM-050.md)** says what fidelity is for a receiver. This result is a
  reason not to assume that whoever chooses the rendering procedure wants
  the most informative one.
- **Rules in equilibrium** ([THEORY-414](THEORY-414.md)) uses correlated equilibrium,
  where a public signal tells each player what to do. Here a committed
  signal does the same for one receiver, chosen by an interested party.
  The pairing is the record's.

## Note of 2026-10-21: the many-player generalization

Bergemann and Morris's survey of information design ([LIT-1313](../literature.d/LIT-1313.md)), read
on 2026-10-21 in its accepted manuscript ([NOTE-1034](../notes.d/NOTE-1034.md)), generalizes this
result to many receivers with information of their own: an omniscient
designer can attain exactly the Bayes correlated equilibria, and a
receiver's own information bounds what can be induced ([THEORY-844](THEORY-844.md)).
With one uninformed receiver the obedience constraints reduce to this
account's. The account is unchanged.
