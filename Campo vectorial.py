import matplotlib.pyplot as plt
import numpy as np
# Crear una cuadrícula de puntos (X, Y)
x = np.linspace(-10, 10, 30)
y = np.linspace(-10, 10, 30)
X, Y = np.meshgrid(x, y)
fig = plt.figure(dpi=350,figsize=(7,7))
# Definir los componentes del campo vectorial
U = X
V = Y
plt.rcParams['text.usetex'] = True
ax = plt.axes()
ax.tick_params(axis='x', colors="black")
ax.tick_params(axis='y', colors="black")
ax.set_facecolor("white")
fig.patch.set_facecolor((0.7,0.7,0.7))
fig.patch.set_alpha(1)
# Graficar el campo vectorial usando quiver
plt.xlim([-10,10])
plt.ylim([-10,10])
xtiks=[i for i in np.arange(-10,12,2)]
ytiks=[i for i in np.arange(-10,12,2)]
plt.xticks(ytiks)
plt.yticks(xtiks)
plt.quiver(X, Y, U, V,color="black",width=0.005,linewidths=0.9)
plt.title('$Campo\;Vectorial$')
plt.xlabel('$X$')
plt.ylabel('$Y$')
plt.grid(True)
plt.show()
