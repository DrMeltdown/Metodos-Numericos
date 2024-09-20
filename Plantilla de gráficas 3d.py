import matplotlib.pyplot as plt
import numpy as np
#Configura el tamaño de la gráfica
#file = pd.read_excel()
#para excel = file[columna]
fig = plt.figure(dpi=300,figsize=(5,5))
caja = dict(boxstyle='round', facecolor=(0.3,0.3,0.3), alpha=0.5)
ax = plt.axes(projection="3d")
ax.view_init(elev=30, azim=-60, roll=0)#Valores por defecto:
#elev=30, azim=-60, roll=0
ax.set_facecolor("white")
fig.patch.set_facecolor("white")
fig.patch.set_alpha(1)
z = np.arange(0,2,0.0001)
a=3
x = z*np.sin(28*z)
y = z*np.cos(5*z)
plt.rcParams['text.usetex'] = True
plt.grid(color="gray")#Activa la cuadrícula
plt.xlim([-2,2])#límites de x
plt.ylim([-2,2])#límites de y
ax.set_zlim(0,2)
xticks = [i for i in np.arange(-2,2,1)]
yticks = [i for i in np.arange(-2,2,1)]
ax.set_xlabel("$eje\;x$",color="black")
ax.set_ylabel("$eje\;y$",color="black")
ax.set_zlabel("$eje\;z$",color="black")
ax.set_zlabel("eje z")
plt.title("$gr\\acute{a}fica$")
ax.tick_params(axis='x', colors="black")
ax.tick_params(axis='y', colors="black")
# color de los planos
ax.xaxis.pane.fill = True
ax.xaxis.pane.set_facecolor((0.2, 0.8, 0.9, 0.5))  # Color del plano xz (RGBA)
ax.yaxis.pane.fill = True
ax.yaxis.pane.set_facecolor((0.9, 0.8, 0.8, 0.5))  # Color del plano yz (RGBA)
ax.zaxis.pane.fill = True
ax.zaxis.pane.set_facecolor((0.8, 0.9, 0.8, 0.5))  # Color del plano xy (RGBA)

ax.set_zticks(np.arange(0, 3,1))
poblacion = "p_{n}"
ax.plot3D(x, y, z,label="$%s$"%poblacion,color="black")#crea la gráfica
legend = plt.legend(edgecolor=("black"),facecolor=("gray"),fontsize=10,loc='upper right')
for text in legend.get_texts():
    text.set_color("black")  # Cambia 'white' por el color que desees
plt.show()
