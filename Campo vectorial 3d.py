import matplotlib.pyplot as plt
import numpy as np

V=1.3
W=8
# Crear un grid en el espacio 3D
x, y, z = np.meshgrid(np.linspace(-V, V, W), np.linspace(-V, V, W), np.linspace(-V, V, W))
plt.rcParams['text.usetex'] = True
# Definir los componentes del campo vectorial
u = 1/y  # Componente x del campo vectorial
v = np.cos(x)   # Componente y del campo vectorial
w = x+z**2  # Componente z del campo vectorial

# Configura el tamaño de la gráfica y características visuales
fig = plt.figure(dpi=300, figsize=(5, 5))
ax = plt.axes(projection="3d")
ax.view_init(elev=30, azim=-60, roll=0)  # Ajuste de la vista 3D
ax.set_facecolor("white")
fig.patch.set_facecolor("white")
fig.patch.set_alpha(1)

# Configuraciones de los ejes
ax.set_xlabel("$eje\;x$", color="black")
ax.set_ylabel("$eje\;y$", color="black")
ax.set_zlabel("$eje\;z$", color="black")
ax.set_xlim([-1.5, 1.5])
ax.set_ylim([-1.5, 1.5])
ax.set_zlim([-1.5, 1.5])
ax.grid(color="gray")

# Ticks personalizados en los ejes
xticks = np.arange(-1.5, 1.6, 0.5)
yticks = np.arange(-1.5, 1.6, 0.5)
zticks = np.arange(-1.5, 1.6, 0.5)
ax.set_xticks(xticks)
ax.set_yticks(yticks)
ax.set_zticks(zticks)

# Color de los planos
ax.xaxis.pane.fill = True
ax.xaxis.pane.set_facecolor((1, 1, 1, 0))  # Color del plano xz
ax.yaxis.pane.fill = True
ax.yaxis.pane.set_facecolor((1, 1, 1, 0))  # Color del plano yz
ax.zaxis.pane.fill = True
ax.zaxis.pane.set_facecolor((1, 1, 1, 0))  # Color del plano xy

# Graficar el campo vectorial 3D
ax.quiver(x, y, z, u, v, w, length=0.2, normalize=True,color="black", label="$Campo\;Vectorial$",alpha=1)

# Título y leyenda
plt.title("$Campo\;Vectorial\;3D$", fontsize=14)
legend = plt.legend(edgecolor="black", facecolor="gray", fontsize=10, loc='upper right')
for text in legend.get_texts():
    text.set_color("black")

# Mostrar la gráfica
plt.show()
