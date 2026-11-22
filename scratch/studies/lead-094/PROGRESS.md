# LEAD-094 progress

- Lead: LEAD-094, "Read the dynamics batch on scale separation and localized
  structure, with Ott and Antonsen's reduction as a candidate defeater"
- Branch: `claude/lead-094-dynamics-batch` (cut from origin/staging)
- Task: read Ott and Antonsen 2008 (arXiv:0806.0004, LIT-2248) first, as the
  candidate defeater (a) of CLAIM-478; then the batch's other open-access
  works (arXiv, Frontiers) in priority order; Fenichel (LIT-1638), Knobloch
  (LIT-1642) and Haken RMP (LIT-2255) only with a lawful copy. File a NOTE
  per work read, a THEORY per supported claim, a verdict as Proposed
  CLAIM(s), dated notes, changelog fragment.

## Done

- Step 1: no changelog fragment for lead-094; none of the twelve LITs has a
  NOTE or THEORY; no duplicate LIT by identifier. All twelve unread.
- Read Ott and Antonsen 2008 (arXiv:0806.0004v1) in full.
- Read, as a supplement the verdict needs, Ott and Antonsen 2009, "Long time
  evolution of phase oscillator systems" (arXiv:0902.2773v2), in full. Not
  held in the record; to be registered (ADR-114).
- Computation: `oa_invariance.py` shows the OA family is invariant for
  first-harmonic coupling only (defect 1e-16 vs 0.1 with a second harmonic).

- Filed OA (commit 6b4e6d198): LIT-2248 Active (v2); LIT-tmpd7koy (supplement,
  Active); NOTE-tmpd7trg, NOTE-tmp5oph4 (Read); THEORY-tmpmvcnr,
  THEORY-tmp0d58z; CLAIM-tmpo6ehq (demonstrated); verdict alternatives
  CLAIM-tmpa694z (leaned to) and CLAIM-tmpervl4; ARG-tmp5xhiv.
- Dated notes (commit 9e4bbb037) on CLAIM-478, CLAIM-388, CLAIM-394,
  CLAIM-157, CLAIM-481, CLAIM-626, CLAIM-405, QUESTION-218, -252, -281, -391.
  Removed LIT-2248 from LEAD-094's excuse and from curation 2026/11/07/015133.

- Copies (2026-11-22): arXiv PDFs fetched for LIT-2241 (2405.14542), LIT-2244
  (2608.20517), LIT-2257 (2605.24135), LIT-2268 (2511.11815); Frontiers
  publisher PDFs for LIT-2231 and LIT-2252 (Europe PMC REST returned HTTP 500
  for PMC13333473 and PMC13148977); Hancock (LIT-2266) accepted version from
  Oxford ORA (ora.ox.ac.uk/objects/uuid:967c1662-3633-40ff-a524-dbd530e1078c/
  files/rjw827d81v).
- No copy: LIT-2254 (Yadav, PRE; OpenAlex no OA location; arXiv searched by
  title and authors) and LIT-2255 (Haken RMP; OpenAlex no OA; arXiv searched).
  -> Unavailable.
- Blocked: LIT-1638 Fenichel, sciencedirect.com/science/article/pii/
  0022039679901529/pdf, HTTP 403; LIT-1642 Knobloch, annualreviews.org/doi/
  pdf/10.1146/annurev-conmatphys-031214-014514, Cloudflare "Just a moment"
  challenge. Stopped; stay Unfetched. Neighbours already held: Kuehn
  (NOTE-1598) for Fenichel; Zelnik, Meron and Bel (NOTE-1909) for Knobloch.

## Next

- Read and file in order in order: LIT-2241, LIT-2254, LIT-2244, LIT-2257, LIT-2268,
  LIT-2231, LIT-2252, LIT-2266; try lawful copies for LIT-2255, LIT-1638,
  LIT-1642.

## Choices

- No subagent tool is available to this worker, so readings are done by the
  worker itself, not delegated; the running notes live here instead of
  per-reader branches (read-and-file step 6, ADR-108).
- Verdict lean (to file as alternatives): OA's reduction does not meet
  CLAIM-478's defeater (a) as worded: the closure holds by exact invariance
  (persistence's limit) in a restricted class (N infinite, first-harmonic
  coupling, analytic data, Lorentzian for finite dimension). Alternative: it
  meets (a) within its class, since its attraction (OA 2009) needs only
  Delta > 0 and no rate ratio, so CLAIM-478 should name invariant-manifold
  closure as a route needing no rate difference.
