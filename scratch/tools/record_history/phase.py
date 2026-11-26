# scratch/tools/record_history/phase.py
"""The stability-generativity view (A34, pilot 2): quadrants, summary, plot."""
from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path

from record_history.profile import QUADRANTS, quadrant


STABILITY = {"revision": "days_since_revision", "prose": "days_since_prose"}


def classify(profiles: dict[str, dict], stable_days: int, generative: int, window: int,
             stability: str = "revision") -> None:
    """Add `quadrant` and `young` (younger than `stable_days`) to each profile.

    `stability` "revision" measures days since prose was last rewritten
    (lines removed); "prose" also counts accretion (appended dated notes).
    """
    for p in profiles.values():
        p["quadrant"] = quadrant(p[STABILITY[stability]], p[f"new_dependents_{window}d"],
                                 stable_days, generative)
        p["young"] = p["age_days"] < stable_days


def summary_table(profiles: dict[str, dict], schemes: list[str] | None = None) -> str:
    """Counts by scheme and quadrant, with entries younger than the threshold apart."""
    counts: dict[str, Counter] = defaultdict(Counter)
    for p in profiles.values():
        if schemes and p["scheme"] not in schemes:
            continue
        counts[p["scheme"]][(p["quadrant"], p["young"])] += 1
    head = "| scheme | " + " | ".join(QUADRANTS) + " | of which young |\n"
    head += "|---" * (len(QUADRANTS) + 2) + "|\n"
    rows = []
    for s in sorted(counts):
        c = counts[s]
        cells = [str(c[(q, False)] + c[(q, True)]) for q in QUADRANTS]
        rows.append(f"| {s} | " + " | ".join(cells) + f" | {sum(v for (q, y), v in c.items() if y)} |")
    return head + "\n".join(rows) + "\n"


def exemplars(profiles: dict[str, dict], scheme: str, window: int, k: int = 5) -> dict[str, list[dict]]:
    """The k most-depended-on entries of each quadrant (old enough to judge)."""
    out = {}
    for q in QUADRANTS:
        ps = [p for p in profiles.values()
              if p["scheme"] == scheme and p["quadrant"] == q and not p["young"]]
        ps.sort(key=lambda p: (p[f"new_dependents_{window}d"], p["in_degree"]), reverse=True)
        out[q] = ps[:k]
    return out


def plot(profiles: dict[str, dict], scheme: str, window: int, stable_days: int, path: Path,
         stability: str = "revision") -> None:
    """Scatter: days since the last substantive prose revision against new dependents."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import random

    rng = random.Random(0)
    colours = dict(zip(QUADRANTS, ("#7c3aed", "#0d9488", "#d97706", "#64748b")))
    fig, ax = plt.subplots(figsize=(8, 5.5), dpi=150)
    for q in QUADRANTS:
        ps = [p for p in profiles.values() if p["scheme"] == scheme and p["quadrant"] == q]
        xs = [p[STABILITY[stability]] + rng.uniform(-0.4, 0.4) for p in ps]
        ys = [p[f"new_dependents_{window}d"] + rng.uniform(-0.25, 0.25) for p in ps]
        ax.scatter(xs, ys, s=7, alpha=0.45, color=colours[q], label=f"{q} ({len(ps)})", linewidths=0)
    ax.axvline(stable_days - 0.5, color="#888", lw=0.8, ls="--")
    ax.axhline(0.5, color="#888", lw=0.8, ls="--")
    ax.set_yscale("symlog", linthresh=2)
    ax.set_xlabel(f"Days since last substantive {stability} (prose stability)")
    ax.set_ylabel(f"New dependents in the last {window} days (generativity, symlog)")
    ax.set_title(f"{scheme}: stability against generativity (jittered)")
    ax.legend(fontsize=8, loc="upper right", frameon=False)
    fig.tight_layout()
    fig.savefig(path)
    plt.close(fig)
