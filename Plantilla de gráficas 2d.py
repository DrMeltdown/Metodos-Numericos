def funcion_a_trozos():
    y=[]
    for i in np.arange(-10,10,0.01):
        if i < 0:
            y.append(1-i)
        elif i==0:
            y.append(0)
        elif i>0:
            y.append(i-1)
    return y
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#Configura el tamaño de la gráfica
plottype="linear"
file = pd.read_excel(r"C:\Users\carlo\OneDrive\Documentos\Resources\excelplot.xlsx")
plt.rcParams['text.usetex'] = True
a = 8
b = 5
fig = plt.figure(dpi=300,figsize=(a,b))
caja = dict(boxstyle='round', facecolor=(0.6,0.6,0.6), alpha=1,edgecolor="black")
#para poner texto en una caja, bbox style
ax = plt.axes()
ax.set_facecolor((1,1,1))
fig.patch.set_facecolor((0.5,0.5,0.5))
fig.patch.set_alpha(1)
Dom=[i for i in np.arange(-10,10,0.01)]
y=[np.sin(i) for i in Dom]
x=[i for i in Dom]
x = np.array(x)
y = np.array(y)
#///////////////////////////////////////
#Suavizar
#X_Y_Spline = make_interp_spline(x, y)
# Returns evenly spaced numbers
# over a specified interval.
#X_ = np.linspace(x.min(), x.max(), 500)
#Y_ = X_Y_Spline(X_)
#///////////////////////////////////////7
plt.grid(color="gray")#Activa la cuadrícula
plt.xlim([-10,10])#límites de x
plt.ylim([-1.5,1.5])#límites de y
xticks = [i for i in np.arange(-10,11,1)]
yticks = [i for i in np.arange(-1.5,2,.5)]
plt.xticks(xticks)
plt.yticks(yticks)
#plt.annotate("$Recta$", xy=(-5,(2*0.4*np.cos(2*0.4)-(0.4-2)**2)),xytext=(0.1,-2),color="black",
#horizontalalignment="center",
#arrowprops=dict(arrowstyle='->',lw=1,color="black"),bbox=caja,size=12)
#Crea una flecha
#///////////////////////////////////////////////////////////////7
#BA.equations_bbox(plottype,x,y,xticks, yticks)
#rectax,rectay,m,b,r_squared = BA.tendencia_lineal(x, y)
#////////////////////////////////////////////////////////////////7
textos=(0,0,0)
plt.xlabel("$y$",size=12,color=textos)
plt.ylabel("$x$",rotation=90,size=12,color=textos)
plt.title("$Ecuaci\\acute{o}n\;para\;punto\;fijo$",size=12,color=textos)
ax.tick_params(axis='x', colors=textos)
ax.tick_params(axis='y', colors=textos)
#/////////////////////////////////////////////////////////////////7
trendx=[]
trendy=[]
#plt.plot(trendx,trendy,label="$Tendencia$",color="darkblue",ls="--",alpha=0.4)
#plt.errorbar(x, y,yerr=yerr,fmt="o",markersize=1,linewidth=0.5,capsize=4,c="r")
#/////////////////////////////////////////////////////////////////
#plt.plot(x,y,"--",label="$label$",color="darkred")#crea la gráfica
plt.plot(x,y,color=(0,0,0),label="$g(c)$")
"""
Linestyles:
    *
    -
    --
    _
    .
    |
"""
legend = plt.legend(edgecolor=("white"),facecolor=("gray"),fontsize=10,loc='lower right')
for text in legend.get_texts():
    text.set_color("black")  # Cambia 'white' por el color que desees
#^
"""
Pandas date_range frequencies:
    Alias    Description
B        business day frequency
C        custom business day frequency
D        calendar day frequency
W        weekly frequency
M        month end frequency
SM       semi-month end frequency (15th and end of month)
BM       business month end frequency
CBM      custom business month end frequency
MS       month start frequency
SMS      semi-month start frequency (1st and 15th)
BMS      business month start frequency
CBMS     custom business month start frequency
Q        quarter end frequency
BQ       business quarter end frequency
QS       quarter start frequency
BQS      business quarter start frequency
A, Y     year end frequency
BA, BY   business year end frequency
AS, YS   year start frequency
BAS, BYS business year start frequency
BH       business hour frequency
H        hourly frequency
T, min   minutely frequency
S        secondly frequency
L, ms    milliseconds
U, us    microseconds
N        nanoseconds
"""