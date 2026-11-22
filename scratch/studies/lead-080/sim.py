"""LEAD-080: A's readiness simulator (QUESTION-394) under two budget regimes.

The simulator is the one QUESTION-394 records from A's proposal: one or two
heavy rescue squads, two incident types (a reported collision that does or
does not need extrication), Poisson arrivals, a first-unit assessment of
configurable accuracy, travel delays from distance, mutual aid as the
substitute, and a skill variable that decays without maintenance. The budget
is CLAIM-577's: a capacity ceiling B_t per period (a month), with spending s_t
the peak capacity occupied in the period.

Capacity.  r = h + r_s * n, where n is the number of squads mobilized at once
(dispatched and not yet back, or drilling). h = 0.7 is holding: the engine
crew on duty and the squad kept in quarters. r_s = 0.6 is one squad called up
and staffed. One squad out costs 1.3, CLAIM-577's worked numbers. A
mobilization is allowed only if h + r_s * (n + 1) <= B_t.

Budget regimes (B_0 = h + r_s * n_squads in all):
  spend-matching   B_{t+1} = s_t                         (CLAIM-577)
  peak-carry       B_{t+1} = s_t + rho * (B_t - s_t)     (the peak rule with the
                                                         unspent part rolled
                                                         over; rho = 1 keeps
                                                         B_t = B_0, the control)
  base-carry       B_{t+1} = Bbar + rho * (B_t - s_t)    (CASE-200's recursion,
                                                         alpha = 0, Bbar = 1.0)

Skill. k_{t+1} = min(1, (1 - delta) k_t + beta * (drills + extrications)),
QUESTION-386's recursion with a cap; delta = 0.09 a month loses half in about
7.4 months (CLAIM-558: half "after between 6 and 9 months of infrequent
use"). A response is qualified when the responder's k >= k_req = 0.5.
Mutual aid is taken as qualified.

Timely: the qualified responder is on scene within D minutes of the call.

All rates, distances and costs are invented to show mechanisms.
"""
import json
import math
import sys
from dataclasses import dataclass, field, asdict, replace

import numpy as np

MONTH = 30 * 24 * 60.0  # minutes
EPS = 1e-9
KEY = {"busy": "gap", "blocked": "blocked"}


@dataclass(frozen=True)
class Params:
    months: int = 120
    lam: float = 6.0          # reported collisions a month in the squad's area
    p_need: float = 0.1       # share needing extrication
    acc: float = 0.9          # first-unit assessment sensitivity = specificity
    policy: str = "provisional"   # or "confirm"
    regime: str = "spend-matching"  # or "peak-carry", "base-carry"
    rho: float = 1.0          # share of unspent budget rolled over
    bbar: float = 1.0         # base budget (base-carry regime)
    n_squads: int = 1
    h: float = 0.7
    r_s: float = 0.6
    drill_every: int = 3      # months between drills; 0 = never
    drill_minutes: float = 240.0
    delta: float = 0.09
    beta: float = 0.3
    k0: float = 1.0
    k_req: float = 0.5
    deadline: float = 20.0    # minutes from call to qualified responder on scene
    recog: float = 10.0       # minutes for a missed need to be recognized
    ma_extra_km: float = 12.0  # mutual aid comes from this much farther
    work_mean: float = 60.0
    fp_release: float = 10.0
    H: float = 10.0           # harm of a true need not met in time (CLAIM-561)
    c0: float = 1.0           # cost of an unneeded dispatch
    c1: float = 0.5           # cost of a needed dispatch


def base_carry_periods_to_reach(bbar, rho_eff, h, target, B0, max_n=1000):
    """Periods of holding needed under B_{t+1} = Bbar + rho_eff (B_t - h)
    for the budget to reach target, or None if it never does."""
    if B0 < target and rho_eff < 1:
        fixed = (bbar - rho_eff * h) / (1 - rho_eff)
        if fixed <= target:   # approached from below, never reached
            return None
    B = B0
    for n in range(max_n + 1):
        if B >= target - EPS:
            return n
        B = bbar + rho_eff * (B - h)
    return None


