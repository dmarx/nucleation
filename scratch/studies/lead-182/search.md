# LEAD-182 literature check: query log

Date: 2026-11-22. No email address was sent to any service (ADR-008): no
`mailto=`, no `email=`, no address in a header or user agent. Scripts used
lived in the session scratchpad; downloads went there too, never here.

Question: has anyone published an adequately powered Contextuality-by-Default
(CbD) test on human pragmatic judgements, with signalling accounted for and
outcome coding fixed in advance? The baseline is CASE-053 (search of
2026-10-10), which found none. This check looks for anything since, and for
anything CASE-053 missed.

## Europe PMC REST (`/webservices/rest/search`, format=json, resultType=lite)

| # | Query | Hits | Relevant |
|---|-------|------|----------|
| E1 | `"contextuality-by-default"` | 45 | Bruza, Lee and Hoyte 2025 (faces, crowdsourced CbD, PMC12386047); Wang and Sadrzadeh 2024 (garden-path, BERT probabilities, PMC10822712); Basieva et al. 2019 (already in CASE-053); the rest theory, physics or position papers |
| E2 | `contextuality AND (pragmatic OR implicature OR "speech act" OR anaphora OR pronoun OR Winograd OR coreference)` | 124 | only Wang and Sadrzadeh 2024 again; the rest is noise (health services, ethics) |
| E3 | `(contextuality OR "Bell inequality" OR CHSH) AND (ambiguity OR "word meaning" OR disambiguation OR "sentence interpretation" OR "garden path")` | 176 | Wang and Sadrzadeh 2024; Aerts et al. 2026 (PMC13298953, quantum structure in AI language; word statistics, not judgements); Leggett-Garg in perceiving cups (2024, perception) |
| E4 | abstracts (resultType=core) of MED 38281713, 40870340, 42495220, 41929793, 41306040, PMC13298953 | | read to sort them; only 40870340 (Bruza et al.) reports a CbD test on elicited human judgements |

## arXiv API (`export.arxiv.org/api/query`, sorted by submission date)

| # | Query | Relevant |
|---|-------|----------|
| A1 | `abs:contextuality AND (abs:pragmatic OR ... )` | ungrouped OR parsed loosely; noise only. Rerun as A2-A6 |
| A2 | `abs:"contextuality by default"` | Dzhafarov and Cervantes 2026, "Degrees, Levels, and Profiles of Contextuality" (2603.26692, method); Lo, Sadrzadeh and Mansfield 2024 (LLMs, held as LIT-844); Kumar et al. 2026 (LLMs); Sassoli de Bianchi and Leporini 2026 reply (word statistics); the rest held or older method papers |
| A3 | `abs:contextuality AND abs:ambiguity` | noise |
| A4 | `abs:contextuality AND abs:pragmatics` | noise (LLM pragmatics benchmarks without contextuality analysis) |
| A5 | `abs:contextuality AND abs:anaphora` | Lo, Sadrzadeh and Mansfield 2024 (2402.04505, cited in CASE-053) |
| A6 | `abs:contextuality AND abs:sheaf AND abs:language` | Lo et al. 2023 Winograd (2308.16498, in CASE-053); the rest held |
| A7 | `au:Sadrzadeh AND abs:contextuality` | nothing after 2412.16806 |
| A8 | `au:Dzhafarov AND submittedDate:[2024 TO 2026]` | 2603.26692 (above); 2511.01783 (book preface) |
| A9 | `abs:contextuality AND abs:"human judgements"` / `"human judgments"` | only 2308.16498 |
| A10 | `abs:contextuality AND abs:crowdsourced` | noise |

## OpenAlex (`api.openalex.org/works`, no mailto, no key)

| # | Query | Result |
|---|-------|--------|
| O1 | `search=contextuality-by-default`, from 2023-01-01 | **Refused: "Rate limit exceeded ... Insufficient budget. This request has no API key"** (2026-11-22). Stopped here, as the brief requires; not retried. The response offered an API key in return for an email address, which was not sent. |
| O2 | `search=contextuality pragmatic judgments experiment`, from 2022-01-01 | Same refusal (sent in the same call, before the first was seen). |

## Result

No powered CbD test on human pragmatic judgements was found. Since CASE-053:

- one new CbD test on elicited human judgements, Bruza, Lee and Hoyte 2025
  (real versus AI-generated faces; perceptual content, nine of twenty
  "coins" contextual by bootstrap);
- one new signalling analysis on psycholinguistic content, Wang and
  Sadrzadeh 2024, whose probabilities are BERT's, not human judgements;
- one method paper, Dzhafarov and Cervantes 2026, on degrees of
  contextuality.

The check is limited: OpenAlex was refused, so the coverage of journals
outside Europe PMC's index and arXiv rests on CASE-053's earlier search.
