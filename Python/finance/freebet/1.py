#!/usr/bin/env python3

# faire 2 paris contradictoires sur un match à 2 issues incompatibles, dont le premier remboursé si perdu

# input

mise1 = 100
mise2 = 117.14  # à déterminer via 3.m

cote1 = 2.4; cote2 = 1.36
# cote1 = 2.25; cote2 = 1.67
# cote1 = 3.4; cote2 = 1.17
# cote1 = 1.9; cote2 = 1.6

# cote1 = float(input('cote1: ')); cote2 = float(input('cote2: '))

# préliminaires

s = 1/cote1 + 1/cote2
cote1_min = mise2 / mise1 + 1

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

# espérance

p1 = 1/cote1
p2 = 1/cote2
e = g_cas_1 * p1 + g_cas_2 * p2

p1_alt = cote2 / (cote1 + cote2)
p2_alt = cote1 / (cote1 + cote2)
e_alt = p1_alt * g_cas_1 + p2_alt * g_cas_2

abscisse_egalite = g1 / cote2

# output

line = 10 * '-'
print()
print(f's {s}')
print(f'cote1min {cote1_min}')
if cote1 < cote1_min:
    print(f'cote1 devrait valoir au moins {cote1_min} !')
if mise2 > g1:
    print(f'mise2 devrait valoir moins de {g1} !')
print()
print(f'cotes {cote1:.2f} {cote2:.2f}')
print(f'mises {mise1:4.0f} {mise2:4.0f}')
print(f'gains {g_cas_1:4.2f} {g_cas_2:4.2f} {g_cas_1+g_cas_2:4.2f} {g_cas_1*g_cas_2:.0f} {e:4.2f} {e_alt:4.2f}')
print(f'conseils {abscisse_egalite:4.2f} | g_cas_2 / g_cas_1 {cote1 / cote2:4.2f}')
print()

