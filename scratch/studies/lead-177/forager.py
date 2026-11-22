"""CASE-239's forager, built for LEAD-177.

A forager with energy E pays an upkeep each step and dissolves at E <= 0.
It meets patches one per step; each patch has five binary features.  It may
skip, probe (pay a small cost to see one sample of the first step's yield)
or enter (stay up to L steps, leaving early on a registered failure).  The
yield depends on the features through rules the learning arms are not
given.  At t_change one change nobody trained for is introduced:

  none     nothing changes;
  delayed  red patches (f0) now raise upkeep by U for D steps after a visit
           (a feature that predicted gain now predicts a later loss);
  newfeat  the same delayed cost, now on f3, a feature always present and
           irrelevant until the change;
  silent   patches with f4 = 1 give no yield at all (the endogenous form of
           the debugger's case, CASE-240).

Arms (CASE-239's five, and two controls):

  learner   learns, from its own energy accounting, a predictor of a visit's
            net energy value over a horizon H, and revises which features it
            attends to (residual test), its failure threshold tau and its
            probe policy;
  frozen    the same learner, but from t_change on it may not change which
            features count, tau, or the probe policy; it keeps re-estimating
            the weights of the features it already attends to;
  selfset   CASE-241's self-set profile: enters every patch, registers a
            failure when a step's yield is below its current upkeep;
  designer  CASE-241's designer profile: a stored table of the training
            yields; enters what the table says pays, registers a failure
            when a yield departs from the table by more than 3 sigma;
  oracle    told the true expected net value of each pattern after the
            change; the ceiling;
  score     the learner, with its target replaced by the visit's immediate
            net intake (a variable the designer could have chosen, which
            matches the energy account in training and omits later upkeep);
  arbitrary the learner, with its target replaced by a fixed linear score of
            the features unrelated to the forager's energy.

Every run uses common random numbers per seed (the same patch stream and the
same per-step yield noise), so the arms receive identical sensory
correlations and differ only in memory, use and revision.
"""
from __future__ import annotations

import dataclasses
import math
from collections import deque

import numpy as np

D_FEAT = 5


@dataclasses.dataclass(frozen=True)
class World:
    T: int = 4000
    t_change: int = 1500
    E0: float = 100.0
    E_max: float = 500.0
    c0: float = 1.0
    L: int = 10            # maximum visit length
    U: float = 2.0         # delayed upkeep surcharge per step
    D: int = 15            # duration of the surcharge
    sigma: float = 0.3     # yield noise
    probe_cost: float = 0.3

    def base_yield(self, x: np.ndarray) -> float:
        return 1.5 + 1.0 * x[0] + 1.0 * x[1] - 1.5 * x[2]

    def silent(self, x, scenario: str, t: int) -> bool:
        return scenario == "silent" and t >= self.t_change and x[4] == 1

    def delayed(self, x, scenario: str, t: int) -> bool:
        if t < self.t_change:
            return False
        if scenario == "delayed":
            return x[0] == 1
        if scenario == "newfeat":
            return x[3] == 1
        return False

    def true_net(self, x, scenario: str, t: int) -> float:
        """Expected net energy of a full visit, relative to resting upkeep."""
        y = 0.0 if self.silent(x, scenario, t) else self.base_yield(x)
        v = self.L * (y - self.c0)
        if self.delayed(x, scenario, t):
            v -= self.U * self.D
        return v


def all_patterns() -> np.ndarray:
    return np.array([[(i >> k) & 1 for k in range(D_FEAT)] for i in range(2 ** D_FEAT)])


# --------------------------------------------------------------------------
# learning rules over an attended subset of features


class RLS:
    """Recursive least squares with forgetting over attended features + bias."""

    def __init__(self, lam: float = 0.98, delta: float = 100.0):
        self.lam, self.delta = lam, delta
        self.feats: list[int] = []
        self.w = np.zeros(1)
        self.P = np.eye(1) * delta

    def _phi(self, x):
        return np.concatenate([[1.0], [float(x[f]) for f in self.feats]])

    def predict(self, x) -> float:
        return float(self.w @ self._phi(x))

    def update(self, x, target: float):
        phi = self._phi(x)
        Pphi = self.P @ phi
        k = Pphi / (self.lam + phi @ Pphi)
        self.w = self.w + k * (target - self.w @ phi)
        self.P = (self.P - np.outer(k, Pphi)) / self.lam
        # guard against covariance wind-up under poor excitation
        tr = np.trace(self.P)
        if tr > self.delta * len(self.w):
            self.P *= self.delta * len(self.w) / tr

    def add_feature(self, f: int):
        if f in self.feats:
            return
        self.feats.append(f)
        n = len(self.w)
        self.w = np.append(self.w, 0.0)
        P = np.eye(n + 1) * self.delta
        P[:n, :n] = self.P
        self.P = P


