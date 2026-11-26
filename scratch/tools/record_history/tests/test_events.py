# scratch/tools/record_history/tests/test_events.py
from record_history.entries import Schema
from record_history.events import alias_map, final_state, replay
from record_history.gitlog import Change, Commit

SCHEMA = Schema.from_config({"schemes": {"CLAIM": {"dir": "record/claims.d",
    "references": {"rests_on": {"scheme": "CLAIM"}}}}})


class FakeBlobs:
    def __init__(self, blobs):
        self.blobs = blobs

    def read(self, sha):
        return self.blobs[sha]


def doc(status, rests=(), body="Body."):
    rel = "".join(f"\n- {c}" for c in rests)
    return f"---\nstatus: {status}\ntitle: T\nrests_on:{rel or ' []'}\n---\n{body}\n"


BLOBS = FakeBlobs({
    "a1": doc("Proposed", body="Body. CLAIM-tmpb"),
    "b1": doc("Proposed", rests=["CLAIM-tmpa"]),
    "a2": doc("Proposed", body="Body. [CLAIM-2](x.md)"),
    "a3": doc("Active", body="Body. CLAIM-2 New line."),
})
P = "record/claims.d/"
COMMITS = [
    Commit("c1", 100, "Owner", "file a", [Change("A", None, "a1", None, P + "CLAIM-tmpa.md")]),
    Commit("c2", 200, "Owner", "file b", [Change("A", None, "b1", None, P + "CLAIM-tmpb.md")]),
    Commit("c3", 300, "github-actions[bot]", "Promote", [
        Change("R", "a1", "a2", P + "CLAIM-tmpa.md", P + "CLAIM-1.md"),
        Change("R", "b1", "b1", P + "CLAIM-tmpb.md", P + "CLAIM-2.md")]),
    Commit("c4", 400, "Owner", "revise 1", [Change("M", "a2", "a3", P + "CLAIM-1.md", P + "CLAIM-1.md")]),
]


def test_alias_map_from_renames_and_formerly():
    alias = alias_map(COMMITS, {"CLAIM-9": ["CLAIM-tmpz"]})
    assert alias == {"CLAIM-tmpa": "CLAIM-1", "CLAIM-tmpb": "CLAIM-2", "CLAIM-tmpz": "CLAIM-9"}


def test_replay_keys_events_by_final_code_and_finds_concretization_mechanical():
    alias = alias_map(COMMITS)
    rows = replay(COMMITS, BLOBS, SCHEMA, alias)
    by = [(r["commit"], r["code"], r["kind"]) for r in rows]
    assert ("c1", "CLAIM-1", "created") in by
    assert ("c2", "CLAIM-2", "relation_add") in by
    assert ("c3", "CLAIM-1", "mechanical") in by
    assert not any(c == "c3" and code == "CLAIM-2" for c, code, _ in by)  # identical content
    assert {k for c, _, k in by if c == "c4"} == {"status", "prose"}
    assert all(r["breadth"] == 2 for r in rows if r["commit"] == "c3")
    edge = next(r for r in rows if r["kind"] == "relation_add")
    assert edge["target"] == "CLAIM-1"


def test_final_state_tracks_status_and_edges():
    rows = replay(COMMITS, BLOBS, SCHEMA, alias_map(COMMITS))
    st = final_state(rows)
    assert st["CLAIM-1"]["status"] == "Active"
    assert st["CLAIM-2"]["edges"] == {("rests_on", "CLAIM-1")}
