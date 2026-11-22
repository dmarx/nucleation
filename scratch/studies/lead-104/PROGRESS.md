# LEAD-104 progress

- Lead: LEAD-104 "Write the model of the competence-restriction loop, with
  reinstatement made a threshold on capacity."
- Branch: claude/lead-104-trap-model (cut from origin/staging).
- Advances: CLAIM-721 (Proposed). Modifies CLAIM-605's model (Active).

## Task as understood

CLAIM-721 names the gap: "A model of the loop would be CLAIM-605's with
reinstatement made a threshold on capacity, which would make the trap
demonstrable; no one has written it." Build it in numpy, demonstrate the
restriction-induced capability trap, test it.

The modification of CLAIM-605's model (dC/dt = lam*P*C*(1-C) - mu*C):
instead of outside support doing the work, a *restriction* removes the
doing (P scaled by the restriction), and *reinstatement* is a threshold
C_r on capacity: the restriction lifts when C >= C_r. The three conditions
of CLAIM-721 become model switches: decay (mu>0), lifting depends on
competence (C_r>0), no route to practice/training (practice rate rho=0,
training input g=0).

## Choices made (see script header for why)

- Restriction modelled as P = rho*min(tau*C,1) while restricted, rho in
  [0,1] the practice route the restricting party supplies; plus g>=0 a
  training input adding capacity directly. rho=0,g=0 is the bare trap.
- Reinstatement one-way (free stable state 0.7 > C_r), C_r a free parameter,
  swept. CLAIM-605's lam=1, mu=0.3, tau=1.5 kept so it is CLAIM-605's model.
- Practice route (multiplicative) vs training route (direct capacity):
  included both; mirrors CLAIM-605's "capacity-first cannot ignite" vs
  asset-transfer distinction.

## Done

- Step 1: confirmed target not already held (CASE-225/262 are the
  substitution/suppression models; no restriction-loop model exists).
- Branch cut, PROGRESS pushed.

- Step 3: wrote restriction_trap.py (model + 4 results) + pytest (8 pass).
  All numbers reproduce. README added.

- Step 6: FILED. CASE-tmprcg71 (executed-study), CLAIM-tmpn5wpc (finding,
  demonstrated), notes on CLAIM-721/605 and LEAD-104, changelog fragment.
  Pre-commit checks pass (frontmatter/title/H1). No held statuses changed.

## Done -- all steps complete; ready to report.

## Owner's calls (left unmade)

- Adopt CASE-tmprcg71 and CLAIM-tmpn5wpc (both Proposed).
- Whether the demonstration moves CLAIM-721's warrant to demonstrated.
- LEAD-104 status/stage (left Open/idea).
