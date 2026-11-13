---
status: Proposed
title: 'Two forms of support that give a party the same capabilities now can leave it different capabilities later: where capacity is learned by doing and decays with disuse, support that does the work shrinks what the party can reach unaided while support that covers only its shortfall does not, so support, or a technology, cannot be ranked by present capability sets and has to be assessed by the capability trajectory it produces'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation: in CLAIM-605's model (dC/dt = λPC(1 − C) −
  μC, λ = 1, μ = 0.3, τ = 1.5), a party at C = 0.7 under full substitutive
  support and under capacity-first support does not have the same
  delivered functioning and the same unaided capability at t = 0, or does
  not have different unaided capability at t = 5 (C = 0.156 against 0.7)
  and after withdrawal (0 against 0.7). Or an argument that the capability
  approach's capability set already includes the person's later sets, so
  that evaluating it at a time is not evaluating it as a snapshot. Not
  defeated by evidence that a given technology does not deskill its
  users, which bears on whether the model applies (CASE-tmpf71w4), not on
  the derivation.
tags:
- society-and-governance
- well-being
- complex-systems
date: '2026-11-13'
line:
- transient-support
- will-organization
rests_on:
- CLAIM-605
- CLAIM-352
bears_on:
- QUESTION-398
summary: >-
  A's, from the exchange "Analyze technological civilization trap"
  (2026-11-13): A17 §V ("A technology can increase what someone
  accomplishes today while reducing what they will be capable of
  accomplishing tomorrow"; "We should investigate how particular forms of
  assistance change the person's future capability trajectory") and A23
  §6 ("We therefore need to evaluate capability trajectories, not merely
  present capability sets"), joining [CLAIM-605](CLAIM-605.md)'s capability trap to Sen's
  capability approach as [CLAIM-352](CLAIM-352.md) reads it. The record holds the
  dynamics ([CLAIM-605](CLAIM-605.md)) and the reading of Sen ([CLAIM-352](CLAIM-352.md)), not the
  consequence for evaluating support. The derivation is checked here in
  [CLAIM-605](CLAIM-605.md)'s own model. The model is illustrative; A17 itself says it is
  "not empirical evidence that a particular technology produces such
  decline", and the proposed study is [CASE-tmpf71w4](../cases.d/CASE-tmpf71w4.md). The wording is A's;
  adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-tmpm76rc THEORY-tmp8m1e4 THEORY-tmpnm1gx THEORY-tmpyot08 THEORY-tmpt34ma THEORY-343 — Proposed; cited with its standing -->
<!-- inactive-ok-file: ARG-tmpar7tl THEORY-tmpa59p3 THEORY-tmpiihve THEORY-tmpj32pb THEORY-tmpo67z2 THEORY-tmpockqy THEORY-tmpt6mee THEORY-tmpwsjea THEORY-tmpzibpi — filed from the exchange "Analyze technological civilization trap" or its readings of 2026-11-13, Proposed -->
<!-- inactive-ok-file: LIT-2225 until 2027-05-13 — Unfetched; Bainbridge's paper, cited with its standing as unread; asked again by that date whether a lawful copy is reached -->
<!-- inactive-ok-file: THEORY-tmpoxssh THEORY-tmpww16o — filed from the readings of 2026-11-13, Proposed -->
<!-- inactive-ok-file: CLAIM-603 — Proposed; the record's claim on division of labour, cited with its standing -->
<!-- inactive-ok-file: CASE-tmpf71w4 — filed from the same exchange, Proposed -->
<!-- inactive-ok-file: NOTE-tmp8ceuj — filed from the readings of 2026-11-13, Skimmed; Illich, a two-page excerpt -->

# CLAIM-tmp6wuql: Two forms of support that give a party the same capabilities now can leave it different capabilities later: where capacity is learned by doing and decays with disuse, support that does the work shrinks what the party can reach unaided while support that covers only its shortfall does not, so support, or a technology, cannot be ranked by present capability sets and has to be assessed by the capability trajectory it produces

## The claim

A17 §V, reading [CLAIM-605](CLAIM-605.md) against A's earlier use of Sen:

> **A technology can increase what someone accomplishes today while
> reducing what they will be capable of accomplishing tomorrow.**
>
> The capability set is dynamic.
>
> This deepens Sen's approach.

A23 §6 put it as a rule of evaluation: "We therefore need to evaluate
**capability trajectories**, not merely present capability sets."

## The derivation

Take [CLAIM-605](CLAIM-605.md)'s model as it stands: demand 1, the party's output τC,
dC/dt = λPC(1 − C) − μC, with λ = 1, μ = 0.3, τ = 1.5. Start a party at
its kept state, C = 0.7, where its unaided output is min(1.05, 1) = 1.

- **Under full substitutive support** (the support does all the work, P =
  0), the demand is met in full, by the support.
- **Under capacity-first support** (P = min(τC, 1)), the demand is met in
  full, by the party, and the support supplies nothing.

At t = 0 the two are the same in every respect a capability set records:
the same functioning delivered (the demand met), and the same set of
functionings the party could reach unaided (C = 0.7). By t = 5 they are
not. Under substitution C = 0.7e^(−1.5) = 0.156, below [CLAIM-605](CLAIM-605.md)'s
threshold of 0.276, with unaided output 0.23; under capacity-first support
C stays 0.7. Withdraw both supports at t = 5 and let sixty units pass:
the first party's capacity goes to 0, the second's stays at 0.7
(recomputed for this filing by Euler integration in `python3 -I`).

So an evaluation that compares the two supports by the capability sets
they leave at the moment of comparison cannot tell them apart at t = 0,
though one of them removes a capability the party has and the other
keeps it. [CLAIM-352](CLAIM-352.md) reads Sen's opportunity aspect as viable reachability
mapped to valued functionings; the reachable set itself moves under the
support, so the opportunity aspect has to be read along the trajectory.

## What it does not say

- Not that any actual technology deskills its users. The model is
  [CLAIM-605](CLAIM-605.md)'s toy, and A17 §IX says so: "the fact that assistance can
  diminish capacity in a particular dynamical model does not establish
  that AI assistance generally diminishes human competence." Whether
  capacity in a real skill is learned by doing, decays with disuse and
  needs capacity present to grow is the question [CASE-tmpf71w4](../cases.d/CASE-tmpf71w4.md) would test.
- Not that substitution is wrong. A17: "Automating dangerous or exhausting
  work may be overwhelmingly beneficial", and [CLAIM-603](CLAIM-603.md) holds that a
  capability given up for reliable supply can be a division of labour.
  The claim is about what an evaluation must look at, not its verdict.
- Not that Sen ignores time. Whether his framework already evaluates
  capability over a life is a question for a reading of Sen's own works
  (registered unread from this exchange), not settled here.

## Note of 2026-11-13: the readings of 2026-11-13

Readings of 2026-11-13 and a recheck.

- **Gardner** ([THEORY-tmpo67z2](../theory.d/THEORY-tmpo67z2.md)): finds Sen's preference for capability over achievement unargued. That is contested support for this claim's framing in Sen's terms; [ARG-tmpar7tl](../arguments.d/ARG-tmpar7tl.md) argues the derivation stands, since the two supports diverge in achieved functionings too. The claim keeps its conclusion; "capability trajectory" should be read as the trajectory of what the party can reach and achieve.
- **Sen**, Development as Freedom ([THEORY-tmpockqy](../theory.d/THEORY-tmpockqy.md)): unemployment has "far-reaching debilitating effects on individual freedom, initiative, and skills" [OCR-normalized] that income support does not make up: support that replaces an outcome, not the activity. Corroborates the premise. The Tanner Lectures ([THEORY-tmpj32pb](../theory.d/THEORY-tmpj32pb.md)) evaluate the capability set at a time; nothing read argues the set includes later sets, the claim's named defeater.
- **Vallor through Adewuyi** ([THEORY-tmpt6mee](../theory.d/THEORY-tmpt6mee.md)): moral deskilling under reliance on algorithmic decision; second-hand. Corroborates the premise.
- **Crawford 2006** ([THEORY-tmpiihve](../theory.d/THEORY-tmpiihve.md)): "the degradation of work is ultimately a cognitive matter", judgment moved out of the job; corroborates the premise at the level of occupations.
- **Feenberg** ([THEORY-tmpa59p3](../theory.d/THEORY-tmpa59p3.md)): the economic code "rewards deskilling"; corroborates the premise at the level of economic codes.
- **Rosa through Susen** ([THEORY-tmpzibpi](../theory.d/THEORY-tmpzibpi.md)): qualifies the evaluative measure from outside. "access to resources is a necessary but not sufficient condition for human fulfilment"; a capability set, even as a trajectory, measures options, not the quality of a person's relation to what they do. The derivation is untouched.
- **Benjamin**, Imagination ([THEORY-tmpwsjea](../theory.d/THEORY-tmpwsjea.md)): a capacity widespread in children declining under arrangements that do not exercise it; weak and second-hand, no relation.
- **Recheck: readings the first search missed.** The record already held the premise's best evidence: Ahn's reading of Bainbridge's ironies of automation ([THEORY-1522](../theory.d/THEORY-1522.md), read in [NOTE-1713](../notes.d/NOTE-1713.md) from [LIT-2222](../literature.d/LIT-2222.md)), that automation leaves the operator's skills "degraded from disuse"; Bainbridge's paper itself ([LIT-2225](../literature.d/LIT-2225.md)) is Unfetched. [THEORY-1522](../theory.d/THEORY-1522.md) now corroborates this claim. [NOTE-1612](../notes.d/NOTE-1612.md) (Oskar et al., procedural skill decay in emergency medicine; [THEORY-1404](../theory.d/THEORY-1404.md)) is the clinical evidence for decay with disuse that [CLAIM-558](CLAIM-558.md) holds; it bears on whether [CLAIM-605](CLAIM-605.md)'s model applies to people, the question [CASE-tmpf71w4](../cases.d/CASE-tmpf71w4.md) asks.

## Note of 2026-11-13: Marcuse and Illich, read

- **Illich, Tools for Conviviality, a two-page excerpt** ([THEORY-tmpww16o](../theory.d/THEORY-tmpww16o.md),
  [NOTE-tmp8ceuj](../notes.d/NOTE-tmp8ceuj.md)). Corroborates the distinction the claim turns on, not its
  derivation: "People need new tools to work with rather than tools that
  “work” for them" is capacity-first against substitutive support, and
  Illich says what substitution costs: "As the power of machines
  increases, the role of persons more and more decreases to that of mere
  consumers"; people need "the freedom to make things among which they
  can live". The excerpt says nothing of capacity decaying with disuse,
  so it gives no dynamics; [THEORY-tmpww16o](../theory.d/THEORY-tmpww16o.md) carries `corroborates` for the
  distinction only.
- **Marcuse, One-Dimensional Man** ([THEORY-tmpoxssh](../theory.d/THEORY-tmpoxssh.md), [NOTE-tmpf1tpw](../notes.d/NOTE-tmpf1tpw.md)). Leaves
  it open, with weak support for the motivation: needs that include
  "enjoying freedom from using the brain" (ch. 9), man "perhaps more
  powerless over his own apparatus than he ever was before" (ch. 9), and
  the worker's lost "professional autonomy" (ch. 2). No model and no
  dynamics; nothing bears on the derivation. No relation.

## Note of 2026-11-13: stand-ins, read

- **Vallor, CyCon 2013** (THEORY-tmpm76rc, NOTE-tmpgn1lo), read in full as a stand-in for her 2015 paper and for The AI Mirror. Corroborates the premise first-hand, where Adewuyi (THEORY-tmpt6mee) gave it second-hand. Virtue "presupposes repeated practice and development of skills of moral analysis, deliberation and action", which automation can make redundant "with a resulting devaluation and/or loss of these skills". She draws the claim's consequence in her own terms: the loss "would not be rendered insignificant by the emergence of machines that produce equivalent, or arguably even better outcomes", so equal present outcomes do not settle the evaluation. "Whether any automated technology produces deskilling, then, is an empirical question that depends upon the particular context of use" matches the claim's own scope (not defeated by a technology that does not deskill). Her remedy, automation only where human judgment is "consistently and gravely inadequate" and machines used for upskilling, is capacity-first support in practice. Her supervisor's paradox ("An expert supervisor of another’s decision, in order to be worthy of the authority to override it, must have acquired expertise in making decisions of the very same or a similar kind") is the hand-back in THEORY-1522, Ahn on Bainbridge, in ethics: two independent statements of one structure.
- **The recheck the reader flagged.** THEORY-1522 already corroborates this claim. NOTE-1612 (procedural skill decay in emergency medicine) is the empirical side of the decay premise; Vallor's "empirical question" is why CASE-tmpf71w4 is needed, and NOTE-1612 is the kind of evidence it would add to. THEORY-343 (laboratory offloading lowers memory for what was offloaded) is about memory, not a skill kept by practice; it bears on the premise only by analogy. No relation from either.
- **Crawford, the 2017 interview** (THEORY-tmp8m1e4) and **Dijkema's review** (THEORY-tmpnm1gx): support in spirit. "as we do not need our skills and brains to move in our environment, companies have more of our brain to exploit" names skill made unnecessary, as a premise about attention; Dijkema's "competence rests on an apprehension of real features of the world" is what substitution removes. No dynamics; no relation.
- **Illich, Energy and Equity** (THEORY-tmpyot08): at a level of compulsory instruction "learning by seeing and doing declines", the capacity-by-doing premise in schooling. No dynamics; no relation.
- **Vallor's Noema essay** (THEORY-tmpt34ma): AI for "the most meaningless tasks in our lives" is a rule for which tasks to hand over, not a trajectory. No relation.
