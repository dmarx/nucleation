# scratch/tools/record_history/tests/test_profile.py
from record_history.profile import Params, profiles, quadrant

DAY = 86400


def ev(t, code, kind, commit=None, bot=False, breadth=1, **kw):
    return {"commit": commit or f"c{t}{code}{kind}", "time": t * DAY, "bot": bot,
            "breadth": breadth, "code": code, "scheme": code.split("-")[0], "kind": kind, **kw}


ROWS = [
    ev(0, "CLAIM-1", "created", status="Proposed"),
    ev(1, "CLAIM-1", "prose", churn=4),
    ev(2, "CLAIM-1", "mechanical", bot=True),
    ev(5, "CLAIM-2", "created", commit="k2", status="Proposed"),
    ev(5, "CLAIM-2", "relation_add", commit="k2", field="rests_on", target="CLAIM-1"),
    ev(40, "CLAIM-3", "created", commit="k3", status="Proposed"),
    ev(40, "CLAIM-3", "relation_add", commit="k3", field="rests_on", target="CLAIM-1"),
    ev(50, "CLAIM-1", "prose", churn=900, breadth=1000),  # a sweep: maintenance
    ev(55, "CLAIM-3", "prose", churn=2),
    ev(58, "CLAIM-4", "created", commit="k4", status="Proposed"),
    ev(58, "CLAIM-4", "relation_add", commit="k4", field="rests_on", target="CLAIM-1"),
    ev(59, "CLAIM-4", "relation_remove", field="rests_on", target="CLAIM-1"),
]
P = Params(now=60 * DAY, sweep_breadth=250, reactivation_days=14)


def test_profile_of_a_claim_that_others_build_on():
    p = profiles(ROWS, P)["CLAIM-1"]
    assert p["created_day"] == 0 and p["age_days"] == 60
    assert p["prose_revisions"] == 1 and p["prose_churn"] == 4
    assert p["days_since_prose"] == 59  # the sweep at day 50 does not count
    assert p["maintenance_commits"] == 2  # bot repair and the sweep
    assert p["in_degree"] == 2  # CLAIM-4's edge was removed
    assert p["new_dependents_30d"] == 2  # CLAIM-3 (day 40) and CLAIM-4 (day 58)
    assert p["new_dependents_7d"] == 1
    assert p["latency_days"] == 5
    assert p["reactivations"] == 2  # quiet days 5-40 and 40-58
    assert p["neighbourhood_30d"] == 2  # CLAIM-3 created + revised, live neighbour only


def test_profile_of_an_unused_claim():
    p = profiles(ROWS, P)["CLAIM-2"]
    assert p["latency_days"] is None and p["in_degree"] == 0
    assert p["out_degree"] == 1


def test_quadrant_labels():
    assert quadrant(days_since_prose=30, new_dependents=3, stable_days=14, generative=1) == "established anchor"
    assert quadrant(2, 3, 14, 1) == "developing nucleus"
    assert quadrant(2, 0, 14, 1) == "unresolved churn"
    assert quadrant(30, 0, 14, 1) == "dormant structure"