def next_budget(regime, B, s, params):
    """The budget rule: B_{t+1} from B_t and the period's peak spending s_t."""
    if regime == "spend-matching":
        return s
    if regime == "peak-carry":
        return s + params.rho * (B - s)
    if regime == "base-carry":
        return params.bbar + params.rho * (B - s)
    raise ValueError(regime)


def capacity(params, n_out):
    return params.h + params.r_s * n_out


def draw_calls(params, rng):
    """All calls for one run: time, need, assessment, A, T, T_ma."""
    n = rng.poisson(params.lam * params.months)
    t = np.sort(rng.uniform(0, params.months * MONTH, n))
    need = rng.random(n) < params.p_need
    correct = rng.random(n) < params.acc
    says_need = np.where(correct, need, ~need)
    dE = rng.uniform(0.3, 3.0, n)
    dS = rng.uniform(1.0, 14.0, n)
    A = 1.0 + dE / 0.7 + 2.0        # engine turnout, travel, assessment
    T = 1.5 + dS / 0.8              # squad turnout and travel
    Tma = 1.5 + (dS + params.ma_extra_km) / 0.8
    work = rng.exponential(params.work_mean, n)
    return [dict(t=float(t[i]), need=bool(need[i]), says=bool(says_need[i]),
                 A=float(A[i]), T=float(T[i]), Tma=float(Tma[i]),
                 work=float(work[i])) for i in range(n)]


