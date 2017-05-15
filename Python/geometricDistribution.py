#!/usr/bin/env python3

import random

def newTry():
    """Return the number of trials necessary for 6 to have appeared."""
    i=1
    while random.randint(1, 6) != 6:
        i+=1
    return i

def newList(n):
    """Repeat n times the experience newTry()."""
    a=[]
    for i in range(n):
        a.append(newTry())
    return a

def main1(n=1000):
    # show the distribution of the number of trials necessary for a 6 to appear
    l=newList(n)
    u=list(set(l))
    for x in sorted(u, key=l.count, reverse=True):
        print(x,"\t",l.count(x))
    print(len(u),"items")

def p(n):
    # probability that n trials are necessary for a 6 to appear
    return (1/6) * (5/6)**(n-1)

def main2():
    # show that it is more likely than not that at least one 6 appears in one the first four trials
    s=0
    i=0
    while s < 1/2:
        i=i+1
        p_i=p(i)
        s+=p_i
        print(i,s,"\t",p_i)
