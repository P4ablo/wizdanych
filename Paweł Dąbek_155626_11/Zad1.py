import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import pandas as pd

fig = plt.figure()
ax = fig.gca( projection = '3d' )

t = np.linspace( 0 , 2 * np.pi, 100 )
z = t
x = np.sin(t)
y = 2*(np.cos(t))
ax.plot(x, y, z, label = 'zadanie 1' )
ax.legend()
plt.show()