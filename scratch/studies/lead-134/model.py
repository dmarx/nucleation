"""CASE-114 'The imagined owner', built in numpy (LEAD-134).

Two systems with EQUIVALENT distributed control and similar behaviour. Both
observe the same per-component signals (equal input, equal capacity). They
differ only in the self-model's belief about the causal graph:

  - accurate    : K parallel autonomous components (the TRUE graph).
  - centralized : one 'owner' command that all effectors execute uniformly
                  (a star graph). Same parameter count; it reconstructs the
                  aggregate outcome EXACTLY (not behaviourally coarser), but
                  it is wrong about who controls what.

CASE-114's main threat is that an accurate model simply carries more
information, so worse attribution would only show that a coarser model
answers component questions less well. We defeat that here: both self-models
reconstruct the aggregate outcome exactly (sum of attribution == observed
error) and are given identical observations and parameter counts. The only
difference is the causal ontology. So any attribution divergence is
wrong-about-control, not merely-coarser.

True causes (which component's drive spiked on each error) are RECORDED APART,
by the simulator, and compared against each self-model's reported cause.

Run with:  python3 -I model.py
"""
import json
import os
import numpy as np

# ----- A distributed-control plant ---------------------------------------

def simulate(K, T, sigmas, fault_rate, fault_scale, obs_noise, seed,
             fault_weights=None):
    """One run of a plant with K independent components.

    Each component i emits an independent drive deviation d_i(t) ~ N(0,sig_i^2).
    The outcome deviation is e(t) = sum_i d_i(t) + obs noise. An 'error event'
    is a timestep where a single component j is given a fault excursion; the
    simulator records (t, j) as the TRUE cause, apart from any self-model.

    `fault_weights` is the distribution over which component faults (defaults
    to uniform). A concentrated distribution models a specific rogue component,
    the setting in which 'revise governance after an error' has real stakes.

    Returns a dict. `obs` (T,K) are the per-component signals both self-models
    observe (identical input). `e` (T,) is the aggregate outcome deviation.
    `fault_t`, `fault_j` index the recorded true causes.
    """
    sigmas = np.asarray(sigmas, dtype=float)
    assert sigmas.shape == (K,)
    if fault_weights is None:
        fw = np.ones(K) / K
    else:
        fw = np.asarray(fault_weights, dtype=float)
        fw = fw / fw.sum()
    rng = np.random.default_rng(seed)
    d = rng.normal(0.0, sigmas, size=(T, K))          # independent drives
    # inject single-component faults at random timesteps
    n_faults = max(1, int(round(fault_rate * T)))
    fault_t = rng.choice(T, size=n_faults, replace=False)
    fault_j = rng.choice(K, size=n_faults, p=fw)
    sign = rng.choice([-1.0, 1.0], size=n_faults)
    # fault magnitude scaled to the faulted component's own sigma so the
    # excursion is a genuine deviation, not a trivially large spike.
    d[fault_t, fault_j] += sign * fault_scale * sigmas[fault_j]
    obs = d + rng.normal(0.0, obs_noise, size=(T, K))  # measured signals
    e = d.sum(axis=1) + rng.normal(0.0, obs_noise, size=T)
    order = np.argsort(fault_t)
    return {
        "K": K, "T": T, "sigmas": sigmas, "obs": obs, "e": e,
        "fault_t": fault_t[order], "fault_j": fault_j[order],
    }


# ----- Two self-models ----------------------------------------------------

def accurate_attribution(obs):
    """Accurate self-model: believes components are autonomous and parallel.
    Attribution is the per-component signal itself (K slots). Reconstructs the
    aggregate exactly up to observation noise: sum == sum(obs)."""
    return obs.copy()


def centralized_attribution(obs):
    """Centralized self-model: believes a single owner command drives all
    effectors uniformly (star graph, W_i = 1). It infers the scalar command
    c = mean(obs) and explains the outcome as the owner's doing, spread
    uniformly over effectors: a_i = c for all i.

    This has the SAME parameter count and reconstructs the aggregate EXACTLY
    (sum a = K*mean(obs) = sum(obs)); it is not a lossy summary of the
    outcome. It is simply wrong about which component caused what."""
    c = obs.mean(axis=1, keepdims=True)
    return np.repeat(c, obs.shape[1], axis=1)


def reported_cause(attribution_row):
    """Which component the self-model names as the cause (argmax |a_i|)."""
    return int(np.argmax(np.abs(attribution_row)))


def aggregate_reconstruction_error(obs, attribution):
    """Max |sum(attribution) - sum(obs)| over timesteps: 0 means the self-model
    reproduces the behaviour (aggregate outcome) exactly."""
    return float(np.max(np.abs(attribution.sum(axis=1) - obs.sum(axis=1))))


# ----- Phase 1: open loop (control held fixed; self-model narrates) --------

