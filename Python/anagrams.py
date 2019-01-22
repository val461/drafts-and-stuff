#!/usr/bin/env python3

import random as r

def fmtcols(mylist, cols):  # based upon a work by gimel
    """Arrange a list of strings into columns."""
    lines = ("\t".join(mylist[i:i+cols]) for i in range(0,len(mylist),cols))
    return '\n'.join(lines)

def p(myList):
    """Print a list of strings into columns."""
    nbCols = 16
    print(fmtcols(myList,nbCols))

def anagrams(inputList):
    """Return a list of the permutations of myList. Inefficient unless myList is short."""
    myList = list(inputList)
    l = len(myList)

    if l <= 1:
        res = myList
    else:
        res = []
        for item in set(myList):
            subword = myList.copy()
            subword.remove(item)
            subanagrams = anagrams(subword)
            for i, word in enumerate(subanagrams):
                subanagrams[i] = item + word
            res.extend(subanagrams)

    return res

def shuffle(string, n = 1):
    """Return a list of n random permutations of a string. May include duplicates."""
    myList = []
    for i in range(0, n):
        myList.append("".join(r.sample(string, len(string))))
    return myList

#p(anagrams(input('word: ')))

#f = lambda x: x[-4:] == 'liev'
#p(filter(f, anagrams('lava')))
#~ f = lambda x: 'lev' in x
#~ p(list(filter(f, shuffle('blopper', 100000))))
#~ p(shuffle('neckofthewoods', 3))
#~ p(anagrams('link'))
