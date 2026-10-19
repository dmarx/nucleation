---
number: 324
status: Active
formerly:
- THEORY-tmpxwn52
title: 'A system adapts by trial and error to an environment whose effect on its essential variables it does not know only if a second feedback, through those variables, changes the parameters of its primary feedback; and if that feedback changes them whenever, and for as long as, an essential variable is outside its limits, every equilibrium the whole can reach is an adapted one'
version: 2
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Narrowed and promoted at the owner's direction, carrying out the
    promotion audit's decision for THEORY-324 (batch 032, ADR-047 v2).
    Ashby's two deductions were re-derived step by step, in the dated
    note below, which is the second reader's check the promote_when
    asked for. The title now says the parameters change whenever, and
    for as long as, an essential variable is outside its limits. A jump
    only on leaving the limits can settle in a field whose equilibrium
    lies outside them, which was the promote_when's second refuter. The
    unknown environment is now stated as Ashby states it: one whose
    effect on the essential variables the system does not know. The
    promote_when's wider form, any system that comes to keep its
    essential variables within limits, moves to QUESTION-tmpvx6hf.
tags:
- complex-systems
- behavioral-integration
- learning-and-conditioning
date: '2026-10-14'
source:
- LIT-787
summary: >-
  Ashby (1952; 2nd ed. 1960), [LIT-787](../literature.d/LIT-787.md), read in [NOTE-851](../notes.d/NOTE-851.md). Necessity is
  deduced from the trial-and-error rule against a Black Box environment;
  sufficiency from the theorem that a whole is at equilibrium only where
  every part is. The Homeostat shows it in a four-unit linear machine.
  The parameter changes are blind, and the account says nothing about how
  long the search takes, which is the subject of [THEORY-307](THEORY-307.md).
supports:
- CLAIM-339
- CLAIM-342
---
<!-- inactive-ok-file: THEORY-307 THEORY-217 THEORY-153 — Proposed; the companion account and the accounts that use Ashby's terms, open -->

# THEORY-324: A system adapts by trial and error to an environment whose effect on its essential variables it does not know only if a second feedback, through those variables, changes the parameters of its primary feedback; and if that feedback changes them whenever, and for as long as, an essential variable is outside its limits, every equilibrium the whole can reach is an adapted one

## Source

Ashby, *Design for a Brain* (2nd ed., 1960), [LIT-787](../literature.d/LIT-787.md), read in
[NOTE-851](../notes.d/NOTE-851.md): Ss. 5/8, 6/8–6/9, 7/2–7/26 and Ch. 8, with the formal
statement in S. 22/6.

## What was actually shown

**Adaptation as stability.** Behaviour is adaptive if it "maintains the
essential variables … within physiological limits" (S. 5/3), which is
stability of the organism–environment system in the region where they
stay within limits (S. 5/8).

**Necessity (Ss. 7/4–7/8).** If the reacting part does not know how the
environment acts on the essential variables, only trial and error can find
out. The rule "if the trial is unsuccessful, change the way of behaving;
when and only when it is successful, retain the way of behaving" requires
that the parameters of the reacting part be unsettled exactly when an
essential variable is outside its limits. So there must be a channel from
the essential variables to those parameters, "formally identical
(isomorphic)" in any adaptive system, living or mechanical (S. 7/8).

**Sufficiency (S. 7/11).** A whole is at equilibrium only where every part
is (S. 6/8). The parameter system is at equilibrium only when the
essential variables are within limits. So every equilibrium of the whole
is adapted, whatever the reacting part's construction and however the new
parameter values are drawn, "at random" included (S. 7/25).

**Demonstration (Ch. 8).** The Homeostat, four magnets coupled through
uniselector-set weights drawn from random-number tables, recovers
stability after an operator reverses a connection, by finding a
compensating reversal, and adapts to a constraint it was not built for.

What could have failed: the veto argument needs the parameter system to be
at rest only within limits; a machine built otherwise (S. 8/13) seeks the
wrong goal, which the Homeostat with mis-set relays would show.

