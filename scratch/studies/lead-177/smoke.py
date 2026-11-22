"""Quick look at the forager arms over a few seeds (not the study run)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import numpy as np  # noqa: E402

import forager as F  # noqa: E402

seeds = range(int(sys.argv[1]) if len(sys.argv) > 1 else 8)
for sc in F.SCENARIOS:
    for a in F.ARMS:
        rs = [F.run(a, sc, s) for s in seeds]
        surv = np.mean([r["survived"] for r in rs])
        inta = np.mean([r["post_intake"] for r in rs])
        fw = [r["first_warn"] for r in rs if r["first_warn"] is not None]
        att = [tuple(r["attended_end"]) for r in rs]
        print(f"{sc:8s} {a:14s} surv {surv:.2f} intake {inta:7.0f} "
              f"miss {np.mean([r['missed'] for r in rs]):6.1f} "
              f"fw {np.mean([r['false_warn'] for r in rs]):5.1f} "
              f"warn {np.median(fw) if fw else None} n{len(fw)} "
              f"probes {np.mean([r['probes_post'] for r in rs]):5.1f} "
              f"att {max(set(att), key=att.count)}")
