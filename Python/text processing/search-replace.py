#!/usr/bin/env python3

# Usage:
# py -i search-replace.py

import clipboard

l=[
(r'''q_2''', r'''q'_2'''),
(r'''q'_2^{-1}''', r'''q_1 q_2^{-1}'''),
(r'''q'_2''', r'''q_2 q_1^{-1}'''),
]

ti=r'''|q_0|^{-1}\cdot
\Delta_Q(q_1^{-1})\cdot
\int_{(V\times Q)^2}
\omega(q_0^{-1} q_2,q_1)\cdot
\omega(q_1^{-1} q_2^{-1},q_0)\cdot
\phi(q_2)(v_0)\cdot
(\phi(q_2)-\xi_0)(v_2+v_3-q_2 v_1)\cdot
(\phi(q_3)-\xi_0)(v_4)
\\\text{\hspace{5em}}
f(q_3^{-1}q_0,q_3^{-1}v_2,q_2 q_1,q_2 v_1-v_4)
\,
\dd_V(v_2)
\frac{\dd_Q(q_3)}{|q_3|_V}
\dd_V(v_4)
\frac{\dd_Q(q_2)}{|q_2|_V}'''

# check for possibly unwanted repetitions
n=len(l)
proceed=True
for k in range(n):
    for j in range(k+1,n):
            if l[j][0] in l[k][1]:
                print(f'Repetition:\n{l[j][0]}\nin\n{l[k][1]}.')
                proceed=False
if not proceed:
    if input('Proceed anyway? [n]/y') in ['y','Y']:
        proceed=True
        print('Proceeding.')
    else:
        print('Exiting.')

if proceed:
    to = ti

    for pi, po in l:
        to=to.replace(pi, po)
        # input(f'pi:{pi}, po:{po}, to:{to}. Go on?')

    print(to)

    # if input('copy? [y]/n') not in ['n','N']:
        # clipboard.copy(to)

    clipboard.copy(to)
