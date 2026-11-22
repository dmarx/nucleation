"""LEAD-095: a small stochastic assembly model with withdrawable support.

Continuous-time Markov chain on states (N, n): N in {0, 1} says whether a
nucleus has formed, n in {0..M} counts the other units bound. Two absorbing
outcomes: the target F and a failure set K (a trap reached from every
unfinished state at rate kappa). Rates (k_on = 1 sets the time unit):

  nucleus forms     (0,n) -> (1,n)    a        (support: a_S)
  nucleus dissolves (1,n) -> (0,n)    d0*theta**n  (support: 0, the scaffold holds it)
  unit binds        (N,n) -> (N,n+1)  k_on * (g if N == 1 and rate_effect else 1)
  unit unbinds      (N,n) -> (N,n-1)  b, for n >= 1
  trap              (N,n) -> K        kappa

theta < 1 means bound units stabilize the nucleus (downstream feedback);
theta = 1 means they do not. Two switches separate the nucleus's two effects
(QUESTION-397):

  state_effect  the nucleus is part of the target: F = {(1, M)}; otherwise
                F = {(0, M), (1, M)} and the nucleus is not needed to finish.
  rate_effect   the nucleus multiplies the binding rate of the other units
                by g (a non-zero Delta k for transitions it takes no part in).

Support is a scaffold that forms and holds the nucleus. Withdrawal at a state
s means the chain continues from s under the unsupported rates, for good.
A's measure (QUESTION-398) is D(s) = q_supported(s) - q_withdrawn(s).

Run:  python3 -I scratch/studies/lead-095/committor_model.py
"""
from __future__ import annotations

import json
import sys
from dataclasses import dataclass, replace

import numpy as np
from scipy.linalg import expm


# ---------------------------------------------------------------- generic solver
def committor(Q: np.ndarray, target, failure) -> np.ndarray:
    """Exact committor q(i) = Pr_i(hit target before failure) of a CTMC.

    Q is a full generator (rows sum to zero, off-diagonals >= 0); target and
    failure are disjoint index collections. Solves sum_j Q_ij q_j = 0 on the
    remaining states with q = 1 on target, 0 on failure.
    """
    Q = np.asarray(Q, float)
    n = Q.shape[0]
    target, failure = set(target), set(failure)
    assert not (target & failure)
    q = np.zeros(n)
    q[list(target)] = 1.0
    free = [i for i in range(n) if i not in target and i not in failure]
    if free:
        A = Q[np.ix_(free, free)]
        rhs = -Q[np.ix_(free, sorted(target))].sum(axis=1) if target else np.zeros(len(free))
        q[free] = np.linalg.solve(A, rhs)
    return q


# ---------------------------------------------------------------- the model
@dataclass(frozen=True)
class Params:
    M: int = 8            # other units in the target
    k_on: float = 1.0
    b: float = 1.5        # unbinding rate; b > k_on: unaided growth drifts back
    g: float = 3.0        # nucleus's multiplier on binding (rate effect)
    kappa: float = 0.02   # trap rate from every unfinished state
    a0: float = 0.2       # nucleus formation, unsupported
    aS: float = 5.0       # nucleus formation, supported
    d0: float = 1.0       # nucleus dissolution at n = 0, unsupported
    theta: float = 0.5    # per-unit stabilization of the nucleus by bound units
    state_effect: bool = True
    rate_effect: bool = True


class Model:
    """Index map: (N, n) -> N*(M+1)+n for the 2(M+1) assembly states, then F, K."""

    def __init__(self, p: Params):
        self.p = p
        self.nS = 2 * (p.M + 1)
        self.F, self.K = self.nS, self.nS + 1
        self.size = self.nS + 2

    def idx(self, N: int, n: int) -> int:
        return N * (self.p.M + 1) + n

    def is_target(self, N: int, n: int) -> bool:
        return n == self.p.M and (N == 1 or not self.p.state_effect)

    def generator(self, supported: bool) -> np.ndarray:
        p = self.p
        Q = np.zeros((self.size, self.size))

        def add(i, j, r):
            if r > 0:
                Q[i, j] += r

        for N in (0, 1):
            for n in range(p.M + 1):
                i = self.idx(N, n)
                if self.is_target(N, n):
                    continue                     # target states are lumped into F
                dest = lambda N2, n2: self.F if self.is_target(N2, n2) else self.idx(N2, n2)
                if N == 0:
                    add(i, dest(1, n), p.aS if supported else p.a0)
                else:
                    add(i, dest(0, n), 0.0 if supported else p.d0 * p.theta ** n)
                if n < p.M:
                    add(i, dest(N, n + 1), p.k_on * (p.g if (N == 1 and p.rate_effect) else 1.0))
                if n >= 1:
                    add(i, dest(N, n - 1), p.b)
                add(i, self.K, p.kappa)
        np.fill_diagonal(Q, -Q.sum(axis=1))
        return Q

    def absorbing(self) -> list[int]:
        """F, K and the (N, M) indices lumped into F (unused rows of the generator)."""
        return [self.F, self.K] + [self.idx(N, self.p.M) for N in (0, 1) if self.is_target(N, self.p.M)]

    def targets(self) -> list[int]:
        return [i for i in self.absorbing() if i != self.K]

    def q(self, supported: bool) -> np.ndarray:
        return committor(self.generator(supported), self.targets(), [self.K])

    def table(self, supported: bool) -> np.ndarray:
        """q as a 2 x (M+1) array indexed [N, n]; target states read 1."""
        q = self.q(supported)
        out = np.empty((2, self.p.M + 1))
        for N in (0, 1):
            for n in range(self.p.M + 1):
                out[N, n] = 1.0 if self.is_target(N, n) else q[self.idx(N, n)]
        return out


