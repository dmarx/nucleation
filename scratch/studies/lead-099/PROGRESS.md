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

## Next

- File LITs and NOTEs, the CASE, the claims, dated notes, changelog.
