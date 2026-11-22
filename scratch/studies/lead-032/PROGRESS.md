# LEAD-032 progress

- Lead: LEAD-032 (advances QUESTION-045)
- Branch: claude/lead-032-dismantling-trials (cut from origin/staging at e3d34ee7f)
- Task: Europe PMC search for (a) dismantling trials that remove safety
  behaviour during exposure with exposure held fixed, and (b) individual-level
  data showing hysteresis or critical-transition signs in psychopathology.
  Log queries in search.md; register the decisive works; read up to three
  (read-and-file steps 5-9); dated notes on the entries advanced and on LEAD-032.

## Step 1 check (target held?)

Not held. The record holds LIT-1491 (standalone safety-behaviour
manipulations, outside exposure) and LIT-1500 (inhibitory-learning review),
and cites Meulders et al. 2016 (SB within exposure) only in NOTE-1128,
THEORY-901, THEORY-903, unregistered. No psychopathology individual
time-series / critical-slowing work is held (LIT-1956 is the generic
early-warning review). QUESTION-045 has no later filing answering it.

## Done

- Europe PMC searches run and logged (search.md, search.py, results/).
  OpenAlex hit its keyless rate limit (asks for an email; none sent).
- Copies:
  - Meulders et al. 2016 (meta-analysis): accepted manuscript located on
    KU Leuven Lirias
    (lirias.kuleuven.be/bitstream/123456789/529579/1/Meulders%20et%20al_CPR_accepted.pdf);
    fetch failed 2026-11-22 with "Recv failure: Connection reset by peer".
    Not retried. -> Unfetched.
  - Meckes et al. 2025: Europe PMC REST fullTextXML gave HTTP 500 (author
    manuscript, not in the OA subset); europepmc.org PDF render gave a
    Cloudflare "Just a moment..." challenge (stopped); read in full from
    pmc.ncbi.nlm.nih.gov/articles/PMC13245588/ (NIH author manuscript).
  - de Jong et al. 2023 HysTAR: read in full from PsyArXiv
    (osf.io/zrcft/download, CC BY), sections 1-8; simulation tables skimmed.
- Readings (notes taken, not yet filed):
  - Meckes: 3-arm RCT, N = 56 spider-fearful adults, one 30-min exposure;
    experimenter-selected novel SB (rubber boots) faded / unfaded / none.
    No time x condition interaction on any outcome at post or 1-month
    follow-up; SB raised approach in trial 1 and post-treatment
    acceptability. Moderation: faded SB worse at follow-up (disgust only)
    when SB lowered threat expectancy; unfaded SB helped high distress
    intolerance. Key limit for QUESTION-045: the SB is ADDED and novel,
    not the person's own maintaining behaviour cut.
  - HysTAR: method (Li et al. 2015 model brought to psychology) for
    hysteresis in a bivariate series (control z, outcome y), two
    thresholds r0 < r1. Depression demonstrated only on data simulated
    from Cramer et al. 2016's network (r1 - r0 = 0.88); the one empirical
    case is speed-accuracy (Dutilh et al. 2011). "has not been used to
    investigate hysteresis in empirical psychological time series, so
    far." Needs the control variable observed crossing both thresholds.

- Third read: Smit et al. 2025 (37 people, not 41) from the PsyArXiv
  preprint; Groningen's copy showed a Cloudflare challenge. A second
  PMC fetch (after the shared scratchpad's dl/ vanished) met a reCAPTCHA.
- Filed: 9 LITs (3 Active read, 5 Deferred, 1 Unfetched), 3 NOTEs, 3
  THEORYs; dated notes on QUESTION-045, THEORY-058, TERM-020, CLAIM-446,
  LEAD-032; curation 2026/11/22/133829; changelog lead-032.md; README.

## Choices made

- Three reads: the most recent dismantling RCT with an open copy
  (Meckes), the one hysteresis method paper (HysTAR), and the larger
  individual CSD replication (Smit) over the single-patient Wichers 2016,
  because it gives sensitivity/specificity. Meulders was the first choice
  and is Unfetched.
- Registered only works the notes cite; the rest stay in search.md.
- Whether Smit meets THEORY-058's promote_when route 1 is left to the
  owner; no status changed.

## Next

- Nothing for this worker. Remaining for the lead: read Meulders when
  Lirias answers; Salkovskis 1999 and Powers 2004 if a lawful copy turns
  up. The lead opens the pull request.
