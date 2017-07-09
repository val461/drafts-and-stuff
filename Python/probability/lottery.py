#!/usr/bin/env python3

"""
N tickets de couleurs différentes, parmi lesquels on marque n tickets comme gagnants (0<n<N, situation supposée équiprobable, au sens où la probabilité qu'on marque un ticket quelconque comme gagnant est la même pour chaque ticket)
c: coût d'un ticket
g: gain obtenu par ticket gagnant
c*N > g*n
A: le ticket jaune est gagnant
B: le ticket bleu est gagnant
X: mes bénéfices nets si je n'ai acheté que le ticket bleu
Y: mes bénéfices nets si je n'ai acheté le ticket bleu et le ticket jaune
Le problème ayant motivé cet effort, bien que ce programme ne l'ait pas résolu, est de savoir si dans certains cas, acheter plusieurs tickets peut être une meilleure stratégie que l'achat d'un seul ticket.

E(X) = P(A)*g - c (car E(X) = P(A)*(g-c) - c*(1-P(A)) = P(A)*g - c * (P(A)+1-P(A)))
E(Y) = P(A ou bien B)*g + P(A et B)*2g - 2c

P(A et B) = P(A)*P(B|A)
P(A ou bien B) = 1 - P(-A et -B) - P(A et B)
P(-A et -B)=P(-(A ou B))=1-P(A ou B)
P(A ou B)=P(A)+P(B)-P(A et B)

P(A)=P(B)=n/N
P(-A)=(N-n)/N
P(B|A)=(n-1)/(N-1)
P(-B|A)= 1-P(B|A) = 1 - (n-1)/N-1 = 1 + (1-n)/N-1 = (N-1+1-n)/N-1 = (N-n)/N-1
P(B|-A)=n/(N-1)
"""

def E_X(N,n,c,g):
    return p(N,n)*g - c

def E_Y(N,n,c,g):
    return p_A_xor_B(N,n)*g + p_A_et_B(N,n)*2*g - 2*c

def p(N,n):
    return n/N

def p_A_xor_B(N,n):
    return 1 - p_nA_et_nB(N,n) - p_A_et_B(N,n)

def p_A_et_B(N,n):
    return p(N,n)*p(N-1,n-1)

def p_nA_et_nB(N,n):
    return 1-p_A_ou_B(N,n)

def p_A_ou_B(N,n):
    return 2*p(N,n)-p_A_et_B(N,n)

def main():
    global N,n,c,g
    N,n,c,g = 120,20,1,5
    print(E_X(N,n,c,g))
    print(E_Y(N,n,c,g))

main()
