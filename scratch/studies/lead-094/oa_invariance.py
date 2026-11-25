"""Check whether the Ott-Antonsen family f_n = alpha**n is invariant under the
continuity equation for globally coupled phase oscillators, with and without a
second harmonic in the coupling.

Continuity equation (Ott and Antonsen 2008, eq. 4; 2009, eqs. 3-4):
    df/dt + d/dtheta (v f) = 0,
    v = omega + (1/2i)(H e^{-i theta} - H* e^{i theta})
              + (1/2i)(H2 e^{-2i theta} - H2* e^{2i theta}).
With f = (g/2pi)[1 + sum_{n>=1} (F_n e^{in theta} + c.c.)], the Fourier
hierarchy is, for n >= 1 (F_0 = 1, F_{-m} = conj(F_m)):
    dF_n/dt = -i n omega F_n - (n/2)(H F_{n+1} - H* F_{n-1})
                             - (n/2)(H2 F_{n+2} - H2* F_{n-2}).
The family is invariant iff, at F_n = alpha**n, the tangent dF_n/dt equals
n alpha**(n-1) * dalpha/dt for one dalpha/dt and every n. We read dalpha/dt off
n = 1 and report the largest mismatch for n = 2..nmax.
"""
from __future__ import annotations

import numpy as np


def hierarchy_rhs(F: dict[int, complex], n: int, omega: float, H: complex, H2: complex) -> complex:
    def get(m: int) -> complex:
        if m == 0:
            return 1.0 + 0j
        if m < 0:
            return np.conj(F[-m])
        return F[m]

    return (-1j * n * omega * get(n)
            - (n / 2) * (H * get(n + 1) - np.conj(H) * get(n - 1))
            - (n / 2) * (H2 * get(n + 2) - np.conj(H2) * get(n - 2)))


def invariance_defect(alpha: complex, omega: float, H: complex, H2: complex, nmax: int = 8) -> float:
    F = {m: alpha ** m for m in range(1, nmax + 3)}
    dalpha = hierarchy_rhs(F, 1, omega, H, H2)  # since dF_1/dt = dalpha/dt
    worst = 0.0
    for n in range(2, nmax + 1):
        lhs = hierarchy_rhs(F, n, omega, H, H2)
        rhs = n * alpha ** (n - 1) * dalpha
        worst = max(worst, abs(lhs - rhs))
    return worst


def main() -> None:
    rng = np.random.default_rng(0)
    rows = []
    for _ in range(5):
        alpha = 0.6 * np.exp(1j * rng.uniform(0, 2 * np.pi))
        omega = rng.normal()
        H = complex(rng.normal(), rng.normal())
        H2 = complex(rng.normal(), rng.normal())
        rows.append((abs(alpha), invariance_defect(alpha, omega, H, 0j),
                     invariance_defect(alpha, omega, H, 0.3 * H2)))
    print("|alpha|  defect(first harmonic only)  defect(with second harmonic)")
    for a, d1, d2 in rows:
        print(f"{a:.2f}     {d1:.2e}                     {d2:.2e}")
    # On |alpha| = 1 (full locking) the second-harmonic defect vanishes.
    a1 = np.exp(0.7j)
    print("defect with second harmonic at |alpha|=1:",
          f"{invariance_defect(a1, 0.4, 0.5+0.2j, 0.3-0.1j):.2e}")


if __name__ == "__main__":
    main()
