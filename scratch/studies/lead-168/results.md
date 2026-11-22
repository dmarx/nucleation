# LEAD-168 results

## A. Fixed policies, every probe enumerated

- probes: 32; first divergence counts: {'None': 31, 'enforcement': 1}
- all_separating_are_x_challenged_adverse_withhold_capable: True
- every_such_probe_separates: True
- no_routine_probe_separates: True
- no_acquiescent_probe_separates: True
- first_stage_of_separation: ['enforcement']

Separating probes (I trace / C trace):

- ('x', 'challenged', 'order', 'executed@1', 'reversed') / ('x', 'challenged', 'order', 'not_executed', 'stands')

## B. Delay variant (order at t=1, deadline 10)

| delay | first divergence | outcome differs |
|---|---|---|
| 0 | enforcement | True |
| 1 | enforcement | False |
| 2 | enforcement | False |
| 3 | enforcement | False |
| 4 | enforcement | False |
| 5 | enforcement | False |
| 6 | enforcement | False |
| 7 | enforcement | False |
| 8 | enforcement | False |
| 9 | enforcement | False |
| 10 | enforcement | True |
| 11 | enforcement | True |
| 12 | enforcement | True |

## C. Anticipation (backward induction on a payoff grid)

- myopic: {'total': 3388, 'first_counts': {'None': 1848, 'enforcement': 1540}, 'share_alike_in_routine_and_parting': 0.45454545454545453}
- reviewer: {'total': 3388, 'first_counts': {'None': 1848, 'ruling': 770, 'enforcement': 770}, 'share_alike_in_routine_and_parting': 0.45454545454545453}
- full: {'total': 3388, 'first_counts': {'None': 1848, 'ruling': 487, 'enforcement': 487, 'action': 566}, 'share_alike_in_routine_and_parting': 0.2874852420306966}
- full-anticipation boundary matches (1-p)g <= pc with g > kw: True over 1620 cases

## D. P(E withheld | not executed) in C (0 in I)

| q_cap | w | P |
|---|---|---|
| 0.5 | 0.05 | 0.0476 |
| 0.5 | 0.2 | 0.1667 |
| 0.5 | 0.5 | 0.3333 |
| 0.8 | 0.05 | 0.1667 |
| 0.8 | 0.2 | 0.4444 |
| 0.8 | 0.5 | 0.6667 |
| 0.95 | 0.05 | 0.4872 |
| 0.95 | 0.2 | 0.7917 |
| 0.95 | 0.5 | 0.9048 |
| 0.99 | 0.05 | 0.8319 |
| 0.99 | 0.2 | 0.9519 |
| 0.99 | 0.5 | 0.9802 |

## E. Structural: F's act depends on E's signal

- I: False; C: True
