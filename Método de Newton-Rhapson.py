import numpy as np

def f(x):
    función=(2*x**4)-(3*x**2)+(3*x)-(4)
    return función
def Df(x):
    función=(8*x**3)-(6*x)+(3)
    return función
x=0
x_0=0.5
Tol=1e-16
Max=100
Root_found=False
print("Aproximación de la raíz por Newton-Rhapson")
for i in np.arange(0,Max,1):
    x=x_0-(f(x_0)/Df(x_0))
    if abs(x-x_0)<Tol:
        print("La raiz es %.16f"%x)
        print("Fueron necesarias %d iteraciones"%i)
        Root_found=True
        break
    else:
        x_0=x

if Root_found==False:
    print("No se pudo encontrar la raíz")