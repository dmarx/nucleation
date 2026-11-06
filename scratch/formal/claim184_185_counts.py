# scratch/formal/claim184_185_counts.py: the twenty-sixth status review's counts for CLAIM-184 (citations of Superseded CLAIMs and TERMs after retirement) and CLAIM-185 (CASE-183's inbound references per code) (run: python3 -I scratch/formal/claim184_185_counts.py record --control)
"""Pass 26, cluster J. Two counts from a Luria record tree (read-only).

A. CLAIM-184: citations of each Superseded CLAIM and TERM made after its
   retirement, split into those acknowledged by an inactive-ok directive
   naming the code in the citing file and those not.
B. CLAIM-185 / CASE-183: inbound references per code (distinct citing
   files, self excluded), by scheme, with the share of codes cited by none.

Usage: python3 -I scratch/formal/claim184_185_counts.py RECORD_DIR [--control]
"""
import sys, os, re, glob, collections
import yaml

CODE = re.compile(r'\b(CLAIM|TERM|THEORY|LIT|NOTE|CASE|QUESTION|ARG|ADR|DP|CHANGELOG|CURATION|WB|WORKBENCH)-(\d+)\b')
NOTE_H = re.compile(r'^## Note of (\d{4}-\d{2}-\d{2})')
ACK = re.compile(r'<!--\s*inactive-ok(?:-file|-block)?:\s*(.*?)-->', re.S)
HIST_FIELDS = {'superseded_by', 'supersedes', 'formerly', 'history'}

def load(root):
    ents = {}
    for f in glob.glob(os.path.join(root, '**', '*.md'), recursive=True):
        t = open(f, encoding='utf-8').read()
        if not t.startswith('---'):
            continue
        parts = t.split('---', 2)
        try:
            fm = yaml.safe_load(parts[1])
        except Exception:
            continue
        if not isinstance(fm, dict):
            continue
        name = os.path.basename(f)[:-3]
        ents[name] = dict(path=f, fm=fm, body=parts[2], text=t)
    return ents

def dstr(x):
    return str(x) if x is not None else ''

def citations(e):
    """Yield (code, date, where) for each citation in entry e.
    Frontmatter relations are dated at the entry's date; history notes at
    their own date; body text at the latest '## Note of' heading above it,
    else the entry's date. Superseded_by/supersedes/formerly are skipped."""
    fm = e['fm']; base = dstr(fm.get('date'))
    for k, v in fm.items():
        if k in HIST_FIELDS:
            continue
        vals = v if isinstance(v, list) else [v]
        for x in vals:
            for m in CODE.finditer(str(x)):
                yield m.group(0), base, 'fm:' + k
    for h in fm.get('history') or []:
        if isinstance(h, dict):
            for m in CODE.finditer(str(h.get('note', ''))):
                yield m.group(0), dstr(h.get('date')), 'history'
    cur = base
    for line in e['body'].splitlines():
        mh = NOTE_H.match(line)
        if mh:
            cur = mh.group(1)
        if line.lstrip().startswith('<!--'):
            continue
        for m in CODE.finditer(line):
            yield m.group(0), cur, 'body'

def acked(e):
    s = set()
    for m in ACK.finditer(e['text']):
        s.update(c.group(0) for c in CODE.finditer(m.group(1).split('—')[0]))
    return s

def retire_date(code, ents):
    fm = ents[code]['fm']
    ds = [dstr(h.get('date')) for h in fm.get('history') or []
          if isinstance(h, dict) and re.search(r'[Ss]upersed', str(h.get('note', '')))]
    if ds:
        return max(ds), 'history'
    succ = fm.get('superseded_by') or []
    succ = succ if isinstance(succ, list) else [succ]
    sd = [dstr(ents[s]['fm'].get('date')) for s in succ if s in ents]
    if sd:
        return min(sd), 'successor-date'
    return dstr(fm.get('date')), 'own-date'

def count_a(ents):
    sup = sorted(c for c, e in ents.items()
                 if c.split('-')[0] in ('CLAIM', 'TERM') and e['fm'].get('status') == 'Superseded')
    rows = []
    for c in sup:
        rd, how = retire_date(c, ents)
        succ = ents[c]['fm'].get('superseded_by') or []
        succ = set(succ if isinstance(succ, list) else [succ])
        after_ack = after_un = before = 0
        files_un = set(); where_un = collections.Counter()
        for n, e in ents.items():
            if n == c:
                continue
            ak = acked(e)
            seen = set()
            for code, d, where in citations(e):
                if code != c or (d, where) in seen:
                    continue
                seen.add((d, where))
                if d and d > rd:
                    if code in ak:
                        after_ack += 1
                    else:
                        after_un += 1; files_un.add(n); where_un[where] += 1
                else:
                    before += 1
        rows.append((c, rd, how, before, after_ack, after_un, sorted(files_un), dict(where_un), sorted(succ)))
    return rows

