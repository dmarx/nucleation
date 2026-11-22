"""CASE-285's simulation arm: same overseer, the acting institution's speed varied.

An acting institution initiates consequential actions as a Poisson stream.
Each action becomes irreversible a random time T after initiation; the
speed factor s divides T's mean. A fraction of actions is objectionable:
the overseer, once it has evaluated one, redirects it. The overseer's
authority (an objection it issues suspends the action), information
(detection delay D), and resources (c reviewers, evaluation time E) are the
same at every speed.

Base path, both arms. The overseer notices an action D after initiation and
queues it for evaluation (first come, first served, c reviewers). An action
whose irreversibility time has passed when a reviewer comes free is skipped
(the overseer does not spend review on what it can no longer stop). An
objectionable action is intercepted iff evaluation finishes and the
objection takes effect (lag I) before T. Benign actions are not delayed.

Variants (CASE-285's three, added one at a time):

- limits: at initiation each action is checked against precommitted limits.
  An objectionable action falls outside them with probability q (coverage),
  a benign one with probability fp. An action outside them is held (its
  clock to irreversibility stops) and escalated: it enters the queue at once,
  needs no detection, and has no deadline. Benign held actions resume after
  evaluation.
- suspend: on detection an action is flagged, objectionable with probability
  h, benign with probability fa. A flagged action detected before T is
  suspended at once and queued without deadline; unflagged ones take the
  base path.
- pause: every action waits a fixed P before its clock to irreversibility
  starts, so T becomes P + T for all actions.

Two readings of "speed" are offered: "latency" (s divides T only; the rate
of actions is the same) and "throughput" (s also multiplies the rate of
actions, so the overseer's fixed capacity is loaded s times as heavily).
"""
from __future__ import annotations

import heapq
from dataclasses import dataclass, replace, asdict

import numpy as np


@dataclass(frozen=True)
class Params:
    speed: float = 1.0          # s: divides the mean time to irreversibility
    reading: str = "latency"    # "latency" or "throughput"
    rate: float = 2.0           # actions per day at s = 1
    p_obj: float = 0.10         # share of actions the overseer would redirect
    t_irr_mean: float = 30.0    # days to irreversibility at s = 1
    t_irr_shape: float = 4.0    # gamma shape of T
    det_mean: float = 2.0       # mean detection delay (exponential), days
    eval_mean: float = 1.5      # mean evaluation time per action, days
    eval_shape: float = 2.0     # gamma shape of E
    reviewers: int = 4          # c
    lag: float = 0.25           # I: time for an issued objection to take effect
    horizon: float = 5.0        # benefit of a benign action = exp(-delay / horizon)
    days: float = 3650.0        # actions initiated in [0, days)
    warmup: float = 365.0       # actions initiated before this are not counted
    variant: str = "none"       # "none", "limits", "suspend", "pause"
    q: float = 0.0              # limits: coverage of objectionable actions
    fp: float = 0.0             # limits: share of benign actions outside limits
    h: float = 0.0              # suspend: share of objectionable actions flagged
    fa: float = 0.0             # suspend: share of benign actions flagged
    pause: float = 0.0          # pause: fixed wait P before each action, days


def fcfs_reneging(enqueue, service, deadline, c):
    """First-come-first-served queue with c servers and reneging at start.

    enqueue, service, deadline: arrays of equal length (deadline may be inf).
    An item whose start time would be at or after its deadline leaves
    unserved and uses no server. Returns (start, finish, served); start and
    finish are nan for unserved items.
    """
    n = len(enqueue)
    order = np.argsort(enqueue, kind="stable")
    free = [0.0] * c
    heapq.heapify(free)
    start = np.full(n, np.nan)
    finish = np.full(n, np.nan)
    served = np.zeros(n, dtype=bool)
    for i in order:
        t0 = max(enqueue[i], free[0])
        if t0 >= deadline[i]:
            continue
        heapq.heapreplace(free, t0 + service[i])
        start[i] = t0
        finish[i] = t0 + service[i]
        served[i] = True
    return start, finish, served


