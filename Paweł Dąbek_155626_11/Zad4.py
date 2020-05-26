import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

kolory=['pink','red','yellow','green','gray','black','orange','brown']
kolory_lista=[kolory[x] for y in range(4) for x in range(0+y,5+y,1)]

fig = plt.figure( figsize =( 8 , 3 ))
ax1 = fig.add_subplot( projection = '3d' )
_x = np.arange( 5 )
_y = np.arange( 4 )
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()
top = (y+x)**(1/2)
bottom = np.zeros_like(top)
width = 0.9
depth = 0.95
ax1.bar3d(x, y, bottom, width, depth, top, color=kolory_lista, shade = True, lightsource=None)
plt.show()