# LEAD-192 progress

- Lead: LEAD-192, "Prove a projection perturbation bound for the coarse-graining claim, reading the biorthogonal diffusion wavelets first"
- Branch: claude/lead-192-projection-bound (cut from origin/staging)
- Advances: CLAIM-164. Named in NOTE-984 (Coifman and Maggioni, LIT-1256), whose open question asks for
  a bound of the form ||P_{V~_j} - P_{V_j}|| <= (something) * eps / gap_j for the compressed
  diffusion-wavelet algorithm across levels.

## Task as understood

1. Check the record does not already hold the bound or the reading (done: not held; no LIT for
   Maggioni, Bremer, Coifman and Szlam 2005; no changelog fragment or note names LEAD-192).
2. Read Maggioni, Bremer, Coifman and Szlam (2005), "Biorthogonal diffusion wavelets", from a lawful
   copy; file LIT, NOTE, THEORY per read-and-file.
3. Attempt the bound; if proved, file a CLAIM (Proposed, demonstrated) with the proof, plus a numpy/pytest check here.
4. Dated notes on LEAD-192, CLAIM-164 (and the entries the reading bears on), changelog fragment.

## Done

- Step 1 (already held?): not held.

## Next

- Locate a lawful copy of the biorthogonal paper.
- Write the proof and the numerical check.