class Tabular:
    """Exponentially forgetting mean per pattern of the attended features."""

    def __init__(self, alpha: float = 0.1):
        self.alpha = alpha
        self.feats: list[int] = []
        self.table: dict[tuple, float] = {}
        self.glob = 0.0

    def _key(self, x):
        return tuple(int(x[f]) for f in self.feats)

    def predict(self, x) -> float:
        return self.table.get(self._key(x), self.glob)

    def update(self, x, target: float):
        k = self._key(x)
        old = self.table.get(k, self.glob)
        self.table[k] = old + self.alpha * (target - old)
        self.glob += 0.02 * (target - self.glob)

    def add_feature(self, f: int):
        if f in self.feats:
            return
        # split each cell: both children start from the parent's estimate
        old = self.table
        self.feats.append(f)
        self.table = {}
        for k, v in old.items():
            self.table[k + (0,)] = v
            self.table[k + (1,)] = v


def make_rule(name: str):
    return RLS() if name == "rls" else Tabular()


# --------------------------------------------------------------------------
# the arms


class Arm:
    """Interface: decide(x, t, E, c_t) -> 'skip' | 'probe' | 'enter';
    after_probe(x, y1) -> bool enter; fail_step(x, y, c_t) -> bool leave;
    record_visit(x, net_value, immediate); warns(x) -> bool."""

    name = "arm"
    learning = False

    def __init__(self, world: World, rng: np.random.Generator):
        self.w, self.rng = world, rng

    def warns(self, x) -> bool:
        return False

    def decide(self, x, t, scenario):
        return "enter"

    def after_probe(self, x, y1, t, scenario) -> bool:
        return True

    def fail_step(self, x, y, c_t, t) -> bool:
        return False

    def record_visit(self, x, value, immediate, t):
        pass

    def record_step(self, x, y, t, failed=False):
        pass

    def attended(self):
        return []


class Oracle(Arm):
    name = "oracle"

    def decide(self, x, t, scenario):
        # the learners' rule (enter unless a loss is predicted), with the truth
        return "enter" if self.w.true_net(x, scenario, t) >= 0 else "skip"

    def warns(self, x):  # evaluated by the runner with scenario/time
        return False


class SelfSet(Arm):
    name = "selfset"

    def fail_step(self, x, y, c_t, t):
        return y < c_t


class Designer(Arm):
    name = "designer"

    def __init__(self, world, rng):
        super().__init__(world, rng)
        self.stored = {tuple(p): world.base_yield(p) for p in all_patterns()}

    def stored_net(self, x):
        return self.w.L * (self.stored[tuple(int(v) for v in x)] - self.w.c0)

    def warns(self, x):
        return self.stored_net(x) < 0

    def decide(self, x, t, scenario):
        return "skip" if self.warns(x) else "enter"

    def fail_step(self, x, y, c_t, t):
        return abs(y - self.stored[tuple(int(v) for v in x)]) > 3 * self.w.sigma


