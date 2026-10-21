---
status: Read
paper: LIT-tmpa8ani
title: 'Di Tella and Franceschelli — Government advertising and media coverage of corruption scandals'
version: 1
history:
- version: 1
  date: '2026-10-21'
  note: >-
    Read in full from NBER Working Paper 15402 as posted by NBER
    (www.nber.org/system/files/working_papers/w15402/w15402.pdf), which is
    dated "October 2009, Revised July 2010", text extracted with pdftotext
    in plain and layout modes. Read: the abstract, all five sections,
    Figures 1–6 from their captions, and Tables A–C and 1–10 from the
    layout extraction. The published article (AEJ: Applied 3(4), 2011) was
    not reached (Unpaywall and OpenAlex report it closed) and was not
    compared; its abstract's figures, 0.23 front pages and 18 percent of a
    standard deviation, differ from this version's 0.31 and 25 percent.
date: '2026-10-21'
summary: >-
  In the four main Argentine national newspapers, April 1998–December 2007,
  months in which a newspaper received more government advertising were
  months in which it gave less front-page space to the federal
  government's corruption scandals, within newspaper and month and within
  each newspaper-president pair: in this version, 0.31 of a front page per
  month per standard deviation of advertising. The association holds for
  advertising placed by the central agency Télam and not for autonomous
  agencies, and not for scandals of non-political actors. The design shows
  an association; the authors read it as consistent with coverage traded
  for transfers.
---
<!-- inactive-ok-file: CLAIM-tmpjo2zr CASE-tmp3uarw TERM-tmpe6jtq — Proposed, or a case filed with them; the entries filed in the same pull request that this reading bears on, cited as open -->

# NOTE-tmpeytex: Di Tella and Franceschelli — Government advertising and media coverage of corruption scandals

## Contribution

It measured, outlet by outlet and month by month, how much front-page space
four national newspapers gave to the sitting government's corruption, and
set that against how much government advertising each newspaper received
that month. The comparison is within newspaper and within presidency. It is
an early systematic test, for a democracy, of the transfer channel that
Besley and Prat model.

## Key insight

Identification comes from relative coverage. The measure compares a
newspaper with itself under the same president, and with the other papers
in the same month. That removes the obvious confound: friendly governments
advertising in ideologically close papers that would have covered them
kindly anyway. "Thus, if all papers are biased, we do not detect it with
our tests."

## Assumptions

- **Sample.** Clarín, La Nación, Página 12 and Ámbito Financiero, 74% of
  national newspaper circulation, for 117 months from April 1998 to
  December 2007, across four presidencies (Menem, De la Rúa, Duhalde,
  Kirchner). There are 466 newspaper-months.
- **Coverage measure.** Front Pages: for each day, the share of the front
  page's area covering any corruption scandal involving the current
  administration, measured by a research assistant with a computer, summed
  over the month (0 to 30). There are 254 scandals on 994 front pages.
  Variants are Hide (scandals another paper has reported and this one has
  not), Incidents (scandals only one paper covered), Affaires (covered by
  at least two) and Front Pages Scandal (per scandal).
- **Advertising measure.** Monthly federal government advertising per
  newspaper in millions of 2000 pesos, from the NGO Poder Ciudadano, which
  obtained it from the government's Secretaría de Medios. The series
  starts in January 2000. For April 1998–December 1999 it was
  reconstructed by measuring government ad space on two random days per
  month and converting with the January–March 2000 overlap. "The first
  author was a member of the board of Poder Ciudadano during parts of our
  sample period."
- **Specification.** OLS of Front Pages on ln(Government Advertising + 1)
  with newspaper and month fixed effects, then newspaper × president
  dummies, then newspaper × president linear trends. Newey–West standard
  errors.

## Key results

- **Table 1.** The coefficient on ln(ads + 1) is −3.303 (s.e. 0.682) with
  newspaper and month effects, −1.652 (0.643) adding the 16
  newspaper × president dummies, and −1.008 (0.589, significant at 10%)
  adding their trends. The authors read the halving as evidence that
  ideological proximity drives both advertising and coverage.
- **Size.** "a one standard deviation increase in government advertising
  (0.26 million pesos of 2000) is associated with a reduction in coverage of
  corruption scandals in the month by 0.31 of a cover, or 25% of a standard
  deviation", evaluated at mean advertising of 0.23. Rechecked here from
  column 2: 1.652 × [ln(1.49) − ln(1.23)] = 0.317.
- **Table 2, the channel.** For 2000–2007 the association holds for
  advertising placed through Télam, the presidency's news agency (−1.718,
  s.e. 0.679, with interactions). It vanishes for agencies that place
  their own advertising (0.115, s.e. 1.454).
- **Table 3, leave-one-out.** All eight coefficients are negative. The one
  excluding the Kirchner presidency, with nearly half the observations
  gone, is insignificant (−0.531, s.e. 1.704). The effect is largest when
  Clarín, the biggest paper, is dropped.
