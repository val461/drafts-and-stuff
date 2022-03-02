#!/usr/bin/env python3

go = False
# TODO : strings de directions : LRUDFB
pieces_seeds = ['']

# TO DO
#   tester parties
#   tester le tout
#   check that Rzx=RyxRzyRxy
#   afficher une solution sur un graphique 3D coloré par pièces.

def iterer(f,n):
    def f_new(x):
        for k in range(n):
            x = f(x)
        return x
    return f_new

def compose(*fs):
    def f_new(x):
        fs.reverse()
        for f in fs:
            x = f(x)
        return x
    return f_new

def add_tuples(U, V):
    return tuple(u + v for (u, v) in zip(U, V))

directions = dict(L=(-1,0,0,0), R=(1,0,0,0), B=(0,-1,0,0), F=(0,1,0,0), D=(0,0,-1,0), U=(0,0,1,0))
def nouvelle_piece(seed, p):
    # seed peut passer plusieurs fois par le même bloc
    piece = {(0,0,0,p)}
    for direction in seed:
        piece.add(add_tuples(piece[-1], directions[direction]))
    return piece

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
    # optimisable en factorisant les rotations_v hors de la boucle des rotations_h
    for rotation_v in rotations_v:
        for rotation_h in rotations_h:
            yield({rotation_h(rotation_v(bloc)) for bloc in piece})


def placer(piece, centre_voulu):
    p = piece[0][3]
    centre_actuel = piece[0][0:3]
    return {[(centre_voulu[k] - centre_actuel[k] + bloc[k]) for k in range(3)] + [p] for bloc in piece}

def contingent(piece, places_prises):
    # check cube boundaries
    for bloc in piece:
        for c in bloc[0:3]:
            if c < 0 or c > 2:
                return False
    # check collisions
    return not intersection(coords(piece), places_prises)

if go:
    pieces_restantes = map(nouvelle_piece, pieces_seeds)
    precubes = [set()]
    while pieces_restantes and precubes:
        print(len(precubes),'précube(s).')
        piece = pieces_restantes.pop()
        new_precubes = []
        for precube in precubes:
            places_prises, places_libres = emplacements(precube)
            for emplacement in places_libres:
                for piece_positionnee in positions(piece):
                    piece_placee = placer(piece_positionnee, emplacement)
                    if contingent(piece_placee, places_prises):
                        new_precubes.append(union(precube, piece_placee))
        precubes = new_precubes
    print(len(precubes),'solution(s).')

    # afficher et trier par pièces la première solution
    print(sorted(precubes[0], key = lambda x: x[3]))
