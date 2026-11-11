---
status: Proposed
title: 'Where a literal rendering loses nothing the source offers on the declared report problems, no rendering made from the source without the situation, a compensating one included, is a better report for an ideal receiver, so compensation serves report fidelity only as a gain in a code-bound reader''s usable information, or where the literal rendering itself loses a distinction the reports concern'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation: a declared family Q of report problems
  about one situation Z, a stated prior, a literal rendering with
  D⁺(U → V_lit) = 0 on Q, and a rendering made from the source and the
  target readers' code alone (V ⫫ Z | U) with lower Bayes risk than the
  literal rendering on some problem in Q. Or the objection that it only
  restates its premises: that CLAIM-199 or CLAIM-326 already places
  compensating renderings, or that CLAIM-461 already says its verdict is
  a receiver-relative one and not the order's.
tags:
- translation
- information-theory
- philosophy-of-language
date: '2026-11-11'
line:
- pragmatic-transport
rests_on:
- CLAIM-326
- CLAIM-199
complements:
- CLAIM-461
- CLAIM-212
summary: >-
  A derivation from the part account of fidelity relative to receivers
  (synthesis review of 2026-11-11). For report fidelity on a declared
  family of problems and a prior, if the literal rendering loses nothing
  the source offers, any rendering made from the source without the
  situation has Bayes risk at least the source's (CLAIM-326, step (a)),
  which is at least the literal rendering's. So CLAIM-461's compensating
  report can beat the literal one only for readers who cannot use the
  literal rendering as an ideal receiver would, which is CLAIM-199's gain
  in usable information, or where the literal rendering itself loses a
  distinction, as English "you" for ты amid вы (CASE-066). It places
  CLAIM-461's objection to CLAIM-212 and does not settle it. The wording
  is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CLAIM-461 CLAIM-212 CLAIM-091 — Proposed; the objection this places, the distinction it bears on and the compensation claim, cited as open -->
<!-- inactive-ok-file: ADR-075 CLAIM-258 — Proposed; cited with its standing -->

# CLAIM-tmpmte91: Where a literal rendering loses nothing the source offers on the declared report problems, no rendering made from the source without the situation, a compensating one included, is a better report for an ideal receiver, so compensation serves report fidelity only as a gain in a code-bound reader's usable information, or where the literal rendering itself loses a distinction the reports concern

## The claim

CLAIM-212 separates report fidelity, where source and rendering are
experiments about the source's situation Z and Blackwell's order is
defined, from re-performance. Its "What it does not say" calls
compensation a re-performance notion. CLAIM-461 objects: "for a reader
whose code gives the literal word a meaning the source lacked, the
compensating rendering can be the more faithful report". This claim says
in which sense that can hold.

**Setting.** Fix a family Q of report problems about Z, with losses in
[0, 1], and a prior π, as CLAIM-326 does. U is the source, V_lit a
literal rendering, V_comp a compensating one. The translator draws on the
source and on the target readers' code, which does not vary with Z, and
not on the situation, so V_comp ⫫ Z | U: it is a garbling of U.

**Derivation.** Suppose the literal rendering loses nothing the source
offers on Q: D⁺(U → V_lit; π) = 0, so r_q,π(V_lit) ≤ r_q,π(U) for every
q in Q. By CLAIM-326's step (a), a garbling never gains:
r_q,π(U) ≤ r_q,π(V_comp). So r_q,π(V_lit) ≤ r_q,π(V_comp) for every q in
Q. For an ideal receiver, one free to use any rule, the compensating
rendering is never the better report.

**Where the advantage can then lie.** CLAIM-199 separates what a
rendering makes possible from what a receiver can use, the best risk
over the rules it can apply. A reader whose code reads the literal word
as procreative cannot apply the rule that reads it as the source meant,
so its usable information from V_lit is lower than the ideal receiver's.
V_comp can then give that reader a lower risk than V_lit does, never
lower than r_q,π(U) (CLAIM-199's ceiling). That is CLAIM-461's case:
its advantage is a gain in usable information under the readers' code,
not a verdict of the order.

**Where the order itself can prefer compensation.** If the literal
rendering loses a distinction a report problem concerns, the premise
fails and the order can rank the compensating rendering higher. Let Z be
whether Dolly's address shifts to intimacy, uniform on two values, and U
mark it (ты amid вы). A literal rendering into English "you" is constant
in Z, risk 1/2 on "did the address shift?" under 0–1 loss; Garnett's
added "Stiva" marks it, risk 0. Both are made from the source alone.
CASE-066 is the documented shape of this case, on the translators'
judgement and not readers'.

## What it does not say

- That the "Son of God" translators were right, or that any reader gains.
  That is CLAIM-461's open condition.
- That compensation is a re-performance notion only, or mainly. It says
  that in the order's sense of report fidelity, compensation helps only
  where the literal rendering loses something; in a receiver's sense it
  can help where the reader's code is the obstacle.
- Anything about a translator who draws on knowledge of the situation
  beyond the text. Such a rendering is not a garbling (CLAIM-323,
  CLAIM-258), and the derivation does not reach it.
- That the literal rendering is lossless in any real case. That is a
  premise to establish per case, relative to Q.

## Admission

**Route: derivation** (ADR-075, step 5). From CLAIM-326's step (a) and
the premise D⁺(U → V_lit) = 0 on Q, two inequalities give
r(V_lit) ≤ r(U) ≤ r(V_comp) on every problem in Q; with CLAIM-199's two
quantities the advantage CLAIM-461 claims is located in usable
information. No claim on the record states it: CLAIM-461 and CLAIM-212
do not mention garblings or the ceiling, CASE-063 says it has "No
probability model of any item", and CLAIM-199 does not mention
compensation. The derivation is short; its content is the placement,
which splits CLAIM-461's objection into a regime where it holds only for
receivers and a regime, a lossy literal rendering, where it holds by the
order as well.

**Free parameter, closed.** "Loses nothing" is fixed as
D⁺(U → V_lit; π) = 0 on the declared Q and prior, and "made without the
situation" as V ⫫ Z | U.

**A realistic case, checked against the defeat condition.** Bible
translators draw on exegetical knowledge, which could be knowledge of
the situation beyond the text. If it is, their rendering is not a
garbling and falls outside the claim's setting; it does not meet the
defeat condition, which needs a rendering made from the source and code
alone. If the knowledge is of the source's code (what the word conveyed
to its own readers), an ideal reader of the source has it, and the claim
applies. The case shows where the claim's scope ends, not that it is
false.
