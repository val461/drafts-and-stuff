#!/usr/bin/env python3

# Script de peu d'intérêt pour Z/nZ, car ses automorphismes de groupe sont ses bijections "Z-linéaires" (automorphismes de Z-module ?), i.e. les f tq f(z)=f(1)z avec f(1) dans U(Z/nZ).
# Ce script ou sa stratégie générale peuvent néanmoins être adaptés à l'étude d'autres groupes.

import math, itertools

def etude(n):
    '''Détermine les automorphismes de Z/nZ.'''
    print(f'n = {n}\nordres = {ordres(n)}\n')
    Bl, Bf = quasi_isomorphismes(n)
    for bl, bf in zip(Bl,Bf):
        print(list(map(bf, range(n))))
        if not est_morphisme(bf, n):
            print('n\'est pas un isomorphisme.\n')
        else:
            print('est un isomorphisme.\n')


def quasi_isomorphismes(n, plat = True):
    '''Retourne les bijections [[0, n-1]] préservant l'ordre dans Z/nZ.'''
    E = range(n)
    ordre_n = lambda k: ordre(k, n)
    # partitionner [[1, n]] par ordre
    partition = [[k for k in E if ordre_n(k) == o] for o in ordres(n)]
    # obtenir les permutés de chaque classe
    permutes_par_classe = [itertools.permutations(partition[i]) for i in range(len(partition))]
    # produit cartésien des permutés
    produit = itertools.product(*permutes_par_classe)
    # aplatir
    if plat:
        B = [list(itertools.chain.from_iterable(b)) for b in produit]
        def faire_fonction(b):
            '''convertit liste en bijection'''
            return lambda i: b[B[0].index(i)]
        return B, map(faire_fonction, B)
    else:
        return produit


def est_morphisme(f, n, verbose = True):
    '''Vérifie si une application de [[0, n-1]] est un endomorphisme du groupe Z/nZ.'''
    for a, b in itertools.product(range(n), repeat=2):
        if f((a+b) % n) != (f(a)+f(b)) % n:
            if verbose:
                print(f'f({a}+{b}) = {f((a+b) % n)} != {(f(a)+f(b)) % n} = {f(a)}+{f(b)} = f({a})+f({b})')
            return False
    return True

def ordres(n):
    ordre_n = lambda k: ordre(k, n)
    return set(map(ordre_n, range(n)))


def ordre(k, n):
    return n // math.gcd(k,n)


etude(6)
