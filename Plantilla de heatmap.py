import matplotlib.pyplot as plt
import numpy as np
import random as rnd
fig = plt.figure(dpi=300)
a = []
b = []
t=3
sup = 6
for i in np.arange(0,sup,1):
    b.append(255)
    a.append(b)
a=np.array(a)
for i in np.arange(0,sup,1):
    for j in np.arange(0,sup,1):
        a[i][j] = rnd.randint(0,255)
ax = plt.axes()
#plt.axis("off")
fig.patch.set_facecolor("gray")
fig.patch.set_alpha(1)
plt.title("")
plt.rcParams['text.usetex'] = True
plt.tick_params(axis='both', colors='white')
plt.imshow(a,cmap="magma")
plt.colorbar()
plt.show()