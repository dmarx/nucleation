"""LEAD-067 study: the null, the planar case, curved charts, noise, underdetermination.

Run: python3 -I run_study.py [out.json]   (a few seconds)
"""

import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # python3 -I drops it
import transport as t  # noqa: E402


def main(out="results.json"):
    rng = np.random.default_rng(20261122)
    res = {"seed": 20261122}

    # 1. the null
    null = []
    for d, k in [(2, 2), (3, 3), (5, 6)]:
        devs, gaps, undetermined = [], [], 0
        for _ in range(1000):
            ctx, g, _ = t.null_construction(d, k, rng)
            T, info = t.derive_transports(ctx)
            undetermined += not all(i["determined"] for i in info.values())
            devs.append(t.deviation(t.holonomy(T)))
            gaps.append(min(np.linalg.norm(g[a] - g[b]) for a, b in (("A", "B"), ("B", "C"), ("C", "A"))))
        null.append(dict(d=d, k=k, draws=1000, undetermined_draws=undetermined,
                         max_holonomy_deviation=max(devs),
                         min_frame_difference=min(gaps), median_frame_difference=float(np.median(gaps))))
    res["null"] = null

    # 2. the planar case: holonomy angle against the sum of internal angles
    planar = []
    for _ in range(12):
        theta = {c: float(rng.uniform(-1.2, 1.2)) for c in t.LOOP}
        ctx, _ = t.planar_construction(theta, rng=rng)
        T, info = t.derive_transports(ctx)
        H = t.holonomy(T)
        _, worst = t.glue(ctx, T)
        total = sum(theta.values())
        planar.append(dict(theta=theta, sum=total,
                           expected_abs_angle=float(abs(np.angle(np.exp(1j * total)))),
                           abs_holonomy_angle=abs(t.rotation_angle_2d(H)),
                           max_fit_residual=max(i["residual"] for i in info.values()),
                           glue_inconsistency=worst))
    theta = {"A": 0.3, "B": -0.1, "C": 0.5}
    ctx, _ = t.planar_construction(theta, rng=rng)
    T, _ = t.derive_transports(ctx)
    rows = t.route_discrepancy(ctx, T, held="A", absent="B", via="C")
    res["planar"] = planar
    res["planar_route_example"] = dict(theta=theta, rows=[dict(held_commitment=m, imported=n, direct=a, via_C=b)
                                                         for m, n, a, b in rows])

    # 3. curved charts: local linear charts of the sphere of normalized profiles
    sphere = []
    for s in (0.2, 0.4, 0.8, 1.2):
        m = {"A": [1, 0, 0], "B": [np.cos(s), np.sin(s), 0], "C": [np.cos(s), 0, np.sin(s)]}
        for spread in (0.04, 0.01, 0.0025):
            angs = []
            for _ in range(20):
                ctx, mm, _ = t.sphere_construction(m, spread, 10, rng)
                T, _ = t.derive_transports(ctx, centred=True)
                angs.append(abs(t.rotation_angle_2d(t.holonomy(T))))
            sphere.append(dict(side=s, spread=spread, excess=t.spherical_excess(mm),
                               mean_abs_angle=float(np.mean(angs)), sd_abs_angle=float(np.std(angs))))
    res["sphere"] = sphere

    # 4. the null under noise: a reference distribution for a test
    noise = []
    for k in (3, 10):
        for sigma in (0.001, 0.01, 0.03, 0.1):
            pairs = [t.noisy_null(3, k, sigma, rng, return_det=True) for _ in range(500)]
            devs = np.array([p[0] for p in pairs])
            flipped = np.array([p[1] < 0 for p in pairs])
            noise.append(dict(d=3, k=k, sigma=sigma, draws=500,
                              median=float(np.median(devs)), mean=float(np.mean(devs)),
                              q95=float(np.quantile(devs, 0.95)),
                              share_orientation_flipped=float(flipped.mean()),
                              q95_unflipped=float(np.quantile(devs[~flipped], 0.95))))
    res["noisy_null"] = noise

    # 5. underdetermination: one shared commitment in R^3
    det, rows = t.underdetermined_family(rng, np.linspace(0, 2 * np.pi, 361))
    res["underdetermined"] = dict(determined=det, max_fit_residual=max(r[1] for r in rows),
                                  min_holonomy_deviation=min(r[2] for r in rows),
                                  max_holonomy_deviation=max(r[2] for r in rows))

    with open(out, "w") as f:
        json.dump(res, f, indent=1)
    print(json.dumps({k: v for k, v in res.items() if k not in ("planar", "planar_route_example")}, indent=1))
    for p in planar:
        print(round(p["expected_abs_angle"], 6), round(p["abs_holonomy_angle"], 6), f"{p['glue_inconsistency']:.2e}")


if __name__ == "__main__":
    main(*sys.argv[1:])
