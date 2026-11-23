---
status: Proposed
title: 'Corporate sanctions that ended, coded from open sources for whether the firm kept weighing others'' harms after: a monitor''s effect on violations lasts only while it is on site, a sanction-only and a redesigned firm both went on doing the harm by report or allegation, the record''s own case is not yet ripe, and no case holds reputation and benefit fixed'
version: 1
history:
- version: 1
  date: '2026-11-23'
  note: >-
    Filed by the lead run of 2026-11-23, as a delegated lead worker. The
    coding rules, the case and event tables, the coefficients read, the
    summary script, its tests and the results are committed under
    scratch/studies/lead-101/.
standing: documented
kind: executed-study
tags:
- society-and-governance
- ethics
- social-ontology
- emotion-and-affect
date: '2026-11-23'
line:
- organizational-affect
- distributed-agency
bears_on:
- QUESTION-265
draws_on:
- THEORY-tmpvtotj
reported_in:
- NOTE-tmpejwjy
- NOTE-tmpwvqch
- NOTE-tmpf8oxn
- NOTE-tmpu1nx5
- NOTE-tmpnnzbf
- NOTE-tmp59pkn
summary: >-
  [LEAD-101](../leads.d/LEAD-101.md) run on open sources: does a corporation changed only by sanction
  keep weighing others' harms once the sanction lifts, and does a
  redesigned one, with reputation and benefit held fixed? Coding rules were
  written before the table. One quantitative study (Gallo, Lynch and Tomy
  2023; [THEORY-tmpvtotj](../theory.d/THEORY-tmpvtotj.md)) finds that a monitor cuts penalised violations by
  18–25% only while it is on site. Three cases were coded: Purdue Pharma
  (sanction only; promotion widened after its integrity agreement ended in
  2012, by a state's allegations), Siemens (redesigned by an outside body's
  assessment; a costly self-report during its monitorship, and a red-flag
  tool exempted where it would bite, with bribery reported after it ended)
  and Wells Fargo, the record's own case (growth restriction lifted on
  2025-06-03; too recent). No case meets the lead's standard: none holds
  reputation and benefit fixed, none of the post-lift outcomes is a finding
  against the firm, and the outcomes found are predicted by [CLAIM-431](../claims.d/CLAIM-431.md) as
  well as by [CLAIM-432](../claims.d/CLAIM-432.md). The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-431 CLAIM-432 CLAIM-039 — Proposed; the claims whose test this study runs -->
<!-- inactive-ok-file: THEORY-tmpvtotj CLAIM-tmpm9a3z CLAIM-tmpsuj5n CLAIM-tmpuvgxw CLAIM-tmpioexk — new, Proposed; the account used and the claims filed from this run -->

# CASE-tmphvbov: Corporate sanctions that ended, coded from open sources for whether the firm kept weighing others' harms after: a monitor's effect on violations lasts only while it is on site, a sanction-only and a redesigned firm both went on doing the harm by report or allegation, the record's own case is not yet ripe, and no case holds reputation and benefit fixed

## What was done

[LEAD-101](../leads.d/LEAD-101.md) asks for cases "where a sanction ended and harm-weighing can be
traced after", to test [CLAIM-432](../claims.d/CLAIM-432.md)'s part 5: "a corporation changed only by
sanction reverts when the sanction lifts, and one whose concerns were
redesigned does not", which is also [CLAIM-431](../claims.d/CLAIM-431.md)'s first route to an answer.
The lead's title adds "with reputation and benefit held fixed".

