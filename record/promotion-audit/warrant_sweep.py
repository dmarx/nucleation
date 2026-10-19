# record/promotion-audit/warrant_sweep.py
"""List Proposed interpretive CLAIMs whose defeat condition sounds empirical (batch 028).

ADR-043 gives each CLAIM a warrant: demonstrated, empirical or interpretive. An
interpretive claim stands or falls on a reading, so a `defeated_if` that names
an observation, a study, a measurement or a reception test is a sign the warrant
may be wrong. That mirrors NOTES pattern 1 (a demonstrated warrant over an
empirical defeater). Batch 022 counted such claims by hand; this makes the count
repeatable. The list orders review only; it decides nothing (ADR-047).

Cues, matched case-insensitively in `defeated_if`, name an empirical procedure or its
result: study or studies, survey, experiment, sample, replication, empirical, finding(s),
measured or measurement, observed or observation, corpus, statistic(s), correlation,
reception study, independent judges. Generic words (evidence, test, rate, data, found)
were tried and dropped: they fire on readings as often as on observations.
"Empirical model" is excluded: in the contextuality literature it is a term of art
for a family of distributions, and says nothing about whether anything was observed.

A hit is not a misclassification. ADR-043's pilot reads an empirical claim with
no observation under it as interpretive (its note on CLAIM-117), so most hits are
correctly interpretive; review looks for defeaters that do not fit the claim.

    python3 record/promotion-audit/warrant_sweep.py
"""
import re
from pathlib import Path

import fire
import yaml
from loguru import logger

HERE = Path(__file__).parent
RECORD = HERE.parent
CUES = (
    r"stud(y|ies)", r"survey", r"experiment\w*", r"sample[ds]?", r"replicat\w*", r"empirical(?!\s+models?\b)\w*",
    r"findings?", r"measure(d|ment)\w*", r"observ(ed|ation)\w*", r"corpus", r"statistic\w*",
    r"correlat\w*", r"reception stud\w*", r"independent judges",
)
CUE = re.compile(r"\b(" + "|".join(CUES) + r")\b", re.I)


def front_matter(path: Path) -> dict:
    m = re.match(r"---\n(.*?)\n---", path.read_text(), re.S)
    return (yaml.safe_load(m.group(1)) or {}) if m else {}


def empirical_cues(text: str) -> list[str]:
    return sorted({m.group(1).lower() for m in CUE.finditer(text or "")})


def sweep(record: Path) -> list[str]:
    found = []
    for p in (record / "claims.d").glob("CLAIM-*.md"):
        d = front_matter(p)
        if d.get("status") != "Proposed" or d.get("warrant") != "interpretive":
            continue
        if empirical_cues(str(d.get("defeated_if") or "")):
            found.append(p.stem)
    return sorted(found, key=lambda c: int(c.rsplit("-", 1)[1]))


def main(record: str = str(RECORD)) -> None:
    codes = sweep(Path(record))
    logger.info(f"{len(codes)} Proposed interpretive CLAIMs with empirical-sounding defeaters")
    for c in codes:
        print(c)


if __name__ == "__main__":
    fire.Fire(main)
