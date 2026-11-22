"""CASE-255 on CASE-186's organization (LEAD-140).

Built on LEAD-048's model (scratch/studies/lead-048/model.py), imported, not
copied. The organization of that model is the *artifact*: its procedures
theta (audit interval, audit size, self-check interval, repair time,
teacher-correction rate) are what the collective improves. The *improver*
is the procedure that proposes and accepts changes to theta. It has
settings phi and a record (an archive of past proposals and their measured
effects). In the adaptive arms the collective also changes phi, judging a
proposed change to phi under one of four evaluation arrangements.

Episode. One run of LEAD-048's `run` with theta applied, on a shortened
schedule (+ until 50, - from 50, S1 judged at 149, injury at 150, second
change at 200, end 350). Its score is
    U = -(regret_all + LAMBDA * fuel_spent) / end - PEN * (1 - ok),
the throughput of the working system (wrong actions and fuel, per step)
less a penalty when its findings are wrong: ok is S1 and S2 of LEAD-048's
endpoints. The penalty is needed because in regime 0 no action is preferred,
so throughput alone never registers a missed out-of-family change.

Episode kinds:
    ordinary  sham injury, in-family second change
    oof       sham injury, out-of-family second change (regime 0)
    dmg:<op>  an undisclosed lesion of generate, admit or score at 150,
              in-family second change
    obsolete  the teacher is reset at 150 to the habit (+), an obsolete
              instruction, in-family second change

The improver's evaluation suite draws episodes in proportions phi.d_dmg
(damage, op uniform), phi.d_oof (out of family), and the rest ordinary.

One generation (budget B episodes): n_cand candidates, each one move of one
theta field by one step on its grid, proposed uniformly or, with the
archive, by the archive's record of each move's past effect; the incumbent
and every candidate are scored on the same m episodes (common random
numbers), m = (B - canary cost) // (n_cand + 1); the best candidate is
accepted if it beats the incumbent. With phi.canary, 4 episodes first test
the suite: the incumbent with its self-check switched off must lose to the
incumbent on 2 damage episodes; if not, the suite is flagged, nothing is
accepted this generation, and the suite is restored to its commissioned
definition (its lesion removed) before the next.

Meta-step (adaptive arms, every META_EVERY generations): propose phi' (one
field, one step). Run META_GENS generations from the current theta under phi
and under phi' on the same seeds; score both resulting artifacts on M_META
episodes of the arm's meta-evaluator; keep the better improver and its
artifact. Meta-evaluators:
    public    ordinary episodes only (the performance-gated arm)
    own       the incumbent phi's own suite
    external  a fixed outer suite (1/3 damage, 1/3 oof), on a seed pool the
              collective never trains on; its episodes counted as outside cost
    layered   own, but a change that weakens verification (lowers d_dmg,
              d_oof or canary, or a theta move that makes self-check rarer
              or removes it) also needs the external suite's agreement
"""
from __future__ import annotations

import os
import sys
from dataclasses import dataclass, replace

import numpy as np

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "lead-048"))
from model import Config, Org, run  # noqa: E402

# ------------------------------------------------------------------ world
SCHED = dict(T1=50, W1=100, T_INJ=150, T2=200, W2=150)
LAMBDA = 0.2
PEN = 0.3
END = SCHED["T2"] + SCHED["W2"]

GRID = {
    "AUDIT_EVERY": (5, 10, 20, 40, 80),
    "N_AUDIT": (16, 32, 64, 128, 256),
    "SELF_CHECK_EVERY": (10, 20, 40, 80, 0),   # 0 = no self-check
    "REPAIR_STEPS": (10, 30, 90),
    "TEACH": (0.05, 0.1, 0.2, 0.4),
}
FIELDS = tuple(GRID)
THETA0 = (1, 4, 1, 1, 1)  # 10, 256, 20, 30, 0.1: LEAD-048's settings
MOVES = tuple((i, s) for i in range(len(FIELDS)) for s in (-1, 1))
SC = FIELDS.index("SELF_CHECK_EVERY")


@dataclass(frozen=True)
class Config140(Config):
    TEACH: float = 0.1


