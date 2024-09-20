import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['text.usetex'] = True
# Configura el tamaño de la gráfica y el DPI
fig = plt.figure(dpi=300)
ax = plt.axes(projection="3d")

# Ajusta la vista inicial
ax.view_init(elev=30, azim=-60, roll=0)

# Colores de fondo
ax.set_facecolor("white")
fig.patch.set_facecolor("white")
fig.patch.set_alpha(1)
a = 15
b = 15
# Ejemplo de datos para la superficie
X = []
for i in np.arange(0,a,1):
    for j in np.arange(0,b,1):
        X.append(i)
Y = []
for i in np.arange(0,a,1):
    for j in np.arange(0,b,1):
        Y.append(j)
Z = []
for i in np.arange(0,(a*b),1):
    Z.append(i)
for i in np.arange(0,(a*b),1):
    Z[i] = np.random.uniform(1,10)
x = np.reshape(X, (a, b))
y = np.reshape(Y, (a, b))
z = np.reshape(Z, (a, b))
# Configuración de la gráfica
plt.rcParams['text.usetex'] = True
ax.grid(color="gray")  # Activa la cuadrícula

# Límites de los ejes
ax.set_xlim([0,a])
ax.set_ylim([0,a])
ax.set_zlim(0,50)  # Ajuste de límite para z

# Etiquetas y título
ax.set_xlabel("$eje\;x$")
ax.set_ylabel("$eje\;y$")
ax.set_zlabel("$eje\;z$")
ax.set_title("$Custom\;plot$")

ax.xaxis.pane.fill = True
ax.xaxis.pane.set_facecolor((0.8, 0.4, 0.7))  # Color del plano xz (RGB)
ax.yaxis.pane.fill = True
ax.yaxis.pane.set_facecolor((0.8, 0.4, 0.7))  # Color del plano yz (RGB)
ax.zaxis.pane.fill = True
ax.zaxis.pane.set_facecolor((0.8, 0.4, 0.7))  # Color del plano xy (RGB)
# Ticks de los ejes
xticks = np.arange(0, a, 3)
yticks = np.arange(0, a, 3)
zticks = np.arange(0,50,10)
ax.set_xticks(xticks)
ax.set_yticks(yticks)
ax.set_zticks(zticks)

# Color de los ticks
ax.tick_params(axis='x', colors="black")
ax.tick_params(axis='y', colors="black")
ax.tick_params(axis='z', colors="black")

# Crear la superficie 3D
surface = ax.plot_surface(x, y, z, cmap="viridis", edgecolor="black")

# Añadir la barra de color
cbar = fig.colorbar(surface, ax=ax, shrink=1, aspect=15,pad=0.1)
cbar.set_label('$Altura\;(z)$')

# Mostrar la gráfica
plt.show()
"""Perceptualmente Uniformes:
viridis
plasma
inferno
magma
cividis
Secuenciales:
Greys
Purples
Blues
Greens
Oranges
Reds
YlOrBr
YlOrRd
OrRd
PuRd
BuPu
GnBu
PuBu
YlGnBu
PuBuGn
BuGn
YlGn
Divergentes:
PiYG
PRGn
BrBG
PuOr
RdGy
RdBu
RdYlBu
RdYlGn
Spectral
coolwarm
bwr
seismic
Cualitativos:
Pastel1
Pastel2
Paired
Accent
Dark2
Set1
Set2
Set3
tab10
tab20
tab20b
tab20c
Misceláneos:
flag
prism
ocean
gist_earth
terrain
gist_stern
gnuplot
gnuplot2
CMRmap
cubehelix
brg
hsv
gist_rainbow
rainbow
jet
nipy_spectral
gist_ncar"""


