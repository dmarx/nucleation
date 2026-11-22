"""Summarize results/runs.jsonl into results/summary.md.

For each arm and gate temperature: mean post-reversal held-out MSE per method
over seeds, and governance against the router, paired by seed (wins, mean
difference, two-sided sign test). Then each method at the temperature it does
best at BEFORE the reversal (chosen on pre-reversal error, never on the
post-reversal window that is scored).
"""
import json
import os
from math import comb

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
rows = [json.loads(l) for l in open(os.path.join(HERE, 'results', 'runs.jsonl'))]
PAIRS = {'scale': [('governance', 'router'), ('governance', 'router_std'), ('governance_raw', 'router')],
         'bandit': [('governance', 'router'), ('governance_explore', 'router_explore')]}


def sign_p(w, n):
    k = min(w, n - w)
    return min(1.0, 2 * sum(comb(n, i) for i in range(k + 1)) / 2 ** n)


def methods_of(r):
    return [m for m in r if isinstance(r[m], dict) and 'post' in r[m]]


out = ['# LEAD-077 results', '',
       'Post-reversal held-out MSE (episodes 42–83), mean over seeds; governance (G) '
       'against router (R) paired by seed. A win is lower error. serve_old: weight '
       'still on each region\'s pre-reversal specialist over the last 10 episodes.', '']
arms = []
for r in rows:
    if r['arm'] not in arms:
        arms.append(r['arm'])
best_lines = ['', '## Each method at its best pre-reversal temperature', '',
              '| arm | pair | tau G | tau R | G pre | R pre | G post | R post | G wins post | p |', '|---|---|---|---|---|---|---|---|---|---|']
for arm in arms:
    ar = [r for r in rows if r['arm'] == arm]
    taus = sorted({r['tau'] for r in ar})
    ms = methods_of(ar[0])
    out += [f'## {arm}', '', '| tau | n | ' + ' | '.join(ms) + ' |', '|---|---|' + '---|' * len(ms)]
    for t in taus:
        rt = [r for r in ar if r['tau'] == t]
        out.append(f'| {t} | {len(rt)} | ' + ' | '.join(
            f"{np.mean([r[m]['post'] for r in rt]):.4f} ({np.mean([r[m]['serve_old_last10'] for r in rt]):.2f})"
            for m in ms) + ' |')
    out.append('')
    for g, ro in PAIRS.get(arm, [('governance', 'router')]):
        for t in taus:
            rt = sorted([r for r in ar if r['tau'] == t], key=lambda r: r['seed'])
            d = np.array([r[g]['post'] - r[ro]['post'] for r in rt])
            w = int(np.sum(d < 0))
            dp = np.array([r[g]['pre'] - r[ro]['pre'] for r in rt])
            out.append(f'- tau {t}: {g} vs {ro}: pre-reversal diff {dp.mean():+.4f} (G wins {int(np.sum(dp < 0))}); post: {g} wins {w}/{len(d)}, mean diff {d.mean():+.4f} '
                       f'(sd {d.std(ddof=1) if len(d) > 1 else 0:.4f}), sign p = {sign_p(w, len(d)):.3g}')
        # best pre-reversal tau per method
        pre = lambda m, t: np.mean([r[m]['pre'] for r in ar if r['tau'] == t])
        tg = min(taus, key=lambda t: pre(g, t)); tr = min(taus, key=lambda t: pre(ro, t))
        G = {r['seed']: r[g]['post'] for r in ar if r['tau'] == tg}
        Rr = {r['seed']: r[ro]['post'] for r in ar if r['tau'] == tr}
        Gp = {r['seed']: r[g]['pre'] for r in ar if r['tau'] == tg}
        Rp = {r['seed']: r[ro]['pre'] for r in ar if r['tau'] == tr}
        seeds = sorted(set(G) & set(Rr))
        d = np.array([G[s] - Rr[s] for s in seeds])
        w = int(np.sum(d < 0))
        best_lines.append(f'| {arm} | {g} vs {ro} | {tg} | {tr} | {np.mean([Gp[s] for s in seeds]):.4f} | {np.mean([Rp[s] for s in seeds]):.4f} | {np.mean([G[s] for s in seeds]):.4f} | '
                          f'{np.mean([Rr[s] for s in seeds]):.4f} | {w}/{len(d)} | {sign_p(w, len(d)):.3g} |')
    out.append('')
open(os.path.join(HERE, 'results', 'summary.md'), 'w').write('\n'.join(out + best_lines) + '\n')
print('\n'.join(out + best_lines))
