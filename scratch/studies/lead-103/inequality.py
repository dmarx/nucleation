"""LEAD-103: operational equivalences of a pragmatic rendering experiment,
and the generalized-noncontextuality inequality they imply.

Run with: python3 -I inequality.py
Writes per-check results to results.jsonl (append-only).

Setup (the pragmatic experiment, in the record's vocabulary).
  - An utterance given in four renderings R1..R4 (preparations).
  - Two binary relational probes X, Z (measurements), outcomes +-1.
  - Predictability of a rendering under a probe: <X>_i = p(+|Ri,X) - p(-|Ri,X).

Operational equivalences assumed.
  OE1 (equal-predictability orbit): |<X>_i| = x and |<Z>_i| = z for every i,
       with the four sign patterns
         R1:(+,+)  R2:(-,+)  R3:(-,-)  R4:(+,-).
  OE2 (mixture equivalence): 1/2 R1 + 1/2 R3  ~  1/2 R2 + 1/2 R4,
       i.e. for every probe the two equal mixtures give identical statistics.

Generalized (preparation) noncontextuality (Spekkens): operationally
equivalent preparations get the same distribution over ontic states, so
OE2 forces  1/2 nu1 + 1/2 nu3 = 1/2 nu2 + 1/2 nu4  on Lambda.

Claim derived: any preparation-noncontextual model reproducing OE1 and OE2
satisfies the diamond  |<X>| + |<Z>| <= 1  (all four +-x +-z <= 1).
A rendering ensemble that violates it witnesses preparation contextuality
that no sheaf / Kochen-Specker test over the cover {X},{Z} can see (no overlap).
"""
import json
import os
import sys
import numpy as np
from scipy.optimize import linprog, minimize

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results.jsonl")


def emit(record):
    with open(OUT, "a") as fh:
        fh.write(json.dumps(record, sort_keys=True) + "\n")
    print(json.dumps(record, sort_keys=True))


# Deterministic response functions for the four joint (X,Z) ontic states,
# ordered  lambda = ++, +-, -+, --   (sign of X then sign of Z).
# xi(lambda) = p(X=+|lambda), zeta(lambda) = p(Z=+|lambda).
X_PLUS = np.array([1.0, 1.0, 0.0, 0.0])   # X=+ on ++, +-
Z_PLUS = np.array([1.0, 0.0, 1.0, 0.0])   # Z=+ on ++, -+
WX = 2 * X_PLUS - 1                        # <X> weight per ontic state: +1/-1
WZ = 2 * Z_PLUS - 1

# target signed predictabilities per rendering, as multiples of (x, z)
SIGNS = {1: (+1, +1), 2: (-1, +1), 3: (-1, -1), 4: (+1, -1)}


def nc_bound_lp(objective=(1.0, 1.0)):
    """Max  cx*x + cz*z  over preparation-noncontextual models on the four
    deterministic ontic states, subject to OE1 (orbit signs) and OE2
    (mixture equivalence). Variables: nu1,nu2,nu3,nu4 (4 each) then x,z = 18.
    Returns the optimum (expected 1.0 for the diamond faces)."""
    nvar = 18
    xi, zi = 16, 17  # indices of x, z

    A_eq, b_eq = [], []
    # each nu_i normalized
    for i in range(4):
        row = np.zeros(nvar)
        row[4 * i:4 * i + 4] = 1.0
        A_eq.append(row); b_eq.append(1.0)
    # predictabilities match the signed orbit:  sum WX*nu_i - sX*x = 0, etc.
    for i in range(4):
        sX, sZ = SIGNS[i + 1]
        rx = np.zeros(nvar); rx[4 * i:4 * i + 4] = WX; rx[xi] = -sX
        A_eq.append(rx); b_eq.append(0.0)
        rz = np.zeros(nvar); rz[4 * i:4 * i + 4] = WZ; rz[zi] = -sZ
        A_eq.append(rz); b_eq.append(0.0)
    # OE2 under noncontextuality: 1/2 nu1 + 1/2 nu3 - 1/2 nu2 - 1/2 nu4 = 0
    for k in range(4):
        row = np.zeros(nvar)
        row[0 + k] = 0.5; row[8 + k] = 0.5      # nu1, nu3
        row[4 + k] = -0.5; row[12 + k] = -0.5   # nu2, nu4
        A_eq.append(row); b_eq.append(0.0)

    c = np.zeros(nvar)
    c[xi] = -objective[0]; c[zi] = -objective[1]  # linprog minimizes
    bounds = [(0, None)] * 16 + [(-1, 1), (-1, 1)]
    res = linprog(c, A_eq=np.array(A_eq), b_eq=np.array(b_eq), bounds=bounds,
                  method="highs")
    return res


