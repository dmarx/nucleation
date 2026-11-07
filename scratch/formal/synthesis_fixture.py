# scratch/formal/synthesis_fixture.py: fire the SYNTHESIS scheme's rules and view on a throwaway record (ADR-tmptu1vn; DP-4)
# run: python3 scratch/formal/synthesis_fixture.py   (needs luria and jinja2; uses the repo's luria.yaml, writes only to a temp dir)
"""A fixture record, built from this repository's luria.yaml in a temporary
directory, holding a few components and six syntheses:

  S1  derived, demonstrated, admitted, Current, premise in force     -> clean
  S2  explanatory integration, admitted, Proposed                   -> clean
  S3  unadmitted, no route                                           -> clean, hidden from the view
  S4  Current, resting on a Proposed claim                           -> current_on_premise_not_in_force
  S5  a premise not among what it integrates                         -> premise_outside_integrates
  S6  derived, but warrant interpretive                              -> derived_not_demonstrated
  S7  Current, resting on the Proposed synthesis S2                  -> current_on_synthesis_not_current
  S8  a synthesis premise not among what it integrates               -> synthesis_premise_outside_integrates
  S9  Current but unadmitted                                         -> current_but_unadmitted
  S10 supposed and Current, on a Proposed premise                    -> clean: the premise rule exempts it
  S11 unadmitted but keeping a route                                 -> refused: route is forbidden once unadmitted

It runs `luria lint` on the fixture and checks each rule fires where it should
and nowhere else, then renders the current-account view, checks what it shows,
changes a component's status, and checks the change appears on the next render.
"""
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]

def entry(code, fm, body=""):
    lines = ["---"] + fm + ["---", "", f"# {code}: {dict(l.split(': ', 1) for l in fm if ': ' in l)['title'].strip(chr(39))}", "", body or "Fixture entry."]
    return "\n".join(lines) + "\n"

def claim(code, status, title):
    return entry(code, [f"status: {status}", f"title: '{title}'", "version: 1", "role: thesis",
                        "warrant: interpretive", "defeated_if: >-\n  a fixture case", "tags:\n- individuation",
                        "date: '2026-11-07'", "line:\n- distributed-agency", "summary: >-\n  Fixture claim."])

def term(code, title):
    return entry(code, ["status: Active", f"title: '{title}'", "version: 1", "tags:\n- individuation",
                        "date: '2026-11-07'", "line: distributed-agency", "summary: >-\n  Fixture term."])

def synthesis(code, title, status, admission, route, warrant, integrates, premises, role="thesis"):
    fm = [f"status: {status}", f"title: '{title}'", "version: 1", f"role: {role}", f"admission: {admission}"]
    if route:
        fm.append(f"route: {route}")
    fm += [f"warrant: {warrant}", "defeated_if: >-\n  a fixture case", "tags:\n- individuation",
           "date: '2026-11-07'", "line:\n- distributed-agency",
           "integrates:\n" + "".join(f"- {c}\n" for c in integrates).rstrip("\n")]
    if premises:
        fm.append("premises:\n" + "".join(f"- {c}\n" for c in premises).rstrip("\n"))
    fm.append("summary: >-\n  Fixture synthesis.")
    return entry(code, fm)

def build(root: Path):
    shutil.copy(REPO / "luria.yaml", root / "luria.yaml")
    (root / "record" / "views.d").mkdir(parents=True)
    shutil.copy(REPO / "record/views.d/current-account.md.j2", root / "record/views.d/")
    for d in ("claims.d", "terms.d", "syntheses.d"):
        (root / "record" / d).mkdir(parents=True, exist_ok=True)
    w = lambda rel, text: (root / rel).write_text(text)
    w("record/claims.d/CLAIM-001.md", claim("CLAIM-001", "Active", "An active fixture claim"))
    w("record/claims.d/CLAIM-002.md", claim("CLAIM-002", "Proposed", "A proposed fixture claim"))
    w("record/terms.d/TERM-001.md", term("TERM-001", "a fixture term"))
    S = [
        ("SYNTHESIS-001", "S1 derived and clean", "Current", "admitted", "derived", "demonstrated", ["CLAIM-001", "TERM-001"], ["CLAIM-001"]),
        ("SYNTHESIS-002", "S2 integration and clean", "Proposed", "admitted", "integration", "interpretive", ["CLAIM-001", "CLAIM-002"], ["CLAIM-002"]),
        ("SYNTHESIS-003", "S3 unadmitted", "Proposed", "unadmitted", None, "interpretive", ["CLAIM-001"], []),
        ("SYNTHESIS-004", "S4 current on a proposed premise", "Current", "admitted", "hypothesis", "interpretive", ["CLAIM-002"], ["CLAIM-002"]),
        ("SYNTHESIS-005", "S5 premise outside integrates", "Proposed", "admitted", "hypothesis", "interpretive", ["CLAIM-001"], ["CLAIM-002"]),
        ("SYNTHESIS-006", "S6 derived but interpretive", "Proposed", "admitted", "derived", "interpretive", ["CLAIM-001"], ["CLAIM-001"]),
        ("SYNTHESIS-007", "S7 current on a proposed synthesis", "Current", "admitted", "hypothesis", "interpretive", ["SYNTHESIS-002", "CLAIM-001"], ["SYNTHESIS-002", "CLAIM-001"]),
        ("SYNTHESIS-008", "S8 synthesis premise outside integrates", "Proposed", "admitted", "hypothesis", "interpretive", ["CLAIM-001"], ["SYNTHESIS-001"]),
        ("SYNTHESIS-009", "S9 current but unadmitted", "Current", "unadmitted", None, "interpretive", ["CLAIM-001"], []),
        ("SYNTHESIS-010", "S10 supposed and current on a proposed premise", "Current", "admitted", "hypothesis", "interpretive", ["CLAIM-002"], ["CLAIM-002"], "supposed"),
        ("SYNTHESIS-011", "S11 unadmitted but keeping a route", "Proposed", "unadmitted", "hypothesis", "interpretive", ["CLAIM-001"], []),
    ]
    for code, *rest in S:
        w(f"record/syntheses.d/{code}.md", synthesis(code, *rest))

