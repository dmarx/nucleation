"""The top rung of LEAD-177's ladder: a sensor network that revises its
correspondences (QUESTION-285, item 3; Robinson's sensor sheaf, LIT-1658,
with its restriction maps made revisable).

A target moves in the plane, z_t.  Four sensors report o_i = A_i z + b_i +
noise.  The apparatus holds correspondences (Ahat_i, bhat_i), fuses by least
squares (the nearest global section) and reports its consistency radius,
the largest residual.  The true maps drift: every bias takes a slow random
walk, and at t_jump sensor 2's bias jumps and its gain rotates.  Nobody told
the apparatus either would happen.

Arms, by what the revision G may not rewrite:

  fixed       no revision (Robinson's networks);
  self        G revises every map to reduce the residuals among the sensors'
              own reports (disagreement only; nothing outside);
  anchored    G revises the maps only on calibration events: the world, not
              the apparatus, places a beacon at z*, and z* arrives through a
              channel G cannot revise or refuse;
  writable    the same events, but the beacon is one more sensor whose map G
              revises by disagreement like the others;
  admitted    the protected channel, but the apparatus admits an event only
              when it agrees with its current maps (residual below a
              threshold): the scoring passes through the interpretation.

Two options, off by default, for the anchored arm (added 2026-11-23):

  beacon_bias  the protected channel reports the beacon at z* + delta, a
               fixed miscalibration, which G can neither rewrite nor refuse;
  survey_every every that many steps a survey, a rarer protected event,
               places a point and reads it through the beacon channel too,
               and a separate, slower revision (eta_survey) estimates the
               beacon's bias from it, which is subtracted from later beacon
               reports. It is an anchor for the anchor.

Measured on the target's true positions, which the apparatus never sees:
fusion error |zhat - z|, and its own consistency radius.
"""
from __future__ import annotations

import math

import numpy as np

ARMS = ["fixed", "self", "anchored", "writable", "admitted"]


def rot(theta):
    c, s = math.cos(theta), math.sin(theta)
    return np.array([[c, -s], [s, c]])


def fuse(A, b, o):
    """Least-squares state from reports o_i under maps (A_i, b_i)."""
    M = np.vstack(A)
    y = np.concatenate([oi - bi for oi, bi in zip(o, b)])
    z, *_ = np.linalg.lstsq(M, y, rcond=None)
    return z


def residuals(A, b, o, z):
    return [oi - Ai @ z - bi for Ai, bi, oi in zip(A, b, o)]


def run(arm: str, seed: int, T: int = 3000, t_jump: int = 500, n: int = 4,
        noise: float = 0.05, drift: float = 0.004, jump=(1.0, -0.6),
        jump_rot: float = math.radians(20), K: int = 10, eta: float = 0.02,
        eta_anchor: float = 0.2, admit_thr: float = 0.3,
        beacon_bias=(0.0, 0.0), survey_every: int = 0,
        eta_survey: float = 0.05) -> dict:
    rng = np.random.default_rng(seed)
    A = [rot(rng.uniform(-0.3, 0.3)) * rng.uniform(0.8, 1.2) for _ in range(n)]
    b = [rng.normal(0, 0.5, 2) for _ in range(n)]
    Ah = [a.copy() for a in A]
    bh = [v.copy() for v in b]
    AB, bB = np.eye(2), np.zeros(2)          # the beacon channel's map (writable arm)
    delta = np.asarray(beacon_bias, float)
    bias_hat = np.zeros(2)                   # the survey's estimate of delta
    z = np.zeros(2)
    err, rad, admitted, offered = [], [], 0, 0
    for t in range(T):
        # the world
        z = np.clip(z + rng.normal(0, 0.1, 2), -3, 3)
        for i in range(n):
            b[i] = b[i] + rng.normal(0, drift, 2)
        if t == t_jump:
            b[2] = b[2] + np.array(jump)
            A[2] = rot(jump_rot) @ A[2]
        o = [A[i] @ z + b[i] + rng.normal(0, noise, 2) for i in range(n)]
        zh = fuse(Ah, bh, o)
        r = residuals(Ah, bh, o, zh)
        err.append(float(np.linalg.norm(zh - z)))
        rad.append(max(float(np.linalg.norm(v)) for v in r))
        # revision
        if arm == "self":
            for i in range(n):
                Ah[i] = Ah[i] + eta * np.outer(r[i], zh)
                bh[i] = bh[i] + eta * r[i]
        if survey_every and arm == "anchored" and t % survey_every == 0 and t:
            # the survey: a separate protected channel, used only to estimate
            # the beacon's miscalibration. Its own generator keeps the main
            # stream unchanged.
            srng = np.random.default_rng([seed, 99, t])
            zq = srng.uniform(-3, 3, 2)
            read = zq + delta + srng.normal(0, noise, 2)  # the beacon channel's reading
            bias_hat = bias_hat + eta_survey * ((read - zq) - bias_hat)
        if arm in ("anchored", "writable", "admitted") and t % K == 0 and arm != "self":
            offered += 1
            zs = rng.uniform(-3, 3, 2)                   # placed by the world
            ob = [A[i] @ zs + b[i] + rng.normal(0, noise, 2) for i in range(n)]
            if arm == "writable":
                # the beacon is one more sensor whose map is revised by disagreement
                Aall, ball = Ah + [AB], bh + [bB]
                oall = ob + [zs]
                zc = fuse(Aall, ball, oall)
                rc = residuals(Aall, ball, oall, zc)
                for i in range(n):
                    Ah[i] = Ah[i] + eta_anchor * np.outer(rc[i], zc) / (1 + zc @ zc)
                    bh[i] = bh[i] + eta_anchor * rc[i] / (1 + zc @ zc)
                AB = AB + eta_anchor * np.outer(rc[n], zc) / (1 + zc @ zc)
                bB = bB + eta_anchor * rc[n] / (1 + zc @ zc)
                admitted += 1
            else:
                zr = zs + delta - bias_hat if arm == "anchored" else zs   # what the channel reports
                rs = residuals(Ah, bh, ob, zr)
                if arm == "admitted" and max(np.linalg.norm(v) for v in rs) > admit_thr:
                    continue
                admitted += 1
                for i in range(n):
                    # normalized LMS against the protected position z*
                    g = eta_anchor / (1 + zr @ zr)
                    Ah[i] = Ah[i] + g * np.outer(rs[i], zr)
                    bh[i] = bh[i] + g * rs[i]
    err, rad = np.array(err), np.array(rad)
    w = slice(T - 1000, T)
    pre = slice(t_jump - 200, t_jump)
    return dict(arm=arm, seed=seed, err_pre=float(err[pre].mean()), rad_pre=float(rad[pre].mean()),
                err_late=float(err[w].mean()), rad_late=float(rad[w].mean()),
                admitted=admitted, offered=offered)
