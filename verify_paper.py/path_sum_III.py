# %%
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
#%%
def H(i, j):
    ik = 50
    jk = 50
    sigma = 0.5
    return np.exp(-((np.square(i - ik) + np.square(j - jk)) / 2*sigma**2))



#%%
fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(40, 60, 0.1)
Y = np.arange(40, 60, 0.1)
X, Y = np.meshgrid(X, Y)

ax.plot_surface(X, Y, H(X, Y), rstride=1, cstride=1, cmap='rainbow')
 
plt.draw()
plt.pause(10)
plt.savefig('3D.jpg')
plt.close()



#%%
