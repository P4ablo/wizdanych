import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

np.random.seed( 19634822 )

def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin

kolory=['red','green','blue']
markers=['1','2','3']


fig = plt.figure()
ax = fig.add_subplot( projection = '3d' )
n=20
xs = randrange(n, 0 , 100 )
ys = randrange(n, 0 , 100 )
zs = 0
ax.scatter(xs, ys, zs, c ='red', marker ='o')
xs = [0,25,25,80,80]
ys = [0,0,70,70,90]
zs = 0
ax.plot(xs, ys, zs, c ='green')
ax.set_zlim(0 , 1 )

plt.show()