# LEAD-111 progress

- **Lead:** LEAD-111 — Construct the operational cover as a family of contexts
  with restriction maps, or give the operational notion its own name.
- **Branch:** claude/lead-111-operational-cover (from origin/staging)
- **Advances:** CLAIM-251 (counter, Proposed), CLAIM-201 (thesis, Proposed),
  CLAIM-257 (thesis, Active).

## Task as understood

CLAIM-201 defines, operationally, "a context is a question whose answers
readers give determinately" and calls a change in which questions a population
answers determinately a "change of cover". CLAIM-251 objects: that is a
property of the responses (empirical model), not of the sheaf-theoretic cover
(which belongs to the measurement scenario); so the operational notion needs
its own name until a functorial/sheaf link is shown. The lead: either
construct the operational cover as a genuine family of contexts with
restriction maps (a sub-site), or give the operational notion its own name
(a TERM). Work formally; numpy-check small constructions.

## Finding

Construction: the operational cover is the determinacy sub-cover — select the
determinable measurements D = {x : max_o marginal_x(o) >= theta} and take the
induced sub-scenario (D, {C∩D : C in M}) with inherited restriction maps.
- Horn 1 (construct): the induced sub-family IS a genuine down-closed cover
  with inherited restriction maps (a sub-presheaf / sub-site).
- The selection e |-> K_theta(e) is a thresholded functional of the empirical
  model, on a fixed scenario M.
Two readings diverge on CLAIM-251, by a modeling choice the record has not
fixed (owner's call) -> file as ALTERNATIVES:
  - Reading A (model-level, fixed full scenario): operational cover is a
    functional of the model, not a cover; corroborates CLAIM-251; rename due.
  - Reading B (domain-level): determinable questions ARE the operational
    domain; the sub-site is the sheaf link CLAIM-251 asked for; "cover" is
    literally correct; objects_to CLAIM-251, corroborates CLAIM-201.
TERM naming the operational notion is needed under either reading (horn 2).

## Done

- Read CLAUDE.md, design principles, ADR-001, ADR-048, run-lead skill, record.md.
- Read lead + CLAIM-251/201/257/197, CASE-048, THEORY-012, TERM-042/039/043,
  QUESTION-005/023. Confirmed target NOT already held (no construction, no name).

## Next

- Write numpy study (presheaf functoriality; down-closed sub-cover; model-level
  selection; theta-dependence/non-injectivity; no-signalling overlap). pytest.
- File: CASE (construction), TERM (name), two alternative CLAIMs, changelog,
  dated note on LEAD-111.
