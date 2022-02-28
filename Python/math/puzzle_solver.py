#!/usr/bin/env python3

go = False
precubes = [set()]

# TO DO
# pieces_restantes = [
# {(x,y,z,0),
 # (x,y,z,0),
# },
# {(x,y,z,1),
 # (x,y,z,1),
# }
# ]

def iterer(f,n):
    def f_new(x):
        for k in range(n):
            x = f(x)
        return x
    return f_new

def compose(*f_s):
    def f_new(x):
        f_s.reverse()
        for f in f_s:
            x = f(x)
        return x
    return f_new

def emplacements_libres(precube): # TO TEST
    emplacements_pris = {(x,y,z) for (x,y,z,p) in precube}
    return {(x,y,z) for x in range(3) for y in range(3) for z in range(3) if (x,y,z) not in emplacements_pris}

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

# TO CHECK : Rzx=RyxRzyRxy
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
    l_coords = [[(centre_voulu[k] - centre_actuel[k] + bloc[k]) for k in range(2)] for bloc in piece]
    return {[(centre_voulu - centre_actuel)]+[bloc[3]] for bloc in piece}
        

def fits(piece, places_libres):
    # check cube boundaries 
    # check collisions 
    # TO DO
    

if go:
    while pieces_restantes and precubes:
        print(len(precubes),'précube(s).')
        piece = pieces_restantes.pop()
        new_precubes = []
        for precube in precubes:
            places_libres = emplacements_libres(precube)
            for emplacement in places_libres:
                for piece_positionnee in positions(piece):
                    piece_placee = placer(piece_positionnee, emplacement)
                    if fits(piece_placee, places_libres):
                        new_precubes.append(union(precube, piece_placee))
        precubes = new_precubes

    print(len(precubes),'solution(s).')