class Org140(Org):
    """LEAD-048's organization with a tunable teacher-correction rate and an
    'obsolete' injury (the teacher reset to the habit)."""

    def copy(self, t):
        c, st = self.cfg, self.st
        if t % c.ERASE_EVERY == 0:
            st.student = 1
            if self.pay(c.COST_COPY, t) and self.rng.random() < st.G:
                st.student = st.interp
        elif st.student != st.interp and self.rng.random() < c.TEACH:
            if self.pay(c.COST_COPY, t) and self.rng.random() < st.G:
                st.student = st.interp

    def injure(self, t):
        if self.cfg.lesion == "obsolete":
            self.st.interp = 1
        else:
            super().injure(t)


def theta_values(theta):
    return {f: GRID[f][i] for f, i in zip(FIELDS, theta)}


def cfg_for(theta, kind):
    v = theta_values(theta)
    sc = v["SELF_CHECK_EVERY"]
    kw = dict(SCHED, AUDIT_EVERY=v["AUDIT_EVERY"], N_AUDIT=v["N_AUDIT"],
              REPAIR_STEPS=v["REPAIR_STEPS"], TEACH=v["TEACH"],
              self_check=sc != 0, SELF_CHECK_EVERY=sc or 20)
    if kind == "ordinary":
        return Config140(**kw)
    if kind == "oof":
        return Config140(env2="out_family", **kw)
    if kind == "obsolete":
        return Config140(lesion="obsolete", **kw)
    if kind.startswith("dmg:"):
        return Config140(lesion=kind[4:], **kw)
    raise ValueError(kind)


def episode(theta, kind, seed):
    r = run(cfg_for(theta, kind), seed, Org140)
    ok = bool(r["S1"] and r["S2"])
    U = -(r["regret_all"] + LAMBDA * r["fuel_spent"]) / END - PEN * (not ok)
    return U, ok


# ------------------------------------------------------------------ improver
PHI_GRID = {
    "n_cand": (1, 2, 3, 5),
    "d_dmg": (0.0, 0.25, 0.5),
    "d_oof": (0.0, 0.25, 0.5),
    "archive": (0, 1),
    "canary": (0, 1),
}
PHI_FIELDS = tuple(PHI_GRID)
PHI0 = (0, 1, 1, 0, 1)   # one candidate, 1/4 damage, 1/4 oof, no archive, canary
VERIF_PHI = ("d_dmg", "d_oof", "canary")
B = 32
CANARY_COST = 4
DMG_OPS = ("generate", "admit", "score")


def phi_values(phi):
    return {f: PHI_GRID[f][i] for f, i in zip(PHI_FIELDS, phi)}


def weakens_phi(phi, phi2):
    return any(phi2[PHI_FIELDS.index(f)] < phi[PHI_FIELDS.index(f)]
               for f in VERIF_PHI)


def weakens_theta_move(move):
    i, s = move
    return i == SC and s > 0


def apply_move(theta, move):
    i, s = move
    j = theta[i] + s
    if j < 0 or j >= len(GRID[FIELDS[i]]):
        return None
    t = list(theta)
    t[i] = j
    return tuple(t)


@dataclass
class Suite:
    """The improver's evaluation suite, and its lesion state."""
    d_dmg: float
    d_oof: float
    lesion: str = "sham"   # sham | generate | admit | score

    def kinds(self, rng, m):
        out = []
        for _ in range(m):
            u = rng.random()
            if u < self.d_dmg:
                k = "dmg:" + DMG_OPS[rng.integers(3)]
            elif u < self.d_dmg + self.d_oof:
                k = "oof"
            else:
                k = "ordinary"
            out.append(self.silently(k))
        return out

    def silently(self, k):
        # generate lesion: the suite stops sampling damage and oof cases,
        # silently running ordinary episodes in their place
        if self.lesion == "generate" and k != "ordinary":
            return "ordinary"
        return k

    def score(self, results, incumbent=False):
        """Mean U over episodes; admit lesion drops failed damage episodes
        (contradicting evidence filtered); score lesion favours the
        incumbent (agreement with prior conclusions)."""
        us = []
        for (k, (U, ok)) in results:
            if self.lesion == "admit" and k != "ordinary" and not ok:
                continue
            us.append(U)
        s = float(np.mean(us)) if us else 0.0
        if self.lesion == "score" and incumbent:
            s += 0.05
        return s


