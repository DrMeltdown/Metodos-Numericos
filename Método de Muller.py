import numpy as np
def f(x):
    función=(x**4)-(3*x**3)+(x**2)+(x)+(1)
    return función
p0=0.5
p1=-0.5
p2=0
Tol=1e-8
Max=100
h1=p1-p0
h2=p2-p1
delta1=(f(p1)-f(p0))/(h1)
delta2=(f(p2)-f(p1))/(h2)
d=(delta2-delta1)/(h2+h1)
i=3
Root_Found=False
print("Método de Muller")
while i<=Max:
    b=delta2+(h2*d)
    ArgD=(b**2)-(4*f(p2)*d)
    if ArgD<0:
        D=np.sqrt(abs(ArgD))*1j
    else:
        D=np.sqrt(ArgD)
    if abs(b-D) < abs(b + D):
        E=b+D
    else:
        E=b-D
    h=(-2*f(p2))/(E)
    p=p2+h
    if abs(h) < Tol:
        print("Programa exitoso tras %d iteraciones"%i)
        print("La raiz es %.16f+%.16fi"%(p.real,p.imag))
        Root_Found=True
        break
    else:
        p0=p1
        p1=p2
        p2=p
        h1=p1-p0
        h2=p2-p1
        delta1=(f(p1)-f(p0))/(h1)
        delta2=(f(p2)-f(p1))/(h2)
        d=(delta2-delta1)/(h2+h1)
        i+=1
if Root_Found==False:
    print("La raiz no se encontró tras %d iteraciones"%i)