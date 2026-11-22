"""LEAD-093: a nucleus that, once formed, produces or repairs the constraint of
its own formation, and when the loop closes.

Variables (dimensionless, mass-action, deterministic unless noted):

  m   material (monomer, fuel), supplied from outside at rate J, washed out at
      rate delta. Material is consumed by formation and by production.
  T   the formation constraint: a teacher / template / scaffold that catalyses
      the formation of nuclei and is not consumed by it. It turns over (is
      damaged and lost) at rate kT. Outside supply of T at rate sigma.
  N   good nuclei: formed spontaneously (slow, a0 m^2) or templated by T
      (a1 m T^2/(K^2 + T^2), cooperative, so a founding is needed). A nucleus
      turns over at rate d. Once formed it produces T from material at rate
      beta m N: the student becomes a teacher. That is the loop.
  B   defective nuclei: formed with probability eps, structurally the same
      (same turnover, same material cost), but they produce no T. A faithful
      student and a poor teacher.

Arm "produce" (the main arm):
  m' = J - delta m - F - beta m N
  T' = sigma - kT T + beta m N
  N' = (1 - eps) F - d N
  B' = eps F - d B,        F = a0 m^2 + a1 m T^2 / (K^2 + T^2)

Arm "repair": nuclei repair damaged teachers instead of making new ones.
  T is damaged at rate kT into D; D is lost at rate lam; a nucleus repairs D
  back into T at rate rho N D, at a material cost rcost per repair (0 by
  default: repair is cheaper than making anew; 1 as a sensitivity check).
  m' = J - delta m - F - rcost rho N D
  T' = sigma - kT T + rho N D
  D' = kT T - rho N D - lam D
  N' = (1 - eps) F - d N ;  B' = eps F - d B

The loop is said to close at a parameter point when the system with sigma = 0
has a stable maintained state (N > 0 well above the spontaneous background)
and, at a time t, when the state at t lies in that state's basin, so that the
outside teacher can be withdrawn at t for good and the nucleus persists.
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

BASE = dict(J=1.0, delta=0.1, a0=1e-6, a1=0.1, K=2.0, d=0.1, beta=0.02,
            kT=0.1, sigma=0.0, eps=0.0, rho=0.0, lam=0.0, rcost=0.0,
            arm="produce")


def params(**kw):
    p = dict(BASE)
    p.update(kw)
    return p


def rhs(t, y, p, sigma_of_t=None):
    m, T, N, B, D = y
    sig = p["sigma"] if sigma_of_t is None else sigma_of_t(t)
    F = p["a0"] * m * m + p["a1"] * m * T * T / (p["K"] ** 2 + T * T)
    if p["arm"] == "produce":
        prod = p["beta"] * m * N
        dm = p["J"] - p["delta"] * m - F - prod
        dT = sig - p["kT"] * T + prod
        dD = 0.0
    elif p["arm"] == "repair":
        rep = p["rho"] * N * D
        dm = p["J"] - p["delta"] * m - F - p["rcost"] * rep
        dT = sig - p["kT"] * T + rep
        dD = p["kT"] * T - rep - p["lam"] * D
    else:
        raise ValueError(p["arm"])
    dN = (1 - p["eps"]) * F - p["d"] * N
    dB = p["eps"] * F - p["d"] * B
    return [dm, dT, dN, dB, dD]


def y0_empty(p):
    """No nuclei, no teacher; material at its unconsumed level J/delta."""
    return np.array([p["J"] / p["delta"], 0.0, 0.0, 0.0, 0.0])


def run(p, y0, t_end, sigma_of_t=None, n_eval=400):
    sol = solve_ivp(rhs, (0.0, t_end), y0, args=(p, sigma_of_t), method="LSODA",
                    rtol=1e-8, atol=1e-11, t_eval=np.linspace(0, t_end, n_eval))
    if not sol.success:
        raise RuntimeError(sol.message)
    return sol.t, sol.y


# ---------- steady states of the produce arm (eps allowed) ----------

def produce_steady_states(p, sigma=None):
    """All steady states (m, T, N, B) of the produce arm at outside supply
    sigma, sorted by N."""
    sig = p["sigma"] if sigma is None else sigma
    return _refine_states(p, sig)


def _refine_states(p, sig):
    """Steady states by eliminating m: for given T, N follows from T' = 0 and
    m from m' = 0, and N' = 0 is the residual in T alone."""
    e, a0, a1, K, beta, kT, d = (p["eps"], p["a0"], p["a1"], p["K"], p["beta"],
                                 p["kT"], p["d"])
    J, delta = p["J"], p["delta"]

    def F(m, T):
        return a0 * m * m + a1 * m * T * T / (K * K + T * T)

    def m_of_T(T):
        # from N' = 0 and T' = 0: beta m N = kT T - sig, N = (1-e)F/d.
        # m' = 0: J - delta m - F - (kT T - sig) = 0 ->
        # F(m,T) + delta m = J - kT T + sig. LHS increasing in m: unique m.
        rhsv = J - kT * T + sig
        if rhsv <= 0:
            return np.nan
        return brentq(lambda m: F(m, T) + delta * m - rhsv, 0.0, rhsv / delta + 1e-12)

    def resid(T):
        m = m_of_T(T)
        if np.isnan(m):
            return np.nan
        N = (1 - e) * F(m, T) / d
        return beta * m * N - (kT * T - sig)

    Tmax = (J + sig) / kT
    grid = np.concatenate([np.linspace(0, 1e-3, 50)[:-1], np.geomspace(1e-3, Tmax * (1 - 1e-9), 6000)])
    vals = np.array([resid(T) for T in grid])
    roots = []
    for i in range(len(grid) - 1):
        a, b = vals[i], vals[i + 1]
        if np.isnan(a) or np.isnan(b):
            continue
        if a == 0:
            roots.append(grid[i])
        elif a * b < 0:
            roots.append(brentq(resid, grid[i], grid[i + 1], xtol=1e-15))
    states = []
    for T in roots:
        m = m_of_T(T)
        Fv = F(m, T)
        N = (1 - e) * Fv / d
        B = e * Fv / d
        states.append((m, T, N, B))
    return sorted(states, key=lambda s: s[2])


def jacobian(p, y, sig=None, h=1e-7):
    q = dict(p)
    if sig is not None:
        q["sigma"] = sig
    y = np.asarray(y, float)
    f0 = np.array(rhs(0, y, q))
    Jm = np.zeros((5, 5))
    for i in range(5):
        yy = y.copy()
        hh = h * max(1.0, abs(y[i]))
        yy[i] += hh
        Jm[:, i] = (np.array(rhs(0, yy, q)) - f0) / hh
    return Jm


def stable(p, state, sig=None):
    m, T, N, B = state
    Jm = jacobian(p, [m, T, N, B, 0.0], sig)
    idx = [0, 1, 2, 3] if p["arm"] == "produce" else [0, 1, 2, 3, 4]
    ev = np.linalg.eigvals(Jm[np.ix_(idx, idx)])
    return bool(np.all(ev.real < 0)), ev


def maintained_state(p, sig=0.0):
    """The stable steady state with the largest N, if it is well above the
    spontaneous background; else None."""
    sts = _refine_states(p, sig)
    good = [s for s in sts if stable(p, s, sig)[0]]
    if not good:
        return None
    top = good[-1]
    if len(good) == 1:
        # one stable state: maintained if far above the spontaneous background
        return top if top[2] >= 50 * background_N(p) else None
    return top if top[2] >= 50 * background_N(p) else None


def closes(p):
    """Does the loop close at p: a stable maintained state with sigma = 0?"""
    return maintained_state(p, 0.0) is not None


def persists_after_withdrawal(p, y, t_after=600.0):
    """Withdraw the outside teacher for good from state y; does the nucleus
    persist (end near the sigma = 0 maintained state)?"""
    q = dict(p)
    q["sigma"] = 0.0
    ms = maintained_state(q, 0.0)
    if ms is None:
        return False
    _, Y = run(q, y, t_after, n_eval=3)
    return bool(Y[2, -1] > 0.5 * ms[2])


def founding(sig, t_w):
    return lambda t: sig if t < t_w else 0.0


def min_founding_time(p, sig, t_hi=400.0, tol=0.05):
    """Shortest duration of an outside teacher supply sigma, from the empty
    state, after which the nucleus persists with the supply withdrawn."""
    q = dict(p)
    y0 = y0_empty(q)

    def ok(tw):
        q2 = dict(q)
        q2["sigma"] = sig
        _, Y = run(q2, y0, tw, n_eval=2)
        return persists_after_withdrawal(q, Y[:, -1])

    if not ok(t_hi):
        return np.inf
    lo, hi = 0.0, t_hi
    if ok(1e-9):
        return 0.0
    while hi - lo > tol:
        mid = 0.5 * (lo + hi)
        if ok(mid):
            hi = mid
        else:
            lo = mid
    return hi


def background_N(p):
    """Nuclei held by spontaneous formation alone at unconsumed material."""
    return p["a0"] * (p["J"] / p["delta"]) ** 2 / p["d"]


def sigma_needed(p, N_target):
    """Standing outside teacher supply needed to hold good nuclei at N_target
    in steady state (produce arm). Returns (sigma, m, T): sigma = 0 when the
    loop alone over-supplies at that level; nan when material cannot carry
    N_target at all."""
    e, a0, a1, K, beta, kT, d = (p["eps"], p["a0"], p["a1"], p["K"], p["beta"],
                                 p["kT"], p["d"])
    F = d * N_target / (1 - e)
    m = (p["J"] - F) / (p["delta"] + beta * N_target)
    if m <= 0:
        return np.nan, np.nan, np.nan
    templ = F - a0 * m * m
    if templ <= 0:
        return 0.0, m, 0.0
    x = templ / (a1 * m)          # = T^2/(K^2+T^2)
    if x >= 1:
        return np.nan, m, np.nan
    T = K * np.sqrt(x / (1 - x))
    sig = kT * T - beta * m * N_target
    return max(0.0, sig), m, T


def critical(p, key, lo, hi, tol=1e-6, closes_low=True):
    """Bisect the value of p[key] at which closure is lost. closes_low: the
    loop closes for small values (e.g. kT, eps) and fails for large."""
    def c(v):
        q = dict(p)
        q[key] = v
        return closes(q)
    clo, chi = c(lo), c(hi)
    if clo == chi:
        return np.nan
    while hi - lo > tol * max(1.0, abs(hi)):
        mid = 0.5 * (lo + hi)
        if c(mid) == clo:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


# ---------- succession: the produce arm resolved by teaching generation ----------

def gen_rhs(t, y, p, G, sigma_of_t):
    """y = [m, T_0..T_G, N_1..N_G]. T_0 is the outside teacher; a nucleus
    taught by a generation-g teacher is generation g+1 and makes generation
    g+1 teachers. Spontaneous nuclei count as generation 1. Generation G
    absorbs all later ones. eps is taken as 0."""
    m = y[0]
    T = y[1:G + 2]
    N = y[G + 2:]
    Ttot = T.sum()
    Ftemp = p["a1"] * m * Ttot * Ttot / (p["K"] ** 2 + Ttot * Ttot)
    Fsp = p["a0"] * m * m
    share = T / Ttot if Ttot > 0 else np.zeros_like(T)
    formN = Ftemp * share[:-1]           # T_g -> N_{g+1}, g = 0..G-1
    formN[-1] += Ftemp * share[-1]       # T_G -> N_G (absorbing)
    formN[0] += Fsp
    prodT = p["beta"] * m * N            # N_g -> T_g, g = 1..G
    dm = p["J"] - p["delta"] * m - Ftemp - Fsp - prodT.sum()
    dT = -p["kT"] * T
    dT[0] += sigma_of_t(t)
    dT[1:] += prodT
    dN = formN - p["d"] * N
    return np.concatenate([[dm], dT, dN])


def run_generations(p, sig, t_w, t_end, G=80, n_eval=801):
    y0 = np.zeros(1 + (G + 1) + G)
    y0[0] = p["J"] / p["delta"]
    sol = solve_ivp(gen_rhs, (0, t_end), y0, args=(p, G, founding(sig, t_w)),
                    method="LSODA", rtol=1e-8, atol=1e-12,
                    t_eval=np.linspace(0, t_end, n_eval))
    if not sol.success:
        raise RuntimeError(sol.message)
    T = sol.y[1:G + 2]
    N = sol.y[G + 2:]
    return sol.t, sol.y[0], T, N


# ---------- finite numbers: a Gillespie version of the produce arm ----------

def gillespie_extinction(p, omega, y_counts, t_max, rng):
    """Exact stochastic simulation of the produce arm in volume omega with
    sigma = 0 from integer counts (m, T, N). Returns the first time at which
    T and N are both 0 (the loop is lost; only spontaneous formation could
    restart it), or t_max if that never happens. Rates in counts: material
    inflow J*omega; washout delta*m; spontaneous a0*m(m-1)/omega; templated
    a1*m*T(T-1)/(omega^2 K^2 + T(T-1)); production beta*m*N/omega; teacher
    loss kT*T; nucleus loss d*N."""
    m, T, N = (int(v) for v in y_counts)
    t = 0.0
    J, de, a0, a1, K, be, kT, d = (p["J"], p["delta"], p["a0"], p["a1"], p["K"],
                                   p["beta"], p["kT"], p["d"])
    while t < t_max:
        if T == 0 and N == 0:
            return t
        TT = T * max(T - 1, 0)
        r = np.array([
            J * omega,
            de * m,
            a0 * m * max(m - 1, 0) / omega,
            a1 * m * TT / (omega * omega * K * K + TT),
            be * m * N / omega,
            kT * T,
            d * N,
        ])
        R = r.sum()
        t += rng.exponential(1.0 / R)
        k = int(np.searchsorted(np.cumsum(r), rng.random() * R, side="right"))
        if k == 0:
            m += 1
        elif k == 1:
            m -= 1
        elif k in (2, 3):
            m -= 1
            N += 1
        elif k == 4:
            m -= 1
            T += 1
        elif k == 5:
            T -= 1
        else:
            N -= 1
    return t_max
