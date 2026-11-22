## C1 frustration, quiet member (CLAIM-631 item 3)
- whole set frustrated: True; minimal non-faces: [['1', '2']]
- outcome: x; unmet and acting there: []
- no member operatively thwarted (no but-for set)

## C2 frustration, unmet acting member, idle
- whole set frustrated: True; minimal non-faces: [['1', '2']]
- outcome: y; unmet and acting there: ['1']
- no member operatively thwarted (no but-for set)

## C3 minimal conflict of 3, responsive rule
- whole set frustrated: True; minimal non-faces: [['0', '1', '2']]
- outcome: r0; unmet and acting there: ['0']
- 0 thwarted; minimal but-for sets: [['1'], ['2']]

## C3' minimal conflict of 5, responsive rule
- whole set frustrated: True; minimal non-faces: [['0', '1', '2', '3', '4']]
- outcome: r0; unmet and acting there: ['0']
- 0 thwarted; minimal but-for sets: [['1'], ['2'], ['3'], ['4']]

## C4 minimal pair inside a larger organization
- whole set frustrated: True; minimal non-faces: [['i', 'j'], ['i', 'k'], ['i', 'l']]
- outcome: y; unmet and acting there: ['i']
- i thwarted; minimal but-for sets: [['j', 'k'], ['j', 'l'], ['k', 'l']]

## C5 thwarting without frustration (authority)
- whole set frustrated: False; minimal non-faces: []
- outcome: y; unmet and acting there: ['1']
- 1 thwarted; minimal but-for sets: [['2']]

## C5' same organization, count-max rule
- whole set frustrated: False; minimal non-faces: []
- outcome: z; unmet and acting there: []
- no member operatively thwarted (no but-for set)

## C6 sentry, static (authority)
- whole set frustrated: False; minimal non-faces: []
- outcome: shelter-blind; unmet and acting there: ['investigator']
- investigator thwarted; minimal but-for sets: [['sentry']]

## C6' sentry, static, count-max rule
- whole set frustrated: False; minimal non-faces: []
- outcome: protect-inspect; unmet and acting there: []
- no member operatively thwarted (no but-for set)

