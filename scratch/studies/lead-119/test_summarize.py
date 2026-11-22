import importlib.util, json, os

spec = importlib.util.spec_from_file_location("summarize", os.path.join(os.path.dirname(__file__), "summarize.py"))
s = importlib.util.module_from_spec(spec)
spec.loader.exec_module(s)


def mk(arm, H, A):
    return {"arm": arm, "H": H, "A": A, "SYS": 0, "vendor": 0}


def test_verdict_holds():
    i = s.rates([mk("internal", 2, 2)] * 9 + [mk("internal", 3, 3)])
    e = s.rates([mk("independent", 4, 5)] * 8 + [mk("independent", 2, 2)] * 2)
    assert s.verdict(i, e) == "prediction holds in the pilot"


def test_verdict_defeater():
    i = s.rates([mk("internal", 4, 4)] * 6 + [mk("internal", 2, 2)] * 4)
    e = s.rates([mk("independent", 4, 4)] * 7 + [mk("independent", 2, 2)] * 3)
    assert s.verdict(i, e) == "defeater's direction met"


def test_load_supersedes(tmp_path):
    p = tmp_path / "c.jsonl"
    p.write_text(json.dumps({"id": "X", "H": 1}) + "\n" + json.dumps({"id": "X", "H": 3}) + "\n")
    assert s.load(p)[0]["H"] == 3
