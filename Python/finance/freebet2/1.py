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

def g(m1,m2,c2):
    return 100*(-m1+(1-m2)*(1-1/c2))

def h(m1,m2):
    # retourne le c2 minimal.
    return 1/(1 - m1/(1-m2))
#c2 > 1/(1 - m1/(1-m2))

#print(f(16,1.01))
#print(h(0.05,0.05))

_, m1 = f(24,11.5,1.13)
print(h(m1,0.05))
print(g(m1,0.05,1.6))