def simulate(params, calls):
    """Run one history. Returns per-month series and totals."""
    P = params
    M = P.months
    busy = [0.0] * P.n_squads           # busy-until time per squad
    B = np.zeros(M + 1)
    s = np.full(M, P.h)                 # peak spending each month
    k = np.zeros(M + 1)
    B[0] = capacity(P, P.n_squads)
    k[0] = P.k0
    practice = np.zeros(M)
    tot = dict(needs=0, met=0, cancelled=0, unneeded=0, needed=0,
               gap=0, blocked=0, busy_min=0.0, drills=0, drills_blocked=0,
               ma=0)
    needs_by_month = np.zeros(M)
    met_by_month = np.zeros(M)

    def month_of(t):
        return min(int(t // MONTH), M - 1)

    def try_mobilize(t, until):
        """Mobilize a free squad at time t if one is free and the budget
        allows; returns the squad index, 'busy' or 'blocked'."""
        m = month_of(t)
        free = [j for j in range(P.n_squads) if busy[j] <= t + EPS]
        if not free:
            return "busy"
        n_out = P.n_squads - len(free)
        need_cap = capacity(P, n_out + 1)
        if need_cap > B[m] + EPS:
            return "blocked"
        j = free[0]
        busy[j] = until
        tot["busy_min"] += until - t
        s[m] = max(s[m], need_cap)
        # a mobilization running into later months occupies them too
        for m2 in range(m + 1, month_of(until) + 1):
            s[m2] = max(s[m2], capacity(P, 1))
        return j

    ci = 0
    for m in range(M):
        t_start = m * MONTH
        # drill at the start of the month
        if P.drill_every and m % P.drill_every == 0:
            ok = True
            for _ in range(P.n_squads):
                r = try_mobilize(t_start, t_start + P.drill_minutes)
                if not isinstance(r, int):
                    ok = False
            if ok:
                tot["drills"] += 1
                practice[m] += 1
            else:
                tot["drills_blocked"] += 1
        while ci < len(calls) and calls[ci]["t"] < (m + 1) * MONTH:
            c = calls[ci]
            ci += 1
            t0, A, T = c["t"], c["A"], c["T"]
            need, says = c["need"], c["says"]
            arrival = None      # own squad on scene, minutes after call
            ma_from = None      # time mutual aid is requested
            used_own = False
            if P.policy == "provisional":
                if says or T <= A:
                    # squad continues: either the engine confirms, or the
                    # squad is on scene first and sees for itself
                    if need:
                        until = t0 + T + c["work"] + T
                    elif says:
                        until = t0 + T + P.fp_release + T
                    else:
                        until = t0 + 2 * T   # arrived first, sees nothing
                    r = try_mobilize(t0, until)
                    if isinstance(r, int):
                        used_own = True
                        if need:
                            arrival = T
                            tot["needed"] += 1
                        else:
                            tot["unneeded"] += 1
                    else:
                        if need:
                            tot[KEY[r]] += 1
                        if need:
                            ma_from = t0
                else:
                    # cancelled when the engine reports no need
                    r = try_mobilize(t0, t0 + 2 * A)
                    if isinstance(r, int):
                        tot["cancelled"] += 1
                        tot["unneeded"] += 1
                    if need:
                        # a missed need, recognized later; re-dispatch
                        t1 = t0 + A + P.recog
                        r2 = try_mobilize(t1, t1 + T + c["work"] + T)
                        if isinstance(r2, int):
                            used_own = True
                            arrival = A + P.recog + T
                            tot["needed"] += 1
                        else:
                            tot[KEY[r2]] += 1
                            ma_from = t1
            elif P.policy == "confirm":
                t1 = t0 + A if says else t0 + A + P.recog
                if says or need:
                    if need:
                        until = t1 + T + c["work"] + T
                    else:
                        until = t1 + T + P.fp_release + T
                    r = try_mobilize(t1, until)
                    if isinstance(r, int):
                        used_own = True
                        if need:
                            arrival = (t1 - t0) + T
                            tot["needed"] += 1
                        else:
                            tot["unneeded"] += 1
                    else:
                        if need:
                            tot[KEY[r]] += 1
                            ma_from = t1
            else:
                raise ValueError(P.policy)
            if need:
                tot["needs"] += 1
                needs_by_month[m] += 1
                met = False
                if used_own and arrival is not None:
                    met = arrival <= P.deadline + EPS and k[m] >= P.k_req
                    practice[m] += 1
                elif ma_from is not None:
                    tot["ma"] += 1
                    met = (ma_from - t0) + c["Tma"] <= P.deadline + EPS
                if met:
                    tot["met"] += 1
                    met_by_month[m] += 1
        B[m + 1] = next_budget(P.regime, B[m], s[m], P)
        k[m + 1] = min(1.0, (1 - P.delta) * k[m] + P.beta * practice[m])
    return dict(B=B, s=s, k=k, tot=tot, needs_by_month=needs_by_month,
                met_by_month=met_by_month)


def lost_for_good(B, full, min_tail=12):
    """First month from which the budget stays below the mobilization cost
    to the end of the run, if that stretch is at least min_tail months."""
    ok = np.nonzero(B >= full - EPS)[0]
    first_bad = 0 if len(ok) == 0 else int(ok[-1]) + 1
    return first_bad if len(B) - first_bad >= min_tail else None


def summarize(params, runs):
    P = params
    full = capacity(P, 1)
    lost_month = [lost_for_good(r["B"][:P.months], full) for r in runs]
    frac_lost = np.mean([lm is not None for lm in lost_month])
    lm = [x for x in lost_month if x is not None]
    reach = np.array([np.mean(r["B"][:P.months] >= full - EPS) for r in runs])
    all_cap = capacity(P, P.n_squads)
    reach_all = np.array([np.mean(r["B"][:P.months] >= all_cap - EPS) for r in runs])
    def pmet(r, a, b):
        n = r["needs_by_month"][a:b].sum()
        return r["met_by_month"][a:b].sum() / n if n else np.nan
    p_all = np.array([pmet(r, 0, P.months) for r in runs])
    p_late = np.array([pmet(r, P.months // 2, P.months) for r in runs])
    k_end = np.array([r["k"][P.months] for r in runs])
    tots = {key: np.array([r["tot"][key] for r in runs], float)
            for key in runs[0]["tot"]}
    cost = (P.H * (tots["needs"] - tots["met"]) + P.c0 * tots["unneeded"]
            + P.c1 * tots["needed"]) / P.months
    meanB = np.array([r["B"][:P.months].mean() for r in runs])
    q = lambda a: [float(np.percentile(a, 25)), float(np.median(a)),
                   float(np.percentile(a, 75))] if len(a) else None
    return dict(
        params=asdict(P), seeds=len(runs),
        frac_lost=float(frac_lost),
        lost_month_quartiles=q(np.array(lm)),
        months_reachable=float(reach.mean()), months_reachable_sd=float(reach.std()),
        months_all_squads_reachable=float(reach_all.mean()),
        p_met=float(np.nanmean(p_all)), p_met_sd=float(np.nanstd(p_all)),
        p_met_late=float(np.nanmean(p_late)), p_met_late_sd=float(np.nanstd(p_late)),
        k_end=float(k_end.mean()),
        cancel_per_month=float((tots["cancelled"] / P.months).mean()),
        busy_hours_per_month=float((tots["busy_min"] / 60 / P.months).mean()),
        gap_needs=float(tots["gap"].mean()), blocked_needs=float(tots["blocked"].mean()),
        needs=float(tots["needs"].mean()),
        drills_blocked=float(tots["drills_blocked"].mean()),
        cost_per_month=float(cost.mean()), cost_sd=float(cost.std()),
        mean_budget=float(meanB.mean()),
    )


def run_config(params, seeds, base_seed=20261122):
    runs = []
    for i in range(seeds):
        rng = np.random.default_rng([base_seed, i])
        runs.append(simulate(params, draw_calls(params, rng)))
    return summarize(params, runs)


REGIMES = [("spend-matching", {}), ("peak-carry", {"rho": 1.0}),
           ("peak-carry", {"rho": 0.6}), ("base-carry", {"rho": 1.0}),
           ("base-carry", {"rho": 0.6})]


def grid():
    regimes = REGIMES
    out = []
    for lam in (2.0, 6.0):
        for policy in ("provisional", "confirm"):
            for drill in (1, 3, 0):
                for regime, kw in regimes:
                    out.append(Params(lam=lam, policy=policy, drill_every=drill,
                                      regime=regime, **kw))
    # two squads: one row pair
    for regime, kw in regimes:
        out.append(Params(lam=6.0, policy="provisional", drill_every=3,
                          n_squads=2, regime=regime, **kw))
    return out


def label(P):
    reg = P.regime + (f"(rho={P.rho})" if P.regime != "spend-matching" else "")
    return (f"lam={P.lam:g} {P.policy:<11} drill={P.drill_every or 'never':<5} "
            f"squads={P.n_squads} {reg}")


def main(seeds=300, out_json=None):
    results = []
    hdr = ("config", "lost", "lost-month IQR", "reach", "P(met)", "sd",
           "P(met) yrs6-10", "sd", "k_end", "cancel/mo", "busy h/mo",
           "blocked", "cost/mo", "mean B")
    print(" | ".join(hdr))
    for P in grid():
        r = run_config(P, seeds)
        results.append(r)
        iqr = r["lost_month_quartiles"]
        iqr_s = f"{iqr[0]:.0f}-{iqr[1]:.0f}-{iqr[2]:.0f}" if iqr else "-"
        print(f"{label(P)} | {r['frac_lost']:.2f} | {iqr_s} | "
              f"{r['months_reachable']:.2f} | {r['p_met']:.3f} | {r['p_met_sd']:.3f} | "
              f"{r['p_met_late']:.3f} | {r['p_met_late_sd']:.3f} | {r['k_end']:.2f} | "
              f"{r['cancel_per_month']:.2f} | {r['busy_hours_per_month']:.1f} | "
              f"{r['blocked_needs']:.1f} | {r['cost_per_month']:.2f} | {r['mean_budget']:.2f}",
              flush=True)
    if out_json:
        with open(out_json, "w") as f:
            json.dump(results, f, indent=1)


if __name__ == "__main__":
    main(out_json=sys.argv[1] if len(sys.argv) > 1 else None)
