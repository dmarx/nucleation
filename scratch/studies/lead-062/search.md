# LEAD-062 search, 2026-11-22

Routes: the Europe PMC REST search API
(`https://www.ebi.ac.uk/europepmc/webservices/rest/search`, resultType lite,
pageSize 10-25) and the arXiv API (`export.arxiv.org/api/query`). No email
address sent. No bot check met.

## Queries

Europe PMC:

1. `("future generations" OR "intergenerational") AND ("inclusion of other in self" OR "self-continuity" OR "self-other overlap" OR "intergenerational identification")` - 118 hits
2. `"future generations" AND ("overlap" OR "inclusion of") AND ("self") AND (concern OR beneficence OR donation)` - 3,823 hits, first 15 off topic but one
3. `("legacy motivation" OR "legacy concern" OR "legacy priming") AND (anonymous OR anonymity OR "no one will know" OR recognition OR remembered)` - 10 hits
4. `"future self-continuity" AND ("future generations" OR intergenerational OR legacy)` - 33 hits
5. `("identification with future generations" OR "connectedness to future generations" OR "closeness to future generations" OR "psychological distance to future generations" OR "kinship with future generations")` - 2 hits
6. `"perceived collective continuity" AND (future OR prosocial OR concern OR sacrifice)` - 11 hits
7. `"identity fusion" AND ("future generations" OR legacy OR posterity)` - 19 hits
8. `"inclusion of other in the self" AND (identification OR "group identification") AND (helping OR donation OR sacrifice OR prosocial) AND (control* OR "unique" OR "over and above")` - 68 hits
9. `("future self-continuity" OR "self-continuity") AND (altruism OR prosocial OR donation) AND (liking OR caring OR closeness)` - 32 hits

arXiv:

10. `abs:"future generations" AND (abs:"self-continuity" OR abs:"identification" OR abs:"legacy")` - nothing relevant
11. `abs:"inclusion of other in the self"` - one hit, on AI companionship, off topic

## Screened in

| work | id | why | outcome |
|---|---|---|---|
| Simić, Sacchi & Perugini 2025, "Our ways will not change" | PMC11687412 | manipulates a temporal continuity (the national group's, 50 years on) with identification measured separately | read in full, Europe PMC fullTextXML |
| Law, Syropoulos, Young & O'Connor 2025, seventh generation stewardship | PMC12569012 | "targeting the interconnectedness of people across time" expands intergenerational concern | Europe PMC fullTextXML answered HTTP 500 three times; Unfetched |
| Law, Syropoulos, Coleman & Young 2023, "A Future Beyond Ourselves" | PPR721445, doi 10.31234/osf.io/29jeb | future self-continuity against responsibility for, and identification with, future generations; 10 studies | Europe PMC holds the abstract only; the OSF copy is outside this lead's routes; Unfetched |
| Law, Young & Syropoulos 2026, one-year longitudinal | PPR1356834, doi 10.31234/osf.io/e4y58 | cross-lagged future self-continuity and intergenerational concern | abstract only; Deferred |

## Screened out (examples)

Syropoulos et al. 2024 (PMC10986099; intergenerational concern and legacy
concern, no continuity measure); Zha et al. 2026 (psychological ownership
of nature); Kuo et al. 2026 (imagined future generations, no self
measure); He et al. 2026 (self-other overlap with one's aged self, ageism);
Imada et al. 2025 (intergroup cooperation across generations).

## Finding

No study found measures felt continuity with future people or with one's
legacy apart from caring and asks whether concern for them follows it. No
study found varies whether anyone will know of a legacy act.
