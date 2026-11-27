# scratch/tools/record_history/tests/test_lead199.py
from record_history.lead199 import to_lead199


def ev(t, code, kind, commit="c", author="Owner", subject="s", breadth=1, **kw):
    return {"commit": commit, "time": t, "bot": "[bot]" in author, "author": author,
            "subject": subject, "breadth": breadth, "code": code,
            "scheme": code.split("-")[0], "kind": kind, **kw}


def test_export_matches_lead199_formats():
    rows = [ev(1, "CLAIM-1", "created", commit="a", status="Proposed"),
            ev(2, "CLAIM-2", "created", commit="b", status="Proposed"),
            ev(2, "CLAIM-2", "relation_add", commit="b", field="rests_on", target="CLAIM-1"),
            ev(2, "ARG-1", "relation_add", commit="b", field="concludes", target="CLAIM-1"),
            ev(3, "CLAIM-1", "body", commit="d", added=1, removed=1),
            ev(3, "CLAIM-1", "status", commit="d", old="Proposed", new="Active"),
            ev(4, "CLAIM-1", "note", commit="e", added=3, removed=0),
            ev(5, "CLAIM-1", "mechanical", commit="f", author="github-actions[bot]"),
            ev(6, "CLAIM-2", "relation_remove", commit="g", field="rests_on", target="CLAIM-1")]
    tip = {"CLAIM-1": set(), "CLAIM-2": set()}
    status = {"CLAIM-1": "Active", "CLAIM-2": "Proposed"}
    revs, edges, pop = to_lead199(rows, tip, status, {"CLAIM-tmpz": "CLAIM-1"})
    kinds = [(r["claim"], r["kind"]) for r in revs]
    assert kinds == [("CLAIM-1", "created"), ("CLAIM-2", "created"), ("CLAIM-1", "substantive"),
                     ("CLAIM-1", "nonsubstantive"), ("CLAIM-1", "mechanical"),
                     ("CLAIM-2", "nonsubstantive")]
    sub = revs[2]
    assert sub["status_change"] and not sub["title_change"] and sub["n_claims_in_commit"] == 1
    assert [(e["src"], e["tgt"], e["op"]) for e in edges] == [("CLAIM-2", "CLAIM-1", 1), ("CLAIM-2", "CLAIM-1", -1)]
    assert pop == {"CLAIM-1": {"status": "Active", "aliases": ["CLAIM-tmpz"]},
                   "CLAIM-2": {"status": "Proposed", "aliases": []}}