## What this does not say

- **Not that adaptation is fast.** The search is blind. Ashby's own
  calculation (S. 11/2) gives 2¹⁰⁰ trials for 100 independent essential
  variables. How it becomes practicable is [THEORY-307](THEORY-307.md).
- **Not that the step-mechanisms choose.** They change "at random" and
  are kept only if the essential variables do not veto them. The second
  feedback alters the parameters of regulation without directing the
  alteration.
- **Not that the brain is a Homeostat.** Ashby says of the step-mechanisms
  "we have at present practically no idea of where to look" (S. 9/4), and
  that the ultrastable form is "only one of a large class of related forms"
  (S. 7/26).
- **Not about environments the repertoire cannot meet.** With no stable
  configuration available, an ultrastable system, like an organism, fails
  (S. 8/11).
- **Necessity holds under the stated case.** Where the reacting part
  already knows how the environment acts on its essential variables, or
  can act on them directly, the deduction does not apply (Ss. 7/3–7/4).

## Connections

- **[THEORY-217](THEORY-217.md)** (Barandiaran) uses Ashby's essential variables and
  regime switches; its "second-order regulation that shifts the system to
  another regime" is this account's second feedback, and its claim that
  malfunction needs no second order of norms is compatible with Ashby,
  whose second feedback is a mechanism, not a norm.
- **[THEORY-153](THEORY-153.md)** (Beer) rests its regulation on Ashby's law of requisite
  variety, which Ashby applies to the ancillary regulations (S. 17/13).
- **[THEORY-134](THEORY-134.md).** Viability theory takes the constraint set as given;
  Ashby likewise takes the essential variables and their limits from the
  species (S. 3/14).

## Note of 2026-10-19: the two deductions, re-derived

Take the whole as a state-determined system with four blocks of
variables: environment E, reacting part R, essential variables V and the
parameters S of R. Its transition is x' = F(x), with one component map
per block. R acts on V only through E and does not know how E is coupled
to V (Ss. 7/3–7/4). A state is adapted when every essential variable is
within its limits there (S. 5/8).

**Sufficiency.** x is an equilibrium of the whole iff F(x) = x, which
holds iff each component map leaves its own block fixed at x, given the
other blocks' values there. That is the veto (S. 6/8), and it needs
nothing beyond state-determinacy. If S changes at every state where some
essential variable is outside its limits, then at an equilibrium, where S
does not change, every essential variable is within its limits. This
holds whatever R's construction and however the new values of S are drawn
(S. 7/25). If no configuration of S is stable, the whole has no
equilibrium and the statement is vacuous (S. 8/11). The condition must
hold for as long as V is outside, as in the Homeostat, whose relay stays
closed and keeps advancing the uniselector while a needle is past its
limit (S. 8/2). A step-mechanism that jumps only on crossing out of the
limits can land in a field with an equilibrium outside them and then stay
there.

**Necessity.** S depends on V, in Ashby's operational sense (S. 12/3), if
two states differing only in V can be followed by different values of S.
The trial-and-error rule (S. 7/7) keeps the way of behaving, which S sets
(S. 6/3), when the trial succeeds, and changes it when it fails. Success
is judged by V. Take two states that agree in E, R and S, with V within
its limits in one and outside in the other. Such pairs exist, because V
is a coordinate of its own, whenever V can leave its limits at all. The
rule keeps S in the first and changes it in the second. So S depends on
V, and there is a channel from V to S, direct or through intermediates.
With S → R → E → V, this closes a second loop beside the primary R ⇄ E.
The deduction fixes no form for the loop, which is why Ashby calls the
ultrastable form "only one of a large class of related forms" (S. 7/26).
Once the rule is assumed, the necessity is close to definitional. A
regulator whose one fixed setting is stable in every environment of the
class needs no such channel, but it does not adapt by trial and error.
Whether systems that do need different settings can do without the
channel is [QUESTION-tmpvx6hf](../questions.d/QUESTION-tmpvx6hf.md).
