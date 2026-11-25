# LEAD-099 coding rules

Written 2026-11-23, before any source was read for this lead.

## Units

A **statement** is one passage on one page that says or shows how the 2005
Washington Nationals stand to an earlier club: the original Washington
Senators of 1901-1960 (S1, now the Minnesota Twins), the expansion Senators
of 1961-1971 (S2, now the Texas Rangers), or the Montreal Expos of
1969-2004 (EX). A page may yield several statements.

## Party

Each statement is coded to one party, by who publishes it:

- **LEAGUE**: Major League Baseball (mlb.com pages outside a club's own
  section, MLB press releases, the league's official historian), and the
  Baseball Hall of Fame only as a check, coded separately as HOF.
- **CLUB**: the Washington Nationals organization (its section of mlb.com,
  its media guide, its press releases, its ballpark's displays as the club
  describes them, and its officers quoted in reputable reporting).
- **SUPPORTERS**: fan blogs, supporter sites and forums, and fan-facing
  usage quoted in reporting. Reporters' own framing is coded **PRESS**,
  not SUPPORTERS.

## Codes (one per statement, the strongest that fits)

- **C-SEN (continuation of the Senators)**: the statement counts the
  Nationals as the same franchise or club as S1 or S2: records,
  statistics, retired numbers, pennants or franchise years are combined
  across the gap, or the Nationals are said to be the Senators returned
  as the same club (not "baseball returned").
- **H-SEN (heritage of the Senators)**: the statement claims or honours
  S1 or S2 as Washington's baseball history, the city's or the club's
  heritage, by commemoration (Ring of Honor, statues, throwback uniforms,
  "Washington baseball history"), without combining records or saying it
  is the same franchise.
- **C-EX (continuation of the Expos)**: the statement counts the
  Nationals as the same franchise as EX: franchise records, all-time
  leaders or franchise years run from 1969 through Montreal.
- **D-SEN (disclaims the Senators)**: the statement says the Nationals
  are not the Senators' franchise, or assigns S1's and S2's records to
  the Twins and Rangers.
- **D-EX (disclaims the Expos)**: the statement says the Nationals do not
  continue the Expos, or drops Montreal from the club's history.

A statement that shows both H-SEN and C-EX (the usual expectation) is coded
as two statements.

## Verdict rule, per party

- A party **counts the Nationals the Senators' continuation** if it has
  at least one C-SEN statement and no D-SEN statement that it has not
  withdrawn.
- A party **claims the Senators as heritage only** if its statements are
  H-SEN (with or without D-SEN) and none is C-SEN.
- A party is **divided** if its statements include both C-SEN and D-SEN
  that stand together (most likely among supporters).
- **Not found** if no statement of that party was reached.

For SUPPORTERS the verdict reports what was found, not a census: a handful
of supporter pages cannot say how supporters divide (CASE-105 already says
the record has no data on that).

## Recording

Each statement goes into findings.md with: party, code, the page's URL,
the date read, and a short verbatim quote. A page refused by a bot check,
a 403 or 429, or a paywall is recorded with the obstacle and not retried.
