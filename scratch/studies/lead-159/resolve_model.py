"""LEAD-159: CASE-188's agents with their slow influence structure ablated
under matched information.

A two-action task. Action B is the long-term commitment; action A is the
alternative. Every trial each action yields two signals:

  immediate payoff  i_k ~ N(mu_i[k], sigma^2)   the locally dominant evaluation
  long-run payoff   l_k ~ N(mu_l[k], sigma^2)   what the experimenter scores

Under ordinary conditions B is better in the long run by DELTA and A is
slightly more tempting immediately by TAU0. At the event onset (the
commitment's age) one of three environments applies, set by the experimenter
and not by any agent (CASE-188's first factor):

  defeater    the long-run advantage flips: mu_l[B] -= DELTA, mu_l[A] += DELTA
  irrelevant  the immediate temptation grows by the same amount:
              mu_i[A] += DELTA, mu_i[B] -= DELTA (long-run unchanged)
  neither     nothing changes

Both events are step changes of the same size (2*DELTA in the difference of
the two actions' means) on channels of the same noise, at the same time, and
they persist to the end of the run: matched size, salience and duration.

Every agent has the same state variables (capacity): per-action estimates of
the immediate payoff I[k] (fast, rate ALPHA_F) and of the long-run payoff
L[k] (the commitment's evaluator, rate ALPHA_C times an admission weight a),
a precedence lam in [0, 1], an admission weight a in [0, 1], and two error
traces e_c, e_q. It chooses B with probability

  sigmoid(BETA * (lam * c + (1 - lam) * q)),  c = L[B]-L[A], q = I[B]-I[A].

The slow influence structure is (lam, a) and how they are maintained:

  R  corrigible resolve: precedence goes to the evaluation that predicts the
     scored outcome, lam = sigmoid(KAPPA * (e_q - e_c)), with e_c, e_q slow
     (rate ETA) traces of the squared error of c and of q against the
     observed long-run difference; a = 1 always.
  E  entrenchment: lam and a are driven by enforcement success, a trial on
     which the choice agreed with the commitment: lam grows toward LAM_MAX
     at rate ETA, a decays at rate ETA_E.
  P  imposed protection: lam = LAM_IMPOSED fixed from outside, a = 1; no
     slow dynamics of its own.
  I  inertia: lam = 0.5 fixed, a = 1, both estimators slow (ALPHA_SLOW),
     inverse temperature BETA_I so that its ordinary choices match.

Conditions, all applied at the event onset, with the observation stream and
the choice noise identical to the intact run (matched information) and the
same state variables (matched capacity):

  intact
  lesion     slow structure reset to its initial value (lam=0.5, a=1) and
             frozen there
  perturb    reset as in lesion, then left free to evolve (maintenance test)
  yoked      lam and a replaced by the trajectory the same agent type
             produced in another run (other seeds, environment neither):
             matched values, causal coupling to this run cut
  timescale  every rate slower than ALPHA_F raised to ALPHA_F

Visibility (CASE-188's third factor), applied to the long-run channel:

  full     both long-run signals observed every trial
  partial  observed on a random P_OBS of trials, independent of choice
  routed   observed every trial, but an observation that disconfirms the
           current commitment is admitted to the commitment's evaluator
           with weight (1 - lam)
"""
from __future__ import annotations

import numpy as np

# ---- parameters (see README for why each value) -------------------------
DELTA = 0.5        # long-run advantage of B under ordinary conditions
TAU0 = 0.2         # immediate temptation of A under ordinary conditions
SIGMA = 1.0        # noise sd of every signal
BETA = 8.0         # choice inverse temperature
ALPHA_F = 0.05     # fast estimator rate
ALPHA_C = 0.01     # commitment evaluator rate
ALPHA_SLOW = 0.001  # inertia agent's rate for both estimators
BETA_I = 21.0      # inertia agent's inverse temperature, set so that it
                   # decides like the others under ordinary conditions
ETA = 0.002        # slow-structure rate
ETA_E = 0.002      # entrenchment: decay rate of the admission weight
KAPPA = 5.0        # R: sensitivity of precedence to the error difference
LAM0 = 0.5         # initial precedence
LAM_MAX = 0.95     # E: ceiling of precedence
LAM_IMPOSED = 0.9  # P: imposed precedence
P_OBS = 0.25       # partial visibility: share of trials with long-run signal
HORIZON = 1500     # trials after the onset
WINDOW = 200       # final window for the revision endpoint
RUNWIN = 50        # running window for time to revision
CHECKPOINTS = (250, 500, HORIZON)  # horizons at which revision is read

