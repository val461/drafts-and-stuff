#!/usr/bin/env python3

def f(*cs):
    '''
    args : cotes, ou liste de cotes
    output : probabilités, fraction de marge
    '''
    if len(cs)==1:
        cs=cs[0]
    ks=[1/c for c in cs]
    t=sum(ks)
    return [k/t for k in ks], 1-1/t

def g(*cs, a=1):
    '''
    input : cotes, montant
    output : espérance pour pari sur probabilité la plus élevée
    '''
    ps, m = f(*cs)
    i = max(range(len(ps)), key = lambda i: ps[i])
    c = cs[i]
    pg = ps[i]
    pl = 1 - pg
    print(ps, m)
    print(f'i={i},c={c},pg={pg},pl={pl}')
    return a*(pg*(c-1) - pl)

#print(f(1.44,5.35,7.2))
'''
a, b : montants
c, d : cotes
ac+bd
-a+(d-1)b
-b+(c-1)a

(d-1)b>a
(c-1)a>b

(d-1)>a/b
(c-1)>b/a

1/(c-1) < a/b < d-1
(ou 1/(d-1) < b/a < c-1)

exemple : c=1.5, d=2.6
c-1=0.5
d-1=1.6
1.6 b > a
0.5 a > b
'''
