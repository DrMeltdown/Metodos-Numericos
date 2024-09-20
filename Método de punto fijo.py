import numpy as np
def f(x):
    función=np.sqrt(3)
    return función
def g(x):
    función=(3+x)/(x+1)
    return función
def localizar_punto_fijo(i,p,p_0,punto_encontrado):
    while i<Max:
        p=g(p_0)
        if abs(p-p_0)<Tol:
            print("Iteración número:%d"%i)
            print("Punto fijo encontrado.\n Valor:%.16f"%p)
            punto_encontrado=True
            break
        p_0=p
        i+=1
    if punto_encontrado==False:
        print("No se pudo encontrar un punto fijo.")
        print("Se tomaron %d iteraciones"%i)
    return p
punto_encontrado=False
#Punto fijo:
#///////////////////////
Tol=1e-4
i=1
Max=100
p=0
p_0=1
print("Aproximación de la raíz por ounto fijo")
punto_fijo=localizar_punto_fijo(i,p,p_0,punto_encontrado)
#print("La raiz vale:%f"%raiz)


