# LEAD-142 progress

- **Lead:** LEAD-142 — State the decision signature and prove or refute the
  eigenspace candidate for the **directed case**.
- **Branch:** claude/lead-142-directed-case (from origin/staging)
- **Advances:** CLAIM-209, QUESTION-052.

## Task as understood

The undirected (symmetric) result: the top eigenspace of the symmetric
positive-pair operator is a stable, decision-sufficient signature for linear
prediction of approximately view-invariant targets (THEORY-007, THEORY-228).
Its directed analog (QUESTION-052's title): the **top-d left singular space**
of the conditional-expectation operator T: L2(P_A)->L2(P_X), (Tg)(x)=E[g(A)|x].

The directed **linear** case is already held and proved (THEORY-239 Active;
QUESTION-245 Answered, with a non-reversible three-state chain). So the
remaining directed case is (a) nonlinear decisions and (b) what makes one span
*the* signature when spans tie -- the open residue of QUESTION-052.

State the signature (hypotheses + claimed theorem) precisely for the directed
case; attempt the proof; where it fails give obstruction/counterexample; check
with numpy on small directed examples. Make open choices explicitly; file
owner's choices as alternatives.

## Done

- Read CLAUDE.md, design-principles, ADR-001/048, run-lead skill.
- Read LEAD-142, CLAIM-209, QUESTION-052, QUESTION-245, THEORY-007/009/239,
  CLAIM-098/210, CASE-117; record.md field specs.
- Confirmed target not already held.
- Pushed branch with this file.

## Next

- numpy study: non-reversible chains; verify (i) top-d left singular span =
  top-d eigenspace of self-adjoint TT* on L2(P_X); (ii) the linear tie
  (THEORY-239) reproduced; (iii) a nonlinear-sufficiency gap; (iv) a
  direction counterexample: two directed laws sharing TT* but differing in
  direction, so no x-function distinguishes them.
- File CASE (executed-study), CLAIM(s) (Proposed), changelog, dated notes.

## Choices made

- The directed case for decisions-about-x is read through the self-adjoint
  two-step operator TT*; direction-dependent decisions are treated separately.
  (Rationale recorded in the CASE/CLAIM.)
