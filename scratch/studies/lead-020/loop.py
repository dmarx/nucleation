"""A single-mind judgement-observation loop with action held fixed (LEAD-020).

The loop is CASE-099's coupled meaning-authority model, made nonlinear and
bounded, and placed inside one mind:

- m = tanh(u) is the interpretation (lean toward hypothesis A, in (-1, 1)).
- a = tanh(v) is the relative authority of the A-favouring sub-process over
  the B-favouring one.
- beta arrow (authority shapes interpretation): a pushes u directly, and a
  sets attention, attenuating readings that favour the other hypothesis
  (the loop selecting its own evidence, NOTE-766 / THEORY-285, without action).
- gamma arrow (interpretation shapes conferral): how authority is scored.

The world is a hidden state h in {+1, -1} that switches every `block` steps.
Action is held fixed: nothing the loop does changes h or when any input
arrives. Lock-in is failure to follow a switch of h.

QUESTION-121's five candidates are switchable, each implemented with the
"Against" the question gives it:

1. unselected input (`sense`): a sensory channel arriving every step, read
   through the interpretation (kappa_1) and attenuable by attention, plus
   exogenous capture (`capture`): a raw input surprising enough against the
   prediction is attended at full weight whatever the authority says.
2. the body (`body`): an interoceptive channel tied to h, arriving every
   step, read through the interpretation more strongly (kappa_2, since
   interoception is predicted) and attenuable; no capture.
3. commitment before evidence (`commit`): the sub-processes commit
   predictions p_A = s + kbar*m, p_B = -s + kbar*m before the evidence and are
   scored by squared error against the evidence as attended and read
   (CASE-106). Without it, authority is scored against the dominant
   interpretation (CASE-092's Regime A), or, in the variant
   `no_commit_mode="posthoc"`, predictions revised after the evidence give no
   score at all (CLAIM-340).
4. processing signals (`fluency`): a content-free disfluency, the running
   mean of the unsigned prediction error on attended inputs; disfluency above
   its expected level shrinks both u and v (lowers confidence and authority).
   Against: computed only from what is attended, so attenuation hides it.
5. other people (`others`): testimony about h arriving unasked at random
   steps, read through the interpretation (kappa_5), weighted by a trust that
   is learned from agreement with the interpretation (whom to believe is
   selected).
"""

from __future__ import annotations

from dataclasses import dataclass, field, replace

import numpy as np

CANDIDATES = ("sense", "capture", "body", "commit", "fluency", "others")


@dataclass(frozen=True)
class Params:
    # core loop (CASE-099 names)
    alpha: float = 0.9      # persistence of interpretation drive u
    beta: float = 0.05      # direct push of authority on interpretation
    lam: float = 0.15       # gain of attended readings on u
    delta: float = 0.9      # persistence of authority drive v
    eta: float = 0.1        # rate at which scores move authority
    gamma_a: float = 1.0    # Regime A: score difference per unit of m
    zeta: float = 1.0       # attention attenuation by authority
    # channels (mu = 1 for all, so readings are commensurable)
    sigma1: float = 1.0
    kappa1: float = 0.2
    sigma2: float = 1.5
    kappa2: float = 0.8
    sigma5: float = 0.5
    kappa5: float = 0.3
    q5: float = 0.05        # chance per step that testimony arrives
    eta_tau: float = 0.05   # trust learning rate
    tau0: float = 0.5
    # candidate 1b: exogenous capture
    theta: float = 2.5      # surprise threshold on |x1 - m|
    # candidate 3: commitment
    s: float = 0.5
    kbar: float = 0.5
    # candidate 4: processing signals
    phi: float = 0.5
    d0: float = 1.0         # expected unsigned error with mu = 1, sigma = 1
    rho_d: float = 0.1      # EMA rate of disfluency
    # bounds
    umax: float = 6.0
    vmax: float = 6.0


@dataclass
class Config:
    sense: bool = True
    capture: bool = True
    body: bool = True
    commit: bool = True
    fluency: bool = True
    others: bool = True
    no_commit_mode: str = "regimeA"   # or "posthoc"

    def without(self, name: str) -> "Config":
        c = replace(self)
        setattr(c, name, False)
        if name == "sense":       # capture is part of candidate 1
            c.capture = False
        return c

    def label(self) -> str:
        on = [n for n in CANDIDATES if getattr(self, n)]
        return "+".join(on) if on else "none"


def attention(a: float, r: float, zeta: float) -> float:
    """Weight on a reading r given authority a: readings that favour the
    dominant sub-process are amplified, the others attenuated, in [0, 2]."""
    return float(np.clip(1.0 + zeta * a * np.sign(r), 0.0, 2.0))


