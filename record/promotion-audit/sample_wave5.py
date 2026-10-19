# record/promotion-audit/sample_wave5.py
"""List wave 5 of the promotion audit and draw a fixed-rule sample (batch 022).

Wave 5 is the broad interpretive and synthesis claims. NOTES (batch 007) says
to sample it rather than rank it, because no textual heuristic has been shown
to predict its yield. The population:

  - Proposed CLAIMs with `warrant: interpretive`, any role;
  - Proposed THEORYs with no `mathematics` tag whose `source` names at least
    three distinct LIT codes: a synthesis across readings, not one paper's
    theorem or measurement.

Codes already a candidate or requeued in queue.yaml are left out. The sample
sorts the population by scheme and number and takes every k-th code, with
k = len(population) // n and the first at k // 2. The sample orders review; it
decides nothing (ADR-047). Run from the repository root on a freshly fetched
origin/main:

    python3 record/promotion-audit/sample_wave5.py
"""
import re
from pathlib import Path

import fire
import yaml
from loguru import logger

HERE = Path(__file__).parent
RECORD = HERE.parent
LIT = re.compile(r"\bLIT-\d+\b")


def front_matter(path: Path) -> dict:
    m = re.match(r"---\n(.*?)\n---", path.read_text(), re.S)
    return yaml.safe_load(m.group(1)) or {} if m else {}


def sort_codes(codes: list[str]) -> list[str]:
    def key(code: str) -> tuple[str, int]:
        scheme, num = code.rsplit("-", 1)
        return scheme, int(num)
    return sorted(codes, key=key)


def queued(queue: Path) -> set[str]:
    q = yaml.safe_load(queue.read_text()) or {}
    return {c["code"] for c in (q.get("candidates") or []) + (q.get("requeue") or [])}


def population(record: Path, queue: Path) -> list[str]:
    skip = queued(queue)
    found = []
    for p in (record / "claims.d").glob("CLAIM-*.md"):
        d = front_matter(p)
        if d.get("status") == "Proposed" and d.get("warrant") == "interpretive":
            found.append(p.stem)
    for p in (record / "theory.d").glob("THEORY-*.md"):
        d = front_matter(p)
        if d.get("status") != "Proposed" or "mathematics" in (d.get("tags") or []):
            continue
        if len(set(LIT.findall(str(d.get("source") or "")))) >= 3:
            found.append(p.stem)
    return sort_codes([c for c in found if c not in skip])


def roots(record: Path, queue: Path) -> list[str]:
    """Population members none of whose `rests_on` premises is a Proposed
    interpretive CLAIM (batch 030). A queued premise still counts: it is
    still Proposed. Deciding roots first keeps a sample from drawing claims
    whose own premises block them (batch 022)."""
    blocking = set()
    rests: dict[str, list[str]] = {}
    for p in (record / "claims.d").glob("CLAIM-*.md"):
        d = front_matter(p)
        rests[p.stem] = list(d.get("rests_on") or [])
        if d.get("status") == "Proposed" and d.get("warrant") == "interpretive":
            blocking.add(p.stem)
    return [c for c in population(record, queue) if not blocking & set(rests.get(c, []))]


def sample(codes: list[str], n: int) -> list[str]:
    if len(codes) <= n:
        return list(codes)
    k = len(codes) // n
    return [codes[k // 2 + i * k] for i in range(n)]


def main(n: int = 5, record: str = str(RECORD), queue: str = str(HERE / "queue.yaml"),
         roots_only: bool = False) -> None:
    pop = population(Path(record), Path(queue))
    frame = roots(Path(record), Path(queue)) if roots_only else pop
    picked = sample(frame, n)
    k = len(frame) // n if len(frame) > n else 1
    logger.info(f"population {len(pop)} (CLAIM {sum(c.startswith('CLAIM') for c in pop)}, "
                f"THEORY {sum(c.startswith('THEORY') for c in pop)}); frame {len(frame)}; "
                f"k = {k}, start = {k // 2}")
    print(yaml.safe_dump({"population": len(pop), "roots_only": roots_only, "frame": len(frame),
                          "k": k, "start": k // 2, "sample": picked}, sort_keys=False))


if __name__ == "__main__":
    fire.Fire(main)
