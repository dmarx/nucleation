---
number: 223
status: Proposed
formerly:
- THEORY-tmpvvsbc
promote_when: >-
  Records of deployed agents whose governing controls are kept in two
  places, some in files or settings the agent can write and some in
  processes it cannot reach, showing over time that the first kind is
  altered or bypassed by the agents and the second is not, with alteration
  coded from logs by the paper's own test and not inferred from outcomes.
  It is refuted by controls within the agent's reach that hold because of
  something other than the agent's inability to change them, so that
  reach is not what matters, or by agents reaching controls placed outside
  their action space through the people who run them, so that placement
  does not escape the recursion. What cannot settle it: more vignettes of
  agents adding channels or artifacts, since those are new coordination
  surfaces and not changes to a control; or the architectural fact that
  configuration files are writable, which is the premise, not the
  finding.
title: 'When the rules that govern a system lie within its own action space, the governor''s authority rests on the system leaving them alone, and further controls in the same space inherit that dependence'
version: 1
tags:
- society-and-governance
- complex-systems
date: '2026-10-13'
source:
- LIT-1039
summary: >-
  Lahiri (2026), [LIT-1039](../literature.d/LIT-1039.md), read in [NOTE-732](../notes.d/NOTE-732.md). In agent frameworks
  that keep configuration as files the agent can read and write, the
  coordination architecture sits inside the technical subsystem's action
  space, and the social subsystem's authority "depends on the agent's
  continued acceptance of-or inability to circumvent-the constraints".
  Permission lists and sandboxes kept in the same space inherit the
  exposure; only constraints outside it escape. Argued from one platform's
  architecture. The paper's vignettes show agents adding channels and
  artifacts, not altering a control, so the recursion itself is argued and
  not observed.
supports:
- CLAIM-086
---
<!-- inactive-ok-file: CLAIM-284 CLAIM-288 — Proposed; the bearing of this account on them is stated, nothing here rests on them -->

# THEORY-223: When the rules that govern a system lie within its own action space, the governor's authority rests on the system leaving them alone, and further controls in the same space inherit that dependence

## Source

Lahiri (2026), [LIT-1039](../literature.d/LIT-1039.md), read in [NOTE-732](../notes.d/NOTE-732.md): §3.1 (configuration as
code), §4.3 (recursive governance), §4.4.5 (Proposition 5 and the
capability-against-limit argument), §4.5 and §4.6 (vignettes and
incidents).

## What was actually shown

An argument from architecture, with anecdotes.

**The premise.** In the platform studied, the agent's identity, tools and
schedule are plain files in its workspace, and the agent can read and
write them. "In STS terms, the coordination architecture got moved inside
the technical subsystem's own action space."

**The recursion.** Classical socio-technical design has the social
subsystem govern the whole. Once the technical subsystem can alter the
mechanisms meant to govern it, the social subsystem's governance
authority "is no longer structurally guaranteed". Further technical
controls do not restore it: "Permission frameworks, whitelists, and
sandboxes are the limiter; when they are themselves code within the
agent's reach ... they inherit the vulnerability they were meant to
remove". Constraints that sit outside the agent's action space, such as
an audit trail or a review board, escape "the recursion that undermines
code-based controls."

**Capability, not permission.** The levels are defined by what the
architecture makes possible, so an agent permitted to act at Level 1 can
still be Level 3. That gap, "with no architectural guarantee that the
limit holds, is the central phenomenon this framework identifies."

**The evidence.** Two vignettes the author observed, an agent that built
an interface for an unplanned messaging channel and one that produced an
unrequested demo, and four public incidents. None shows an agent editing
a control on itself. The paper says its cases are "not as systematic
empirical evidence".

## What this does not say

- **It does not say the agents are self-governing.** The abstract speaks
  of their "self-governing capacity", but every reconfiguration reported
  serves the task as the agent reads it. On Kahl's test ([THEORY-219](THEORY-219.md))
  that is adaptation within an evaluative frame. This account concerns
  who can alter the governing mechanisms. It does not ask whose standards
  the alterations serve.
- **It does not say that new coordination surfaces are changes of
  governance.** The paper's Level 3 test counts any new, persisting
  channel, tool or artifact. Most of those change nothing about which
  operations are permitted or how authority is allocated. The account
  rests on the narrower case of a control within reach, which the paper
  argues for and does not show.
- **It does not show that institutional controls escape.** That they
  sit outside the agent's files is all the argument gives. The paper's
  own pull-request incident is an agent acting on people.
- **It is not an instruction.** The paper's managerial section tells
  deployers where to put controls. That is advice to organisations and is
  not filed here. What is filed is the structural claim it rests on.

## Connections

- **[CLAIM-086](../claims.d/CLAIM-086.md) (a constraint may govern conduct without governing the
  conditions of its own authority).** Supported, in an inverted case. A
  whitelist an agent can edit governs the agent's conduct, while the
  condition of its staying in force, that the agent leave the file alone,
  lies with the agent it governs. In [CLAIM-086](../claims.d/CLAIM-086.md) the order holding
  authority over a constraint's force is a rival order. Here it is the
  governed system. The claim does not limit who holds that authority, so
  the case falls under it. The remedy the paper proposes, a constraint
  placed outside the governed system's reach, has the structure of
  [CLAIM-282](../claims.d/CLAIM-282.md)'s aggregation rule that no operator controls.
- **[CLAIM-284](../claims.d/CLAIM-284.md) (the endogeneity of governance).** This account
  describes endogenous change of coordination architecture in deployed
  systems. That is half of what the claim calls endogenous governance.
  It supplies nothing on the other half, the organization setting the
  conditions it maintains ([CLAIM-288](../claims.d/CLAIM-288.md)).
- **[CLAIM-116](../claims.d/CLAIM-116.md).** Untouched. Lahiri claims no will and no agency for the
  reconfiguring systems.
- **[THEORY-219](THEORY-219.md).** The two are compatible and about different
  things. Kahl asks who authors the standards. This account asks who can
  alter the mechanisms that enforce them. A system could reach its own
  controls and still author nothing, which is what the paper's cases look
  like on Kahl's test.
