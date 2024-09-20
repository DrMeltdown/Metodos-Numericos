import matplotlib.pyplot as plt
import numpy as np

# Configura el tamaño de la gráfica y el DPI
fig = plt.figure(dpi=300)
ax = plt.axes(projection="3d")
# Ajusta la vista inicial
ax.view_init(elev=30, azim=-60, roll=0)

# Colores de fondo
ax.set_facecolor((0,0,0.2))
fig.patch.set_facecolor((0,0,0.2))
fig.patch.set_alpha(1)

# Ejemplo de datos para la superficie
x = np.arange(-100, 100, 10)
y = np.arange(-100, 100, 10)
x, y = np.meshgrid(x, y)
z = x**2 + y**2

# Configuración de la gráfica
plt.rcParams['text.usetex'] = True
"""
La línea de arriba configura el uso de formato LaTeX para
los textos, los cuales se crean usando $$. eliminar esta
línea o dejarla en False en caso no tener LaTeX
"""
ax.grid(color="gray")  # Activa la cuadrícula

# Límites de los ejes
ax.set_xlim([-100, 100])
ax.set_ylim([-150, 100])
ax.set_zlim(0, 10000)  # Ajuste de límite para z

# Etiquetas y título
ax.set_xlabel("$eje\;x$",color="white")
ax.set_ylabel("$eje\;y$",color="white")
ax.set_zlabel("$eje\;z$",color="white")
ax.set_title("$Plot\;of\;the\;function\;z=x^{2}+y^{2}$",color="white")

# Ticks de los ejes
xticks = np.arange(-100, 110, 50)
yticks = np.arange(-150, 110, 50)
zticks = np.arange(0, 10000, 1000)
ax.set_xticks(xticks)
ax.set_yticks(yticks)
ax.set_zticks(zticks)

# Color de los ticks
ax.tick_params(axis='x', colors="white")
ax.tick_params(axis='y', colors="white")
ax.tick_params(axis='z', colors="white")
# color de los planos
ax.xaxis.pane.fill = True
ax.xaxis.pane.set_facecolor((0.8, 0.4, 0.7))  # Color del plano xz (RGB)
ax.yaxis.pane.fill = True
ax.yaxis.pane.set_facecolor((0.8, 0.4, 0.7))  # Color del plano yz (RGB)
ax.zaxis.pane.fill = True
ax.zaxis.pane.set_facecolor((0.8, 0.4, 0.7))  # Color del plano xy (RGB)
# Crear la superficie 3D
surface = ax.plot_surface(x, y, z, cmap="magma", edgecolor="black")

# Añadir la barra de color
cbar = fig.colorbar(surface, ax=ax, shrink=1, aspect=15,pad=0.1)
cbar.set_label('$Altura\;(z)$',color="white")
cbar.ax.yaxis.set_tick_params(color='white')
plt.setp(plt.getp(cbar.ax.axes, 'yticklabels'), color='white')
# Mostrar la gráfica
plt.show()
#////////////////////////////////////
data_x = np.arange(-100, 100, 0.1)
data_y = np.arange(-100, 100, 0.1)
data_x, data_y = np.meshgrid(data_x,data_y)
data_z = data_x**3 +data_y**2

plot2 = plt.figure(dpi=300,figsize=(5,5))

ax = plt.axes()
ax.set_facecolor("white")
plot2.patch.set_facecolor((0,0,0.2))
fig.patch.set_alpha(1)
ax.tick_params(axis='x', colors="white")
ax.tick_params(axis='y', colors="white")

plt.xlabel("$x$",size=12,color="white")
plt.ylabel("$y$",size=12,rotation=90,color="white")
plt.title("$Contorno\;de\;nivel$",size=12,color="white")
plot2 = plt.contourf(data_z,levels=50,cmap="magma")
"""
parámetros de contour()
levels=n
cmap=""
linestyles=""
linewidth=""
"""
plt.show()
#//////////////////////////////////
"""
Estas variables data sirven para crear arreglos de datos 
de la misma función que se gráfica, pero estas variables
no se grafican, por lo que puedes aumentar la cantidad de
puntos almacenados en el objeto de arreglo y así consultar
valores más precisos
"""
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

