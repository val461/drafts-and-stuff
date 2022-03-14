#!/usr/bin/env python3

# Usage:
# py -i search-replace.py

import clipboard

l=[
# (r'''q_2''', r'''q_2^{-1}'''),
# (r'''q_1''', r'''q_2^{-1}q_1'''),
# (r'''v_2''', r'''-q_2^{-1}v_2'''),
# (r'''v_1''', r'''q_2^{-1}(v_1-v_2)'''),
(r'''q_1''', r'''q'_3'''),
(r'''v_1''', r'''v'_3'''),
(r'''q_3''', r'''q_1'''),
(r'''v_3''', r'''v_1'''),
(r'''q_2''', r'''q'_4'''),
(r'''v_2''', r'''v'_4'''),
(r'''q_4''', r'''q_2'''),
(r'''v_4''', r'''v_2'''),
(r'''q'_''', r'''q_'''),
(r'''v'_''', r'''v_'''),
]

ti=r'''\begin{align*}
&(\Lambda_\omega^* f)(q_1,v_1;q_2,v_2)
\\&=\begin{multlined}[t]
\int_{G\times V}
\frac{
\F_V^*(\omega(q_3^{-1},\phi^{-1}(\bullet)))(v_3)
}{
e^{i\ang{q_3^\flat\xi_0,v_3}}\;
e^{-i\ang{q_3^\flat\xi_0-\xi_0,v_4}}
|q_1^{-1}q_3|_V^{-1/2}\;
}\,
 f((1,v_4)^{-1}(q_1,v_1)
,(q_3,v_3)^{-1}(q_2,v_2))\;
d_G(q_3,v_3)
d_V(v_4)
.\end{multlined}
\end{align*}
'''

# check for possibly unwanted repetitions
n=len(l)
proceed=True
for k in range(n):
    for j in range(k+1,n):
            if l[j][0] in l[k][1]:
                print(f'Repetition:\n{l[j][0]}\nin\n{l[k][1]}.')
                proceed=False
if not proceed:
    if input('Proceed anyway? [n]/y ') in ['y','Y']:
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