def D_table(p: Params) -> np.ndarray:
    m = Model(p)
    return m.table(True) - m.table(False)


# ---------------------------------------------------------------- decomposition
def withdrawal_decomposition(p: Params) -> np.ndarray:
    """D(s) as E_s^supported[ integral of ((Q_S - Q_0) q_0)(X_t) dt ].

    Exact identity on the transient states T: (Q_S)_TT (q_S - q_0) =
    -((Q_S - Q_0) q_0)_T, so D = (-(Q_S)_TT)^{-1} f with f = (Q_S - Q_0) q_0.
    Here support acts only on the nucleus, so f(1,n) = d_n * (q_0(1,n) -
    q_0(0,n)) and f(0,n) = (a_S - a_0) * (q_0(1,n) - q_0(0,n)): fragility (or
    formation deficit) times the nucleus's unsupported productivity.
    Returns D on the full index space (0 on F, K).
    """
    m = Model(p)
    QS, Q0 = m.generator(True), m.generator(False)
    q0 = m.q(False)
    f = (QS - Q0) @ q0
    T = [i for i in range(m.size) if i not in m.absorbing()]
    D = np.zeros(m.size)
    D[T] = np.linalg.solve(-QS[np.ix_(T, T)], f[T])
    return D


# ---------------------------------------------------------------- time-based withdrawal
def time_withdrawal(p: Params, times, start=(0, 0)) -> list[dict]:
    """Withdraw at a clock time t instead of a state: run supported to t, then unsupported.

    Returns for each t: success Y(t), the completed-before-withdrawal share
    p_t(F), and the state-matched part sum_s p_t(s) q_0(s).
    """
    m = Model(p)
    QS = m.generator(True)
    q0 = m.q(False)
    qS = m.q(True)
    p0 = np.zeros(m.size)
    p0[m.idx(*start)] = 1.0
    out = []
    for t in times:
        pt = p0 @ expm(QS * t)
        done = pt[m.F]
        T = [i for i in range(m.size) if i not in m.absorbing()]
        matched = float(pt[T] @ q0[T])          # unfinished states only
        out.append(dict(t=float(t), Y=float(done + matched), completed=float(done),
                        matched=matched, q_supported_start=float(qS[m.idx(*start)])))
    return out


# ---------------------------------------------------------------- Monte Carlo check
def simulate_success(Q: np.ndarray, start: int, target: int, failure: int, n: int, rng) -> float:
    """Fraction of n jump-chain runs from start that hit target before failure."""
    P = Q.copy()
    np.fill_diagonal(P, 0)
    rates = P.sum(axis=1)
    hits = 0
    for _ in range(n):
        i = start
        while i not in (target, failure):
            i = rng.choice(len(P), p=P[i] / rates[i])
        hits += i == target
    return hits / n


# ---------------------------------------------------------------- the study
MECHANISMS = {
    # name: (theta, rate_effect)
    "feedback+rate": (0.5, True),
    "feedback only": (0.5, False),
    "rate only": (1.0, True),
    "neither": (1.0, False),
}


def first_below(row, eps):
    for n, v in enumerate(row):
        if v < eps:
            return n
    return None


