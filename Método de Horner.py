import numpy as np
def f(x):
    función=(2*x**4)-(3*x**2)+(3*x)-(4)
    return función
grado=4
x_0=-2
k=1
while k<grado:
    a=[-4,3,-3,0,2]
    y=a[-1]
    z=a[-1]
    for i in np.arange(1,grado,1):
        j=grado-i
#    print("i:%d"%i)
#    print("j:%f"%j)
#    print("Coeff:%f"%a[j])
        y=(x_0*y)+a[j]
#    print("y=%f"%y)
        z=(x_0*z)+y
#    print("z:%f"%z)
    y=(x_0*y)+a[0]
#    print("y:%f,z:%f"%(y,z))
#    print("x_n:%f"%(x_0-(y/z)))
    x_0=x_0-(y/z)
    k+=1
print("x:%f"%x_0)