Everything is under scratch/studies/lead-101/: `CODING.md` (the rules,
written after one scoping search and before the table), `cases.csv`,
`events.csv` (13 dated events, each with its source and locator),
`studies.csv` (eight coefficients from Gallo et al.'s Table 5),
`summarize.py` and `test_summarize.py` (11 tests, passing), `results.json`.

**The coding rules, in brief.** A unit is one firm and one sanction with a
fixed term that ended on a documented date. The *arm* is R (a procedure or
role duty that makes harm of the sanctioned kind an input with authority
over decisions, installed beyond the sanction's terms or kept after it,
shown by an independent source or internal documents), S (only what the
sanction required) or U. The *outcome* in the five years after the end is
W+ (harm weighed against the firm's interest, at a cost to it), W- (the
harm done again, or information about it reaching decision-makers without
restraining them) or W0; each W- is timed as `reversion` (begun after the
end) or `through` (begun or continued during). Each outcome carries its
source's standing (finding, allegation, study, report). *Reputation* is
`exposed`, `private` or `unknown`; *benefit* `aligned`, `opposed` or
`unknown`. A case meets the standard only with a post-lift W+ or W- from a
finding or study, and reputation and benefit that do not explain it (for
W+: private and opposed; for W-: a pair across arms with equal codes).

**The frame** is purposive, as the rules say: the quantitative studies a
search found, the record's own case, and two cases whose end date and
post-lift record are in open documents. It can show whether the cases
looked at meet the standard, not how often firms revert.

**Sources not reached.** The Justice Department's site showed a bot check
(the Purdue plea of 2020, which would turn allegations into admissions);
the Corporate Prosecution Registry's downloads page and a mirror of the
Department's site were refused by this session's permission system;
Violation Tracker answered 403. None was retried.

## The quantitative arm

Gallo, Lynch and Tomy (2023; [LIT-tmpaya40](../literature.d/LIT-tmpaya40.md), [NOTE-tmpejwjy](../notes.d/NOTE-tmpejwjy.md), [THEORY-tmpvtotj](../theory.d/THEORY-tmpvtotj.md)):
193 deferred and non-prosecution agreements with listed firms, 2001–2019.

| term (Table 5) | full sample | CEM matched | entropy balanced |
|---|---|---|---|
| monitor × during the agreement | −23% (t −2.61) | −25% (t −2.15) | −27% (t −2.23) |
| monitor × after the agreement | −9% (t −0.87) | −13% (t −1.07) | −2% (t −0.17) |
| board changes × after | −15% (t −1.71) | −24% (t −2.30) | — |

Percent changes recomputed from the log-count coefficients. The
ethics-and-compliance measure from earnings calls rises during the
monitorship and falls after it. Coded: outcome penalised violations (not
harm-weighing); post window estimated; reputation and benefit not held
fixed; both arms sanctioned.

## The cases

| case | sanction, end | arm | during | after (5 years) | timing | standing | reputation | benefit |
|---|---|---|---|---|---|---|---|---|
| Purdue Pharma | integrity agreement, 2012 | S | W- | W- | through | allegation | exposed | aligned |
| Siemens | DOJ/SEC monitorship, 2012 | R | W+ and W- | W- | through | report, allegation | exposed | aligned |
| Wells Fargo | Fed growth restriction, 2025-06-03 | U | — | unripe | — | — | — | — |

- **Purdue** ([LIT-tmpqqqt1](../literature.d/LIT-tmpqqqt1.md), [LIT-tmpy9yua](../literature.d/LIT-tmpy9yua.md)). The 2007 agreement ran five
  years and required compliance machinery, not a procedure able to stop
  sales on harm grounds. Purdue kept its own list of prescribers it
  suspected of abuse and diversion (Region Zero); by Indiana's complaint,
  the board was given the revenue each provided and told that losing them
  would cost "almost 10% of its sales" (2011). After the term, reported
  initiatives for 2013 included promotion to opioid-naive and elderly
  patients. After a 2013 subpoena the detailed board reports stopped and
  other information was, in the complaint's words, to be "relay[ed] orally". Arm S; W- during and after.
- **Siemens** ([LIT-tmp5i00q](../literature.d/LIT-tmp5i00q.md), [LIT-tmptlfo6](../literature.d/LIT-tmptlfo6.md)). After the 2008 settlement it
  built a compliance organization of about 600 positions and EUR 100
  million, which the Norwegian fund's Council on Ethics judged in June 2012
  left it no riskier than comparable firms: arm R. During the monitorship
  it stopped a planned bribe in Kuwait and lost the tender (W+), and its
  compliance officers exempted three of four China reseller models from the
  red-flag tool while noting they could be abused (W-). After it, a Chinese
  verdict against a hospital president reports a bribe offer by a Siemens
  manager in the year the monitorship concluded, and a dismissed senior
  manager alleged in 2013 that the practice went on. Its compliance leaders
  gave staff the reasons of prosecution and exclusion.
- **Wells Fargo** ([LIT-tmppg6h5](../literature.d/LIT-tmppg6h5.md); [CASE-151](CASE-151.md)). The growth restriction was
  lifted on 2025-06-03 on improved governance and risk management; the
  action's other provisions stay. Under six months of window; unripe.

## The results

1. **No case meets the lead's standard.** `results.json`: Purdue and
   Siemens lack a finding-level post-lift outcome and a reputation and
   benefit that would not explain it; Wells Fargo lacks a window. The test
   [CLAIM-431](../claims.d/CLAIM-431.md) and [CLAIM-432](../claims.d/CLAIM-432.md) call unrun remains unrun in the form the lead
   sets.
2. **What the sanction itself produces does not outlast it**, in the one
   estimate that separates the periods ([CLAIM-tmpm9a3z](../claims.d/CLAIM-tmpm9a3z.md)). This is the first
   half of [CLAIM-432](../claims.d/CLAIM-432.md)'s prediction, but [CLAIM-431](../claims.d/CLAIM-431.md)'s prudence reading predicts
   it too.
3. **The prediction separates the claims only in the redesigned arm**
   ([CLAIM-tmpsuj5n](../claims.d/CLAIM-tmpsuj5n.md)). Reversion of a sanction-only firm cannot tell remorse
   from prudence; only a redesigned firm's conduct after the lift, with
   reputation and benefit fixed, can.
4. **The one redesigned case does not supply that.** Siemens's weighing at
   a cost happened under the monitor and in public; after the monitor, the
   evidence is of the harm continuing, by report and allegation; and its
   procedure was explained by threat. Within it, a harm-weighing tool was
   held and denied precedence where it would have cost sales, which is
   [CLAIM-432](../claims.d/CLAIM-432.md)'s distinction inside the arm meant to lack it.
5. **The board-change result** in the quantitative arm is open to two
   readings, filed as alternatives: [CLAIM-tmpuvgxw](../claims.d/CLAIM-tmpuvgxw.md) (evidence that redesign
   persists where sanction does not) and [CLAIM-tmpioexk](../claims.d/CLAIM-tmpioexk.md) (no separation,
   since a board changed under sanction and judged by penalties fits
   prudence equally). The run leans to the second.

## What would meet the standard

A firm coded R whose post-lift decision weighed a harm at a cost, recorded
in documents not made public at the time (internal records released later
in litigation or by a monitor's public report), set against an S firm with
the same exposure. Wells Fargo's window opens in mid-2027 on the rules'
two-year ripeness test. [CLAIM-039](../claims.d/CLAIM-039.md) is untouched: nothing here bears on
whether the affect is functional, only on which affect.
