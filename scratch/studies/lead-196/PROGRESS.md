# LEAD-196 progress

- Lead: LEAD-196, "Read the consumer-resource competition works"
- Branch: claude/lead-196-consumer-resource (cut from origin/staging)
- Advances: CLAIM-369, QUESTION-132, QUESTION-083

## Task as understood

Read Chesson 1990 (LIT-1826, Unfetched; author's reprint located on the
University of Arizona faculty pages). Chesson 1994 is already held
(LIT-1827, Unavailable): seek a lawful copy again, read it if reached.
Servan and Allesina is already held and read (LIT-1824, NOTE-1422): no
second code. File NOTE, THEORY, dated notes on CLAIM-369, QUESTION-132,
QUESTION-083, CASE-118, LEAD-196; curation entry; changelog fragment.

## Check (step 1)

- No dated note on LEAD-196; no changelog fragment names it.
- The curation entry of 2026-11-22 (132527) lists LEAD-196 as not held.
- LIT-1826 Unfetched, LIT-1827 Unavailable, LIT-1824 Active (read).

## Done

- Step 1 check.
- Chesson 1990 sought 2026-11-22, not reached:
  - author's reprint (eebweb.arizona.edu): proxy 503 "upstream connect
    error ... connection timeout" over http, reset over https;
  - Wayback capture 20240413215848 of the reprint, located by the
    availability API: web.archive.org tunnel closed mid-exchange
    (agent proxy, ws_closed_mid_exchange) — this client's network;
  - CiteSeerX 10.1.1.361.5142 redirects to web.archive.org, same;
  - OpenAlex closed; Semantic Scholar gives only the author's reprint.
  So LIT-1826 stays Unfetched.
- Neighbour read in full: Chesson (2011), "Ecological Niches and
  Diversity Maintenance", InTech, doi:10.5772/24534, CC BY 3.0, from the
  publisher's own PDF (https://www.intechopen.com/chapter/pdf-download/21528).
  core.ac.uk download gave a Cloudflare challenge (stopped there). The
  chapter restates the 1990 paper's reworking of MacArthur's model (its
  ref. [28]) with Table 1's ρ, s, κ.
- Chesson 1994: Semantic Scholar CLOSED, OpenAlex closed, no copy found by
  search. Stays Unavailable.
- Computation: chesson_overlap.py + tests (41 pass). ρ is the cosine of
  u_j = c_j √(vK/r); κ_j = (Uᵀb − μ)_j/‖u_j‖; invasion against a lone
  resident = ‖u_i‖(κ_i − ρκ_j).

## Choices

- The 2011 chapter is filed as a neighbour (ADR-114), own LIT/NOTE/THEORY.
- Alternatives on whether it settles CASE-118's open point: (A) settled
  for MacArthur's Lotka–Volterra overlap by the author's own restatement;
  (B) not settled until 1990 is read, whose "measures of association" may
  differ. Lean A, file both.

## Filed (all pushed)

- LIT-tmp7sngn (Chesson 2011, Active), NOTE-tmp6d961 (Read),
  THEORY-tmpac7iw, CLAIM-tmpv65bg, ARG-tmpyjmij (all Proposed).
- LIT-1826 v2 (still Unfetched; status note, history, Standing).
- Dated notes: LIT-1827, CASE-118 (+draws_on), CLAIM-369, QUESTION-132,
  QUESTION-083, CLAIM-279, LEAD-196.
- Curation entry record/curation.d/2026/11/22/235643.md; changelog
  record/changelog.d/lead-196.md.
- Narrow ref_status scan of the changed files: no unused excuses, no
  unexcused new citations.

## Next

- Report to the lead. Remaining for the owner: allow web.archive.org (or
  supply a copy) to read Chesson 1990; a copy of Chesson 1994; choose
  between the alternatives on CASE-118 and QUESTION-083; the two ideas
  offered in the curation entry; lead status.
