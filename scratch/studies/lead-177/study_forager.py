"""Run the forager study: every scenario x arm x seed, one JSON line per run.

Resumes by skipping (scenario, arm, seed) triples already in the file.
Usage: python3 -I study_forager.py [n_seeds]
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
import forager as F  # noqa: E402

OUT = HERE / "results" / "forager.jsonl"


def jsonable(v):
    if hasattr(v, "item"):
        return v.item()
    if isinstance(v, (list, tuple)):
        return [jsonable(u) for u in v]
    return v


def main(n_seeds=40):
    OUT.parent.mkdir(exist_ok=True)
    done = set()
    if OUT.exists():
        for line in OUT.read_text().splitlines():
            r = json.loads(line)
            done.add((r["scenario"], r["arm"], r["seed"]))
    with OUT.open("a") as fh:
        for sc in F.SCENARIOS:
            for arm in F.ARMS:
                for seed in range(n_seeds):
                    if (sc, arm, seed) in done:
                        continue
                    r = F.run(arm, sc, seed)
                    fh.write(json.dumps({k: jsonable(v) for k, v in r.items()}) + "\n")
                    fh.flush()


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 40)
