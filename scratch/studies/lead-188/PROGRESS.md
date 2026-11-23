# LEAD-188 progress

- Lead: LEAD-188, "Find production testimony of how the fan redub reached the reshoot, and compare a circulation-network model with the list of identifiable contributions"
- Branch: `claude/lead-188-fan-redub` (cut from origin/staging, 0f746cc90)
- Started and finished: 2026-11-23

## Task as understood

1. Check whether the result is already held.
2. Search interviews and trade press (lawful public pages) for production testimony of how the fan redub reached the reshoot of *X-Men: The Last Stand*. Coding rules first; each finding with URL and date read.
3. Build a small numpy network model of CASE-100 comparing a circulation route with the list of identifiable contributions, priced as CLAIM-332's defeater asks; pytest tests.
4. File an executed-study CASE, CLAIMs, dated notes, a changelog fragment.

## Done

- Step 1: not held. No changelog fragment names LEAD-188; CLAIM-332's note of 2026-10-30 says no case has had the comparison; CASE-100's note of 2026-10-29 says no production testimony on why.
- CODING.md written before reading; TESTIMONY.md: 11 findings coded, 2 sources not reached (Polygon refused by the fetch tool; The Playlist 403). Quotes of F1 to F4 checked verbatim against page HTML.
- model.py, test_model.py (8 passing), results.json, sensitivity.py, sensitivity.jsonl (36 settings), README.md.
- Filed: LIT-tmpcw761, LIT-tmpwof77, LIT-tmp7hzxw; NOTE-tmphwsps, NOTE-tmpurc5c, NOTE-tmpubj66; CASE-tmpktyr7; CLAIM-tmp24fw0, CLAIM-tmp4ybsw, CLAIM-tmp48sm1 (alternative A, the lean), CLAIM-tmp9av3u (alternative B); dated notes on LEAD-188, CLAIM-332, CASE-100, QUESTION-119, NOTE-1272; changelog fragment lead-188.md.

## Choices made

- Supplements (the three interviews) registered as LIT + NOTE without a THEORY: journalism, no account the record uses (read-and-file step 5, supplements).
- NOTEs Skimmed: only the passages on the film were read closely.
- With one observation, the exact Bayes factor is used rather than CLAIM-154's large-sample rule.
- Two readings of the testimony filed as alternatives; no ARG on whether CASE-100 grounds CLAIM-332, since its status turns on the owner's choice between them.

## Next

- None for this run. For the owner: choose between CLAIM-tmp48sm1 and CLAIM-tmp9av3u; a cross-case study (adoption against reach beyond the named distributors) would separate them; Polygon's interview and Ratner's own account remain unread.
- Pre-existing, not from this run: the narrow ref scan flags unexcused CLAIM-271 and CLAIM-332 in QUESTION-119, and CLAIM-192 and CLAIM-278 in CLAIM-332; left to CI's repair.
