# scratch/tools/record_history/tests/test_profile.py
from record_history.profile import Params, profiles, quadrant

DAY = 86400


def ev(t, code, kind, commit=None, bot=False, breadth=1, **kw):
    return {"commit": commit or f"c{t}{code}{kind}", "time": t * DAY, "bot": bot,
            "breadth": breadth, "code": code, "scheme": code.split("-")[0], "kind": kind, **kw}


ROWS = [
    ev(0, "CLAIM-1", "created", status="Proposed"),
    ev(1, "CLAIM-1", "body", added=2, removed=2),
    ev(2, "CLAIM-1", "mechanical", bot=True),
    ev(5, "CLAIM-2", "created", commit="k2", status="Proposed"),
    ev(5, "CLAIM-2", "relation_add", commit="k2", field="rests_on", target="CLAIM-1"),
    ev(40, "CLAIM-3", "created", commit="k3", status="Proposed"),
    ev(40, "CLAIM-3", "relation_add", commit="k3", field="rests_on", target="CLAIM-1"),
    ev(50, "CLAIM-1", "statement", breadth=1000),  # a sweep: maintenance
    ev(55, "CLAIM-3", "body", added=1, removed=1),
    ev(58, "CLAIM-4", "created", commit="k4", status="Proposed"),
    ev(58, "CLAIM-4", "relation_add", commit="k4", field="rests_on", target="CLAIM-1"),
    ev(59, "CLAIM-4", "relation_remove", field="rests_on", target="CLAIM-1"),
]
P = Params(now=60 * DAY, sweep_breadth=250, reactivation_days=14)


def test_profile_of_a_claim_that_others_build_on():
    p = profiles(ROWS, P)["CLAIM-1"]
    assert p["created_day"] == 0 and p["age_days"] == 60
    assert p["revisions"] == 1 and p["body_churn"] == 4
    assert p["days_since_revision"] == 59  # the sweep at day 50 does not count
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
    assert quadrant(days_since_revision=30, new_dependents=3, stable_days=14, generative=1) == "established anchor"
    assert quadrant(2, 3, 14, 1) == "developing nucleus"
    assert quadrant(2, 0, 14, 1) == "unresolved churn"
    assert quadrant(30, 0, 14, 1) == "dormant structure"


def test_a_deleted_entry_loses_its_edges_and_is_flagged():
    rows = ROWS + [ev(59, "CLAIM-3", "deleted")]
    ps = profiles(rows, P)
    assert ps["CLAIM-1"]["in_degree"] == 1  # only CLAIM-2 is left
    assert ps["CLAIM-3"]["deleted"] is True
    assert ps["CLAIM-1"]["deleted"] is False


def test_sweep_needs_breadth_and_few_creations():
    from record_history.profile import sweep_commits
    rows = [ev(1, f"CLAIM-{i}", "title", commit="s", breadth=300) for i in range(300)]
    rows += [ev(2, f"CLAIM-{i}", "created", commit="f", breadth=300) for i in range(100)]
    rows += [ev(2, f"CLAIM-{i}", "body", commit="f", breadth=300, added=1) for i in range(100, 300)]
    assert sweep_commits(rows, breadth=250, created_share=0.1) == {"s"}


def test_a_dated_note_does_not_reset_revision_stability():
    rows = [ev(0, "CLAIM-9", "created", commit="a", status="Proposed"),
            ev(10, "CLAIM-9", "body", commit="b", added=1, removed=1),
            ev(50, "CLAIM-9", "note", commit="c", added=5, removed=0)]
    p = profiles(rows, P)["CLAIM-9"]
    assert p["days_since_revision"] == 50
    assert (p["revisions"], p["notes"]) == (1, 1)


def test_tip_state_overrides_replayed_present_state():
    tip = {"CLAIM-1": set(), "CLAIM-2": {("rests_on", "CLAIM-1")}, "CLAIM-3": set(),
           "CLAIM-4": {("rests_on", "CLAIM-1")}}  # the replay lost CLAIM-4's edge
    ps = profiles(ROWS + [ev(59, "CLAIM-3", "deleted")], P, tip=tip)
    assert ps["CLAIM-3"]["deleted"] is False  # live at the tip
    assert ps["CLAIM-1"]["in_degree"] == 2  # CLAIM-2 and CLAIM-4, from the tip
    assert ps["CLAIM-1"]["new_dependents_30d"] == 1  # CLAIM-4 (day 58); CLAIM-3's edge is gone
