# scratch/manuscripts/governance-of-possibility/analysis/model.py
"""The industrial model of A48 section 9, made stochastic and run.

Configurations and paths.  Two production configurations, A and B, each held
at r = 1 (HOLD).  A path between them is a sequence of intermediate
configurations with their own r; each edge of a path takes a geometric number
of periods (chance q per period of completing) and, while it is crossed,
occupies max(r(from), r(to)).  A path's threshold is its peak (CLAIM-571);
an architecture's threshold is the least over its paths.  The graph is
symmetric: the same paths lead back from B to A.

  original   A -> M -> B,        r(M) = 3, two edges          (A48 9.1)
  staged     A -> S1 -> S2 -> B, r(S) = theta', three edges   (A48 9.3)

The staged route is slower by default (three edges to two); this is a
choice, stated, and the study varies theta' but not the length.

Budget rules (B_t is a capacity ceiling; s_t the period's peak use):
  peak    B_{t+1} = s_t                         (CLAIM-577)
  floor   B_{t+1} = max(s_t, F)                 (a held reserve F - HOLD)
  carry   B_{t+1} = min(cap, Bbar + rho (B_t - s_t))   (CASE-200, capped)
A floor may lapse: with chance `revoke` a period the commitment ends and the
rule becomes `peak` (a budget-setter cutting what is not used).

Contingency.  With chance p a period (while none is pending) demand switches
to the other configuration.  The organization takes the fastest affordable
path (threshold <= B_t).  If none is affordable, outside money arrives after
a geometric wait (chance g a period; g = 0 means never) and raises the budget
to the least threshold (CLAIM-577 step 4).  A transition once started is
funded to completion.  Response time is counted in periods from the start of
the contingency's period; it is late for deadline tau when it exceeds tau.

Drill (regime IV).  Every `drill_every` periods, when no transition is under
way and the budget allows, the staging configuration is occupied for part of
the period, so the peak use that period is the drill level.

Costs.  Each period the organization pays c per unit of budget above HOLD
(the reserve, whether held by a floor or by drilling); a contingency met late
costs L; redesign costs K once, reported as a break-even.

Output.  1 a period while the demanded configuration is held and no
contingency is pending, else 0.  Output does not depend on the budget except
through how fast a contingency is met, so it is identical across regimes in
any period before the first contingency.

Novel demand (CLAIM-361).  See `novel_demand`.
All numbers are invented to show mechanisms; none is a measurement.
"""
from __future__ import annotations

from dataclasses import dataclass, replace

import numpy as np

HOLD = 1.0
EPS = 1e-9


@dataclass(frozen=True)
class Path:
    name: str
    nodes: tuple[float, ...]   # r of each intermediate configuration
    q: float = 0.5             # per-period chance an edge is completed

    @property
    def full(self) -> tuple[float, ...]:
        return (HOLD, *self.nodes, HOLD)

    @property
    def edges(self) -> int:
        return len(self.nodes) + 1

    @property
    def threshold(self) -> float:
        return max(self.full)

    @property
    def expected_time(self) -> float:
        return self.edges / self.q

    def need(self, e: int) -> float:
        return max(self.full[e], self.full[e + 1])


ORIGINAL = Path("original", (3.0,))


def staged(theta: float, n: int = 2, q: float = 0.5) -> Path:
    return Path("staged", (theta,) * n, q)


@dataclass(frozen=True)
class Regime:
    name: str
    paths: tuple[Path, ...]
    rule: str = "peak"          # "peak", "floor" or "carry"
    floor: float = HOLD
    drill_every: int = 0        # 0 = never
    drill_level: float = HOLD
    bbar: float = 1.5
    rho: float = 1.0
    cap: float = 3.0
    revoke: float = 0.0
    redesigned: bool = False

    @property
    def threshold(self) -> float:
        return min(p.threshold for p in self.paths)


def regimes(theta_r: float = 2.0, **kw: float) -> dict[str, Regime]:
    """The draft's three regimes, split as the brief asks, plus carry-over."""
    red = (ORIGINAL, staged(theta_r))
    return {
        "I": Regime("I peak, original", (ORIGINAL,), "peak"),
        "II": Regime("II reserve at 3, original", (ORIGINAL,), "floor",
                     floor=ORIGINAL.threshold, revoke=kw.get("revoke", 0.0)),
        "III-a": Regime("III-a redesigned, peak", red, "peak", redesigned=True),
        "III-b": Regime("III-b redesigned, reserve at theta'", red, "floor",
                        floor=theta_r, revoke=kw.get("revoke", 0.0),
                        redesigned=True),
        "IV": Regime("IV redesigned, peak, drill each period", red, "peak",
                     drill_every=1, drill_level=theta_r, redesigned=True),
        "V": Regime("V carry-over (CASE-200), original", (ORIGINAL,), "carry"),
    }