def lint(root: Path) -> str:
    r = subprocess.run(["luria", "lint"], cwd=root, capture_output=True, text=True)
    return r.stdout + r.stderr

def render(root: Path) -> str:
    code = ("import os,sys; os.chdir(sys.argv[1]); from luria.config import current; from luria import views;"
            "print(views.render(current().views['current-account']))")
    r = subprocess.run([sys.executable, "-c", code, str(root)], capture_output=True, text=True)
    if r.returncode:
        raise SystemExit("render failed:\n" + r.stderr[-2000:])
    return r.stdout

def main():
    failures = []
    def check(ok, what):
        print(("ok   " if ok else "FAIL ") + what)
        if not ok:
            failures.append(what)
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        build(root)
        out = lint(root)
        lines = out.splitlines()
        expect = {"current_on_premise_not_in_force": "SYNTHESIS-004",
                  "premise_outside_integrates": "SYNTHESIS-005",
                  "derived_not_demonstrated": "SYNTHESIS-006",
                  "current_on_synthesis_not_current": "SYNTHESIS-007",
                  "synthesis_premise_outside_integrates": "SYNTHESIS-008",
                  "current_but_unadmitted": "SYNTHESIS-009"}
        def matches(rule):
            # the documents listed under "N match(es) of the pattern `rule`"
            found, on = [], False
            for l in lines:
                if f"of the pattern `{rule}`" in l:
                    on = True
                    continue
                if on and l.strip().startswith("record/"):
                    found.append(l.split(":")[0].rsplit("/", 1)[-1].removesuffix(".md"))
                    continue
                on = False
            return found
        for rule, code in expect.items():
            got = matches(rule)
            check(got == [code], f"{rule} fires on {code} and nothing else (got {got})")
        check(not any("SYNTHESIS-010" in l for r in ("current_on_premise_not_in_force",) for l in matches(r)),
              "a supposed Current synthesis on a Proposed premise is exempt from the premise rule")
        route_lines = [l for l in lines if "SYNTHESIS-011" in l and "route" in l]
        check(bool(route_lines), "an unadmitted synthesis that keeps a route is refused" + (f" ({route_lines[0].strip()[:90]})" if route_lines else ""))
        page = render(root)
        check("SYNTHESIS-001" in page and "SYNTHESIS-002" in page, "the view shows the admitted syntheses")
        check("SYNTHESIS-003" not in page and "SYNTHESIS-009" not in page, "the view hides the unadmitted syntheses")
        s10 = page[page.find("SYNTHESIS-010"):][:1500]
        check("SYNTHESIS-010" in page and "**Conditional.**" in s10, "the view labels a supposed synthesis as conditional")
        check("| TERM |" in page and "| CLAIM |" in page, "the view shows each component's kind")
        claim_file = root / "record/claims.d/CLAIM-001.md"
        claim_file.write_text(claim_file.read_text().replace("status: Active", "status: Superseded", 1))
        page2 = render(root)
        row = [l for l in page2.splitlines() if l.startswith("| [CLAIM-001]") or l.startswith("| CLAIM-001")]
        check(bool(row) and "Superseded" in row[0], "a component's status change shows on the next render")
        if failures:
            print("\n--- lint output (tail) ---\n" + "\n".join(lines[-40:]))
    print(f"\n{len(failures)} failure(s)")
    sys.exit(1 if failures else 0)

if __name__ == "__main__":
    main()
