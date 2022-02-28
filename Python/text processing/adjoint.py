#!/usr/bin/env python3

# Usage:
# py -i search-replace.py

import clipboard

# un facteur par ligne
ti=r'''
M_{(q_1,q_0) \mapsto \conj{\omega}(q_0^{-1},q_1)}
\Sigma
(1\otimes T_\phi)
(1\otimes\F_V)
M_{(q_0,v_0) \mapsto e^{-i\langle q_0^{\flat}\xi_0,v_0\rangle}}
'''[1:-1]

L=ti.split('\n')
L.reverse()
to = '\n'.join(l+r'^{*}' for l in L) + '\n'
print(to)
clipboard.copy(to)
