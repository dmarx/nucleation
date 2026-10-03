---
number: 71
status: Proposed
formerly:
- THEORY-tmplg7y1
promote_when: >-
  The test the authors set for their own definition: measures of
  individuality (closure) and of normativity, plus a criterion of
  interactional asymmetry that does not depend on how the modeller splits
  parameters from variables, applied almost mechanically to explicit
  models. A protocell model, an evolved robot controller and a
  homeostat should all go through the same procedure, and the verdicts
  should match the cases of Table 1 of LIT-566 without being tuned
  to them. Such a result would promote the account. It is refuted by a
  system that meets all three conditions and is plainly not acting, which
  the authors say they cannot conceive of, or by a clear case of action
  that lacks one of them: action whose regulating norm cannot be traced to
  the acting system's own organisation, or action by a system whose
  boundary only an observer draws. What cannot settle it: more intuitive
  cases chosen to fit the conditions, since the definition was built
  from such cases; how "agent" is used in machine learning or economics,
  which is a different and thinner notion; or the bare assertion that
  some designed system is, or is not, an agent.
title: 'Minimal agency requires individuality, interactional asymmetry and self-generated normativity, and individuality without the other two is not agency'
version: 1
tags:
- agency
- individuation
- philosophy-of-biology
- embodied-cognition
date: '2026-10-03'
source:
- LIT-566
summary: >-
  Barandiaran, Di Paolo & Rohde (2009), [LIT-566](../literature.d/LIT-566.md), read in
  [NOTE-458](../notes.d/NOTE-458.md). The three conditions are that the system distinguishes
  itself from its environment with no observer doing it, that it is the
  active source of modulations of its coupling with the environment, and
  that it regulates that coupling against norms its own organisation
  sets. Each is necessary, and together they are claimed to be
  sufficient. Individuality is the precondition of the other two and
  does not suffice. A cell in passive osmosis, a kitten warmed by its
  mother and a person with a Parkinsonian tremor are each individuals,
  and none of them is acting. The generative definition is an open
  autonomous organisation that adaptively modulates its coupling so as
  to maintain itself. Here "autonomy" and "self" mean organisational
  closure. They do not mean a subject or self-governance. Proposed: a
  conceptual analysis checked against intuitive cases, with an
  asymmetry criterion its authors call incomplete.
---
<!-- inactive-ok-file: THEORY-072 THEORY-073 THEORY-043 THEORY-029 THEORY-054 THEORY-047 THEORY-056 — Proposed; the bearing of this account on them is stated, nothing here rests on them -->
<!-- inactive-ok-file: LIT-536 — Deferred, no lawful full text; Biological Autonomy is named for its chapter on agency, not leaned on -->

# THEORY-071: Minimal agency requires individuality, interactional asymmetry and self-generated normativity, and individuality without the other two is not agency

## Source

Barandiaran, Di Paolo & Rohde (2009), [LIT-566](../literature.d/LIT-566.md), read in
[NOTE-458](../notes.d/NOTE-458.md): §2 (the three conditions), Table 1 (the cases), §4 (the
generative definition), footnote 3 (emergent regulation), §6 (the
consequences for models).

## What was actually shown

The paper argues from cases. It does not measure anything.

**Three conditions.** Individuality: the system distinguishes itself from
its environment, and an observer does not do it for the system. Otherwise
the explanation regresses through the observer. The paper quotes Jonas: an
identity "owned by, not loaned to its subject" (§2.1). Interactional
asymmetry: the system is the source of modulations of its coupling with
the environment. This is defined as the system changing a subset of the
constraints on an otherwise symmetrical coupling (Eqs. 1–3), not as being
the bigger energy source or the stronger statistical influence. Both of
those fail on clear cases, the gliding bird and the diver against the
faller (§2.2). Normativity: the coupling is regulated against a condition
that can fail and that the system's own organisation sets (§2.3).

**Individuality is necessary and not sufficient.** Table 1 sorts cases.
- A cell undergoing passive osmosis is an individual, "producing and
  maintaining its organization including its membrane". The process may
  even serve it. But the process is physically unconstrained and not
  caused asymmetrically by the cell, so it is not action.
- A kitten warmed by its mother is an individual, and the coupling meets
  the kitten's norm of staying within viable temperature. But the mother
  drives the coupling, so the kitten is not acting.
- A person with a Parkinsonian tremor is an individual and the
  energetic source of the movement. The movement answers to no
  internally generated norm, so it is not action.
- A bacterium in metabolism-dependent chemotaxis meets all three, and it
  acts.

The authors claim sufficiency more weakly: they "find it very difficult
to conceive of any system that jointly fulfills these three criteria and
it is not an agent".

**The generative definition.** A system S is an agent for a coupling C
with an environment E iff S is an open autonomous system and S modulates
C adaptively, that is, so as to maintain some of its own processes (§4).
An autonomous system is a network in which every process depends on at
least one other and enables at least one other, and which would run down
in isolation. The three conditions follow from this. Autonomy here is
Varela's, explicitly "not restrict[ed] or reduce[d]" to metabolism, and
its processes may be neural, sensorimotor or social. Footnote 3 adds that
the modulation must be emergent. "Subsystems that regulate according to a
fixed norm independent of the agent's current state … act as external
constraints on the system."

