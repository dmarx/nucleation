# LEAD-183 progress

- Lead: LEAD-183 (advances QUESTION-380).
- Branch: `claude/lead-183-nonmonotone-predictor`, cut from `origin/staging` at 48930bdb3.
- Task: state a predictor of productive seed sets, computed from the constraint
  architecture alone, that can flag supersets that lower the chance of reaching
  the target (UFI cannot: it is monotone in the actuator set; CLAIM-562's note
  of 2026-11-07); test it out of sample in a small numpy simulation with pytest
  tests; search and read the origami literature for multi-fold data in which a
  fold's melting temperature rises once a neighbour has closed; file a CASE,
  CLAIMs (Proposed), dated notes, a changelog fragment.

## Step 1: is it already held?

Not held (checked 2026-11-23). No changelog fragment or dated note names LEAD-183.
CLAIM-969 / CASE-374 score intermediates by committor, which needs the full
chain, not the architecture; CASE-374's two-seam trap is a hard-coded
incompatibility, not a superset of compatible seeds. CLAIM-562's note of
2026-11-07 states that UFI is monotone and files no replacement.

## Done

- Branch cut; PROGRESS.md pushed.
- arXiv API search (2026-11-23): found arXiv:1111.7130, Arbona, Aime and
  Elezgaray, "Cooperativity in the annealing of DNA origamis" (not held).
  The API returned HTTP 429 on the fourth query; not retried.

## Next

- Pre-register the predictor (PREREGISTRATION.md), commit before any test run.
- Build the test system and tests; run; record results.
- Read arXiv:1111.7130; file LIT, NOTE, THEORY.
- File CASE, CLAIMs, dated notes, changelog fragment.
