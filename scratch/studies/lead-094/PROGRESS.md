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

## Status: done (all readable works filed); no pull request opened

## Done

- Step 1: no changelog fragment for lead-094; none of the twelve LITs had a
  NOTE or THEORY; no duplicate LIT by identifier.
- Ott and Antonsen 2008 read in full; 2009 sequel (arXiv:0902.2773, not
  held) registered and read as a supplement. Filed LIT-2248 Active (v2),
  LIT-tmpd7koy, NOTE-tmpd7trg, NOTE-tmp5oph4, THEORY-tmpmvcnr,
  THEORY-tmp0d58z.
- Computation: `oa_invariance.py` (+ pytest): the OA family is invariant
  for first-harmonic coupling only. Filed CLAIM-tmpo6ehq (demonstrated).
- Verdict: CLAIM-tmpa694z (leaned to: not a defeater) and CLAIM-tmpervl4
  (a defeater within its class), ARG-tmp5xhiv.
- Read: LIT-2241 Caprioglio (NOTE-tmp3gqv7, THEORY-tmpgdriu), LIT-2244
  Augustsson (NOTE-tmp3oxzv, THEORY-tmpq02z9), LIT-2231 Schmietendorf
  (NOTE-tmphm1ot, THEORY-tmpkt3xf).
- Skimmed: LIT-2257 Kaur (NOTE-tmpj6fck, THEORY-tmpqdy16), LIT-2268 Lee
  (NOTE-tmprzmfk, THEORY-tmpp4w4k), LIT-2252 Müller (NOTE-tmpnfczs,
  THEORY-tmpd9neo), LIT-2266 Hancock (NOTE-tmp3om59, THEORY-tmp31kx6;
  accepted manuscript from Oxford ORA).
- No copy: LIT-2254 Yadav, LIT-2255 Haken -> Unavailable. Blocked again:
  LIT-1638 Fenichel (ScienceDirect HTTP 403), LIT-1642 Knobloch (Annual
  Reviews Cloudflare challenge) -> stay Unfetched. Europe PMC REST returned
  HTTP 500 for PMC13333473 and PMC13148977; Frontiers publisher PDFs used.
- Dated notes on LEAD-094, CLAIM-478, -157, -172, -327, -331, -388, -394,
  -405, -481, -526, -626, QUESTION-218, -252, -281, -391.
- Excuses for works now Active removed from LEAD-094 and curation
  2026/11/07/015133.
- Changelog fragment record/changelog.d/lead-094.md; curation entry
  record/curation.d/2026/11/22/223102.md.

## Next (for the owner)

- Choose between CLAIM-tmpa694z and CLAIM-tmpervl4 (and so ARG-tmp5xhiv's
  status).
- Supply copies of Fenichel, Knobloch, Haken or Yadav, if wanted.
- Offers (not filed): a simulation lead on the actual approach rate to the
  OA manifold; questions on whether the chimeras' "metastability" is
  Hancock's, and on heavy-tailed residences vs Hancock's dwell-time test;
  a revision of CLAIM-478 if CLAIM-tmpervl4 is adopted.

## Choices

- No subagent tool was available, so readings were done by the worker
  itself, not delegated; the running notes live here instead of per-reader
  branches (read-and-file step 6, ADR-108).
- Ott and Antonsen 2009 registered as a supplement (ADR-114) because the
  verdict turns on whether the 2008 manifold attracts.
- Skimmed rather than read for the four long works, in priority order, to
  finish the batch in one run; each NOTE's history lists what was skipped.
- Quotations checked by script (scratchpad tools/qcheck.py) against the
  downloaded texts; downloads kept in the scratchpad only.
