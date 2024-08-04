import pandas as pd
import Bee_Adjust as BA
#file = pd.read_csv(r"")#aquí copia la dirección del archivo pdf como una
#raw string
#también puedes llenar las listas manualmente aquí
x=[1.3,1.98,3.5,4.06,4.78,5.6,8.6,8.04,8.99,10.06]#dentro de los paréntesis anota el nombre de las columna x
y=[1.4,4.06,8.7,15.78,26.098,35.6,50.4,63.8,82.1,99.7]#dentro de los paréntesis anota el nombre de la columna y
plottype = "cuadratic" #Si tu función es lineal anota "linear" si es cuadrática
#anota "cuadratic"
a=8#aquí pones el tamaño horizontal de la gráfica
b=5#aquí pones el tamaño vertical de la gráfica
data=["titulo",#aquí pon el titulo
      "x",#auí pon el titulo del eje x
      "y",#aquí pon el titulo del eje y
      "dato",#aquí pon la descripción de los datos que irá en la leyenda
      "tendencia",
      "default"#asigna una palita de colores precondigurada
      ]
"""
Lista de paletas de colores
default
Chocolate-WIP
Beach-WIP
Forest
Ocean-WIP
Volcano-WIP
Summer-WIP
"""
BA.custom_plot(x,y,plottype,a,b,data)