#!/usr/bin/env python3

# go = False
go = True
pieces_seeds = ['BRU','FRU','RFF','LFUDF','DRBB','BDRB']
# optimisable en mettant les 3 pièces de volume 5 avant les 3 pièces de volume 4 dans pieces_seeds

# TO DO
#   tester parties
#   check that Rzx=RyxRzyRxy
#   afficher une solution sur un graphique 3D coloré par pièces.

# 1st successful run: took a few minutes.
# Input: pieces_seeds = ['BRU','FRU','RFF','LFUDF','DRBB','BDRB']
# Output:
# 1 précube(s).
# 96 précube(s).
# 3168 précube(s).
# 18864 précube(s).
# 133056 précube(s).
# 94848 précube(s).
# 1152 solution(s).
# [[1, 2, 0, 0], [0, 2, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [1, 2, 1, 1], [2, 2, 1, 1], [2, 2, 0, 1], [2, 1, 0, 1], [0, 2, 1, 2], [0, 2, 2, 2], [0, 1, 2, 2], [0, 0, 2, 2], [0, 0, 1, 3], [0, 0, 0, 3], [1, 0, 0, 3], [1, 1, 0, 3], [1, 0, 0, 3], [2, 0, 0, 3], [1, 0, 1, 4], [1, 0, 2, 4], [2, 0, 2, 4], [2, 1, 2, 4], [2, 2, 2, 4], [1, 2, 2, 5], [1, 1, 2, 5], [1, 1, 1, 5], [2, 1, 1, 5], [2, 0, 1, 5]]


def iterer(f,n):
    # pourrait être codé à partir de compose() de façon plus élégante ?
    def f_new(x):
        for k in range(n):
            x = f(x)
        return x
    return f_new

def compose(*fs):
    lfs = list(fs)
    lfs.reverse()
    def f_new(x):
        for f in lfs:
            x = f(x)
        return x
    return f_new

def add_tuples(U, V):
    return tuple(u + v for (u, v) in zip(U, V))

directions = dict(L=(-1,0,0,0), R=(1,0,0,0), B=(0,-1,0,0), F=(0,1,0,0), D=(0,0,-1,0), U=(0,0,1,0))
def nouvelle_piece(seed, p):
    # seed peut passer plusieurs fois par le même bloc
    piece = [(0,0,0,p)]
    for direction in seed:
        piece.append(add_tuples(piece[-1], directions[direction]))
    return list(set(piece))

def coords(L):
    return {(x,y,z) for (x,y,z,p) in L}

def emplacements(precube, places_prises = None):
    if not places_prises:
        places_prises = coords(precube)
    places_libres = {(x,y,z) for x in range(3) for y in range(3) for z in range(3) if (x,y,z) not in places_prises}
    return places_prises, places_libres


def R1(bloc):
    return bloc

def Rxy(bloc):
    (x,y,z,p) = bloc
    return (-y,x,z,p)

def Rzy(bloc):
    (x,y,z,p) = bloc
    return (x,z,-y,p)

Ryx = iterer(Rxy,3)
Ryz = iterer(Rzy,3)

rotations_v = [R1,Rzy,iterer(Rzy,2),Ryz,compose(Ryx,Rzy,Rxy),compose(Ryx,Ryz,Rxy)]
rotations_h = [R1,Rxy,iterer(Rxy,2),Ryx]

def positions(piece):
    # optimisable en factorisant rotation_v(bloc) hors de la boucle des rotations_h
    for rotation_v in rotations_v:
        for rotation_h in rotations_h:
            yield([rotation_h(rotation_v(bloc)) for bloc in piece])


def placer(piece, centre_voulu):
    p = piece[0][3]
    centre_actuel = piece[0][0:3]
    return [[(centre_voulu[k] - centre_actuel[k] + bloc[k]) for k in range(3)] + [p] for bloc in piece]

def contingent(piece, places_prises):
    # check cube boundaries
    for bloc in piece:
        for c in bloc[0:3]:
            if c < 0 or c > 2:
                return False
    # check collisions
    return not places_prises.intersection(coords(piece))

if go:
    pieces_restantes = [nouvelle_piece(pieces_seeds[k], k) for k in range(len(pieces_seeds))]
    precubes = [[]]
    while pieces_restantes and precubes:
        print(len(precubes),'précube(s).')
        piece = pieces_restantes.pop()
        new_precubes = []
        for precube in precubes:
            places_prises, places_libres = emplacements(precube)
            # optimisable en n'appliquant pas positions() pour la 1ère pièce (grâce aux symétries du cube)
            for piece_positionnee in positions(piece):
                for emplacement in places_libres:
                    piece_placee = placer(piece_positionnee, emplacement)
                    if contingent(piece_placee, places_prises):
                        new_precubes.append(precube + piece_placee)
        precubes = new_precubes
    print(len(precubes),'solution(s).')

    # afficher et trier par pièces la première solution
    print(sorted(precubes[0], key = lambda x: x[3]))
