---
number: 480
status: Active
formerly:
- THEORY-tmpa54f5
title: "Where a general-search monopoly was kept by exclusive distribution deals, the court in United States v. Google treated the user-interaction data that scale produced as a fruit of the violation and ordered the raw data and index metadata shared with qualified competitors, but not the engineered signals and models built from them, as a behavioural remedy while rejecting divestiture; that the sharing will let rivals compete is the court's expectation, not a finding"
version: 2
history:
- version: 2
  date: '2026-10-30'
  note: >-
    Narrowed and promoted by the twenty-fourth status review, at the status
    review's ruling (the owner delegated these rulings); ADR-065, ADR-057.
    This answers, for this entry, the report-title question the promotion
    audit left open on 2026-10-21. The title reports the remedies opinion
    and keeps the court's hedge. NOTE-004 read the opinion in full, and
    nothing in the record contradicts the report. The old title said the
    court "held that sharing ... can restore rivals' ability to compete".
    The opinion orders the sharing to deny a fruit and unfetter the
    market. It also accepts testimony that the shared data will not let
    rivals clone Search (NOTE-004, C16). So the title now says what was
    ordered, and leaves its effect as the court's expectation. That was an
    imprecise statement, and correcting it drops nothing (ADR-047, kind
    3). The old title: Where a general-search monopoly was kept by exclusive distribution deals, the court in United States v. Google treated the user-interaction data that scale produced as the fruit to be remedied, and held that sharing the raw data and index metadata, but not the engineered signals and models built from them, can restore rivals' ability to compete without breaking the firm up; that the sharing will work is the court's expectation, not a finding. The old promote_when asked what the decree did,
    which the title concedes is unknown: "An account of what the decree in
    United States v. Google did once Qualified Competitors had used the
    index snapshot, the Glue and RankEmbed data and the syndication
    licence: whether their results closed the gap on long-tail queries,
    and whether search share moved, compared with rivals or periods
    without the data. It is supported if the data measurably improved
    rivals' long-tail quality and their share, and in trouble if rivals
    that took the data gained nothing, or if the privacy treatment left
    too little of it to use. The court's reasoning, the appellate history
    and the decree's terms cannot settle it, since they say what the court
    expected, not what happened." It moves unchanged to QUESTION-352 (ADR-065 §3).
tags:
- society-and-governance
- information-retrieval
date: '2026-10-16'
source:
- LIT-006
bears_on:
- QUESTION-352
summary: >-
  Mehta (2025), [LIT-006](../literature.d/LIT-006.md), the remedies opinion, read in full in [NOTE-004](../notes.d/NOTE-004.md).
  The court finds that exclusive distribution produced a scale advantage
  (9× the queries of all rivals; 93% of unique phrases seen only by
  Google), calls it a fruit of the violation, and remedies it with raw
  data and syndication rather than with divestiture, on a sliding scale
  of causal connection. Whether the shared data will let rivals compete
  is untested; the parameters that decide it were left to a Technical
  Committee. The opinion also finds no proof that search scale gives
  Google's GenAI a quality edge (op. p. 156), which is an absence of
  proof, not a finding that there is none.
---

# THEORY-480: Where a general-search monopoly was kept by exclusive distribution deals, the court in United States v. Google treated the user-interaction data that scale produced as a fruit of the violation and ordered the raw data and index metadata shared with qualified competitors, but not the engineered signals and models built from them, as a behavioural remedy while rejecting divestiture; that the sharing will let rivals compete is the court's expectation, not a finding

## Source

Mehta (2025), [LIT-006](../literature.d/LIT-006.md), the remedies opinion in *United States v. Google
LLC* (D.D.C., ECF No. 1436, filed 2 September 2025), read in full in
[NOTE-004](../notes.d/NOTE-004.md). Page references are the opinion's own ("op. p.").

## What was actually shown

**The wrong and its fruit.** Liability rests only on exclusive distribution
agreements, not on product design, Chrome or self-preferencing (op. pp.
9–11). The fruits the court identifies are freedom from threats, scale and
revenue (op. pp. 82–97). Scale is carried forward from the liability
opinion: Google receives 9× the queries of all rivals combined (19× on
mobile); 13 months of NavBoost data is about 17.5 years of Bing's; of 3.7M
unique phrases over 7 days, 93% were seen only by Google and 4.8% only by
Bing (op. pp. 89–95). Long-tail queries are about a third of volume and 90%
of distinct queries.

**The causal standard.** "Significant causal connection" is not but-for
causation. "The more drastic the remedy, the greater the causal connection
required" (op. p. 73, following *New York v. Microsoft*). The court grades
the liability-phase inference as stronger than in *Microsoft*, enough for
behavioural remedies, not structural ones (op. pp. 74–82). So Chrome and
Android divestiture, the payment ban and choice screens are rejected.

**The tailoring.** What is shared is the input scale produced: a one-time
snapshot of six index fields per document, the data underlying Glue and
RankEmbed "at least twice" under a cap and privacy treatment, and five-year
search and text-ads syndication (op. pp. 136–186). What is not shared is
what Google engineered from it or what scale earned: ranking signals,
models, the Knowledge Graph, ads data. The court accepts the testimony of
Google's own expert, qualified on cross-examination, that sharing raw Glue
and RankEmbed data will not let rivals clone Search (op. pp. 159–163;
[NOTE-004](../notes.d/NOTE-004.md) C16).

**What could have come out otherwise.** The court could have found the
causal inference strong enough for structural relief, or found scale not a
fruit at all. It did neither.

## What this does not say

- **That the remedy works.** No one has used the data yet. The cap, the
  privacy treatment, the syndication taper and who qualifies are delegated
  to the Technical Committee and the final judgment ([NOTE-004](../notes.d/NOTE-004.md),
  Limitations). Both privacy experts agreed raw logs can re-identify users,
  and the EU Digital Markets Act precedent excluded 99% of queries after
  filtering (op. pp. 161–164). Whether it does is [QUESTION-352](../questions.d/QUESTION-352.md).
- **That search data is a moat for LLMs.** The court found plaintiffs "did
  not establish that Google's scale advantage in Search translates into a
  quality advantage in GenAI search-assisted responses" (op. p. 156), and
  so ordered no Gemini training data shared. That is a failure of proof on
  this record, not a finding of no advantage. Citing the opinion for the
  moat would be citing it for the opposite of what it holds.
- **That remedies declined were judged ineffective.** Several were refused
  for want of evidence (popularity signals, synthetic queries, publisher
  opt-out, Vertex access never requested), not on the merits.
- **That this is settled law.** It is a district-court opinion, and the
  court says it is "prepared to revisit" a payment ban (op. p. 128).
- **Anything about how LLMs work.** The GenAI findings restate testimony at
  a lay level under the court's own heading "Greatly Simplified".

## Connections

- [THEORY-150](THEORY-150.md) and [THEORY-470](THEORY-470.md), Doctorow's account of platform decay,
  name competition and interoperability as checks, and the talk read in
  [NOTE-041](../notes.d/NOTE-041.md) counts this case among the antitrust revival. This opinion is
  the record's one primary document on how such a check is designed, and
  it chose data sharing over structure.
- [THEORY-152](THEORY-152.md) (exit and voice) treats exit as a recuperation mechanism.
  The court's default-bias findings (op. pp. 83–85; of users paid to
  switch to Bing for 14 days, 33% stayed) bear on how far exit operates in
  this market.