def run(base: Params = Params()) -> dict:
    res: dict = {"params": base.__dict__, "D": {}, "q": {}, "decomposition_check": {}}
    # E1: D(s) at nucleus-present states, four mechanisms
    for name, (theta, rate) in MECHANISMS.items():
        p = replace(base, theta=theta, rate_effect=rate)
        m = Model(p)
        qS, q0 = m.table(True), m.table(False)
        D = qS - q0
        Ddec = withdrawal_decomposition(p)
        err = max(abs(Ddec[m.idx(N, n)] - D[N, n]) for N in (0, 1) for n in range(p.M + 1)
                  if not m.is_target(N, n))
        res["D"][name] = dict(D1=D[1].round(4).tolist(), D0=D[0].round(4).tolist(),
                              first_n_D1_below_0p05=first_below(D[1, :p.M], 0.05),
                              first_n_D1_below_0p01=first_below(D[1, :p.M], 0.01))
        res["q"][name] = dict(qS1=qS[1].round(4).tolist(), q01=q0[1].round(4).tolist(),
                              q00=q0[0].round(4).tolist(),
                              DeltaN_unsupported=(q0[1] - q0[0]).round(4).tolist(),
                              fragility=[round(p.d0 * p.theta ** n, 4) for n in range(p.M + 1)])
        res["decomposition_check"][name] = float(err)

    # E2: withdrawal by clock time, 'neither' and 'feedback+rate'
    times = [0, 1, 2, 5, 10, 20, 40, 80, 160]
    res["time_withdrawal"] = {}
    for name in ("neither", "feedback+rate"):
        theta, rate = MECHANISMS[name]
        p = replace(base, theta=theta, rate_effect=rate)
        res["time_withdrawal"][name] = [{k: round(v, 4) for k, v in r.items()}
                                        for r in time_withdrawal(p, times)]

    # E3: QUESTION-397's factorial, unsupported, at matched n (theta = 1 so the
    # nucleus's own persistence is not a third effect)
    res["factorial"] = {}
    for S in (False, True):
        for R in (False, True):
            p = replace(base, theta=1.0, state_effect=S, rate_effect=R)
            q0 = Model(p).table(False)
            dk = (p.g - 1.0) * p.k_on if R else 0.0
            res["factorial"][f"state={int(S)} rate={int(R)}"] = dict(
                q1=q0[1].round(4).tolist(), q0=q0[0].round(4).tolist(),
                DeltaN=(q0[1] - q0[0]).round(4).tolist(), Delta_k_binding=dk)
    # interaction contrast of Delta_N at n = 0 and n = M//2
    f = res["factorial"]
    for n in (0, base.M // 2):
        res[f"interaction_contrast_DeltaN_n{n}"] = round(
            f["state=1 rate=1"]["DeltaN"][n] - f["state=1 rate=0"]["DeltaN"][n]
            - f["state=0 rate=1"]["DeltaN"][n] + f["state=0 rate=0"]["DeltaN"][n], 4)

    # E4: support while the state effect is off (nucleus not needed to finish)
    res["D_state_off"] = {}
    for name, (theta, rate) in MECHANISMS.items():
        p = replace(base, theta=theta, rate_effect=rate, state_effect=False)
        D = D_table(p)
        res["D_state_off"][name] = dict(D1=D[1].round(4).tolist(),
                                        first_n_D1_below_0p05=first_below(D[1, :p.M], 0.05))
    return res


def show(res: dict) -> None:
    M = res["params"]["M"]
    print("D(1,n) = q_supported - q_withdrawn, withdrawal with nucleus present; n = 0..%d" % (M - 1))
    for name, r in res["D"].items():
        print(f"  {name:14s}", " ".join(f"{v:6.3f}" for v in r["D1"][:M]),
              f"| first n with D<0.05: {r['first_n_D1_below_0p05']}")
    print("q_supported(1,n):")
    for name, r in res["q"].items():
        print(f"  {name:14s}", " ".join(f"{v:6.3f}" for v in r["qS1"][:M]))
    print("q_withdrawn(1,n):")
    for name, r in res["q"].items():
        print(f"  {name:14s}", " ".join(f"{v:6.3f}" for v in r["q01"][:M]))
    print("Delta_N unsupported = q0(1,n) - q0(0,n):")
    for name, r in res["q"].items():
        print(f"  {name:14s}", " ".join(f"{v:6.3f}" for v in r["DeltaN_unsupported"][:M]))
    print("decomposition identity, max error:", max(res["decomposition_check"].values()))
    print("Withdrawal by clock time from (0,0):  t, Y(t), completed, state-matched, D_time")
    for name, rows in res["time_withdrawal"].items():
        print(" ", name)
        for r in rows:
            print(f"    t={r['t']:5.0f}  Y={r['Y']:.4f}  completed={r['completed']:.4f}  "
                  f"matched={r['matched']:.4f}  D_time={r['q_supported_start'] - r['Y']:.4f}")
    print("Factorial (theta = 1, unsupported): Delta_N(n) at n = 0..%d, Delta k" % (M - 1))
    for k, r in res["factorial"].items():
        print(f"  {k}", " ".join(f"{v:6.3f}" for v in r["DeltaN"][:M]), f"| dk={r['Delta_k_binding']}")
    for k in res:
        if k.startswith("interaction"):
            print(" ", k, res[k])
    print("D(1,n) with the state effect off:")
    for name, r in res["D_state_off"].items():
        print(f"  {name:14s}", " ".join(f"{v:6.3f}" for v in r["D1"][:M]),
              f"| first n with D<0.05: {r['first_n_D1_below_0p05']}")


if __name__ == "__main__":
    res = run()
    show(res)
    out = sys.argv[1] if len(sys.argv) > 1 else None
    if out:
        with open(out, "w") as fh:
            json.dump(res, fh, indent=1)