def next_budget(reg: Regime, B: float, s: float, committed: bool) -> float:
    """B_{t+1} from the budget actually in force and the period's peak use."""
    if reg.rule == "peak" or (reg.rule == "floor" and not committed):
        return s
    if reg.rule == "floor":
        return max(s, reg.floor)
    if reg.rule == "carry":
        return min(reg.cap, reg.bbar + reg.rho * (B - s))
    raise ValueError(reg.rule)


def initial_budget(reg: Regime) -> float:
    return ORIGINAL.threshold     # A48: "begins in A, with a budget of 3"


class Org:
    """One organization's state; `step` advances it one period."""

    def __init__(self, reg: Regime, seed: list[int], g: float):
        # three streams (edges, outside money, lapse), so that regimes run on
        # one seed share common random numbers wherever their paths agree
        self.rng, self.rng_money, self.rng_lapse = (
            np.random.default_rng([*seed, k]) for k in range(3))
        self.reg, self.g = reg, g
        self.B = initial_budget(reg)
        self.committed = True
        self.pending = False
        self.t0 = 0
        self.path: Path | None = None
        self.edge = 0
        self.fund = 0.0
        self.wait: int | None = None
        self.t = 0
        self.extra: float = 0.0   # capacity above HOLD used by other activity

    def start_contingency(self) -> None:
        self.pending, self.t0, self.wait = True, self.t, None

    def _choose(self) -> Path | None:
        ok = [p for p in self.reg.paths if p.threshold <= self.B + EPS]
        return min(ok, key=lambda p: p.expected_time) if ok else None

    def step(self, other_need: float | None = None) -> dict[str, float]:
        """One period. other_need: capacity above HOLD wanted by an activity
        outside the specification's transitions (the novel-demand review);
        it is granted only when affordable (None: no such activity). Returns the period's record."""
        reg, rng = self.reg, self.rng
        arrived, s = False, HOLD
        if self.pending and self.path is None:
            p = self._choose()
            if p is None and self.g > 0:
                if self.wait is None:
                    self.wait = int(self.rng_money.geometric(self.g))
                self.wait -= 1
                if self.wait <= 0:
                    p = min(reg.paths, key=lambda x: (x.threshold, x.expected_time))
            if p is not None:
                self.path, self.edge, self.fund = p, 0, p.threshold
        B_eff = max(self.B, self.fund) if self.path is not None else self.B
        if self.path is not None:
            s = self.path.need(self.edge)
            if rng.random() < self.path.q:
                self.edge += 1
                if self.edge == self.path.edges:
                    arrived = True
        granted = 0.0
        if other_need is not None and s + other_need <= B_eff + EPS:
            granted = 1.0
            s += other_need
        drilled = False
        if (self.path is None and not self.pending and reg.drill_every
                and self.t % reg.drill_every == 0
                and s + reg.drill_level - HOLD <= B_eff + EPS):
            s += reg.drill_level - HOLD
            drilled = True
        rec = dict(B=B_eff, s=s, cap=B_eff - HOLD, drilled=float(drilled),
                   granted=granted,
                   output=float(not self.pending), resp=-1.0)
        if arrived:
            rec["resp"] = float(self.t - self.t0 + 1)
            self.pending, self.path, self.fund, self.wait = False, None, 0.0, None
        if (reg.rule == "floor" and self.committed
                and self.rng_lapse.random() < reg.revoke):
            self.committed = False
        self.B = next_budget(reg, B_eff, s, self.committed)
        self.t += 1
        return rec


def run(reg: Regime, p: float, T: int, seed: int, g: float = 0.1
        ) -> dict[str, np.ndarray]:
    """A long run: contingencies at chance p a period. Seeds are shared
    across regimes, but the contingency draws come from their own stream so
    every regime sees the same arrival opportunities."""
    arr = np.random.default_rng([20261123, seed, 0]).random(T) < p
    org = Org(reg, [20261123, seed, 1], g)
    B, s, cap, out, resp = (np.zeros(T) for _ in range(5))
    first = -1
    for t in range(T):
        if arr[t] and not org.pending:
            org.start_contingency()
            if first < 0:
                first = t
        r = org.step()
        B[t], s[t], cap[t], out[t] = r["B"], r["s"], r["cap"], r["output"]
        resp[t] = r["resp"]
    return dict(B=B, s=s, cap=cap, output=out, resp=resp[resp > 0],
                first=np.array([first]))


