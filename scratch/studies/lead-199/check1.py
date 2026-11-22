import json, collections, os
D = os.path.dirname(os.path.abspath(__file__))
E = json.load(open(f'{D}/edges.json')); R = json.load(open(f'{D}/revisions.json')); P = json.load(open(f'{D}/population.json'))
st = {}
for e in sorted(E, key=lambda e: e['t']): st[(e['src'], e['tgt'])] = e['op']
live = [k for k, v in st.items() if v == 1]
print('live edges', len(live), 'adds', sum(e['op'] == 1 for e in E), 'removes', sum(e['op'] == -1 for e in E))
print('targets not in pop', sum(1 for s, t in live if t not in P), [t for s, t in live if t not in P][:10])
print(collections.Counter(r['kind'] for r in R))
print('pop', len(P), collections.Counter(v['status'] for v in P.values()))
print('claims with created event', len({r['claim'] for r in R if r['kind'] == 'created'} & set(P)))
