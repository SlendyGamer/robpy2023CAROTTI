# Arquivo de testes

import numpy as np
import RobPy as rp
import matplotlib.pyplot as plot
from mpl_toolkits.mplot3d.axes3d import Axes3D

a = np.asarray([[1, 2, 3]]).T
b =np.asarray([[4, 5, 6]]).T

fig: plot.Figure = plot.figure()
ax = Axes3D(fig)
fig.add_axes(ax)
rp.plota_vetor3(a, color='m')

plot.show()