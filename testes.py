# Arquivo de testes

import RobPy as rp
import numpy as np

R_0_1: np.ndarray = rp.matriz_rotacao_z(30)
R_1_2: np.ndarray = rp.matriz_rotacao_y(250)
R_2_3: np.ndarray = rp.matriz_rotacao_x(70)
R_0_2: np.ndarray = R_1_2 @ R_0_1
R_0_3: np.ndarray = R_2_3 @ R_0_2
R_1_3: np.ndarray = R_2_3 @ R_1_2
R_1_0 = R_0_1.T
R_2_0 = R_0_2.T
R_3_0 = R_0_3.T
R_2_1 = R_1_2.T
R_3_1 = R_1_3.T
R_3_2 = R_2_3.T

print("exer 1")
print("1 a)")
print(R_0_1)

print("1 b)")
print(R_0_2)

print("1 c)")
print(R_0_3)

print("1 d - I)")
print(R_2_0 @ rp.cria_vetor3([3, 0, 1]))

print("1 d - II)")
print(R_1_3 @ rp.cria_vetor3([0, 1, 0]))

print("1 d - III)")
print(R_0_1 @ rp.cria_vetor3([2, 0, 0]))

print("1 d - IV)")
print(R_3_1 @ rp.cria_vetor3([0, 4, -1]))

print("1 d - V)")
print(R_0_2 @ rp.cria_vetor3([-3, 1, 0]))

print("1 d - VI)")
print(R_1_2 @ rp.cria_vetor3([0, 0, -1]))

print("1 d - VII)")
print(R_3_0 @ rp.cria_vetor3([-2, 0, 1]))

print("1 d - VIII)")
print(R_2_0 @ rp.cria_vetor3([3, -1, 1]))

print("1 d - IX)")
print(R_0_3 @ rp.cria_vetor3([4, 1, -1]))

print("1 d - X)")
print(R_2_3 @ rp.cria_vetor3([0, -1, 1]))

print("1 e)")
va = rp.cria_vetor3([4, 0, -2])
vb = rp.cria_vetor3([1, 1, -3])
print("1 e - I)")
mod_va = np.sqrt(np.vdot(va, va))
mod_vb = np.sqrt(np.vdot(vb, vb))
print((180 / np.pi) * np.arccos(np.vdot(va, vb) / (mod_va * mod_vb) ))

print("1 e - II)")
proj_va_vb = ((np.vdot(va, vb) / np.vdot(vb, vb)) * vb)
print(proj_va_vb)

print("1 e - III)")
proj_vb_va = ((np.vdot(vb, va) / np.vdot(va, va)) * va)
print(proj_vb_va)

print("1 e - IV)")
# O warning "code unreachable" abaixo é um bug
va3 = np.cross(np.squeeze(R_2_3 @ va), np.squeeze(vb))
va3b3 = rp.cria_vetor3(va3)
print(va3b3)

print("1 e - V)")
va0b0 = np.vdot(va, vb)
print(va0b0)

print("1 e - VI)")
vab3 = np.cross(np.squeeze(va), (np.squeeze(R_1_3 @ vb)))
vab0 = rp.cria_vetor3(R_3_0 @ vab3)
print(vab0)

print("1 e - VII)")
va1 = (R_2_1 @ va)
va1b1 = va1 + vb
print(va1b1)

print("1 e - VIII)")
mod_va = np.sqrt(np.vdot(va, va))
print(mod_va)

print("1 e - IX)")
va1 = R_3_1 @ va1
mod_va1 = np.sqrt(np.vdot(va1, va1))
print(mod_va1)

print("1 e - X)")
vb_1 = R_2_1 @ vb
va_1 = R_3_1 @ va
vab_1 = np.cross(np.squeeze(va_1), np.squeeze(vb_1))
vab1 = np.vdot(va, vab_1)
print(vab1)

print("exer 2")
print("2 a)")
#garra tem 0.1m de comprimento
dBP = 0.1
vBP = rp.cria_vetor3([dBP, 0, 0])
print(vBP)

print("2 b)")
l1, l2, l3, l4 = 0.8, 0.25, 0.2, 0.2
lt = 0.1
r0a_s = rp.cria_vetor3([0, 0, l1])
rab_s = rp.cria_vetor3([0, l2, 0])
rbc_s = rp.cria_vetor3([0, 0, -l3])
rcd_s = rp.cria_vetor3([0, l4, 0])
rdt_b = rp.cria_vetor3([lt, 0, 0])
R_s_b = rp.matriz_rotacao_z(90)
R_b_s = R_s_b.T
R_s = r0a_s + rab_s + rbc_s + rcd_s
R_sb = R_s_b @ R_s
R_bs = R_b_s @ rdt_b
R_sb_ponta = R_sb + rdt_b
print(R_sb + rdt_b)
print(R_bs + R_s)
#valores diferentes dependendo da ordem das transformações

print("2 c)")
l1, l2, l3, l4 = 0.8, 0.25, 0.2, 0.2
lt = 0.1
w1d = 0  # w1d é o ângulo w1 em graus
w2d = -30  # w2d é o ângulo w2 em graus
w3d = 135  # w3d é o ângulo w3 em graus
R_s_1 = rp.matriz_rotacao_z(w1d)  # Eu gosto de denotar matrizes com letra maiúscula, mas o PEP8 é contra...
R_1_2 = rp.matriz_rotacao_y(w2d)  # Eu gosto de denotar matrizes com letra maiúscula, mas o PEP8 é contra...
R_2_3 = rp.matriz_rotacao_z(w3d)  # Eu gosto de denotar matrizes com letra maiúscula, mas o PEP8 é contra...
R_3_b = rp.matriz_rotacao_x(-90)  # Eu gosto de denotar matrizes com letra maiúscula, mas o PEP8 é contra...
r0a_s = rp.cria_vetor3([0, 0, l1])
rab_1 = rp.cria_vetor3([0, l2, 0])
rbc_2 = rp.cria_vetor3([l3, 0, 0])
rcd_3 = rp.cria_vetor3([l4, 0, 0])
rdt_b = rp.cria_vetor3([lt, 0, 0])
print(r0a_s +
      R_s_1.T @ rab_1 +
      R_s_1.T @ R_1_2.T @ rbc_2 +
      R_s_1.T @ R_1_2.T @ R_2_3.T @ rcd_3 +
      R_s_1.T @ R_1_2.T @ R_2_3.T @ R_3_b.T @ rdt_b)
