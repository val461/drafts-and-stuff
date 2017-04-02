#!/usr/bin/env python3.6

import random as r

def fmtcols(mylist, cols):  # based upon a work by gimel
    lines = ("\t".join(mylist[i:i+cols]) for i in range(0,len(mylist),cols))
    return '\n'.join(lines)

def p(myList):
    nbCols = 16
    print(fmtcols(myList,nbCols))

def anagrams(inputList):
    """Return a list of the permutations of inputList. Inefficient unless inputList is short."""
    inputList = list(inputList)
    l = len(inputList)
    res = []

    if l == 1:
        res = inputList
    elif l >= 2:
        for item in set(inputList):
            subword = inputList.copy()
            subword.remove(item)
            subanagrams = anagrams(subword)
            for i, word in enumerate(subanagrams):
                subanagrams[i] = item + word
            res.extend(subanagrams)

    return res

def shuffle(string, n = 1):
    """Print n (possibly identical) random permutations of a string."""
    myList = []
    for i in range(0, n):
        myList.append("".join(r.sample(string, len(string))))
    return myList

#p(anagrams(input('word: ')))

#f = lambda x: x[-4:] == 'liev'
#p(list(filter(f, anagrams('valentin'))))