def nc_bound_general(trials=200, K=6, seed=0):
    """Corroboration WITHOUT the deterministic reduction. The analytic result
    reduces preparation noncontextuality to deterministic response functions
    (Schmid-Spekkens-Wolfe: WLOG when the measurement effects carry no
    nontrivial operational equivalences). To check that non-determinism
    cannot beat the bound, we draw random response functions xi, zeta over K
    ontic states (values in [0,1], i.e. genuinely indeterministic), and for
    each one solve the LINEAR program that maximizes x+z over the ontic
    distributions nu1..nu4 subject to OE1 (orbit signs) and OE2 (mixture
    equivalence under noncontextuality). Returns the largest x+z over all
    draws; it should never exceed 1."""
    rng = np.random.default_rng(seed)
    best = 0.0
    nvar = 4 * K + 2  # nu1..nu4 (K each), then x, z
    xi_, zi_ = 4 * K, 4 * K + 1
    for _ in range(trials):
        vX = 2 * rng.random(K) - 1   # effective X-value 2*xi-1 in [-1,1]
        vZ = 2 * rng.random(K) - 1
        A_eq, b_eq = [], []
        for i in range(4):
            row = np.zeros(nvar); row[i * K:(i + 1) * K] = 1.0
            A_eq.append(row); b_eq.append(1.0)
        for i in range(4):
            sX, sZ = SIGNS[i + 1]
            rx = np.zeros(nvar); rx[i * K:(i + 1) * K] = vX; rx[xi_] = -sX
            A_eq.append(rx); b_eq.append(0.0)
            rz = np.zeros(nvar); rz[i * K:(i + 1) * K] = vZ; rz[zi_] = -sZ
            A_eq.append(rz); b_eq.append(0.0)
        for k in range(K):
            row = np.zeros(nvar)
            row[0 * K + k] = 0.5; row[2 * K + k] = 0.5
            row[1 * K + k] = -0.5; row[3 * K + k] = -0.5
            A_eq.append(row); b_eq.append(0.0)
        c = np.zeros(nvar); c[xi_] = -1.0; c[zi_] = -1.0
        bounds = [(0, None)] * (4 * K) + [(-1, 1), (-1, 1)]
        r = linprog(c, A_eq=np.array(A_eq), b_eq=np.array(b_eq),
                    bounds=bounds, method="highs")
        if r.success:
            best = max(best, float(-r.fun))
    return best


def qubit_orbit(x, z):
    """Qubit realization. Four pure/mixed states with Bloch vectors in the
    xz-plane: r1=(x,0,z), r2=(-x,0,z), r3=(-x,0,-z), r4=(x,0,-z).
    X = sigma_x, Z = sigma_z. Returns the operational statistics and checks
    OE1 and OE2 exactly."""
    sx = np.array([[0, 1], [1, 0]], complex)
    sz = np.array([[1, 0], [0, -1]], complex)
    I = np.eye(2, dtype=complex)

    def rho(rx, rz):
        return 0.5 * (I + rx * sx + rz * sz)
    rhos = [rho(x, z), rho(-x, z), rho(-x, -z), rho(x, -z)]
    exX = [float(np.real(np.trace(r @ sx))) for r in rhos]
    exZ = [float(np.real(np.trace(r @ sz))) for r in rhos]
    mixA = 0.5 * rhos[0] + 0.5 * rhos[2]
    mixB = 0.5 * rhos[1] + 0.5 * rhos[3]
    oe2_gap = float(np.max(np.abs(mixA - mixB)))
    return exX, exZ, oe2_gap


