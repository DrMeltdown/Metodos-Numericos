import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
fig = plt.figure(dpi=350)
plt.rcParams['text.usetex'] = True
#plt.axis("off")
caja = dict(boxstyle='round', facecolor=(0.3,0.3,0.3), alpha=1)
fig.patch.set_facecolor("gray")
fig.patch.set_alpha(1)
img_path = r""
img = mpimg.imread(img_path)
imgc = np.copy(img)
lumimg = imgc[:,:,0]
redimage = np.copy(imgc)
blueimage = np.copy(imgc)
greenimage = np.copy(imgc)
redimage[:,:,1]=0
redimage[:,:,2]=0
greenimage[:,:,0]=0
greenimage[:,:,2]=0
blueimage[:,:,0]=0
blueimage[:,:,1]=0
#plt.annotate('$This\;results\;is$\n$interesting$', xy=(300,670),xytext=(850,970),color="black",
#horizontalalignment="center",
#arrowprops=dict(arrowstyle='->',lw=1.5,color="black"),bbox=caja)             
# Para el canal rojo, ponemos a cero los canales verde y azul
#//////////////////////////////////////
plt.title("$Title\;of\;image$")
plt.imshow(lumimg,cmap="viridis")
#file=open(r"C:\Users\carlo\OneDrive\Documentos\Resources\image.txt","a")
#file.write("")
#file.closed
plt.colorbar(shrink=1, aspect=10,pad=0.06)
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