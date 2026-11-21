# scratch/formal/analytics/census_nodes.py
"""Hamilton nodes: the hand-coded decision census (decision-census/census.py).

The census is coded by hand, so it cannot be recomputed for decisions filed
after it. `census_coverage` says how many decisions the record now holds that
the census has not coded, and `census_status_drift` which coded decisions
have changed status since they were coded, so staleness is visible beside
the figures. Input: `census_dir` (the directory holding batch-*.json).
"""
from hamilton.function_modifiers import tag

import gitread  # noqa: F401  (puts scratch/formal and decision-census on sys.path)
import census  # noqa: E402  (decision-census/census.py)


@tag(role="intermediate")
def census_rows(census_dir: str) -> list[dict]:
    return census.load_rows(census_dir)


@tag(role="intermediate")
def census_recode(census_dir: str) -> dict[str, dict]:
    return census.load_recode(census_dir)


@tag(feeds="§13.1, §15.1, §15.3, §15.4, §16.1", section="census")
def census_summary(census_rows: list[dict]) -> dict:
    """The census tables: regime, component, operation, residue, outcome, by period, migrations, harm."""
    return census.summary(census_rows)


@tag(feeds="§13.1 (agreement table), §15.1", section="census")
def census_agreement(census_rows: list[dict], census_recode: dict[str, dict]) -> dict:
    """Raw agreement and Cohen's kappa per field over the decisions coded twice."""
    return census.agreement(census_rows, census_recode)


def _is_decision(e: dict) -> bool:
    return e["scheme"] == "ADR"


@tag(feeds="staleness of §§13-16", section="census")
def census_coverage(census_rows: list[dict], entries: list[dict]) -> dict:
    """Decisions in record/decisions.d at the snapshot against those the census coded."""
    coded = {r["adr"] for r in census_rows}
    held = {e["code"] for e in entries if _is_decision(e)}
    uncoded = sorted(held - coded)
    return {
        "decisions_in_record": len(held),
        "decisions_coded": len(coded),
        "uncoded_count": len(uncoded),
        "uncoded": uncoded,
        "coded_not_in_record": sorted(coded - held),
        "last_coded_date": max((r["date"] for r in census_rows), default=None),
    }


@tag(feeds="staleness of §14.1", section="census")
def census_status_drift(census_rows: list[dict], entries: list[dict]) -> dict:
    """Coded decisions whose status at the snapshot differs from the status the census recorded."""
    now = {e["code"]: str(e["fm"].get("status")) for e in entries if _is_decision(e)}
    moved = {r["adr"]: {"coded": r.get("status"), "now": now[r["adr"]]}
             for r in census_rows if r["adr"] in now and str(r.get("status")) != now[r["adr"]]}
    return {"changed_count": len(moved), "changed": moved}