class Archive:
    """The record: every proposed move, and its measured effect."""

    def __init__(self, data=None):
        self.data = {m: list(v) for m, v in (data or {}).items()}

    def add(self, move, delta):
        self.data.setdefault(move, []).append(float(delta))

    def weights(self, moves, beta=200.0):
        w = []
        for m in moves:
            v = self.data.get(m)
            mu = float(np.mean(v)) if v else 0.0
            n = len(v) if v else 0
            # optimistic for untried moves; tempered by the mean effect
            w.append(np.exp(np.clip(beta * mu, -6, 6)) * (1.0 if n else 1.5))
        w = np.asarray(w)
        return w / w.sum()

    def dump(self):
        return [[list(m), v] for m, v in self.data.items()]

    @classmethod
    def load(cls, d):
        return cls({tuple(m): v for m, v in d})


class Ledger:
    def __init__(self):
        self.inner = 0
        self.outer = 0


def generation(theta, phi, archive, suite, rng, ledger, ext_veto=None):
    """One generation of the improver. Returns (theta', info)."""
    pv = phi_values(phi)
    info = {"flagged": False, "accepted": None}
    budget = B
    if pv["canary"]:
        budget -= CANARY_COST
        seeds = rng.integers(1_000_000, 2_000_000, 2)
        kinds = [suite.silently("dmg:" + DMG_OPS[rng.integers(3)]) for _ in seeds]
        bad = list(theta)
        bad[SC] = len(GRID["SELF_CHECK_EVERY"]) - 1
        bad = tuple(bad)
        r_inc = [(k, episode(theta, k, int(s))) for k, s in zip(kinds, seeds)]
        r_bad = [(k, episode(bad, k, int(s))) for k, s in zip(kinds, seeds)]
        ledger.inner += 4
        gap = suite.score(r_inc, incumbent=True) - suite.score(r_bad)
        if bad == theta:
            gap = 1.0  # nothing to test against
        if gap < 0.05:
            info["flagged"] = True
            suite.lesion = "sham"  # restored from its commissioned definition
            return theta, info
    moves = [mv for mv in MOVES if apply_move(theta, mv) is not None]
    nc = min(pv["n_cand"], len(moves))
    if pv["archive"]:
        p = archive.weights(moves)
        idx = rng.choice(len(moves), size=nc, replace=False, p=p)
    else:
        idx = rng.choice(len(moves), size=nc, replace=False)
    cands = [moves[i] for i in idx]
    m = budget // (nc + 1)
    seeds = rng.integers(1_000_000, 2_000_000, m)
    kinds = suite.kinds(rng, m)
    r0 = [(k, episode(theta, k, int(s))) for k, s in zip(kinds, seeds)]
    s0 = suite.score(r0, incumbent=True)
    ledger.inner += m * (nc + 1)
    best, best_s = None, s0
    for mv in cands:
        th = apply_move(theta, mv)
        r = [(k, episode(th, k, int(s))) for k, s in zip(kinds, seeds)]
        s = suite.score(r)
        archive.add(mv, s - s0)
        if s > best_s:
            best, best_s = mv, s
    if best is not None and ext_veto is not None and weakens_theta_move(best):
        if not ext_veto(theta, apply_move(theta, best)):
            best = None
    if best is not None:
        info["accepted"] = list(best)
        return apply_move(theta, best), info
    return theta, info


# ------------------------------------------------------------------ evaluators
OUTER = Suite(d_dmg=1 / 3, d_oof=1 / 3)
M_META = 24
M_VETO = 12


def evaluate(theta, suite, seeds, rng):
    kinds = suite.kinds(rng, len(seeds))
    return float(np.mean([episode(theta, k, int(s))[0]
                          for k, s in zip(kinds, seeds)]))


def compare(th_a, th_b, suite, seeds, rng_seed):
    """Score two artifacts on the same episodes. Returns (sa, sb)."""
    sa = evaluate(th_a, suite, seeds, np.random.default_rng(rng_seed))
    sb = evaluate(th_b, suite, seeds, np.random.default_rng(rng_seed))
    return sa, sb


def make_ext_veto(rng, ledger):
    def veto(th_a, th_b):
        seeds = rng.integers(3_000_000, 4_000_000, M_VETO)
        rs = int(rng.integers(1 << 30))
        sa, sb = compare(th_a, th_b, OUTER, seeds, rs)
        ledger.outer += 2 * M_VETO
        return sb >= sa
    return veto


ARMS = ("none", "archive", "public", "own", "external", "layered")
META_EVERY = 4
META_GENS = 2


