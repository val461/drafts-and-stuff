#!/usr/bin/env python3

go = False
precubes = set()

# TO DO
# pieces_restantes = [
# [(x,y,z,0),
 # (x,y,z,0),
# ],
# [(x,y,z,1),
 # (x,y,z,1),
# ]
# ]

# centre d'une pièce : 1er bloc de sa liste

def emplacements_libres(precube): # TO TEST
    emplacements_pris = {(x,y,z) for (x,y,z,p) in precube}
    for x in range(3):
        for y in range(3):
            for z in range(3):
                if (x,y,z) not in emplacements_pris:
                    yield (x,y,z)

def Rxy(bloc):
    (x,y,z,p) = bloc
    return (-y,x,z,p)

def Rzy(bloc):
    (x,y,z,p) = bloc
    return (x,z,-y,p)

def iterer(R,n):
    def iR(bloc):
        for k in range(n):
            bloc = R(bloc)
        return bloc
    return iR

Ryx = iterer(Rxy,3)
Rzy = iterer(Rzy,3)
Rv_xpxm = iterer(Rxy,2)
Rv_ypym = iterer(Rzy,2)


def positions(piece):
    # TO CHECK : Rzx=RyxRzyRxy
    # TO DO
    rotations_v =
    # TO DO
    rotations_h = 
    for rotation_v in rotations_v:
        for rotation_h in rotations_h:
            yield(rotation_v(rotation_h(piece))) # TO FIX

if go:
    while pieces_restantes and precubes:
        piece = pieces_restantes.pop()
        piece_placee = False
        new_precubes = []
        for precube in precubes:
            for emplacement in emplacements_libres(precube):
                for position in positions(piece):
                    if fits(piece, precube):
                        precube |= piece
                        new_precubes.append(precube)
                        piece_placee = True
                        break
                if piece_placee:
                    break
        precubes = new_precubes

    print(len(precubes),'solution(s).')
