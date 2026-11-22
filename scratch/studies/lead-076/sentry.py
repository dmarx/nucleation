"""CASE-153's self-protecting sentry, run in full (LEAD-076, part 2).

A hidden world x_t in {safe=0, dangerous=1}; the experimenter sees it, the
agent does not. Each step the agent (1) inspects or shelters; inspecting
reveals x with accuracy `acc` at cost `c`, sheltering yields nothing;
(2) takes a posture, protect (cost `ell`, whatever the state) or engage
(harm `L` if the state is dangerous). Inspection is physically safe.

A sentry process holds authority g in [0, 1]. It biases posture toward
protection and, where evidence restriction is on, blocks inspection:

    P(inspect) = sigma(beta_i * (VOI_t - c - kappa_e * g * restrict))
    P(protect) = sigma(beta_p * (b_t * L - ell + kappa_a * g))
    g <- (1 - eta) * g + eta * F_t

VOI_t is the myopic value of one inspection for the posture decision,
b_t the agent's belief in danger under a known switching hazard h.
F_t is the governance feedback:

- 'independent': F = the evaluator's belief in danger, formed from the
  evidence the evaluator receives (the agent's own observations, plus the
  audit's where there is one);
- 'success': F = 1 when the sentry's policy looked successful, i.e. the
  agent protected (no harm followed) or engaged and was harmed; F = 0 when
  it engaged and nothing happened. Under protection the outcome is the same
  in both states, so relief reinforces the sentry whatever x is;
- 'fixed': F = g (authority never changes).

Correction rights: 'ordinary' (nothing more), 'audit' (with probability q
each step an independent observation of x, accuracy acc, reaches the
evaluator; under success feedback it replaces F on that step with 1 or 0
as the audit reads danger or safety), or 'protected' (the investigator
keeps a floor p_min on P(inspect)).

Baselines: 'bayes' (no authority state: kappa = 0), 'bayes_cost' (the same
with a higher inspection cost), and 'habit' (the authority state replaced by
two habit traces of matched memory eta: H_p, the running frequency of
protecting, in the posture term, and H_s, the running frequency of
sheltering, in the inspection term).

All conditions share common random numbers: the uniforms that decide
inspections, observations, audits and postures are drawn once per seed and
reused, so differences between conditions are paired.
"""
from __future__ import annotations

from dataclasses import dataclass, replace, field
from typing import Dict, Optional

import numpy as np


@dataclass(frozen=True)
class Params:
    T1: int = 150          # danger (training)
    T2: int = 400          # safe
    T3: int = 100          # danger again
    h: float = 0.02        # switching hazard the agent assumes
    acc: float = 0.9
    L: float = 5.0
    ell: float = 1.0
    c: float = 0.05
    beta_i: float = 60.0
    beta_p: float = 3.0
    kappa: float = 1.5     # sentry strength; kappa_a = kappa, kappa_e = 0.2 * kappa
    kappa_e_ratio: float = 0.2
    eta: float = 0.02
    g0: float = 0.2
    b0: float = 0.5
    q: float = 0.2         # audit rate
    p_min: float = 0.2     # protected investigator's floor

    @property
    def T(self) -> int:
        return self.T1 + self.T2 + self.T3

    @property
    def kappa_a(self) -> float:
        return self.kappa

    @property
    def kappa_e(self) -> float:
        return self.kappa * self.kappa_e_ratio


@dataclass(frozen=True)
class Condition:
    model: str = "governance"        # governance | habit | bayes
    feedback: str = "success"        # success | independent | fixed
    restrict: bool = True            # sentry can block inspection
    correction: str = "ordinary"     # ordinary | audit | protected
    c_override: Optional[float] = None
    intervention: Optional[str] = None   # belief | authority | evidence | reinforcement
    t_int: Optional[int] = None          # step of the intervention (default T1 + 50)


def world(p: Params) -> np.ndarray:
    return np.concatenate([np.ones(p.T1, int), np.zeros(p.T2, int), np.ones(p.T3, int)])


def draws(p: Params, n: int, seed: int = 0) -> Dict[str, np.ndarray]:
    rng = np.random.default_rng(seed)
    return {k: rng.random((n, p.T)) for k in ("insp", "obs", "audit", "aobs", "post")}


def sigma(z):
    return 1.0 / (1.0 + np.exp(-np.clip(z, -50, 50)))


def predict(b, h):
    return b * (1 - h) + (1 - b) * h


def posterior(b, o, acc):
    """Belief in danger after observing o (1 = reads danger)."""
    like_d = np.where(o == 1, acc, 1 - acc)
    like_s = np.where(o == 1, 1 - acc, acc)
    num = b * like_d
    return num / (num + (1 - b) * like_s)


def posture_loss(b, L, ell):
    return np.minimum(b * L, ell)


def voi(b, p: Params):
    """Myopic value of one inspection for the posture decision."""
    po1 = b * p.acc + (1 - b) * (1 - p.acc)          # P(reads danger)
    b1 = posterior(b, np.ones_like(b, dtype=int), p.acc)
    b0 = posterior(b, np.zeros_like(b, dtype=int), p.acc)
    after = po1 * posture_loss(b1, p.L, p.ell) + (1 - po1) * posture_loss(b0, p.L, p.ell)
    return posture_loss(b, p.L, p.ell) - after


