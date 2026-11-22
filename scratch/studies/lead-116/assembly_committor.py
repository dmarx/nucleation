# scratch/studies/lead-116/assembly_committor.py
#
# LEAD-116: run CASE-219 (stochastic assembly) and CASE-220 (factorial variant),
# extending CASE-216's four-state annealing toy, scoring intermediates by the
# committor q(s) = Pr_s(tau_F < tau_K) -- the chance of reaching the target F
# before a designated failure set K.
#
# Run: python3 -I scratch/studies/lead-116/assembly_committor.py
#
# The model generalises CASE-216's U/N/F/M chain to several components. A
# microstate is the SET of bonds currently formed (a subset of {a,b,c,d}); the
# generator is built over all 2^4 = 16 subsets plus an absorbing misfold sink K.
# Rates are invented constants (as CASE-215's are); a temperature knob T scales
# the off-rates for the persistence part, echoing CASE-216's melting. None is a
# DNA-origami measurement.
#
# Two alternative seams, a and b (the "two routings" of CASE-220), each nucleate
# the shared body c,d. Seam a completes to the valid form F_A = {a,c,d}; seam b
# to the valid form F_B = {b,c,d}; both are feasible folds. Two kinetic traps,
# both from the DNA-origami readings:
#   (i) incompatible-seam trap (Dunn et al.): any state holding BOTH seams a and
#       b strains the scaffold and misfolds, irreversibly, to K;
#   (ii) unnucleated collapse (DeLuca et al.; Sobczak): a body bond cannot form
#       without a seam to template it, and a seamless assembly collapses to K.
# So establishing seam a alone, or seam b alone, is each a productive nucleus,
# while establishing both is a trap: an assembly-dynamics instance of CLAIM-599's
# non-monotone V. Reallocating a fixed component stock between the two seams
# selects F_A against F_B with the attainable set {F_A, F_B} unchanged
# (QUESTION-400).

import itertools
import json
import numpy as np
from scipy.linalg import expm

BONDS = ("a", "b", "c", "d")
SEAMS = frozenset(("a", "b"))
BODY = ("c", "d")
F_A = frozenset(("a", "c", "d"))
F_B = frozenset(("b", "c", "d"))
SUBSETS = [frozenset(s) for n in range(len(BONDS) + 1) for s in itertools.combinations(BONDS, n)]
SI = {s: i for i, s in enumerate(SUBSETS)}  # 16 subset states; index 16 is the sink K
KSTATE = len(SUBSETS)
NST = len(SUBSETS) + 1


def n_seams(s):
    return len(s & SEAMS)


def default_params():
    return dict(
        T=300.0,          # temperature knob (K); scales off-rates (melting), as in CASE-216
        T_ref=300.0,
        T_scale=18.0,     # each T_scale K above T_ref multiplies off-rates by e
        seam_on=0.3,      # base rate to form a seam, scaled by its availability
        seam_off=0.2,     # base rate to break a seam
        body_on=3.0,      # rate to form a body bond WHEN a seam is present (nucleated), scaled by availability
        body_off=0.3,     # base rate to break a body bond
        collapse=2.0,     # unnucleated collapse rate from a seamless state -> K
        misfold_both=8.0, # incompatible-seam trap rate from any both-seams state -> K
        designed_seam={"a": 1.0, "b": 1.0},  # routing: multiplier on the designed seam's on-rate
        stabilize={"a": 1.0, "b": 1.0, "c": 1.0, "d": 1.0},  # targeted early stabilisation divides off-rate
        conc={"a": 1.0, "b": 1.0, "c": 1.0, "d": 1.0},        # availability; sum is the budget
        targets_absorbing=True,
    )


def _temp_factor(p):
    return np.exp((p["T"] - p["T_ref"]) / p["T_scale"])


def on_rate(bond, s, p):
    """Rate of forming `bond` from state s (0 if already present)."""
    if bond in s:
        return 0.0
    if bond in SEAMS:
        return p["seam_on"] * p["conc"][bond] * p["designed_seam"][bond]
    # body bond: forms only when at least one seam is present (nucleation)
    if n_seams(s) >= 1:
        return p["body_on"] * p["conc"][bond]
    return 0.0


def off_rate(bond, s, p):
    """Rate of breaking `bond` from state s (0 if absent). Scaled by temperature;
    targeted stabilisation divides the off-rate."""
    if bond not in s:
        return 0.0
    base = p["seam_off"] if bond in SEAMS else p["body_off"]
    return base * _temp_factor(p) / p["stabilize"][bond]


