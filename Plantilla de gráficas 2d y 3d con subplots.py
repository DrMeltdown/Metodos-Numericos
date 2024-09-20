import matplotlib.pyplot as plt
import numpy as np


# set up a figure twice as wide as it is tall
fig = plt.figure(dpi=300,figsize=(10,3))

# =============
# First subplot
# =============
# set up the Axes for the first plot
ax = fig.add_subplot(1, 2, 1, projection='3d')

# plot a 3D surface like in the example mplot3d/surface3d_demo

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
ax.set_title("$Plot\;of\;the\;function\;f(x,y)=x^{2}+y^{2}$",color="white")

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
#/////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////
# set up the Axes for the second plot
x=[i for i in np.arange(-10,10,0.01)]
y=[i**2 for i in np.arange(-10,10,0.01)]
ax = fig.add_subplot(1, 2, 2)
ax.set_facecolor((0.5, 0.1, 0.4))
fig.patch.set_facecolor((0,0,0.2))
fig.patch.set_alpha(1)
plt.grid(color="white")#Activa la cuadrícula
plt.xlim([-10,10])#límites de x
plt.ylim([0,100])#límites de y
xticks = [i for i in np.arange(-10,11,2)]
yticks = [i for i in np.arange(0,110,20)]
plt.xticks(xticks)
plt.yticks(yticks)
plt.xlabel("$x$",size=10,color="white")
plt.title("$x^{2}\;taken\;from\;f(x,y)\;for\;y=0$\n$on\;xz$",size=12,color="white")
ax.tick_params(axis='x', colors="white")
ax.tick_params(axis='y', colors="white")
plt.plot(x,y,color=(1,0.5,0.5),label="$sin(x)$")
legend = plt.legend(edgecolor=("black"),facecolor=("gray"),fontsize=12,loc='lower right')
for text in legend.get_texts():
    text.set_color("white")  # Cambia 'white' por el color que desees

plt.show()