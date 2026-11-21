# scratch/tools/adoption_signals.py
# Evidence that a Proposed ADR is functionally adopted, derived from the tree
# on each pass and kept nowhere (the adoption-review skill, step 1).
# Usage: python3 -I scratch/tools/adoption_signals.py <repo root> <out.json> [YYYY-MM-DD]
import re, sys, yaml, pathlib, datetime as dt, subprocess, json
root = pathlib.Path(sys.argv[1])
today = dt.date.fromisoformat(sys.argv[3]) if len(sys.argv) > 3 else dt.date.today()
def fm(p):
    t = p.read_text(); e = t.index('\n---\n', 4); return yaml.safe_load(t[4:e]), t
adrs = {}
for p in sorted((root/'record/decisions.d').glob('ADR-*.md')):
    m, t = fm(p); code = p.stem
    if str(m.get('status')).strip("'") != 'Proposed': continue
    adrs[code] = dict(title=m['title'], date=str(m.get('date')), number=m.get('number'), formerly=m.get('formerly') or [])
files = [p for p in root.rglob('*') if p.is_file() and '.git' not in p.parts and not str(p.relative_to(root)).startswith('docs/') and p.suffix in ('.md','.yml','.yaml','.py','.sh','.j2')]
texts = {str(p.relative_to(root)): p.read_text(errors='ignore') for p in files}
rows = []
for code, a in adrs.items():
    names = [code] + list(a['formerly'])
    pat = re.compile(r'\b(' + '|'.join(map(re.escape, names)) + r')\b')
    cites = excuses = adopt_excuses = 0; where = {'CLAUDE.md':0,'skills':0,'workflows':0,'luria.yaml':0}
    citing_files = 0
    for path, t in texts.items():
        if path == f'record/decisions.d/{code}.md': continue
        n = len(pat.findall(t))
        if not n: continue
        citing_files += 1; cites += n
        if path == 'CLAUDE.md': where['CLAUDE.md'] += n
        elif path.startswith('.claude/skills'): where['skills'] += n
        elif path.startswith('.github'): where['workflows'] += n
        elif path == 'luria.yaml': where['luria.yaml'] += n
        for line in t.splitlines():
            if 'inactive-ok' in line and pat.search(line):
                excuses += 1
                if re.search(r'until the owner adopts|the decision (this|these|that) .*(follow|carr|appl)|applied|first application', line, re.I): adopt_excuses += 1
    try: age = (today - dt.date.fromisoformat(a['date'].strip("'"))).days
    except Exception: age = None
    rows.append(dict(code=code, age=age, files=citing_files, cites=cites, excuses=excuses, adopt=adopt_excuses, **where, title=a['title'][:110]))
rows.sort(key=lambda r: (-(r['CLAUDE.md']>0) - (r['skills']>0) - (r['workflows']>0), -r['adopt'], -r['files']))
json.dump(rows, open(sys.argv[2],'w'), indent=1)
print(f"{'code':14} {'age':>4} {'files':>5} {'exc':>4} {'adopt':>5} {'CLMD':>4} {'skl':>3} {'wf':>3} {'yaml':>4}  title")
for r in rows:
    print(f"{r['code']:14} {r['age'] if r['age'] is not None else '?':>4} {r['files']:>5} {r['excuses']:>4} {r['adopt']:>5} {r['CLAUDE.md']:>4} {r['skills']:>3} {r['workflows']:>3} {r['luria.yaml']:>4}  {r['title']}")