def to_K_rate(s, p):
    """Rate from state s into the misfold sink K."""
    if n_seams(s) == 2:
        return p["misfold_both"]          # incompatible-seam trap (Dunn et al.)
    if n_seams(s) == 0:
        return p["collapse"]              # unnucleated collapse (DeLuca et al.; Sobczak)
    return 0.0


def is_success(s):
    return s == F_A or s == F_B


def build_Q(p):
    """Continuous-time generator over 16 subsets + sink K (index 16)."""
    Q = np.zeros((NST, NST))
    for s in SUBSETS:
        i = SI[s]
        if is_success(s) and p["targets_absorbing"]:
            continue  # absorbing valid fold
        for bond in BONDS:
            if bond not in s:
                r = on_rate(bond, s, p)
                if r > 0:
                    Q[i, SI[s | {bond}]] += r
            else:
                r = off_rate(bond, s, p)
                if r > 0:
                    Q[i, SI[s - {bond}]] += r
        m = to_K_rate(s, p)
        if m > 0:
            Q[i, KSTATE] += m
    for i in range(NST):
        Q[i, i] = -Q[i].sum()
    return Q


def targets_and_failures(p):
    """Default success set = either valid fold; failure = the sink K."""
    return [SI[F_A], SI[F_B]], [KSTATE]


def committor(p, F=None, Kset=None):
    """q(s) = Pr_s(reach F before K), exact linear solve on transient states.

    Transient T: Q_TT q_T + Q_TF 1 = 0  (q = 1 on F, 0 on K)."""
    Q = build_Q(p)
    if F is None or Kset is None:
        F, Kset = targets_and_failures(p)
    F, Kset = set(F), set(Kset)
    absorbing = F | Kset
    trans = [i for i in range(NST) if i not in absorbing]
    ti = {s: k for k, s in enumerate(trans)}
    A = Q[np.ix_(trans, trans)]
    b = -Q[np.ix_(trans, list(F))].sum(axis=1)
    qT = np.linalg.solve(A, b)
    q = np.zeros(NST)
    for s in F:
        q[s] = 1.0
    for s in trans:
        q[s] = qT[ti[s]]
    return q, Q


def q_of(q, bonds):
    return q[SI[frozenset(bonds)]]


def assembly_prob(p, horizon):
    """Pr(X_horizon = F) occupancy, F absorbing: the yield at a fixed horizon."""
    Q = build_Q(p)
    P = expm(Q * horizon)
    F, _ = targets_and_failures(p)
    p0 = np.zeros(NST)
    p0[SI[frozenset()]] = 1.0
    pt = p0 @ P
    return float(pt[list(F)].sum()), float(pt[KSTATE])


def mean_first_passage(p):
    """Expected time from empty to absorption (F or K), transient linear solve."""
    Q = build_Q(p)
    F, Kset = targets_and_failures(p)
    absorbing = set(F) | set(Kset)
    trans = [i for i in range(NST) if i not in absorbing]
    ti = {s: k for k, s in enumerate(trans)}
    A = Q[np.ix_(trans, trans)]
    t = np.linalg.solve(A, -np.ones(len(trans)))
    return float(t[ti[SI[frozenset()]]])


# ------------------------------------------------------------------ checks ----

def _check_gamblers_ruin():
    """A linear birth-death chain's committor must match (1-r^i)/(1-r^M).
    Build a bespoke chain here so the solver is checked against a closed form."""
    M, up, down = 6, 0.8, 0.5
    n = M + 1
    Q = np.zeros((n, n))
    for i in range(1, M):
        Q[i, i + 1] = up
        Q[i, i - 1] = down
    np.fill_diagonal(Q, 0.0)
    for i in range(n):
        Q[i, i] = -Q[i].sum()
    trans = list(range(1, M))
    A = Q[np.ix_(trans, trans)]
    b = -Q[np.ix_(trans, [M])].sum(axis=1)
    qT = np.linalg.solve(A, b)
    r = down / up
    exact = [(1 - r**i) / (1 - r**M) for i in range(1, M)]
    assert np.allclose(qT, exact, atol=1e-12), (qT, exact)