def open_loop(sim):
    """Both self-models are passive observers of the SAME plant run, so the
    plant's control and behaviour are identical (held fixed). Only the reports
    differ. Compare each report against the recorded true causes."""
    obs, ft, fj, K = sim["obs"], sim["fault_t"], sim["fault_j"], sim["K"]
    acc = accurate_attribution(obs)
    cen = centralized_attribution(obs)

    # measure: capacity / behavioural match -- both reconstruct the outcome.
    cap = {
        "accurate_aggregate_recon_err": aggregate_reconstruction_error(obs, acc),
        "centralized_aggregate_recon_err": aggregate_reconstruction_error(obs, cen),
    }

    # measure: localization accuracy on recorded faults.
    acc_rep = np.array([reported_cause(acc[t]) for t in ft])
    cen_rep = np.array([reported_cause(cen[t]) for t in ft])
    loc = {
        "n_faults": int(len(ft)),
        "accurate_localization_acc": float(np.mean(acc_rep == fj)),
        "centralized_localization_acc": float(np.mean(cen_rep == fj)),
        "chance": 1.0 / K,
    }

    # measure: mean attribution mass placed on the TRUE culprit (share of the
    # total attributed magnitude). Accurate concentrates on the culprit;
    # centralized spreads uniformly (~1/K).
    def mass_on_true(att):
        rows = att[ft]
        mag = np.abs(rows)
        share = mag[np.arange(len(ft)), fj] / (mag.sum(axis=1) + 1e-12)
        return float(share.mean())
    mass = {
        "accurate_mass_on_true_cause": mass_on_true(acc),
        "centralized_mass_on_true_cause": mass_on_true(cen),
        "uniform_baseline": 1.0 / K,
    }

    # measure: judgment of authorship -- entropy of the control distribution
    # the self-model reports (over components), averaged on faults. High
    # entropy = distributed; 0 = a single owner. Accurate tracks the true
    # (one culprit -> low entropy per event); centralized is ~uniform.
    def report_entropy(att):
        rows = np.abs(att[ft]) + 1e-12
        p = rows / rows.sum(axis=1, keepdims=True)
        return float(np.mean(-(p * np.log(p)).sum(axis=1)))
    authorship = {
        "accurate_report_entropy": report_entropy(acc),
        "centralized_report_entropy": report_entropy(cen),
        "max_entropy": float(np.log(K)),
    }
    return {"capacity": cap, "localization": loc,
            "mass": mass, "authorship": authorship}


# ----- Phase 2: closed loop (self-model feeds governance; A27 s.12 loop) ----

def closed_loop(K, T, sigmas, fault_rate, fault_scale, obs_noise,
                seed, rounds, lr, which, fault_weights=None):
    """After each round the self-model's blame drives a governance revision:
    the gain (sigma) of the blamed component is reduced. The accurate model
    blames the true culprit; the centralized model spreads blame uniformly and
    so revises every component a little. We track the error rate over rounds.

    Faults concentrate on a rogue component (default: component 0 carries 70%),
    so suppressing the right component helps far more than suppressing all. A
    component's fault excursion scales with its gain, so reducing a rogue's
    gain reduces its faults -- governance has real purchase.

    This is the loop CASE-114 warns breaks the held-fixed equivalence: here the
    two systems' control diverges BECAUSE the self-models differ, which is
    exactly A27's fourth measure (ability to revise governance after error)."""
    sig = np.asarray(sigmas, dtype=float).copy()
    base_sig = sig.copy()
    if fault_weights is None:
        fw = np.full(K, 0.30 / (K - 1))
        fw[0] = 0.70
    else:
        fw = np.asarray(fault_weights, dtype=float)
    # an error is an outcome excursion well above the baseline aggregate noise,
    # so that (with a large fault_scale) errors are dominated by rogue faults
    # and almost never by quiet-step noise. Fixed from the base gains.
    baseline_std = np.sqrt((base_sig ** 2).sum())
    thresh = 3.2 * baseline_std
    rng_seed = seed
    trajectory = []
    for r in range(rounds):
        sim = simulate(K, T, sig, fault_rate, fault_scale, obs_noise,
                       seed=rng_seed + r * 101, fault_weights=fw)
        obs, ft, fj = sim["obs"], sim["fault_t"], sim["fault_j"]
        err_rate = float(np.mean(np.abs(sim["e"]) > thresh))
        trajectory.append(err_rate)
        att = (accurate_attribution(obs) if which == "accurate"
               else centralized_attribution(obs))
        # accumulate blame over this round's fault events
        blame = np.zeros(K)
        for t in ft:
            mag = np.abs(att[t])
            blame += mag / (mag.sum() + 1e-12)
        if blame.sum() > 0:
            blame = blame / blame.sum()
        # governance: shrink gain of blamed components (never below a floor)
        sig = np.maximum(sig * (1.0 - lr * K * blame), 0.05 * base_sig)
    # final error rate after the last revision
    sim = simulate(K, T, sig, fault_rate, fault_scale, obs_noise,
                   seed=rng_seed + rounds * 101, fault_weights=fw)
    final_err = float(np.mean(np.abs(sim["e"]) > thresh))
    trajectory.append(final_err)
    # collateral damage: how much legitimate gain was stripped from components
    # that were NOT disproportionately faulty (measured vs accurate's target).
    collateral = float(np.mean((base_sig - sig) / base_sig))
    cumulative_err = float(np.sum(trajectory))   # errors incurred while revising
    # collateral measured on the non-rogue (innocent) components only
    innocent = np.ones(K, dtype=bool)
    innocent[int(np.argmax(fw))] = False
    innocent_loss = float(np.mean(((base_sig - sig) / base_sig)[innocent]))
    return {"trajectory": trajectory, "final_err": final_err,
            "cumulative_err": cumulative_err,
            "collateral_gain_loss_frac": collateral,
            "innocent_gain_loss_frac": innocent_loss,
            "final_sigmas": sig.tolist()}


