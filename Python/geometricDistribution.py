#!/usr/bin/env python3

import random

def newTry():
    # how many trials are necessary for a 6 to appear?
    i=1
    while random.randint(1, 6) != 6:
        i+=1
    return i

def newList(n):
    a=[]
    i=0
    while i < n:
        a.append(newTry())
        i=i+1
    return a

def main1(n=1000):
    # show the distribution of the number of trials necessary for a 6 to appear
    l=newList(n)
    u=list(set(l))
    for x in sorted(u, key=l.count, reverse=True):
        print(x,"\t",l.count(x))
    print(len(u),"items")

def p(n):
    return (1/6) * (5/6)**(n-1)

def main2():
    # show that it is more likely that the first 6 appears in one the first four trials than later
    s=0
    i=0
    while s < 1/2:
        i=i+1
        a=p(i)
        s+=a
        print(i,s,"\t",a)