def _check_committor_vs_montecarlo(p, n_runs=40000, seed=7):
    """Committor from the empty state against a Gillespie estimate."""
    q, Q = committor(p)
    F, Kset = targets_and_failures(p)
    F, Kset = set(F), set(Kset)
    rng = np.random.default_rng(seed)
    hits = 0
    for _ in range(n_runs):
        s = SI[frozenset()]
        while s not in F and s not in Kset:
            rate = -Q[s, s]
            if rate <= 0:
                break
            probs = Q[s].copy()
            probs[s] = 0.0
            probs = np.clip(probs, 0, None)
            probs /= probs.sum()
            s = rng.choice(NST, p=probs)
        if s in F:
            hits += 1
    est = hits / n_runs
    exact = q[SI[frozenset()]]
    se = (exact * (1 - exact) / n_runs) ** 0.5
    assert abs(est - exact) < 5 * se + 0.01, (est, exact, se)
    return est, exact


# --------------------------------------------------------------- scenarios ----

def scenario_nonmonotone():
    """CLAIM-599 from dynamics: {a} and {b} each productive, {a,b} a trap.
    Here F = either valid fold (completing at all); K = the misfold sink."""
    p = default_params()
    q, _ = committor(p)
    out = {
        "q_empty": q_of(q, []),
        "q_a": q_of(q, ["a"]),
        "q_b": q_of(q, ["b"]),
        "q_ab": q_of(q, ["a", "b"]),
        "q_ac": q_of(q, ["a", "c"]),
        "q_abc": q_of(q, ["a", "b", "c"]),
    }
    out["delta_a"] = out["q_a"] - out["q_empty"]
    out["delta_b"] = out["q_b"] - out["q_empty"]
    out["delta_ab"] = out["q_ab"] - out["q_empty"]
    return p, q, out


def committor_ranking(p, q):
    """All transient subset states ranked by committor, with bond count."""
    rows = []
    F, Kset = targets_and_failures(p)
    F = set(F)
    for s in SUBSETS:
        i = SI[s]
        if i in F:
            continue
        rows.append((tuple(sorted(s)), len(s), round(float(q[i]), 4)))
    rows.sort(key=lambda r: -r[2])
    return rows


def scenario_factorial():
    """CASE-220: 2 routings x {uniform, targeted early stabilisation}.
    Routing A designs seam a (a nucleates faster); Routing B designs seam b.
    Targeted stabilisation divides the designed seam's off-rate (it persists once
    formed). delta_q_N = q(do designed seam) - q(empty) scores the nucleus."""
    cells = {}
    for routing, designed in (("A", "a"), ("B", "b")):
        for stab_name, stab_on in (("uniform", False), ("targeted", True)):
            p = default_params()
            p["designed_seam"][designed] = 2.0   # routing: designed seam nucleates twice as fast
            if stab_on:
                p["stabilize"][designed] = 4.0    # targeted early stabilisation of the designed seam
            q, _ = committor(p)
            cells[(routing, stab_name)] = {
                "q_empty": q_of(q, []),
                "q_designed_seam": q_of(q, [designed]),
                "delta_q_N": q_of(q, [designed]) - q_of(q, []),
                "q_both_seams": q_of(q, ["a", "b"]),
                "yield_1e6": assembly_prob(p, 1e6)[0],
            }
    # A fifth condition: targeted stabilisation of BOTH seams (locks in the trap)
    p = default_params()
    p["stabilize"]["a"] = 4.0
    p["stabilize"]["b"] = 4.0
    q, _ = committor(p)
    cells[("both-seams", "targeted")] = {
        "q_empty": q_of(q, []),
        "q_designed_seam": q_of(q, ["a", "b"]),
        "delta_q_N": q_of(q, ["a", "b"]) - q_of(q, []),
        "q_both_seams": q_of(q, ["a", "b"]),
        "yield_1e6": assembly_prob(p, 1e6)[0],
    }
    return cells


def committor_form_A(p):
    """Which-form committor: q_A(s) = Pr_s(reach F_A before F_B or K)."""
    q, _ = committor(p, F=[SI[F_A]], Kset=[SI[F_B], KSTATE])
    return q


