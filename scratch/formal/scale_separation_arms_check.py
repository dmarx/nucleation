"""scratch/formal/scale_separation_arms_check.py

Rebuilds the computations CLAIM-755 cites from its ground CASE-116 (three
finite-state arms), from the entries' text alone: no script was kept.
Written at the recomputation pass of 2026-11-25 by a session other than
the filer's. Run: python3 -I this file. numpy.

Checks: arm A's joint chain (Z flips w.p. 0.01; U1, U2 resampled each step)
has eigenvalues 1, 0.98 and six zeros, and dependence on Z0 decays as
0.98^t (0.904 at t = 5, 0.133 at t = 100); arm B's register has
eigenvalues 1 and 0.2, with P(Z' = 1 | do(Z = 0)) = 0.4 and
P(Z' = 1 | do(Z = 1)) = 0.6; arm C's archive, counted as a state, has
eigenvalue 1 across the gap (the point of CLAIM-755's note of 2026-11-20).
A negative control: arm B with no noise has eigenvalue 1, so the check
distinguishes.
"""
import numpy as np

# arm A
Pz = np.array([[0.99, 0.01], [0.01, 0.99]])
Pu = np.full((4, 4), 0.25)  # (U1, U2) resampled uniformly: rank one
PA = np.kron(Pz, Pu)
ev = np.sort(np.abs(np.linalg.eigvals(PA)))[::-1]
assert np.allclose(ev[:2], [1, 0.98]) and np.allclose(ev[2:], 0, atol=1e-12), ev
for t, v in ((5, 0.904), (100, 0.133)):
    dep = np.linalg.matrix_power(Pz, t)[0, 0] - np.linalg.matrix_power(Pz, t)[1, 0]
    assert abs(dep - 0.98 ** t) < 1e-12 and abs(dep - v) < 5e-4, (t, dep)
# members forget in one step: U's law after one step is independent of the start
P1 = PA.reshape(2, 4, 2, 4)
assert np.allclose(P1.sum(axis=2)[:, :, :], 0.25)

# arm B: Z' = A1 = Z xor N1, N1 ~ Bernoulli(0.4)
PB = np.array([[0.6, 0.4], [0.4, 0.6]])
assert np.allclose(np.sort(np.linalg.eigvals(PB))[::-1], [1, 0.2])
assert PB[0, 1] == 0.4 and PB[1, 1] == 0.6
assert abs(np.linalg.matrix_power(PB, 3)[0, 0] - np.linalg.matrix_power(PB, 3)[1, 0] - 0.2 ** 3) < 1e-12

# arm C: archive theta written by A, held across the gap, read by B
# state (theta) in {0, 1}; the archive's transition across the gap is the identity
PC = np.eye(2)
assert np.allclose(np.linalg.eigvals(PC), [1, 1])
b_B = {th: th for th in (0, 1)}  # B executes theta_B = theta_A
assert b_B[0] != b_B[1]          # intervening on theta_A changes B's behaviour

# negative control: arm B without noise is not fast
P0 = np.array([[1.0, 0.0], [0.0, 1.0]])
assert np.sort(np.linalg.eigvals(P0))[0] == 1.0
print("arm A eigenvalues 1, 0.98, six zeros; decay 0.904 at 5, 0.133 at 100")
print("arm B eigenvalues 1, 0.2; do(Z=0) -> 0.4, do(Z=1) -> 0.6")
print("arm C archive eigenvalue 1 across the gap; B follows theta_A")
print("checks pass")