class Learner(Arm):
    """CASE-239 arm 1; with freeze='all' arm 5 (features, tau and probe
    policy fixed from t_change); with freeze='features' only the attended
    features are fixed (a decomposition of arm 5, added here).

    target: 'energy' (the visit's net energy account over the horizon H,
    including the share of later upkeep above resting), 'score' (immediate
    net intake only) or 'arbitrary' (a fixed linear score of the features).
    """

    learning = True

    def __init__(self, world, rng, rule="rls", freeze=False, target="energy",
                 eps=0.05, margin=0.5, test_every=20, window=120, z_add=4.0):
        super().__init__(world, rng)
        self.rule_name = rule
        self.V = make_rule(rule)        # visit value
        self.Y = make_rule(rule)        # per-step yield, for in-visit failure
        self.freeze, self.target = freeze, target
        self.eps, self.margin = eps, margin
        self.test_every, self.window, self.z_add = test_every, window, z_add
        self.frozen = False                     # features fixed
        self.frozen_all = False                 # tau and probe policy fixed too
        self.buf = deque(maxlen=window)         # (x, value residual)
        self.ybuf = deque(maxlen=window)        # (x, yield residual)
        self.resid_sd = 1.0                     # running sd of yield residuals
        self.tau = 3.0
        self.recent_fail = deque(maxlen=20)     # 1 if a visit/probe failed
        self.probe_on = False
        self.n_records = 0
        self.added: list[tuple[int, int]] = []  # (t, feature)
        self.name = {None: "learner", False: "learner", "all": "frozen",
                     True: "frozen", "features": "featfrozen"}[freeze] + "-" + rule
        if target != "energy":
            self.name = target + "-" + rule
        self._arb = np.array([2.0, -1.0, 1.5, -2.0, 0.5])

    # --- criterion
    def warns(self, x):
        return self.V.predict(x) < -self.margin

    def attended(self):
        return sorted(self.V.feats)

    def maybe_freeze(self, t):
        if self.freeze and not self.frozen and t >= self.w.t_change:
            self.frozen = True
            self.frozen_all = self.freeze in ("all", True)

    def decide(self, x, t, scenario):
        self.maybe_freeze(t)
        if self.rng.random() < self.eps:
            return "enter"
        if self.warns(x):
            return "skip"
        return "probe" if self.probe_on else "enter"

    def after_probe(self, x, y1, t, scenario):
        failed = y1 < self.Y.predict(x) - self.tau
        self.recent_fail.append(1 if failed else 0)
        self.Y.update(x, y1)
        self._yres(x, y1)
        if failed:
            # an expected yield that did not come: a failure, registered
            # without entering, and recorded as a visit worth only its step
            self.record_visit(x, -self.w.c0, -self.w.c0, t, failed=True)
            return False
        return True

    def fail_step(self, x, y, c_t, t):
        failed = y < self.Y.predict(x) - self.tau
        return failed

    def _yres(self, x, y):
        r = y - self.Y.predict(x)
        self.ybuf.append((x, r))

    def record_step(self, x, y, t, failed=False):
        pred = self.Y.predict(x)
        r = y - pred
        if not self.frozen_all and not failed:
            self.resid_sd = math.sqrt(0.98 * self.resid_sd ** 2 + 0.02 * min(r * r, 25.0))
            self.tau = max(3.0 * self.resid_sd, 0.5)
        self.ybuf.append((x, r))
        self.Y.update(x, y)

    def record_visit(self, x, value, immediate, t, failed=False):
        if self.target == "score":
            tgt = immediate
        elif self.target == "arbitrary":
            tgt = float(self._arb @ x) + self.rng.normal(0, 0.3)
        else:
            tgt = value
        self.buf.append((x, tgt - self.V.predict(x)))
        self.V.update(x, tgt)
        self.recent_fail.append(1 if failed else 0)
        self.n_records += 1
        if not self.frozen_all:
            # probe policy: probe while recent failures are frequent
            self.probe_on = sum(self.recent_fail) >= 3
        if not self.frozen:
            if self.n_records % self.test_every == 0:
                self._revise_features(t)

    def _revise_features(self, t):
        for buf, model in ((self.buf, self.V), (self.ybuf, self.Y)):
            if len(buf) < 60:
                continue
            X = np.array([b[0] for b in buf], dtype=float)
            r = np.array([b[1] for b in buf])
            for f in range(D_FEAT):
                if f in self.V.feats:
                    continue
                a, b = r[X[:, f] == 1], r[X[:, f] == 0]
                if len(a) < 10 or len(b) < 10:
                    continue
                se = math.sqrt(a.var() / len(a) + b.var() / len(b)) + 1e-9
                z = (a.mean() - b.mean()) / se
                if abs(z) > self.z_add:
                    self.V.add_feature(f)
                    self.Y.add_feature(f)
                    self.added.append((t, f))
                    self.buf.clear()
                    self.ybuf.clear()
                    return


ARMS = ["oracle", "designer", "selfset", "learner-rls", "frozen-rls",
        "featfrozen-rls", "learner-tab", "frozen-tab", "featfrozen-tab",
        "score-rls", "arbitrary-rls"]
SCENARIOS = ["none", "delayed", "newfeat", "silent"]


def make_arm(name, world, rng):
    if name == "oracle":
        return Oracle(world, rng)
    if name == "designer":
        return Designer(world, rng)
    if name == "selfset":
        return SelfSet(world, rng)
    kind, rule = name.split("-")
    if kind == "learner":
        return Learner(world, rng, rule=rule)
    if kind == "frozen":
        return Learner(world, rng, rule=rule, freeze="all")
    if kind == "featfrozen":
        return Learner(world, rng, rule=rule, freeze="features")
    return Learner(world, rng, rule=rule, target=kind)


