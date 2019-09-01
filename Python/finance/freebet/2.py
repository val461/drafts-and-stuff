#!/usr/bin/env python3

# comme 1.py, sauf que cote2 n'est plus un paramètre

# input

mise1 = 100
mise2 = 50

s = 1.0432468396540253
cote1 = 2.25

# préliminaires

cote2 = 1/(s-1/cote1)

print()
print(f's {s}')

cote1_min = mise2 / mise1 + 1
print(f'cote1min {cote1_min}')
if cote1 < cote1_min:
    print(f'cote1 devrait valoir au moins {cote1_min} !')


# 1er pari remboursé si perdu
g1 = (cote1 - 1) * mise1
l1 = 0

# 2nd pari non remboursé
g2 = (cote2 - 1) * mise2
l2 = mise2


# si le 1er gagne, le 2nd est perdu

g_cas_1 = g1 - l2

# mise2 = (cote1 - 1) * mise1 - g
# cote1 = (mise2 + g) / mise1 + 1


# si le 2nd gagne, le 1er est perdu

g_cas_2 = g2 - l1

line = 10 * '-'
print()
print(f'cotes {cote1:.2f} {cote2:.2f}')
print(f'mises {mise1:4.0f} {mise2:4.0f}')
print(f'gains {g_cas_1:4.2f} {g_cas_2:4.2f} {g_cas_1+g_cas_2:4.2f} {g_cas_1*g_cas_2:.0f}')
print()

