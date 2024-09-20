import numpy as np
def f(x):
    función=(np.e**x)-x**2
    return función

a=-50
b=40
p=0
Max=100
Tolerancia=10e-16
FA=0
FP=0
i=1
root_found=False
print("Buscando raíz de la función ingresada por medio de bisección...")
while i <= Max and root_found==False:
    p=a+((b-a)/2)
    FP=f(p)
    FA=f(a)
    if p==0+Tolerancia or p==0-Tolerancia or (b-a)/2 < Tolerancia:
        print("\nPrograma exitoso")
        print("la raíz vale:%.16f"%p)
        print("Fueron requeridas %d iteraciones para llegar al resultado"%i)
        root_found=True
        break
    else:
        i=i+1
        if FA*FP>0:
            a=p
            FA=FP
        else:
            b=p
if root_found==False:
    print("\nNo se ha logrado encontrar una raíz")
print("Ejecución finalizada")