## What this does not say

- **It does not say that an agent is a self or a person.** The paper's
  "self" is the *autos* of an autonomous organisation, and its
  "autonomy" is organisational. [ADR-024](../decisions.d/ADR-024.md) keeps agent, individual, self and
  person apart. This account separates the first two and says nothing
  about the other two. A bacterium is an agent on this account, and no
  one in the record claims it is a subject or a person.
- **It is not about self-governance.** Personal autonomy, governing
  oneself by standards that are one's own, is the subject of [THEORY-029](THEORY-029.md),
  [THEORY-054](THEORY-054.md) and [THEORY-047](THEORY-047.md). The same word names a different thing.
  Nothing here bears on whether a motive is one's own.
- **It is not about any of the four unities.** It does not say how many
  control systems act as one (behavioral-integration). Footnote 3's
  exclusion of a central controller has the same shape as [THEORY-056](THEORY-056.md)'s
  denial of a distinct regulating system, but neither paper cites the
  other, and the resemblance is the record's.
- **The asymmetry criterion is incomplete by its authors' account.**
  "What counts as a parametric modulation and what as a coupling between
  variables is often a matter of choice for the modeler"
  ([NOTE-458](../notes.d/NOTE-458.md), Limitations). That is the same kind of
  modeller-dependence that [THEORY-073](THEORY-073.md) finds in Markov blankets,
  and the authors name it as the open problem.
- **Life is sufficient, not necessary.** The definition is meant to admit
  non-living agents. It does not say what any present machine is.
  Consequence (b) says that systems "that only satisfy constraints or
  norms imposed from outside (e.g. optimization according to an
  externally fixed function) should not be treated as models of agency".
  That is a remark about modelling. It is not a finding about any system,
  and it is no instruction for machine-learning practice.

## Connections

- **[THEORY-072](THEORY-072.md) (organisms versus dissipative structures)** is not
  extended. Both ground norms in a self-maintaining organisation, and
  this paper cites Mossio et al. 2009 ([LIT-570](../literature.d/LIT-570.md)) for that. But its
  autonomy is a network of mutually enabling processes, not closure of
  constraints, and it makes no use of differentiation. Its line against a
  flame is a different one. A flame may well be self-maintaining in the
  broad sense, but it does not adaptively modulate its coupling. So this
  account neither needs nor refines the demarcation in [THEORY-072](THEORY-072.md).
  The two are independent conditions, and an organism in that account's
  sense is not thereby an agent in this one.
- **[THEORY-073](THEORY-073.md) (blankets do not individuate).** Both conditions
  this paper puts first, individuality the system defines for itself
  and asymmetry that is not a statistical measure, are what a Friston
  blanket lacks on that account. The blanket is drawn by the modeller,
  and its arrow structure is stipulated in the graph. Bruineberg et al.
  borrow this paper's term "interactional asymmetry" for that arrow
  structure ([LIT-603](../literature.d/LIT-603.md)). On this account, the arrow structure is not
  interactional asymmetry.
- **[THEORY-043](THEORY-043.md) (minds of agents).** That account reports that its
  readings agree that "agency survives both directions": Block's
  homunculi-head, List's group agents ([LIT-401](../literature.d/LIT-401.md)) and Levin's nested
  collectives. The agency they agree on is the thin functionalist or
  cybernetic kind. On this account, the agency is not cheap. Minsky's
  mindless agents and Brooks's behaviours have norms that their designers
  set, and no individuality of their own. Whether a firm or a court
  meets the three conditions is a substantive question, which neither
  List nor this paper answers. [THEORY-043](THEORY-043.md)'s verdict on consciousness is
  untouched. Its premise that agency is not in dispute holds for the
  thinner notion only.
- **Levin ([LIT-439](../literature.d/LIT-439.md), [NOTE-341](../notes.d/NOTE-341.md)).** Levin's Self is the set of parts that
  pursue a goal together, where a goal is the set point of "a feedback
  system that operates to maximize some specific state of affairs".
  [NOTE-341](../notes.d/NOTE-341.md) records that this makes any homeostat a Self, and that the
  paper accepts it. On this account a homeostat is not, by that alone,
  an agent. Its norm is fixed from outside, which
  footnote 3 counts as an external constraint, and it does not make
  itself an individual. The two criteria also run in opposite orders:
  Levin individuates by the goal, and this account needs the individual
  first. [ADR-024](../decisions.d/ADR-024.md) already reads Levin's Selves as agents and individuals.
  This account says that on the organisational reading, many of them
  would be neither.
- **Participatory sense-making ([LIT-571](../literature.d/LIT-571.md)).** The same group extends
  "sense-making", a deviation from a self-generated norm becoming
  significant, to social interaction. It requires that the participants
  remain autonomous agents in this sense.
- **Biological Autonomy ([LIT-536](../literature.d/LIT-536.md))** has a chapter on agency (chapter 4).
  It is unread, and the paper's autonomy is wider than that book's
  metabolic one.