def main():
    results = {}

    # 1. Noncontextual bound by LP: the four diamond faces.
    faces = {"x+z": (1, 1), "x-z": (1, -1), "-x+z": (-1, 1), "-x-z": (-1, -1)}
    lp = {}
    for name, obj in faces.items():
        r = nc_bound_lp(obj)
        lp[name] = round(float(-r.fun), 10)
    emit({"check": "nc_bound_lp_diamond_faces", "optima": lp,
          "expected": 1.0, "pass": all(abs(v - 1.0) < 1e-7 for v in lp.values())})
    results["lp"] = lp

    # 2. Corroboration on general (non-deterministic) NC models.
    gen = nc_bound_general(trials=80, K=6, seed=1)
    emit({"check": "nc_bound_general_search", "max_x_plus_z": round(gen, 6),
          "bound": 1.0, "pass": gen <= 1.0 + 1e-4})

    # 3. Qubit realization violates the bound (and satisfies OE1, OE2).
    for (x, z, tag) in [(1 / np.sqrt(2), 1 / np.sqrt(2), "max"),
                        (0.8, 0.6, "pure_r=1"), (0.6, 0.6, "sub")]:
        exX, exZ, oe2 = qubit_orbit(x, z)
        oe1 = (max(abs(abs(v) - x) for v in exX) < 1e-9 and
               max(abs(abs(v) - z) for v in exZ) < 1e-9)
        signs_ok = all(
            (np.sign(exX[i]) == SIGNS[i + 1][0] or abs(exX[i]) < 1e-12) and
            (np.sign(exZ[i]) == SIGNS[i + 1][1] or abs(exZ[i]) < 1e-12)
            for i in range(4))
        emit({"check": "qubit_orbit", "x": round(x, 6), "z": round(z, 6),
              "tag": tag, "OE1_equal_predictabilities": bool(oe1),
              "OE1_sign_pattern": bool(signs_ok),
              "OE2_mixture_gap": round(oe2, 12),
              "x_plus_z": round(x + z, 6),
              "violates_bound": bool(x + z > 1.0 + 1e-9),
              "violation_ratio": round((x + z), 6)})

    # 4. OE2 is load-bearing: drop it, keep only OE1, and a NC model reaches
    #    joint predictability 1 (x=z=1), i.e. no bound. (simplicial/classical.)
    r = nc_bound_lp_no_oe2()
    emit({"check": "nc_bound_without_OE2", "max_x_plus_z": round(float(-r.fun), 8),
          "note": "dropping the mixture equivalence removes the bound; "
                  "equivalence is what the inequality rests on",
          "pass": float(-r.fun) > 1.5})

    print("\nAll results appended to", OUT)


def nc_bound_lp_no_oe2():
    """Same LP but without the OE2 mixture-equivalence constraints."""
    nvar = 18
    xi, zi = 16, 17
    A_eq, b_eq = [], []
    for i in range(4):
        row = np.zeros(nvar); row[4 * i:4 * i + 4] = 1.0
        A_eq.append(row); b_eq.append(1.0)
    for i in range(4):
        sX, sZ = SIGNS[i + 1]
        rx = np.zeros(nvar); rx[4 * i:4 * i + 4] = WX; rx[xi] = -sX
        A_eq.append(rx); b_eq.append(0.0)
        rz = np.zeros(nvar); rz[4 * i:4 * i + 4] = WZ; rz[zi] = -sZ
        A_eq.append(rz); b_eq.append(0.0)
    c = np.zeros(nvar); c[xi] = -1.0; c[zi] = -1.0
    bounds = [(0, None)] * 16 + [(-1, 1), (-1, 1)]
    return linprog(c, A_eq=np.array(A_eq), b_eq=np.array(b_eq), bounds=bounds,
                   method="highs")


if __name__ == "__main__":
    main()