AGENTS = ("R", "E", "P", "I")
CONDITIONS = ("intact", "lesion", "perturb", "yoked", "timescale")
ENVS = ("defeater", "irrelevant", "neither")
VISIBILITIES = ("full", "partial", "routed")

_ENV_CODE = {"defeater": 1, "irrelevant": 2, "neither": 3}
_VIS_CODE = {"full": 1, "partial": 2, "routed": 3}


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))


def make_stream(env: str, age: int, vis: str, n: int, seed: int):
    """The observation stream and choice noise, a function of the
    environment, age, visibility and seed only, never of agent or condition.
    Returns a dict of arrays with leading dimension T = age + HORIZON."""
    T = age + HORIZON
    rng = np.random.default_rng([seed, _ENV_CODE[env], age, _VIS_CODE[vis]])
    mu_i = np.zeros((T, 2))  # columns: A, B
    mu_l = np.zeros((T, 2))
    mu_i[:, 0] = TAU0 / 2
    mu_i[:, 1] = -TAU0 / 2
    mu_l[:, 0] = -DELTA / 2
    mu_l[:, 1] = DELTA / 2
    if env == "defeater":
        mu_l[age:, 0] += DELTA
        mu_l[age:, 1] -= DELTA
    elif env == "irrelevant":
        mu_i[age:, 0] += DELTA
        mu_i[age:, 1] -= DELTA
    noise = rng.standard_normal((T, n, 4)) * SIGMA
    imm = mu_i[:, None, :] + noise[:, :, 0:2]
    lng = mu_l[:, None, :] + noise[:, :, 2:4]
    if vis == "partial":
        obs = rng.random((T, n)) < P_OBS
    else:
        obs = np.ones((T, n), dtype=bool)
    u = rng.random((T, n))
    return {"imm": imm, "lng": lng, "obs": obs, "u": u, "mu_l": mu_l,
            "T": T, "age": age, "vis": vis}


def simulate(agent: str, cond: str, stream: dict, yoke=None,
             record_slow: bool = False):
    """Run one agent under one condition on a stream; vectorized over runs.

    Returns choices (T, n) with 1 = B, and per-trial lam, a and c."""
    if agent not in AGENTS:
        raise ValueError(agent)
    if cond not in CONDITIONS:
        raise ValueError(cond)
    imm, lng, obs, u = stream["imm"], stream["lng"], stream["obs"], stream["u"]
    T, n = u.shape
    age, vis = stream["age"], stream["vis"]

    # every agent starts with the commitment installed: it holds the
    # ordinary-condition values as its initial estimates
    I = np.tile([TAU0 / 2, -TAU0 / 2], (n, 1)).astype(float)
    L = np.tile([-DELTA / 2, DELTA / 2], (n, 1)).astype(float)
    a = np.ones(n)
    e_c = np.ones(n)
    e_q = np.ones(n)
    if agent == "P":
        lam = np.full(n, LAM_IMPOSED)
    else:
        lam = np.full(n, LAM0)
    if agent == "I":
        af, ac = ALPHA_SLOW, ALPHA_SLOW
    else:
        af, ac = ALPHA_F, ALPHA_C
    eta, eta_e = ETA, ETA_E
    beta = BETA_I if agent == "I" else BETA
    frozen = False

    choices = np.zeros((T, n), dtype=np.int8)
    lam_tr = np.zeros((T, n)) if record_slow else None
    a_tr = np.zeros((T, n)) if record_slow else None
    c_tr = np.zeros((T, n))

    for t in range(T):
        if t == age and cond != "intact":
            if cond in ("lesion", "perturb"):
                lam = np.full(n, LAM0)
                a = np.ones(n)
                e_c = np.ones(n)
                e_q = np.ones(n)
                frozen = cond == "lesion"
            elif cond == "timescale":
                af = max(af, ALPHA_F)
                ac = max(ac, ALPHA_F)
                eta = max(eta, ALPHA_F)
                eta_e = max(eta_e, ALPHA_F)
        if cond == "yoked" and t >= age:
            lam = yoke["lam"][t].copy()
            a = yoke["a"][t].copy()

        c = L[:, 1] - L[:, 0]
        q = I[:, 1] - I[:, 0]
        pref = lam * c + (1 - lam) * q
        pB = sigmoid(beta * pref)
        chooseB = u[t] < pB
        choices[t] = chooseB
        c_tr[t] = c
        if record_slow:
            lam_tr[t] = lam
            a_tr[t] = a

        # fast evaluation: immediate payoffs, always observed
        I += af * (imm[t] - I)

        # commitment's evaluator: long-run payoffs, admitted with weight a
        o = obs[t]
        resid = lng[t] - L
        w = np.ones((n, 2))
        if vis == "routed":
            # the commitment favours B when c > 0: a residual that raises A
            # or lowers B disconfirms it, and conversely
            sgn = np.where(c >= 0, 1.0, -1.0)
            discon_A = resid[:, 0] * sgn > 0
            discon_B = resid[:, 1] * sgn < 0
            w[:, 0] = np.where(discon_A, 1 - lam, 1.0)
            w[:, 1] = np.where(discon_B, 1 - lam, 1.0)
        L += (ac * a * o)[:, None] * w * resid

        # slow influence structure
        if frozen or agent in ("P", "I"):
            continue
        if cond == "yoked" and t >= age:
            continue
        if agent == "R":
            y = lng[t, :, 1] - lng[t, :, 0]
            e_c = np.where(o, e_c + eta * ((y - c) ** 2 - e_c), e_c)
            e_q = np.where(o, e_q + eta * ((y - q) ** 2 - e_q), e_q)
            lam = sigmoid(KAPPA * (e_q - e_c))
        elif agent == "E":
            agree = chooseB == (c >= 0)
            lam = lam + eta * (LAM_MAX - lam) * agree
            a = a - eta_e * a * agree
    return {"choices": choices, "lam": lam_tr, "a": a_tr, "c": c_tr}


