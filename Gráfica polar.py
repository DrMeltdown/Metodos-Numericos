import matplotlib.pyplot as plt
import numpy as np
import math as math
#Configura el tamaño de la gráfica
plt.figure(dpi=350)
plt.rcParams['text.usetex'] = True
# setting the axes projection as polar 
plt.axes(projection = 'polar') 
#plt.grid()#Activa la cuadrícula
plt.xlim([0,(2*math.pi)])#límites de x
plt.ylim([0,(2*math.pi)])#límites de y
xticks = []
yticks = []
#plt.xlabel("prueba")
#plt.ylabel("prueba")
plt.title("$prueba$")
for i in np.arange(0,16,3):#Crea los pasos de y
    yticks.append(i)
plt.yticks(yticks) 
r = 5
# creating an array containing the 
# radian values 
rads = np.arange(0, (2 * np.pi), 0.01) 
# plotting the circle 
for rad in rads: 
    plt.polar(pow(np.e,rad), r, 'g.')
plt.show()    