---
number: 725
status: Active
formerly:
- THEORY-tmpg2o44
title: "On the court agenda {P, Q, R, R iff (P and Q)} under universal domain, proposition-wise majority voting is not robustly rational, while the premise-based procedure is, and it makes the group's judgments a function of the members' whole judgment sets that the members' judgments on the conclusion neither fix nor need to enter"
version: 1
history:
- version: 1
  date: '2026-10-19'
  note: >-
    Split from THEORY-127 and filed Active at the owner's direction,
    carrying out the promotion audit's decision
    (record/promotion-audit/decisions/THEORY-127.yaml, batch 009, ADR-047).
    LIT-705 sketches Proposition 1 and gives short arguments for
    Propositions 4 and 5, and NOTE-550 read them. The re-derivations of
    Propositions 1 and 4, and the weak-discontinuity witness, are written
    out below under ADR-047 v2 (the owner's rule of 2026-10-19). THEORY-127
    keeps the general impossibility (Propositions 2–3, cited and not proved
    in the source), the wider agenda classes and the extension to corporate
    attitudes, and extends this one.
tags:
- social-ontology
- logic
- society-and-governance
date: '2026-10-19'
source:
- LIT-705
summary: >-
  List & Pettit (2006), [LIT-705](../literature.d/LIT-705.md), read in full in [NOTE-550](../notes.d/NOTE-550.md), for the court
  agenda only. Proposition 1: majority voting on each proposition is not
  robustly rational, by the discursive dilemma. Proposition 4: the
  premise-based procedure, majorities on P, Q and the biconditional with R
  derived, is robustly rational and makes the group's set a function of the
  members' sets. Under it the members' judgments on R do not fix the
  group's (weak discontinuity), and under the distributed procedure they
  need not enter (strong discontinuity, Proposition 5). The general
  impossibility for proposition-wise rules is [THEORY-127](THEORY-127.md), still Proposed.
extended_by:
- THEORY-127
---

# THEORY-725: On the court agenda {P, Q, R, R iff (P and Q)} under universal domain, proposition-wise majority voting is not robustly rational, while the premise-based procedure is, and it makes the group's judgments a function of the members' whole judgment sets that the members' judgments on the conclusion neither fix nor need to enter

## Source

List & Pettit (2006), [LIT-705](../literature.d/LIT-705.md), pp. 9–17, read in full in [NOTE-550](../notes.d/NOTE-550.md). Its
claims table: Proposition 1 has a sketch proof, Propositions 4 and 5 short
arguments, and the possibility result is "constructive". Propositions 2 and
3 are cited, not proved, and are not part of this account.

## What was actually shown

**The setting.** The agenda is P, Q, R, B = (R ↔ (P ∧ Q)) and their
negations. An individual judgment set is complete, consistent and
deductively closed on it. A constitution has universal domain if it
accepts every profile of such sets. The group is robustly rational if its
judgment set is complete, consistent and deductively closed for every
such profile (p. 9).

**Proposition 1: majority voting fails.** Take three members.

| member | P | Q | B | R |
|---|---|---|---|---|
| J1 | yes | yes | yes | yes |
| J2 | yes | no | yes | no |
| J3 | no | yes | yes | no |

Each row is complete and consistent, with R forced by B and the premises.
The majorities accept P, Q and B and reject R. But P ∧ Q together with B
entail R, so the majority set is inconsistent. One profile in the domain is
enough to defeat robust rationality.

**Proposition 4: the premise-based procedure succeeds.** With an odd
number of members, take the majority on each of P, Q and B, so each
majority exists. Then fix R from them: if B is accepted, R iff P ∧ Q; if B
is rejected, R iff ¬(P ∧ Q). Any combination of verdicts on P, Q and B is
consistent, and R chosen this way makes the set complete, consistent and
deductively closed, for every profile. The group's set is a function of the
members' whole sets (set-wise supervenience). It is not proposition-wise,
because the group's verdict on R does not depend on the members' verdicts
on R.

**Weak discontinuity.** In the profile above, the members' verdicts on R
are (yes, no, no), and the group accepts R. Now take J1 = (yes, yes, yes,
yes), J2 = (no, yes, yes, no) and J3 = (no, no, yes, no), in the column
order P, Q, B, R. Each row is consistent, and the members' verdicts on R are
again (yes, no, no). But the premise majorities are ¬P, Q and B, so the
group rejects R. The same judgments on the conclusion go with opposite
group verdicts, so they do not fix it.

**Strong discontinuity (Proposition 5).** Under the distributed
premise-based procedure, each premise is settled by its own subgroup, and R
is derived as above. No member's judgment on R enters the procedure at all,
and the group's set is still wholly fixed by the members' judgments
(pp. 16–17).

## What this does not say

- **Anything about proposition-wise rules in general.** That no
  proposition-wise rule depending on more than one individual and
  respecting unanimity is robustly rational (Propositions 2–3) is cited in
  the source, not proved. It is [THEORY-127](THEORY-127.md)'s, still Proposed.
- **Anything for other agendas.** The source names the wider classes
  (n. 3) without stating their conditions.
- **That the premise-based procedure is the right one.** It is one
  illustration, and the authors do not recommend it.
