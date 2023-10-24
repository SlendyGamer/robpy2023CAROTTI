# Arquivo de testes

import numpy as np
import RobPy as rp

po1 = rp.cria_vetor3([1, 0, 0])
vs1 = rp.cria_vetor3([0, 1, 0])
po2 = rp.cria_vetor3([0, 0, 1])
vs2 = rp.cria_vetor3([-1, 0, 0])

print(rp.ang_twist_dir_nc_rad(po1, vs1, po2, vs2)* 180 / np.pi)