# ----- grid driver, persisting per config to JSONL ------------------------

def run_grid(out_path):
    configs = []
    for K in (3, 5, 8):
        # a spread of component sigmas so control is genuinely unequal
        sig_profiles = {
            "equal": [1.0] * K,
            "graded": list(np.linspace(0.5, 1.5, K)),
        }
        for pname, sig in sig_profiles.items():
            for seed in range(10):
                configs.append((K, pname, sig, seed))

    done = set()
    if os.path.exists(out_path):
        with open(out_path) as fh:
            for line in fh:
                line = line.strip()
                if line:
                    r = json.loads(line)
                    done.add((r["K"], r["profile"], r["seed"]))

    with open(out_path, "a") as fh:
        for (K, pname, sig, seed) in configs:
            if (K, pname, seed) in done:
                continue
            T, fault_rate, obs_noise = 4000, 0.03, 0.05
            # open-loop attribution uses a strong single-component excursion
            # with uniform fault placement (the general attribution test);
            # closed-loop uses a larger scale so errors are fault-dominated.
            sim = simulate(K, T, sig, fault_rate, 4.0, obs_noise, seed)
            ol = open_loop(sim)
            cl_acc = closed_loop(K, T, sig, fault_rate, 15.0, obs_noise,
                                 seed, rounds=10, lr=0.06, which="accurate")
            cl_cen = closed_loop(K, T, sig, fault_rate, 15.0, obs_noise,
                                 seed, rounds=10, lr=0.06, which="centralized")
            rec = {"K": K, "profile": pname, "seed": seed,
                   "open_loop": ol,
                   "closed_loop_accurate": cl_acc,
                   "closed_loop_centralized": cl_cen}
            fh.write(json.dumps(rec) + "\n")
            fh.flush()
    return out_path


def summarize(out_path):
    rows = [json.loads(l) for l in open(out_path) if l.strip()]
    import statistics as st
    def avg(xs):
        return sum(xs) / len(xs)
    acc_loc = avg([r["open_loop"]["localization"]["accurate_localization_acc"] for r in rows])
    cen_loc = avg([r["open_loop"]["localization"]["centralized_localization_acc"] for r in rows])
    acc_mass = avg([r["open_loop"]["mass"]["accurate_mass_on_true_cause"] for r in rows])
    cen_mass = avg([r["open_loop"]["mass"]["centralized_mass_on_true_cause"] for r in rows])
    acc_recon = max(r["open_loop"]["capacity"]["accurate_aggregate_recon_err"] for r in rows)
    cen_recon = max(r["open_loop"]["capacity"]["centralized_aggregate_recon_err"] for r in rows)
    acc_fin = avg([r["closed_loop_accurate"]["final_err"] for r in rows])
    cen_fin = avg([r["closed_loop_centralized"]["final_err"] for r in rows])
    acc_cum = avg([r["closed_loop_accurate"]["cumulative_err"] for r in rows])
    cen_cum = avg([r["closed_loop_centralized"]["cumulative_err"] for r in rows])
    acc_inn = avg([r["closed_loop_accurate"]["innocent_gain_loss_frac"] for r in rows])
    cen_inn = avg([r["closed_loop_centralized"]["innocent_gain_loss_frac"] for r in rows])
    cum_wins = sum(r["closed_loop_accurate"]["cumulative_err"]
                   < r["closed_loop_centralized"]["cumulative_err"] for r in rows)
    inn_wins = sum(r["closed_loop_accurate"]["innocent_gain_loss_frac"]
                   < r["closed_loop_centralized"]["innocent_gain_loss_frac"] for r in rows)
    return {
        "n_configs": len(rows),
        "localization_acc": {"accurate": acc_loc, "centralized": cen_loc},
        "mass_on_true_cause": {"accurate": acc_mass, "centralized": cen_mass},
        "max_aggregate_recon_err": {"accurate": acc_recon, "centralized": cen_recon},
        "closed_loop_final_err": {"accurate": acc_fin, "centralized": cen_fin},
        "closed_loop_cumulative_err": {"accurate": acc_cum, "centralized": cen_cum},
        "innocent_gain_loss_frac": {"accurate": acc_inn, "centralized": cen_inn},
        "accurate_wins_cumulative_err": f"{cum_wins}/{len(rows)}",
        "accurate_wins_innocent_loss": f"{inn_wins}/{len(rows)}",
    }


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    out = os.path.join(here, "results.jsonl")
    run_grid(out)
    summary = summarize(out)
    with open(os.path.join(here, "summary.json"), "w") as fh:
        json.dump(summary, fh, indent=2)
    print(json.dumps(summary, indent=2))
