import matplotlib.pyplot as plt
import numpy as np

# set up a figure twice as wide as it is tall
fig = plt.figure(dpi=300,figsize=(9,8))
plt.subplots_adjust(top=0.9,hspace=0.4,wspace=0.05)
# =============
# First subplot
# =============
# set up the Axes for the first plot
ax = fig.add_subplot(2, 2, 1, projection='3d')
ax.view_init(elev=30, azim=-60, roll=0)#Valores por defecto:
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
# ==============
# Second subplot
# ==============
# set up the Axes for the second plot
ax = fig.add_subplot(2, 2, 2, projection='3d')
ax.view_init(elev=30, azim=-60, roll=0)#Valores por defecto:

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
ax.grid(color="gray")  # Activa la cuadrícula

# Límites de los ejes
ax.set_xlim([-100, 100])
ax.set_ylim([-150, 100])
ax.set_zlim(0, 10000)  # Ajuste de límite para z

# Etiquetas y título
ax.set_xlabel("$eje\;x$",color="white")
ax.set_ylabel("$eje\;y$",color="white")
ax.set_zlabel("$eje\;z$",color="white")
ax.set_title("$Plot\;of\;the\;function\;z=x^{2}-y^{2}$",color="white")

# Ticks de los ejes
xticks = np.arange(-100, 110, 75)
yticks = np.arange(-150, 110, 75)
zticks = np.arange(0, 10000, 2500)
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
surface = ax.plot_surface(x, y, z, cmap="viridis", edgecolor="black")

# Añadir la barra de color
cbar = fig.colorbar(surface, ax=ax, shrink=1, aspect=15,pad=0.1)
cbar.set_label('$Altura\;(z)$',color="white")
cbar.ax.yaxis.set_tick_params(color='white')
plt.setp(plt.getp(cbar.ax.axes, 'yticklabels'), color='white')


# =============
# Third subplot
# =============
# set up the Axes for the first plot
ax = fig.add_subplot(2, 2, 3, projection='3d')
ax.view_init(elev=30, azim=-60, roll=0)#Valores por defecto:
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
ax.grid(color="gray")  # Activa la cuadrícula

# Límites de los ejes
ax.set_xlim([-100, 100])
ax.set_ylim([-150, 100])
ax.set_zlim(0, 10000)  # Ajuste de límite para z

# Etiquetas y título
ax.set_xlabel("$eje\;x$",color="white")
ax.set_ylabel("$eje\;y$",color="white")
ax.set_zlabel("$eje\;z$",color="white")
ax.set_title("$Plot\;of\;the\;function\;z=x^{2}-y^{2}$",color="white")

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
surface = ax.plot_surface(x, y, z, cmap="inferno", edgecolor="black")

# Añadir la barra de color
cbar = fig.colorbar(surface, ax=ax, shrink=1, aspect=15,pad=0.1)
cbar.set_label('$Altura\;(z)$',color="white")
cbar.ax.yaxis.set_tick_params(color='white')
plt.setp(plt.getp(cbar.ax.axes, 'yticklabels'), color='white')
# ==============
# Fourth subplot
# ==============
# set up the Axes for the second plot
ax = fig.add_subplot(2, 2, 4, projection='3d')
ax.view_init(elev=30, azim=-60, roll=0)#Valores por defecto:

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
surface = ax.plot_surface(x, y, z, cmap="copper", edgecolor="black")

# Añadir la barra de color
cbar = fig.colorbar(surface, ax=ax, shrink=1, aspect=15,pad=0.1)
cbar.set_label('$Altura\;(z)$',color="white")
cbar.ax.yaxis.set_tick_params(color='white')
plt.setp(plt.getp(cbar.ax.axes, 'yticklabels'), color='white')


plt.show()