def simulate(p: Params, seed: int) -> dict:
    rng = np.random.default_rng(seed)
    lam = p.rate * (p.speed if p.reading == "throughput" else 1.0)
    n = rng.poisson(lam * p.days)
    t_init = np.sort(rng.uniform(0.0, p.days, n))
    obj = rng.random(n) < p.p_obj
    T = rng.gamma(p.t_irr_shape, p.t_irr_mean / p.speed / p.t_irr_shape, n)
    D = rng.exponential(p.det_mean, n)
    E = rng.gamma(p.eval_shape, p.eval_mean / p.eval_shape, n)
    u1 = rng.random(n)  # limits or flag draw; drawn in every variant so arms share draws

    P = p.pause if p.variant == "pause" else 0.0
    T_eff = P + T                      # time from initiation to irreversibility, unsuspended
    held = np.zeros(n, dtype=bool)     # held/suspended, queued without deadline
    enq = t_init + D                   # base: queued on detection
    if p.variant == "limits":
        held = np.where(obj, u1 < p.q, u1 < p.fp)
        enq = np.where(held, t_init, enq)
    elif p.variant == "suspend":
        flagged = np.where(obj, u1 < p.h, u1 < p.fa)
        held = flagged & (D < T_eff)
    elif p.variant not in ("none", "pause"):
        raise ValueError(p.variant)

    # The overseer skips a base-path action only once it is already
    # irreversible; it does not skip one it could no longer stop in time.
    deadline = np.where(held, np.inf, t_init + T_eff)
    detected_in_time = held | (D < T_eff)
    # actions detected after irreversibility never enter the queue
    enq_q = np.where(detected_in_time, enq, np.inf)
    deadline_q = np.where(detected_in_time, deadline, -np.inf)
    start, finish, served = fcfs_reneging(enq_q, E, deadline_q, p.reviewers)

    intercepted = np.zeros(n, dtype=bool)
    base_ok = served & ~held & (finish + p.lag < t_init + T_eff)
    intercepted |= base_ok & obj
    intercepted |= held & obj  # suspended before irreversibility, whether or not yet evaluated
    # Delay to effect for benign actions: T_eff plus time held. Holding stops
    # the clock (at initiation for limits, at detection for suspension) and it
    # restarts when evaluation finishes; nan if still held at the end of the run.
    hold_time = np.where(held, np.where(served, finish - enq, np.nan), 0.0)
    delay = T_eff + hold_time

    count = (t_init >= p.warmup) & (t_init < p.days - 10 * p.t_irr_mean)
    ob = count & obj
    be = count & ~obj
    be_done = be & np.isfinite(delay)
    benefit = np.where(be_done, np.exp(-np.nan_to_num(delay, nan=np.inf) / p.horizon), 0.0)

    busy = float(np.nansum(np.where(served, E, 0.0)))
    return {
        "n_counted": int(count.sum()),
        "intervention_capacity": float(intercepted[ob].mean()) if ob.any() else float("nan"),
        "detected_before_irreversible_obj": float(detected_in_time[ob].mean()) if ob.any() else float("nan"),
        "benefit_per_benign": float(benefit[be].mean()),
        "benign_mean_delay": float(np.nanmean(np.where(be_done, delay, np.nan)[be])),
        "benign_share_held": float(held[be].mean()),
        "benign_unfinished_held": float((be & held & ~served).mean() / max(be.mean(), 1e-12)),
        "obj_irreversible_per_1000": float(1000 * (ob & ~intercepted).sum() / count.sum()),
        "reviewer_utilization": busy / (p.reviewers * p.days),
        "reviews_per_interception": float(served[count].sum() / max(intercepted[ob].sum(), 1)),
    }


def summarize(rows) -> dict:
    keys = rows[0].keys()
    out = {}
    for k in keys:
        v = np.array([r[k] for r in rows], dtype=float)
        out[k] = {"mean": float(np.mean(v)), "sd": float(np.std(v, ddof=1)) if len(v) > 1 else 0.0,
                  "min": float(np.min(v)), "max": float(np.max(v))}
    return out


def run(p: Params, seeds) -> tuple[dict, list[dict]]:
    """Per-seed rows and their summary (mean, sd across seeds, min, max)."""
    rows = [simulate(p, s) for s in seeds]
    return {"params": asdict(p), **summarize(rows)}, rows


def timing_prediction(p: Params) -> bool:
    """A23 section 3's condition read deterministically at the means:
    detection + evaluation + intervention within the time before harm."""
    return p.det_mean + p.eval_mean + p.lag < p.pause * (p.variant == "pause") + p.t_irr_mean / p.speed


__all__ = ["Params", "fcfs_reneging", "simulate", "run", "summarize", "timing_prediction", "replace"]
