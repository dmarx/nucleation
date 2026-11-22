# LEAD-157 progress

- Lead: LEAD-157 (advances QUESTION-069, CLAIM-263, CLAIM-187)
- Branch: claude/lead-157-loss-barriers (cut from origin/staging)

## Task as understood

Train small numpy networks; align pairs by permutation (weight matching and
activation matching); measure the loss barrier along several path families
(linear, aligned linear, fitted curve, piecewise via a centre); build a pair
known to share a mechanism by an independent test and ask whether alignment
always removes its barrier (CLAIM-263's defeater).

Step 1 check: no case, claim or study in record/ or scratch/studies/ holds
an executed permutation-alignment barrier study (grep of "permutation
alignment", "loss barrier", "linear mode connectivity"; only the lead,
CLAIM-263, CLAIM-187, QUESTION-312 and curation entries mention it).

## Done

- Step 1 check (not held).

## Next

- Write the code and tests; run; file a CASE and CLAIM(s); dated notes.
