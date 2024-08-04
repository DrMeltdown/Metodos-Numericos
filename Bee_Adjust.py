import matplotlib.pyplot as plt
import numpy as np

def tendencia_lineal(x,y):
    # Data vectors
    Y = np.array(y)
    X = np.array(x)
    # Plot data
    # Compute the trendline
    coeff = np.polyfit(X, Y, 1)  # 1=linear

    m = coeff[0]
    b = coeff[1]
    
    Xtrend = np.linspace(X[0], X[-1], 100)
    Ytrend = m * Xtrend + b
    x=Xtrend
    y=Ytrend
    
    Y_pred = m * X + b
    ss_res = np.sum((Y - Y_pred) * (Y - Y_pred))
    ss_tot = np.sum((Y - np.mean(Y)) * (Y - np.mean(Y)))
    r_squared = 1 - (ss_res / ss_tot)
   
    return x,y,m,b,r_squared
def tendencia_cuadratica(x,y):
    Y=np.array(y)
    X=np.array(x)
    
    coefficients = np.polyfit(x, y, 2)
    quadratic_function = np.poly1d(coefficients)
    x_fit = np.linspace(min(x), max(x), 100)
    y_fit = quadratic_function(x_fit)
    
    Y_pred = quadratic_function(X)
    
    # Calculate R^2
    ss_res = np.sum((Y - Y_pred) ** 2)
    ss_tot = np.sum((Y - np.mean(Y)) ** 2)
    r_squared = 1 - (ss_res / ss_tot)
    
    a,b,c = coefficients
    return x_fit,y_fit,a,b,c,r_squared

def custom_plot(x,y,plottype,a,b,data):
    backgroundcolor=""
    gridcolor=""
    facecolor=""
    dotcolor=""
    trendcolor=""
    textcolors=""
    if data[5]=="default":
        backgroundcolor="gray"
        gridcolor=(0.2,0.2,0.2)
        facecolor="white"
        dotcolor=".r"
        trendcolor="darkblue"
        textcolors="black"
    elif data[5]=="forest":
        backgroundcolor=(0,0.3,0)
        gridcolor=(0,0.4,0)
        facecolor=(0,0.15,0)
        dotcolor=".g"
        trendcolor="brown"
        textcolors=(0,0.9,0)
    hor = a
    ver = b
    fig = plt.figure(dpi=300,figsize=(hor,ver))
    caja = dict(boxstyle='round', facecolor=(0.6,0.6,0.6), alpha=1,edgecolor="black")
    if plottype=="linear":
        x2,y2,m,b,r_squared=tendencia_lineal(x, y)
    elif plottype=="cuadratic":
        x2,y2,a,b,c,r_squared=tendencia_cuadratica(x, y)
    #para poner texto en una caja, bbox style
    ax = plt.axes()
    
    ax.set_facecolor(facecolor)
    fig.patch.set_facecolor(backgroundcolor)
    fig.patch.set_alpha(1)
    x = np.array(x)
    y = np.array(y)
    #///////////////////////////////////////
    #Suavizar
    #X_Y_Spline = make_interp_spline(x, y)

    # Returns evenly spaced numbers
    # over a specified interval.
    #X_ = np.linspace(x.min(), x.max(), 500)
    #Y_ = X_Y_Spline(X_)
    #///////////////////////////////////////
    plt.grid(color=gridcolor)#Activa la cuadrícula
    minx=x2[0]-(x2[0]*.1)
    maxx=x2[-1]+(x2[-1]*.1)
    miny=y2[0]-(y2[0]*.1)
    many=y2[-1]+(y2[-1]*.1)
    plt.xlim([minx,maxx])#límites de x
    plt.ylim([miny,many])#límites de y
    xticks = [i for i in np.arange(minx,maxx,1)]
    if plottype=="cuadratic":
        yticks = [i for i in np.arange(miny,many,10)]
    elif plottype=="linear":
        yticks = [i for i in np.arange(miny,many,1)]
    if plottype == "linear":
        if b>=0 and m>=0:
            plt.text(x[0]+(x[0]*.1),y[-1]-(y[-1]*.1),"$y=%fx%f$\n$R^{2}=%f$"%(m,b,r_squared),bbox=caja,size=12)
        elif b<0 and m>=0:
            plt.text(x[0]+(x[0]*.1),y[-1]-(y[-1]*.1),"$y=%fx%f$\n$R^{2}=%f$"%(m,b,r_squared),bbox=caja,size=12)
        elif b>0 and m<=0:
            plt.text(x[0]+(x[0]*.1),y[-1]-(y[-1]*.1),"$y=-%fx%f$\n$R^{2}=%f$"%(m,b,r_squared),bbox=caja,size=12)
        elif b<0 and m<=0:
            plt.text(x[0]+(x[0]*.1),y[-1]-(y[-1]*.1),"$y=-%fx%f$\n$R^{2}=%f$"%(m,b,r_squared),bbox=caja,size=12)
    elif plottype=="cuadratic":
        plt.text(x[0]+(x[0]*.1),y[-1]-(y[-1]*.1),"$y=%fx^{2}%fx+%f$\n$R^{2}=%f$"%(a,b,c,r_squared),bbox=caja,size=12)
    plt.xticks(xticks)
    plt.yticks(yticks)
    #plt.annotate("$Estos\;puntos\;son$\n$datos\;experimentales$", xy=(4,20),xytext=(1.5,50),color="black",
    #horizontalalignment="center",
    #arrowprops=dict(arrowstyle='->',lw=1,color="black"),bbox=caja,size=10)
    #Crea una flecha
    plt.xlabel(data[1],size=12,color=textcolors)
    plt.ylabel(data[2],size=12,rotation=90,color=textcolors)
    plt.title(data[0],size=12,color=textcolors)
    ax.tick_params(axis='y', colors=textcolors)
    ax.tick_params(axis='x', colors=textcolors)
    plt.plot(x2,y2,label=data[4],color=trendcolor)
    plt.plot(x,y,dotcolor,label=data[3])#crea la gráfica
    """
    Linestyles:
        *
        -
        --
        _
        .
        |
    """
    legend = plt.legend(edgecolor=("black"),facecolor=("gray"),fontsize=13,loc='lower right')
    for text in legend.get_texts():
        text.set_color("black")  # Cambia 'white' por el color que desees
    #^
    
def equations_bbox(plottype,x,y,xticks,yticks):
    caja = dict(boxstyle='round', facecolor=(0.6,0.6,0.6), alpha=1,edgecolor="black")
    if plottype == "linear":
        x,y,m,b,r_squared=tendencia_lineal(x, y)
        if b>0:
            texto=plt.text(xticks[0]+(xticks[1]*.2),yticks[-1]-(yticks[-1]*.1),"$y=%fx+%f$\n$R^{2}=%f$"%(m,b,r_squared),bbox=caja,size=10)
        else:
            texto=plt.text(xticks[0]+(xticks[1]*.2),yticks[-1]-(yticks[-1]*.1),"$y=%fx%f$\n$R^{2}=%f$"%(m,b,r_squared),bbox=caja,size=10)
    elif plottype=="cuadratic":
        x,y,a,b,c,r_squared=tendencia_lineal(x, y)
        texto=plt.text(x[0]+(x[1]*.2),y[-1]-(y[-1]*.1),"$y=%fx^{2}+%fx+%f$\n$R^{2}=%f$"%(a,b,c,r_squared),bbox=caja,size=10)
    return texto