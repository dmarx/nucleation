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
  The API (export.arxiv.org) returned HTTP 429 on the fourth query; not retried.
- Read arXiv:1111.7130v2 in full (PDF from arxiv.org). Crossref: J. Chem. Phys.
  138, 2013, DOI 10.1063/1.4773405.
- Pre-registration committed (PREREGISTRATION.md), then two amendments, each
  committed before the run it governs.
- Study run: README.md has the table. VIC and ICN fail to transfer; harmful
  additions confirmed; TFF (post hoc) transfers to fresh architectures.

## Choices made

- Out-of-sample system: a kinetic constraint-growth model (kTAM-like), not
  origami. The lead names no specific system; the origami part is a reading
  task, and no lawful open multi-fold dataset was found to test on.
- The predictor generalizes the folding island as a race (VIC); an alternative
  (ICN) was registered beside it.

## Next

- File LIT, NOTE, THEORY for Arbona et al.; CASE; CLAIMs; dated notes on
  LEAD-183, QUESTION-380, CLAIM-562, CLAIM-599; changelog fragment.
