# LEAD-118: the Unfetched works through the Europe PMC REST route

Run on 2026-11-22. For each of the 48 LITs that LEAD-118 lists (all still
Unfetched), `epmc_lookup.py` searches Europe PMC's REST API by DOI (falling
back to title), and where the hit has a PMCID asks the documented full-text
route `rest/<PMCID>/fullTextXML` for it. It also searches by title for other
versions Europe PMC indexes (preprints, source PPR) and asks the same route
for those. No email address is sent in any request (ADR-008); the
User-Agent is generic.

Rerun from the repository root:

    python3 -m pytest -q scratch/studies/lead-118/
    python3 -I scratch/studies/lead-118/epmc_lookup.py --out scratch/studies/lead-118/results.tsv

`results.tsv` has one row per LIT: code, identifier, PMID, PMCID,
`isOpenAccess`, the HTTP status of `fullTextXML`, the result
(open-full-text / abstract-only / not-found / obstacle), the obstacle, and
other versions with their `fullTextXML` status.

## Result

| result | count |
|---|---|
| open full text through the REST route | 0 |
| abstract only (PMID, no PMCID) | 31 |
| not found in Europe PMC | 5 |
| obstacle: PMCID held, `fullTextXML` answers HTTP 500 | 12 |

The 12 obstacles are all works free to read at PMC but outside the
open-access subset (`isOpenAccess: N`). The full-text route serves only the
open-access subset: a control article in it (PMC1762313) was served (HTTP
200) in the same session, so the 500s are the route declining these works,
not an outage. Four works have a bioRxiv preprint indexed (PPR21674,
PPR30232, PPR21684, PPR599073, for LIT-1158, LIT-1572, LIT-1602, LIT-2176);
the route answers 500 for those too. Their bioRxiv PDFs are lawful copies of
the preprints and were not fetched, the run's scope being the REST route.

No downloaded text is committed.