def endpoints(choices, c_tr, stream, lam_at_onset=None):
    """Preregistered endpoints of one cell."""
    age = stream["age"]
    T = stream["T"]
    post = choices[age:].astype(float)           # 1 = B
    shareA_final = 1 - post[-WINDOW:].mean(axis=0)
    revised = shareA_final > 0.5
    pre = choices[max(0, age - WINDOW):age].astype(float)
    # time to revision: first trial after onset at which the running share
    # of A over RUNWIN trials exceeds one half
    A = 1 - post
    cs = np.cumsum(A, axis=0)
    run = (cs[RUNWIN - 1:] - np.vstack([np.zeros((1, A.shape[1])),
                                        cs[:-RUNWIN]])) / RUNWIN
    hit = run > 0.5
    first = np.where(hit.any(axis=0), hit.argmax(axis=0) + RUNWIN, -1)
    # long-run regret per trial after onset, against the best action
    mu_l = stream["mu_l"][age:]
    best = mu_l.max(axis=1)
    got = np.where(post == 1, mu_l[:, [1]], mu_l[:, [0]])
    regret = (best[:, None] - got).mean(axis=0)
    # revision checked at three horizons after the onset
    checks = {}
    for h in CHECKPOINTS:
        sh = 1 - post[h - WINDOW:h].mean(axis=0)
        checks[f"p_revise_at_{h}"] = float((sh > 0.5).mean())
    c_on = c_tr[age]
    c_end = c_tr[-1]
    n = choices.shape[1]
    p = revised.mean()
    out = {
        "n": int(n),
        "p_revise": float(p),
        "se": float(np.sqrt(p * (1 - p) / n)),
        "shareA_final": float(shareA_final.mean()),
        "pre_shareB": float(pre.mean()) if pre.size else None,
        "t_revise_median": (float(np.median(first[first >= 0]))
                            if (first >= 0).any() else None),
        "p_ever": float((first >= 0).mean()),
        "regret_per_trial": float(regret.mean()),
        "c_onset": float(c_on.mean()),
        "c_end": float(c_end.mean()),
        # share of the defeater's shift in c (from +DELTA to -DELTA) that
        # reached the commitment's evaluator by the end
        "absorbed": float(((c_on - c_end) / (2 * DELTA)).mean()),
    }
    out.update(checks)
    return out