def scenario_allocation(n=21):
    """QUESTION-400: fixed total stock, vary allocation; attainable forms fixed.
    Budget C = conc[a]+conc[b]+conc[c]+conc[d] held constant. Both valid folds
    F_A and F_B stay reachable throughout, so the attainable set is unchanged;
    only the allocation changes which form results. q_succeed = chance of any
    valid fold before K; q_formA = chance of F_A before F_B or K; share_A =
    P(F_A)/P(F_A or F_B) at a long horizon."""
    C = 4.0
    # (1) split a fixed seam budget between the two seams; body fixed.
    body_each = 1.0
    seam_budget = C - 2 * body_each  # = 2.0
    split = []
    for phi in np.linspace(0.0, 1.0, n):   # phi = fraction of seam budget on b
        p = default_params()
        p["conc"]["a"] = seam_budget * (1 - phi) + 1e-6
        p["conc"]["b"] = seam_budget * phi + 1e-6
        p["conc"]["c"] = body_each
        p["conc"]["d"] = body_each
        q, _ = committor(p)
        qA = committor_form_A(p)
        occ = _form_occupancies(p, 1e6)
        split.append({"frac_on_b": round(float(phi), 4),
                      "conc_a": round(p["conc"]["a"], 3), "conc_b": round(p["conc"]["b"], 3),
                      "q_succeed": round(q_of(q, []), 4),
                      "q_formA_empty": round(qA[SI[frozenset()]], 4),
                      "share_A": round(occ["share_A"], 4)})
    # (2) move budget between the seams (together) and the body; total fixed.
    seambody = []
    for psi in np.linspace(0.1, 0.9, n):   # psi = fraction of budget on the two seams (split evenly)
        p = default_params()
        seam_tot = C * psi
        body_tot = C * (1 - psi)
        p["conc"]["a"] = seam_tot / 2
        p["conc"]["b"] = seam_tot / 2
        p["conc"]["c"] = body_tot / 2
        p["conc"]["d"] = body_tot / 2
        q, _ = committor(p)
        seambody.append({"frac_on_seams": round(float(psi), 4),
                         "conc_seam_each": round(p["conc"]["a"], 3), "conc_body_each": round(p["conc"]["c"], 3),
                         "q_succeed": round(q_of(q, []), 4),
                         "yield_1e6": round(assembly_prob(p, 1e6)[0], 4)})
    return {"budget": C, "split_seams": split, "seam_vs_body": seambody}


def _form_occupancies(p, horizon):
    Q = build_Q(p)
    P = expm(Q * horizon)
    p0 = np.zeros(NST); p0[SI[frozenset()]] = 1.0
    pt = p0 @ P
    pa, pb = float(pt[SI[F_A]]), float(pt[SI[F_B]])
    share = pa / (pa + pb) if (pa + pb) > 0 else float("nan")
    return {"P_A": pa, "P_B": pb, "share_A": share}


def _fold_survival(p, horizon):
    """Pr(X_horizon in {F_A, F_B} | X_0 = F_A), folds reversible."""
    Q = build_Q(p)
    P = expm(Q * horizon)
    p0 = np.zeros(NST); p0[SI[F_A]] = 1.0
    pt = p0 @ P
    return float(pt[SI[F_A]] + pt[SI[F_B]])


def scenario_persistence():
    """CLAIM-566: assembly is not persistence. Two separate probabilities.
    `reached` = chance a valid fold is reached from empty (folds absorbing).
    `survival(t)` = chance the formed fold is still folded at t (folds reversible,
    warming melts them). The fold off-rates are lowered here so the fold is
    metastable; the point is that reaching a fold and keeping it are distinct and
    move differently with T."""
    rows = []
    for Temp in (300.0, 330.0, 360.0):
        base = default_params()
        base["seam_off"] = 0.01   # lowered so the formed fold is metastable
        base["body_off"] = 0.01
        base["T_scale"] = 15.0
        p = dict(base); p["T"] = Temp; p["targets_absorbing"] = False
        pf = dict(base); pf["T"] = Temp; pf["targets_absorbing"] = True
        reached, _ = assembly_prob(pf, 1e4)
        rows.append({"T": Temp, "reached_F": round(reached, 4),
                     "survival_t1": round(_fold_survival(p, 1.0), 4),
                     "survival_t10": round(_fold_survival(p, 10.0), 4),
                     "survival_t100": round(_fold_survival(p, 100.0), 4)})
    return rows