- **Tables 4–5, timing.** Current advertising matters more than lagged. In
  the Granger tables, lagged advertising predicts coverage weakly (F = 3.48
  at 10% with one lag, 1.85 with two, 2.73 with three), and lagged
  coverage does not predict advertising (F = 0.96, 0.26, 0.08). "it is the
  government the one that leads".
- **Table 6, a placebo.** For scandals of the police, unions, the church
  and piqueteros (321 scandals, 941 front pages), the coefficients are
  −0.373 and −0.489, both insignificant.
- **Tables 7–9, scandal-level measures.** Affaires carry 81% of the
  association (1.33 of 1.64) and Incidents 19%. Per scandal, with scandal
  and newspaper × scandal effects, the coefficient is −0.017 (s.e. 0.010),
  2.7% of a standard deviation. Hide is +30.1 (s.e. 5.4) without the
  president interactions and −0.015 (s.e. 2.3) with them. The authors call
  this "not ... robust" and conclude that advertising goes with how much
  space a scandal gets, not with whether or when it is first reported.
- **Table 10, circulation.** For Clarín and La Nación, more corruption
  coverage goes with higher circulation, and more Hide with lower.
- **Footnote 28, an instrument.** Using the government's fiscal position
  times ideological proximity as an instrument for advertising gives
  −6.081 (s.e. 1.271) for Table 1's column 1. This is reported in a
  footnote, with no first stage shown.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Within newspaper and month, and within newspaper-president pairs, more government advertising goes with less front-page coverage of the government's corruption | strong as an association | Table 1, columns 1–2; Tables 3–4 |
| C2 | The association is specific to discretionary advertising placed centrally, and to scandals of the government | moderate | Table 2 (Télam against autonomous agencies); Table 6 (non-political scandals) |
| C3 | The government's advertising leads and coverage follows | weak | Granger tests, with F-statistics at or near the 10% level |
| C4 | Advertising affects how much space a scandal gets, not whether it is reported | moderate | Tables 7–9; Hide is not robust |
| C5 | The negative association reflects coverage traded for transfers | weak | consistent with C1–C4 and the documented Argentine practice; an instrument in a footnote; the authors "do not offer any further interpretation" |

## Concepts

- **Front Pages**: monthly sum of the daily share of front-page area on
  scandals of the current administration.
- **Hide**: scandals already reported by another of the four papers and
  not yet by this one.
- **Incidents and Affaires**: scandals covered by one paper, and by at
  least two.
- **Motivated reporting**: reporting "not independent of monetary
  transfers", covering both bribery by the government and extortion by the
  paper. The negative association cannot tell these apart, but the timing
  favours the first.

## Connections

It takes Besley and Prat (LIT-tmptgfjj) as its model and argues that with
non-verifiable news the government may gain from buying some outlets and
not others, which their model rules out. Its identification is like
Larcinese, Puglisi and Snyder's comparison of papers' coverage of a common
event, and its private-sector counterparts are Reuter and Zitzewitz on
mutual funds and Gambaro and Puglisi on Italian companies. Szeidl and
Szucs (LIT-tmp6b6sj) cite it as "suggestive evidence" that "did not rule
out plausible market-based explanations", and they address that with
private advertisers as a control.

## Bearing on the record

- **CASE-tmp3uarw, press variant.** This is the documented variant the
  case said it was waiting for, with the scope the design allows: an
  evaluator (the press) whose resources (advertising) the evaluated party
  (the federal government) allocates at its discretion, and whose coverage
  of that party moves inversely with the allocation, within paper and
  within presidency. The case can cite THEORY-tmplatcg for the
  association, and should keep its own sentence from A21: "evidence of an
  association, not by itself proof of a particular covert intent."
- **CLAIM-tmpjo2zr, the loop between institutions.** The data show one
  arrow of the claim's loop, the evaluated party's influence on the
  evaluator's resources going with the evaluator's output. They do not
  show the other arrow, the evaluator's output shaping the party's
  standing. No feedback over time is estimated beyond the Granger tables.
- **TERM-tmpe6jtq.** The authors measure bias relative to the other papers'
  average, which is the term's requirement of a standard set apart from
  the process judged, in its weakest form. If all four papers were
  captured alike, the test would not see it.

No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **An association.** Fixed effects remove the stable ideological match
  between a paper and a president, but not month-to-month shocks that
  move both advertising and coverage within a pair. The instrument is
  reported only in a footnote.
- **Advertising is one channel.** Laws, licences, debt relief and access
  are not measured, and the authors expect substitution among them to bias
  the estimate toward zero. The Economist passage they quote, on
  Clarín's licences and a law capping foreign stakes, is an example.
- **The early advertising series is reconstructed** from two days a month.
- **Small units.** Four newspapers, and one presidency carries much of the
  identifying variation (Table 3).
- **The version read is not the published one.** The published abstract
  reports 0.23 front pages and 18 percent of a standard deviation. The
  differences between the versions are not known here.

## Open questions

- Does the published version's smaller effect come from a changed sample
  or specification? A reading of the AEJ article would say.
- Would an exogenous shift in advertising, such as Szeidl and Szucs's
  ownership events, move coverage in the Argentine papers too?