def count_b(ents):
    inbound = collections.defaultdict(set)
    inbound_nopaper = collections.defaultdict(set)
    for n, e in ents.items():
        for code, d, where in citations(e):
            if code == n or code not in ents:
                continue
            inbound[code].add(n)
            if not (where == 'fm:paper'):
                inbound_nopaper[code].add(n)
    by = collections.defaultdict(list)
    for c, e in ents.items():
        sch = c.split('-')[0]
        by[(sch, str(e['fm'].get('status')))].append(len(inbound_nopaper.get(c, ())))
    return inbound, inbound_nopaper, by

def med(xs):
    xs = sorted(xs); n = len(xs)
    return xs[n // 2] if n % 2 else (xs[n // 2 - 1] + xs[n // 2]) / 2

def report(root):
    ents = load(root)
    print(f'entries loaded: {len(ents)}')
    rows = count_a(ents)
    print('\nA. Superseded CLAIM/TERM: code retired(how) before after_acked after_unacked')
    tot = [0, 0, 0]
    for r in rows:
        tot[0] += r[3]; tot[1] += r[4]; tot[2] += r[5]
        print(f'  {r[0]:10s} {r[1]} ({r[2]}) {r[3]:3d} {r[4]:3d} {r[5]:3d}  {r[7]}  unacked-in:{r[6][:8]}')
    print(f'  TOTAL superseded={len(rows)} before={tot[0]} after_acked={tot[1]} after_unacked={tot[2]}')
    print(f'  codes with any after-retirement citation: {sum(1 for r in rows if r[4]+r[5])}; with unacked: {sum(1 for r in rows if r[5])}')
    _, inb, by = count_b(ents)
    print('\nB. inbound references per code (distinct citing files, NOTE paper: link excluded)')
    print('  scheme status n mean median zero_share')
    for (s, st), xs in sorted(by.items()):
        if len(xs) < 3:
            continue
        z = sum(1 for x in xs if x == 0) / len(xs)
        print(f'  {s:9s} {st:12s} {len(xs):5d} {sum(xs)/len(xs):6.2f} {med(xs):5} {z:6.2f}')

def control():
    import tempfile
    d = tempfile.mkdtemp()
    os.makedirs(os.path.join(d, 'claims.d')); os.makedirs(os.path.join(d, 'literature.d'))
    def w(name, fm, body):
        open(os.path.join(d, 'claims.d' if name.startswith('CLAIM') else 'literature.d', name + '.md'), 'w').write(
            '---\n' + yaml.safe_dump(fm) + '---\n' + body)
    w('CLAIM-001', dict(status='Superseded', date='2026-10-01', superseded_by=['CLAIM-002'],
        history=[dict(version=2, date='2026-10-05', note='Superseded by CLAIM-002.')]), '# x\n')
    w('CLAIM-002', dict(status='Active', date='2026-10-05', supersedes=['CLAIM-001']), '# y\nCLAIM-001 before.\n')
    w('CLAIM-003', dict(status='Active', date='2026-10-03', rests_on=['CLAIM-001']),
      '# z\n## Note of 2026-10-07: later\nCLAIM-001 again, unacked.\n')
    w('CLAIM-004', dict(status='Active', date='2026-10-09'),
      '<!-- inactive-ok-file: CLAIM-001 — Superseded; history -->\n# w\nCLAIM-001 as history. LIT-001.\n')
    w('LIT-001', dict(status='Active', date='2026-10-01'), '# l\n')
    w('LIT-002', dict(status='Active', date='2026-10-01'), '# l2\n')
    ents = load(d)
    r = count_a(ents)[0]
    # expected: retired 2026-10-05 (history); before: CLAIM-002 body (10-05, not after) + CLAIM-003 fm (10-03) = 2;
    # after acked: CLAIM-004 = 1; after unacked: CLAIM-003 note of 10-07 = 1; supersedes field skipped.
    exp = ('CLAIM-001', '2026-10-05', 'history', 2, 1, 1)
    assert r[:6] == exp, (r, exp)
    _, inb, _ = count_b(ents)
    assert len(inb['LIT-001']) == 1 and len(inb.get('LIT-002', ())) == 0, inb
    assert inb['CLAIM-001'] == {'CLAIM-002', 'CLAIM-003', 'CLAIM-004'}, inb['CLAIM-001']
    print('control: PASS', r[:6])

if __name__ == '__main__':
    if '--control' in sys.argv:
        control()
    report(sys.argv[1])
