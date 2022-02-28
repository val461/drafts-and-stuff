#!/usr/bin/env python3

precubes = []

# TO FIX
# pieces_restantes = [
# [(x,y,z,c),
 # (x,y,z,c),
# ],
# [(x,y,z,c),
 # (x,y,z,c),
# ]
# ]

# centre d'une pièce : 1er bloc de sa liste

continuer = True

while pieces_restantes and continuer:
    piece = pop(pieces_restantes) # TO CHECK
    piece_placee = False
    new_precubes = []
    for precube in precubes:
        for emplacement in precube: # TO FIX
            for position in positions(piece): # TO FIX
                if piece fits: # TO FIX
                    # TO DO
                    mettre piece dans precube # TO FIX
                    piece_placee = True
                    new_precubes.append(precube)
                    break
            if piece_placee:
                break
    precubes = new_precubes
