# LEAD-067 progress

- Lead: LEAD-067 (advances QUESTION-130)
- Branch: claude/lead-067-holonomy-null
- Task: build the finite evaluative-transport construction of QUESTION-130
  (A19 §8): three overlapping contexts, each a local representation of the
  same commitments; comparisons fixed on each overlap by shared commitments;
  transport derived from those; holonomy around the loop. First the null
  (different local coordinates, trivial holonomy), then a case with
  nontrivial holonomy whose transport is not chosen to produce it. numpy +
  pytest. File a CLAIM (demonstrated) and a CASE, dated notes on
  QUESTION-130 and LEAD-067, changelog fragment.

## Done

- Read LEAD-067, QUESTION-130, CLAIM-148, CLAIM-495, record.md fields.
- transport.py, test_transport.py (18 pass), run_study.py, results.json, README.md.
- CLAIM-tmpmov06 filed (null, gluing criterion, planar realization, underdetermination).
- CASE-tmpg9x2o filed (executed-study, documented, Proposed).
- Dated notes on QUESTION-130 (version 5, history entry, as its earlier notes did) and LEAD-067.
- Changelog fragment record/changelog.d/lead-067.md.

## Next

- Report to the lead (no PR opened, per the run-lead skill).

## Choices

- Gauge group O(d): a change of local coordinates preserves the context's
  comparisons (inner products). Transport derived by orthogonal Procrustes
  on the shared commitments; anything else would be chosen.
- Transport counts as derived only when the fit is unique (overlap anchors
  give a nonsingular cross-covariance). Underdetermined overlaps are shown
  to leave the holonomy free (LIT-038's arbitrariness).
- Nontrivial case: planar construction, holonomy = sum of each context's own
  internal comparison angle; plus curved charts (sphere of normalized
  profiles), holonomy -> spherical excess. The second's curvature belongs to
  the representation format, said so in the entries.