def commitment_score(m: float, rbar: float, s: float, kbar: float) -> float:
    """CASE-106's score difference (p_B - r)^2 - (p_A - r)^2 for committed
    predictions p_A = s + kbar*m, p_B = -s + kbar*m; equals 4 s (r - kbar m)."""
    pa, pb = s + kbar * m, -s + kbar * m
    return (pb - rbar) ** 2 - (pa - rbar) ** 2


def simulate(cfg: Config, p: Params, steps: int, block: int, seed: int,
             record: bool = False):
    rng = np.random.default_rng(seed)
    u = v = 0.0
    tau = p.tau0
    dis = p.d0
    h_seq = np.where((np.arange(steps) // block) % 2 == 0, 1.0, -1.0)
    ms = np.empty(steps)
    as_ = np.empty(steps)
    n_capture = 0
    for t in range(steps):
        h = h_seq[t]
        m, a = np.tanh(u), np.tanh(v)
        readings, weights, raw_err = [], [], []
        if cfg.sense:
            x1 = h + p.sigma1 * rng.standard_normal()
            r1 = x1 + p.kappa1 * m
            w1 = attention(a, r1, p.zeta)
            if cfg.capture and abs(x1 - m) > p.theta:
                w1 = max(w1, 1.0)
                n_capture += 1
            readings.append(r1); weights.append(w1); raw_err.append(abs(x1 - m))
        if cfg.body:
            x2 = h + p.sigma2 * rng.standard_normal()
            r2 = x2 + p.kappa2 * m
            w2 = attention(a, r2, p.zeta)
            readings.append(r2); weights.append(w2); raw_err.append(abs(x2 - m))
        if cfg.others and rng.random() < p.q5:
            x5 = h + p.sigma5 * rng.standard_normal()
            r5 = x5 + p.kappa5 * m
            readings.append(r5); weights.append(tau); raw_err.append(abs(x5 - m))
            agree = 1.0 if np.sign(r5) == np.sign(m) else 0.0
            tau += p.eta_tau * (agree - tau)
        readings = np.asarray(readings); weights = np.asarray(weights)
        drive = float(np.dot(weights, readings)) if readings.size else 0.0
        u_new = p.alpha * u + p.beta * a + p.lam * drive
        # authority scoring
        if cfg.commit:
            wsum = weights.sum() if readings.size else 0.0
            score = (commitment_score(m, float(np.dot(weights, readings) / wsum),
                                      p.s, p.kbar) if wsum > 0 else 0.0)
        elif cfg.no_commit_mode == "regimeA":
            score = p.gamma_a * np.tanh(u_new)
        else:   # "posthoc": predictions revised after the evidence: no score
            score = 0.0
        v_new = p.delta * v + p.eta * score
        # processing signals
        if cfg.fluency:
            wsum = weights.sum() if readings.size else 0.0
            if wsum > 0:
                e = float(np.dot(weights, raw_err) / wsum)
                dis += p.rho_d * (e - dis)
            excess = min(max(dis - p.d0, 0.0) * p.phi, 1.0)
            u_new *= 1.0 - excess
            v_new *= 1.0 - excess
        u = float(np.clip(u_new, -p.umax, p.umax))
        v = float(np.clip(v_new, -p.vmax, p.vmax))
        ms[t], as_[t] = np.tanh(u), np.tanh(v)
    out = {"lockin": lockin_rate(ms, h_seq, block),
           "first_block_tracked": tracked(ms[:block], 1.0),
           "captures": n_capture}
    if record:
        out.update(m=ms, a=as_, h=h_seq)
    return out


def tracked(ms_block: np.ndarray, h: float, run: int = 20) -> bool:
    """True if sign(m) matches h for `run` consecutive steps in the block."""
    ok = np.sign(ms_block) == h
    best = cur = 0
    for x in ok:
        cur = cur + 1 if x else 0
        best = max(best, cur)
    return best >= run


def lockin_rate(ms: np.ndarray, h_seq: np.ndarray, block: int) -> float:
    """Fraction of switches that the interpretation fails to follow within the
    block, counting only switches away from the interpretation held at the
    switch (a loop stuck on one side scores 1.0, not 0.5). Returns nan if no
    switch went against the held interpretation."""
    nblocks = len(ms) // block
    if nblocks < 2:
        raise ValueError("need at least two blocks")
    fails = counted = 0
    for b in range(1, nblocks):
        start = b * block
        h_new = h_seq[start]
        if np.sign(ms[start - 1]) == h_new:
            continue
        counted += 1
        fails += not tracked(ms[start:start + block], h_new)
    return fails / counted if counted else float("nan")
