# LEAD-099 progress

- Lead: LEAD-099, whether the league, the club or its supporters count the
  2005 Washington Nationals as the original Senators' continuation.
- Branch: claude/lead-099-franchise-count (cut from origin/staging).
- Targets: CLAIM-329 (its named test, the "2005 Nationals" defeater
  paragraph), QUESTION-118; context CASE-105, CLAIM-328.

## Task as understood

Read the league's (MLB) and the club's (Nationals) public statements on
franchise history, and supporters' usage on the web, from lawful public
pages. Write coding rules first, then code how each party counts the 2005
Nationals relative to (a) the Montreal Expos and (b) the original
Washington Senators (1901-1960) and expansion Senators (1961-1971). File
the verdict as Proposed empirical CLAIMs (alternatives where readings
differ), a CASE if it fits, LITs for the sources relied on, dated notes,
a changelog fragment.

## Step 1: already held?

Checked 2026-11-23: no changelog fragment for LEAD-099; no dated note on
LEAD-099, CLAIM-329, QUESTION-118, CASE-105 or CLAIM-328 reports the
lead's result. Not held.

## Done

- Branch cut; step 1 check.
- Coding rules written before reading (CODING.md).
- Sources read 2026-11-23; coded statements in statements.tsv, refusals in
  obstacles.tsv (a file named findings.md was refused by the harness as a
  report file, so the data went to TSV).
- Verdict by the rules: LEAGUE's own voice not reached (mlb.com 406); every
  page stating the standard count (Hall of Fame, Baseball-Reference, AP)
  is C-EX and D-SEN. CLUB: heritage only (H-SEN), "a new team" at founding,
  Senators and Expos records on separate pages; Ring of Honor honours both
  Senators clubs, the Expos and the Homestead Grays as Washington baseball.
  SUPPORTERS (two pages): no C-SEN; one D-SEN, one claims the Senators'
  legacy for Washington against the Expos' without their records.
  PRESS counts franchise (Expos) and city (1924) at once.
- Read, not coded and not registered: The Hoya 2019, Bleacher Report
  (Wood), SABR (Thornley 2024; Thorn 2018 repost), IBWAA (Livacari 2023),
  Fox Sports 2017, Wikipedia "History of the Washington Nationals",
  District on Deck (Wilkerson 2025).

## Choices

- LITs only for sources relied on: NBC Sports Washington 2020; Wikipedia
  "Washington Nationals"; Baseball Hall of Fame team page;
  Baseball-Reference WSN page; AP via SI 2019; The W board thread 2004;
  District on Deck (Bestwick 2023). Each primary or reference document gets
  a LIT and a NOTE and no THEORY (as LIT-tmp0go6t was filed).
- Verdict as a Proposed empirical thesis CLAIM grounded in an
  executed-study CASE; its bearing on CLAIM-329 as two alternative
  interpretive claims (lean: the defeater is not met).

## Filed (2026-11-23)

- LIT/NOTE pairs: LIT-tmpsigvb/NOTE-tmpr4az8 (NBC Sports Washington
  2020), LIT-tmpccmbp/NOTE-tmp89bvx (Wikipedia), LIT-tmpx9m37/NOTE-tmp41tft
  (Hall of Fame), LIT-tmpb3jca/NOTE-tmpomjp5 (Baseball-Reference),
  LIT-tmpwbrdw/NOTE-tmpdyoej (AP via SI 2019), LIT-tmp7a59o/NOTE-tmpleeno
  (The W board 2004), LIT-tmpa65x4/NOTE-tmp5w6pe (District on Deck 2023).
- CASE-tmp44mzc (executed-study, documented, Proposed).
- CLAIM-tmp7z7si (verdict; thesis, empirical), CLAIM-tmpl3ubq (lean;
  thesis, interpretive), CLAIM-tmpzrzml (alternative; counter,
  interpretive, objects_to CLAIM-329).
- Dated notes on LEAD-099, CLAIM-329, QUESTION-118, CASE-105, CLAIM-328;
  changelog fragment record/changelog.d/lead-099.md.
- Narrow diagnosis with luria.ref_status.scan on the changed files: no
  unused, lost or dangling excuse, no unexcused citation of the new codes
  (an excuse block ends at a blank line; fixed in LEAD-099 and CLAIM-329).

## Next

- Nothing for the worker. The owner chooses between CLAIM-tmpl3ubq and
  CLAIM-tmpzrzml, and may want the league's own pages read from a client
  mlb.com does not refuse.
