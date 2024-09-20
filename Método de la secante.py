import numpy as np
def f(x):
    función=(np.e**x)-(x**2)
    return función
x_0=-4
x_1=-2
Tol=1e-16
Max=100
q_0=f(x_0)
q_1=f(x_1)
x=x_1-q_1*(x_1-x_0)/(q_1-q_0)
Root_found=False
print("Aproximación de la raíz por método de secante")
for i in np.arange(2,Max,1):
   if q_1-q_0!=0:
       x=x_1-q_1*(x_1-x_0)/(q_1-q_0)
       if abs(x-x_1)<Tol:
           print("La raíz es %.16f"%x)
           print("Fueron necesarias %d iteraciones"%i)
           Root_found=True
           break
   x_0=x_1
   q_0=q_1
   x_1=x
   q_1=f(x)
if Root_found==False:
    print("No se ha encontrado una solución\n tras %d iteraciones"%(i+1))