def main():
    _check_gamblers_ruin()
    p0, q0, nm = scenario_nonmonotone()
    est, exact = _check_committor_vs_montecarlo(default_params())
    ranking = committor_ranking(p0, q0)
    fac = scenario_factorial()
    alloc = scenario_allocation()
    pers = scenario_persistence()
    mfpt = mean_first_passage(default_params())

    out = {
        "nonmonotone": nm,
        "committor_ranking": ranking,
        "mc_check": {"estimate": round(est, 4), "exact": round(exact, 4)},
        "mean_first_passage_empty": round(mfpt, 3),
        "factorial": {f"{k[0]}/{k[1]}": v for k, v in fac.items()},
        "allocation": alloc,
        "persistence": pers,
    }
    here = __file__.rsplit("/", 1)[0]
    with open(here + "/results.json", "w") as fh:
        json.dump(out, fh, indent=2, default=lambda x: round(float(x), 6))

    lines = []
    def pr(x=""):
        lines.append(x)
        print(x)

    pr("=== LEAD-116: stochastic and factorial assembly scored by committor ===")
    pr("Model: bonds a,b (alternative seams), c,d (body). Target F = body + exactly")
    pr("one seam. Both seams present -> misfold trap K. Committor q(s)=Pr_s(tau_F<tau_K).")
    pr(f"Solver check vs gambler's ruin: pass.  Committor from empty: exact {exact:.4f}, "
       f"Monte Carlo {est:.4f}.")
    pr()
    pr("--- CLAIM-599 from assembly dynamics: two productive nuclei combine into a trap ---")
    pr(f"q(empty)   = {nm['q_empty']:.4f}")
    pr(f"q({{a}})     = {nm['q_a']:.4f}   (Delta_a  = {nm['delta_a']:+.4f}, productive)")
    pr(f"q({{b}})     = {nm['q_b']:.4f}   (Delta_b  = {nm['delta_b']:+.4f}, productive)")
    pr(f"q({{a,b}})   = {nm['q_ab']:.4f}   (Delta_ab = {nm['delta_ab']:+.4f}, a TRAP: more bonds, lower q)")
    pr()
    pr("--- Committor ranks intermediates by future, not by progress (CLAIM-567) ---")
    pr("state                    bonds   q")
    for st, nb, qq in ranking:
        pr(f"  {str(st):22}   {nb}     {qq:.4f}")
    pr()
    pr("--- CASE-220 factorial: 2 routings x {uniform, targeted early stabilisation} ---")
    pr("cell                 q_empty  delta_q_N  q(both seams)  yield(t=1e6)")
    for k, v in fac.items():
        pr(f"  {k[0]:11} {k[1]:9} {v['q_empty']:.4f}   {v['delta_q_N']:+.4f}       "
           f"{v.get('q_both_seams', float('nan')):.4f}        {v['yield_1e6']:.4f}")
    pr()
    pr("--- QUESTION-400: fixed total stock, vary allocation (attainable forms unchanged) ---")
    pr("(1) split a fixed seam budget between seam a and seam b (body fixed):")
    pr("  frac_on_b  conc_a conc_b  q_succeed  q(F_A|empty)  share_A(t=1e6)")
    for r in alloc["split_seams"][::4]:
        pr(f"   {r['frac_on_b']:.3f}     {r['conc_a']:.2f}   {r['conc_b']:.2f}    "
           f"{r['q_succeed']:.4f}     {r['q_formA_empty']:.4f}       {r['share_A']:.4f}")
    pr("(2) move a fixed budget between the two seams and the body:")
    pr("  frac_on_seams conc_seam conc_body  q_succeed  yield")
    for r in alloc["seam_vs_body"][::4]:
        pr(f"   {r['frac_on_seams']:.3f}       {r['conc_seam_each']:.2f}     {r['conc_body_each']:.2f}     "
           f"{r['q_succeed']:.4f}  {r['yield_1e6']:.4f}")
    pr()
    pr("--- CLAIM-566: assembly is not persistence (fold off-rates lowered; folds reversible) ---")
    pr("  A formed fold is lost two ways: melting (off-rates, rise with T) and")
    pr("  mis-binding the competing seam into the trap (T-independent).")
    pr("  T(K)  reached_F  surv(t=1)  surv(t=10)  surv(t=100)")
    for r in pers:
        pr(f"  {r['T']:.0f}   {r['reached_F']:.4f}     {r['survival_t1']:.4f}     "
           f"{r['survival_t10']:.4f}      {r['survival_t100']:.4f}")
    pr()
    pr(f"Mean first-passage time empty->absorption (default): {mfpt:.3f}")

    with open(here + "/results.txt", "w") as fh:
        fh.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
