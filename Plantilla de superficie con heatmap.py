import matplotlib.pyplot as plt
import numpy as np
import random as rnd

# set up a figure twice as wide as it is tall
fig = plt.figure(dpi=300)

# =============
# First subplot
# =============
# set up the Axes for the first plot
ax = plt.subplot(1,2,1, projection='3d')

# plot a 3D surface like in the example mplot3d/surface3d_demo

# Colores de fondo
ax.view_init(elev=45, azim=-60, roll=0)

# Colores de fondo
ax.set_facecolor((0,0,0.2))
fig.patch.set_facecolor((0,0,0.2))
fig.patch.set_alpha(1)
lima = 10
limb = 10
# Ejemplo de datos para la superficie
X = []
for i in np.arange(0,lima,1):
    for j in np.arange(0,limb,1):
        X.append(i)
Y = []
for i in np.arange(0,lima,1):
    for j in np.arange(0,limb,1):
        Y.append(j)
Z = []
for i in np.arange(0,(lima*limb),1):
    Z.append(i)
for i in np.arange(0,(lima*limb),1):
    Z[i] = rnd.randint(1,10)
x = np.reshape(X, (lima, limb))
y = np.reshape(Y, (lima, limb))
z = np.reshape(Z, (lima, limb))
# Configuración de la gráfica
plt.rcParams['text.usetex'] = True
ax.grid(color="gray")  # Activa la cuadrícula

# Límites de los ejes
ax.set_xlim([0,lima])
ax.set_ylim([0,lima])
ax.set_zlim(0,20)  # Ajuste de límite para z

# Etiquetas y título
ax.set_xlabel("$eje\;x$",color="white")
ax.set_ylabel("$eje\;y$",color="white")
ax.set_zlabel("$eje\;z$",color="white")
ax.set_title("$Custom\;plot$",color="white")

ax.xaxis.pane.fill = True
ax.xaxis.pane.set_facecolor((0.8, 0.4, 0.7))  # Color del plano xz (RGB)
ax.yaxis.pane.fill = True
ax.yaxis.pane.set_facecolor((0.8, 0.4, 0.7))  # Color del plano yz (RGB)
ax.zaxis.pane.fill = True
ax.zaxis.pane.set_facecolor((0.8, 0.4, 0.7))  # Color del plano xy (RGB)
# Ticks de los ejes
xticks = np.arange(0, lima, 10)
yticks = np.arange(0, lima, 10)
zticks = np.arange(0,20,5)
ax.set_xticks(xticks)
ax.set_yticks(yticks)
ax.set_zticks(zticks)

# Color de los ticks
ax.tick_params(axis='x', colors="white")
ax.tick_params(axis='y', colors="white")
ax.tick_params(axis='z', colors="white")

# Crear la superficie 3D
surface = ax.plot_surface(x, y, z, cmap="magma", edgecolor="black")

# Añadir la barra de color

#/////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////
plt.subplot(1,2,2)
ax.set_facecolor((0, 0, 0.2))
a = []
b = []
supa = lima
supb = limb
for i in np.arange(0,supb,1):
    b.append(255)
for i in np.arange(0,supa,1):
    a.append(b)
a=np.array(a)
for i in np.arange(0,supa,1):
    for j in np.arange(0,supb,1):
        a[i][j] = z[i][j]
#plt.axis("off")
fig.patch.set_facecolor((0,0,0.2))
fig.patch.set_alpha(1)
plt.title("$values$",color="white")
plt.rcParams['text.usetex'] = True
plt.imshow(a,cmap="magma")
dbar = plt.colorbar()
plt.tick_params(axis='x', colors="white")
ax.tick_params(axis='both', colors='white')
dbar.ax.yaxis.set_tick_params(color='white')
plt.setp(plt.getp(dbar.ax.axes, 'yticklabels'), color='white')
dbar.set_label('$Altura\;(z)$',color="white")
plt.show()