# LEAD-054: experience-sampling studies of flow with affect in the episode

Search run 2026-11-22.

    python3 -I search.py OUTDIR            # Europe PMC REST + arXiv API; writes OUTDIR/hits.json
    python3 -I screen.py OUTDIR/hits.json > screening.tsv
    python3 -m pytest -q test_search.py

No email address is sent to any service (ADR-008). `counts.txt` holds the
query strings and hit counts as run. Europe PMC also indexes PsyArXiv
preprints (source `PPR`), so PsyArXiv was searched through it.

## Counts

- Europe PMC, five flow queries: 53 + 15 + 1 + 9 + 12 hits; arXiv, two
  queries: 0 + 2; 83 unique records after merging by DOI or id.
- Screened on title and abstract against I1 (flow reported at the signal,
  during the activity), I2 (affect at the same signal), I3 (the two related
  or compared): 6 qualify (Q), 7 sample flow but name no affect relation (U),
  70 excluded (X; most are ESM studies of other things that say "the flow of
  daily life").
- Supplementary, by targeted Crossref title search and from the two read
  papers' citations: 6 records, 4 Q, 1 U, 1 X (diary).
- Qualifying in all: 10. None was held in `record/literature.d`.
- The second part of the lead, a measure separating intrinsic pleasantness
  from goal-conduciveness valence in flow: two Europe PMC queries, 0 hits.

## Obstacles (2026-11-22)

- OpenAlex: `api.openalex.org` answered "Rate limit exceeded" (shared
  no-key budget); not retried. Crossref and Semantic Scholar used instead.
- Tavares, Freire and Faria 2020 (CC BY): `onlinelibrary.wiley.com/doi/pdfdirect/10.1111/jora.12522`
  answered 403 with a Cloudflare challenge; not retried. No PMC copy.

## Read

- Rheinberg et al. 2007, the version of record self-archived by the
  University of Potsdam (publishup docId 1785).
- Engeser and Baumann 2014/2016, the published PDF on the authors'
  department pages at the University of Trier.

The two papers report what appears to be the same Potsdam sample (101
employees, newspaper recruitment, 30 euros, age 18 to 60, about 70% women);
Engeser and Baumann do not say so. They are not independent evidence.
