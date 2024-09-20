import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['text.usetex'] = True
caja = dict(boxstyle='round', facecolor=(0.6,0.6,0.6), alpha=1,edgecolor="black")
fig = plt.figure(dpi=350,figsize=(10,10))
x=[i for i in np.arange(0,10,0.01)]
#////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////
ax=plt.subplot(2,2,1)
plt.suptitle("$Plots$",color="black",size=20)
plt.subplots_adjust(top=0.9,hspace=0.25,wspace=0.25)
ax.set_facecolor("white")
fig.patch.set_facecolor("gray")
fig.patch.set_alpha(1)
plt.grid(color="gray")#Activa la cuadrícula
plt.xlim([1,10])#límites de x
plt.ylim([-1,1])#límites de y
xticks = [i for i in np.arange(0,11,1)]
yticks = [i for i in np.arange(-1,1.1,0.5)]
plt.xticks(xticks)
plt.yticks(yticks)
plt.xlabel("$Academia$",size=15)
plt.ylabel("$y$",size=15,rotation=90)
plt.title("$f(x)=sin(x)$",size=15,color="black")
ax.tick_params(axis='x', colors="black")
ax.tick_params(axis='y', colors="black")
plt.plot(x,np.sin(x),color="red",label="$sin(x)$")
legend = plt.legend(edgecolor=("black"),facecolor=("gray"),fontsize=15,loc='lower right')
for text in legend.get_texts():
    text.set_color("black")  # Cambia 'white' por el color que desees
#////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////
plt.subplot(2,2,2)
ax.set_facecolor("white")
fig.patch.set_facecolor("gray")
fig.patch.set_alpha(1)
plt.grid(color="gray")#Activa la cuadrícula
plt.xlim([1,10])#límites de x
plt.ylim([-1,1])#límites de y
xticks = [i for i in np.arange(0,11,1)]
yticks = [i for i in np.arange(-1,1.1,0.5)]
plt.xticks(xticks)
plt.yticks(yticks)
plt.title("$g(x)=cos(x)$",size=15,color="black")
plt.xlabel("$x$",size=15)
plt.ylabel("$g(x)$",size=15,rotation=90)
ax.tick_params(axis='x', colors="black")
ax.tick_params(axis='y', colors="black")
plt.plot(x,np.cos(x),color="purple",label="$cos(x)$")
legend = plt.legend(edgecolor=("black"),facecolor=("gray"),fontsize=15,loc='lower right')
for text in legend.get_texts():
    text.set_color("black")  # Cambia 'white' por el color que desees
#////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////
plt.subplot(2,2,3)
ax.set_facecolor("white")
fig.patch.set_facecolor("gray")
fig.patch.set_alpha(1)
plt.grid(color="gray")#Activa la cuadrícula
plt.xlim([1,10])#límites de x
plt.ylim([-1,1])#límites de y
xticks = [i for i in np.arange(0,11,1)]
yticks = [i for i in np.arange(-1,1.1,0.5)]
plt.xticks(xticks)
plt.yticks(yticks)
plt.xlabel("$x$",size=15)
plt.title("$h(x)=tan(x)$",size=15,color="black")
plt.ylabel("$h(x)$",size=15,rotation=90)
ax.tick_params(axis='x', colors="black")
ax.tick_params(axis='y', colors="black")
plt.plot(x,np.tan(x),color="blue",label="$tan(x)$")
legend = plt.legend(edgecolor=("black"),facecolor=("gray"),fontsize=15,loc='lower right')
for text in legend.get_texts():
    text.set_color("black")  # Cambia 'white' por el color que desees
#////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////
plt.subplot(2,2,4)
ax.set_facecolor("white")
fig.patch.set_facecolor("gray")
fig.patch.set_alpha(1)
plt.grid(color="gray")#Activa la cuadrícula
plt.xlim([1,10])#límites de x
plt.ylim([-3,3])#límites de y
xticks = [i for i in np.arange(0,11,1)]
yticks = [i for i in np.arange(-3,3.1,1.5)]
plt.xticks(xticks)
plt.yticks(yticks)
plt.xlabel("$x$",size=15)
plt.title("$i(x)=sec(x)$",size=15,color="black")
plt.ylabel("$i(x)$",size=15,rotation=90)
ax.tick_params(axis='x', colors="black")
ax.tick_params(axis='y', colors="black")
plt.plot(x,1/np.cos(x),color="green",label="$sec(x)$")
legend = plt.legend(edgecolor=("black"),facecolor=("gray"),fontsize=15,loc='lower right')
for text in legend.get_texts():
    text.set_color("black")  # Cambia 'white' por el color que desees
plt.show()


"""
Linestyles:
    *
    -
    --
    _
    .
    |
"""
#^