def simulate(p: Params, cond: Condition, U: Dict[str, np.ndarray],
             x: Optional[np.ndarray] = None) -> Dict[str, np.ndarray]:
    n, T = U["insp"].shape
    x = world(p) if x is None else x
    c = p.c if cond.c_override is None else cond.c_override
    gov = cond.model == "governance"
    habit = cond.model == "habit"
    k_a = p.kappa_a if (gov or habit) else 0.0
    k_e = p.kappa_e if ((gov or habit) and cond.restrict) else 0.0
    t_int = cond.t_int if cond.t_int is not None else p.T1 + 50

    b = np.full(n, p.b0)
    e = np.full(n, p.b0)          # evaluator's belief
    g = np.full(n, p.g0)          # authority (governance) / H_p (habit)
    Hs = np.full(n, p.g0)         # habit of sheltering (habit model only)
    feedback = cond.feedback
    restrict_on = k_e > 0
    floor = p.p_min if cond.correction == "protected" else 0.0

    rec = {k: np.zeros((n, T)) for k in ("b", "g", "pp", "pi", "insp", "prot", "harm", "e")}
    for t in range(T):
        if t == t_int and cond.intervention:
            if cond.intervention == "belief":
                b = np.full(n, 0.01)   # the agent's appraisal only
            elif cond.intervention == "authority":
                g = np.full(n, 0.05)
                Hs = np.full(n, 0.05)
            elif cond.intervention == "evidence":
                restrict_on = False
                floor = max(floor, p.p_min)
            elif cond.intervention == "reinforcement":
                feedback = "independent"
        b = predict(b, p.h)
        e = predict(e, p.h)
        block = (Hs if habit else g) * (k_e if restrict_on else 0.0)
        pi = sigma(p.beta_i * (voi(b, p) - c - block))
        pi = np.maximum(pi, floor)
        insp = U["insp"][:, t] < pi
        o = np.where(U["obs"][:, t] < p.acc, x[t], 1 - x[t])
        b = np.where(insp, posterior(b, o, p.acc), b)
        e = np.where(insp, posterior(e, o, p.acc), e)
        audited = np.zeros(n, bool)
        if cond.correction == "audit":
            audited = U["audit"][:, t] < p.q
            a = np.where(U["aobs"][:, t] < p.acc, x[t], 1 - x[t])
            e = np.where(audited, posterior(e, a, p.acc), e)
        pp = sigma(p.beta_p * (b * p.L - p.ell + k_a * g))
        prot = U["post"][:, t] < pp
        harm = (~prot) & (x[t] == 1)
        if gov:
            if feedback == "success":
                F = (prot | harm).astype(float)
                if cond.correction == "audit":
                    F = np.where(audited, a.astype(float), F)
            elif feedback == "independent":
                F = e.copy()
            else:
                F = g.copy()
            g = (1 - p.eta) * g + p.eta * F
        elif habit:
            g = (1 - p.eta) * g + p.eta * prot
            Hs = (1 - p.eta) * Hs + p.eta * (~insp)
        for k, v in (("b", b), ("g", g), ("pp", pp), ("pi", pi), ("insp", insp),
                     ("prot", prot), ("harm", harm), ("e", e)):
            rec[k][:, t] = v
    rec["loss"] = rec["prot"] * p.ell + rec["harm"] * p.L + rec["insp"] * c
    return rec


def first_true(mask: np.ndarray, censor: int) -> np.ndarray:
    any_ = mask.any(axis=1)
    idx = mask.argmax(axis=1)
    return np.where(any_, idx, censor)


def measures(p: Params, rec: Dict[str, np.ndarray], window: int = 20, t_from: Optional[int] = None) -> Dict[str, np.ndarray]:
    """Per-seed measures over the safe phase (from t_from, default the switch)."""
    s = p.T1 if t_from is None else t_from
    e_ = p.T1 + p.T2
    n = rec["b"].shape[0]
    span = e_ - s
    b = rec["b"][:, s:e_]
    pp = rec["pp"][:, s:e_]
    # forward window mean of P(protect)
    csum = np.concatenate([np.zeros((n, 1)), np.cumsum(pp, axis=1)], axis=1)
    m = span - window + 1
    fwd = (csum[:, window:window + m] - csum[:, :m]) / window
    exit_ = first_true(fwd < 0.5, span)
    recog = first_true(b < p.ell / p.L, span)
    out = {
        "recognition": recog,
        "exit": exit_,
        "recognized": recog < span,
        "exited": exit_ < span,
        "persistence": np.where((recog < span), exit_ - recog, np.nan),
        "needless_cost": rec["prot"][:, s:e_].sum(axis=1) * p.ell,
        "inspections": rec["insp"][:, s:e_].sum(axis=1),
        "g_end": rec["g"][:, e_ - 1],
        "b_end": rec["b"][:, e_ - 1],
        "harm3": rec["harm"][:, e_:].mean(axis=1),
        "prot3": rec["prot"][:, e_:].mean(axis=1),
        "loss": rec["loss"].sum(axis=1),
        "brier": ((rec["b"] - world(p)[None, :]) ** 2).mean(axis=1),
        "info_sampled": rec["insp"].mean(axis=1),
    }
    # corrected belief with protection still on at the end of the safe phase
    out["outlasts"] = (rec["b"][:, e_ - window:e_].mean(axis=1) < p.ell / p.L) & (pp[:, -window:].mean(axis=1) >= 0.5)
    return out


def summarize(meas: Dict[str, np.ndarray]) -> Dict[str, float]:
    d = {}
    d["recognized"] = float(meas["recognized"].mean())
    d["exited"] = float(meas["exited"].mean())
    d["median_recognition"] = float(np.median(meas["recognition"]))
    d["median_exit"] = float(np.median(meas["exit"]))
    pers = meas["persistence"][~np.isnan(meas["persistence"])]
    d["median_persistence"] = float(np.median(pers)) if pers.size else float("nan")
    d["outlasts"] = float(meas["outlasts"].mean())
    for k in ("needless_cost", "inspections", "g_end", "b_end", "harm3", "prot3", "loss", "brier", "info_sampled"):
        d[k] = float(meas[k].mean())
    return d