def impose(reg: Regime, reps: int, quiet: int = 50, horizon: int = 60,
           g: float = 0.1, seed: int = 0) -> np.ndarray:
    """Response times under do(c) after `quiet` periods of ordinary operation
    (TERM-115's imposed contingency); horizon+1 marks never within horizon."""
    out = np.full(reps, horizon + 1.0)
    for i in range(reps):
        org = Org(reg, [20261123, seed, 2, i], g)
        for _ in range(quiet):
            org.step()
        org.start_contingency()
        for _ in range(horizon):
            r = org.step()
            if r["resp"] > 0:
                out[i] = r["resp"]
                break
    return out


def readiness(times: np.ndarray, ts: np.ndarray) -> np.ndarray:
    """R(t) = P(B reached within t of the contingency), t in ts."""
    return np.array([(times <= t).mean() for t in ts])


def exact_readiness(path: Path, ts: np.ndarray) -> np.ndarray:
    """P(sum of path.edges geometric(q) times <= t): a negative binomial."""
    from math import comb
    n, q = path.edges, path.q
    return np.array([sum(comb(k - 1, n - 1) * q ** n * (1 - q) ** (k - n)
                         for k in range(n, int(t) + 1)) for t in ts])


def dominance(Ri: np.ndarray, Rj: np.ndarray, tol: float = 0.0) -> str:
    """First-order dominance of readiness curves (TERM-115's note)."""
    if np.all(Ri >= Rj - tol):
        return "equal" if np.all(np.abs(Ri - Rj) <= tol) else "dominates"
    if np.all(Rj >= Ri - tol):
        return "dominated"
    return "cross"


def novel_demand(reg: Regime, policy: str, reps: int, theta_c: float = 2.5,
                 review_cost: float = 0.5, review_len: int = 3,
                 quiet: int = 50, horizon: int = 120, g: float = 0.1,
                 seed: int = 0) -> dict[str, float]:
    """A harm absent from the specification appears after `quiet` periods.

    Holding A causes it each period until the organization reaches C (held at
    HOLD; path A -> N -> C with r(N) = theta_c, two edges), a configuration
    the specification does not name. Policy "excise": the demand is never
    entered in the specification (CLAIM-361's suppression). Policy "revise":
    the specification is revised after `review_len` periods of review, each
    occupying review_cost above HOLD, granted only when the budget allows;
    once revised, the demand is a contingency like the specified one, met by
    the fastest affordable path or outside money. Scores: the original
    specification D0 (output while A is held; nothing in D0 changes), the
    organization's own current specification, and the true demands."""
    to_c = Path("to-C", (theta_c,))
    harm = own_viol = revised = reached = blocked_review = d0 = b_end = 0.0
    for i in range(reps):
        org = Org(reg, [20261123, seed, 3, i], g)
        for _ in range(quiet):
            org.step()
        alt = replace(reg, paths=(to_c,))
        done, rev_left, rev_done = False, review_len, False
        for t in range(horizon):
            if policy == "revise" and not rev_done:
                r = org.step(other_need=review_cost)
                if r["granted"] > 0:
                    rev_left -= 1
                else:
                    blocked_review += 1
                if rev_left == 0:
                    rev_done = True
                    org.reg = alt   # the revised demand: reach C
                    org.start_contingency()
            else:
                r = org.step()
            d0 += 1.0 - r["output"]   # output lost while moving to C
            if rev_done and r["resp"] > 0:
                done = True
            if not done:
                harm += 1
                own_viol += float(rev_done)
            else:
                break
        revised += float(rev_done)
        reached += float(done)
        org.reg = replace(org.reg, paths=reg.paths)
        org.pending, org.path, org.fund = False, None, 0.0
        for _ in range(3):
            org.step()
        b_end += org.B
    n = float(reps)
    return dict(revised=revised / n, reached_C=reached / n,
                harm_periods=harm / n, own_spec_violations=own_viol / n,
                d0_violations=d0 / n, review_blocked_periods=blocked_review / n,
                B_end=b_end / n)