# --------------------------------------------------------------------------
# the run


def streams(seed: int, world: World):
    rng = np.random.default_rng(seed)
    X = rng.integers(0, 2, size=(world.T + 1, D_FEAT))
    noise = rng.normal(0.0, world.sigma, size=world.T + world.L + 2)
    return X, noise


def run(arm_name: str, scenario: str, seed: int, world: World = World(),
        H: int = 20) -> dict:
    X, noise = streams(seed, world)
    arm = make_arm(arm_name, world, np.random.default_rng(10_000 + seed))
    E = world.E0
    t = 0
    i = 0                      # index into the patch stream (common numbers)
    surch: list[list] = []     # [until_t, U]
    pending: list[dict] = []   # visit records awaiting their horizon
    changed = lambda x: (world.true_net(x, scenario, world.t_change) < 0
                         <= world.true_net(x, scenario, 0))
    out = dict(arm=arm_name, scenario=scenario, seed=seed, died=None,
               post_intake=0.0, enc_post=0, false_warn=0, missed=0,
               first_warn=None, first_register=None, probes_pre=0,
               probes_post=0, enc_pre=0)
    attended_at_change = None

    def upkeep(tt):
        return world.c0 + sum(u for until, u in surch if tt < until)

    def step(y, tt):
        nonlocal E
        c = upkeep(tt)
        E = min(E + y - c, world.E_max)
        excess = c - world.c0
        live = [p for p in pending if p["t_end"] <= tt < p["t_end"] + H]
        for p in live:
            p["excess"] += excess / len(live)
        if tt >= world.t_change:
            out["post_intake"] += y - c
        return c

    def flush(tt):
        for p in [p for p in pending if tt >= p["t_end"] + H]:
            arm.record_visit(p["x"], p["net"] - p["excess"], p["net"], tt,
                             failed=p["failed"]) if arm.learning else None
            pending.remove(p)

    while t < world.T:
        if t >= world.t_change and attended_at_change is None:
            attended_at_change = arm.attended()
        x = X[i % len(X)]
        i += 1
        post = t >= world.t_change
        out["enc_post" if post else "enc_pre"] += 1
        tn = world.true_net(x, scenario, t)
        act = arm.decide(x, t, scenario)
        if act == "probe":
            out["probes_post" if post else "probes_pre"] += 1
            E -= world.probe_cost
            if post:
                out["post_intake"] -= world.probe_cost
            y1 = 0.0 if world.silent(x, scenario, t) else world.base_yield(x) + noise[t]
            enter = arm.after_probe(x, y1, t, scenario)
            if not enter and post and changed(x) and out["first_register"] is None:
                out["first_register"] = t - world.t_change
            act = "enter" if enter else "skip"
        if post:
            if act == "skip":
                if tn > 0:
                    out["false_warn"] += 1
                elif changed(x) and out["first_warn"] is None:
                    out["first_warn"] = t - world.t_change
            elif tn < 0:
                out["missed"] += 1
        step(0.0, t)              # the encounter step
        t += 1
        if E <= 0:
            out["died"] = t
            break
        flush(t)
        if act == "enter":
            net, failed = 0.0, False
            for s in range(world.L):
                if t >= world.T:
                    break
                y = 0.0 if world.silent(x, scenario, t) else world.base_yield(x) + noise[t]
                c = step(y, t)
                net += y - world.c0
                fail = arm.fail_step(x, y, c, t)
                if arm.learning:
                    arm.record_step(x, y, t, failed=fail)
                t += 1
                if E <= 0:
                    break
                flush(t)
                if fail:
                    failed = True
                    if t - 1 >= world.t_change and changed(x) and out["first_register"] is None:
                        out["first_register"] = t - 1 - world.t_change
                    break
            if E <= 0:
                out["died"] = t
                break
            if world.delayed(x, scenario, t - 1):
                surch.append([t + world.D, world.U])
            pending.append(dict(x=x, net=net, excess=0.0, t_end=t, failed=failed))
            surch[:] = [s for s in surch if s[0] > t]
    out["E_final"] = E if out["died"] is None else 0.0
    out["survived"] = out["died"] is None
    out["attended_change"] = attended_at_change
    out["attended_end"] = arm.attended()
    out["added"] = getattr(arm, "added", [])
    return out