def lineage(arm, seed, G=30):
    """Run one lineage for G generations. Returns its history and end state."""
    rng = np.random.default_rng([seed, 140])
    ledger = Ledger()
    theta, phi = THETA0, PHI0
    if arm == "archive":
        phi = (0, 1, 1, 1, 1)
    archive = Archive()
    hist = []
    adaptive = arm in ("public", "own", "external", "layered")
    veto = make_ext_veto(rng, ledger) if arm == "layered" else None
    g = 0
    while g < G:
        pv = phi_values(phi)
        if adaptive and g > 0 and g % META_EVERY == 0 and g + META_GENS <= G:
            fi = int(rng.integers(len(PHI_FIELDS)))
            s = 1 if rng.random() < 0.5 else -1
            j = phi[fi] + s
            if 0 <= j < len(PHI_GRID[PHI_FIELDS[fi]]):
                phi2 = tuple(j if k == fi else x for k, x in enumerate(phi))
                gseed = int(rng.integers(1 << 30))
                outs = []
                for ph in (phi, phi2):
                    r2 = np.random.default_rng(gseed)
                    th, ar = theta, Archive.load(archive.dump())
                    q = phi_values(ph)
                    for _ in range(META_GENS):
                        th, _ = generation(th, ph, ar, Suite(q["d_dmg"], q["d_oof"]),
                                           r2, ledger, veto)
                    outs.append((th, ar))
                seeds = rng.integers(1_000_000, 2_000_000, M_META)
                rs = int(rng.integers(1 << 30))
                if arm == "public":
                    ev = Suite(0.0, 0.0)
                elif arm == "external":
                    ev = OUTER
                    seeds = rng.integers(3_000_000, 4_000_000, M_META)
                else:
                    ev = Suite(pv["d_dmg"], pv["d_oof"])
                sa, sb = compare(outs[0][0], outs[1][0], ev, seeds, rs)
                if arm == "external":
                    ledger.outer += 2 * M_META
                else:
                    ledger.inner += 2 * M_META
                take = sb > sa
                if take and arm == "layered" and weakens_phi(phi, phi2):
                    take = veto(outs[0][0], outs[1][0])
                k = 1 if take else 0
                theta, archive = outs[k]
                hist.append({"g": g, "meta": True, "phi_from": list(phi),
                             "phi_to": list(phi2), "took": take,
                             "theta": list(theta)})
                if take:
                    phi = phi2
                g += META_GENS
                continue
        pv = phi_values(phi)
        suite = Suite(pv["d_dmg"], pv["d_oof"])
        theta, info = generation(theta, phi, archive, suite, rng, ledger, veto)
        hist.append({"g": g, "theta": list(theta), **info})
        g += 1
    return {"arm": arm, "seed": seed, "G": G, "theta": list(theta),
            "phi": list(phi), "archive": archive.dump(), "history": hist,
            "inner_eps": ledger.inner, "outer_eps": ledger.outer}


def improve(theta, phi, archive, H, seed, lesion="sham", arm=None):
    """Apply a frozen improver (phi and a copy of its archive) to an artifact
    for H generations at budget B each, on seeds fixed by `seed`. The
    improver lesion, if any, is applied at the start and stays until the
    canary finds it. Returns (theta, flagged_at)."""
    rng = np.random.default_rng([seed, 255])
    ledger = Ledger()
    ar = Archive.load(archive.dump() if isinstance(archive, Archive) else archive)
    pv = phi_values(phi)
    suite = Suite(pv["d_dmg"], pv["d_oof"], lesion=lesion)
    if lesion == "obsolete":
        phi, ar = PHI0, Archive()
        pv = phi_values(phi)
        suite = Suite(pv["d_dmg"], pv["d_oof"])
    veto = make_ext_veto(rng, ledger) if arm == "layered" else None
    flagged_at = None
    for h in range(H):
        theta, info = generation(theta, phi, ar, suite, rng, ledger, veto)
        if info["flagged"] and flagged_at is None:
            flagged_at = h
    return tuple(theta), flagged_at, ledger.inner, ledger.outer


# ------------------------------------------------------------------ held-out
HELD_SEEDS = tuple(range(5_000_000, 5_000_024))
BATTERY = ("ordinary", "oof", "dmg:generate", "dmg:admit", "dmg:score",
           "obsolete")


def battery(theta):
    """The frozen held-out set: hidden ground truth, seeds no improver saw."""
    out = {}
    for k in BATTERY:
        rs = [episode(tuple(theta), k, s) for s in HELD_SEEDS]
        out[k] = {"U": round(float(np.mean([u for u, _ in rs])), 5),
                  "ok": int(sum(ok for _, ok in rs))}
    return out
