# Arquivo de testes

import numpy as np
import RobPy as rp

R = rp.matriz_rotacao_y(77*np.pi/180)
r = rp.cria_vetor3([1, 4, -3])

T = rp.cria_operador4(m_rot_b_a=R)

print(T)
print(np.linalg.inv(T))

print(-R.T @ r)